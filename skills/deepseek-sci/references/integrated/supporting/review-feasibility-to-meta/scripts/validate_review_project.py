#!/usr/bin/env python3
"""Validate phase artifacts and optionally advance review_state.json."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


PHASES = [
    "DISCOVERY",
    "FEASIBILITY",
    "ROUTE_LOCKED",
    "PROTOCOL_LOCKED",
    "REGISTERED",
    "SEARCHED",
    "SCREENED",
    "EXTRACTED",
    "APPRAISED",
    "SYNTHESIZED",
    "DRAFTED",
    "AUDITED",
    "SUBMISSION_READY",
]

REQUIRED_FILES = {
    "ROUTE_LOCKED": [
        "01_feasibility/feasibility_decision.md",
        "01_feasibility/pilot_search_log.csv",
        "01_feasibility/overlap_map.csv",
    ],
    "PROTOCOL_LOCKED": [
        "02_protocol/protocol.md",
        "02_protocol/analysis_plan.md",
        "02_protocol/search_strategy_draft.md",
        "02_protocol/protocol_snapshot.sha256",
    ],
    "REGISTERED": [
        "02_protocol/registration_record.md",
        "02_protocol/amendment_log.csv",
    ],
    "SEARCHED": [
        "03_search/search_log.csv",
        "03_search/dedup_log.csv",
        "03_search/deduplicated_master.csv",
    ],
    "SCREENED": [
        "04_screening/screening_decisions.csv",
        "04_screening/fulltext_exclusions.csv",
        "04_screening/prisma_counts.json",
        "04_screening/prisma_flow.mmd",
        "06_extraction/cohort_family_map.csv",
    ],
    "EXTRACTED": [
        "06_extraction/data_extraction.csv",
        "06_extraction/effect_size_inputs.csv",
    ],
    "APPRAISED": ["07_risk_of_bias/risk_of_bias.csv"],
    "SYNTHESIZED": [
        "08_synthesis/synthesis_decision.csv",
        "08_synthesis/results_summary.md",
    ],
    "DRAFTED": ["09_manuscript/manuscript.md"],
    "AUDITED": [
        "11_audit/protocol_deviations.csv",
        "11_audit/prisma_2020_checklist.csv",
        "11_audit/citation_verification.csv",
        "11_audit/statistical_consistency_report.md",
    ],
    "SUBMISSION_READY": [
        "10_submission/cover_letter.md",
        "10_submission/data_code_availability.md",
    ],
}

CSV_HEADERS = {
    "01_feasibility/pilot_search_log.csv": ["source", "query", "run_date", "raw_count"],
    "01_feasibility/overlap_map.csv": ["review_id", "title", "overlap_decision"],
    "02_protocol/amendment_log.csv": ["amendment_id", "date", "change"],
    "03_search/search_log.csv": ["source", "query", "run_date", "raw_count"],
    "03_search/dedup_log.csv": ["step", "records_before", "records_after"],
    "04_screening/screening_decisions.csv": ["record_id", "stage", "final_decision"],
    "04_screening/fulltext_exclusions.csv": ["report_id", "primary_reason"],
    "06_extraction/cohort_family_map.csv": ["report_id", "cohort_family_id"],
    "06_extraction/data_extraction.csv": ["report_id", "study_id", "outcome", "event_time"],
    "06_extraction/effect_size_inputs.csv": ["effect_id", "study_id", "outcome", "effect_measure"],
    "07_risk_of_bias/risk_of_bias.csv": ["result_id", "tool", "overall_judgement"],
    "08_synthesis/synthesis_decision.csv": ["synthesis_id", "estimand", "pool_decision"],
    "11_audit/protocol_deviations.csv": ["deviation_id", "protocol_item", "actual_method"],
    "11_audit/prisma_2020_checklist.csv": ["item", "status", "location"],
    "11_audit/citation_verification.csv": ["citation_id", "identifier", "verification_status"],
}

CSV_ALLOW_HEADER_ONLY = {
    "02_protocol/amendment_log.csv",
    "04_screening/fulltext_exclusions.csv",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--target-phase", required=True, choices=PHASES)
    parser.add_argument("--advance", action="store_true")
    return parser.parse_args()


def read_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return next(csv.reader(handle), [])


def data_row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return max(sum(1 for _ in csv.reader(handle)) - 1, 0)


def main() -> int:
    args = parse_args()
    root = args.project_dir.resolve()
    state_path = root / "review_state.json"
    if not state_path.exists():
        print("FAIL: review_state.json is missing")
        return 2
    state = json.loads(state_path.read_text(encoding="utf-8"))
    target_index = PHASES.index(args.target_phase)
    errors = []

    for phase in PHASES[: target_index + 1]:
        for relative in REQUIRED_FILES.get(phase, []):
            path = root / relative
            if not path.exists() or path.stat().st_size == 0:
                errors.append(f"missing or empty: {relative}")
            elif path.suffix.lower() == ".md" and "[REQUIRED]" in path.read_text(encoding="utf-8"):
                errors.append(f"unresolved required field: {relative}")

    for relative, expected in CSV_HEADERS.items():
        path = root / relative
        if path.exists() and PHASES.index(args.target_phase) >= min(
            [PHASES.index(p) for p, files in REQUIRED_FILES.items() if relative in files] or [0]
        ):
            header = read_header(path)
            missing = [name for name in expected if name not in header]
            if missing:
                errors.append(f"CSV header {relative} missing: {', '.join(missing)}")
            if relative not in CSV_ALLOW_HEADER_ONLY and data_row_count(path) == 0:
                errors.append(f"CSV has no data rows: {relative}")

    if args.target_phase == "ROUTE_LOCKED" and state.get("route") == "undecided":
        errors.append("review_state.json route is still undecided")

    if args.target_phase == "SYNTHESIZED" and state.get("route") == "systematic-meta":
        meta_path = root / "08_synthesis/meta_analysis_results.csv"
        if not meta_path.exists() or meta_path.stat().st_size == 0:
            errors.append("systematic-meta route requires 08_synthesis/meta_analysis_results.csv")

    if target_index >= PHASES.index("SEARCHED"):
        raw_dir = root / "03_search/raw"
        if not raw_dir.exists() or not any(path.is_file() for path in raw_dir.rglob("*")):
            errors.append("03_search/raw contains no preserved raw export")

    if errors:
        print(f"FAIL: {len(errors)} validation issue(s)")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"PASS: project satisfies {args.target_phase}")
    if args.advance:
        current = state.get("phase", "DISCOVERY")
        current_index = PHASES.index(current)
        if target_index != current_index + 1:
            print(f"FAIL: --advance requires the next phase after {current}, not {args.target_phase}")
            return 3
        state["phase"] = args.target_phase
        state["updated_at"] = datetime.now(timezone.utc).isoformat()
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"ADVANCED: {current} -> {args.target_phase}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
