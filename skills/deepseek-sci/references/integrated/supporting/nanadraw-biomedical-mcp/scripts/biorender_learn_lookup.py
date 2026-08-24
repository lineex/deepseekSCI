#!/usr/bin/env python3
"""Query the locally collected BioRender Learning Hub Overview corpus."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_CORPUS = Path(__file__).resolve().parents[1] / "references" / "biorender-learn-overviews-2026-07-16.json"


def compact(value: str) -> str:
    return " ".join(value.split())


def load_corpus(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Corpus not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload.get("records"), list):
        raise ValueError(f"Invalid corpus: {path}")
    return payload


def overview_snippet(text: str, query: str, limit: int = 560) -> str:
    clean = compact(text)
    if not clean:
        return ""
    terms = [term for term in re.findall(r"[a-z0-9]{3,}", query.casefold())]
    match = next((re.search(re.escape(term), clean, re.IGNORECASE) for term in terms if re.search(re.escape(term), clean, re.IGNORECASE)), None)
    if not match:
        return clean[:limit] + ("..." if len(clean) > limit else "")
    start = max(0, match.start() - limit // 3)
    end = min(len(clean), start + limit)
    prefix = "..." if start else ""
    suffix = "..." if end < len(clean) else ""
    return prefix + clean[start:end] + suffix


def record_row(record: dict[str, Any], query: str | None = None, include_text: bool = False) -> dict[str, Any]:
    text = str(record.get("overview_text", ""))
    row = {
        "title": record.get("title"),
        "url": record.get("url"),
        "category": record.get("category"),
        "overview_found": bool(record.get("overview_found")),
        "overview_paragraphs": int(record.get("overview_paragraphs", 0)),
        "overview_characters": len(text),
        "description": record.get("description"),
        "summary": record.get("summary"),
    }
    if include_text:
        row["overview_text"] = text
    elif text:
        row["excerpt"] = overview_snippet(text, query or str(record.get("title", "")))
    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--stats", action="store_true", help="Print corpus coverage and extraction counts")
    parser.add_argument("--list", action="store_true", help="List all detail pages without Overview text")
    parser.add_argument("--missing-only", action="store_true", help="Limit --list or --query output to pages without Overview")
    parser.add_argument("--query", action="append", default=[], help="Search title, category, description, summary, and Overview text")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--include-text", action="store_true", help="Include complete matching Overview text")
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be positive")
    corpus = load_corpus(args.corpus)
    records = corpus["records"]
    if args.missing_only:
        records = [record for record in records if not record.get("overview_found")]

    if args.stats:
        output: dict[str, Any] = {
            "source": corpus.get("source"),
            "collected_at_utc": corpus.get("collected_at_utc"),
            "catalog_display_count": corpus.get("catalog_display_count"),
            "accessible_detail_pages": corpus.get("accessible_detail_pages"),
            "extraction": corpus.get("extraction"),
        }
    elif args.list:
        output = {"count": len(records), "records": [record_row(record) for record in records]}
    elif args.query:
        query = " ".join(args.query).casefold()
        tokens = [token for token in re.findall(r"[a-z0-9]{2,}", query)]
        ranked: list[tuple[int, str, dict[str, Any]]] = []
        for record in records:
            title = str(record.get("title", ""))
            haystack = " ".join(
                str(record.get(field, ""))
                for field in ("title", "category", "description", "summary", "overview_text")
            ).casefold()
            title_lower = title.casefold()
            score = sum(8 if token in title_lower else 2 for token in tokens if token in haystack)
            if score:
                ranked.append((score, title_lower, record))
        ranked.sort(key=lambda row: (-row[0], row[1]))
        output = {
            "query": args.query,
            "count": len(ranked),
            "records": [record_row(record, query, args.include_text) for _, _, record in ranked[: args.limit]],
        }
    else:
        raise SystemExit("Specify one of --stats, --list, or --query")

    # Keep terminal JSON portable across Windows consoles configured for GBK.
    text = json.dumps(output, indent=2, ensure_ascii=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        print(json.dumps({"output": str(args.output.resolve())}, ensure_ascii=False))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
