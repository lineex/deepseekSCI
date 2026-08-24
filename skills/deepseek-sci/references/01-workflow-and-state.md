# Workflow and State

## 1. Project control

Treat `project_state.md` as the control plane. Before substantive work:

1. Identify the newest coherent protocol, dataset, result package and manuscript.
2. Compare them with the locked definitions in state.
3. Inspect the change log and version-control status.
4. Set one immediate objective and one next action.

Use these statuses: `not_started`, `in_progress`, `needs_review`, `accepted`, `blocked`, `superseded`. `accepted` means the underlying artifact was inspected, not merely created.

## 2. Source-of-truth hierarchy

When files disagree, use this order and record the decision:

1. latest explicitly accepted project state;
2. locked protocol/SAP and amendments;
3. current executable code plus run manifest;
4. current machine-readable tables and figures;
5. manuscript text;
6. older drafts and backups.

Manuscript prose never overrides verified analytical output.

## 3. Change classification

Definition-changing events include changes to eligibility, time zero, exposure/intervention, comparator, primary outcome, follow-up, phenotype, subgroup, unit, transformation, covariate definition, missing-data rule or main sample.

For a definition-changing event:

1. record the amendment and rationale;
2. preserve the former baseline;
3. identify affected extraction, analysis, tables, figures and text;
4. rerun all affected outputs;
5. update abstract, methods, results, discussion, legends, supplements and cover letter;
6. mark superseded artifacts.

Label-only and formatting changes normally do not trigger analysis, but verify that computation keys are unchanged.

## 4. Decision log

For every consequential choice, record:

```text
date | stage | decision | alternatives | evidence | rationale | affected files | owner
```

Keep protocol deviations distinct from amendments made before data/results were examined.

## 5. Default folders

```text
project/
|-- project_state.md
|-- discovery/
|-- protocol/
|-- search/raw/
|-- search/exports/
|-- evidence/screening/
|-- evidence/extraction/
|-- data/raw/              # read-only or external pointer
|-- data/intermediate/
|-- data/derived/
|-- analysis/scripts/
|-- analysis/outputs/
|-- manuscript/drafts/
|-- manuscript/tables/
|-- manuscript/figures/
|-- manuscript/supplement/
|-- quality/
|-- submission/
|-- logs/
`-- backups/
```

Do not copy protected or very large raw clinical data merely to satisfy this layout. Store a pointer, access method, schema and checksum where appropriate.

## 6. Handoff checkpoints

At each checkpoint provide:

- decision reached;
- evidence inspected;
- files created or superseded;
- validation performed;
- unresolved uncertainty;
- next single action.

Use a human checkpoint for selecting among scientifically different primary questions, approving a locked protocol, entering credentials/CAPTCHA, confirming author/ethics information and clicking final submission. Continue independently through mechanical and analytical work.

## 7. Failure handling

- Parsing/encoding: preserve raw input, fix the parser, regenerate structured output and compare counts.
- Network/rate limit: retain partial results and cursor, apply documented backoff, then resume without duplicating records.
- Login: keep the browser at the correct login page and record the database as pending.
- Model failure: diagnose data separation, sparse cells, convergence, positivity and specification; choose a defensible method and document it. Do not silently delete observations or covariates.
- Conflicting baselines: select the newest internally coherent accepted package when evidence is clear; otherwise pause before overwriting.

## 8. Reproducible run manifest

Each computational run should capture:

```json
{
  "run_id": "timestamp-or-commit",
  "protocol_version": "VERSION",
  "input_files": [{"path": "PATH", "sha256": "HASH"}],
  "script": "PATH",
  "software": {"language": "Python", "version": "VERSION"},
  "seed": "SEED-or-not-applicable",
  "parameters": {},
  "outputs": [{"path": "PATH", "sha256": "HASH"}],
  "status": "success-or-failed"
}
```

## 9. Resume format

```text
Project:
Route:
Current accepted baseline:
Open definition change:
Current stage and gate:
Last verified artifact:
Known limitations:
Next single action:
```
