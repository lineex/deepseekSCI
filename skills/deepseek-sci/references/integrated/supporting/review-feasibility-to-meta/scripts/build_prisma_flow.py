#!/usr/bin/env python3
"""Validate PRISMA 2020 counts and render a Mermaid flow diagram."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import argparse


KEYS = [
    "records_databases",
    "records_registers",
    "records_other",
    "duplicates_removed",
    "automation_removed",
    "other_removed_before_screening",
    "records_screened",
    "records_excluded_title_abstract",
    "reports_sought",
    "reports_not_retrieved",
    "reports_assessed",
    "reports_excluded",
    "reports_included",
    "studies_included",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    return parser.parse_args()


def main() -> int:
    root = parse_args().project_dir.resolve()
    source = root / "04_screening/prisma_counts.csv"
    if not source.exists():
        print(f"FAIL: missing {source}")
        return 2
    values = {}
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("key"):
                values[row["key"]] = int(row.get("value") or 0)
    missing = [key for key in KEYS if key not in values]
    if missing:
        print("FAIL: missing PRISMA keys: " + ", ".join(missing))
        return 1

    identified = values["records_databases"] + values["records_registers"] + values["records_other"]
    removed = values["duplicates_removed"] + values["automation_removed"] + values["other_removed_before_screening"]
    checks = [
        (identified - removed, values["records_screened"], "identified minus pre-screen removals"),
        (
            values["records_screened"] - values["records_excluded_title_abstract"],
            values["reports_sought"],
            "screened minus title/abstract exclusions",
        ),
        (values["reports_sought"] - values["reports_not_retrieved"], values["reports_assessed"], "reports assessed"),
        (values["reports_assessed"] - values["reports_excluded"], values["reports_included"], "reports included"),
    ]
    errors = [f"{label}: expected {left}, recorded {right}" for left, right, label in checks if left != right]
    if values["studies_included"] > values["reports_included"]:
        errors.append("studies_included exceeds reports_included")
    if errors:
        print(f"FAIL: {len(errors)} PRISMA arithmetic issue(s)")
        for error in errors:
            print(f"  - {error}")
        return 1

    output_json = root / "04_screening/prisma_counts.json"
    output_mmd = root / "04_screening/prisma_flow.mmd"
    output_json.write_text(json.dumps(values, indent=2) + "\n", encoding="utf-8")
    diagram = f"""flowchart TD
  A[Records from databases: {values['records_databases']}] --> D[Total records identified: {identified}]
  B[Records from registers: {values['records_registers']}] --> D
  C[Records from other sources: {values['records_other']}] --> D
  D --> E[Removed before screening: {removed}]
  D --> F[Records screened: {values['records_screened']}]
  F --> G[Records excluded: {values['records_excluded_title_abstract']}]
  F --> H[Reports sought: {values['reports_sought']}]
  H --> I[Reports not retrieved: {values['reports_not_retrieved']}]
  H --> J[Reports assessed: {values['reports_assessed']}]
  J --> K[Reports excluded with reasons: {values['reports_excluded']}]
  J --> L[Reports included: {values['reports_included']}]
  L --> M[Studies included: {values['studies_included']}]
"""
    output_mmd.write_text(diagram, encoding="utf-8")
    print(f"PASS: wrote {output_json}")
    print(f"PASS: wrote {output_mmd}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

