# Integrated supporting reference: nhanesr-function-reference/references/expressions-drug_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-drug_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `drug_`

## `drug_anti.Diabetic` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("antidiabetic", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, 
        drugname = drugname, fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, 
        other.code = other.code, no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, 
        join = join, Year = Year)
}
```

## `drug_anti.Hyperlipidemic` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("antiHyperlipidemic", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, 
        drugname = drugname, fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, 
        other.code = other.code, no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, 
        join = join, Year = Year)
}
```

## `drug_anti.Hypertensive` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("antihypertensive|angiotensin converting enzyme|calcium channel blocking agents|agents for hypertensive emergencies|adrenergic blocking agents|beta blockers|diuretics|loop diuretics|renin inhibitors|angiotensin ii inhibitors|aldosterone receptor antagonists", 
        data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, drugname = drugname, 
        fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, other.code = other.code, 
        no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, join = join, Year = Year)
}
```

## `drug_anti.infectives` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("anti-infectives", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, 
        drugname = drugname, fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, 
        other.code = other.code, no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, 
        join = join, Year = Year)
}
```

## `drug_anti.parkinson` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code, other.code, no.code, remove.other = TRUE, dup.take.drug = "remove", 
    join = "left", Year = FALSE) 
{
    Drug("antiparkinson agents", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, 
        drugname = drugname, fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, 
        other.code = other.code, no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, 
        join = join, Year = Year)
}
```

## `drug_fibrates` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("fibric acid", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, drugname = drugname, 
        fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, other.code = other.code, 
        no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, join = join, Year = Year)
}
```

## `drug_niacin` [exported]

```r
function (data, years, take_drug = TRUE, DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, dcn = FALSE, 
    icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = TRUE, 
    dup.take.drug = "remove", join = "left", Year = FALSE) 
{
    Drug("niacin", data = data, years = years, take_drug = take_drug, DrugNumber = DrugNumber, drugname = drugname, 
        fdaNDC = fdaNDC, dcn = dcn, icn = icn, icd10 = icd10, yes.code = yes.code, other.code = other.code, 
        no.code = no.code, remove.other = remove.other, dup.take.drug = dup.take.drug, join = join, Year = Year)
}
```

## `drug_search` [exported]

```r
function (..., years = NULL) 
{
    h0 <- c(...)
    lss <- ls(envir = .GlobalEnv, all.names = T)
    if (is.null(years)) 
        years <- get_config_years()
    years <- prepare_years(years)
    if (!".drug_search_data" %in% lss) 
        build_drug_search_data(years)
    if (".drug_search_years" %in% lss) {
        ck1 <- all(.drug_search_years %in% years)
        ck2 <- all(years %in% .drug_search_years)
        if (ck1 & ck2) {
            "do nothing"
        }
        else {
            build_drug_search_data(years)
        }
    }
    else {
        .drug_search_years <<- years
    }
    d <- .drug_search_data
    d <- nhs_view.data.frame(d, h0)
    invisible(d)
}
```


