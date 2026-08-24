# Integrated supporting reference: nhanesr-function-reference/references/expressions-fndds_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-fndds_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `fndds_`

## `fndds_AddFoodDesc` [exported]

```r
function (..., data, years, start = NULL, Year = FALSE, join = "left") 
{
    d <- db_fndds(data = data, years = years, files = "AddFoodDesc", Year = Year, join = join)
    h0 <- c(...)
    if (!is.null(h0)) 
        d <- d[lookl(d$additional.food.description, ..., ignore.case = TRUE), ]
    if (!is.null(start)) {
        for (i in 1:length(start)) {
            cki <- do::left(d$food.code, nchar(start[i])) %in% start[i]
            if (i == 1) {
                ck <- cki
            }
            else {
                ck <- ck | cki
            }
        }
        d <- d[ck, ]
    }
    row.names(d) <- NULL
    d
}
```

## `fndds_DerivDesc` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "DerivDesc", Year = Year, join = join)
}
```

## `fndds_FNDDSIngred` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FNDDSIngred", Year = Year, join = join)
}
```

## `fndds_FNDDSNutVal` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FNDDSNutVal", Year = Year, join = join)
}
```

## `fndds_FoodPortionDesc` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodPortionDesc", Year = Year, join = join)
}
```

## `fndds_FoodSubcodeLinks` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodSubcodeLinks", Year = Year, join = join)
}
```

## `fndds_FoodWeights` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodWeights", Year = Year, join = join)
}
```

## `fndds_IngredNutVal` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    drop_col(db_fndds(data = data, years = years, files = "IngredNutVal", Year = Year, join = join), 
        "nutrient.value.source", "sr.28.derivation.code", "sr.28.addmod.year")
}
```

## `fndds_MainFoodDesc` [exported]

```r
function (..., data, years, start = NULL, Year = FALSE, abbr = TRUE, fortify = TRUE, wweia = TRUE, join = "left") 
{
    d <- db_fndds(data = data, years = years, files = "MainFoodDesc", Year = Year, join = join)
    h0 <- c(...)
    if (!is.null(h0)) 
        d <- d[lookl(d[, c(colnames(d) %in% c("main.food.description", "wweia.category.description"))], 
            ..., ignore.case = TRUE), ]
    if (!is.null(start)) {
        for (i in 1:length(start)) {
            cki <- do::left(d$food.code, nchar(start[i])) %in% start[i]
            if (i == 1) {
                ck <- cki
            }
            else {
                ck <- ck | cki
            }
        }
        d <- d[ck, ]
    }
    row.names(d) <- NULL
    if (!abbr) 
        d <- drop_col(d, "abbreviated.description")
    if (!fortify) 
        d <- drop_col(d, "fortification.identifier")
    if (!wweia) 
        d <- drop_col(d, c("wweia.category.code", "wweia.category.description"))
    d
}
```

## `fndds_MoistAdjust` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "MoistAdjust", Year = Year, join = join)
}
```

## `fndds_NutDesc` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    drop_col(db_fndds(data = data, years = years, files = "NutDesc", Year = Year, join = join), "tagname", 
        "decimals")
}
```

## `fndds_SubcodeDesc` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "SubcodeDesc", Year = Year, join = join)
}
```

## `fndds_comp.food.Desc` [exported]

```r
function (..., data, years, start = NULL, Year = FALSE, abbr = TRUE, fortify = TRUE, wweia = TRUE, add = TRUE, 
    join = "left") 
{
    years <- data_years(data, years)
    d1 <- fndds_MainFoodDesc(years = years, start = start, Year = TRUE, abbr = abbr, fortify = fortify, 
        wweia = wweia)
    d2 <- fndds_AddFoodDesc(years = years, start = start)
    if (add) {
        d <- dplyr::left_join(d1, d2, "food.code")
        h0 <- c(...)
        if (!is.null(h0)) {
            search <- paste0_columns(select_col(d, "main.food.description", "wweia.category.description", 
                "additional.food.description"))
            d <- d[lookl(search, h0), ]
        }
    }
    else {
        d <- d1
        h0 <- c(...)
        if (!is.null(h0)) {
            search <- paste0_columns(select_col(d, "main.food.description", "wweia.category.description"))
            d <- d[lookl(search, h0), ]
        }
    }
    return_data(data, d, Year, key = "food.code", join = join)
}
```

## `fndds_comp.food.Portion.Weight` [exported]

