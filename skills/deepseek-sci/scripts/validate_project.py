#!/usr/bin/env python3
"""Validate DeepSeekSCI stage artifacts and unresolved placeholders."""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


STAGES = (
    "intake",
    "discovery",
    "protocol",
    "retrieval",
    "analysis",
    "manuscript",
    "review",
    "submission",
    "all",
)

TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json", ".yaml", ".yml", ".tex", ".py"}
PLACEHOLDER_PATTERN = re.compile(
    r"\{\{[^{}]+\}\}|\[(?:TO COMPLETE|TODO|VERIFY|DATA CHECK|CITATION NEEDED)\]|\bTBD\b",
    re.IGNORECASE,
)


@dataclass
class Issue:
    severity: str
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a DeepSeekSCI project stage.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--stage", choices=STAGES, default="all")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument(
        "--report",
        type=Path,
        help="JSON report path; defaults to PROJECT_DIR/quality/validation_report.json",
    )
    return parser.parse_args()


def is_nonempty(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def csv_has_data(path: Path) -> bool:
    if not is_nonempty(path):
        return False
    for encoding in ("utf-8-sig", "utf-16", "gb18030", "cp1252"):
        try:
            with path.open("r", encoding=encoding, newline="") as handle:
                reader = csv.reader(handle)
                next(reader, None)
                return next(reader, None) is not None
        except UnicodeError:
            continue
    return False


def add_required_file(
    project: Path,
    relative: str,
    issues: list[Issue],
    require_csv_data: bool = False,
) -> None:
    path = project / relative
    valid = csv_has_data(path) if require_csv_data else is_nonempty(path)
    if not valid:
        detail = "missing or has no data rows" if require_csv_data else "missing or empty"
        issues.append(Issue("error", "required_artifact", relative, detail))


def matching_nonempty_files(project: Path, relative_dir: str, suffixes: set[str] | None = None) -> list[Path]:
    root = project / relative_dir
    if not root.is_dir():
        return []
    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.stat().st_size > 0
        and (suffixes is None or path.suffix.casefold() in suffixes)
    ]


def add_any_file(
    project: Path,
    relative_dir: str,
    issues: list[Issue],
    label: str,
    suffixes: set[str] | None = None,
) -> None:
    if not matching_nonempty_files(project, relative_dir, suffixes):
        issues.append(Issue("error", "required_artifact_group", relative_dir, f"no {label} found"))


def validate_stage(project: Path, stage: str, issues: list[Issue], strict: bool) -> None:
    requested = set(STAGES[:-1]) if stage == "all" else {stage}
    add_required_file(project, "project_state.md", issues)

    if "discovery" in requested:
        add_required_file(project, "discovery/topic_brief.md", issues)
        add_required_file(project, "discovery/feasibility_report.md", issues)
        add_required_file(project, "discovery/candidate_questions.csv", issues, True)

    if "protocol" in requested:
        add_required_file(project, "protocol/protocol.md", issues)
        add_required_file(project, "protocol/sap.md", issues)
        add_required_file(project, "protocol/variable_dictionary.csv", issues, True)

    if "retrieval" in requested:
        search_ready = csv_has_data(project / "search/search_log.csv")
        data_ready = bool(matching_nonempty_files(project, "data/derived"))
        evidence_ready = csv_has_data(project / "evidence/deduplicated_records.csv")
        if not (search_ready or data_ready or evidence_ready):
            issues.append(
                Issue(
                    "error",
                    "acquisition_artifact",
                    "search/ or data/derived/ or evidence/",
                    "no completed search log, derived dataset, or deduplicated evidence file found",
                )
            )

    if "analysis" in requested:
        add_required_file(project, "analysis/run_manifest.json", issues)
        add_any_file(project, "analysis/outputs", issues, "analysis output")
        result_files = [
            path
            for path in matching_nonempty_files(project, "analysis/outputs")
            if any(
                token in path.name.casefold()
                for token in ("primary", "effect", "meta_result", "model_performance", "diagnostic")
            )
        ]
        if not result_files:
            issues.append(
                Issue(
                    "error" if strict else "warning",
                    "primary_result",
                    "analysis/outputs/",
                    "no clearly named primary effect/model/meta-analysis result found",
                )
            )

    if "manuscript" in requested:
        add_any_file(project, "manuscript/drafts", issues, "manuscript draft", {".md", ".docx", ".tex"})
        add_required_file(project, "manuscript/claim_evidence.csv", issues, True)

    if "review" in requested:
        add_required_file(project, "quality/internal_review.md", issues)
        add_required_file(project, "quality/traceability_report.md", issues)

    if "submission" in requested:
        add_required_file(project, "submission/submission_manifest.md", issues)
        add_required_file(project, "manuscript/claim_evidence.csv", issues, True)
        add_required_file(project, "quality/internal_review.md", issues)
        add_required_file(project, "quality/traceability_report.md", issues)
        submission_documents = [
            path
            for path in matching_nonempty_files(
                project, "submission", {".docx", ".pdf", ".tex", ".zip"}
            )
            if any(token in path.name.casefold() for token in ("manuscript", "main_text", "maintext"))
        ]
        if not submission_documents:
            issues.append(
                Issue(
                    "error",
                    "submission_files",
                    "submission/",
                    "no clearly named manuscript document found",
                )
            )
        cover_letters = [
            path
            for path in matching_nonempty_files(project, "submission")
            if "cover" in path.name.casefold() and "letter" in path.name.casefold()
        ]
        if not cover_letters:
            severity = "error" if strict else "warning"
            issues.append(
                Issue(
                    severity,
                    "cover_letter",
                    "submission/",
                    "cover letter not found; verify whether the target journal requires one",
                )
            )


