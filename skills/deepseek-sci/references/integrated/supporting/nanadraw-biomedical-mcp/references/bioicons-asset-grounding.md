# Integrated supporting reference: nanadraw-biomedical-mcp/references/bioicons-asset-grounding.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/bioicons-asset-grounding.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Bioicons And Local Asset Grounding

Read this reference when a biomedical figure contains canonical cells, tissues,
microorganisms, organs, instruments, or when a reference-guided redraw needs
more organic and biologically recognizable contours.

## Contents

1. Search order
2. Query expansion
3. Candidate decision
4. Reference-guided adaptation
5. Pure-vector and license rules
6. Validation gates

## 1. Search order

Use this order once per object family:

1. Call `nanadraw_search_bioicons` with the user's scientific term.
2. Retry common aliases and Bioicons filename forms.
3. If MCP search returns no useful candidate, run
   `scripts/bioicons_asset_grounder.py` against NanaDraw's local
   `backend/static/bioicons/metadata.json`.
4. Route the entity across the full category map in
   `references/bioicons-library-map.md`; do not stop after one exact-name or
   one-category miss.
5. Generate `--preview-dir`, then inspect the top 3-6 SVG candidates and their
   complete contours at approximately final size. Do not select from filenames
   or scores alone.
6. If the library lacks an anatomically acceptable candidate after the routed
   semantic search, call NanaDraw's standalone asset generator for three
   isolated variants. Pass the working image model explicitly when status and
   endpoint defaults differ.
7. Record selected and rejected IDs, license, intended use, and reason in the
   FigureSpec `assets` notes or generation brief.

Do not search the full library separately for every repeated instance. Search
once for an object family, choose one visual grammar, then reuse it consistently.

## 2. Query expansion

MCP search can miss filenames containing hyphens or underscores. Expand terms
before concluding that no asset exists:

| Requested object | Search aliases |
| --- | --- |
| macrophage / MP | `macrophage`, `monocyte`, `phagocyte` |
| dendritic cell / DC | `dendritic-cell`, `dendritic_cell`, `antigen presenting cell` |
| CTL / T cell | `t-lymphocyte`, `T lymphocyte`, `lymphocyte` |
| CAR T cell | search `t-lymphocyte` and `receptor` separately, then compose |
| MDSC | `myeloid`, `monocyte`, `neutrophil`, `suppressor cell` |
| tumor cell | `tumor`, `cancer_cell`, `cancerous-cell` |
| epithelium / IEC | `epithelial_cell`, `epithelium`, `epithel`, `columnar` |
| fungi | `fungal`, `yeast`, `candida`, `budding yeast` |
| red blood cell | `erythrocyte`, `redbloodcell`, `red blood cell` |
| endothelial cell | `capillary`, `capillaries`, `Continuous_capillary`, `endothelium` |
| blood vessel | `artery`, `vein`, `capillary`, `blood-flow`, `bloodstream` |
| mouse | `Mouse`, `mouse-gray`, `mouse-small`; exclude embryo/head/organ variants for a whole animal |

Use the helper for fuzzy expansion:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
LOCAL_PATH `
  "$skill\scripts\bioicons_asset_grounder.py" `
  --root LOCAL_PATH `
  --query macrophage `
  --query "dendritic cell" `
  --query CTL `
  --query "tumor cell" `
  --limit 6 `
  --output ASSET_SHORTLIST.json `
  --preview-dir ASSET_PREVIEWS
```

## 3. Candidate decision

Classify every shortlisted asset into exactly one mode:

- `direct_reuse`: Anatomy, silhouette, perspective, and line language already
  match the figure. Recolor only when the license and SVG structure allow it.
- `contour_adaptation`: The biological silhouette is useful but highlights,
  nucleus, palette, or detail density conflict with the reference. Retain or
  simplify the contour and rebuild the interior in the figure's visual grammar.
- `visual_grammar_reference`: Use the candidate only to understand protrusion
  count, membrane irregularity, nucleus proportion, or canonical anatomy. Draw a
  new native shape.
- `reject`: The icon is semantically related but visually incompatible.

Rank candidates using this order:

1. Correct biological identity and anatomy.
2. Silhouette agreement with the reference or selected journal grammar.
3. Perspective and orientation.
4. Detail density and ability to remain legible at final size.
5. Palette adaptability and stroke compatibility.
6. License and attribution feasibility.

Never force an asset into the figure merely because it was found. A mismatched
Bioicon is weaker than a clean native vector built from the correct grammar.
Likewise, reject generated candidates that use the wrong species silhouette,
cartoon anatomy, malformed receptor architecture, or decorative details that
conflict with the scientific role.

For generated teacher assets, require a single isolated subject, transparent or
pure-white background, no text, and a prompt naming species- or cell-defining
anatomy. Generate three candidates, inspect them at native size, and record the
selected candidate and rejection reasons. For pure-vector delivery, trace or
redraw the selected teacher; do not embed its PNG.

## 4. Reference-guided adaptation

For a supplied reference image:

1. Freeze the native aspect ratio, panel boundaries, object bounding boxes, and
   abundance differences before choosing icons.
2. Compare candidate silhouettes at approximately the final rendered size.
3. Preserve the reference's object count, overlap, scale, and orientation. The
   asset supplies anatomy, not layout authority.
4. Normalize selected assets to one palette, outline weight, highlight model,
   nucleus style, and opacity system.
5. For repeated cells, keep one canonical symbol and vary only scale, rotation,
   and biologically meaningful state.
6. When a candidate has attractive organic contours but incompatible internal
   rendering, use `contour_adaptation`; do not mix its full rendering with flat
   native cells.

For before/after validation, render at the reference's native dimensions and
compare with `reference_fidelity.py`. Promote the revision only when the target
region improves visually and global geometry, labels, and adjacent regions do
not regress.

## 5. Pure-vector and license rules

- Keep pure-vector SVG self-contained. Inline allowed vector geometry; do not
  use `<image>`, external file URLs, or rasterized icon previews.
- Remove imported `clipPath` or `mask` dependencies only by reconstructing the
  same complete geometry. Do not create missing edges.
- Keep live text separate from imported or adapted artwork.
- Add a `<metadata>` entry or adjacent attribution manifest containing asset ID,
  author, license, and source URL for every reused or adapted icon.
- Preserve attribution requirements for CC BY and share-alike requirements for
  CC BY-SA. Prefer CC0 when two candidates are otherwise equal.
- Do not describe an adapted Bioicon as an original native primitive.

Recommended SVG metadata form:

```xml
<metadata>
  Asset: Blood_Immunology__Servier__macrophage;
  author: Servier; license: CC BY 3.0; source: https://bioicons.com/
</metadata>
```

## 6. Validation gates

Before promoting an asset-grounded revision, require:

- `semantic`: Every reused silhouette represents the stated biomedical object.
- `style`: No object looks imported from a different illustration system.
- `geometry`: Counts, positions, overlaps, and panel-specific abundance match the
  locked blueprint or reference.
- `license`: Every selected external-library asset has recorded provenance.
- `vector`: Pure-vector output has zero raster payloads and external image links.
- `comparison`: Native-size reference metrics and enlarged crops were checked;
  local gains did not damage neighboring regions.

