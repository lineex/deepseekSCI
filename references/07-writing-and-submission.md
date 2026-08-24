# Writing and Submission

## 1. Write from verified objects

Before drafting, freeze a result package and create `manuscript/claim_evidence.csv`:

```text
claim_id,section,claim_text,claim_type,source_type,source_path_or_id,
locator,verification_status,limitations,last_checked
```

Use analysis outputs for study results and primary/authoritative sources for external claims. Keep `[VERIFY]`, `[DATA CHECK]` and `[CITATION NEEDED]` until resolved; the final submission package must contain none.

## 2. Original research architecture

### Title and abstract

Name the population, key exposure/intervention, outcome and design without overstating causality. In the abstract report sample size, event count, primary estimate with interval, key sensitivity result and restrained conclusion.

### Introduction

Use four moves:

1. burden and decision context;
2. what current evidence establishes;
3. the precise unresolved gap or contradiction;
4. objective, hypothesis and design.

Do not turn the introduction into a broad review or claim novelty without the dated search.

### Methods

Describe what was actually executed: design, data source, dates, eligibility, time zero, variables, outcomes, bias controls, missing data, statistics, software, ethics and reporting guideline. Include enough detail to reproduce the primary estimand.

### Results

Follow participant flow -> characteristics/missingness -> primary result -> diagnostics -> sensitivity/subgroups -> harms or secondary outcomes. Lead with estimates and intervals. Do not interpret mechanisms in Results.

### Discussion

Use six moves:

1. principal finding with magnitude and uncertainty;
2. comparison with directly relevant studies;
3. plausible mechanisms separated from evidence;
4. clinical/scientific meaning without causal overreach;
5. strengths and design-specific limitations;
6. calibrated conclusion and next study.

Explain discordant evidence by comparing population, intervention/exposure, comparator, estimand, outcome timing and model scale before calling results inconsistent.

## 3. Review manuscript architecture

Match the chosen review type and target journal. Build section architecture and a figure/table storyboard before prose. Distribute citations at claim level rather than stacking them at paragraph ends. Include null evidence, controversies and uncertainty. Keep any author-created framework explicitly provisional unless independently validated.

## 4. Scientific editing and language

Run separate passes:

1. **scientific edit**: argument, methods, evidence, causality and internal consistency;
2. **structural edit**: paragraph roles, section order and transitions;
3. **language edit**: precision, concision, grammar and native academic register;
4. **format edit**: journal style, citations, headings and files.

Language polishing must preserve numbers, effect direction, uncertainty, citations, table/figure identifiers and scientific meaning. Prefer neutral result-first prose. Remove exaggerated novelty, empty intensifiers, formulaic AI phrasing, citation dumping and unexplained jargon.

For bilingual manuscripts, translate by scientific intent and venue convention, then synchronize substantive revisions in both versions.

## 5. Tables and figures

- Generate tables and plot data from the analysis pipeline.
- Use consistent denominators, units, precision, abbreviations and footnotes.
- Reserve the main text for primary results; map every supplement item to a Methods step and Results statement.
- Prefer vector PDF/SVG/EPS for line art and journal-compliant raster resolution for images.
- Use accessible colors and verify grayscale/print readability.
- Captions should explain the cognitive purpose, panels, symbols, analysis population and uncertainty.
- Inspect every rendered page/figure, not just file existence.

## 6. Internal peer review

Conduct defect-first reviews from distinct lenses:

- clinical relevance and comparator;
- epidemiology/causal design;
- statistical analysis and reproducibility;
- domain evidence and missing counterevidence;
- reporting guideline and journal fit;
- language, tables, figures and accessibility.

For each finding record severity, exact location, why it matters, supporting evidence and a concrete fix. Resolve major scientific findings before stylistic edits. Re-run affected analyses rather than editing prose around a defect.

## 7. Journal targeting

Build a current shortlist based on scope, article type, audience, methodological fit, recent related publications, indexing, open-access model, fees, word/figure limits and realistic selectivity. Verify all mutable facts on official journal pages and save access date/URL.

Do not select a journal solely by impact factor. Flag predatory or unverifiable venues. Confirm whether preprints, data sharing, code sharing, AI-use disclosure and reporting checklists have specific requirements.

## 8. Submission package

Assemble only applicable files:

```text
submission/
|-- manuscript.docx or manuscript.tex/pdf
|-- title_page.docx
|-- cover_letter.docx
|-- highlights.docx
|-- tables/
|-- figures/
|-- supplementary/
|-- reporting_checklist.*
|-- graphical_abstract.*
|-- permissions/
|-- author_statements/
`-- submission_manifest.md
```

The manifest should record requirement, file, version, hash, validation and remaining owner. Include author names/order, affiliations, corresponding author, ORCID, contributions, acknowledgments, funding, conflicts, ethics, consent, registration, data/code availability and AI-use statements only from confirmed information.

## 9. Cover letter

Keep it approximately one page unless the journal asks otherwise:

1. manuscript title and article type;
2. clinical/scientific problem;
3. central verified finding or contribution;
4. fit with the journal's audience and scope;
5. originality/no simultaneous submission and required declarations;
6. corresponding-author close.

Do not repeat the abstract or make claims stronger than the manuscript.

## 10. Online submission

Use the live submission system to prepare:

- manuscript metadata and abstract;
- authors, affiliations and contributions;
- suggested/opposed reviewers when provided and appropriate;
- classifications, keywords, funding and declarations;
- ordered file uploads and file designations;
- generated proof inspection.

Save a field map and screenshots/receipts as permitted. Resolve conversion warnings and inspect the generated proof. Stop before the irreversible final submission action until the user confirms the exact package and author declarations.

## 11. Revision and resubmission

Create a response matrix:

```text
comment_id,reviewer_comment,classification,decision,response,
manuscript_change,location,evidence_or_analysis,status
```

Quote each comment, answer directly and respectfully, describe the exact change and location, and provide scientific reasoning when declining. Treat any definition or analysis change as a rerun trigger. Produce clean and tracked versions if requested and revalidate the whole submission package.

## 12. Final checks

Run:

```bash
python scripts/validate_project.py PROJECT_DIR --stage submission --strict
```

Then perform journal-specific checks the generic script cannot know: live limits, author forms, checklist locations, file rendering, reference style and generated proof.