```r
function (..., data, years, start = NULL, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d1 <- fndds_FoodWeights(years = years, Year = TRUE)
    d2 <- drop_col(fndds_FoodPortionDesc(years = years), "change.type")
    d12 <- dplyr::left_join(d1, d2, "portion.code")
    d3 <- fndds_SubcodeDesc(years = years)
    d <- dplyr::left_join(d12, d3, "subcode")
    if (!is.null(start)) {
        for (i in 1:length(start)) {
            cki <- do::left(d$food.code, nchar(start[i])) %in% start[i]
            if (i == 1) {
                ck <- cki
            }
            else {
                ck <- ck | cki
            }
        }
        d <- d[ck, ]
    }
    h0 <- c(...)
    if (!is.null(h0)) {
        search <- paste0(select_col(d, "subcode.description", "portion.description"))
        d <- d[lookl(search, ...), ]
    }
    return_data(data, d, Year, key = "food.code", join = join)
}
```

## `fndds_comp.nutrients` [exported]

```r
function (..., data, years, Year = FALSE, join = "left") 
{
    d.nutValue <- fndds_FNDDSNutVal(years = years, Year = TRUE)
    d.nutCode <- fndds_NutDesc(years = years)
    d <- dplyr::left_join(d.nutValue, d.nutCode, "nutrient.code")
    h0 <- c(...)
    if (!is.null(h0)) {
        d <- d[lookl(d$nutrient.description, ...), ]
    }
    return_data(data, d, Year, key = "food.code", join = join)
}
```

## `fndds_download` [exported]

```r
function () 
{
    fndds_dir <- paste0(get_config_path(), "/fndds")
    if (!dir.exists(fndds_dir)) 
        dir.create(fndds_dir)
    html <- rvest::read_html("https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds-download-databases/")
    url1 <- unique(sprintf(do::attr_href(set::grep_and(rvest::html_elements(html, xpath = "//a[@href]"), 
        c("access.exe", "FNDDS"))), fmt = "https://www.ars.usda.gov%s"))
    url2 <- unique(sprintf(do::attr_href(set::grep_and(rvest::html_elements(html, xpath = "//a[@href]"), 
        c("VitaminAE", "access.exe"))), fmt = "https://www.ars.usda.gov%s"))
    url <- c(url1, url2)
    message("all fndds:", length(url))
    for (i in 1:length(url)) {
        cat("\n", i, " ")
        fn <- do::file.name(url[i])
        cat(fn)
        to <- paste0(fndds_dir, "/", fn)
        nullcon <- file(nullfile(), open = "wb")
        sink(nullcon, type = "message")
        download.file(url[i], to, mode = "wb")
        sink(type = "message")
        close(nullcon)
    }
    for (i in 1:5) {
        from <- paste0(fndds_dir, sprintf("/FNDDS%s_ACCESS.EXE", i))
        to <- paste0(fndds_dir, sprintf("/FNDDS_%s-%s_ACCESS.EXE", 2000 + 2 * (i - 1) + 1, 2000 + 2 * 
            (i - 1) + 2))
        file.rename(from, to)
    }
    exe <- list.files(fndds_dir, "access.exe", ignore.case = TRUE, full.names = TRUE)
    to <- paste0(do::knife_right(exe, 3), "zip")
    file.rename(exe, to)
    invisible()
}
```

## `fndds_file_colnames` [exported]

```r
function (files = NULL, years, view = TRUE) 
{
    years <- prepare_years(years)
    if (is.null(files)) {
        x <- fndds_file_names(view = F)$FileName
        y <- c("MainFoodDesc", "AddFoodDesc", "FoodWeights", "FoodPortionDesc", "SubcodeDesc", "FoodSubcodeLinks", 
            "FNDDSNutVal", "NutDesc", "MoistAdjust", "FNDDSIngred", "IngredNutVal", "DerivDesc", "SRNutVal", 
            "MoistNFatAdjust", "FNDDSSRLinks", "FNDDSRecCount")
        x <- y[y %in% x]
        x0 <- x
        ck <- x %in% c("MainFoodDesc", "AddFoodDesc")
        x[ck] <- crayon::red(x[ck])
        ck <- x %in% c("FoodWeights", "FoodPortionDesc", "SubcodeDesc", "FoodSubcodeLinks")
        x[ck] <- crayon::blue(x[ck])
        ck <- x %in% c("FNDDSNutVal", "NutDesc", "MoistAdjust", "FNDDSIngred", "IngredNutVal", "DerivDesc", 
            "SRNutVal", "MoistNFatAdjust", "FNDDSSRLinks")
        x[ck] <- crayon::red(x[ck])
        ck <- x %in% c("ModDesc", "ModNutVal")
        x[ck] <- crayon::green(x[ck])
        ch <- select.list(x, multiple = TRUE)
        files <- x0[x %in% ch]
    }
    d <- db_fndds(years = years, files = files, Year = TRUE, nrow = 10)
    if (view) 
        View(nhs_brief(d))
    invisible(d)
}
```

