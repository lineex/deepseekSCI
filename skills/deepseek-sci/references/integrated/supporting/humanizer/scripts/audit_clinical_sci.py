#!/usr/bin/env python3
"""Transparent heuristic language audit for clinical SCI manuscript prose.

The audit highlights passages for editorial review. It does not classify
authorship, make changes, or replace statistical and scientific review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


AI_PHRASES = {
    "increasing evidence indicates": "Replace with the specific evidence or a direct claim.",
    "it is important to note": "Delete the lead-in and state the point directly.",
    "it is worth noting": "Delete the lead-in and state the point directly.",
    "this is clinically relevant because": "State the clinical consequence directly.",
    "plays a central role": "Name the observed relation or evidence-supported mechanism.",
    "highly useful": "Describe the specific utility and its scope.",
    "provides novel insights": "State the precise contribution and its comparator.",
    "highlights the importance": "State what the findings show.",
    "underscores the importance": "State what the findings show.",
    "groundbreaking": "Remove promotional language.",
    "pivotal": "Remove promotional language or state the concrete reason.",
    "transformative": "Remove promotional language or state the concrete reason.",
    "taken together": "Use only when the preceding evidence warrants a synthesis.",
}

TRANSITIONS = {
    "additionally",
    "furthermore",
    "moreover",
    "in addition",
    "importantly",
    "notably",
}

CAUSAL_TERMS = re.compile(
    r"\b(?:caused|causes|causing|led to|resulted in|reduced|increased|"
    r"improved|worsened|affected)\b",
    re.IGNORECASE,
)

ESSENTIAL_ING_WORDS = {"including", "using", "adjusting", "accounting"}
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])(?:\s+|\n+)")
WORD_PATTERN = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)?|\d+(?:\.\d+)?%?")


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    location: str
    excerpt: str
    recommendation: str


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        try:
            from docx import Document
        except ImportError as exc:
            raise RuntimeError(
                "Reading .docx files requires python-docx. Install it or export the text as .txt/.md."
            ) from exc
        document = Document(path)
        return "\n".join(paragraph.text for paragraph in document.paragraphs if paragraph.text.strip())

    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def exclude_reference_list(text: str) -> str:
    """Exclude a conventional reference list from a whole-manuscript audit."""
    match = re.search(r"(?im)^\s*references\s*$", text)
    return text[: match.start()].rstrip() if match else text


def sentences(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    return [sentence.strip() for sentence in SENTENCE_SPLIT.split(normalized) if sentence.strip()]


def excerpt(text: str, limit: int = 220) -> str:
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def find_phrase_matches(text: str) -> Iterable[Finding]:
    lowered = text.lower()
    for phrase, recommendation in AI_PHRASES.items():
        offset = lowered.find(phrase)
        while offset != -1:
            context = text[max(0, offset - 70) : min(len(text), offset + len(phrase) + 100)]
            yield Finding(
                severity="medium",
                category="template-like phrase",
                location=f"character {offset + 1}",
                excerpt=excerpt(context),
                recommendation=recommendation,
            )
            offset = lowered.find(phrase, offset + len(phrase))


def find_sentence_matches(
    source_sentences: list[str], observational: bool, max_sentence_words: int
) -> Iterable[Finding]:
    starts: Counter[str] = Counter()
    indexed_starts: list[tuple[int, str, str]] = []

    for index, sentence in enumerate(source_sentences, start=1):
        location = f"sentence {index}"
        word_count = len(WORD_PATTERN.findall(sentence))
        if word_count > max_sentence_words:
            yield Finding(
                severity="medium",
                category="long sentence",
                location=location,
                excerpt=excerpt(sentence),
                recommendation=(
                    "Check whether the result, explanation, and qualification should be split into separate sentences."
                ),
            )

        if "—" in sentence:
            yield Finding(
                severity="low",
                category="em dash",
                location=location,
                excerpt=excerpt(sentence),
                recommendation="Use a period, comma, or parentheses according to the logical relation.",
            )

        if re.match(r"^(?:Moreover|Furthermore|Additionally|In addition|Importantly|Notably),?\b", sentence, re.I):
            yield Finding(
                severity="low",
                category="stock transition",
                location=location,
                excerpt=excerpt(sentence),
                recommendation="Remove it or replace it with an explicit logical relation.",
            )

        tail = re.search(r",\s+([A-Za-z]+ing)\b[^,;:.]*[.]?$", sentence)
        if tail and tail.group(1).lower() not in ESSENTIAL_ING_WORDS:
            yield Finding(
                severity="low",
                category="terminal -ing clause",
                location=location,
                excerpt=excerpt(sentence),
                recommendation="Check whether the clause adds a separate claim. A new sentence is often clearer.",
            )

        if re.match(
            r"^(?:This|These|It)\s+(?:is|are|was|were|does|did|has|have|may|"
            r"might|can|could|should|will|would|supports|suggests|shows)\b",
            sentence,
        ):
            yield Finding(
                severity="low",
                category="ambiguous pronoun opening",
                location=location,
                excerpt=excerpt(sentence),
                recommendation="Name the result, population, model, or outcome if the antecedent is not immediate.",
            )

        association_language = re.search(
            r"\b(?:associated|correlated|linked|related) with\b", sentence, re.IGNORECASE
        )
        reference_entry = re.match(r"^[A-Z][A-Za-z-]+,\s+et al\.,", sentence)
        if observational and CAUSAL_TERMS.search(sentence) and not association_language and not reference_entry:
            yield Finding(
                severity="high",
                category="causal wording in observational manuscript",
                location=location,
                excerpt=excerpt(sentence),
                recommendation="Confirm that causal language is justified; otherwise use association wording.",
            )

        words = WORD_PATTERN.findall(sentence.lower())
        if len(words) >= 3:
            start = " ".join(words[:3])
            starts[start] += 1
            indexed_starts.append((index, start, sentence))

    for index, start, sentence in indexed_starts:
        if starts[start] >= 3:
            yield Finding(
                severity="low",
                category="repeated sentence opening",
                location=f"sentence {index}",
                excerpt=excerpt(sentence),
                recommendation=f"This three-word opening occurs {starts[start]} times. Vary it only if meaning remains precise.",
            )


def audit(text: str, observational: bool, max_sentence_words: int) -> list[Finding]:
    source_sentences = sentences(text)
    findings = list(find_phrase_matches(text))
    findings.extend(find_sentence_matches(source_sentences, observational, max_sentence_words))
    return findings


def print_report(path: Path, findings: list[Finding], sentence_count: int, section: str | None) -> None:
    counts = Counter(finding.severity for finding in findings)
    print("Clinical SCI Language Audit")
    print(f"File: {path}")
    if section:
        print(f"Section: {section}")
    print(f"Sentences reviewed: {sentence_count}")
    print(f"Findings: high={counts['high']}, medium={counts['medium']}, low={counts['low']}")
    print()

    if not findings:
        print("No heuristic flags. This is not a scientific or factual validation result.")
        return

    severity_order = {"high": 0, "medium": 1, "low": 2}
    for finding in sorted(findings, key=lambda item: (severity_order[item.severity], item.location)):
        print(f"[{finding.severity.upper()}] {finding.category} | {finding.location}")
        print(f"  Excerpt: {finding.excerpt}")
        print(f"  Review: {finding.recommendation}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Flag language patterns for manual review in clinical SCI prose."
    )
    parser.add_argument("input", type=Path, help="UTF-8 .txt/.md file or a .docx file.")
    parser.add_argument("--section", help="Optional section name for the report header.")
    parser.add_argument(
        "--observational",
        action="store_true",
        help="Flag causal verbs for manual review in observational manuscripts.",
    )
    parser.add_argument(
        "--max-sentence-words",
        type=int,
        default=35,
        help="Flag sentences above this word count (default: 35).",
    )
    parser.add_argument(
        "--include-references",
        action="store_true",
        help="Audit the reference list as well as manuscript body text.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON rather than a text report.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_sentence_words < 10:
        print("--max-sentence-words must be at least 10.", file=sys.stderr)
        return 2
    if not args.input.is_file():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        return 2

    try:
        text = read_text(args.input)
    except (OSError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    working_text = text if args.include_references else exclude_reference_list(text)
    findings = audit(working_text, args.observational, args.max_sentence_words)
    if args.json:
        payload = {
            "file": str(args.input),
            "section": args.section,
            "references_excluded": not args.include_references,
            "sentences_reviewed": len(sentences(working_text)),
            "findings": [asdict(finding) for finding in findings],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print_report(args.input, findings, len(sentences(working_text)), args.section)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
