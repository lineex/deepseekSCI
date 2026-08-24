#!/usr/bin/env python3
"""Audit agreement among confidence intervals, p values and manuscript claims."""

from __future__ import annotations

import csv
from pathlib import Path
import argparse


def boolean(value: str) -> bool | None:
    normalized = (value or "").strip().lower()
    if normalized in {"true", "yes", "1", "significant"}:
        return True
    if normalized in {"false", "no", "0", "not significant", "nonsignificant"}:
        return False
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--alpha", type=float, default=0.05)
    args = parser.parse_args()
    root = args.project_dir.resolve()
    source = root / "08_synthesis/meta_analysis_results.csv"
    report = root / "11_audit/statistical_consistency_report.md"
    if not source.exists():
        print(f"FAIL: missing {source}")
        return 2
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    issues = []
    lines = ["# Statistical consistency audit", "", f"Source: `{source}`", ""]
    for row in rows:
        sid = row.get("synthesis_id", "unknown")
        estimate = float(row["estimate"])
        lower = float(row["ci_lower"])
        upper = float(row["ci_upper"])
        p_value = float(row["p_value"])
        null = float(row.get("null_value") or 0)
        ci_significant = lower > null or upper < null
        p_significant = p_value < args.alpha
        computed = boolean(row.get("computed_significant", ""))
        claimed = boolean(row.get("manuscript_claim_significant", ""))
        local = []
        if not lower <= estimate <= upper:
            local.append("estimate lies outside its confidence interval")
        if ci_significant != p_significant:
            local.append("confidence interval and p value disagree at the prespecified alpha")
        if computed is not None and computed != ci_significant:
            local.append("computed_significant field disagrees with the confidence interval")
        if claimed is None:
            local.append("manuscript significance claim is missing")
        elif claimed != ci_significant:
            local.append("manuscript significance claim disagrees with the confidence interval")
        lines.extend(
            [
                f"## {sid}",
                "",
                f"- Estimate: `{estimate}`",
                f"- 95% CI: `{lower}` to `{upper}`",
                f"- p value: `{p_value}`",
                f"- CI excludes null: `{ci_significant}`",
                f"- Manuscript claims significance: `{claimed}`",
            ]
        )
        if local:
            issues.extend(f"{sid}: {message}" for message in local)
            lines.append("- Status: `FAIL`")
            lines.extend(f"  - {message}" for message in local)
        else:
            lines.append("- Status: `PASS`")
        lines.append("")
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if issues:
        print(f"FAIL: {len(issues)} statistical consistency issue(s)")
        for issue in issues:
            print(f"  - {issue}")
        print(f"Wrote: {report}")
        return 1
    print(f"PASS: {len(rows)} synthesis result(s) are internally consistent")
    print(f"Wrote: {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
