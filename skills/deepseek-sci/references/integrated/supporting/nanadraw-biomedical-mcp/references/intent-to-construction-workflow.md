# Integrated supporting reference: nanadraw-biomedical-mcp/references/intent-to-construction-workflow.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/intent-to-construction-workflow.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Intent-to-Construction Workflow

Use this workflow whenever a user starts with prose, a long image prompt, a method paragraph, or a rough visual idea.

## Provenance

This workflow adapts several engineering ideas from [ResearAI/AutoFigure-Edit](https://github.com/ResearAI/AutoFigure-Edit), reviewed at commit `a14889f82b9ed1376b848d8e8eaaf6bca6077033`:

- persist inspectable intermediate artifacts
- map regions and assets through stable IDs
- render the current editable artifact before optimization
- compare, revise iteratively, and preserve the previous valid version
- separate structural templating from final asset assembly

NanaDraw extends those ideas with a scientific intent contract, composition scoring, Bioicons grounding, connector semantics, editable-text requirements, and a seven-category post-generation audit. No AutoFigure-Edit code, SAM assets, or editor bundle is copied into this workflow.

## Pass 1: Requirement Ledger

Call `nanadraw_interpret_figure_request` and keep these categories separate:

- `explicit_requirements`: facts, entities, labels, panels, relationships, style instructions, and deliverables stated by the user
- `inferred_requirements`: conservative visual defaults needed to make a complete figure
- `uncertainties`: scientifically or visually important details that remain unresolved
- `forbidden_inferences`: causal directions, quantities, anatomy, timepoints, outcomes, or entities that the system must not invent
- `success_criteria`: observable conditions the rendered figure must satisfy

Never hide an inference inside an explicit requirement. A polished prompt is not a substitute for traceability.

## Pass 2: Scientific Reader Task

Write one sentence for each:

- scientific claim
- reader question
- evidence boundary
- take-home message

The reader question controls the visual narrative. If a reader cannot answer it from the figure without reading the full prompt, the design is incomplete.

## Pass 3: Content Inventory And Stable IDs

Inventory all panels, entities, relations, ordered steps, compartments, and exact labels before placing artwork.

Stable-ID rules:

- IDs describe scientific identity, not screen position.
- IDs persist through layout changes and local refinements.
- Every connector stores source and target IDs.
- Every generated or reused asset maps to one stable entity ID.
- Intermediate placeholders may be used for assembly, but placeholder graphics never survive into the final figure.

## Pass 4: Composition Tournament

Generate up to three materially different candidates. Do not produce three cosmetic variants of one layout.

Score each candidate on:

1. scientific claim visibility
2. topology-to-relation fit
3. reader-path clarity
4. focal hierarchy
5. scale-transition clarity
6. information density and whitespace
7. editable construction feasibility
8. connector and label collision risk

Select the highest-scoring candidate unless the user locked a layout. Record strengths, risks, and the selection rationale.

## Pass 5: Construction Contract

Build in this order:

1. canvas, panels, and whitespace corridors
2. primary focal region and major compartments
3. focal entities
4. supporting entities and reviewed assets
5. semantic connectors with verified endpoints
6. tiered live text
7. restrained material and color polish

Lock approved geometry before moving to the next stage. Do not regenerate a stable region to repair a local issue elsewhere.

## Pass 6: Artifact Sequence

Preserve these artifacts when the task is substantial:

1. `intent-contract.json`
2. `figure-spec.json`
3. `construction-plan.json`
4. `asset-shortlist.json`
5. `baseline-render.png`
6. `issue-register.json`
7. `revision-N.svg` or draw.io XML
8. `final-audit.json`
9. final editable source and preview

The files form an audit trail. The final image alone does not explain why a composition or scientific relationship was chosen.

## Pass 7: Rendered-Artifact Review

Review the actual render, not only the prompt or source code. Open issues under:

- science
- content
- geometry
- connectors
- typography
- style
- technical integrity

For each issue record region, stable object IDs, expected state, observed state, correction operation, and verification result.

## Pass 8: Region-Scoped Optimization

Use one operation family per iteration:

- reposition or resize
- connector reroute
- label hierarchy or collision repair
- asset identity or anatomy replacement
- palette or material normalization
- vector-edge cleanup

Render after every serious edit. Promote a revision only when the target region improves, neighboring regions do not regress, locked invariants remain true, and the editable artifact still passes validation. Keep the previous best immutable.

## Default Academic Style

When the user does not specify style, use:

- white or very light neutral background
- restrained multi-hue pastel palette
- precise medium-dark outlines
- one dominant focal mechanism
- balanced whitespace and meaningful scale transitions
- coherent membranes, tissues, cells, and engineered materials
- live readable text with three hierarchy levels
- solid arrows for established direction, T-bars for inhibition, dashed arrows for uncertainty

Avoid decorative card grids, forced boxes around every biological object, one-hue palettes, malformed pseudo-text, glossy rendering, heavy shadows, and connectors that terminate in empty space.


