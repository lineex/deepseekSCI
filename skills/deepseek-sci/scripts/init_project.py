#!/usr/bin/env python3
"""Initialize a portable DeepSeekSCI research project."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


MODES = (
    "discovery",
    "observational",
    "trial",
    "prediction",
    "diagnostic",
    "review",
    "meta",
    "manuscript",
)

DIRECTORIES = (
    "discovery",
    "protocol",
    "search/raw",
    "search/exports",
    "evidence/screening",
    "evidence/extraction",
    "data/raw",
    "data/intermediate",
    "data/derived",
    "analysis/scripts",
    "analysis/outputs/figure_data",
    "manuscript/drafts",
    "manuscript/tables",
    "manuscript/figures",
    "manuscript/supplement",
    "quality",
    "submission",
    "logs",
    "backups",
)

TEMPLATE_MAP = {
    "project_state.md": "project_state.md",
    "protocol.md": "protocol/protocol.md",
    "sap.md": "protocol/sap.md",
    "candidate_questions.csv": "discovery/candidate_questions.csv",
    "search_log.csv": "search/search_log.csv",
    "evidence_matrix.csv": "evidence/extraction/evidence_matrix.csv",
    "variable_dictionary.csv": "protocol/variable_dictionary.csv",
    "claim_evidence.csv": "manuscript/claim_evidence.csv",
    "submission_manifest.md": "submission/submission_manifest.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a DeepSeekSCI project tree and starter artifacts."
    )
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--mode", choices=MODES, default="discovery")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace starter artifacts after backing up existing files.",
    )
    return parser.parse_args()


def render_template(source: Path, destination: Path, mode: str) -> None:
    text = source.read_text(encoding="utf-8")
    text = text.replace("{{DATE}}", datetime.now().astimezone().isoformat(timespec="seconds"))
    text = text.replace("{{MODE}}", mode)
    destination.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()
    project = args.project_dir.expanduser().resolve()
    template_dir = Path(__file__).resolve().parents[1] / "assets" / "templates"
    if not template_dir.is_dir():
        raise SystemExit(f"Template directory not found: {template_dir}")

    project.mkdir(parents=True, exist_ok=True)
    for relative in DIRECTORIES:
        (project / relative).mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    created: list[str] = []
    skipped: list[str] = []
    backed_up: list[str] = []

    for template_name, relative_destination in TEMPLATE_MAP.items():
        source = template_dir / template_name
        destination = project / relative_destination
        if destination.exists() and not args.force:
            skipped.append(relative_destination)
            continue
        if destination.exists():
            backup = project / "backups" / f"init_{timestamp}" / relative_destination
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(destination, backup)
            backed_up.append(str(backup.relative_to(project)))
        destination.parent.mkdir(parents=True, exist_ok=True)
        render_template(source, destination, args.mode)
        created.append(relative_destination)

    log_path = project / "logs" / "process_log.md"
    if not log_path.exists():
        log_path.write_text("# Process Log\n", encoding="utf-8", newline="\n")
    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(
            f"\n- {datetime.now().astimezone().isoformat(timespec='seconds')}: "
            f"initialized mode={args.mode}; created={len(created)}; "
            f"skipped={len(skipped)}; backed_up={len(backed_up)}.\n"
        )

    print(f"Project: {project}")
    print(f"Mode: {args.mode}")
    print(f"Created or replaced: {len(created)}")
    for item in created:
        print(f"  + {item}")
    if skipped:
        print(f"Preserved existing: {len(skipped)}")
        for item in skipped:
            print(f"  = {item}")
    if backed_up:
        print(f"Backups: {len(backed_up)}")
        for item in backed_up:
            print(f"  < {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
