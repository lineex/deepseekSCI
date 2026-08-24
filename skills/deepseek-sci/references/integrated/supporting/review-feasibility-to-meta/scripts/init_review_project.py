#!/usr/bin/env python3
"""Initialize an idempotent gated evidence-synthesis project."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


DIRECTORIES = [
    "00_governance",
    "01_feasibility",
    "02_protocol",
    "03_search/raw",
    "04_screening",
    "05_fulltext",
    "06_extraction",
    "07_risk_of_bias",
    "08_synthesis",
    "09_manuscript",
    "10_submission",
    "11_audit",
]

TEMPLATES = {
    "feasibility_decision_template.md": "01_feasibility/feasibility_decision.md",
    "pilot_search_log_template.csv": "01_feasibility/pilot_search_log.csv",
    "overlap_map_template.csv": "01_feasibility/overlap_map.csv",
    "protocol_template.md": "02_protocol/protocol.md",
    "analysis_plan_template.md": "02_protocol/analysis_plan.md",
    "search_strategy_draft_template.md": "02_protocol/search_strategy_draft.md",
    "registration_record_template.md": "02_protocol/registration_record.md",
    "amendment_log_template.csv": "02_protocol/amendment_log.csv",
    "search_log_template.csv": "03_search/search_log.csv",
    "dedup_log_template.csv": "03_search/dedup_log.csv",
    "screening_decisions_template.csv": "04_screening/screening_decisions.csv",
    "fulltext_exclusions_template.csv": "04_screening/fulltext_exclusions.csv",
    "prisma_counts_template.csv": "04_screening/prisma_counts.csv",
    "data_extraction_template.csv": "06_extraction/data_extraction.csv",
    "effect_size_inputs_template.csv": "06_extraction/effect_size_inputs.csv",
    "cohort_family_map_template.csv": "06_extraction/cohort_family_map.csv",
    "risk_of_bias_template.csv": "07_risk_of_bias/risk_of_bias.csv",
    "synthesis_decision_template.csv": "08_synthesis/synthesis_decision.csv",
    "protocol_deviations_template.csv": "11_audit/protocol_deviations.csv",
    "reporting_checklist_template.csv": "11_audit/prisma_2020_checklist.csv",
    "citation_verification_template.csv": "11_audit/citation_verification.csv",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--route",
        default="undecided",
        choices=["undecided", "retarget", "narrow", "scoping", "systematic", "systematic-meta"],
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_dir.resolve()
    assets = Path(__file__).resolve().parent.parent / "assets"
    root.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (root / directory).mkdir(parents=True, exist_ok=True)

    state_path = root / "review_state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        print(f"Existing project: {state.get('title', '')}")
    else:
        now = datetime.now(timezone.utc).isoformat()
        state = {
            "schema_version": "1.0",
            "title": args.title,
            "phase": "DISCOVERY",
            "route": args.route,
            "status": "active",
            "created_at": now,
            "updated_at": now,
            "protocol_version": None,
            "registration_id": None,
            "search_last_run": None,
            "notes": [],
        }
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    created = []
    for source_name, target_name in TEMPLATES.items():
        source = assets / source_name
        target = root / target_name
        if not source.exists():
            raise FileNotFoundError(f"Missing bundled template: {source}")
        if not target.exists():
            shutil.copyfile(source, target)
            created.append(target_name)

    print(f"Project: {root}")
    print(f"Phase: {state.get('phase')}")
    print(f"Created templates: {len(created)}")
    for item in created:
        print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

