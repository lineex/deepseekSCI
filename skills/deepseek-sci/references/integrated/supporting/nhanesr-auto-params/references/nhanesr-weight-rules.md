# Integrated supporting reference: nhanesr-auto-params/references/nhanesr-weight-rules.md

> Embedded source: `embedded-source/nhanesr-auto-params/references/nhanesr-weight-rules.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# NHANES Weight Rules

Use this reference whenever the user asks about NHANES weights, survey design, or merged-cycle analysis.

## Base-weight families

- `WTINT2YR`, `WTINT4YR`, `WTINTPRP`: interview weights.
- `WTMEC2YR`, `WTMEC4YR`, `WTMECPRP`: MEC exam weights.
- Never mix interview and MEC base weights in one model.
- Choose the base family first from the most restrictive variable in the analysis.

## Cycle scaling

- Regular 2-year cycles: use `1 / n`, where `n` is the number of merged cycles.
- Non-consecutive regular cycles: still use `1 / n` over the included cycles only.
- 1999-2002: treat as a 4-year cycle and scale by `4 / total_years`.
- 2017-March 2020: treat as a 3.2-year pre-pandemic cycle and scale by `3.2 / total_years`.
- Keep `SDMVSTRA` and `SDMVPSU` unchanged when stacking cycles.

## Practical formulas

- For `n` regular 2-year cycles, `new_weight = base_weight * (2 / (2n)) = base_weight / n`.
- For `1999-2002 + 2003-2004`, `new_weight = base_weight * (4 / 6)` for 1999-2002 and `base_weight * (2 / 6)` for 2003-2004.
- For `2015-2016 + 2017-March 2020`, `new_weight = base_weight * (2 / 5.2)` and `base_weight * (3.2 / 5.2)`.

## Output rule

When the user wants a ready-to-run expression, generate a `dplyr::case_when()` mutation that maps each cycle label to its scaled weight.

## Tooling

- `scripts/nhanesr_weights.R plan ...` prints the scaled weights for a cycle list.
- `scripts/nhanesr_weights.R code ...` prints a ready-to-run `dplyr::mutate()` expression.

