# Integrated supporting reference: nanadraw-biomedical-mcp/references/editable-vector-reconstruction.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/editable-vector-reconstruction.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Editable Vector Reconstruction

Read this reference when the user requests a pure-vector SVG, editable labels,
no embedded raster, no text background blocks, or a close reconstruction of a
raster biomedical figure.

## Non-negotiable invariants

- Preserve the full scientific geometry before editing text.
- Keep labels as live SVG `<text>` when the font is recognizable.
- Keep arrows, leader lines, membranes, receptors, particles, and cell contours
  continuous behind text regions.
- Use named SVG layers and stable IDs.
- Keep the previous best candidate until the replacement passes visual and
  structural validation.
- Treat pure-vector fidelity and pixel identity as separate deliverables.

## Reconstruction sequence

1. Lock the native canvas, exact labels, panel boundaries, colors, arrows, and
   regions that must remain unchanged.
2. Trace the complete reference image. Never erase rectangular text regions
   before tracing.
3. Sweep a narrow range of multi-scan parameters and render every candidate at
   the native reference size.
4. Select candidates using global metrics, non-text metrics, edge comparison,
   and 200-400% crops.
5. Remove old traced letters at the SVG subpath level.
6. Add live text in a separate named layer.
7. Rebuild only connectors that were pixel-connected to old glyphs.
8. Audit SVG purity, hide the text layer, and inspect the artwork-only render.
9. Export native and 4x PNG previews from the final SVG.

## Trace sweep

Use the skill-bundled script with the NanaDraw environment:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
$nanadraw = if ($env:NANADRAW_ROOT) { $env:NANADRAW_ROOT } else { (Get-Location).Path }
& "$nanadraw\.venv\Scripts\python.exe" `
  "$skill\scripts\inkscape_trace_sweep.py" `
  --reference REF.png `
  --output-dir TRACE_DIR `
  --scans 24 32 40 48 `
  --speckles 0 `
  --smooth-corners 0.3 `
  --optimize 0.08
```

Start with `smooth=false`, `stack=true`, `remove_background=false`, and
`speckles=0`. Tiny granules, receptors, dotted signals, and fibrin fibers are
easy to destroy with speckle removal or aggressive node optimization.

Do not select the highest scan count automatically. In antialiased scientific
art, 40-48 scans may improve color MAE while weakening edge metrics. Keep a
24-32 scan candidate as the stable-outline baseline.

## Editable text without missing vector geometry

Do not use visible white rectangles, transparent knockout rectangles, masks,
or clip paths to hide traced text. Those methods create rectangular gaps in the
underlying vector artwork even when the block itself looks transparent.

Create a JSON file containing padded text bounds:

```json
{
  "regions": [
    {"id": "title", "x": 100, "y": 40, "width": 240, "height": 48},
    {"id": "label-a", "x": 320, "y": 210, "width": 160, "height": 34}
  ]
}
```

Remove only closed subpaths fully contained in those bounds:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
$nanadraw = if ($env:NANADRAW_ROOT) { $env:NANADRAW_ROOT } else { (Get-Location).Path }
& "$nanadraw\.venv\Scripts\python.exe" `
  "$skill\scripts\editable_vector_refine.py" remove-text-subpaths `
  --input TRACE.svg `
  --regions text-regions.json `
  --output TRACE_TEXT_CLEAN.svg `
  --drop-page-background
```

This preserves any path that crosses a text boundary, including long arrows,
leader lines, membranes, and cell contours. If an old glyph is pixel-connected
to a short leader line, remove that connected subpath and rebuild the line as a
native SVG path in a `Native connector repairs` layer.

After subpath cleaning:

- Add labels in a `Live editable text` layer.
- Use the closest installed font, exact capitalization, and real multiline
  `<tspan>` elements.
- Set `letter-spacing:0`.
- Add a rectangle only when the reference visibly contains a semantic box.
- Keep ordinary text backgrounds transparent.

## Detail and outline hybrid

When a high-scan candidate gives the best color fidelity but a low-scan
candidate has cleaner dark edges, replace only the deepest tail path first:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
$nanadraw = if ($env:NANADRAW_ROOT) { $env:NANADRAW_ROOT } else { (Get-Location).Path }
& "$nanadraw\.venv\Scripts\python.exe" `
  "$skill\scripts\editable_vector_refine.py" hybridize `
  --detail HIGH_SCAN.svg `
  --outline LOW_SCAN.svg `
  --remove-detail-tail 1 `
  --append-outline-tail 1 `
  --output HYBRID.svg
```

Render and measure the hybrid before promoting it. Try a wider dark-tail swap
only if replacing the deepest path improves both visual edges and metrics.
Renumber final paths as `vector-color-path-01`, `vector-color-path-02`, and so
on.

## Quantitative selection

Compare native-size renders, not 4x previews:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
$nanadraw = if ($env:NANADRAW_ROOT) { $env:NANADRAW_ROOT } else { (Get-Location).Path }
& "$nanadraw\.venv\Scripts\python.exe" `
  "$skill\scripts\reference_fidelity.py" compare `
  --reference REF.png `
  --candidate CANDIDATE.png
```

Use metrics together:

- Global SSIM and MAE for overall fidelity.
- Body-only or non-text MAE for vector artwork quality.
- Edge or gradient error for contour stability.
- Panel crops for local biological structures.

A candidate is promoted only when metrics and visual inspection agree. A small
global improvement does not justify malformed receptors, missing particles,
broken fibers, or damaged arrows.

## Structural audit

Run the pure-vector audit:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
$nanadraw = if ($env:NANADRAW_ROOT) { $env:NANADRAW_ROOT } else { (Get-Location).Path }
& "$nanadraw\.venv\Scripts\python.exe" `
  "$skill\scripts\editable_vector_refine.py" audit `
  --svg FINAL.svg `
  --strict-pure-vector `
  --require-live-text
```

For a strict pure-vector delivery, require:

- `images=0`
- `embedded_rasters=0`
- `masks=0`
- `clip_paths=0`
- continuous `vector-color-path-*` IDs
- at least one live text node when editable labels are required
- only reference-grounded semantic rectangles

Hide `Live editable text` and inspect the artwork-only render. It must show
continuous lines and complete biological structures without rectangular holes.
Then show the text layer and inspect every label at native resolution and
200-400% zoom.

## Failure patterns

- Erasing text with rectangular white fills before tracing.
- Hiding traced text with transparent knockout rectangles.
- Removing the page background and assuming missing artwork is repaired.
- Converting every label to paths when live text is feasible.
- Keeping the imported raster inside an SVG labeled pure vector.
- Increasing scan count without measuring color and edge behavior.
- Replacing multiple dark layers before testing a one-layer hybrid.
- Reporting SSIM as proof of scientific or semantic correctness.

