#!/usr/bin/env python3
"""Conservatively deduplicate bibliographic CSV exports."""

from __future__ import annotations

import argparse
import csv
import io
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path


TITLE_FIELDS = ("title", "articletitle", "documenttitle", "itemtitle")
DOI_FIELDS = ("doi", "digitalobjectidentifier")
PMID_FIELDS = ("pmid", "pubmedid", "pubmedidentifier")
YEAR_FIELDS = ("year", "publicationyear", "pubyear", "coverdate", "date")
ID_FIELDS = ("recordid", "id", "uid", "eid", "accessionnumber", "ut")
COMMON_FIRST_WORDS = {"a", "an", "the"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Merge exact DOI/PMID/title-year duplicates and report fuzzy title "
            "matches for manual review."
        )
    )
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--counts", type=Path, required=True)
    parser.add_argument("--fuzzy-threshold", type=float, default=0.95)
    return parser.parse_args()


def header_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def first_value(row: dict[str, str], candidates: tuple[str, ...]) -> str:
    keyed = {header_key(key): (value or "").strip() for key, value in row.items()}
    for candidate in candidates:
        if keyed.get(candidate):
            return keyed[candidate]
    return ""


def normalize_doi(value: str) -> str:
    value = value.strip().casefold()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)
    value = value.strip().rstrip(".,;)")
    return value if "/" in value else ""


def normalize_pmid(value: str) -> str:
    match = re.search(r"\b(\d{1,9})\b", value)
    return match.group(1) if match else ""


def normalize_year(value: str) -> str:
    match = re.search(r"\b(?:19|20)\d{2}\b", value)
    return match.group(0) if match else ""


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.casefold())
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = "".join(char if char.isalnum() else " " for char in value)
    return " ".join(value.split())


def decode_csv(path: Path) -> str:
    raw = path.read_bytes()
    errors: list[str] = []
    encodings = ["utf-8-sig", "gb18030", "cp1252"]
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        encodings.insert(0, "utf-16")
    for encoding in encodings:
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError as exc:
            errors.append(f"{encoding}: {exc}")
    raise UnicodeError(f"Could not decode {path}: {' | '.join(errors)}")


def read_records(paths: list[Path]) -> tuple[list[dict[str, str]], list[str]]:
    records: list[dict[str, str]] = []
    field_order: list[str] = []
    for path in paths:
        path = path.expanduser().resolve()
        reader = csv.DictReader(io.StringIO(decode_csv(path)))
        if not reader.fieldnames:
            raise ValueError(f"CSV has no header: {path}")
        for field in reader.fieldnames:
            if field not in field_order:
                field_order.append(field)
        for row_number, raw_row in enumerate(reader, start=2):
            row = {str(key): (value or "").strip() for key, value in raw_row.items() if key}
            if not any(row.values()):
                continue
            uid = f"{path.name}:{row_number}"
            row["_record_uid"] = uid
            row["_source_file"] = path.name
            row["_source_id"] = first_value(row, ID_FIELDS) or uid
            row["_norm_doi"] = normalize_doi(first_value(row, DOI_FIELDS))
            row["_norm_pmid"] = normalize_pmid(first_value(row, PMID_FIELDS))
            row["_norm_title"] = normalize_title(first_value(row, TITLE_FIELDS))
            row["_norm_year"] = normalize_year(first_value(row, YEAR_FIELDS))
            records.append(row)
    return records, field_order


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def identity_keys(record: dict[str, str]) -> list[tuple[str, str]]:
    keys: list[tuple[str, str]] = []
    if record["_norm_doi"]:
        keys.append(("doi", record["_norm_doi"]))
    if record["_norm_pmid"]:
        keys.append(("pmid", record["_norm_pmid"]))
    if record["_norm_title"] and record["_norm_year"]:
        keys.append(
            ("title_year", f"{record['_norm_title']}|{record['_norm_year']}")
        )
    return keys


def completeness(record: dict[str, str], original_fields: list[str]) -> tuple[int, int]:
    populated = sum(bool(record.get(field, "").strip()) for field in original_fields)
    text_length = sum(len(record.get(field, "")) for field in original_fields)
    return populated, text_length


def match_reason(left: dict[str, str], right: dict[str, str]) -> str:
    if left["_norm_doi"] and left["_norm_doi"] == right["_norm_doi"]:
        return "exact_doi"
    if left["_norm_pmid"] and left["_norm_pmid"] == right["_norm_pmid"]:
        return "exact_pmid"
    if (
        left["_norm_title"]
        and left["_norm_title"] == right["_norm_title"]
        and left["_norm_year"]
        and left["_norm_year"] == right["_norm_year"]
    ):
        return "exact_title_year"
    return "transitive_exact_identity"


def display_title(record: dict[str, str]) -> str:
    return first_value(record, TITLE_FIELDS)


