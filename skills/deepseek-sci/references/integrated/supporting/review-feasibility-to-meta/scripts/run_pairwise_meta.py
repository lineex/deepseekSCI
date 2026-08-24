#!/usr/bin/env python3
"""Run a guarded pairwise meta-analysis from standardized effect inputs."""

from __future__ import annotations

import argparse
import csv
import math
import os
import time
from contextlib import contextmanager
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, stats


SUPPORTED = {"MD", "SMD", "logRR", "logOR", "provided"}


def number(row: dict[str, str], key: str) -> float:
    value = (row.get(key) or "").strip()
    if not value:
        raise ValueError(f"{row.get('effect_id', '?')}: missing {key}")
    return float(value)


def truthy(value: str | None) -> bool:
    return (value or "").strip().lower() not in {"false", "0", "no", "exclude"}


def effect_from_row(row: dict[str, str]) -> tuple[float, float]:
    measure = row["effect_measure"].strip()
    if measure == "provided":
        yi = number(row, "yi")
        sei = number(row, "sei")
        if sei <= 0:
            raise ValueError(f"{row['effect_id']}: sei must be positive")
        return yi, sei * sei

    n1, n2 = number(row, "arm1_n"), number(row, "arm2_n")
    if n1 <= 0 or n2 <= 0:
        raise ValueError(f"{row['effect_id']}: arm sizes must be positive")
    if measure in {"MD", "SMD"}:
        m1, m2 = number(row, "arm1_mean"), number(row, "arm2_mean")
        sd1, sd2 = number(row, "arm1_sd"), number(row, "arm2_sd")
        if sd1 <= 0 or sd2 <= 0:
            raise ValueError(f"{row['effect_id']}: SDs must be positive")
        if measure == "MD":
            return m1 - m2, sd1 * sd1 / n1 + sd2 * sd2 / n2
        df = n1 + n2 - 2
        if df <= 1:
            raise ValueError(f"{row['effect_id']}: insufficient degrees of freedom for SMD")
        pooled_sd = math.sqrt(((n1 - 1) * sd1 * sd1 + (n2 - 1) * sd2 * sd2) / df)
        if pooled_sd == 0:
            raise ValueError(f"{row['effect_id']}: pooled SD is zero")
        d = (m1 - m2) / pooled_sd
        correction = 1 - 3 / (4 * df - 1)
        g = correction * d
        variance = (n1 + n2) / (n1 * n2) + g * g / (2 * df)
        return g, variance

    a, c = number(row, "arm1_events"), number(row, "arm2_events")
    if not (0 <= a <= n1 and 0 <= c <= n2):
        raise ValueError(f"{row['effect_id']}: events must be between zero and arm size")
    b, d = n1 - a, n2 - c
    if a + c == 0 or b + d == 0:
        raise ValueError(f"{row['effect_id']}: double-zero/double-one study has no binary relative effect")
    if min(a, b, c, d) == 0:
        a, b, c, d = a + 0.5, b + 0.5, c + 0.5, d + 0.5
    if measure == "logRR":
        risk1, risk2 = a / (a + b), c / (c + d)
        return math.log(risk1 / risk2), 1 / a - 1 / (a + b) + 1 / c - 1 / (c + d)
    if measure == "logOR":
        return math.log((a * d) / (b * c)), 1 / a + 1 / b + 1 / c + 1 / d
    raise ValueError(f"{row['effect_id']}: unsupported effect measure {measure}")


