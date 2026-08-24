# Integrated supporting reference: nanadraw-biomedical-mcp/references/prompt-compilation-workflow.md

> Embedded source: `embedded-source/nanadraw-biomedical-mcp/references/prompt-compilation-workflow.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Prompt Compilation Workflow

Use this workflow for prose ideas, paper sections, captions, and long image prompts before drafting the final FigureSpec.

## Provenance

The layer separation was informed by [BAIKEMARK/happy-figure-skill](https://github.com/BAIKEMARK/happy-figure-skill), reviewed at commit `6292597250ed874d65756d13a492f6eefe07fb65` under CC BY-NC-SA 4.0. NanaDraw uses an independently written implementation and does not copy that project's prompt masters, reference prose, or extraction code.

## Compilation Layers

Keep these decisions independent:

1. `domain_master`: controls scientific objects, compartments, relation semantics, and domain failure checks.
2. `figure_type_master`: controls topology, panels, reader path, and connector grammar.
3. `visual_treatment`: controls publication density and finish without changing the scientific structure.
4. `target_renderer`: controls editability, component generation, and text handling.
5. `instruction_language`: controls the language used to instruct the renderer.
6. `visible_text_language`: controls the language actually shown in the figure.
7. `visible_text_whitelist`: controls every label permitted to render.

Apply this priority order when layers conflict:

`scientific facts > explicit user requirements > domain master > figure-type master > renderer constraints > visual treatment`

## Document Inputs

For a local PDF, DOCX, LaTeX, Markdown, or text file, call `nanadraw_extract_research_document` before interpretation. Select the candidate context that contains the mechanism, workflow, comparison, or graphical-abstract message. Keep extraction warnings with the artifact and do not treat a parser guess as a scientific claim.

## Visible Text Contract

- Build the whitelist from exact user labels, panel titles, entity names, and required process labels.
- Do not render internal words such as `ZONE`, `PANEL`, `LAYOUT CONFIGURATION`, `CONNECTIONS`, field names, or placeholder text.
- Use live SVG/draw.io text when editability is required.
- The renderer may omit a secondary label only after the FigureSpec is updated and revalidated; it may not improvise replacements.

## Quality Gate

Before generation, require:

- no unresolved template marker
- every whitelisted label appears in the compiled brief
- an explicit evidence boundary
- renderer alignment with the requested deliverable
- explicit prohibition of unlisted visible text

After generation, continue with the rendered-artifact audit. Prompt quality is an input gate, not evidence that the finished figure is correct.

