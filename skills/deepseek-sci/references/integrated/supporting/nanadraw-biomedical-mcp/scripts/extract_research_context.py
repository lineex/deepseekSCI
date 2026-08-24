from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract structured research context for NanaDraw figure planning.")
    parser.add_argument("document", help="Path to .txt, .md, .tex, .latex, or .docx")
    parser.add_argument("--root", help="NanaDraw repository root; defaults to NANADRAW_ROOT or the current directory")
    args = parser.parse_args()

    root = Path(args.root or os.environ.get("NANADRAW_ROOT") or Path.cwd()).expanduser().resolve()
    if not (root / "mcp_server" / "research_context.py").is_file():
        raise SystemExit("NanaDraw root not found. Pass --root or set NANADRAW_ROOT.")
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    from mcp_server.research_context import extract_research_context

    result = extract_research_context(Path(args.document))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
