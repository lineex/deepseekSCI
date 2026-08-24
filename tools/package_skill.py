#!/usr/bin/env python3
"""Build a deterministic Cherry Studio compatible ZIP for DeepSeekSCI."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path


ARCHIVE_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
MAX_FILE_COUNT = 2_000
MAX_TOTAL_SIZE = 100 * 1024 * 1024
IGNORED_DIRECTORIES = {".git", "__pycache__"}
IGNORED_SUFFIXES = {".pyc", ".pyo"}
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def parse_args() -> argparse.Namespace:
    repository = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Package a skill with SKILL.md at the ZIP root."
    )
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=repository / "skills" / "deepseek-sci",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repository / "releases" / "deepseek-sci-cherry-studio.zip",
    )
    return parser.parse_args()


def collect_files(skill_dir: Path) -> list[Path]:
    files = [
        path
        for path in skill_dir.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_DIRECTORIES for part in path.parts)
        and path.suffix.casefold() not in IGNORED_SUFFIXES
    ]
    files.sort(key=lambda path: path.relative_to(skill_dir).as_posix())
    return files


def validate_skill(skill_dir: Path, files: list[Path]) -> None:
    descriptor = skill_dir / "SKILL.md"
    if not descriptor.is_file():
        raise ValueError(f"SKILL.md not found: {descriptor}")

    content = descriptor.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not frontmatter:
        raise ValueError("SKILL.md has invalid YAML frontmatter delimiters")
    header = frontmatter.group(1)
    if not re.search(r"^name:\s*deepseek-sci\s*$", header, re.MULTILINE):
        raise ValueError("SKILL.md name must be deepseek-sci")
    if not re.search(r"^description:\s*\S", header, re.MULTILINE):
        raise ValueError("SKILL.md description is missing")

    relative_files = {path.relative_to(skill_dir).as_posix() for path in files}
    for target in LINK_PATTERN.findall(content):
        target = target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith("#"):
            continue
        normalized = Path(target).as_posix()
        if normalized not in relative_files:
            raise ValueError(f"SKILL.md references a missing file: {target}")

    if len(files) > MAX_FILE_COUNT:
        raise ValueError(f"Skill has {len(files)} files; limit is {MAX_FILE_COUNT}")
    total_size = sum(path.stat().st_size for path in files)
    if total_size > MAX_TOTAL_SIZE:
        raise ValueError(f"Skill size is {total_size} bytes; limit is {MAX_TOTAL_SIZE}")


def write_zip(skill_dir: Path, output: Path, files: list[Path]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    try:
        with zipfile.ZipFile(
            temporary,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for path in files:
                relative = path.relative_to(skill_dir).as_posix()
                info = zipfile.ZipInfo(relative, ARCHIVE_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)


def verify_zip(output: Path, expected_names: list[str]) -> None:
    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        if names != expected_names:
            raise ValueError("ZIP content differs from the source skill")
        if not names or names[0] != "SKILL.md":
            raise ValueError("SKILL.md must be present at the ZIP root")
        bad_entry = archive.testzip()
        if bad_entry:
            raise ValueError(f"Corrupt ZIP entry: {bad_entry}")


def main() -> int:
    args = parse_args()
    skill_dir = args.skill_dir.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not skill_dir.is_dir():
        raise SystemExit(f"Skill directory not found: {skill_dir}")

    files = collect_files(skill_dir)
    validate_skill(skill_dir, files)
    write_zip(skill_dir, output, files)
    names = [path.relative_to(skill_dir).as_posix() for path in files]
    verify_zip(output, names)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"Package: {output}")
    print(f"Files: {len(files)}")
    print(f"SHA-256: {digest}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