def scan_placeholders(project: Path, stage: str, strict: bool) -> list[Issue]:
    issues: list[Issue] = []
    excluded_roots = {
        (project / "backups").resolve(),
        (project / "data/raw").resolve(),
        (project / "search/raw").resolve(),
    }
    stage_roots = {
        "intake": {"project_state.md"},
        "discovery": {"project_state.md", "discovery"},
        "protocol": {"project_state.md", "protocol"},
        "retrieval": {"project_state.md", "search", "evidence", "data/derived"},
        "analysis": {"project_state.md", "protocol", "analysis"},
        "manuscript": {"project_state.md", "manuscript"},
        "review": {"project_state.md", "manuscript", "quality"},
        "submission": {"project_state.md", "manuscript", "quality", "submission"},
        "all": {
            "project_state.md",
            "discovery",
            "protocol",
            "search",
            "evidence",
            "data/derived",
            "analysis",
            "manuscript",
            "quality",
            "submission",
        },
    }
    active_roots = stage_roots[stage]
    for path in project.rglob("*"):
        if not path.is_file() or path.suffix.casefold() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(project)
        if relative.name == "validation_report.json":
            continue
        relative_posix = relative.as_posix()
        if not any(
            relative_posix == root or relative_posix.startswith(f"{root}/")
            for root in active_roots
        ):
            continue
        resolved = path.resolve()
        if any(root == resolved or root in resolved.parents for root in excluded_roots):
            continue
        if path.stat().st_size > 5_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeError:
            continue
        matches = list(PLACEHOLDER_PATTERN.finditer(text))
        if matches:
            examples = ", ".join(sorted({match.group(0) for match in matches[:5]}))
            issues.append(
                Issue(
                    "error" if strict else "warning",
                    "unresolved_placeholder",
                    str(relative),
                    f"{len(matches)} unresolved marker(s): {examples}",
                )
            )
    return issues


def main() -> int:
    args = parse_args()
    project = args.project_dir.expanduser().resolve()
    if not project.is_dir():
        raise SystemExit(f"Project directory not found: {project}")

    issues: list[Issue] = []
    validate_stage(project, args.stage, issues, args.strict)
    issues.extend(scan_placeholders(project, args.stage, args.strict))

    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]
    status = "PASS" if not issues else "PASS_WITH_WARNINGS" if not errors else "FAIL"
    report_path = args.report or project / "quality" / "validation_report.json"
    report_path = report_path.expanduser().resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "project": str(project),
        "stage": args.stage,
        "strict": args.strict,
        "status": status,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "issues": [asdict(issue) for issue in issues],
    }
    report_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Status: {status}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for issue in issues:
        print(f"[{issue.severity.upper()}] {issue.path}: {issue.message}")
    print(f"Report: {report_path}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
