# Integrated supporting reference: nanadraw-biomedical-mcp/references/biorender-learn-derived-figure-rules.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/biorender-learn-derived-figure-rules.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# BioRender Learn Derived Figure Rules

Use this reference for figure composition, visual hierarchy, path/flow diagrams,
graphical abstracts, protocol figures, posters, grant figures, label placement,
color systems, scale transitions, or figure-makeover requests.

## Evidence Scope

The local corpus at `references/biorender-learn-overviews-2026-07-16.json` was
collected from the public BioRender Learning Hub on 2026-07-16. The page exposed
71 accessible detail pages while its visible counter said 52 videos. Of those
detail pages, 44 exposed a visible `Overview` section with a combined 545,224
characters; 3 lacked `Overview` but exposed a usable `Summary`; 24 currently
exposed neither teaching-text field and remain as sourced metadata records. This
document contains distilled, reusable rules rather than copied teaching text.

Query the corpus rather than loading it wholesale:

```powershell
$skill = "$env:USERPROFILE\.codex\skills\nanadraw-biomedical-mcp"
LOCAL_PATH `
  "$skill\scripts\biorender_learn_lookup.py" --stats

LOCAL_PATH `
  "$skill\scripts\biorender_learn_lookup.py" `
  --query "biological pathways" --query contrast --limit 6
