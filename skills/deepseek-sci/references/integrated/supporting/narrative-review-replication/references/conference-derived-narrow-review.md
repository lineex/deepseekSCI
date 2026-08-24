# Integrated supporting reference: narrative-review-replication/references/conference-derived-narrow-review.md

> Embedded source: `embedded-source/narrative-review-replication/references/conference-derived-narrow-review.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Conference-Derived Narrow Review Route

Use this route when the source article states that its content originated from a scientific meeting, symposium, expert lectures, invited abstracts, workshop, or faculty consensus, and it does not report a formal literature search.

## Classification gate

Classify as `conference-derived expert narrative review` when all applicable source statements support this production logic:

1. a named meeting or symposium supplied the content;
2. contributors presented lectures or prepared topic abstracts;
3. one or more editors harmonised those contributions;
4. figures or visual summaries were prepared as integrative teaching devices;
5. all authors reviewed or approved the manuscript;
6. the article is described as selective, focused, non-exhaustive, or partly expert interpretation;
7. no database, query, eligibility, screening, risk-of-bias, or certainty process is reported.

Do not infer a systematic, scoping, or PRISMA method from a long reference list.

## Mandatory two-lane model

### Lane A: author-method replication

Reproduce only source-disclosed production steps. Typical fields are:

```text
review_type
purpose
source_event
event_dates
event_location
content_units
contributor_process
topic_coverage
harmonisation
manuscript_preparation
figure_author
meeting_faculty
author_participation
approval
comprehensiveness
interpretive_position
database_search
search_dates
eligibility_criteria
screening
risk_of_bias
certainty_grading
data_generation
intended_function
```

For absent formal-review fields, record `Not reported; no claim added`. Absence preservation is a scored fidelity behavior.

### Lane B: independent audit

Label all of the following as auditor procedures:

```text
publisher-reference recovery
DOI/PMID verification
reference-role classification
evidence-layer classification
claim-evidence mapping
uncertainty calibration
SANRA-oriented appraisal
optional topic-search recall audit
```

Never merge Lane B into Lane A. An optional reconstructed search may test coverage or support an update, but it is not the source authors' method.

## Dual scoring

Report separate scores:

1. **Disclosed-method fidelity**: exact matched source-disclosed fields / all source-disclosed fields.
2. **Method completeness**: appraisal of the method the source actually reports, using SANRA where applicable.

A result such as `24/24 = 100.000000% disclosed-method fidelity` is valid only when the denominator is explicitly defined. It does not imply that hidden literature selection is reproducible.

Never calculate a single blended score that rewards faithful omission as if it improved methodological completeness.

## Minimum artifacts

```text
01_protocol/review_type_decision.md
01_protocol/author_method_reconstruction.md
01_protocol/original_architecture_map.md
02_search/author_method_search_status.md
02_search/audit_search_protocol.md
03_screening/source_references.csv
03_screening/source_references_enriched.csv
03_screening/reference_recovery_summary.md
04_extraction/original_evidence_map.csv
04_extraction/annotated_reference_roles.csv
04_extraction/evidence_layer_summary.csv
04_extraction/claim_evidence_matrix.csv
04_extraction/source_article_figure_box_inventory.csv
04_extraction/source_article_visual_grammar.md
05_appraisal/methodological_appraisal.md
07_outputs/author_method_flow.mmd
08_benchmark/methodology_field_comparison.csv
08_benchmark/replication_scorecard.csv
08_benchmark/methodology_similarity_report.md
08_benchmark/narrative_architecture_scorecard.csv
08_benchmark/final_architecture_replication_report.md
09_manuscript/replicated_narrow_review.md
10_audit/unresolved_differences.md
10_audit/final_reproducibility_report.md
10_audit/quality_gates.md
```

## Evidence and reference matrices

The reference-role matrix should include:

```text
ref_no,topic_module,evidence_domain,evidence_type,claim_role,directness,identifier_status
```

The claim-evidence matrix should include:

```text
claim_id,module,claim,supporting_refs,evidence_layer,calibrated_language,limitation
```

Every major claim in the replicated manuscript must map to verified references and an explicit limitation or uncertainty statement. Preserve publisher citations when identifiers remain unresolved; do not infer identifiers.

## Architecture benchmark

Recover the source's section functions and argument order, not its sentences. Score:

```text
structured abstract
major section sequence
topic-module coverage
reference corpus and order
figure cognitive functions
uncertainty calibration
declarations and data-availability position
```

Textual duplication and pixel-identical figure copying are not replication targets.

## Figure pairing

When supported by the source, pair two complementary figure functions:

1. **Trajectory figure**: patient journey, disease phases, or care transitions.
2. **Systems figure**: central biological or clinical mediator linked to upstream drivers and downstream consequences.

For each figure, record layout, color semantics, arrow semantics, cognitive function, evidence status, and overclaim risk. Arrows must not imply stronger causal certainty than the evidence supports.

## Appraisal

Use SANRA as an appraisal lens for narrative reviews:

```text
importance for readership
statement of aims
description of literature search
referencing
scientific reasoning
presentation of endpoint data
```

Report SANRA separately from replication fidelity.

## Quality gates

The route is complete only when:

1. every disclosed author-method field is compared;
2. all non-reported formal-review fields remain non-reported;
3. the independent audit is visibly separated from author method;
4. all source references are recovered or explicitly unresolved;
5. all manuscript references are cited in context;
6. all architecture nodes and topic modules are scored;
7. each figure is nonblank and recovers its intended cognitive function;
8. the claim-evidence matrix contains evidence layer, calibrated language, and limitation for every claim;
9. SANRA is reported separately;
10. `unresolved_differences.md` states that hidden literature selection is not estimable.

## Reporting language

Use wording equivalent to:

```text
The source is a conference-derived expert narrative review. Disclosed-method fidelity was calculated only from explicitly reported production fields. Literature-selection procedures not reported by the source were not reconstructed as author methods. Reference recovery, identifier verification, evidence classification, claim mapping, and SANRA appraisal were independent audit procedures.
```

