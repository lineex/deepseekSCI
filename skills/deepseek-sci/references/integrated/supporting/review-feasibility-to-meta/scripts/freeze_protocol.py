#!/usr/bin/env python3
"""Create a dated, checksummed snapshot of protocol-defining files."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


FILES = ["protocol.md", "analysis_plan.md", "search_strategy_draft.md"]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    root = args.project_dir.resolve()
    protocol_dir = root / "02_protocol"
    missing = [name for name in FILES if not (protocol_dir / name).exists()]
    if missing:
        print("FAIL: missing protocol files: " + ", ".join(missing))
        return 1
    unresolved = [name for name in FILES if "[REQUIRED]" in (protocol_dir / name).read_text(encoding="utf-8")]
    if unresolved:
        print("FAIL: unresolved required fields: " + ", ".join(unresolved))
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    snapshot_dir = protocol_dir / "snapshots" / f"v{args.version}_{stamp}"
    snapshot_dir.mkdir(parents=True, exist_ok=False)
    lines = []
    for name in FILES:
        source = protocol_dir / name
        target = snapshot_dir / name
        shutil.copyfile(source, target)
        lines.append(f"{digest(target)}  snapshots/{snapshot_dir.name}/{name}")
    manifest = "\n".join(lines) + "\n"
    (protocol_dir / "protocol_snapshot.sha256").write_text(manifest, encoding="ascii")

    state_path = root / "review_state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["protocol_version"] = args.version
        state["updated_at"] = datetime.now(timezone.utc).isoformat()
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: protocol snapshot {snapshot_dir}")
    print(manifest, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