def fuzzy_block(record: dict[str, str]) -> tuple[str, str]:
    words = record["_norm_title"].split()
    first = next((word for word in words if word not in COMMON_FIRST_WORDS), "")
    return record["_norm_year"], first


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    if not 0.80 <= args.fuzzy_threshold <= 1.0:
        raise SystemExit("--fuzzy-threshold must be between 0.80 and 1.0")
    records, original_fields = read_records(args.inputs)
    if not records:
        raise SystemExit("No non-empty records found")

    union_find = UnionFind(len(records))
    seen: dict[tuple[str, str], int] = {}
    for index, record in enumerate(records):
        for key in identity_keys(record):
            if key in seen:
                union_find.union(index, seen[key])
            else:
                seen[key] = index

    groups: dict[int, list[int]] = defaultdict(list)
    for index in range(len(records)):
        groups[union_find.find(index)].append(index)

    merged_records: list[dict[str, str]] = []
    exact_decisions: list[dict[str, object]] = []
    group_sources: list[set[str]] = []
    for indices in groups.values():
        kept_index = max(indices, key=lambda item: completeness(records[item], original_fields))
        kept = dict(records[kept_index])
        members = [records[item] for item in indices]
        for field in original_fields:
            if not kept.get(field, ""):
                kept[field] = next((member.get(field, "") for member in members if member.get(field, "")), "")
        sources = sorted({member["_source_file"] for member in members})
        source_ids = sorted({member["_source_id"] for member in members})
        kept["_sources"] = ";".join(sources)
        kept["_source_ids"] = ";".join(source_ids)
        kept["_duplicate_count"] = str(len(indices) - 1)
        kept["_dedup_key"] = ";".join(f"{kind}:{value}" for kind, value in identity_keys(kept))
        merged_records.append(kept)
        group_sources.append(set(sources))
        for index in indices:
            if index == kept_index:
                continue
            candidate = records[index]
            exact_decisions.append(
                {
                    "candidate_type": "exact",
                    "kept_uid": kept["_record_uid"],
                    "candidate_uid": candidate["_record_uid"],
                    "reason": match_reason(kept, candidate),
                    "similarity": "1.000000",
                    "status": "auto_merged",
                    "kept_title": display_title(kept),
                    "candidate_title": display_title(candidate),
                }
            )

    blocks: dict[tuple[str, str], list[int]] = defaultdict(list)
    for index, record in enumerate(merged_records):
        if len(record["_norm_title"]) >= 20:
            block = fuzzy_block(record)
            if block[0] and block[1]:
                blocks[block].append(index)

    fuzzy_decisions: list[dict[str, object]] = []
    for indices in blocks.values():
        for left_index, right_index in combinations(indices, 2):
            left = merged_records[left_index]
            right = merged_records[right_index]
            similarity = SequenceMatcher(
                None, left["_norm_title"], right["_norm_title"], autojunk=False
            ).ratio()
            if similarity >= args.fuzzy_threshold:
                fuzzy_decisions.append(
                    {
                        "candidate_type": "fuzzy_title",
                        "kept_uid": left["_record_uid"],
                        "candidate_uid": right["_record_uid"],
                        "reason": "similar_title_same_year",
                        "similarity": f"{similarity:.6f}",
                        "status": "manual_review",
                        "kept_title": display_title(left),
                        "candidate_title": display_title(right),
                    }
                )

    metadata_fields = (
        "_record_uid",
        "_sources",
        "_source_ids",
        "_duplicate_count",
        "_dedup_key",
    )
    output_fields = original_fields + [field for field in metadata_fields if field not in original_fields]
    write_csv(args.output, output_fields, merged_records)
    decision_fields = [
        "candidate_type",
        "kept_uid",
        "candidate_uid",
        "reason",
        "similarity",
        "status",
        "kept_title",
        "candidate_title",
    ]
    write_csv(args.decisions, decision_fields, exact_decisions + fuzzy_decisions)

    input_counts = Counter(record["_source_file"] for record in records)
    represented_counts = Counter()
    for sources in group_sources:
        represented_counts.update(sources)
    count_rows = []
    for source in sorted(input_counts):
        represented = represented_counts[source]
        count_rows.append(
            {
                "source_file": source,
                "input_records": input_counts[source],
                "retained_groups_containing_source": represented,
                "exact_duplicates_removed": input_counts[source] - represented,
            }
        )
    write_csv(
        args.counts,
        [
            "source_file",
            "input_records",
            "retained_groups_containing_source",
            "exact_duplicates_removed",
        ],
        count_rows,
    )

    print(f"Input records: {len(records)}")
    print(f"Records after exact deduplication: {len(merged_records)}")
    print(f"Exact duplicates merged: {len(exact_decisions)}")
    print(f"Fuzzy candidates for manual review: {len(fuzzy_decisions)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
