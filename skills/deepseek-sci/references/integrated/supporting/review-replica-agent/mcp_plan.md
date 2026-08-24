# Integrated supporting reference: review-replica-agent/mcp_plan.md

> Embedded source: `embedded-source/review-replica-agent/mcp_plan.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# ReviewReplicaAgent MCP Plan

## Already available / should be used first

| Capability | Current MCP/skill | Use in ReviewReplicaAgent |
|---|---|---|
| PubMed search and metadata | `aipubmed` MCP; `pm-*` skills | Rebuild PubMed searches, fetch PMID metadata, export RIS, inspect articles. |
| Web/PDF page inspection | Browser / Chrome DevTools tools | Locate supplements, publisher pages, PRISMA/Cochrane guidance, trial registries. |
| Medical review methodology | `medical-review-writing`, `Critical Care Review Master` | PRISMA/Cochrane-style review workflow and reporting. |
| Statistical analysis | `medical-stat-project-agent`, `stat-project-agent` | R scripts, tables, diagnostic reports, reproducible analysis. |
| Replication verification | `scholar-replication`, `scholar-verify`, `scholar-code-review` | Audit code-output-manuscript consistency. |

## Recommended new MCPs if you want near-complete automation

1. `zotero-mcp`
   - Priority: high
   - Why: local PDF/library access, collections, item keys, tags, included-study matching.

2. `crossref-openalex-mcp`
   - Priority: high
   - Why: DOI enrichment, duplicate report detection, preprint/published-version matching, author-year normalization.

3. `pdf-table-mcp`
   - Priority: high
   - Why: extracting tables and target values from PDFs/supplements/forest plots.

4. `screening-sqlite-mcp`
   - Priority: medium-high
   - Why: durable audit trail for screening decisions, exclusion reasons, PRISMA counts, human adjudication.

5. Database-specific MCPs, depending on access: `embase-mcp`, `cochrane-central-mcp`, `web-of-science-mcp`, `scopus-mcp`, `cinahl-mcp`.
   - Priority: conditional
   - Why: original reviews often use databases beyond PubMed; without them search replication may be partial.

## If new MCPs are not installed

Use file-based fallbacks:

- Export RIS/CSV from databases manually into `02_search/raw_exports/`.
- Export Zotero collections manually as RIS/CSV/BibTeX.
- Put PDF supplements into `00_original/` and extract tables manually or with local scripts.
- Store screening decisions in CSV files under `03_screening/`.

## Rule

Never claim an MCP is available unless the active tool list/source list confirms it. If unavailable, state the limitation and continue with a transparent file-based workflow.

