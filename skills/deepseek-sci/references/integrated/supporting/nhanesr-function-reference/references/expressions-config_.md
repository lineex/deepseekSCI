# Integrated supporting reference: nhanesr-function-reference/references/expressions-config_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-config_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `config_`

## `config_items` [exported]

```r
function (items) 
{
    if (do::cnOS()) {
        setitems <- tmcn::toUTF8("<U+6210><U+529F><U+914D><U+7F6E><U+4EE5><U+4E0B><U+6570><U+636E>")
    }
    else {
        setitems <- "config items: "
    }
    if (missing(items)) 
        items <- c("Demographics", "Dietary", "Examination", "Laboratory", "LimitedAccess", "Questionnaire")
    names(items) <- NULL
    temp <- config_temp()
    if (!dir.exists(temp)) 
        dir.create(temp, showWarnings = FALSE, recursive = TRUE)
    (nhs_items <- paste0(temp, "/items.nhanes"))
    write.table(x = items, file = nhs_items, row.names = FALSE, col.names = FALSE, append = FALSE)
    message(setitems)
    items <- utils::read.table(nhs_items)[, 1]
    for (i in 1:length(items)) {
        if (i == 1) 
            cat("    ")
        cat(items[i], "")
        if (i%%1 == 0) 
            cat("\n    ")
    }
    cat("\n\n", nhs_items)
}
```

## `config_path` [exported]

```r
function (path) 
{
    if (!dir.exists(path)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+8DEF><U+5F84><U+4E0D><U+5B58><U+5728>"))
        if (!do::cnOS()) 
            stop("path not exsit")
    }
    if (do::cnOS()) {
        setpath <- tmcn::toUTF8("<U+8BBE><U+7F6E>NHANES<U+6570><U+636E><U+8DEF><U+5F84><U+81F3>: ")
    }
    else {
        setpath <- "set NHANES path to: "
    }
    temp <- config_temp()
    if (!dir.exists(temp)) 
        dir.create(temp, showWarnings = FALSE, recursive = TRUE)
    nhs_path <- paste0(temp, "/path.nhanes")
    path <- do::formal_dir(path)
    write.table(x = path, file = nhs_path, row.names = FALSE, col.names = FALSE)
    cat(setpath, path)
    cat("\n\n", nhs_path)
}
```

## `config_temp` [exported]

```r
function () 
{
    if (do::is.windows()) {
        temp <- paste0(do::upper.dir(do::upper.dir(list.files(.libPaths(), pattern = "nhanesR", full.names = TRUE))), 
            "nhanesR")
        temp <- do::last(temp[which.max(nchar(temp))])
        if (!dir.exists(temp)) {
            ck <- dir.create(temp, showWarnings = FALSE, recursive = TRUE)
            if (isFALSE(ck)) {
                temp <- "LOCAL_PATH"
                ck <- dir.create(temp, showWarnings = FALSE, recursive = TRUE)
            }
        }
        temp
    }
    else {
        temp <- sapply(.libPaths(), function(i) paste0(do::upper.dir(do::upper.dir(do::upper.dir(i))), 
            "nhanesR"))
        names(temp) <- NULL
        temp <- do::last(temp[which.max(nchar(temp))])
        if (!dir.exists(temp)) 
            dir.create(temp, showWarnings = FALSE, recursive = TRUE)
        temp
    }
}
```

## `config_years` [exported]

```r
function (cat = T) 
{
    if (do::cnOS()) {
        setyears <- tmcn::toUTF8("<U+6210><U+529F><U+914D><U+7F6E><U+4EE5><U+4E0B><U+5E74><U+4EFD>")
    }
    else {
        setyears <- "config years: "
    }
    years <- c("1999-2000", "2001-2002", "2003-2004", "2005-2006", "2007-2008", "2009-2010", "2011-2012", 
        "2013-2014", "2015-2016", "2017-2018", "2019-2020", "2021-2023")
    temp <- config_temp()
    if (!dir.exists(temp)) 
        dir.create(temp, showWarnings = FALSE, recursive = TRUE)
    (nhs_years <- paste0(temp, "/years.nhanes"))
    write.table(x = years, file = nhs_years, row.names = FALSE, col.names = FALSE, append = FALSE)
    if (cat) 
        message(setyears)
    years <- utils::read.table(nhs_years)[, 1]
    for (i in 1:length(years)) {
        if (i == 1) 
            cat("    ")
        if (cat) 
            cat(years[i], "")
        if (i%%3 == 0) 
            cat("\n    ")
    }
    if (cat) 
        cat("\n\n", nhs_years)
}
```


