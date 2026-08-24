# Integrated supporting reference: nanadraw-biomedical-mcp/references/post-generation-scientific-audit.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/post-generation-scientific-audit.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Post-Generation Scientific And Spatial Audit

Read this reference after rendering every non-trivial biomedical figure and
before calling any artifact final.

## Contents

1. Audit inputs
2. Scientific audit
3. Spatial and connector audit
4. Typography and rendering audit
5. Correction loop
6. Scientific explanation
7. Delivery gate

## 1. Audit inputs

Audit the rendered artifact, not only the prompt or XML. Keep these inputs side
by side:

- validated `NanaDrawFigureSpec`
- generation brief and selected asset manifest
- native-resolution render
- editable SVG or draw.io source
- supplied reference image, when present

Inspect the whole figure at native size, then inspect every panel and dense
region at 200-400%. Hide live text once and verify that underlying artwork and
connectors remain complete.

## 2. Scientific audit

Check every entity and relation against the spec and scientific message:

- entity identity, phenotype, state, localization, and abundance direction
- compartment placement, membrane sidedness, tissue orientation, and temporal
  order
- causal direction, activation, inhibition, transport, secretion, killing, and
  blocked-pathway semantics
- panel-specific differences and control-versus-disease comparisons
- exact labels, gene/protein capitalization, cytokine names, arrows, subscripts,
  and increase/decrease symbols
- absence of invented pathways, unsupported molecules, or causal claims that
  are only correlations
- immediate recognizability of canonical animal models, cell classes, organs,
  instruments, and receptors at final rendered size

For animal models, verify species-defining anatomy rather than accepting a
generic silhouette. A laboratory mouse should show an appropriate pointed
muzzle, paired rounded ears, eye position, arched back, abdomen, limbs/paws, and
long thin tail. Treat an unrecognizable or wrong-species silhouette as a
scientific error.

For abundance symbols such as `↑↑↑`, verify that the drawing shows a visibly
larger population. Treat illustrative cell counts as schematic unless the source
defines quantitative counts.

## 3. Spatial and connector audit

Check object geometry independently from scientific semantics:

- no object is in the wrong panel, compartment, layer, or z-order
- paired panels align equivalent anatomical boundaries
- labels sit near their targets without covering nuclei, receptors, or arrows
- arrows start and end at the intended objects; arrowheads do not float
- inhibition bars touch the inhibited target and do not look like activation
- dashed or blocked connectors remain visually distinct from active pathways
- leader lines terminate at the correct cell cluster
- repeated objects preserve intended count, spacing, overlap, scale, and
  orientation
- no connector crosses a label or unrelated object when a clear route exists
- no text, marker, cell, or panel title is clipped by the canvas

Treat a scientifically correct arrow with a wrong endpoint as a scientific
error, not a cosmetic issue.

## 4. Typography and rendering audit

Require:

- live, readable labels with transparent ordinary text backgrounds
- no pseudo-text baked into generated components
- no duplicated labels, spelling drift, or unexplained abbreviations
- coherent palette, line weight, membrane grammar, nucleus style, and icon
  density across native shapes and Bioicons
- smooth vector edges at high zoom and no missing geometry behind text
- stable native, high-resolution, and publication exports

## 5. Correction loop

Create an issue register with one row per defect:

- category: `science`, `content`, `geometry`, `connectors`, `typography`,
  `rendering`, or `technical`
- severity: `critical`, `major`, or `minor`
- region or panel
- finding
- correction
- evidence after correction

Repair in this order:

1. scientific identity and causal direction
2. missing or unsupported content
3. wrong panel, compartment, alignment, or connector endpoint
4. labels and typography
5. icon integration and visual polish
6. export and metadata defects

Change one issue family or region at a time. Re-render after every correction,
re-check the edited region and its neighbors, then re-run all global invariants.
Keep the previous best artifact until the corrected candidate passes.

## 6. Scientific explanation

Write the figure explanation from the corrected final render, not from the
initial prompt. Include:

- one-sentence take-home message
- panel-by-panel explanation
- explicit causal or sequential chain for mechanism and workflow figures
- arrow grammar: activation, inhibition, dashed/blocked, transport, or leader
  line meanings
- scope notes distinguishing schematic abundance from measured quantities
- caveats for uncertain, indirect, or correlation-only relationships

Every explanatory claim must have a basis in the validated spec, supplied
reference, user-provided evidence, or an explicitly cited scientific source.
Do not use the caption to compensate for a wrong or ambiguous drawing; fix the
drawing first.

## 7. Delivery gate

Use `scripts/figure_audit_gate.py` to create and check the audit report:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
LOCAL_PATH `
  "$skill\scripts\figure_audit_gate.py" template `
  --figure-class mechanism_pathway `
  --output FIGURE_AUDIT.json
```

```powershell
LOCAL_PATH `
  "$skill\scripts\figure_audit_gate.py" check `
  --report FIGURE_AUDIT.json `
  --require-mechanism-explanation
```

Do not deliver while the gate reports an open issue, missing audit category,
missing evidence, or incomplete scientific explanation.