## `fndds_file_names` [exported]

```r
function (view = TRUE) 
{
    fndds <- paste0(get_config_path(), "/fndds")
    mdb <- set::grep_or(list.files(fndds, "tsv", full.names = TRUE, recursive = TRUE), prepare_years())
    Year <- do::Replace0(mdb, fndds, "_ACCESS.*", ".*FNDDS_")
    FileName <- do::Replace0(do::file.name(mdb), "\\.tsv")
    d <- data.frame(FileName, Year, x = 1)
    d <- reshape2::dcast(d, FileName ~ Year, value.var = "x")
    d[is.na(d)] <- ""
    dF <- d$FileName
    d <- d[, -1]
    d$FileName <- dF
    row.names(d) <- dF
    order <- c("MainFoodDesc", "AddFoodDesc", "FoodWeights", "FoodSubcodeLinks", "SubcodeDesc", "FoodPortionDesc", 
        "FNDDSNutVal", "MoistAdjust", "NutDesc", "FNDDSIngred", "IngredNutVal", "DerivDesc")
    dod <- set::and(order, dF)
    dod <- c(dod, set::not(dF, dod))
    d <- d[dod, ]
    row.names(d) <- NULL
    fd <- data.frame(FileName = c("MainFoodDesc", "AddFoodDesc", "FoodWeights", "FoodSubcodeLinks", "SubcodeDesc", 
        "FoodPortionDesc", "FNDDSNutVal", "FNDDSSRLinks", "MoistNFatAdjust", "NutDesc", "FNDDSRecCount", 
        "ModDesc", "ModNutVal", "SRNutVal", "FNDDSIngred", "IngredNutVal", "MoistAdjust", "DerivDesc"), 
        Description = c("Main Food Descriptions", "Additional Food Descriptions", "Food Weights", "Food Code-Subcode Links", 
            "Subcode Descriptions", "Food Portion Descriptions", "FNDDS Nutrient Values", "FNDDS-SR Links", 
            "Moisture & Fat Adjustments", "Nutrient Descriptions", "FNDDS databases record counts", "Modifications Descriptions", 
            "Modifications Nutrient Values", "SR Nutrient Values", "FNDDS Ingredients", "Ingredient Nutrient Values", 
            "Moisture Adjustment", "Derivation Descriptions"), Component = c("Food Descriptions", "Food Descriptions", 
            "Food Portions & Weights", "Food Portions & Weights", "Food Portions & Weights", "Food Portions & Weights", 
            "Nutrients", "Nutrients", "Nutrients", "Nutrients", "Nutrients", "Nutrients", "Nutrients", 
            "Nutrients", "Nutrients", "Nutrients", "Nutrients", "Nutrients"))
    FNDDS_FileName <- dplyr::left_join(d, fd, "FileName")
    if (view) 
        View(FNDDS_FileName)
    invisible(FNDDS_FileName)
}
```

## `fndds_food.code` [exported]

```r
function (years, cat = TRUE) 
{
    years <- prepare_years(years)
    files <- list.files(paste0(get_config_path(slash = TRUE), "fndds/"), recursive = TRUE, full.names = TRUE)
    files <- look(files, "food_code_", "\\.codebook")
    x <- look(files, paste0(years, collapse = "|"))
    if (cat) 
        print(x)
    invisible(x)
}
```

## `fndds_tsv` [exported]

```r
function (..., years, cat = TRUE) 
{
    years <- prepare_years(years)
    files <- list.files(paste0(get_config_path(slash = TRUE), "fndds/"), recursive = TRUE, full.names = TRUE)
    pattern <- c(...)
    if (is.null(pattern)) 
        return(files)
    x <- look(files, paste0(years, collapse = "|"), "\\.tsv", pattern, ignore.case = TRUE)
    if (cat) 
        print(x)
    invisible(x)
}
```


