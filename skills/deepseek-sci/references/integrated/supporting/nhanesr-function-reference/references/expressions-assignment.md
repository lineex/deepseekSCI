# Integrated supporting reference: nhanesr-function-reference/references/expressions-assignment.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-assignment.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `assignment`

## `append<-` [exported]

```r
function (x, value) 
{
    x <- c(x, value)
    x
}
```

## `col_rename<-` [exported]

```r
function (x, value) 
{
    col_rename(x, value)
}
```

## `digit2character<-` [exported]

```r
function (x, value) 
{
    digit2character(x, value)
}
```

## `digit2numeric<-` [exported]

```r
function (x, value) 
{
    digit2numeric(x, value)
}
```

## `drop_col<-` [exported]

```r
function (x, value) 
{
    rule <- value
    if (is.logical(rule)) {
        x[, !rule, drop = FALSE]
    }
    else if (is.numeric(rule)) {
        x[, -rule, drop = FALSE]
    }
    else if (is.character(rule)) {
        x[, !colnames(x) %in% rule, drop = FALSE]
    }
}
```

## `drop_row<-` [exported]

```r
function (x, value) 
{
    x <- drop_row(x, value)
    x
}
```

## `select_col<-` [exported]

```r
function (x, value) 
{
    rule <- value
    if (is.logical(rule)) {
        x[, rule, drop = FALSE]
    }
    else if (is.numeric(rule)) {
        x[, rule, drop = FALSE]
    }
    else if (is.character(rule)) {
        x[, rule, drop = FALSE]
    }
}
```

## `select_row<-` [exported]

```r
function (x, value) 
{
    x <- select_row(x, value)
    x
}
```

## `to_numeric<-` [exported]

```r
function (x, value) 
{
    if (is.data.frame(x)) {
        for (i in 1:length(value)) {
            xi <- tryCatch(as.numeric(x[, value[i]]), error = function(e) "error", warning = function(w) "error")
            if (all(xi %in% "error")) 
                (next)(i)
            x[, value[i]] <- xi
        }
    }
    else if (is.character(x)) {
        x <- as.numeric(x)
    }
    return(x)
}
```

## `yes1<-` [internal]

```r
function (x, value) 
{
    value <- set::and(colnames(x), value)
    if (length(value) == 0) 
        stop("colnames not exist")
    d1 <- x[, value, drop = FALSE]
    ck <- d1 == 1
    d1[ck] <- "yes"
    d1[!ck] <- "no"
    x[, value] <- d1
    x
}
```


