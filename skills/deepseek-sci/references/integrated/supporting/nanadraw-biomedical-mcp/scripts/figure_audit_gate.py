#!/usr/bin/env python3
"""Create and validate post-generation biomedical figure audit reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_CATEGORIES = (
    "science",
    "content",
    "geometry",
    "connectors",
    "typography",
    "rendering",
    "technical",
)
SEVERITIES = {"critical", "major", "minor"}
STATUSES = {"pass", "fixed", "open", "not_applicable"}


def report_template(figure_class: str) -> dict[str, Any]:
    checks = []
    prompts = {
        "science": "Verify identities, states, compartments, and causal directions.",
        "content": "Verify every required entity is present and unsupported content is absent.",
        "geometry": "Verify panel alignment, object positions, overlap, scale, and clipping.",
        "connectors": "Verify every arrow, inhibition bar, leader, and endpoint.",
        "typography": "Verify exact live labels, spelling, symbols, and transparent backgrounds.",
        "rendering": "Verify coherent icon grammar, smooth edges, and complete artwork behind text.",
        "technical": "Verify file readability, dimensions, editability, exports, and provenance.",
    }
    for index, category in enumerate(REQUIRED_CATEGORIES, start=1):
        checks.append(
            {
                "id": f"{category}-{index:02d}",
                "category": category,
                "severity": "major",
                "status": "open",
                "region": "global",
                "finding": prompts[category],
                "correction": "",
                "evidence": "",
            }
        )
    return {
        "figure": {
            "id": "",
            "figure_class": figure_class,
            "editable_artifact": "",
            "reviewed_render": "",
            "spec_or_brief": "",
            "reference": "",
        },
        "checks": checks,
        "scientific_explanation": {
            "title": "",
            "take_home_message": "",
            "panel_explanations": [],
            "causal_chain": [],
            "arrow_grammar": {},
            "scope_notes": [],
            "claim_basis": [],
        },
    }


def nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def evaluate(report: dict[str, Any], require_mechanism_explanation: bool = False) -> dict[str, Any]:
    errors: list[str] = []
    open_issues: list[str] = []
    categories_seen: set[str] = set()

    figure = report.get("figure")
    if not isinstance(figure, dict):
        errors.append("figure must be an object")
        figure = {}
    for field in ("figure_class", "editable_artifact", "reviewed_render", "spec_or_brief"):
        if not nonempty_text(figure.get(field)):
            errors.append(f"figure.{field} is required")

    checks = report.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("checks must be a non-empty list")
        checks = []
    seen_ids: set[str] = set()
    for index, row in enumerate(checks, start=1):
        prefix = f"checks[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{prefix} must be an object")
            continue
        check_id = str(row.get("id", "")).strip()
        if not check_id:
            errors.append(f"{prefix}.id is required")
        elif check_id in seen_ids:
            errors.append(f"duplicate check id: {check_id}")
        seen_ids.add(check_id)
        category = str(row.get("category", "")).strip()
        if category not in REQUIRED_CATEGORIES:
            errors.append(f"{prefix}.category is invalid: {category}")
        else:
            categories_seen.add(category)
        severity = str(row.get("severity", "")).strip()
        status = str(row.get("status", "")).strip()
        if severity not in SEVERITIES:
            errors.append(f"{prefix}.severity is invalid: {severity}")
        if status not in STATUSES:
            errors.append(f"{prefix}.status is invalid: {status}")
        if not nonempty_text(row.get("finding")):
            errors.append(f"{prefix}.finding is required")
        if status == "open":
            open_issues.append(check_id or prefix)
        if status == "fixed" and not nonempty_text(row.get("correction")):
            errors.append(f"{prefix}.correction is required when status=fixed")
        if status in {"pass", "fixed", "not_applicable"} and not nonempty_text(row.get("evidence")):
            errors.append(f"{prefix}.evidence is required when status={status}")

    missing = sorted(set(REQUIRED_CATEGORIES) - categories_seen)
    if missing:
        errors.append("missing audit categories: " + ", ".join(missing))
    if open_issues:
        errors.append("open issues remain: " + ", ".join(open_issues))

    explanation = report.get("scientific_explanation")
    if not isinstance(explanation, dict):
        errors.append("scientific_explanation must be an object")
        explanation = {}
    for field in ("title", "take_home_message"):
        if not nonempty_text(explanation.get(field)):
            errors.append(f"scientific_explanation.{field} is required")
    panels = explanation.get("panel_explanations")
    if not isinstance(panels, list) or not panels:
        errors.append("scientific_explanation.panel_explanations must be non-empty")
    claims = explanation.get("claim_basis")
    if not isinstance(claims, list) or not claims:
        errors.append("scientific_explanation.claim_basis must be non-empty")

    figure_class = str(figure.get("figure_class", ""))
    mechanism_required = require_mechanism_explanation or figure_class in {"mechanism_pathway", "graphical_abstract"}
    if mechanism_required:
        chain = explanation.get("causal_chain")
        grammar = explanation.get("arrow_grammar")
        if not isinstance(chain, list) or len(chain) < 2 or not all(nonempty_text(item) for item in chain):
            errors.append("scientific_explanation.causal_chain requires at least two steps")
        if not isinstance(grammar, dict) or not grammar or not all(nonempty_text(value) for value in grammar.values()):
            errors.append("scientific_explanation.arrow_grammar must describe the connector semantics")

    return {
        "valid": not errors,
        "errors": errors,
        "open_issues": open_issues,
        "categories_seen": sorted(categories_seen),
        "check_count": len(checks),
        "figure_class": figure_class,
    }


def command_template(args: argparse.Namespace) -> int:
    payload = report_template(args.figure_class)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "figure_class": args.figure_class}))
    return 0


def command_check(args: argparse.Namespace) -> int:
    payload = json.loads(args.report.read_text(encoding="utf-8"))
    result = evaluate(payload, require_mechanism_explanation=args.require_mechanism_explanation)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["valid"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    template = subparsers.add_parser("template", help="Create an open audit report template")
    template.add_argument("--figure-class", default="mechanism_pathway")
    template.add_argument("--output", type=Path, required=True)
    template.set_defaults(func=command_template)
    check = subparsers.add_parser("check", help="Validate a completed audit report")
    check.add_argument("--report", type=Path, required=True)
    check.add_argument("--require-mechanism-explanation", action="store_true")
    check.set_defaults(func=command_check)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

