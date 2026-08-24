# Integrated Execution Contract

This file makes the package a single executable skill rather than a directory that merely names other skills. The chapters in `references/integrated/` are embedded operational knowledge. They are selected by capability and executed under the contracts below; no external skill installation or handoff is required.

## 1. Precedence and conflict resolution

Apply rules in this order:

1. User's current study question, data, target output, and explicit constraints.
2. This `deepseek-sci` `SKILL.md`, including its Python-only and provenance requirements.
3. This integrated execution contract and the stage references `01`–`09`.
4. The relevant embedded chapter(s) in `references/integrated/`.
5. Examples in an embedded chapter.

When embedded chapters disagree, preserve the stricter provenance, reproducibility, missing-data, reporting, or quality rule. Resolve naming differences by writing a mapping in `project_state.md`; never silently maintain two competing definitions.

## 2. Capability loading is internal

Use the source-skill index to select chapters. The names in that index are provenance labels, not calls to another agent. Load the chapter into the current reasoning context and apply its procedures directly. If a chapter mentions an unavailable MCP, browser connector, R package, or command, preserve the scientific operation and implement it with the available Python/API/browser capability; record the substitution and its evidence boundary.

## 3. Stage-to-capability integration

### S0: Intake, question and research direction

Load the chapters for `medical_research_architect`, `personal_research_discovery_os`, `data_to_discovery_agent`, `method_innovation_engine`, `theoretical_discovery_engine`, `nsfc_topic_ideation`, and `research_workflow_adapter`.

Produce a single question tree: clinical problem or mechanism, PICO/PECO/PCC, target population, time zero, exposure/intervention, comparator, outcome, estimand, candidate mechanism, data source, target journal, and feasibility denominator. Generate several candidate questions, challenge each for duplication and measurement feasibility, then lock one primary question.

### S1: Evidence retrieval and landscape

Load the relevant PubMed, Embase, Web of Science, Scopus, Cochrane, ScienceDirect, Google Scholar, IEEE, citation-intelligence, and Zotero chapters. Use the eight-action connector contract in the parent skill, plus the source-specific syntax and export procedures in these chapters. Every query receives a stable `query_id`; raw responses and formal exports are immutable.

### S2: Screening, extraction and review architecture

Load `literature_review_workflow`, `review_feasibility_to_meta`, `review_replica_agent`, `narrative_review_replication`, `iterative_review_writing`, `review_notes_summary`, `review_notes_questioning`, and `medical_review_writing` as needed. Decide review type before writing. Preserve independent screening decisions, exclusion reasons, extraction versions, risk-of-bias judgments, certainty judgments, and a claim-level evidence matrix.

### S3: Design, data and statistical analysis

Load `medical_rct_advanced` for trials, `medical_stat_project_agent` and `stat_project_agent` for general analysis, `mimicr_agent` for MIMIC/EHR, and the NHANES chapters for survey data. Implement observational, target-trial, prediction, diagnostic, causal, and meta-analytic paths in Python. Separate raw extraction, normalized data, analysis datasets, model objects, diagnostics, and manuscript outputs. Do not replace the prespecified estimand with a result-driven alternative.

### S4: Synthesis and manuscript construction

Load `manuscript_writing_polish_format`, `research_paper_writer`, `medical_review_writing`, `critical_care_review_master`, `academic_humanizer`, `humanizer`, `bachert_academic_polish`, and `bilingual_academic_writer`. Draft only from verified evidence objects and locked analysis outputs. Keep scientific editing, language editing, citation verification, figure/table QA, and format conversion as separate audit events.

### S5: Internal review, journal targeting and submission

Load `ai_peer_reviewer`, `academic_email_writer_en`, `zotero_csl_skill`, and `sync_docs`, together with the submission section of `medical_research_submission`. Run methodological, statistical, citation, reporting-guideline, and presentation reviews. Recheck the current journal instructions, assemble the submission manifest, and stop at the final user-confirmed submission action.

## 4. Cross-cutting object contract

Every stage reads and writes the same objects:

- `project_state.md`: phase, locked definitions, assumptions, approvals, substitutions, and next action.
- `protocol/protocol.md` and `protocol/sap.md`: question, estimand, design, variables, outcomes, models, missingness, sensitivity analyses, and reporting guideline.
- `search/search_log.csv`: source, platform, query, query translation, date, count, export count, raw path, hash, access status, and limitations.
- `evidence/`: normalized records, screening, extraction, risk of bias, certainty, and claim evidence.
- `analysis/`: Python scripts, run manifest, derived data, model objects, diagnostics, tables, and figures.
- `manuscript/`: drafts, claims, references, tables, figures, supplements, and journal format state.
- `quality/`: internal review, citation audit, number traceability, encoding/structure/visual checks, and unresolved issues.
- `submission/`: manuscript, title page, cover letter, declarations, checklists, figures, tables, supplements, and manifest.

## 5. No silent delegation

Do not answer that a separate skill must be activated. Use the embedded chapter. If a required source is absent, state the exact missing capability, perform the available portion, and record the limitation in `project_state.md` and the relevant audit file.

## 6. Python-only translation table

| Source instruction | Integrated implementation |
|---|---|
| R/Rscript analysis | Python with pandas/Polars, SciPy, statsmodels, scikit-learn, lifelines, PyMC, or a documented equivalent |
| Bash/PowerShell pipeline | Python `argparse` entry point and `pathlib` file operations |
| Zotero/MCP search | Available Zotero API/MCP/browser or a reproducible export/API connector, with a saved query log |
| Browser-only export | Playwright or the host browser connector, preserving the downloaded source file and hash |
| Image-generation helper | Editable SVG/PNG/PDF generated from Python plotting or an available figure tool, with a figure manifest |

The translation does not erase source-specific methods; it changes only the execution mechanism and is recorded in the run manifest.
