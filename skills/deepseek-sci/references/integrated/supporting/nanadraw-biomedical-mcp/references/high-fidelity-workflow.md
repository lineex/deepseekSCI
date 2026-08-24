# Integrated supporting reference: nanadraw-biomedical-mcp/references/high-fidelity-workflow.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/high-fidelity-workflow.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# High-Fidelity Biomedical Figure Workflow

Read this reference for reference-guided redraws, iterative visual polishing, and exact-appearance requests.

## Contents

1. Fidelity contract
2. Reference analysis
3. Iteration strategy
4. Raster-to-vector strategy
5. Quantitative validation
6. Deliverable policy
7. Failure modes
8. Pure-vector audit

## 1. Fidelity contract

Freeze these values before the first revision:

- native canvas dimensions and aspect ratio
- panel count, panel boundaries, and reading order
- exact visible text, including symbols, subscripts, and capitalization
- scientific entities, relations, arrows, compartments, and outcomes
- approved colors, line weights, corner treatment, and visual density
- regions that must not change
- required output formats and editability level

Treat each frozen value as an invariant. Re-check all invariants after every revision.

## 2. Reference analysis

Inspect the source at native resolution and at 200-400% zoom. Record:

- dominant and accent colors sampled from the source
- background color and transparency behavior
- typography family, weight, size hierarchy, and alignment
- stroke widths, dash patterns, arrowheads, and corner radii
- repeated icon grammar and membrane/receptor details
- panel spacing, whitespace, and clipping behavior
- antialiasing, gradients, texture, and edge softness

Do not describe a reference only as "Nature style." Convert the visual evidence into explicit constraints.

## 3. Iteration strategy

Use this order:

1. Correct scientific content.
2. Correct panel topology and major geometry.
3. Correct labels and typography.
4. Correct palette and line language.
5. Correct local contours and spacing.
6. Apply micro-polish and export tuning.

Keep a baseline and version every candidate. Change one variable per iteration whenever possible. Compare against the previous best, not only against the immediately preceding candidate.

For multi-panel figures, compute panel-wise metrics and inspect panel crops. A globally weaker candidate can still be the best source for one panel. Assemble panel-specific winners only when boundaries fall in blank gutters or can be clipped without visible seams.

## 4. Raster-to-vector strategy

Prefer a true redraw from native shapes and editable text when source assets or sufficient time are available. Use tracing only as a reconstruction fallback.

For pure-vector SVG, editable labels, or removal of traced text, read
[editable-vector-reconstruction.md](editable-vector-reconstruction.md) and follow its
subpath-level workflow. Preserve complete geometry before cleaning text. Never
delete rectangular text regions or use transparent knockout rectangles; both
produce missing vector artwork behind labels.

### Inkscape multi-scan tracing

The CLI action accepts:

```text
object-trace:{scans},{smooth},{stack},{remove_background},{speckles},{smooth_corners},{optimize}
```

Start with a narrow scan sweep for a muted scientific illustration:

```text
scans=24, 32, 40, or 48
smooth=false
stack=true
remove_background=false
speckles=0
smooth_corners=0.24 to 0.4
optimize=0.05 to 0.10
```

Do not assume that more scans are better. Antialiased scientific figures can score worse at 48-128 scans because edge pixels become extra color paths. Sweep a narrow range, render every candidate at the reference dimensions, and rank the rendered result.

Disable or reduce speckle removal when tiny receptors, dotted fibers, dashed borders, or small labels disappear. Increase corner smoothing only after checking that arrowheads and receptor shapes remain intact.

When high-scan color fidelity wins but low-scan contours are cleaner, test a
one-path hybrid: use the high-scan color stack and replace only its deepest
outline path with the low-scan deepest path. Promote the hybrid only after
native-size metrics and enlarged crops both improve.

### Supersampled export

For smoother presentation PNGs, render vector artwork at 4x and downsample with Lanczos. Keep the native render for exact comparison. Report round-trip metrics separately because a high-resolution export is not pixel-comparable until normalized.

### Layered exact delivery

If the user requires exact appearance from a raster-only source, create a layered SVG:

- place the editable vector reconstruction in a bottom layer
- place the lossless reference in a top layer
- label both layers clearly
- keep the pure-vector SVG as a separate artifact

This is an explicit hybrid, not a claim that the raster was converted into exact editable paths.

## 5. Quantitative validation

Use the bundled script to calculate:

- `SHA-256`: proves byte identity for copied or embedded reference data
- `SSIM`: structural similarity after dimensions are normalized
- `MAE`: mean absolute channel error
- `PSNR`: signal-to-noise summary
- `exact_pixel_percent`: percentage of RGB pixels that match exactly

Interpret metrics together with visual inspection. Metrics can reward blur, miss malformed scientific symbols, or hide a local panel failure inside a large white background.

Only claim complete pixel identity when:

- dimensions match
- `SSIM=1.0`
- `MAE=0`
- `exact_pixel_percent=100`

For embedded reference layers, also verify that the decoded embedded bytes have the same SHA-256 as the source.

## 6. Deliverable policy

For high-fidelity reconstruction, prefer this bundle:

- native PNG: exact or primary visual artifact
- 4x PNG: presentation artifact with smoother edges
- layered SVG: exact appearance plus editable vector fallback
- pure-vector SVG: honest editable approximation
- draw.io XML: only when the structure is meaningfully editable in draw.io

Use stable, versioned filenames. Preserve the previous best until validation completes.

## 7. Failure modes

- Re-generating the full image to fix one local issue and damaging approved regions.
- Treating a journal name as a complete style specification.
- Increasing trace color count without measuring the result.
- Converting labels into malformed traced glyphs when editable text is required.
- Reporting a 4x image metric without first normalizing dimensions.
- Calling an embedded raster a pure vector.
- Claiming 99.9% or 100% based on visual impression alone.
- Optimizing SSIM while missing an arrow direction, label, receptor, or panel boundary.
- Deleting rectangular text regions before tracing and removing underlying lines or contours.
- Using white or transparent text knockout blocks and mistaking them for complete vector artwork.
- Leaving old text as traced paths while claiming that labels are fully editable.

## 8. Pure-vector audit

Before delivering editable SVG:

1. Require zero `<image>` nodes and embedded raster payloads.
2. For strict reconstruction, require zero `<mask>` and `<clipPath>` nodes.
3. Keep artwork, connector repairs, and live text in separate named layers.
4. Renumber color paths continuously as `vector-color-path-01...N`.
5. Hide the live-text layer and render the artwork alone. Confirm that arrows,
   membranes, cells, particles, and leader lines remain continuous behind every
   label.
6. Show live text and verify exact wording, line breaks, font, alignment, and
   transparent ordinary text backgrounds.

