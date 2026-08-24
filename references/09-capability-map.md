# Capability Map and Provenance

## Purpose

This skill is a new portable synthesis of the medical-research capabilities found in the local Codex and agent skill libraries. Duplicate copies under `.codex/skills` and `.agents/skills` were consolidated by capability/name. The listed skills are design inputs and optional local accelerators, not runtime dependencies.

## Integrated capability families

### Research control, discovery and methods

- `medical_research_architect`: stateful PICO-to-publication control.
- `medical-research-submission`: staged idea-to-submission pipeline.
- `research-workflow-adapter`: project structure, definition locks and analysis-manuscript synchronization.
- `personal-research-discovery-os`: intent routing and research opportunity exploration.
- `data-to-discovery-agent`: dataset-to-finding and hypothesis loop.
- `method-innovation-engine`: construct, comparator and validation design for new methods.
- `theoretical-discovery-engine`: theory and falsifiable mechanism generation.
- `nsfc-topic-ideation`: literature-grounded grant topic development.
- `reference-intelligence-mining`, `citing-papers-intelligence`: backward/forward citation intelligence.

### Clinical design, data and statistics

- `medical-stat-project-agent`, `stat-project-agent`: clinical and general statistical project execution.
- `mimicr-agent`: MIMIC cohort/extraction/analysis contracts and time alignment.
- `nhanesr-research-agent`, `nhanesr-auto-params`, `nhanesr-function-reference`: NHANES extraction, parameter mapping and survey design.
- `medical-rct-advanced`: RCT design, multicenter analysis, estimands and null-result interpretation.
- `data-to-discovery-agent`: bias-aware analysis and discovery extraction.
- `supabase-postgres-best-practices`: database performance patterns when research data use Postgres.

### Review and evidence synthesis

- `review-feasibility-to-meta`: feasibility gates, protocol, screening, extraction, synthesis and certainty.
- `literature-review-workflow`: review-mode routing and shared artifacts.
- `medical-review-writing`: journal-shaped medical review architectures.
- `critical-care-review-master`: critical-care evidence synthesis and review writing.
- `narrative-review-replication`: architecture recovery, evidence maps and review-to-new-research translation.
- `review-replica-agent`: protocol/search/extraction/statistical replication of reviews.
- `iterative-review-writing`: multi-round, evidence-anchored review drafting.
- `review-notes-summary`, `review-notes-questioning`: structured note synthesis and critical questioning.
- `narrative-review-replication`, `review-replica-agent`: figure/box storyboards and replication scorecards.

### Bibliographic search and retrieval

- PubMed: `pm-search`, `pm-advanced-search`, `pm-paper-detail`, `pm-navigate-pages`, `pm-export`, `pm-fulltext`.
- Embase: `embase-session`, `embase-check-login`, `embase-login`, `embase-web-search`.
- Web of Science: `wos-search`, `wos-parse-results`, `wos-navigate-pages`, `wos-paper-detail`, `wos-export`, `wos-download`, `wos_lit_mining`.
- Scopus: `scopus-search`, `scopus-advanced-search`, `scopus-parse-results`, `scopus-navigate-pages`, `scopus-document-detail`, `scopus-author-detail`, `scopus-source-browse`, `scopus-export`, `scopus-fulltext`, `scopus-login`.
- Cochrane: `ch-search`, `ch-advanced-search`, `ch-parse-results`, `ch-navigate-pages`, `ch-paper-detail`, `ch-export`, `ch-download`.
- ScienceDirect: `sd-search`, `sd-advanced-search`, `sd-parse-results`, `sd-navigate-pages`, `sd-paper-detail`, `sd-journal-browse`, `sd-export`, `sd-download`.
- Google Scholar: `gs-search`, `gs-advanced-search`, `gs-navigate-pages`, `gs-cited-by`, `gs-export`, `gs-fulltext`.
- Engineering evidence: `ieee-xplore-database`.
- Reference management and styles: `zotero-csl-skill`, `pm-export`, database-specific export skills.
- Cross-database coordination: `literature-review-workflow`, `review-feasibility-to-meta`, `WOS Literature Mining`.

### Manuscript, language, review and submission

- `manuscript-writing-polish-format`: draft-to-submission gates and revision control.
- `humanizer`, `academic-humanizer`: evidence-preserving clinical/academic prose repair.
- `bilingual-academic-writer`: intent-preserving Chinese-English academic rewriting.
- `bachert-academic-polish`: restrained biomedical review style.
- `ai-peer-reviewer`: defect-oriented scientific peer review.
- `academic-email-writer-en`: journal/editor/reviewer correspondence.
- `zotero-csl-skill`: citation style generation and validation.
- `nanadraw-biomedical-mcp`: editable biomedical figures.
- `sync-docs`: cross-artifact consistency checks.
- `research-paper-writer`: general formal manuscript construction.

### Domain lenses retained as optional overlays

- `demetrios-demetriades-perspective`: trauma mechanism, lethal priority and system accountability.
- `critical-care-review-master`: ICU evidence and journal expectations.
- `bachert-academic-polish`: rhinology/mucosal immunology prose conventions.
- `medical-rct-advanced`: high-impact trial methodology.

Domain lenses refine reasoning or prose; they never replace evidence, design or statistical validation.

## Portability decisions

The integrated skill intentionally:

1. uses generic capability names instead of requiring MCP/tool identifiers;
2. uses standard-library Python scripts;
3. stores reusable templates in the repository;
4. preserves authenticated-browser pauses and provenance;
5. avoids claims that every database exposes every abstract or that a fixed database count suits every question;
6. avoids mechanical fixes such as automatic VIF deletion, automatic trim-and-fill or significance-driven model changes;
7. makes actual artifacts and stage gates the definition of progress.

## External capabilities not bundled

Access to subscription databases, private clinical data, R/Python packages, reference managers, Office/PDF renderers and online submission systems depends on the host environment. At startup, inventory available capabilities and substitute equivalent tools while preserving the workflow contracts.