```

## 1. Build A Figure Blueprint Before Drawing

For every non-trivial figure, state these fields in the FigureSpec or generation
brief before placing icons:

- `take_home_message`: one sentence that a viewer can understand at thumbnail
  scale.
- `reader_path`: `left_to_right`, `top_to_bottom`, `z_path`, `radial`,
  `cyclical`, or a named comparison layout.
- `entry_point` and `focal_endpoint`: the first object a reader should see and
  the scientific consequence or decision they should reach.
- `primary_focal_region`: one visually dominant region only; define what is
  deliberately quiet.
- `scale_plan`: macro, tissue, cell, organelle, molecule, and the permitted
  transitions between them.
- `arrow_grammar`: one legend or explicit definitions for activation,
  inhibition, movement, transformation, correlation, uncertainty, and future or
  past events.
- `label_tiers`: panel title, step title, object label, and optional annotation.

Reject a generation brief that names many objects but does not specify a reader
path, hierarchy, or scale plan.

## 2. Select The Correct Topology

| Scientific job | Preferred composition | Required constraints |
| --- | --- | --- |
| Ordered protocol or workflow | left-to-right or top-to-bottom sequence | Number steps; preserve one direction; create equal step spacing. |
| Biological pathway | unidirectional path or deliberately planned Z path | Avoid spontaneous reversals and crossing arrows; group each causal unit. |
| Feedback, plasmid, recurrent process | closed circular loop | Use circular arrows only for a genuine cycle; label the entry or phase ordering. |
| Multiscale mechanism | macro-to-micro progression with insets | Use explicit zoom frames or connector lines; retain orientation across scales. |
| Comparison or intervention study | aligned parallel panels or lanes | Keep baseline, intervention, time point, and outcome in consistent positions. |
| Graphical abstract | one central causal claim with limited supporting scenes | Prefer an uncluttered reading path over encyclopedic coverage. |
| Grant figure | hypothesis-to-test-to-readout chain | Make the proposed causal logic and expected outcome visible before methods detail. |
| Poster or presentation | scanable blocks with a dominant conclusion | Use large section hierarchy, low local density, and distance-readable labels. |

Never use a circular layout merely as decoration. Never use a pyramid, radial, or
wheel topology when it hides the requested temporal or causal order.

## 3. Compose With Flow, Proximity, And Visual Hallways

1. Choose one main reading direction. Do not make arrows reverse direction unless
   the reversal itself carries meaning.
2. Group objects that form one concept into a compact cluster. Use smaller gaps
   within a cluster than between clusters.
3. Align related objects to shared baselines, centers, or grid tracks. Use equal
   inter-panel and inter-step spacing.
4. Preserve empty corridors between concept groups. A clear corridor is an active
   compositional element that separates ideas and protects arrow readability.
5. For a dense mechanism, simplify before shrinking. Retain entities that change
   the causal claim; move nice-to-have detail to an inset or remove it.
6. In a multi-panel figure, use panel frames only when they clarify distinct
   states. Do not box every object.

For a reference-guided revision, measure the original group bounding boxes and
gaps before changing icons. A better icon does not compensate for a broken reader
path.

## 4. Establish Hierarchy And Focal Control

- Give the take-home mechanism the greatest combination of scale, contrast, and
  centrality. Do not maximize all three for multiple unrelated objects.
- Use restrained context icons at low contrast, lower opacity, or smaller scale.
- Use bold text and numbered steps for sequence hierarchy; use color only as a
  second cue.
- Treat a callout as a deliberate microscope-like focus frame. Link it to its
  source region, state the scale jump when relevant, and prevent it from looking
  like an unrelated panel.
- During review, blur or thumbnail the figure. The entry point, focal region,
  sequence, and final result must still be identifiable.

## 5. Use Color As Scientific Encoding

- Define the semantic palette before drawing: biological compartments, cell
  states, treatment/control groups, and highlighted causal agents.
- Reserve high saturation and high value contrast for the primary focal region
  and a small number of scientifically meaningful exceptions.
- Keep background and contextual material soft, especially when labels or
  molecular overlays sit above it.
- Run a grayscale check. Labels, receptor domains, arrows, and different groups
  must remain separable without hue alone.
- Test color-blind separability and use redundant cues such as outline, shape,
  texture, or annotation for critical comparisons.
- Use opacity to subordinate a background object or reveal an overlay. Inspect
  every overlap after changing opacity because the background changes the
  perceived color.
- Keep one lighting and highlight model across native shapes, Bioicons, and
  generated components.

## 6. Apply A Fixed Connector Grammar

Define and reuse one connector system:

| Connector | Default meaning | Drawing requirement |
| --- | --- | --- |
| Solid arrow | directed causal action, transport, or ordered transition | Tail and head must touch their intended entities. |
| T-bar | inhibition | Perpendicular terminal touches the inhibited entity. |
| Dashed arrow or line | inferred, projected, historical/future, optional, or indirect relation | Explain its special meaning once in a legend or nearby label. |
| Dotted outline | region, crop, boundary, or provisional area | Do not use as an ordinary connector. |
| Circular arrow | feedback, recurrence, or a true cycle | Keep the loop closed and phase order legible. |
| Leader line | label attachment | Do not cross another leader; terminate on the named structure. |

Normalize line weight, arrowhead size, corner radius, dash pattern, and endpoint
clearance across a figure. Connector crossings require rerouting, an inset, or a
reordered layout rather than an unexplained overpass.

## 7. Manage Scale And Zoom

- Show macro-to-micro transitions through a bounded inset, crop, or transparent
  continuation, not a sudden unrelated magnification.
- Keep object orientation stable across a scale jump unless rotation is labelled
  or scientifically necessary.
- Use a circular crop for a microscopy-field or focal viewport; use a rectangular
  crop for a structural section, panel crop, or composited component.
- Do not use decorative crop frames. Every crop needs a scale, locality, or
  attention-management purpose.
- For a mechanism spanning organism, tissue, cell, and molecule, make each scale
  transition explicit and limit the number of jumps in one reader path.

## 8. Labels And Typography

- Keep labels in a consistent external lane or a deliberate in-object label zone.
- Distribute labels evenly. Avoid stacked leader-line tangles and cramped labels
  at one side while the opposite side is empty.
- Preserve exact biological notation, including superscripts, subscripts,
  Greek symbols, hyphenation, and gene/protein capitalization.
- Do not use a white rectangle behind labels to hide incomplete artwork. Build
  complete vector geometry behind text and use contrast-aware placement.
- Let typography establish tiers: strong panel/step titles, smaller object labels,
  smallest explanatory annotations. Do not use hero-scale type inside dense panels.

## 9. Reuse And Adapt Assets Deliberately

- Start from a canonical asset silhouette, then use contour adaptation only when
  it keeps the biological identity intact.
- Use editable custom shapes for missing outlines such as tumor boundaries,
  highlighted anatomy, or modular composite proteins. Keep control points and
  meaningful path IDs stable.
- Use crop-based assembly only when the combined structure is scientifically
  interpretable. Inspect cut edges at 200-400% zoom.
- Lock approved background or contextual layers before editing foreground
  mechanism elements. This preserves panel geometry and prevents accidental
  drift.
- Select repeated object families together and normalize their palette, scale,
  stroke weight, and label treatment in one pass.

## 10. Add A Composition Review Gate

Before final delivery, score each item as pass/fail and correct all failures:

- `message`: A reader can state the claim without reading every label.
- `reading_path`: Start, order, and endpoint remain obvious at thumbnail size.
- `hierarchy`: One primary focal region and quiet contextual regions are evident.
- `topology`: Layout matches the scientific relation: sequence, cycle, scale,
  comparison, or hierarchy.
- `grouping`: Within-concept gaps are smaller than between-concept gaps.
- `connectors`: Arrow semantics and endpoints are correct; no gratuitous crossings.
- `scale`: Insets and magnification transitions are explicit and oriented.
- `color`: Critical differences survive grayscale and color-blind review.
- `labels`: Text is exact, readable, evenly distributed, and not obscuring art.
- `density`: Detail supports the claim rather than turning the figure into a map.

## Evidence Anchors

Use the local corpus to trace or refine a rule. High-yield sources include:

- `Tips for Illustrating Biological Pathways`: flow, proximity, scale, color,
  contrast, and connector consistency.
- `4 ways to align objects`: grids, guides, alignment, and spacing discipline.
- `How to label a diagram`: label distribution and leader-line clarity.
- `Creating 'dashed' or 'dotted' lines` and `Draw cycles with circular arrows`:
  relationship-specific line grammar.
- `Designing a Winning Poster & Live Poster Makeover`, `Figure Makeover - Live
  Design Feedback!`, and `Back-to-Conference! Design Tips for Posters`:
  hierarchy, density, scanability, and revision.
- `Designing Your Grant for the Reviewer`, `BioRender Top Grant Tips`, and
  `Panel Session: Why Strong Visuals Secure Grants`: reviewer-first narrative.
- `Anatomy of a Figure: From BioRender Templates to Graphical Abstracts`:
  graphical-abstract structure and visual storytelling.
- `Using circle crop`, `Using custom crop`, and `Using rectangle crop`: attention
  management and structural assembly.