def reml_tau2(y: np.ndarray, v: np.ndarray) -> float:
    upper = max(float(np.var(y, ddof=1)), float(np.mean(v)), 1e-8) * 1000

    def objective(tau2: float) -> float:
        w = 1.0 / (v + tau2)
        mu = float(np.sum(w * y) / np.sum(w))
        return 0.5 * (float(np.sum(np.log(v + tau2))) + math.log(float(np.sum(w))) + float(np.sum(w * (y - mu) ** 2)))

    result = optimize.minimize_scalar(objective, bounds=(0.0, upper), method="bounded")
    if not result.success:
        raise RuntimeError("REML tau-squared optimization failed")
    return max(float(result.x), 0.0)


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    temporary = path.with_suffix(path.suffix + f".{os.getpid()}.tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


@contextmanager
def exclusive_lock(path: Path, timeout_seconds: float = 30.0):
    """Serialize read-modify-write updates to the shared meta result file."""
    lock_path = path.with_suffix(path.suffix + ".lock")
    deadline = time.monotonic() + timeout_seconds
    descriptor = None
    while descriptor is None:
        try:
            descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(descriptor, f"pid={os.getpid()}\n".encode("ascii"))
        except FileExistsError:
            if lock_path.exists() and time.time() - lock_path.stat().st_mtime > 300:
                lock_path.unlink(missing_ok=True)
                continue
            if time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out waiting for result lock: {lock_path}")
            time.sleep(0.1)
    try:
        yield
    finally:
        if descriptor is not None:
            os.close(descriptor)
        lock_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--synthesis-id", required=True)
    parser.add_argument("--model", choices=["fixed", "random"], default="random")
    parser.add_argument("--ci-method", choices=["normal", "hk"], default="hk")
    parser.add_argument("--alpha", type=float, default=0.05)
    args = parser.parse_args()

    root = args.project_dir.resolve()
    source = root / "06_extraction/effect_size_inputs.csv"
    if not source.exists():
        print(f"FAIL: missing {source}")
        return 2
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [
            row
            for row in csv.DictReader(handle)
            if row.get("synthesis_id") == args.synthesis_id and truthy(row.get("include_in_primary"))
        ]
    if len(rows) < 2:
        print("FAIL: at least two included effects are required")
        return 1

    for field in ["outcome", "event_time", "scale", "effect_measure"]:
        values = {(row.get(field) or "").strip() for row in rows}
        if len(values) != 1 or "" in values:
            print(f"FAIL: synthesis contains inconsistent or missing {field}: {sorted(values)}")
            return 1
    measure = rows[0]["effect_measure"].strip()
    if measure not in SUPPORTED:
        print(f"FAIL: unsupported effect measure {measure}")
        return 1
    families = [(row.get("cohort_family_id") or row.get("study_id") or "").strip() for row in rows]
    duplicates = sorted({value for value in families if value and families.count(value) > 1})
    if duplicates:
        print("FAIL: nonindependent cohort families in primary synthesis: " + ", ".join(duplicates))
        return 1

    study_rows = []
    y_values, v_values = [], []
    for row in rows:
        yi, vi = effect_from_row(row)
        if (row.get("direction_flipped") or "").strip().lower() in {"true", "1", "yes"}:
            yi = -yi
        y_values.append(yi)
        v_values.append(vi)
        study_rows.append(
            {
                "effect_id": row["effect_id"],
                "study_id": row["study_id"],
                "cohort_family_id": row.get("cohort_family_id", ""),
                "study_label": row.get("study_label") or row["study_id"],
                "yi": yi,
                "sei": math.sqrt(vi),
            }
        )
    y = np.asarray(y_values, dtype=float)
    v = np.asarray(v_values, dtype=float)
    k = len(y)
    fixed_w = 1.0 / v
    fixed_mu = float(np.sum(fixed_w * y) / np.sum(fixed_w))
    q = float(np.sum(fixed_w * (y - fixed_mu) ** 2))
    q_p = float(stats.chi2.sf(q, k - 1))
    i2_q = max(0.0, (q - (k - 1)) / q * 100) if q > 0 else 0.0

    tau2 = 0.0 if args.model == "fixed" else reml_tau2(y, v)
    typical_variance = (k - 1) * float(np.sum(fixed_w)) / (
        float(np.sum(fixed_w)) ** 2 - float(np.sum(fixed_w * fixed_w))
    )
    i2_model = 100.0 * tau2 / (tau2 + typical_variance) if tau2 + typical_variance > 0 else 0.0
    h2_model = (tau2 + typical_variance) / typical_variance if typical_variance > 0 else math.nan
    weights = 1.0 / (v + tau2)
    pooled = float(np.sum(weights * y) / np.sum(weights))
    base_se = math.sqrt(1.0 / float(np.sum(weights)))
    if args.ci_method == "hk" and k > 1:
        hk_scale = float(np.sum(weights * (y - pooled) ** 2) / (k - 1))
        pooled_se = math.sqrt(max(hk_scale, 0.0) / float(np.sum(weights)))
        critical = float(stats.t.ppf(1 - args.alpha / 2, k - 1))
        p_value = float(2 * stats.t.sf(abs(pooled / pooled_se), k - 1)) if pooled_se > 0 else 0.0
    else:
        pooled_se = base_se
        critical = float(stats.norm.ppf(1 - args.alpha / 2))
        p_value = float(2 * stats.norm.sf(abs(pooled / pooled_se))) if pooled_se > 0 else 0.0
    lower, upper = pooled - critical * pooled_se, pooled + critical * pooled_se
    if args.model == "random" and k >= 3:
        pred_critical = float(stats.t.ppf(1 - args.alpha / 2, k - 2))
        pred_se = math.sqrt(tau2 + pooled_se * pooled_se)
        pred_lower, pred_upper = pooled - pred_critical * pred_se, pooled + pred_critical * pred_se
    else:
        pred_lower = pred_upper = math.nan

    transform = measure in {"logRR", "logOR"}
    study_fields = ["effect_id", "study_id", "cohort_family_id", "study_label", "yi", "sei", "ci_lower", "ci_upper", "display_effect", "display_lower", "display_upper"]
    for row in study_rows:
        row["ci_lower"] = float(row["yi"]) - 1.96 * float(row["sei"])
        row["ci_upper"] = float(row["yi"]) + 1.96 * float(row["sei"])
        row["display_effect"] = math.exp(float(row["yi"])) if transform else row["yi"]
        row["display_lower"] = math.exp(float(row["ci_lower"])) if transform else row["ci_lower"]
        row["display_upper"] = math.exp(float(row["ci_upper"])) if transform else row["ci_upper"]

    result = {
        "synthesis_id": args.synthesis_id,
        "k": k,
        "model": args.model,
        "ci_method": args.ci_method,
        "effect_measure": measure,
        "estimate": pooled,
        "ci_lower": lower,
        "ci_upper": upper,
        "p_value": p_value,
        "tau2": tau2,
        "q": q,
        "q_p_value": q_p,
        "i2": i2_q,
        "i2_q_based": i2_q,
        "i2_model_based": i2_model,
        "h2_model_based": h2_model,
        "prediction_lower": pred_lower,
        "prediction_upper": pred_upper,
        "null_value": 0.0,
        "computed_significant": str(lower > 0 or upper < 0).lower(),
        "manuscript_claim_significant": "",
        "display_estimate": math.exp(pooled) if transform else pooled,
        "display_lower": math.exp(lower) if transform else lower,
        "display_upper": math.exp(upper) if transform else upper,
        "notes": "Exponentiated display from logarithmic analysis scale." if transform else "Analysis and display scales are identical.",
    }
    output_dir = root / "08_synthesis"
    output_dir.mkdir(parents=True, exist_ok=True)
    study_path = output_dir / f"{args.synthesis_id}_study_effects.csv"
    write_csv(study_path, study_rows, study_fields)

    results_path = output_dir / "meta_analysis_results.csv"
    result_fields = list(result.keys())
    with exclusive_lock(results_path):
        prior = []
        if results_path.exists():
            with results_path.open("r", encoding="utf-8-sig", newline="") as handle:
                prior = [row for row in csv.DictReader(handle) if row.get("synthesis_id") != args.synthesis_id]
        write_csv(results_path, prior + [result], result_fields)

    labels = [row["study_label"] for row in study_rows]
    effects = np.asarray([row["display_effect"] for row in study_rows], dtype=float)
    lows = np.asarray([row["display_lower"] for row in study_rows], dtype=float)
    highs = np.asarray([row["display_upper"] for row in study_rows], dtype=float)
    pooled_display, low_display, high_display = result["display_estimate"], result["display_lower"], result["display_upper"]
    ypos = np.arange(k, 0, -1)
    fig, ax = plt.subplots(figsize=(8, max(3.5, 0.45 * k + 2)))
    ax.errorbar(effects, ypos, xerr=[effects - lows, highs - effects], fmt="s", color="#175676", ecolor="#5d737e", capsize=3)
    ax.errorbar([pooled_display], [0], xerr=[[pooled_display - low_display], [high_display - pooled_display]], fmt="D", color="#b23a48", capsize=4)
    null_display = 1.0 if transform else 0.0
    ax.axvline(null_display, color="#555555", linewidth=1)
    ax.set_yticks(list(ypos) + [0], labels + ["Pooled"])
    if transform:
        ax.set_xscale("log")
    ax.set_xlabel(measure.replace("log", ""))
    ax.set_title(f"{args.synthesis_id}: {args.model}-effects meta-analysis")
    ax.grid(axis="x", color="#dddddd", linewidth=0.6)
    fig.tight_layout()
    forest_path = output_dir / f"{args.synthesis_id}_forest.png"
    fig.savefig(forest_path, dpi=200)
    plt.close(fig)

    print(f"PASS: k={k}, estimate={pooled:.6g}, 95% CI [{lower:.6g}, {upper:.6g}], p={p_value:.6g}")
    print(
        f"Heterogeneity: tau2={tau2:.6g}, Q-based I2={i2_q:.2f}%, "
        f"model-based I2={i2_model:.2f}%, H2={h2_model:.3f}, Q p={q_p:.6g}"
    )
    print(f"Wrote: {results_path}")
    print(f"Wrote: {study_path}")
    print(f"Wrote: {forest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
