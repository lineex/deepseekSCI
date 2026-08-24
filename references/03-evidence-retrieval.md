# Evidence Retrieval

## 1. Match sources to the question

Use databases for distinct coverage rather than prestige or a fixed count.

| Need | Typical sources |
|---|---|
| Biomedical core | MEDLINE/PubMed, Embase |
| Trials and protocols | CENTRAL, ClinicalTrials.gov, WHO ICTRP |
| Multidisciplinary citation coverage | Web of Science, Scopus, OpenAlex |
| Nursing/allied health | CINAHL |
| Psychology/behavior | PsycINFO |
| Engineering/medical AI | IEEE Xplore, ACM Digital Library |
| Reviews/guidance | Cochrane Library, guideline organizations |
| Preprints | medRxiv, bioRxiv, arXiv when appropriate |
| Regional evidence | Relevant regional databases, documented explicitly |

Google Scholar and publisher platforms can support citation chasing and access, but are poor substitutes for a reproducible primary search.

## 2. Preserve provenance

For every database save:

- database and platform/vendor;
- interface or API version where known;
- full line-by-line query exactly as executed;
- search date and date limits;
- query translation or controlled-vocabulary mapping;
- hit count, export count and coverage limit;
- export format, filename and SHA-256;
- access state and unresolved limitations.

Never reuse old counts as current. Refresh searches for novelty checks and before final submission when recency matters.

## 3. Build searches

1. Express the question as PICO/PICOS, PECO, PCC or SPIDER.
2. Derive concepts, controlled vocabulary and free-text synonyms.
3. Test sentinel papers: the query should recover known eligible studies.
4. Inspect false positives and refine field restrictions without deleting true concept variants.
5. Translate the validated conceptual strategy into each database's native syntax.
6. Peer-review protocol-grade strategies with PRESS when feasible.

Do not force outcome terms when they materially reduce recall. Keep search filters validated and document their source.

## 4. Retrieval and export

Prefer structured APIs or formal exports. Use browser automation for authenticated or dynamic interfaces, while preserving the same provenance fields. Pause at user-controlled login or CAPTCHA and resume after the session is ready.

For PubMed E-utilities retain `count`, `querytranslation`, PMID list, title, abstract when present, publication type, DOI, journal/date and raw XML/JSON. Parse XML with a structured parser, not regular expressions.

Abstract availability is an observed field, not a completion guarantee. Record `abstract_status` as `present`, `not_supplied`, `retrieval_pending` or `full_text_used`. Do not invent or silently reconstruct missing abstracts.

## 5. Deduplication

Use a conservative hierarchy:

1. exact normalized DOI;
2. exact PMID/other stable accession;
3. exact normalized title plus compatible year;
4. high title similarity as a candidate for manual review, not an automatic merge.

Keep companion reports, protocols, abstracts, corrections and secondary analyses linked but distinct unless they are true duplicate records. Preserve all source database identifiers in the retained record.

Use:

```bash
python scripts/deduplicate_records.py search/exports/*.csv \
  --output evidence/deduplicated_records.csv \
  --decisions evidence/deduplication_decisions.csv \
  --counts evidence/source_counts.csv
```

## 6. Screening

- Pilot eligibility rules on a mixed set before full screening.
- Use two independent reviewers for systematic reviews when feasible; record conflicts and adjudication.
- Keep one explicit exclusion reason at full-text stage.
- Distinguish “not retrieved” from “excluded.”
- Preserve screening software export and version.
- Generate PRISMA numbers from the screening table, never from memory.

## 7. Evidence extraction

At minimum capture citation, setting, design, population, sample size, intervention/exposure, comparator, outcome definition, time point, effect measure, estimate, uncertainty, adjustment set, missingness, risk-of-bias information, funding and notes.

For each claim, prefer the primary source over a review's paraphrase. Do not treat multiple reports of one cohort as independent studies.

## 8. Citation network and gap discovery

For anchor papers:

1. inspect references for intellectual ancestry;
2. inspect cited-by records for updates, replications and contradictions;
3. inspect related-article networks for terminology drift;
4. identify active authors, cohorts, trials and unpublished protocols;
5. update the novelty matrix.

## 9. Search completion statement

Report exactly:

```text
Sources completed:
Sources pending or inaccessible:
Last search date:
Records retrieved by source:
Records after deterministic deduplication:
Fuzzy candidates awaiting review:
Known coverage limits:
```

Call work “systematic” only when protocol, coverage, screening, extraction and audit requirements support that label.
