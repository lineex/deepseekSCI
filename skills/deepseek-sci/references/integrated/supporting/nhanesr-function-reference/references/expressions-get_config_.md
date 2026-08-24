# Integrated supporting reference: nhanesr-function-reference/references/expressions-get_config_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-get_config_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `get_config_`

## `get_config_items` [exported]

```r
function () 
{
    if (do::cnOS()) {
        retrieve <- tmcn::toUTF8("<U+63D0><U+53D6><U+6570><U+636E>(<U+5E74>):")
        nolocal <- tmcn::toUTF8("<U+6CA1><U+6709><U+672C><U+5730><U+6570><U+636E><U+5E93>,<U+8BF7><U+4F7F><U+7528>config_items()<U+914D><U+7F6E><U+672C><U+5730><U+6570><U+636E><U+5E93>")
    }
    else {
        retrieve <- "retrieve items (year):"
        nolocal <- "No local database, please use config_items() to config"
    }
    temp <- config_temp()
    if (!dir.exists(temp)) 
        dir.create(temp, showWarnings = FALSE, recursive = TRUE)
    (nhs_items <- paste0(temp, "/items.nhanes"))
    if (!file.exists(nhs_items)) {
        message(nolocal)
    }
    else {
        utils::read.table(nhs_items)[, 1]
    }
}
```

## `get_config_path` [exported]

```r
function (slash = FALSE) 
{
    if (do::cnOS()) {
        msg <- tmcn::toUTF8("<U+6CA1><U+6709><U+914D><U+7F6E>NHANES<U+8DEF><U+5F84>  \n<U+5728><U+4F7F><U+7528>nhanesR<U+5305><U+4E4B><U+524D>,<U+8BF7><U+5148><U+5B8C><U+6210><U+4EE5><U+4E0B>3<U+9879><U+914D><U+7F6E>\n     1.<U+4F7F><U+7528>config_path()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+8DEF><U+5F84>\n     2.<U+4F7F><U+7528>config_years()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+5E74><U+4EFD>\n     3.<U+4F7F><U+7528>config_items()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+6587><U+4EF6><U+7C7B><U+578B>")
    }
    else {
        msg <- "No path of NHANES configed"
    }
    (temp <- config_temp())
    nhs.path <- paste0(temp, "/path.nhanes")
    if (!file.exists(nhs.path)) {
        message(msg)
    }
    else {
        path <- gsub(utils::read.table(nhs.path)[1, 1], pattern = "//", replacement = "/")
        if (slash) 
            path <- do::formal_dir(path, TRUE)
        path
    }
}
```

## `get_config_years` [exported]

```r
function (range = TRUE) 
{
    if (do::cnOS()) {
        nolocal <- tmcn::toUTF8("<U+6CA1><U+6709><U+672C><U+5730><U+6570><U+636E><U+5E93>,<U+8BF7><U+4F7F><U+7528>config_path()<U+914D><U+7F6E><U+672C><U+5730><U+6570><U+636E><U+5E93>")
    }
    else {
        nolocal <- "No local database, please use config_path() to config"
    }
    (temp <- config_temp())
    if (!dir.exists(temp)) 
        dir.create(temp, showWarnings = FALSE, recursive = TRUE)
    (nhs_years <- paste0(temp, "/years.nhanes"))
    if (!file.exists(nhs_years)) {
        message(nolocal)
    }
    else {
        years <- utils::read.table(nhs_years)[, 1]
        if (!range) 
            years <- do::Replace0(years, "-.*")
        years
    }
}
```


