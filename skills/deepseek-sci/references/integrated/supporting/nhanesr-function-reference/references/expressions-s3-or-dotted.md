# Integrated supporting reference: nhanesr-function-reference/references/expressions-s3-or-dotted.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-s3-or-dotted.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `s3-or-dotted`

## `BA.i` [internal]

```r
function (d, biomarkers) 
{
    mtr <- do.call(lapply(biomarkers, function(i) {
        fit <- lm(d[[i]] ~ d$age)
        fs <- summary(fit)
        data.frame(q = fit$coefficients[1], k = fit$coefficients[2], s = fs$sigma, r2 = fs$r.squared, 
            row.names = i)
    }), what = rbind)
    BAe.up <- rowSums(do.call(lapply(biomarkers, function(i) {
        (d[[i]] - mtr[i, "q"]) * (mtr[i, "k"]/(mtr[i, "s"]^2))
    }), what = cbind))
    BAe.down <- sum(sapply(biomarkers, function(i) {
        (mtr[i, "k"]/mtr[i, "s"])^2
    }))
    BAe <- BAe.up/BAe.down
    Rchar <- sum(mtr$r2/sqrt(1 - mtr$r2))/sum(sqrt(mtr$r2)/sqrt(1 - mtr$r2))
    S2.BA <- sd(BAe - d$age, na.rm = T)^2 - (1/Rchar^2 - 1) * (diff(range(d$age, na.rm = T))^2/12/length(biomarkers))
    d$BiologicalAge <- (BAe.up + d$age/S2.BA)/(BAe.down + 1/S2.BA)
    d[, c("datasseeqqnn", "BiologicalAge")]
}
```

## `HeartAge.table` [internal]

```r
function () 
{
    structure(list(sex = c("female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male"), points = c("<1", "1", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "11", "12", "13", "14", ">=15", "<0", "0", "1", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "11", "12", "13", "14", "15", "16", ">=17"), HeartAge = c("<30", "31", "34", 
        "36", "39", "42", "45", "48", "51", "55", "59", "64", "68", "73", "79", ">80", "<30", "30", "32", 
        "34", "36", "38", "40", "42", "45", "48", "51", "54", "57", "60", "64", "68", "72", "76", ">80")), 
        class = "data.frame", row.names = c(NA, -35L))
}
```

## `OBS.score.table` [internal]

```r
function () 
{
    structure(list(`male-0` = c("xi < 12.56", "xi < 98.83", "xi < 1.79", "xi < 20.65", "xi < 1.59", "xi < 316.00", 
        "xi < 3.36", "xi < 42.44", "xi < 5.82", "xi < 646.00", "xi < 257.00", "xi < 9.75", "xi < 1.12", 
        "xi < 94.94", "xi >= 107.43", "xi >= 19.17", "xi < 417.86", "xi >= 30", "xi >= 29.17", "xi >= 1.13"), 
        `male-1` = c("xi >= 12.56 & xi <19.70", "xi >= 98.83 & xi <306.25", "xi >= 1.79 & xi <2.69", 
            "xi >= 20.65 & xi <29.75", "xi >= 1.59 & xi <2.40", "xi >= 316.00 & xi <492.00", "xi >= 3.36 & xi <6.20", 
            "xi >= 42.44 & xi <113.21", "xi >= 5.82 & xi <9.42", "xi >= 646.00 & xi <1072.00", "xi >= 257.00 & xi <361.28", 
            "xi >= 9.75 & xi <15.10", "xi >= 1.12 & xi <1.57", "xi >= 94.94 & xi <141.80", "xi >= 69.83 & xi <107.43", 
            "xi >= 12.88 & xi <19.17", "xi >= 417.86 & xi <1135.71", "xi >= 0 & xi <30", "xi > 25.54 & xi <29.17", 
            "xi > 0.038 & xi <1.13"), `male-2` = c("xi >= 19.70", "xi >= 306.25", "xi >= 2.69", "xi >= 29.75", 
            "xi >= 2.40", "xi >= 492.00", "xi >= 6.20", "xi >= 113.21", "xi >= 9.42", "xi >= 1072.00", 
            "xi >= 361.28", "xi >= 15.10", "xi >= 1.57", "xi >= 141.80", "xi < 69.83", "xi < 12.88", 
            "xi >= 1135.71", "None", "xi <= 25.54", "xi <= 0.038"), `female-0` = c("xi < 10.10", "xi < 98.08", 
            "xi < 1.34", "xi < 14.52", "xi < 1.13", "xi < 251.00", "xi < 2.22", "xi < 38.01", "xi < 4.53", 
            "xi < 499.24", "xi < 187.00", "xi < 6.73", "xi < 0.85", "xi < 67.79", "xi >= 75.79", "xi >= 14.32", 
            "xi < 270.00", "xi >= 15", "xi >= 28.64", "xi >= 0.172"), `female-1` = c("xi >= 10.10 & xi <16.31", 
            "xi >= 98.08 & xi <383.50", "xi >= 1.34 & xi <2.02", "xi >= 14.52 & xi <21.86", "xi >= 1.13 & xi <1.77", 
            "xi >= 251.00 & xi <388.96", "xi >= 2.22 & xi <4.22", "xi >= 38.01 & xi <98.49", "xi >= 4.53 & xi <7.52", 
            "xi >= 499.24 & xi <849.00", "xi >= 187.00 & xi <283.43", "xi >= 6.73 & xi <10.75", "xi >= 0.85 & xi <1.28", 
            "xi >= 67.79 & xi <99.50", "xi >= 50.98 & xi <75.79", "xi >= 9.65 & xi <14.32", "xi >= 270.00 & xi <845.71", 
            "xi >= 0 & xi <15", "xi > 23.74 & xi <28.64", "xi > 0.035 & xi <0.172"), `female-2` = c("xi >= 16.31", 
            "xi >= 383.50", "xi >= 2.02", "xi >= 21.86", "xi >= 1.77", "xi >= 388.96", "xi >= 4.22", 
            "xi >= 98.49", "xi >= 7.52", "xi >= 849.00", "xi >= 283.43", "xi >= 10.75", "xi >= 1.28", 
            "xi >= 99.50", "xi < 50.98", "xi < 9.65", "xi >= 845.71", "None", "xi <= 23.74", "xi <= 0.035")), 
        row.names = c("dietary_fiber_g", "carotene_RE", "riboflavin_mg", "niacin_mg", "vitamin_B6_mg", 
            "total_folate_mcg", "vitamin_B12_mcg", "vitamin_C_mg", "vitamin_E_ATE_mg", "calcium_mg", 
            "magnesium_mg", "zinc_mg", "copper_mg", "selenium_mcg", "total_fat_g", "iron_mg", "PA_total_MET", 
            "alcohol_g", "BMI_kg.m2", "cotinine_ng.ml"), class = "data.frame")
}
```

## `YJP.ps` [internal]

```r
function (dii) 
{
    min = dii[, 5]
    ps <- ifelse(is.na(dii[, 1]), 1, 0) + ifelse(is.na(dii[, 2]), 1, 0) + ifelse(is.na(dii[, 3]), 1, 
        0) + ifelse(is.na(dii[, 4]), 3, 0)
    c(min, min + ps)
}
```

## `add_col.data.frame` [internal]

```r
function (data, colname = NULL, value = NULL, condition = NULL, position = NULL) 
{
    if (is.null(condition)) {
        data[, colname] <- value
    }
    else {
        condition[is.na(condition)] <- FALSE
        if (length(value) == 1) {
            data[condition, colname] <- value
        }
        else if (sum(condition) == length(value)) {
            data[condition, colname] <- value
        }
        else if (nrow(data) == length(value)) {
            data[condition, colname] <- value[condition]
        }
    }
    if (is.numeric(position)) {
        (b1 <- which((1:ncol(data)) < position[1]))
        (b3 <- which((1:ncol(data)) >= position[1]))
        fcol <- unique(c(colnames(data)[b1], colname, colnames(data)[b3]))
        data <- data[, fcol]
    }
    else if (is.character(position)) {
        position <- which(colnames(data) %in% position)
        (b1 <- which((1:ncol(data)) <= position[1]))
        (b3 <- which((1:ncol(data)) > position[1]))
        (fcol <- unique(c(set::not(colnames(data)[b1], colname), colname, colnames(data)[b3])))
        data <- data[, fcol]
    }
    data
}
```

## `add_col.survey.design` [internal]

```r
function (data, colname = NULL, value = NULL, condition = NULL, position = NULL) 
{
    if (is.null(condition)) {
        design$variables[, colname] <- value
    }
    else {
        condition[is.na(condition)] <- FALSE
        if (length(value) == 1) {
            design$variables[condition, colname] <- value
        }
        else if (sum(condition) == length(value)) {
            design$variables[condition, colname] <- value
        }
        else if (nrow(design$variables) == length(value)) {
            design$variables[condition, colname] <- value[condition]
        }
    }
    if (is.numeric(position)) {
        (b1 <- which((1:ncol(design$variables)) < position[1]))
        (b3 <- which((1:ncol(design$variables)) >= position[1]))
        fcol <- unique(c(colnames(design$variables)[b1], colname, colnames(design$variables)[b3]))
        design$variables <- design$variables[, fcol]
    }
    else if (is.character(position)) {
        position <- which(colnames(design$variables) %in% position)
        (b1 <- which((1:ncol(design$variables)) <= position[1]))
        (b3 <- which((1:ncol(design$variables)) > position[1]))
        (fcol <- unique(c(set::not(colnames(design$variables)[b1], colname), colname, colnames(design$variables)[b3])))
        design$variables <- design$variables[, fcol]
    }
    design
}
```

## `browser.fndds` [exported]

```r
function () 
{
    browseURL(system.file("data/fndds.html", package = "nhanesR"))
}
```

## `browser.fped` [exported]

```r
function () 
{
    browseURL(system.file("data/fped.html", package = "nhanesR"))
}
```

## `browser.survey` [exported]

```r
function () 
{
    url <- paste0("http://127.0.0.1:", tools::startDynamicHelp(NA), "/library/survey/html/00Index.html")
    cat(url)
    browseURL(url)
}
```

## `bu_above.equal` [exported]

```r
function (x, n) 
{
    x <- deparse(substitute(x))
    st <- sprintf("bu_x <- %s\n", x)
    for (i in 1:n) {
        st <- paste0(st, sprintf("%s[bu('[ , )')] <- \n", x))
    }
    context <- rstudioapi::getActiveDocumentContext()
    contents <- context$contents
    start <- context$selection[[1]]$range$start[[1]]
    for (i in start:1) {
        if (do::left(do::Trim(contents[i]), 15) == "bu_above.equal(") {
            (break)(i)
        }
    }
    rstudioapi::insertText(c(i, 1), "# ")
    rstudioapi::insertText(c(i + 1, 1), st)
    rstudioapi::setCursorPosition(c(i + 2, nchar(x) + 10))
}
```

## `bu_lower.equal` [exported]

```r
function (x, n) 
{
    x <- deparse(substitute(x))
    st <- sprintf("bu_x <- %s\n", x)
    for (i in 1:n) {
        st <- paste0(st, sprintf("%s[bu('( , ]')] <- \n", x))
    }
    context <- rstudioapi::getActiveDocumentContext()
    contents <- context$contents
    start <- context$selection[[1]]$range$end[[1]]
    for (i in start:1) {
        if (do::left(do::Trim(contents[i]), 15) == "bu_lower.equal(") {
            (break)(i)
        }
    }
    rstudioapi::insertText(c(i, 1), "# ")
    rstudioapi::insertText(c(i + 1, 1), st)
    rstudioapi::setCursorPosition(c(i + 2, nchar(x) + 10))
}
```

## `census_2000.All.ages` [exported]

```r
function () 
{
    age <- c("0-1", "1-1", "2-4", "5-5", "6-8", "9-9", "10-11", "12-14", "15-17", "18-19", "20-24", "25-29", 
        "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", 
        "85+")
    Population_in_thousands <- c(3795, 3759, 11433, 3896, 11800, 4224, 8258, 11799, 11819, 8001, 18257, 
        17722, 19511, 22180, 22479, 19806, 17224, 13307, 10654, 9410, 8726, 7415, 4900, 4259)
    Adjustment_Weight <- c(0.013818, 0.013687, 0.04163, 0.014186000000000001, 0.042965999999999997, 0.01538, 
        0.030068999999999999, 0.042963000000000001, 0.043034999999999997, 0.029132999999999999, 0.066477999999999995, 
        0.064530000000000004, 0.071043999999999996, 0.080762, 0.081850999999999993, 0.072118000000000002, 
        0.062715999999999994, 0.048453999999999997, 0.038793000000000001, 0.034264000000000003, 0.031773000000000003, 
        0.027, 0.017842, 0.015507999999999999)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2000.age20.40.60plus` [internal]

```r
function () 
{
    age <- c("20-39", "40-59", "60+")
    Population_in_thousands <- c(77670, 72816, 45364)
    Adjustment_Weight <- c(0.39657900000000001, 0.37179499999999999, 0.231626)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2000.age20plus` [internal]

```r
function () 
{
    age <- c("20-29", "30-39", "40-49", "50-59", "60-69", "70+")
    Population_in_thousands <- c(35979, 41691, 42285, 30531, 20064, 25300)
    Adjustment_Weight <- c(0.18370700000000001, 0.21287200000000001, 0.21590500000000001, 0.15589, 0.102446, 
        0.12917999999999999)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2000.age6plus` [internal]

```r
function () 
{
    age <- c("6-11", "12-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70+")
    Population_in_thousands <- c(24282, 31619, 35979, 41691, 42285, 30531, 20064, 25300)
    Adjustment_Weight <- c(0.096451999999999996, 0.12559600000000001, 0.14291499999999999, 0.165604, 
        0.167964, 0.12127499999999999, 0.079698000000000005, 0.100496)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2010.All.ages` [exported]

```r
function () 
{
    age <- c("0-1", "1-1", "2-4", "5-5", "6-8", "9-9", "10-11", "12-14", "15-17", "18-19", "20-24", "25-29", 
        "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", 
        "85+")
    Population_in_thousands <- c(3944, 3978, 12279, 4057, 12143, 4148, 8287, 12390, 12954, 9086, 21586, 
        21102, 19962, 20180, 20891, 22709, 22298, 19665, 16818, 12435, 9278, 7318, 5743, 5493)
    Adjustment_Weight <- Population_in_thousands/sum(Population_in_thousands)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2010.age20.40.60plus` [internal]

```r
function () 
{
    age <- c("20-39", "40-59", "60+")
    Population_in_thousands <- c(82830, 85563, 57085)
    Adjustment_Weight <- Population_in_thousands/sum(Population_in_thousands)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2010.age20plus` [internal]

```r
function () 
{
    age <- c("20-29", "30-39", "40-49", "50-59", "60-69", "70+")
    Population_in_thousands <- c(42688, 40142, 43600, 41963, 29253, 27832)
    Adjustment_Weight <- Population_in_thousands/sum(Population_in_thousands)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_2010.age6plus` [internal]

```r
function () 
{
    age <- c("6-11", "12-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70+")
    Population_in_thousands <- c(24578, 34430, 42688, 40142, 43600, 41963, 29253, 27832)
    Adjustment_Weight <- Population_in_thousands/sum(Population_in_thousands)
    data.frame(age, Population_in_thousands, Adjustment_Weight)
}
```

## `census_range.2010` [exported]

```r
function (..., sum = FALSE) 
{
    range <- c(...)
    if (length(range) == 1) {
        df <- do::col_split(do::Replace(census_2010.All.ages()$age, "\\+", "-100000"), "-")
        ck <- as.numeric(df$x1) >= range
        r <- census_2010.All.ages()[ck, ]
    }
    else if (length(range) == 2) {
        min <- min(range)
        max <- max(range)
        df <- do::col_split(do::Replace(census_2010.All.ages()$age, "\\+", "-100000"), "-")
        ck <- as.numeric(df$x1) >= min & max >= as.numeric(df$x2)
        r <- census_2010.All.ages()[ck, ]
    }
    if (sum) {
        return(sum(r[, 2]))
    }
    else {
        return(r)
    }
}
```

## `ci.no.by` [internal]

```r
function (design, x, round) 
{
    mean <- sapply(x, function(i) mean(do::complete.data(design[, i])))
    sd <- sapply(x, function(i) sd(do::complete.data(design[, i])))
    low <- (mean - 1.96 * sd)
    high <- (mean + 1.96 * sd)
    digit2character(mean) <- round
    digit2character(sd) <- round
    digit2character(low) <- round
    digit2character(high) <- round
    ci <- do::give_names(sprintf("%s(%s,%s)", mean, low, high), x)
    meanPMsd <- do::give_names(paste0(mean, "<U+00B1>", sd), x)
    meanSQsd <- do::give_names(paste0(mean, "(", sd, ")"), x)
    r <- data.frame(cbind(mean, sd, low, high, ci, meanPMsd, meanSQsd))
    r <- cbind(iiiiiii = row.names(r), r)
    row.names(r) <- NULL
    colnames(r)[1] <- "variable"
    r
}
```

## `coffee.1day` [internal]

```r
function (years, day = 1, unit = "gram", caffeinate = FALSE, sweeten = FALSE, fat = FALSE, milk = FALSE, 
    brewed = FALSE, cappuccino = FALSE, cuban = FALSE, espresso = FALSE, frappuccino = FALSE, latte = FALSE, 
    macchiato = FALSE, mexican = FALSE, mocha = FALSE, turkish = FALSE, food.code = NULL) 
{
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d.iff <- iff.gram.kcl(years = years, day = day)
    fndds.food.code <- coffee.food.code(years = years, food.code = food.code)
    fndds.food.code <- fndds.food.code[fndds.food.code$food.code %in% d.iff$food.code, ]
    fndds.food.code$food.code <- as.numeric(fndds.food.code$food.code)
    ck <- (!d.iff$food.code %in% fndds.food.code$food.code) & !is.na(d.iff$food.code)
    d.iff$gram[ck] <- 0
    d.iff$kcal[ck] <- 0
    d <- drop_col(dplyr::left_join(d.iff, fndds.food.code, c("Year", "food.code")), "seq.num")
    d$cup <- d$gram/d$portion.weight
    d$cup[grepl("oz", d$portion.description)] <- d$cup[grepl("oz", d$portion.description)]/6
    d <- d[, c("Year", "seqn", "gram", "kcal", "cup", "main.food.description")]
    d$cup[d$kcal %in% 0] <- 0
    ck.caffeinate <- lookl(d$main.food.description, "!~decaffeinate", NA2false = TRUE)
    d$coffee.caffeinate.gram[d$gram >= 0] <- 0
    d$coffee.caffeinate.kcal[d$gram >= 0] <- 0
    d$coffee.caffeinate.cup[d$gram >= 0] <- 0
    d$coffee.caffeinate.gram[ck.caffeinate] <- d$gram[ck.caffeinate]
    d$coffee.caffeinate.kcal[ck.caffeinate] <- d$kcal[ck.caffeinate]
    d$coffee.caffeinate.cup[ck.caffeinate] <- d$cup[ck.caffeinate]
    ck.decaffeinate <- lookl(d$main.food.description, "decaffeinate", NA2false = TRUE)
    d$coffee.decaffeinate.gram[d$gram >= 0] <- 0
    d$coffee.decaffeinate.kcal[d$gram >= 0] <- 0
    d$coffee.decaffeinate.cup[d$gram >= 0] <- 0
    d$coffee.decaffeinate.gram[ck.decaffeinate] <- d$gram[ck.decaffeinate]
    d$coffee.decaffeinate.kcal[ck.decaffeinate] <- d$kcal[ck.decaffeinate]
    d$coffee.decaffeinate.cup[ck.decaffeinate] <- d$cup[ck.decaffeinate]
    ck.sweeten <- lookl(d$main.food.description, "sweetened", NA2false = TRUE)
    d$coffee.sweeten.gram[d$gram >= 0] <- 0
    d$coffee.sweeten.kcal[d$gram >= 0] <- 0
    d$coffee.sweeten.cup[d$gram >= 0] <- 0
    d$coffee.sweeten.gram[ck.sweeten] <- d$gram[ck.sweeten]
    d$coffee.sweeten.kcal[ck.sweeten] <- d$kcal[ck.sweeten]
    d$coffee.sweeten.cup[ck.sweeten] <- d$cup[ck.sweeten]
    ck.unsweeten <- lookl(d$main.food.description, "!~sweetened", NA2false = TRUE)
    d$coffee.unsweeten.gram[d$gram >= 0] <- 0
    d$coffee.unsweeten.kcal[d$gram >= 0] <- 0
    d$coffee.unsweeten.cup[d$gram >= 0] <- 0
    d$coffee.unsweeten.gram[ck.unsweeten] <- d$gram[ck.unsweeten]
    d$coffee.unsweeten.kcal[ck.unsweeten] <- d$kcal[ck.unsweeten]
    d$coffee.unsweeten.cup[ck.unsweeten] <- d$cup[ck.unsweeten]
    ck.fat <- lookl(d$main.food.description, "fat", NA2false = TRUE)
    d$coffee.fat.gram[d$gram >= 0] <- 0
    d$coffee.fat.kcal[d$gram >= 0] <- 0
    d$coffee.fat.cup[d$gram >= 0] <- 0
    d$coffee.fat.gram[ck.fat] <- d$gram[ck.fat]
    d$coffee.fat.kcal[ck.fat] <- d$kcal[ck.fat]
    d$coffee.fat.cup[ck.fat] <- d$cup[ck.fat]
    ck.nofat <- lookl(d$main.food.description, "!~fat", NA2false = TRUE)
    d$coffee.nofat.gram[d$gram >= 0] <- 0
    d$coffee.nofat.kcal[d$gram >= 0] <- 0
    d$coffee.nofat.cup[d$gram >= 0] <- 0
    d$coffee.nofat.gram[ck.nofat] <- d$gram[ck.nofat]
    d$coffee.nofat.kcal[ck.nofat] <- d$kcal[ck.nofat]
    d$coffee.nofat.cup[ck.nofat] <- d$cup[ck.nofat]
    ck.milk <- lookl(d$main.food.description, "!~with non-dairy milk", NA2false = TRUE)
    d$coffee.milk.gram[d$gram >= 0] <- 0
    d$coffee.milk.kcal[d$gram >= 0] <- 0
    d$coffee.milk.cup[d$gram >= 0] <- 0
    d$coffee.milk.gram[ck.milk] <- d$gram[ck.milk]
    d$coffee.milk.kcal[ck.milk] <- d$kcal[ck.milk]
    d$coffee.milk.cup[ck.milk] <- d$cup[ck.milk]
    ck.nomilk <- lookl(d$main.food.description, "with non-dairy milk", NA2false = TRUE)
    d$coffee.nomilk.gram[d$gram >= 0] <- 0
    d$coffee.nomilk.kcal[d$gram >= 0] <- 0
    d$coffee.nomilk.cup[d$gram >= 0] <- 0
    d$coffee.nomilk.gram[ck.nomilk] <- d$gram[ck.nomilk]
    d$coffee.nomilk.kcal[ck.nomilk] <- d$kcal[ck.nomilk]
    d$coffee.nomilk.cup[ck.nomilk] <- d$cup[ck.nomilk]
    ck.cappuccino <- lookl(d$main.food.description, "cappuccino", NA2false = TRUE)
    d$coffee.cappuccino.gram[d$gram >= 0] <- 0
    d$coffee.cappuccino.kcal[d$gram >= 0] <- 0
    d$coffee.cappuccino.cup[d$gram >= 0] <- 0
    d$coffee.cappuccino.gram[ck.cappuccino] <- d$gram[ck.cappuccino]
    d$coffee.cappuccino.kcal[ck.cappuccino] <- d$kcal[ck.cappuccino]
    d$coffee.cappuccino.cup[ck.cappuccino] <- d$cup[ck.cappuccino]
    ck.cuban <- lookl(d$main.food.description, "cuban", NA2false = TRUE)
    d$coffee.cuban.gram[d$gram >= 0] <- 0
    d$coffee.cuban.kcal[d$gram >= 0] <- 0
    d$coffee.cuban.cup[d$gram >= 0] <- 0
    d$coffee.cuban.gram[ck.cuban] <- d$gram[ck.cuban]
    d$coffee.cuban.kcal[ck.cuban] <- d$kcal[ck.cuban]
    d$coffee.cuban.cup[ck.cuban] <- d$cup[ck.cuban]
    ck.espresso <- lookl(d$main.food.description, "espresso", NA2false = TRUE)
    d$coffee.espresso.gram[d$gram >= 0] <- 0
    d$coffee.espresso.kcal[d$gram >= 0] <- 0
    d$coffee.espresso.cup[d$gram >= 0] <- 0
    d$coffee.espresso.gram[ck.espresso] <- d$gram[ck.espresso]
    d$coffee.espresso.kcal[ck.espresso] <- d$kcal[ck.espresso]
    d$coffee.espresso.cup[ck.espresso] <- d$cup[ck.espresso]
    ck.frappuccino <- lookl(d$main.food.description, "frappuccino", NA2false = TRUE)
    d$coffee.frappuccino.gram[d$gram >= 0] <- 0
    d$coffee.frappuccino.kcal[d$gram >= 0] <- 0
    d$coffee.frappuccino.cup[d$gram >= 0] <- 0
    d$coffee.frappuccino.gram[ck.frappuccino] <- d$gram[ck.frappuccino]
    d$coffee.frappuccino.kcal[ck.frappuccino] <- d$kcal[ck.frappuccino]
    d$coffee.frappuccino.cup[ck.frappuccino] <- d$cup[ck.frappuccino]
    ck.latte <- lookl(d$main.food.description, "latte", NA2false = TRUE)
    d$coffee.latte.gram[d$gram >= 0] <- 0
    d$coffee.latte.kcal[d$gram >= 0] <- 0
    d$coffee.latte.cup[d$gram >= 0] <- 0
    d$coffee.latte.gram[ck.latte] <- d$gram[ck.latte]
    d$coffee.latte.kcal[ck.latte] <- d$kcal[ck.latte]
    d$coffee.latte.cup[ck.latte] <- d$cup[ck.latte]
    ck.macchiato <- lookl(d$main.food.description, "macchiato", NA2false = TRUE)
    d$coffee.macchiato.gram[d$gram >= 0] <- 0
    d$coffee.macchiato.kcal[d$gram >= 0] <- 0
    d$coffee.macchiato.cup[d$gram >= 0] <- 0
    d$coffee.macchiato.gram[ck.macchiato] <- d$gram[ck.macchiato]
    d$coffee.macchiato.kcal[ck.macchiato] <- d$kcal[ck.macchiato]
    d$coffee.macchiato.cup[ck.macchiato] <- d$cup[ck.macchiato]
    ck.mexican <- lookl(d$main.food.description, "mexican", NA2false = TRUE)
    d$coffee.mexican.gram[d$gram >= 0] <- 0
    d$coffee.mexican.kcal[d$gram >= 0] <- 0
    d$coffee.mexican.cup[d$gram >= 0] <- 0
    d$coffee.mexican.gram[ck.mexican] <- d$gram[ck.mexican]
    d$coffee.mexican.kcal[ck.mexican] <- d$kcal[ck.mexican]
    d$coffee.mexican.cup[ck.mexican] <- d$cup[ck.mexican]
    ck.mocha <- lookl(d$main.food.description, "mocha", NA2false = TRUE)
    d$coffee.mocha.gram[d$gram >= 0] <- 0
    d$coffee.mocha.kcal[d$gram >= 0] <- 0
    d$coffee.mocha.cup[d$gram >= 0] <- 0
    d$coffee.mocha.gram[ck.mocha] <- d$gram[ck.mocha]
    d$coffee.mocha.kcal[ck.mocha] <- d$kcal[ck.mocha]
    d$coffee.mocha.cup[ck.mocha] <- d$cup[ck.mocha]
    ck.turkish <- lookl(d$main.food.description, "turkish", NA2false = TRUE)
    d$coffee.turkish.gram[d$gram >= 0] <- 0
    d$coffee.turkish.kcal[d$gram >= 0] <- 0
    d$coffee.turkish.cup[d$gram >= 0] <- 0
    d$coffee.turkish.gram[ck.turkish] <- d$gram[ck.turkish]
    d$coffee.turkish.kcal[ck.turkish] <- d$kcal[ck.turkish]
    d$coffee.turkish.cup[ck.turkish] <- d$cup[ck.turkish]
    (nms <- colnames(d)[do::left(colnames(d), 7) %in% "coffee."])
    x <- c(unit, nms[do::right(nms, 4) %in% c(unit, paste0(".", unit))])
    var <- unit
    title <- "coffee"
    if (sweeten) 
        append(var) <- c(paste0(title, ".sweeten.", unit), paste0(title, ".unsweeten.", unit))
    if (caffeinate) 
        append(var) <- c(paste0(title, ".caffeinate.", unit), paste0(title, ".decaffeinate.", unit))
    if (fat) 
        append(var) <- c(paste0(title, ".fat.", unit), paste0(title, ".nofat.", unit))
    if (milk) 
        append(var) <- c(paste0(title, ".milk.", unit), paste0(title, ".nomilk.", unit))
    if (cappuccino) 
        append(var) <- paste0(title, ".", "cappuccino", ".", unit)
    if (cuban) 
        append(var) <- paste0(title, ".", "cuban", ".", unit)
    if (espresso) 
        append(var) <- paste0(title, ".", "espresso", ".", unit)
    if (frappuccino) 
        append(var) <- paste0(title, ".", "frappuccino", ".", unit)
    if (latte) 
        append(var) <- paste0(title, ".", "latte", ".", unit)
    if (macchiato) 
        append(var) <- paste0(title, ".", "macchiato", ".", unit)
    if (mexican) 
        append(var) <- paste0(title, ".", "mexican", ".", unit)
    if (mocha) 
        append(var) <- paste0(title, ".", "mocha", ".", unit)
    if (turkish) 
        append(var) <- paste0(title, ".", "turkish", ".", unit)
    d2 <- aggregate2(data = d, x = var, by = c("Year", "seqn"), fun = ".sum.nona")
    colnames(d2) <- do::Replace0(colnames(d2), paste0("\\.", unit))
    col_rename(d2) <- paste0(unit, ":coffee.", unit)
    at <- unique(fndds.food.code[, c("food.code", "main.food.description")])
    row.names(at) <- NULL
    attr(d2, "food.code") <- at
    d2
}
```

## `coffee.food.code` [internal]

```r
function (years, food.code = NULL) 
{
    years <- prepare_years(years)
    d1 <- fndds_comp.food.Desc(years = years, start = 921, abbr = F, add = F, wweia = F, fortify = F, 
        Year = T)
    d1$main.food.description <- do::Replace0(d1$main.food.description, c("ns as to type[, ]{0,}", "ns as to ground or instant[, ]{0,}", 
        "ns as to regular or decaffeinated[, ]{0,}", "ns as to brewed or instant[, ]{0,}"))
    if (!is.null(food.code)) 
        d1 <- d1[d1$food.code %in% food.code, ]
    d2 <- fndds_comp.food.Portion.Weight(data = d1)
    d2 <- d2[d2$seq.num == 1, ]
    df <- unique(d2[, c("Year", "food.code", "main.food.description", "portion.weight", "portion.description")])
    df$portion.weight <- as.numeric(df$portion.weight)
    df <- df[order(df$Year, df$food.code, df$portion.weight), ]
    dup <- duplicated(paste0(df$Year, "-", df$food.code))
    df <- df[!dup, ]
    df[, c("Year", "food.code", "main.food.description", "portion.weight", "portion.description")]
}
```

## `col.counts` [exported]

```r
function (data) 
{
    colSums(!is.na(data))
}
```

## `col.max` [exported]

```r
function (data) 
{
    if (is.vector(data)) {
        maxit(data)
    }
    else {
        apply(data, 2, maxit)
    }
}
```

## `col.means` [exported]

```r
function (data, na.rm = TRUE) 
{
    if (na.rm) {
        x <- colMeans(data, na.rm = TRUE)
        x[colSums(is.na(data)) == nrow(data)] <- NA
    }
    else {
        x <- colMeans(data, na.rm = FALSE)
    }
    x
}
```

## `col.sums` [exported]

```r
function (data, na.rm = TRUE) 
{
    if (na.rm) {
        x <- colSums(data, na.rm = TRUE)
        countNA <- colSums(is.na(data))
        x[countNA == nrow(data)] <- NA
    }
    else {
        x <- colSums(data, na.rm = FALSE)
    }
    x
}
```

## `create_db_dr.live.microbes` [internal]

```r
function (version = 1) 
{
    tb <- live_microbes_table()
    fdcd.lo <- tb$food.code[tb$`Asigned category` == "Lo"]
    fdcd.med <- tb$food.code[tb$`Asigned category` == "Med"]
    fdcd.hi <- tb$food.code[tb$`Asigned category` == "Hi"]
    d <- db_driff(Year = T, grams = "grams_Lo")
    d$grams_Med <- d$grams_Lo
    d$grams_Hi <- d$grams_Lo
    d$grams_Lo[!d$food.code %in% fdcd.lo] <- 0
    d$grams_Med[!d$food.code %in% fdcd.med] <- 0
    d$grams_Hi[!d$food.code %in% fdcd.hi] <- 0
    d <- aggregate_sum(data = d, x = c("grams_Lo", "grams_Med", "grams_Hi"), by = c("Year", "seqn"))
    attachdir <- paste0(get_config_path(), "/attach")
    if (!dir.exists(attachdir)) 
        dir.create(attachdir, recursive = T, showWarnings = F)
    (file <- paste0(attachdir, "/db_dr.live.microbes~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `create_diag_MASLD.FLI` [internal]

```r
function (version = 1) 
{
    library(dplyr)
    d <- dex_FLI(Year = T)
    d <- db_demo(d, ageyr = "age", sex = T)
    d <- d[d$age >= 18, ]
    d <- db_bodyMeasure(d, BMI_kg.m2 = "bmi", waist_circumference_cm = "wc")
    d$cc1 <- ifelse(d$bmi >= 25 | (d$sex == "male" & d$wc > 94) | (d$sex == "female" & d$wc >= 80), 1, 
        0)
    d <- diag_DM(d, told = T, drug = T, HbA1c = F, fast_glu = F, OGTT2 = F, rand_glu = F, cat = F) %>% 
        db_HemalBiochemistry(fast_glucose_mmol.L = "fglu")
    ghb <- nhs_tsv("lab10\\.|l10_b\\.|l10_c\\.|ghb", cat = F, items = "lab")
    ogtt <- nhs_tsv("ogtt", items = "Laboratory", cat = F)
    d2 <- nhs_read(ghb, "lbxgh:HbA1c", ogtt, "lbdgltsi:ogtt2", cat = F, lower_cd = TRUE)
    d <- Left_Join(d, d2, cat = F)
    ck <- d$fglu >= 5.5999999999999996 | d$ogtt2 >= 7.7999999999999998 | d$HbA1c >= 5.7000000000000002 | 
        d$DM %in% "DM"
    d$cc2 <- as.numeric(ck)
    d <- diag_Hypertension(d, systolic = 130, diastolic = 85, cat = F)
    d$cc3 <- as.numeric(d$Hypertension == "yes")
    d <- db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "tg", hdl_cholesterol_mmol.L = "hdl") %>% 
        drug_anti.Hyperlipidemic(take_drug = "lipid.low.drug")
    ck <- d$tg >= 1.7 | d$lipid.low.drug == "yes"
    d$cc4 <- as.numeric(ck)
    ck <- (d$sex == "male" & d$hdl <= 1) | (d$sex == "female" & d$hdl <= 1.3) | d$lipid.low.drug == "yes"
    d$cc5 <- as.numeric(ck)
    d$cc <- as.numeric(row.sums(d[, c("cc1", "cc2", "cc3", "cc4", "cc5")]) >= 1)
    d1 <- diag_alcohol.user()
    d2 <- diag_viral.hepatitis(HBV = T, HCV = T)
    drug.key <- "amiodarone|methotrexate|tamoxifen|aspirin|ibuprofen|nrtis|protease inhibitors|valproic acid|carbamazepine|fluorouracil|irinotecan|glucocorticoids"
    d3 <- Drug(drug.key, take_drug = "drug", yes.code = 1, no.code = 0, other.code = 0)
    tsv <- nhs_tsv("lab06|l40fe_b|l40fe_c|fetib", "!~lab06hm", cat = F)
    d4 <- nhs_read(tsv, "lbxpct,lbdpct:transferrin.saturation", cat = F, Year = F)
    d.oc <- Full_Join(d1, d2, d3, d4)
    d.oc$oc1 <- Recode(d.oc$alcohol.user, "never::0", "former::0", "mild::0", "moderate::1", "heavy::1", 
        "NA::", to.numeric = T)
    d.oc$oc2 <- Recode(d.oc$viral.hepatitis, "no::0", "yes::1", "NA::", to.numeric = T)
    d.oc$oc3 <- d.oc$drug
    d.oc$oc4 <- as.numeric(d.oc$transferrin.saturation >= 50)
    d.oc$oc <- as.numeric(row.sums(d.oc[, c("oc1", "oc2", "oc3", "oc4")]) >= 1)
    d <- Left_Join(d, d.oc, cat = F)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/diag_MASLD.FLI~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `create_diag_MASLD.cap` [exported]

```r
function (version = 2) 
{
    (file <- paste0(get_config_path(), "/attach/diag_MASLD.cap~~version-", version, ".txt"))
    if (!file.exists(file)) {
        library(dplyr)
        (tsv <- nhs_tsv("lux", cat = FALSE))
        d <- nhs_read(tsv, "luxcapm")
        d <- db_demo(d, ageyr = "age", sex = T)
        d <- d[d$age >= 18, ]
        d <- db_bodyMeasure(d, BMI_kg.m2 = "bmi", waist_circumference_cm = "wc")
        d$cc1 <- ifelse(d$bmi >= 25 | (d$sex == "male" & d$wc > 94) | (d$sex == "female" & d$wc >= 80), 
            1, 0)
        d <- diag_DM(d, told = T, drug = T, HbA1c = F, fast_glu = F, OGTT2 = F, rand_glu = F, cat = F) %>% 
            db_HemalBiochemistry(fast_glucose_mmol.L = "fglu")
        ghb <- nhs_tsv("lab10\\.|l10_b\\.|l10_c\\.|ghb", cat = F, items = "lab")
        ogtt <- nhs_tsv("ogtt", items = "Laboratory", cat = F)
        d2 <- nhs_read(ghb, "lbxgh:HbA1c", ogtt, "lbdgltsi:ogtt2", cat = F, lower_cd = TRUE)
        d <- Left_Join(d, d2, cat = F)
        ck <- d$fglu >= 5.5999999999999996 | d$ogtt2 >= 7.7999999999999998 | d$HbA1c >= 5.7000000000000002 | 
            d$DM %in% "DM"
        d$cc2 <- as.numeric(ck)
        d <- diag_Hypertension(d, systolic = 130, diastolic = 85, cat = F)
        d$cc3 <- as.numeric(d$Hypertension == "yes")
        d <- db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "tg", hdl_cholesterol_mmol.L = "hdl") %>% 
            drug_anti.Hyperlipidemic(take_drug = "lipid.low.drug")
        ck <- d$tg >= 1.7 | d$lipid.low.drug == "yes"
        d$cc4 <- as.numeric(ck)
        ck <- (d$sex == "male" & d$hdl <= 1) | (d$sex == "female" & d$hdl <= 1.3) | d$lipid.low.drug == 
            "yes"
        d$cc5 <- as.numeric(ck)
        d$cc <- as.numeric(row.sums(d[, c("cc1", "cc2", "cc3", "cc4", "cc5")]) >= 1)
        d1 <- diag_alcohol.user()
        d2 <- diag_viral.hepatitis(HBV = T, HCV = T)
        drug.key <- "amiodarone|methotrexate|tamoxifen|aspirin|ibuprofen|nrtis|protease inhibitors|valproic acid|carbamazepine|fluorouracil|irinotecan|glucocorticoids"
        d3 <- Drug(drug.key, take_drug = "drug", yes.code = 1, no.code = 0, other.code = 0)
        tsv <- nhs_tsv("lab06|l40fe_b|l40fe_c|fetib", "!~lab06hm", cat = F)
        d4 <- nhs_read(tsv, "lbxpct,lbdpct:transferrin.saturation", cat = F, Year = F)
        d.oc <- Full_Join(d1, d2, d3, d4)
        d.oc$oc1 <- Recode(d.oc$alcohol.user, "never::0", "former::0", "mild::0", "moderate::1", "heavy::1", 
            "NA::", to.numeric = T)
        d.oc$oc2 <- Recode(d.oc$viral.hepatitis, "no::0", "yes::1", "NA::", to.numeric = T)
        d.oc$oc3 <- d.oc$drug
        d.oc$oc4 <- as.numeric(d.oc$transferrin.saturation >= 50)
        d.oc$oc <- as.numeric(row.sums(d.oc[, c("oc1", "oc2", "oc3", "oc4")]) >= 1)
        d <- Left_Join(d, d.oc, cat = F)
        data.table::fwrite(d, file)
    }
    data.table::fread(file, data.table = F, na.strings = c(NA_character_, ""))
}
```

## `create_diag_MASLD.usFLI` [internal]

```r
function (version = 1) 
{
    library(dplyr)
    d <- dex_usFLI(Year = T)
    d <- db_demo(d, ageyr = "age", sex = T)
    d <- d[d$age >= 18, ]
    d <- db_bodyMeasure(d, BMI_kg.m2 = "bmi", waist_circumference_cm = "wc")
    d$cc1 <- ifelse(d$bmi >= 25 | (d$sex == "male" & d$wc > 94) | (d$sex == "female" & d$wc >= 80), 1, 
        0)
    d <- diag_DM(d, told = T, drug = T, HbA1c = F, fast_glu = F, OGTT2 = F, rand_glu = F, cat = F) %>% 
        db_HemalBiochemistry(fast_glucose_mmol.L = "fglu")
    ghb <- nhs_tsv("lab10\\.|l10_b\\.|l10_c\\.|ghb", cat = F, items = "lab")
    ogtt <- nhs_tsv("ogtt", items = "Laboratory", cat = F)
    d2 <- nhs_read(ghb, "lbxgh:HbA1c", ogtt, "lbdgltsi:ogtt2", cat = F, lower_cd = TRUE)
    d <- Left_Join(d, d2, cat = F)
    ck <- d$fglu >= 5.5999999999999996 | d$ogtt2 >= 7.7999999999999998 | d$HbA1c >= 5.7000000000000002 | 
        d$DM %in% "DM"
    d$cc2 <- as.numeric(ck)
    d <- diag_Hypertension(d, systolic = 130, diastolic = 85, cat = F)
    d$cc3 <- as.numeric(d$Hypertension == "yes")
    d <- db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "tg", hdl_cholesterol_mmol.L = "hdl") %>% 
        drug_anti.Hyperlipidemic(take_drug = "lipid.low.drug")
    ck <- d$tg >= 1.7 | d$lipid.low.drug == "yes"
    d$cc4 <- as.numeric(ck)
    ck <- (d$sex == "male" & d$hdl <= 1) | (d$sex == "female" & d$hdl <= 1.3) | d$lipid.low.drug == "yes"
    d$cc5 <- as.numeric(ck)
    d$cc <- as.numeric(row.sums(d[, c("cc1", "cc2", "cc3", "cc4", "cc5")]) >= 1)
    d1 <- diag_alcohol.user()
    d2 <- diag_viral.hepatitis(HBV = T, HCV = T)
    drug.key <- "amiodarone|methotrexate|tamoxifen|aspirin|ibuprofen|nrtis|protease inhibitors|valproic acid|carbamazepine|fluorouracil|irinotecan|glucocorticoids"
    d3 <- Drug(drug.key, take_drug = "drug", yes.code = 1, no.code = 0, other.code = 0)
    tsv <- nhs_tsv("lab06|l40fe_b|l40fe_c|fetib", "!~lab06hm", cat = F)
    d4 <- nhs_read(tsv, "lbxpct,lbdpct:transferrin.saturation", cat = F, Year = F)
    d.oc <- Full_Join(d1, d2, d3, d4)
    d.oc$oc1 <- Recode(d.oc$alcohol.user, "never::0", "former::0", "mild::0", "moderate::1", "heavy::1", 
        "NA::", to.numeric = T)
    d.oc$oc2 <- Recode(d.oc$viral.hepatitis, "no::0", "yes::1", "NA::", to.numeric = T)
    d.oc$oc3 <- d.oc$drug
    d.oc$oc4 <- as.numeric(d.oc$transferrin.saturation >= 50)
    d.oc$oc <- as.numeric(row.sums(d.oc[, c("oc1", "oc2", "oc3", "oc4")]) >= 1)
    d <- Left_Join(d, d.oc, cat = F)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/diag_MASLD.usFLI~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `crude.Model.n` [exported]

```r
function (..., round = 2, xlsx = NULL, style = 1, character2integer = TRUE, quadratic = FALSE, browseXLSX = TRUE) 
{
    fs <- list(...)
    fn <- do::get_names(...)
    names(fs) <- fn
    r <- order_fit(fs)
    model.i <- lapply(1:length(r), function(i) {
        do.call(lapply(1:length(r[[i]]), function(j) {
            rj <- lapply(1:length(r[[i]][[j]]), function(k) {
                d1 <- reg_table(r[[i]][[j]][[k]], x = names(r)[i], style = 2, view = F, round = round)
                if (nrow(d1) > 1) 
                  d1 <- d1[-1, ]
                d1 <- do::give_names(d1[, c(1, which(grepl("95", colnames(d1))), which(grepl("p", colnames(d1), 
                  T)))], "character", "95%CI", "P")
                d1$P[d1$P == "ref"] <- ""
                d1
                d2 <- do::give_names(as.data.frame(p4trend(fit = r[[i]][[j]][[k]], x = names(r)[i], character2integer = T, 
                  quadratic = F, round = round)), "P")
                d2 <- cbind(character = row.names(d2), d2)
                d2
                d3 <- plyr::rbind.fill(d1, d2)
                d3[is.na(d3)] <- ""
                d3
                d4 <- do::give_names(rbind(do::give_names(data.frame(t(colnames(d3)), check.names = F), 
                  colnames(d3)), d3), paste0(names(r)[i], "_", 1:ncol(d3)))
                d4
                if (k == 1) {
                  thismodel <- "crude model"
                }
                else {
                  thismodel <- paste0("Model ", k - 1)
                }
                if (style == 2) {
                  (Ql <- sum(paste0("Q", 1:nrow(d4)) %in% do::Trim(d4[, 1])))
                  (d4qi <- d4[2:(min(which(grepl("p for trend", d4[, 1]))) - 1), ])
                  (dl <- lapply(1:nrow(d4qi), function(qi) {
                    matrix(c(d4qi[qi, 1], d4qi[qi, 2], "P", d4qi[qi, 3]), nrow = 2)
                  }) %>% do.call(what = cbind) %>% data.frame)
                  dr <- lapply(which(grepl("p for trend", d4[, 1])), function(pi) {
                    matrix(c(d4[pi, 1], d4[pi, 3]), ncol = 1)
                  }) %>% do.call(what = cbind) %>% data.frame
                  (d7 <- cbind(data.frame(c("outcome", "model")), dl, dr))
                  d7 <- d7[, nchar(as.character(d7[2, ])) > 0]
                  colnames(d7) <- paste0(names(r)[i], "_", 1:ncol(d7))
                  row.names(d7) <- NULL
                  d7[2, 1] <- thismodel
                  d7
                }
                else {
                  rbind(do::give_names(data.frame(t(c("", thismodel, thismodel))), colnames(d4)), d4)
                }
            })
            rj
            if (style == 1) {
                rj <- do.call(cbind, rj)
                ck <- do::right(colnames(rj), 2) != "_1"
                ck[1] <- T
                rj <- rj[, ck]
                colnames(rj) <- c("character", paste0(names(r)[i], "_", 1:(ncol(rj) - 1)))
                rj[1, 1] <- paste0("data&&y:", names(r[[i]])[j])
            }
            else if (style == 2) {
                (rj <- as.data.frame(do.call(rbind, rj)))
                (rj <- rj[-(odd(1:nrow(rj))[-1]), ])
                colnames(rj) <- c("character", paste0(names(r)[i], "_", 1:(ncol(rj) - 1)))
                rj[1, 1] <- paste0("data&&y:", names(r[[i]])[j])
            }
            rj
        }), what = rbind)
    })
    (model.i <- full_join_character(model.i))
    model.i[is.na(model.i)] <- ""
    (datay <- which(do::left(model.i$character, 8) == "data&&y:"))
    if (sum(datay) >= 2) {
        if (style == 1) {
            for (i in datay[-1]) {
                model.i[i, 2:ncol(model.i)] <- ""
                model.i[i + 1, 1] <- NA
                model.i[i + 2, 1] <- NA
            }
            model.i <- model.i[!is.na(model.i$character), ]
            model.i <- rbind(model.i[1:2, ], model.i[2, ], model.i[-c(1, 2), ])
            model.i[3, 1] <- model.i[1, 1]
            model.i[3, -1] <- ""
            model.i[1:2, 1] <- ""
        }
        else if (style == 2) {
            for (i in datay[-1]) model.i[i, 2:ncol(model.i)] <- ""
            model.i <- rbind(model.i[1, ], model.i)
            model.i[1, 1] <- ""
            model.i[2, -1] <- ""
        }
    }
    (x1 <- do::knife_right(colnames(model.i)[do::right(colnames(model.i), 2) == "_1"], 2))
    if (style == 1) {
        ck <- sapply(1:nrow(model.i), function(i) any(as.character(model.i[i, ]) %in% "noPvalue4trend"))
        model.i <- model.i[!ck, ]
    }
    else if (style == 2) {
        ck <- sapply(1:ncol(model.i), function(i) any(model.i[, i] %in% "noPvalue4trend"))
        model.i <- model.i[, !ck]
    }
    (xp <- sapply(x1, function(i) {
        j = 1
        while (paste0(i, "_", j) %in% colnames(model.i)) {
            j <- j + 1
        }
        j - 1
    }))
    colnames(model.i)[1] <- " "
    if (!is.null(xlsx)) {
        center <- createStyle(halign = "center")
        bold <- createStyle(textDecoration = "Bold")
        red <- createStyle(fontColour = "red")
        border <- createStyle(border = "TopBottomLeftRight", borderStyle = "medium")
        wrap <- createStyle(wrapText = TRUE)
        wb <- createWorkbook()
        addWorksheet(wb, "Sheet 1")
        showGridLines(wb, 1, showGridLines = FALSE)
        for (i in 1:(nrow(model.i) + 1)) {
            addStyle(wb, 1, border, rows = i, cols = 1:ncol(model.i), stack = T)
        }
        for (i in x1) {
            (rg <- range(which(colnames(model.i) %in% paste0(i, "_", 1:ncol(model.i)))))
            mergeCells(wb, 1, rows = 1, cols = rg)
            writeData(wb, 1, x = i, startRow = 1, startCol = rg[1])
            addStyle(wb, 1, center, rows = 1, cols = rg[1], stack = T)
            addStyle(wb, 1, bold, rows = 1, cols = rg[1], stack = T)
        }
        for (i in 1:nrow(model.i)) {
            modev <- new.env()
            modev$modj <- 0
            curCol <- 1
            for (m in 1:ncol(model.i)) {
                if (m > 1) 
                  addStyle(wb, 1, center, rows = i + 1, cols = curCol, stack = T)
                (j <- model.i[i, m])
                if (do::left(j, 8) == "data&&y:") {
                  writeData(wb, 1, do::Replace0(j, "data&&y:"), startRow = i + 1, startCol = curCol)
                  addStyle(wb, 1, bold, rows = i + 1, cols = curCol, stack = T)
                  curCol <- curCol + 1
                }
                else if (style == 1 & j %in% c("crude model", paste0("Model ", 1:ncol(model.i)))) {
                  if (modev$modj == 0) {
                    modev$modj <- 1
                    mergeCells(wb, 1, rows = i + 1, cols = c(curCol, curCol + 1))
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                    curCol <- curCol + 2
                  }
                  else {
                    modev$modj <- 0
                  }
                }
                else if (style == 1 & j %in% c("95%CI", "P")) {
                  writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                  curCol <- curCol + 1
                }
                else if (style == 1 & m > 2 & model.i[2, m] == "P" & j != "ref" & nchar(j) > 0) {
                  ck1 <- do::left(j, 1) == "<"
                  ck2 <- suppressWarnings(as.numeric(j) <= 0.050000000000000003)
                  if (ck1 | ck2) {
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                    addStyle(wb, 1, red, rows = i + 1, cols = curCol, stack = T)
                  }
                  else {
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                  }
                  curCol <- curCol + 1
                }
                else if (style == 2 & i > 1 & j != "P" & (model.i[1, m] == "P" | grepl("p for trend", 
                  model.i[1, m])) & j != "ref" & nchar(j) > 0) {
                  (ck1 <- do::left(j, 1) == "<")
                  (ck2 <- suppressWarnings(as.numeric(j) <= 0.050000000000000003))
                  ck2[is.na(ck2)] <- F
                  if (ck1 | ck2) {
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                    addStyle(wb, 1, red, rows = i + 1, cols = curCol, stack = T)
                    curCol <- curCol + 1
                  }
                  else {
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                    curCol <- curCol + 1
                  }
                }
                else if (style == 2 & i == 1) {
                  if (grepl("p for trend", j)) {
                    writeData(wb, 1, x = do::Replace(j, "trend", "trend\n"), startRow = i + 1, startCol = curCol)
                    addStyle(wb, 1, wrap, rows = i + 1, cols = curCol, stack = T)
                    curCol <- curCol + 1
                  }
                  else {
                    writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                    curCol <- curCol + 1
                  }
                }
                else {
                  writeData(wb, 1, x = j, startRow = i + 1, startCol = curCol)
                  curCol <- curCol + 1
                }
            }
        }
        x.df <- lapply(1:length(r), function(i) {
            x <- sapply(r[[1]][[1]], function(i) paste0(do::model.x(i), collapse = ", "))
            names(x) <- c("crudel model", paste0("model ", 1:(length(r[[1]][[1]]) - 1)))
            data.frame(x) %>% do::give_names(names(r)[i])
        }) %>% do.call(what = cbind)
        x.df <- data.frame(t(unique(t(unique(x.df)))), check.names = F)
        setColWidths(wb, 1, cols = 1, widths = 28)
        setColWidths(wb, 1, cols = 2:ncol(model.i), widths = "auto")
        curRow <- nrow(model.i) + 3
        for (j in 1:ncol(x.df)) {
            addStyle(wb, 1, bold, rows = curRow, cols = 1, stack = T)
            writeData(wb, 1, x = colnames(x.df)[j], startRow = curRow, startCol = 1)
            curRow <- curRow + 1
            for (i in 1:nrow(x.df)) {
                writeData(wb, 1, x = paste0(row.names(x.df)[i], ": ", x.df[i, 1]), startRow = curRow, 
                  startCol = 1)
                curRow <- curRow + 1
            }
            curRow <- curRow + 2
        }
        x <- tryCatch(saveWorkbook(wb, file = xlsx, overwrite = TRUE), error = function(e) "e")
        if (!is.character(x) & browseXLSX) 
            browseURL(xlsx)
    }
    (head <- shiny::tagList(trB(lapply(colnames(model.i), function(i) {
        if (i %in% unlist(lapply(x1, function(xi) paste0(xi, "_", 1:ncol(model.i))))) {
            if (i %in% paste0(x1, "_1")) 
                thB(x1[paste0(x1, "_1") == i], colspan = xp[x1[paste0(x1, "_1") == i]])
        }
        else {
            thB(i)
        }
    }))))
    body <- tbodyB(shiny::tagList(lapply(1:nrow(model.i), function(i) {
        modev <- new.env()
        modev$modj <- 0
        trB(shiny::tagList(lapply(1:ncol(model.i), function(m) {
            j <- model.i[i, m]
            if (do::left(j, 8) == "data&&y:") {
                add_style(tdB(do::Replace0(j, "data&&y:")), font_weight.bold = T)
            }
            else if (style == 1 & j %in% c("crude model", paste0("Model ", 1:ncol(model.i)))) {
                if (modev$modj == 0) {
                  modev$modj <- 1
                  add_style(tdB(j, colspan = 2), text_align.center = T)
                }
                else {
                  modev$modj <- 0
                  NULL
                }
            }
            else if (style == 1 & j %in% c("95%CI", "P")) {
                add_style(tdB(j), text_align.center = T)
            }
            else if (style == 1 & m > 2 & model.i[2, m] == "P" & j != "ref" & nchar(j) > 0) {
                ck1 <- do::left(j, 1) == "<"
                ck2 <- suppressWarnings(as.numeric(j) <= 0.050000000000000003)
                if (ck1 | ck2) {
                  add_style(tdB(j), color = "red")
                }
                else {
                  tdB(j)
                }
            }
            else if (style == 2 & i > 2 & j != "P" & (model.i[1, m] == "P" | grepl("p for trend", model.i[1, 
                m])) & j != "ref" & nchar(j) > 0) {
                ck1 <- do::left(j, 1) == "<"
                ck2 <- suppressWarnings(as.numeric(j) <= 0.050000000000000003)
                ck2[is.na(ck2)] <- F
                if (ck1 | ck2) {
                  add_style(tdB(j), color = "red")
                }
                else {
                  tdB(j)
                }
            }
            else if (style == 2 & i == 1) {
                if (grepl("p for trend", j)) {
                  add_style(tdB(shiny::span("p for trend", shiny::tags$br(), do::Replace0(j, "p for trend"))), 
                    text_align.center = T)
                }
                else {
                  add_style(tdB(j), text_align.center = T)
                }
            }
            else {
                tdB(j)
            }
        })))
    })))
    htmltools::browsable(tableB(add_style(selector = "table,th,td", border = "1px solid black", border_collapse.collapse = T), 
        head, body))
}
```

## `cut_headtail.data.frame` [internal]

```r
function (x, col, ..., cat = T) 
{
    per <- c(...)
    per <- sort(per)
    if (length(per) == 1) {
        if (per >= 0.5) {
            q <- quantile(x = x[[col]], probs = per, na.rm = T)
            x[x[[col]] <= q & !is.na(x[[col]]), ]
        }
        else {
            q <- quantile(x = x[[col]], probs = per, na.rm = T)
            x[x[[col]] >= q & !is.na(x[[col]]), ]
        }
    }
    else if (length(per) == 2) {
        q1 <- quantile(x = x[[col]], probs = per[1], na.rm = T)
        q2 <- quantile(x = x[[col]], probs = per[2], na.rm = T)
        r0 <- nrow(x)
        x1 <- x[x[[col]] >= q1 & x[[col]] <= q2 & !is.na(x[[col]]), ]
        r1 <- nrow(x1)
        if (cat) {
            cat(paste0(tmcn::toUTF8("<U+539F><U+59CB><U+6570><U+636E><U+884C><U+6570>"), ": ", r0, "\n"))
            cat(paste0(tmcn::toUTF8("<U+5220><U+9664><U+884C><U+6570>"), ": ", r0 - r1, "\n"))
            cat(paste0(tmcn::toUTF8("<U+5269><U+4F59><U+884C><U+6570>"), ": ", r1, "\n"))
        }
        x1
    }
}
```

## `cut_headtail.numeric` [internal]

```r
function (x, col, ..., cat = T) 
{
    per <- c(...)
    per <- sort(per)
    if (length(per) == 1) {
        if (per >= 0.5) {
            q <- quantile(x = x, probs = per, na.rm = T)
            x[x <= q & !is.na(x)]
        }
        else {
            q <- quantile(x = x, probs = per, na.rm = T)
            x[x >= q & !is.na(x)]
        }
    }
    else if (length(per) == 2) {
        q1 <- quantile(x = x, probs = per[1], na.rm = T)
        q2 <- quantile(x = x, probs = per[2], na.rm = T)
        x[x >= q1 & x <= q2 & !is.na(x)]
    }
}
```

## `cvd.points.men.table` [internal]

```r
function () 
{
    structure(list(points = c(-2, -1, 0, 1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15), sex = c("male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male"), age = c("", "", "30<U+2013>34", "", "35<U+2013>39", "", "", "40<U+2013>44", "45<U+2013>49", 
        "50<U+2013>54", "55<U+2013>59", "60<U+2013>64", "65<U+2013>69", "70<U+2013>74", ">=75"), hdl = c(">=60", 
        "50<U+2013>59", "45<U+2013>49", "35<U+2013>44", "<35", "", "", "", "", "", "", "", "", "", ""), 
        tc = c("", "", "<160", "160<U+2013>199", "200<U+2013>239", "240<U+2013>279", ">=280", "", "", 
            "", "", "", "", "", ""), sbp_no_treat = c("<120", "", "120<U+2013>129", "130<U+2013>139", 
            "140<U+2013>159", ">=160", "", "", "", "", "", "", "", "", ""), sbp_treat = c("", "", "<120", 
            "", "120<U+2013>129", "130<U+2013>139", "140<U+2013>159", ">=160", "", "", "", "", "", "", 
            ""), smoker = c("", "", "no", "", "", "", "yes", "", "", "", "", "", "", "", ""), diabetic = c("", 
            "", "no", "", "", "yes", "", "", "", "", "", "", "", "", "")), row.names = 1:15, class = "data.frame")
}
```

## `cvd.points.women.table` [internal]

```r
function () 
{
    structure(list(points = c(-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), sex = c("female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female"), age = c("", "", "", "30<U+2013>34", "", "35<U+2013>39", 
        "", "40<U+2013>44", "45<U+2013>49", "", "50<U+2013>54", "55<U+2013>59", "60<U+2013>64", "65<U+2013>69", 
        "70<U+2013>74", ">=75"), hdl = c("", ">=60", "50<U+2013>59", "45<U+2013>49", "35<U+2013>44", 
        "<35", "", "", "", "", "", "", "", "", "", ""), tc = c("", "", "", "<160", "160<U+2013>199", 
        "", "200<U+2013>239", "240<U+2013>279", ">=280", "", "", "", "", "", "", ""), sbp_no_treat = c("<120", 
        "", "", "120<U+2013>129", "130<U+2013>139", "140<U+2013>149", "", "150<U+2013>159", ">=160", 
        "", "", "", "", "", "", ""), sbp_treat = c("", "", "<120", "", "", "120<U+2013>129", "130<U+2013>139", 
        "", "140<U+2013>149", "150<U+2013>159", ">=160", "", "", "", "", ""), smoker = c("", "", "", 
        "no", "", "", "yes", "", "", "", "", "", "", "", "", ""), diabetic = c("", "", "", "no", "", 
        "", "", "yes", "", "", "", "", "", "", "", "")), row.names = 1:16, class = "data.frame")
}
```

## `df.tolower` [internal]

```r
function (x) 
{
    for (i in 1:ncol(x)) {
        x[, i] <- tolower(x[, i])
    }
    x
}
```

## `dietary_food.code` [internal]

```r
function (..., data, years, start = NULL, Year = FALSE) 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("fmt|fcd", years = years, cat = F)
    d <- nhs_read(tsv, "start,drxfdcd:food.code", "drxfcld,label:description")
    if ("food.code" %in% colnames(d) & "drxfdcd" %in% colnames(d)) {
        d$food.code <- format(d$food.code, width = 8)
        ck <- d$Year %in% set::not(prepare_years(), "1999-2000", "2001-2002")
        d$food.code[ck] <- d$drxfdcd[ck]
        d <- drop_col(d, "drxfdcd")
    }
    else if ("food.code" %in% colnames(d)) {
        d$food.code <- format(d$food.code, width = 8)
    }
    else if ("drxfdcd" %in% colnames(d)) {
        d$food.code <- d$drxfdcd
        d <- drop_col(d, "drxfdcd")
    }
    d <- d[, c("Year", "food.code", "description")]
    if (!is.null(start)) {
        for (i in 1:length(start)) {
            if (i == 1) {
                ck <- do::left(d$food.code, nchar(start[i])) %in% start[i]
            }
            else {
                cki <- do::left(d$food.code, nchar(start[i])) %in% start[i]
                ck <- ck | cki
            }
        }
        d <- d[ck, ]
    }
    h0 <- c(...)
    if (!is.null(h0)) {
        ck <- lookl(d$description, h0)
        d <- d[ck, ]
    }
    d <- unique(d)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dii.xlsx` [internal]

```r
function () 
{
    diitable <- list(alcohol = c(-0.27800000000000002, 13.98, 3.7200000000000002, -0.27800000000000002), 
        anthocyanidins = c(-0.13100000000000001, 18.050000000000001, 21.140000000000001, -0.44900000000000001), 
        b_carotene = c(-0.58399999999999996, 3718, 1720, -0.58399999999999996), caffeine = c(-0.11, 8.0500000000000007, 
            6.6699999999999999, -0.124), carbohydrates = c(0.097000000000000003, 272.19999999999999, 
            40, 0.109), cholesterol = c(0.11, 279.39999999999998, 51.200000000000003, 0.34699999999999998), 
        energy = c(0.17999999999999999, 2056, 338, 0.17999999999999999), eugenol = c(-0.14000000000000001, 
            0.01, 0.080000000000000002, -0.86799999999999999), fibre = c(-0.66300000000000003, 18.800000000000001, 
            4.9000000000000004, -0.66300000000000003), `flavan-3-ol` = c(-0.41499999999999998, 95.799999999999997, 
            85.900000000000006, -0.41499999999999998), flavones = c(-0.61599999999999999, 1.55, 0.070000000000000007, 
            -0.61599999999999999), flavonols = c(-0.46700000000000003, 17.699999999999999, 6.79, -0.46700000000000003), 
        flavonones = c(-0.25, 11.699999999999999, 3.8199999999999998, -0.90800000000000003), folic_acid = c(-0.19, 
            273, 70.700000000000003, -0.20699999999999999), Fe = c(0.032000000000000001, 13.35, 3.71, 
            0.032000000000000001), garlic = c(-0.41199999999999998, 4.3499999999999996, 2.8999999999999999, 
            -0.41199999999999998), ginger = c(-0.45300000000000001, 59, 63.200000000000003, -0.58799999999999997), 
        `green/black_tea` = c(-0.53600000000000003, 1.6899999999999999, 1.53, -0.53600000000000003), 
        isoflavones = c(-0.59299999999999997, 1.2, 0.20000000000000001, -0.59299999999999997), Mg = c(-0.48399999999999999, 
            310.10000000000002, 139.40000000000001, -0.48399999999999999), MUFA = c(-0.0089999999999999993, 
            27, 6.0999999999999996, -0.019), niacin = c(-0.246, 25.899999999999999, 11.77, -1), `n-3_fatty_acids` = c(-0.436, 
            1.0600000000000001, 1.0600000000000001, -0.436), `n-6_fatty_acids` = c(-0.159, 10.800000000000001, 
            7.5, -0.159), onion = c(-0.30099999999999999, 35.899999999999999, 18.399999999999999, -0.48999999999999999), 
        pepper = c(-0.13100000000000001, 10, 7.0700000000000003, -0.39700000000000002), protein = c(0.021000000000000001, 
            79.400000000000006, 13.9, 0.049000000000000002), PUFA = c(-0.33700000000000002, 13.880000000000001, 
            3.7599999999999998, -0.33700000000000002), riboflavin = c(-0.068000000000000005, 1.7, 0.79000000000000004, 
            -0.72699999999999998), rosemary = c(-0.012999999999999999, 1, 15, -0.33300000000000002), 
        saffron = c(-0.14000000000000001, 0.37, 1.78, 1), saturated_fat = c(0.373, 28.600000000000001, 
            8, 0.42899999999999999), selenium = c(-0.191, 67, 25.100000000000001, -0.191), tfat = c(0.29799999999999999, 
            71.400000000000006, 19.399999999999999, 0.29799999999999999), thiamin = c(-0.098000000000000004, 
            1.7, 0.66000000000000003, -0.35399999999999998), `thyme/oregano` = c(-0.10199999999999999, 
            0.33000000000000002, 0.98999999999999999, -1), trans_fat = c(0.22900000000000001, 3.1499999999999999, 
            3.75, 0.432), turmeric = c(-0.78500000000000003, 533.60000000000002, 754.29999999999995, 
            -0.78500000000000003), vb12 = c(0.106, 5.1500000000000004, 2.7000000000000002, 0.20499999999999999), 
        vb6 = c(-0.36499999999999999, 1.47, 0.73999999999999999, -0.379), vitamin_A = c(-0.40100000000000002, 
            983.89999999999998, 518.60000000000002, -0.40100000000000002), vitamin_C = c(-0.42399999999999999, 
            118.2, 43.460000000000001, -0.42399999999999999), vitamin_D = c(-0.44600000000000001, 6.2599999999999998, 
            2.21, -0.44600000000000001), vitamin_E = c(-0.41899999999999998, 8.7300000000000004, 1.49, 
            -0.41899999999999998), zinc = c(-0.313, 9.8399999999999999, 2.1899999999999999, -0.313))
    df <- data.frame(diitable)
    df <- df[-c(1, 2, 3, 4), ]
    openxlsx::write.xlsx(df, "dii.xlsx")
}
```

## `distinct.survey.design` [internal]

```r
function (.data, ...) 
{
    dplyr::distinct(.data$variables, ...)
}
```

## `drop_row.data.frame` [internal]

```r
function (x, ..., cat = TRUE, title = NULL, title.space = "", subtitle.space = "") 
{
    n0 = nrow(x)
    rule <- tryCatch(c(...), error = function(e) "errerrerrerrerrerrerrerrrrerrrererrerererere")
    if (is.character(rule)) {
        if (rule[1] == "errerrerrerrerrerrerrerrrrerrrererrerererere") {
            r2 <- substitute(alist(...))
            rule <- with(x, eval(r2))
            if (is.list(rule)) {
                rule0 <- tryCatch(do.call(c, rule), error = function(e) "eeeerrrroooorrrreee")
                if (all(rule0 %in% "eeeerrrroooorrrreee")) {
                  for (i in 1:length(rule)) {
                    rule[[i]] <- with(x, eval(rule[[i]]))
                  }
                  rule <- do.call(c, rule)
                }
                else {
                  rule <- rule0
                }
            }
            rule <- with(x, eval(rule))
        }
    }
    if (is.logical(rule)) {
        x <- x[!rule | is.na(rule), ]
    }
    else if (is.numeric(rule)) {
        x <- x[-rule, ]
    }
    else if (is.character(rule)) {
        x <- x[!row.names(x) %in% rule, ]
    }
    n1 <- nrow(x)
    if (cat) {
        if (!is.null(title)) 
            cat(paste0("\n", title.space, title))
        cat(paste0("\n", subtitle.space, "origin:", n0))
        cat(paste0("\n", subtitle.space, "drop:", n0 - n1, paste0("(", round((n0 - n1)/n0 * 100), "%", 
            ")")))
        cat(paste0("\n", subtitle.space, "left:", n1))
        cat("\n")
    }
    x
}
```

## `drop_row.survey.design` [internal]

```r
function (x, ..., cat = TRUE, title = NULL, title.space = "", subtitle.space = "") 
{
    rule <- tryCatch(c(...), error = function(e) "errerrerrerrerrerrerrerrrrerrrererrerererere")
    if (is.character(rule)) {
        if (rule[1] == "errerrerrerrerrerrerrerrrrerrrererrerererere") {
            r2 <- substitute(alist(...))
            rule <- with(x$variables, eval(r2))
            if (is.list(rule)) {
                rule0 <- tryCatch(do.call(c, rule), error = function(e) "eeeerrrroooorrrreee")
                if (all(rule0 %in% "eeeerrrroooorrrreee")) {
                  for (i in 1:length(rule)) {
                    rule[[i]] <- with(x$variables, eval(rule[[i]]))
                  }
                  rule <- do.call(c, rule)
                }
                else {
                  rule <- rule0
                }
            }
            rule <- with(x$variables, eval(rule))
        }
    }
    if (is.logical(rule)) {
        chose <- !rule | is.na(rule)
    }
    else if (is.numeric(rule)) {
        chose <- !(1:nrow(x)) %in% rule
    }
    else if (is.character(rule)) {
        chose <- !row.names(x) %in% rule
    }
    total <- nrow(x)
    x$variables <- subset(x$variables, chose)
    x$cluster <- subset(x$cluster, chose)
    x$strata <- subset(x$strata, chose)
    x$prob <- x$prob[chose]
    x$allprob <- subset(x$allprob, chose)
    x$fpc$sampsize <- subset(x$fpc$sampsize, chose)
    filter <- sprintf("%s(%s)", sum(chose), paste0(round(sum(chose)/total, 4) * 100, "%"))
    drop <- sprintf("%s(%s)", sum(!chose), paste0(round(sum(!chose)/total, 4) * 100, "%"))
    if (cat) {
        cat("\ntotal :", total)
        cat("\nfilter:", filter)
        cat("\ndrop  :", drop)
    }
    invisible(x)
}
```

## `dxa.aspx` [internal]

```r
function (url, years, items) 
{
    wait <- TRUE
    while (wait) {
        html <- tryCatch(xml2::read_html(url), error = function(e) "e")
        wait <- ifelse(is.character(html), TRUE, FALSE)
    }
    xpturl <- sprintf(do::attr_href(rvest::html_elements(set::grep_and(rvest::html_elements(html, xpath = "//table[@id=\"GridView1\"]/tbody/tr"), 
        years), xpath = "td[4]/a")), fmt = "https://wwwn.cdc.gov%s")
    docurl <- sprintf(do::attr_href(rvest::html_elements(set::grep_and(rvest::html_elements(html, xpath = "//table[@id=\"GridView1\"]/tbody/tr"), 
        years), xpath = "td[3]/a")), fmt = "https://wwwn.cdc.gov%s")
    ftablej <- as.data.frame(do::select(rvest::html_table(rvest::html_elements(html, xpath = "//table[@id=\"GridView1\"]")), 
        1, drop = TRUE))
    ftablej <- ftablej[grepl(years, ftablej$Years), ]
    cbind(years = ftablej[, 1], items, ftablej[, -1], docurl, xpturl)
}
```

## `fdup_seqn.foodcode` [internal]

```r
function (x, n = 10) 
{
    kit::countOccur(x[, c("seqn", "food.code")]) %>% arrange(desc(Count)) %>% head(n)
}
```

## `file.info2` [internal]

```r
function (file, i) 
{
    info <- file.info(file)
    yeari <- i
    itemsi <- do::Replace0(do::Replace0(rownames(info), paste0(".*", i, "/")), "/.*")
    filei <- do::Replace0(rownames(info), ".*/")
    size <- sapply(info$size, size_bt2unit)
    mtime <- as.character(info$mtime)
    data.frame(cbind(year = yeari, items = itemsi, file = filei, size = size, mtime = mtime))
}
```

## `fndds.db.food` [internal]

```r
function (..., years, start = NULL, cat = T, food.code = NULL) 
{
    d <- unique(fndds_MainFoodDesc(..., years = years, start = start, abbr = F, fortify = F, wweia = F))
    if (!is.null(food.code)) 
        d <- d[d$food.code %in% food.code, ]
    fd <- d$food.code
    attr(fd, "food.code") <- d
    if (cat) 
        print(d)
    invisible(fd)
}
```

## `fndds.db.food.and.weight` [internal]

```r
function (..., years, start = NULL, food.code = NULL, seq.num = NULL, cat = TRUE, portion.description = NULL) 
{
    years <- prepare_years(years)
    d1 <- fndds_MainFoodDesc(years = years, start = start, abbr = F, fortify = F, wweia = F, Year = TRUE)
    if (!is.null(food.code)) 
        d1 <- d1[d1$food.code %in% food.code, ]
    attr.fd <- d1
    d1 <- fndds_comp.food.Portion.Weight(data = d1)
    d1 <- d1[!d1$portion.description %in% "quantity not specified", ]
    if (cat) {
        cat("food code number:", length(unique(d1$food.code)))
        cat("\n\nseq.num")
        d1t <- table(d1$seq.num)
        print(d1t[order(as.numeric(names(d1t)))])
        if (!is.null(seq.num)) {
            df <- do::row.freq(d1[d1$seq.num %in% seq.num, c("seq.num", "portion.description")])
            df <- df[order(df$seq.num), ]
            row.names(df) <- NULL
            cat("\n")
            df
        }
    }
    if (!is.null(seq.num)) 
        d1 <- d1[d1$seq.num %in% seq.num, ]
    if (!is.null(portion.description)) 
        d1 <- d1[lookl(d1$portion.description, portion.description), ]
    d1$portion.weight <- as.numeric(d1$portion.weight)
    d1 <- d1[, c("Year", "food.code", "main.food.description", "seq.num", "portion.weight", "portion.description")]
    if (cat) {
        cat("\nFinal:")
        cat("food code number:", length(unique(d1$food.code)))
        d1t <- table(d1$seq.num)
        cat("\n")
        print(d1t[order(as.numeric(names(d1t)))])
    }
    invisible(d1)
}
```

## `fndds.mango` [internal]

```r
function (years, cat = F, food.code = NULL) 
{
    d <- unique(fndds_MainFoodDesc("mango", years = years, start = 6, abbr = F, fortify = F, wweia = F))
    if (!is.null(food.code)) 
        d <- d[d$food.code %in% food.code, ]
    if (cat) 
        message("main food description and food code:")
    if (cat) 
        cat(paste0(paste0("       ", d[, 2], "(", d[, 1], ")"), collapse = "\n"))
    if (cat) 
        cat("\n")
    fd <- d$food.code
    attr(fd, "food.code") <- d
    fd
}
```

## `food.code_used` [exported]

```r
function (d) 
{
    attr(d, "food.code")
}
```

## `forestplot.stratum_model_1` [internal]

```r
function (x, ci_position = 3, ci_wd = 18, ci_col = "gray", txt.size = 11, family = "", redtxt = T, xlim = NULL, 
    xticks = NULL, xticks_size = 1.1000000000000001, box_col = "black", box_size = 0.40000000000000002, 
    box_pch = 19, zero_wd = 1.6000000000000001, bg_color = "#f0f3f2", H1 = NULL, H2 = NULL, H3 = NULL, 
    H4 = NULL, H5 = NULL, H6 = NULL, H7 = NULL, H8 = NULL, H9 = NULL, h1 = 0, h2 = -1, h3 = 0, h4 = -1, 
    h5 = 0, h6 = 0, h7 = 0, h8 = 0, h9 = 0, file = NULL, width = par("din")[1], height = par("din")[2], 
    dpi = 300) 
{
    xi = as.data.frame(x)
    xi$`p for trend` <- NULL
    if (all(do::rm_nchar(unique(xi[, 2]), 0) %in% "ref")) {
        colnames(xi)[3] <- sprintf("%s/%s", colnames(xi)[2], colnames(xi)[3])
        xi[, 2] <- NULL
    }
    ck <- nchar(xi[, 2]) > 0
    xi$character[ck] <- paste0("    ", xi$character[ck])
    xi$` ` <- paste0(rep(" ", ci_wd), collapse = "")
    range(c(as.numeric(do::Replace0(xi[, 2], ".*\\( {0,}", " {0,},.*")), as.numeric(do::Replace0(xi[, 
        2], ".*, {0,}", "\\)"))), na.rm = T)
    hh <- c(h1, h2, h3, h4, h5, h6, h7, h8, h9)[1:ncol(xi)]
    di <- cbind(xi[, 1:(ci_position - 1), drop = F], xi[, ncol(xi), drop = F], xi[, ci_position:(ncol(xi) - 
        1)])
    for (i in 1:ncol(di)) {
        if (is.null(eval(parse(text = paste0("H", i))))) {
            eval(parse(text = sprintf("H%s <- colnames(di)[i]", i)))
        }
    }
    (HH <- c(H1, H2, H3, H4, H5, H6, H7, H8, H9))
    HH[HH %in% "p for interaction"] <- "P for\ninteraction"
    colnames(di) <- HH
    p <- forest(data = di, est = as.numeric(do::Replace0(xi[, 2], "\\(.*")), lower = as.numeric(do::Replace0(xi[, 
        2], ".*\\( {0,}", " {0,},.*")), upper = as.numeric(do::Replace0(xi[, 2], ".*, {0,}", "\\)")), 
        ci_column = ci_position, ref_line = ifelse(attr(x, "regtype") == "linear", 0, 1), sizes = box_size, 
        xlim = xlim, ticks_at = xticks, theme = forest_theme(base_family = family, base_size = txt.size, 
            core = list(bg_params = list(fill = c(bg_color[1], "white"))), colhead = list(fg_params = list(hjust = hh, 
                x = 0)), ci_pch = box_pch, ci_col = ci_col, ci_fill = box_col, ci_lwd = 1.8999999999999999, 
            ci_Theight = 0.29999999999999999, refline_gp = gpar(lwd = zero_wd, lty = "dashed", col = "grey20"), 
            xaxis_gp = gpar(lwd = 1.3, cex = xticks_size), )) %>% edit_plot(row = which(nchar(xi[, 2]) == 
        0), col = 1, gp = gpar(fontface = "bold"))
    ck.red <- sapply(xi[, 3], function(i) {
        if (nchar(i) == 0) 
            return(F)
        if (grepl("<", i)) 
            return(T)
        if (as.numeric(i) <= 0.050000000000000003) 
            return(T)
        F
    })
    if (redtxt) {
        p <- edit_plot(p, row = which(ck.red), gp = gpar(col = "red"))
    }
    if (!is.null(file)) {
        ggsave(file, p, width = width, height = height, units = "in", dpi = dpi)
        browseURL(file)
    }
    print(p)
}
```

## `forestplot.stratum_model_2` [internal]

```r
function (x, ci_position = 3, txt.size = 11, family = "", redtxt = T, bg_color = "#f0f3f2", ci_wd1 = NULL, 
    ci_wd2 = NULL, ci_wd3 = NULL, ci_wd4 = NULL, ci_wd5 = NULL, ci_wd6 = NULL, ci_wd7 = NULL, ci_wd8 = NULL, 
    ci_wd9 = NULL, ci_wd10 = NULL, xlim1 = NULL, xlim2 = NULL, xlim3 = NULL, xlim4 = NULL, xlim5 = NULL, 
    xlim6 = NULL, xlim7 = NULL, xlim8 = NULL, xlim9 = NULL, xlim10 = NULL, xticks1 = NULL, xticks2 = NULL, 
    xticks3 = NULL, xticks4 = NULL, xticks5 = NULL, xticks6 = NULL, xticks7 = NULL, xticks8 = NULL, xticks9 = NULL, 
    xticks10 = NULL, xticks_size = 10, box_col = NULL, box_size = 0.40000000000000002, zero_wd = 1.6000000000000001, 
    H1 = NULL, H2 = NULL, H3 = NULL, H4 = "P value", H5 = NULL, H6 = NULL, H7 = NULL, H8 = NULL, H9 = NULL, 
    H10 = NULL, H11 = NULL, H12 = NULL, H13 = NULL, H14 = NULL, H15 = NULL, H16 = NULL, H17 = NULL, H18 = NULL, 
    H19 = NULL, H20 = NULL, H21 = NULL, H22 = NULL, H23 = NULL, H24 = NULL, H25 = NULL, H26 = NULL, H27 = NULL, 
    H28 = NULL, H29 = NULL, H30 = NULL, H31 = NULL, H32 = NULL, H33 = NULL, H34 = NULL, H35 = NULL, H36 = NULL, 
    H37 = NULL, H38 = NULL, H39 = NULL, H40 = NULL, H41 = NULL, H42 = NULL, H43 = NULL, H44 = NULL, H45 = NULL, 
    H46 = NULL, H47 = NULL, H48 = NULL, H49 = NULL, H50 = NULL, h1 = 0, h2 = -1, h3 = 0.40000000000000002, 
    h4 = 0, h5 = -1, h6 = 0, h7 = 0, h8 = 0, h9 = 0, h10 = 0, h11 = 0, h12 = 0, h13 = 0, h14 = 0, h15 = 0, 
    h16 = 0, h17 = 0, h18 = 0, h19 = 0, h20 = 0, h21 = 0, h22 = 0, h23 = 0, h24 = 0, h25 = 0, h26 = 0, 
    h27 = 0, h28 = 0, h29 = 0, h30 = 0, h31 = 0, h32 = 0, h33 = 0, h34 = 0, h35 = 0, h36 = 0, h37 = 0, 
    h38 = 0, h39 = 0, h40 = 0, h41 = 0, h42 = 0, h43 = 0, h44 = 0, h45 = 0, h46 = 0, h47 = 0, h48 = 0, 
    h49 = 0, h50 = 0, file = NULL, width = par("din")[1], height = par("din")[2], dpi = 300) 
{
    xlim <- list(xlim1[c(1, 2)], xlim2[c(1, 2)], xlim3[c(1, 2)], xlim4[c(1, 2)], xlim5[c(1, 2)], xlim6[c(1, 
        2)], xlim7[c(1, 2)], xlim8[c(1, 2)], xlim9[c(1, 2)], xlim10)
    xlim <- xlim[!sapply(xlim, is.null)]
    if (length(xlim) == 0) 
        xlim <- NULL
    xticks <- list(xticks1, xticks2, xticks3, xticks4, xticks5, xticks6, xticks7, xticks8, xticks9, xticks10)
    xticks <- xticks[!sapply(xticks, is.null)]
    if (length(xticks) == 0) 
        xticks <- NULL
    ci_wd <- c(ci_wd1, ci_wd2, ci_wd3, ci_wd4, ci_wd5, ci_wd6, ci_wd7, ci_wd8, ci_wd9, ci_wd10)
    if (is.null(ci_wd)) 
        ci_wd <- 10
    (xi <- data.frame(x, check.names = F))
    for (i in 1:ncol(xi)) {
        if (any(xi[, i] == "ref")) {
            (break)(i)
        }
    }
    (ref <- colnames(xi)[i])
    xi[, i] <- NULL
    xi[nchar(xi[, 2]) > 0, 1] <- paste0("    ", xi[nchar(xi[, 2]) > 0, 1])
    (px <- which(colnames(x) == "p") - 1)
    nuor <- do::Replace0(xi[, px - 1, drop = F], "\\(.*", " ")
    for (i in 1:ncol(nuor)) {
        nuor[, i] <- as.numeric(nuor[, i])
    }
    nupa <- do::complete.data(as.numeric(do::rm_nchar(unique(unlist(c(nuor))), 0)))
    for (i in 1:nrow(nuor)) {
        if (!is.na(nuor[i, 1])) {
            (qe <- quantile(0:1, (1:ncol(nuor))/ncol(nuor)) * box_size[1])
            names(qe) <- NULL
            nuor[i, ] <- qe[order(as.numeric(nuor[i, ]))]
        }
    }
    nuor_color <- nuor
    if (is.null(box_col)) {
        (plt <- colorRampPalette(c("#e8ea68", "green", "red"))(ncol(nuor)))
    }
    else {
        (plt <- colorRampPalette(box_col)(ncol(nuor)))
    }
    for (i in 1:nrow(nuor_color)) {
        if (!is.na(nuor[i, 1])) {
            nuor_color[i, ] <- plt[order(as.numeric(nuor[i, ]))]
        }
    }
    (px1 <- px + (0:(length(px) - 1)))
    for (ii in 1:length(px1)) {
        i <- px1[ii]
        xi <- data.frame(xi[, 1:(i - 1), drop = F], ` ` = paste0(rep(" ", ifelse(is.na(ci_wd[ii]), ci_wd[1], 
            ci_wd[ii])), collapse = ""), xi[, i:ncol(xi), drop = F], check.names = F)
        colnames(xi)[i] <- paste0(colnames(xi)[i - 1], " Vs ", ref)
        colnames(xi)[i - 1] <- "95% CI"
    }
    colnames(xi)[colnames(xi) %in% paste0("p.", 1:ncol(xi))] <- "p"
    colnames(xi)[colnames(xi) %in% paste0("95% CI.", 1:ncol(xi))] <- "95% CI"
    for (i in 1:ncol(xi)) {
        if (is.null(eval(parse(text = paste0("H", i))))) {
            eval(parse(text = sprintf("H%s <- colnames(xi)[i]", i)))
        }
    }
    HH <- c(H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16, H17, H18, H19, H20, 
        H21, H22, H23, H24, H25, H26, H27, H28, H29, H30, H31, H32, H33, H34, H35, H36, H37, H38, H39, 
        H40, H41, H42, H43, H44, H45, H46, H47, H48, H49, H50)
    HH <- do::Replace0(HH, " {0,}\\(.*")
    HH[HH %in% "p for trend"] <- "P for\ntrend"
    HH[HH %in% "p for interaction"] <- "P for\ninteraction"
    hh <- c(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, 
        h21, h22, h23, h24, h25, h26, h27, h28, h29, h30, h31, h32, h33, h34, h35, h36, h37, h38, h39, 
        h40, h41, h42, h43, h44, h45, h46, h47, h48, h49, h50)[1:ncol(xi)]
    (est <- lapply(px1, function(i) {
        as.numeric(do::Replace0(xi[, i - 1], "\\(.*", " "))
    }))
    (lower <- lapply(px1, function(i) {
        as.numeric(do::Replace0(xi[, i - 1], ".*\\(", ",.*", " "))
    }))
    (upper <- lapply(px1, function(i) {
        as.numeric(do::Replace0(xi[, i - 1], ".*,", "\\)", " "))
    }))
    colnames(xi) <- HH
    p <- forest(data = xi, est = est, lower = lower, upper = upper, ci_column = px1, ticks_at = xticks, 
        xlim = xlim, sizes = 0.40000000000000002, ref_line = ifelse(attr(x, "regtype") == "linear", 0, 
            1), theme = forest_theme(base_family = family, base_size = 9, core = list(bg_params = list(fill = c(bg_color[1], 
            "white"))), colhead = list(fg_params = list(hjust = hh, x = 0)), ci_pch = 19, ci_col = "gray", 
            ci_lwd = 1.8999999999999999, ci_Theight = 0.29999999999999999, refline_gp = gpar(lwd = zero_wd, 
                lty = "dashed", col = "grey20"), xaxis_gp = gpar(lwd = 1.3, cex = 1, fontsize = xticks_size))) %>% 
        edit_plot(row = which(nchar(xi[, 2]) == 0), col = 1, gp = gpar(fontface = "bold"))
    for (i in 1:length(px1)) {
        name <- unlist(lapply(px1[i], function(i) paste0("ci-", 1:nrow(xi), "-", i, "-")))
        (id <- which(grepl(paste0(name, collapse = "|"), p$layout$name)))
        for (j in 1:length(id)) {
            p$grobs[[id[j]]]$size <- do::complete.data(nuor[, i])[j]
        }
    }
    for (i in 1:length(px1)) {
        name <- unlist(lapply(px1[i], function(i) paste0("ci-", 1:nrow(xi), "-", i, "-")))
        (id <- which(grepl(paste0(name, collapse = "|"), p$layout$name)))
        for (j in 1:length(id)) {
            p$grobs[[id[j]]]$gp$fill <- do::complete.data(nuor_color[, i])[j]
        }
    }
    if (redtxt) {
        for (i in (px1 + 1)) {
            ck.red <- sapply(xi[, i], function(i) {
                if (nchar(i) == 0) 
                  return(F)
                if (grepl("<", i)) 
                  return(T)
                if (as.numeric(i) <= 0.050000000000000003) 
                  return(T)
                F
            })
            p <- edit_plot(p, row = which(ck.red), col = c(i - 2, i), gp = gpar(col = "red"))
        }
    }
    file <- paste0(tempfile(), ".pdf")
    ggsave(file, p, width = width, height = height, dpi = dpi)
    browseURL(file)
}
```

## `funique.noNA` [internal]

```r
function (x) 
{
    x <- kit::funique(x)
    if (anyNA(x)) {
        x[!is.na(x)]
    }
    else {
        x
    }
}
```

## `getChangepoints.m1` [internal]

```r
function (r, range = NULL) 
{
    (rcsx <- attr(r, "rcsx"))
    if (".predictor." %in% colnames(r)) 
        r <- r[r$.predictor. %in% rcsx, ]
    if (!is.null(range)) 
        r <- r[r[, rcsx] >= min(range) & r[, rcsx] <= max(range), ]
    res <- unique(do.call(sapply(2:(nrow(r) - 1), function(i) {
        (y0 <- r$yhat[i] - r$yhat[i - 1])
        (x0 <- r[, rcsx][i] - r[, rcsx][i - 1])
        (delt1 <- y0/x0)
        y2 <- r$yhat[i + 1] - r$yhat[i]
        x2 <- r[, rcsx][i + 1] - r[, rcsx][i]
        delt2 <- y2/x2
        if (delt1 * delt2 < 0) 
            return(r[i, ])
        if (delt2 == 0) 
            return(r[i + 1, ])
    }), what = rbind))
    res[, c(rcsx, "yhat", "lower", "upper", "modelName", "rcsName", "method", "Ref")]
}
```

## `getChangepoints.m1by` [internal]

```r
function (r, range = NULL) 
{
    (rcsx <- attr(r, "rcsx"))
    if (".predictor." %in% colnames(r)) 
        (r <- r[r$.predictor. %in% rcsx, ])
    (by <- attr(r, "by"))
    if (!is.null(range)) 
        r <- r[r[, rcsx] >= min(range) & r[, rcsx] <= max(range), ]
    if (length(by) == 1) 
        byp = r[, by]
    else byp = do::paste0_columns(r[, by], collapse = ";;;")
    (byu <- as.character(unique(byp)))
    res <- do.call(lapply(byu, function(bi) {
        (ri <- r[byp %in% bi, ])
        si <- do.call(lapply(2:(nrow(ri) - 1), function(i) {
            y0 <- ri$yhat[i] - ri$yhat[i - 1]
            x0 <- ri[, rcsx][i] - ri[, rcsx][i - 1]
            (delt1 <- y0/x0)
            y2 <- ri$yhat[i + 1] - ri$yhat[i]
            x2 <- ri[, rcsx][i + 1] - ri[, rcsx][i]
            (delt2 <- y2/x2)
            if (delt1 * delt2 * 10000000 < 0) {
                return(ri[i, ])
            }
            else if (delt2 == 0) {
                return(ri[i + 1, ])
            }
        }), what = rbind)
        if (is.null(si)) {
            message(paste0(bi, tmcn::toUTF8("<U+6CA1><U+6709><U+5207><U+70B9>")))
        }
        si
    }), what = rbind)
    res[, c(rcsx, by, "yhat", "lower", "upper", "modelName", "rcsName", "method", "Ref")]
}
```

## `getReference.m1` [internal]

```r
function (r) 
{
    if (any(r$method %in% c("cph", "lrm"))) {
        minrow <- which.min(abs(r$yhat - 1))
        r[minrow, ]
    }
    else if (any(r$method %in% c("ols"))) {
        minrow <- which.min(abs(r$yhat - 0))
        r[minrow, ]
    }
}
```

## `getReference.m1by` [internal]

```r
function (r) 
{
    by <- attr(r, "by")
    if (length(by) == 1) 
        byp = r[, by]
    else byp = do::paste0_columns(r[, by], collapse = ";;;")
    byu <- unique(byp)
    do.call(lapply(byu, function(i) {
        ck <- byp %in% i
        di <- r[ck, ]
        if (any(di$method %in% c("cph", "lrm"))) {
            minrow <- which.min(abs(r$yhat - 1))
            di[minrow, ]
        }
        else if (any(di$method %in% c("ols"))) {
            minrow <- which.min(abs(di$yhat - 0))
            di[minrow, ]
        }
    }), what = rbind)
}
```

## `ggplot.m1` [internal]

```r
function (data, mapping, ..., environment = parent.frame(), vline = TRUE, hline = TRUE, point = FALSE, 
    ylab = NULL, xlab = NULL, color = "red") 
{
    (x = unique(data$rcsName))
    if (".predictor." %in% colnames(data)) 
        data <- data[data$.predictor. == x, ]
    p <- ggplot() + geom_line(data = data, aes_string(x, "yhat"), linetype = "solid", size = 1, alpha = 0.69999999999999996, 
        colour = color) + geom_ribbon(data = data, aes_string(x, ymin = "lower", ymax = "upper"), alpha = 0.10000000000000001, 
        fill = color) + theme_classic()
    if (isTRUE(vline)) {
        p <- p + geom_vline(xintercept = unique(data$Ref), linetype = 2)
        px <- unique(data$Ref)
    }
    else if (is.numeric(vline)) {
        p <- p + geom_vline(xintercept = vline, linetype = 2)
        px <- vline
    }
    if (isTRUE(hline)) {
        py <- ifelse(attr(data, "log"), 0, 1)
        p <- p + geom_hline(yintercept = py, size = 0.75, linetype = 2)
    }
    else if (is.numeric(hline)) {
        p <- p + geom_hline(yintercept = hline, size = 0.75, linetype = 2)
        py <- hline
    }
    if (is.null(ylab)) 
        ylab <- attr(data, "ylab")
    if (point) 
        p <- p + geom_point(aes(x = px, y = py), size = 2)
    if (!is.null(ylab)) 
        p <- p + ylab(ylab)
    if (!is.null(xlab)) 
        p <- p + xlab(xlab)
    p
}
```

## `ggplot.m1by` [internal]

```r
function (data, mapping, ..., environment = parent.frame(), vline = TRUE, hline = TRUE, point = FALSE, 
    ylab = NULL, xlab = NULL, text = TRUE) 
{
    (x = unique(data$rcsName))
    if (".predictor." %in% colnames(data)) 
        data <- data[data$.predictor. %in% x, ]
    (by = attr(data, "by"))
    p <- ggplot() + geom_line(data = data, aes_string(x, "yhat", group = by, color = by), linetype = "solid", 
        size = 1, alpha = 0.69999999999999996) + geom_ribbon(data = data, aes_string(x, group = by, ymin = "lower", 
        ymax = "upper", fill = by), alpha = 0.10000000000000001) + theme_classic()
    p
    legend.color <- data.frame(colours = unique(ggplot_build(p)$data[[1]]["colour"]), label = ggplot_build(p)$plot$scales$scales[[1]]$get_labels())
    if (isTRUE(vline)) {
        p <- p + geom_vline(xintercept = unique(data[, c(by, "Ref")])$Ref, linetype = 2)
        px <- unique(data[, c(by, "Ref")])$Ref
    }
    else if (is.numeric(vline)) {
        p <- p + geom_vline(xintercept = vline, linetype = 2)
        px <- vline
    }
    else {
        px <- unique(data[, c(by, "Ref")])$Ref
    }
    if (isTRUE(hline)) {
        py <- ifelse(attr(data, "log"), 0, 1)
        p <- p + geom_hline(yintercept = py, size = 0.75, linetype = 2)
    }
    else if (is.numeric(hline)) {
        p <- p + geom_hline(yintercept = hline, size = 0.75, linetype = 2)
        py <- hline
    }
    else {
        py <- ifelse(do::left(ylab, 3) == "log", 0, 1)
    }
    if (point) 
        p <- p + geom_point(aes(x = px, y = py), size = 2)
    if (is.null(ylab)) 
        ylab <- attr(data, "ylab")
    if (!is.null(ylab)) 
        p <- p + ylab(ylab)
    if (!is.null(xlab)) 
        p <- p + xlab(xlab)
    if (text) {
        p <- p + ggrepel::geom_text_repel(aes(px, py, label = paste0(unique(data[[by]]), ":", round(px))))
    }
    p
}
```

## `iff.fode.code` [internal]

```r
function (years, day = 1, start = NULL) 
{
    tsv <- sprintf("drxiff|dr%siff", day)
    tsv <- nhs_tsv(tsv, cat = F, years = years)
    d <- nhs_read(tsv, "seqn", cat = F)
    d <- rename_fdcd(d, "food.code")[, c("Year", "food.code")]
    if (!is.null(start)) 
        d <- d[do::left(d$food.code, nchar(start)) %in% start, ]
    d <- unique(d)
    row.names(d) <- NULL
    d
}
```

## `iff.gram.kcl` [internal]

```r
function (years, day) 
{
    iff1 <- nhs_tsv(paste0(day, "iff|xiff"), years = years, cat = FALSE)
    dr1 <- nhs_read(iff1, "drxigrms,dr1igrms,dr2igrms:gram", "drxikcal,dr1ikcal,dr2ikcal:kcal", cat = FALSE)
    if (all(c("drdifdcd", "dr2ifdcd") %in% colnames(dr1))) {
        dr1$dr2ifdcd[is.na(dr1$dr2ifdcd)] <- dr1$drdifdcd[is.na(dr1$dr2ifdcd)]
        dr1 <- drop_col(dr1, "drdifdcd")
    }
    if (all(c("drdifdcd", "dr1ifdcd") %in% colnames(dr1))) {
        dr1$dr1ifdcd[is.na(dr1$dr1ifdcd)] <- dr1$drdifdcd[is.na(dr1$dr1ifdcd)]
        dr1 <- drop_col(dr1, "drdifdcd")
    }
    col_rename(dr1) <- c("dr1ifdcd:food.code", "dr2ifdcd:food.code", "drdifdcd:food.code")
    dr1[, c("Year", "food.code", "seqn", "gram", "kcal")]
}
```

## `make.formula` [internal]

```r
function (names) 
{
    formula(paste("~", paste(names, collapse = "+")))
}
```

## `md.pattern` [exported]

```r
function (data) 
{
    if (is.data.frame(data)) {
        for (i in unique(data$Year)) {
            cat(crayon::red(i), "\n")
            x <- mice::md.pattern(plot = FALSE, data[data$Year == i, set::not(colnames(data), "Year", 
                "seqn", "sdmvpsu", "sdmvstra")])
            print(t(x))
        }
        cat(crayon::red("Overall\n"))
        x <- mice::md.pattern(plot = FALSE, data[, set::not(colnames(data), "Year", "seqn", "sdmvpsu", 
            "sdmvstra")])
        print(t(x))
    }
    else {
        for (i in 1:length(data)) {
            cat(crayon::red(names(data)[i]), "\n")
            x <- mice::md.pattern(plot = FALSE, data[[i]][, set::not(colnames(data[[i]]), "Year", "seqn", 
                "sdmvpsu", "sdmvstra")])
            print(t(x))
        }
        cat(crayon::red("Overall\n"))
        data <- do.call(plyr::rbind.fill, data)
        x <- mice::md.pattern(plot = FALSE, data[, set::not(colnames(data), "Year", "seqn", "sdmvpsu", 
            "sdmvstra")])
        print(t(x))
    }
}
```

## `md.value` [exported]

```r
function (data) 
{
    if (!is.data.frame(data)) {
        for (i in 1:length(data)) {
            data[[i]] <- cbind(Year = names(data)[i], data[[i]])
        }
        data <- do.call(plyr::rbind.fill, data)
    }
    ms <- do.call(lapply(unique(data$Year), function(i) {
        as.data.frame(t(sapply(set::not(colnames(data), "Year", "seqn", "sdmvpsu", "sdmvstra"), function(j) {
            round((sum(is.na(data[data$Year == i, j]))/length(data[data$Year == i, j]) * 100), 2)
        })))
    }), what = plyr::rbind.fill)
    row.names(ms) <- unique(data$Year)
    oa <- data.frame(t(round((colSums(is.na(data[, set::not(colnames(data), "Year", "seqn", "sdmvpsu", 
        "sdmvstra")]))/nrow(data) * 100), 2)), row.names = "overall")
    rbind(oa, ms)
}
```

## `milk.food.code` [internal]

```r
function (years, food.code = NULL) 
{
    years <- prepare_years(years)
    unique(fndds_MainFoodDesc(years = years, start = 1, Year = T, abbr = F, fortify = F, wweia = F))
}
```

## `model.data` [internal]

```r
function (fit, data = NULL) 
{
    if (!is.null(data)) 
        return(data)
    if (any(c("svyglm", "svycoxph") %in% class(fit))) 
        return(fit$survey.design$variables)
    eval(fit$call$data, envir = parent.frame())
}
```

## `mutate.survey.design` [internal]

```r
function (.data, ...) 
{
    .data$variables <- mutate(.data$variables, ...)
    .data
}
```

## `nhs.iff.food.code` [internal]

```r
function (years, day = 1, food.code = NULL) 
{
    iff1 <- nhs_tsv(paste0(day, "iff|xiff"), years = years, cat = FALSE)
    dr1 <- nhs_read(iff1, "drxigrms,dr1igrms,dr2igrms:grms", "drxikcal,dr1ikcal,dr2ikcal:kcal", cat = FALSE)
    if (all(c("drdifdcd", "dr2ifdcd") %in% colnames(dr1))) {
        dr1$dr2ifdcd[is.na(dr1$dr2ifdcd)] <- dr1$drdifdcd[is.na(dr1$dr2ifdcd)]
        dr1 <- drop_col(dr1, "drdifdcd")
    }
    if (all(c("drdifdcd", "dr1ifdcd") %in% colnames(dr1))) {
        dr1$dr1ifdcd[is.na(dr1$dr1ifdcd)] <- dr1$drdifdcd[is.na(dr1$dr1ifdcd)]
        dr1 <- drop_col(dr1, "drdifdcd")
    }
    col_rename(dr1) <- "dr1ifdcd,dr2ifdcd,drdifdcd:food.code"
    ck <- dr1$food.code %in% food.code
    dr1$grms[!ck & !is.na(dr1$grms)] <- 0
    dr1$kcal[!ck & !is.na(dr1$kcal)] <- 0
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d <- aggregate2(data = dr1, x = c("kcal", "grms"), by = c("Year", "seqn"), fun = ".sum.nona")
    d <- d[, c("Year", "seqn", "grms", "kcal")]
    attr(d, "food.code") <- attr(food.code, "food.code")
    d
}
```

## `nhs.pubmed` [exported]

```r
function (...) 
{
    DBkey = "((National Health and Nutrition Examination Survey[Title/Abstract]) OR (NHANES[Title/Abstract]))"
    keys <- c(...)
    if (is.null(keys)) {
        key <- DBkey
    }
    else {
        key <- sprintf("(%s) AND %s", paste0(sprintf("(%s[Title/Abstract])", keys), collapse = " AND "), 
            DBkey)
    }
    (url <- sprintf("https://pubmed.ncbi.nlm.nih.gov/?term=(%s)&sort=date&size=200", URLencode(key)))
    browseURL(url)
}
```

## `nhs.pubmed_title` [exported]

```r
function (...) 
{
    DBkey = "((National Health and Nutrition Examination Survey[Title/Abstract]) OR (NHANES[Title/Abstract]))"
    keys <- c(...)
    if (is.null(keys)) {
        key <- DBkey
    }
    else {
        key <- sprintf("(%s) AND %s", paste0(sprintf("(%s[Title])", keys), collapse = " AND "), DBkey)
    }
    (url <- sprintf("https://pubmed.ncbi.nlm.nih.gov/?term=(%s)&sort=date&size=200", URLencode(key)))
    browseURL(url)
}
```

## `optimal_nKnots.default` [internal]

```r
function (fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F) 
{
    if (class(fit)[1] == "svytableone") 
        fit <- attr(fit, "fit")
    (rcsx <- rcsx(fit))
    if (length(rcsx) != 1) {
        if (length(rcsx) == 0) {
            if (do::cnOS()) 
                stop("<U+6A21><U+578B><U+4E2D><U+6CA1><U+6709><U+8FDB><U+884C>RCS")
            if (!do::cnOS()) 
                stop("no rcs() was conducted in the model")
        }
        else {
            if (do::cnOS()) 
                stop("<U+4EC5><U+652F><U+6301><U+4E00><U+4E2A>rcs")
            if (!do::cnOS()) 
                stop("only one rcs() was supported")
        }
    }
    s2r <- svy2rms(fit)
    if (is.null(data)) 
        data = s2r[[2]]
    fit <- s2r[[1]]
    old <- options()
    if (is.null(by)) {
        options(datadist = rms::datadist(data))
        fs <- do.call(lapply(n, function(i) {
            if (cat) 
                cat("\n", i)
            uf <- updateKnot(fit, i, data = data)
            d1 <- do::give_names(data.frame(matrix(i, nrow = 1)), paste0(rcsx, "_knot"))
            d2 <- tryCatch(data.frame(AIC = AIC(uf), P_nonlinear = anova(uf)[" Nonlinear", "P"]), error = function(e) "e")
            if (is.data.frame(d2)) 
                cbind(d1, d2)
        }), what = rbind)
        row.names(fs) <- NULL
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        fs$min <- ""
        if (any(fs$P_nonlinear <= 0.050000000000000003)) {
            ck <- fs$P_nonlinear <= 0.050000000000000003
            p <- fs$P_nonlinear
            p[!ck] <- 10
            fs$min[which.min(p)] <- "***"
        }
        else {
            fs$min[which.min(fs$AIC)] <- "***"
        }
        fs$sig <- ifelse(fs$P_nonlinear < 0.050000000000000003, "<0.05", ">=0.05")
        if (plot) {
            p <- ggplot(fs, aes_string(paste0(rcsx, "_knot"), "AIC", color = "sig")) + geom_point() + 
                geom_line() + scale_x_continuous(breaks = n)
            plot(p)
        }
        if (cat) 
            cat("\n\n")
        fs
    }
    else {
        if (length(by) == 1) 
            bycat = data[, by]
        else bycat = do::paste0_columns(data[, by], ";;;")
        byu <- unique(bycat)
        (byu <- as.character(byu[!is.na(byu)]))
        res <- do.call(lapply(byu, function(bi) {
            di <- data[bycat %in% bi, ]
            options(datadist = suppressWarnings(rms::datadist(di)))
            ei <- eval(parse(text = sprintf("update(fit,formula. = .~. - %s, data=di)", paste0(by, collapse = " - "))))
            fs <- do.call(lapply(1:length(n), function(i) {
                if (i == 1 & cat) 
                  cat("\n")
                if (cat) 
                  cat(paste0(n[i]), ", ")
                if (i == length(n) & cat) 
                  cat("\n")
                uf <- updateKnot(ei, n[i], data = di)
                d1 <- do::give_names(data.frame(matrix(n[i], nrow = 1)), paste0(rcsx, "_knot"))
                d2 <- data.frame(AIC = AIC(uf), P_nonlinear = anova(uf)[" Nonlinear", "P"])
                cbind(d1, d2)
            }), what = rbind)
            fs <- cbind(do::col_split(bi, ";;;", colnames = by), fs)
            fs$min <- ""
            if (any(fs$P_nonlinear <= 0.050000000000000003)) {
                ck <- fs$P_nonlinear <= 0.050000000000000003
                p <- fs$P_nonlinear
                p[!ck] <- 10
                fs$min[which.min(p)] <- "***"
            }
            else {
                fs$min[which.min(fs$AIC)] <- "***"
            }
            if (cat) 
                cat("\n\n")
            fs
        }), what = rbind)
        row.names(res) <- NULL
        res$sig <- ifelse(res$P_nonlinear <= 0.050000000000000003, " <0.05", ">=0.05")
        if (plot) {
            if (length(by == 1)) {
                res$bycat <- paste0(by, "=", res[, by])
            }
            else {
                res$bycat <- do::paste0_columns(do.call(apply(by, function(i) {
                  paste0(i, "=", res[, i])
                }), what = cbind), collapse = ", ")
            }
            p <- ggplot(res, aes_string(paste0(rcsx, "_knot"), "AIC", color = "sig")) + geom_point() + 
                geom_line() + scale_x_continuous(breaks = n) + facet_wrap(~bycat, scales = "free")
            plot(p)
            res <- res[, -ncol(res)]
        }
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        res
    }
}
```

## `optimal_nKnots.svycoxph` [internal]

```r
function (fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F) 
{
    if (class(fit)[1] == "svytableone") 
        fit <- attr(fit, "fit")
    svyfit <- svy2rms(fit)
    optimal_nKnots(fit = svyfit$fit, n = n, by = by, plot = plot, title = title, cat = cat, data = svyfit[[2]])
}
```

## `optimal_nKnots.svyglm` [internal]

```r
function (fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F) 
{
    if (class(fit)[1] == "svytableone") 
        fit <- attr(fit, "fit")
    s2r <- svy2rms(fit)
    optimal_nKnots(fit = s2r[[1]], n = n, by = by, plot = plot, title = title, cat = cat, data = s2r[[2]])
}
```

## `paste_dcn.icn` [internal]

```r
function (x, key = "rxddcn") 
{
    funi <- function(xi) {
        xi <- do::rm_nchar(do::unique_no.NA(xi), 1)
        paste0(xi, collapse = ";")
    }
    nmx <- set::grep_and(colnames(x), key)
    x <- x[, nmx, drop = FALSE]
    apply(x, 1, funi)
}
```

## `pkg.tgz2zip` [internal]

```r
function () 
{
    rawpath <- getwd()
    devtools::document()
    devtools::build(binary = T)
    if (do::is.windows()) {
        fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T)
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        zip <- paste0(do::knife_right(f1, 3), "zip")
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("winrar x \"%s\" \"%s\"", f1, forwin))
        system(st)
        pkg <- list.files(forwin, full.names = T)
        (st <- sprintf("winrar a -ep1 \"%s\" \"%s\"", paste0(do::knife_right(f1, 3), "zip"), pkg))
        a = system(st)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    else {
        pkg <- "nhanesR"
        if (do::right(getwd(), nchar(pkg)) != pkg) 
            stop("<U+8DEF><U+5F84><U+4E0D><U+662F><U+7A0B><U+5E8F><U+5305><U+7684><U+540D><U+5B57>")
        (fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T))
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (fs <- do::Replace(fs, "//", "/"))
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        (zip <- paste0(do::knife_right(f1, 3), "zip"))
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("tar -xvzf %s -C %s", f1, forwin))
        a = system(st, intern = T)
        (st <- sprintf("cd %s && zip -r %s %s", forwin, zip, pkg))
        a = system(st, intern = T)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    (fs2 <- paste0(do::file.dir(zip), "2github"))
    message("===windows===")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    dir.create(fs2, recursive = T, showWarnings = F)
    setwd(fs2)
    file.copy(zip, fs2)
    system(paste0("cd ", fs2))
    system("git config --global user.email \"zj391120@163.com\"")
    system("git config --global user.name \"zhangjing\"")
    system("git init")
    system(paste0("git add ", do::file.name(zip)))
    system("git commit -m \"update\"")
    system("git branch -M main")
    system("git remote add origin https://github.com/yikeshu0611/nhanesR_win.git")
    system("git remote set-url origin git@nhanes.github.com:yikeshu0611/nhanesR_win.git")
    system("git push -u origin main --force")
    message("===mac===")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    dir.create(fs2, recursive = T, showWarnings = F)
    setwd(fs2)
    file.copy(f1, fs2)
    system(paste0("cd ", fs2))
    system("git init")
    system(paste0("git add ", do::file.name(f1)))
    system("git commit -m \"update\"")
    system("git branch -M main")
    system("git remote add origin https://github.com/yikeshu0611/nhanesR_mac.git")
    system("git remote set-url origin git@nhanes.github.com:yikeshu0611/nhanesR_mac.git")
    system("git push -u origin main --force")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    setwd(rawpath)
}
```

## `pkg.tgz2zip_mac` [internal]

```r
function () 
{
    rawpath <- getwd()
    devtools::document()
    devtools::build(binary = T)
    if (do::is.windows()) {
        fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T)
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        zip <- paste0(do::knife_right(f1, 3), "zip")
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("winrar x \"%s\" \"%s\"", f1, forwin))
        system(st)
        pkg <- list.files(forwin, full.names = T)
        (st <- sprintf("winrar a -ep1 \"%s\" \"%s\"", paste0(do::knife_right(f1, 3), "zip"), pkg))
        a = system(st)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    else {
        pkg <- "nhanesR"
        if (do::right(getwd(), nchar(pkg)) != pkg) 
            stop("<U+8DEF><U+5F84><U+4E0D><U+662F><U+7A0B><U+5E8F><U+5305><U+7684><U+540D><U+5B57>")
        (fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T))
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (fs <- do::Replace(fs, "//", "/"))
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        (zip <- paste0(do::knife_right(f1, 3), "zip"))
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("tar -xvzf %s -C %s", f1, forwin))
        a = system(st, intern = T)
        (st <- sprintf("cd %s && zip -r %s %s", forwin, zip, pkg))
        a = system(st, intern = T)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    (fs2 <- paste0(do::file.dir(zip), "2github"))
    message("===mac===")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    dir.create(fs2, recursive = T, showWarnings = F)
    setwd(fs2)
    file.copy(f1, fs2)
    system(paste0("cd ", fs2))
    system("git config --global user.email \"zj391120@163.com\"")
    system("git config --global user.name \"zhangjing\"")
    system("git init")
    system(paste0("git add ", do::file.name(f1)))
    system("git commit -m \"update\"")
    system("git branch -M main")
    system("git remote add origin https://github.com/yikeshu0611/nhanesR_mac.git")
    system("git remote set-url origin git@nhanes.github.com:yikeshu0611/nhanesR_mac.git")
    system("git push -u origin main --force")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    setwd(rawpath)
}
```

## `pkg.tgz2zip_win` [internal]

```r
function () 
{
    rawpath <- getwd()
    devtools::document()
    devtools::build(binary = T)
    if (do::is.windows()) {
        fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T)
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        zip <- paste0(do::knife_right(f1, 3), "zip")
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("winrar x \"%s\" \"%s\"", f1, forwin))
        system(st)
        pkg <- list.files(forwin, full.names = T)
        (st <- sprintf("winrar a -ep1 \"%s\" \"%s\"", paste0(do::knife_right(f1, 3), "zip"), pkg))
        a = system(st)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    else {
        pkg <- "nhanesR"
        if (do::right(getwd(), nchar(pkg)) != pkg) 
            stop("<U+8DEF><U+5F84><U+4E0D><U+662F><U+7A0B><U+5E8F><U+5305><U+7684><U+540D><U+5B57>")
        (fs <- list.files(do::upper.dir(getwd()), "tgz", full.names = T))
        if (length(fs) == 0) 
            stop("<U+6CA1><U+6709>tgz<U+7A0B><U+5E8F><U+5305>")
        (fs <- do::Replace(fs, "//", "/"))
        (f1 <- fs[which.max(file.info(fs)$mtime)])
        (zip <- paste0(do::knife_right(f1, 3), "zip"))
        if (file.exists(zip)) 
            file.remove(zip)
        forwin <- paste0(do::upper.dir(getwd()), "forwin")
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
        fs::dir_create(forwin)
        (st <- sprintf("tar -xvzf %s -C %s", f1, forwin))
        a = system(st, intern = T)
        (st <- sprintf("cd %s && zip -r %s %s", forwin, zip, pkg))
        a = system(st, intern = T)
        if (dir.exists(forwin)) 
            fs::dir_delete(forwin)
    }
    (fs2 <- paste0(do::file.dir(zip), "2github"))
    message("===windows===")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    dir.create(fs2, recursive = T, showWarnings = F)
    setwd(fs2)
    file.copy(zip, fs2)
    system(paste0("cd ", fs2))
    system("git config --global user.email \"zj391120@163.com\"")
    system("git config --global user.name \"zhangjing\"")
    system("git init")
    system(paste0("git add ", do::file.name(zip)))
    system("git commit -m \"update\"")
    system("git branch -M main")
    system("git remote add origin https://github.com/yikeshu0611/nhanesR_win.git")
    system("git remote set-url origin git@nhanes.github.com:yikeshu0611/nhanesR_win.git")
    system("git push -u origin main --force")
    if (dir.exists(fs2)) 
        fs::dir_delete(fs2)
    setwd(rawpath)
}
```

## `print.svy_roc` [internal]

```r
function (x, ...) 
{
    print(as.numeric(x))
}
```

## `pvalue.digit` [internal]

```r
function (p, round = 3) 
{
    if (p < 0.0001) {
        "< 0.0001"
    }
    else if (p < 0.001) {
        "< 0.001"
    }
    else {
        (p0 <- round(p, round))
        while (p0 == 0) {
            round = round + 1
            p0 <- round(p, round)
        }
        p0
    }
}
```

## `pvalue.format` [internal]

```r
function (x, round = 2) 
{
    if (x < 0.0001) {
        "<0.0001"
    }
    else if (x < 0.001) {
        "<0.001"
    }
    else if (x < 0.01) {
        "<0.01"
    }
    else {
        digit(janitor::round_half_up(x, round), round)
    }
}
```

## `quant.median` [exported]

```r
function (x, n, round = 3, cat = TRUE) 
{
    if (n == 1) 
        stop("n must be >= 2")
    s <- sprintf("quantile(x,c(%s),na.rm = TRUE)", paste0(paste0(rep(1:(n - 1), 1), "/", n), collapse = ","))
    cut <- round(eval(parse(text = s)), 3)
    cuts <- c(min(x, na.rm = TRUE), cut, max(x, na.rm = TRUE))
    x2 <- rep(NA, length(x))
    lev <- c()
    for (i in 1:(length(cuts) - 1)) {
        if (i == 1) {
            (levi <- sprintf("[%s,%s]", cuts[i], cuts[i + 1]))
            lev <- c(lev, levi)
            ck <- x <= cuts[i + 1]
            (md <- median(x[ck], na.rm = T))
            x2[ck] <- round(md, round)
        }
        else if (i < (length(cuts) - 1)) {
            levi <- sprintf("(%s,%s]", cuts[i], cuts[i + 1])
            ck <- x > cuts[i] & x <= cuts[i + 1]
            (md <- median(x[ck], na.rm = T))
            x2[ck] <- round(md, round)
            lev <- c(lev, levi)
        }
        else if (i == (length(cuts) - 1)) {
            levi <- sprintf("(%s,%s]", cuts[i], cuts[i + 1])
            lev <- c(lev, levi)
            ck <- x > cuts[i]
            (md <- median(x[ck], na.rm = T))
            x2[ck] <- round(md, round)
        }
    }
    if (cat) {
        (tb <- as.data.frame(table(x2, useNA = "i")))
        colnames(tb)[1] <- paste0(deparse(substitute(x)), collapse = "")
        tb$Per <- paste0(round(tb$Freq/sum(tb$Freq) * 100, 2), "%")
        colnames(tb)[1] <- "median"
        tb <- cbind(range = NA, tb)
        tb$range[1:length(lev)] <- lev
        print(tb)
    }
    x2
}
```

## `rename.survey.design` [internal]

```r
function (.data, ...) 
{
    qs <- rlang::quos(...)
    (expr <- sapply(1:length(qs), function(i) deparse(qs[[i]][[2]])))
    notchag <- c(deparse(.data$call$weights[[2]]), deparse(.data$call$id[[2]]), deparse(.data$call$strata[[2]]))
    if (any(expr %in% notchag)) {
        stop(paste0(tmcn::toUTF8("<U+4E0D><U+53EF><U+4EE5><U+4FEE><U+6539>: "), paste0(notchag, collapse = ", ")))
    }
    .data$variables <- dplyr::rename(.data$variables, ...)
    invisible(.data)
}
```

## `row.counts` [exported]

```r
function (data) 
{
    rowSums(!is.na(data))
}
```

## `row.max` [exported]

```r
function (x, na.rm = T) 
{
    if (is.data.frame(x)) {
        data <- apply(x, 1, max)
        if (anyNA(data)) {
            ii <- which.na(data)
            for (i in ii) {
                iii <- as.numeric(x[i, ])
                if (all(is.na(iii))) {
                  data[i] <- NA
                }
                else {
                  data[i] <- max(iii, na.rm = na.rm)
                }
            }
        }
        names(data) <- NULL
        data
    }
}
```

## `row.means` [exported]

```r
function (data, na.rm = TRUE) 
{
    if (is.atomic(data) & !is.matrix(data)) 
        return(data)
    if (na.rm) {
        x <- rowMeans(data, na.rm = TRUE)
        x[rowSums(is.na(data)) == ncol(data)] <- NA
    }
    else {
        x <- rowMeans(data, na.rm = FALSE)
    }
    x
}
```

## `row.min` [exported]

```r
function (x, na.rm = T) 
{
    if (is.data.frame(x)) {
        data <- apply(x, 1, min)
        if (anyNA(data)) {
            ii <- which.na(data)
            for (i in ii) {
                iii <- as.numeric(x[i, ])
                if (all(is.na(iii))) {
                  data[i] <- NA
                }
                else {
                  data[i] <- min(iii, na.rm = na.rm)
                }
            }
        }
        names(data) <- NULL
        data
    }
}
```

## `row.sums` [exported]

```r
function (data, na.rm = TRUE) 
{
    if (is.atomic(data) & !is.matrix(data)) 
        return(data)
    if (na.rm) {
        x <- rowSums(data, na.rm = TRUE)
        countNA <- rowSums(is.na(data))
        x[countNA == ncol(data)] <- NA
    }
    else {
        x <- rowSums(data, na.rm = FALSE)
    }
    x
}
```

## `select.survey.design` [internal]

```r
function (.data, ...) 
{
    notchag <- c(deparse(.data$call$weights[[2]]), deparse(.data$call$id[[2]]), deparse(.data$call$strata[[2]]))
    d0 <- .data
    .data$variables <- dplyr::select(.data$variables, ...)
    notchag <- set::not(notchag, colnames(.data))
    if (length(notchag) > 0) {
        for (i in notchag) {
            .data$variables[, i] <- d0$variables[, i]
        }
    }
    d0 <- NULL
    .data
}
```

## `select_row.data.frame` [internal]

```r
function (x, ..., cat = TRUE) 
{
    rule <- tryCatch(c(...), error = function(e) "errerrerrerrerrerrerrerrrrerrrererrerererere")
    n0 = nrow(x)
    if (is.character(rule)) {
        if (rule[1] == "errerrerrerrerrerrerrerrrrerrrererrerererere") {
            r2 <- substitute(alist(...))
            rule <- with(x, eval(r2))
            if (is.list(rule)) {
                rule0 <- tryCatch(do.call(c, rule), error = function(e) "eeeerrrroooorrrreee")
                if (all(rule0 %in% "eeeerrrroooorrrreee")) {
                  for (i in 1:length(rule)) {
                    rule[[i]] <- with(x, eval(rule[[i]]))
                  }
                  rule <- do.call(c, rule)
                }
                else {
                  rule <- rule0
                }
            }
            rule <- with(x, eval(rule))
        }
    }
    if (is.logical(rule)) {
        x <- x[rule & !is.na(rule), ]
    }
    else if (is.numeric(rule)) {
        x <- x[rule, ]
    }
    else if (is.character(rule)) {
        x <- x[row.names(x) %in% rule, ]
    }
    n1 <- nrow(x)
    if (cat) {
        cat("\norigin:", n0)
        cat("\nselect:", n1, paste0("(", round(n1/n0 * 100), "%", ")"))
        cat("\n")
    }
    x
}
```

## `select_row.survey.design` [internal]

```r
function (x, ..., cat = TRUE) 
{
    (FilterRowNumber <- 1:nrow(x$variables))
    x$variables$FilterRowNumber <- FilterRowNumber
    d0 <- dplyr::filter(x$variables, ...)
    ck <- FilterRowNumber %in% d0$FilterRowNumber
    x$variables <- subset(x$variables, ck)
    x$cluster <- subset(x$cluster, ck)
    x$strata <- subset(x$strata, ck)
    x$prob <- x$prob[ck]
    x$allprob <- subset(x$allprob, ck)
    x$fpc$sampsize <- subset(x$fpc$sampsize, ck)
    total <- length(FilterRowNumber)
    filter <- sprintf("%s(%s)", sum(ck), paste0(round(sum(ck)/total, 4) * 100, "%"))
    drop <- sprintf("%s(%s)", sum(!ck), paste0(round(sum(!ck)/total, 4) * 100, "%"))
    if (cat) {
        cat("\ntotal :", total)
        cat("\nfilter:", filter)
        cat("\ndrop  :", drop)
    }
    invisible(x)
}
```

## `tab.NA` [internal]

```r
function (x) 
{
    ns <- sum(is.na(x))
    nns <- sum(!is.na(x))
    cat("NA:", ns)
    cat("\nNot-NA:", nns)
}
```

## `tableB.shinytag` [internal]

```r
function (df, id = NULL) 
{
    head <- shiny::tagList(lapply(colnames(df), shiny::tags$th))
    body <- tbodyB(shiny::tagList(lapply(1:nrow(df), function(i) {
        trB(shiny::tagList(lapply(as.character(df[i, ]), tdB)))
    })))
    tableB(head, body, id = id)
}
```

## `tb1.categorial` [internal]

```r
function (design, x, by = NULL, value = FALSE, per = FALSE, perSQse = FALSE, NSQper = FALSE, nSQper = FALSE, 
    ci = FALSE, direction = "h", total = FALSE, round = 2, pvalue = TRUE) 
{
    rr <- lapply(x, function(i) {
        tb1.categorial.i(design, i, by, value, per, perSQse, NSQper, nSQper, ci, direction, total, round, 
            pvalue = pvalue)
    })
    do.call(what = plyr::rbind.fill, rr)
}
```

## `tb1.categorial.i` [internal]

```r
function (design, x, by = NULL, value = FALSE, per = FALSE, perSQse = FALSE, NSQper = FALSE, nSQper = FALSE, 
    ci = FALSE, direction = "h", total = FALSE, round = 2, pvalue = TRUE) 
{
    if (is.numeric(design$variables[, x])) 
        if (length(unique(design$variables[, x])) > 20) 
            stop(paste0("#############\n\n\n\n", x, "<U+4E0D><U+662F><U+5206><U+7C7B><U+53D8><U+91CF>"))
    if (is.null(levels(design$variables[[x]]))) {
        (ku <- kit::funique(design$variables[[x]]))
    }
    else {
        (ku <- unique(design$variables[[x]]))
    }
    if (length(ku) == 1) {
        if (do::cnOS()) 
            stop(paste0("<U+53D8><U+91CF>", x, "<U+4E2D><U+53EA><U+6709><U+4E00><U+4E2A><U+6570><U+503C>", 
                ku))
        if (!do::cnOS()) 
            stop(paste0(x, " only has one value: ", ku))
    }
    (direction <- ifelse(direction == "h", "v", "h"))
    (sumck <- sum(value, per, perSQse, NSQper, nSQper, ci))
    if (sumck == 0) 
        nSQper = TRUE
    if (sum(sumck) > 1) {
        if (do::cnOS()) 
            stop("value,per,perSQse,NSQper,nSQper,ci: ", " <U+53EA><U+80FD><U+6307><U+5B9A>1<U+4E2A>")
        if (!do::cnOS()) 
            stop("value,per,perSQse,NSQper,nSQper,ci: can only be one")
    }
    design <- eval(parse(text = sprintf("update(design,xxvvaalluuee = design$variables[,'%s'])", x)))
    if (length(by) == 1) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = design$variables[,'%s'])", by)))
    }
    else if (length(by) >= 2) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = paste0_columns(design$variables[,c('%s')]))", 
            paste0(by, collapse = "','"))))
    }
    if (total | is.null(by)) {
        tr <- svy_count(value = value, per = per, perSQse = perSQse, valueSQper = NSQper, ci = ci, direction = direction, 
            design = design, x = "xxvvaalluuee", round = round)
        tr
        colnames(tr)[1] <- "total"
        tr$variable <- do::Replace0(row.names(tr), "xxvvaalluuee")
        tr <- tr[, c("variable", "total")]
        row.names(tr) <- NULL
        tr
        if (nSQper) {
            total.per <- do::Replace0(tr$total, "\\(.*")
            tr$total <- paste0(table(design$variables[["xxvvaalluuee"]]), "(", total.per, ")")
        }
        tr$variable <- paste0("~~~~", tr$variable)
        tr <- rbind(data.frame(variable = x, total = ""), tr)
        tr
        if (is.null(by)) 
            return(tr)
    }
    r <- svy_count(value = value, per = per, perSQse = perSQse, valueSQper = NSQper, ci = ci, direction = direction, 
        design = design, x = "xxvvaalluuee", by = "ggrroouupp", remove.suffix = TRUE, round = round)
    colnames(r) <- do::Replace0(colnames(r), "xxvvaalluuee-")
    r <- reshape2::dcast(reshape2::melt(r, id.var = "ggrroouupp"), variable ~ ggrroouupp, value.var = "value")
    if (nSQper) {
        r <- reshape2::dcast(as.data.frame(table(design$variables$ggrroouupp, design$variables$xxvvaalluuee)), 
            Var2 ~ Var1, value.var = "Freq")
        colnames(r)[1] <- "variable"
        r2 <- svy_count(per = TRUE, direction = direction, design = design, x = "xxvvaalluuee", by = "ggrroouupp", 
            remove.suffix = TRUE, round = round)
        colnames(r2) <- do::Replace0(colnames(r2), "xxvvaalluuee-")
        r2 <- reshape2::dcast(reshape2::melt(r2, id.var = "ggrroouupp"), variable ~ ggrroouupp, value.var = "value")
        for (i in 2:ncol(r)) {
            r[, i] <- paste0(r[, i], "(", r2[, i], ")")
        }
    }
    r$variable <- paste0("~~~~", r$variable)
    r <- plyr::rbind.fill(data.frame(variable = x), r)
    r[1, -1] <- ""
    r$Pvalue <- ""
    if (is.null(pvalue)) {
        r[1, "Pvalue"] <- "NULL"
    }
    else if (isTRUE(pvalue)) {
        design <- update(design, xxvvaalluuee = as.character(xxvvaalluuee))
        design <- update(design, ggrroouupp = as.character(ggrroouupp))
        p <- tryCatch(survey::svychisq(~xxvvaalluuee + ggrroouupp, design, na.rm = TRUE)$p.value, error = function(e) "e")
        if (is.character(p)) {
            print(eval(parse(text = sprintf("table(%s=design$variables$ggrroouupp,%s=design$variables$xxvvaalluuee)", 
                paste0(by, collapse = ", "), x))))
            stop(paste0("<U+53D8><U+91CF>: ", x, "<U+4E0D><U+80FD><U+8FDB><U+884C><U+5361><U+65B9><U+68C0><U+9A8C>"))
        }
        r[1, "Pvalue"] <- pvalue.digit(p, round)
    }
    else if (isFALSE(pvalue)) {
        design <- update(design, xxvvaalluuee = as.character(xxvvaalluuee))
        design <- update(design, ggrroouupp = as.character(ggrroouupp))
        p <- tryCatch(survey::svychisq(~xxvvaalluuee + ggrroouupp, design, na.rm = TRUE)$p.value, error = function(e) "e")
        if (is.character(p)) {
            print(eval(parse(text = sprintf("table(%s=design$variables$ggrroouupp,%s=design$variables$xxvvaalluuee)", 
                paste0(by, collapse = ", "), x))))
            stop(paste0("<U+53D8><U+91CF>: ", x, "<U+4E0D><U+80FD><U+8FDB><U+884C><U+5361><U+65B9><U+68C0><U+9A8C>"))
        }
        r[1, "Pvalue"] <- p
    }
    if (total) 
        r <- cbind(tr, r[, -1])
    r
}
```

## `tb1.contineous.normal` [internal]

```r
function (design, x, by = NULL, meanSQse = FALSE, meanPMse = FALSE, ci = FALSE, total = FALSE, round = 2, 
    pvalue = TRUE, c_geometric = FALSE) 
{
    do.call(lapply(x, function(i) {
        r <- tb1.contineous.normal.i(design, i, by, meanSQse, meanPMse, ci, total, round, pvalue = pvalue, 
            c_geometric = c_geometric)
        r
    }), what = plyr::rbind.fill)
}
```

## `tb1.contineous.normal.i` [internal]

```r
function (design, x, by = NULL, meanSQse = FALSE, meanPMse = FALSE, ci = FALSE, total = FALSE, round = 2, 
    pvalue = TRUE, c_geometric = FALSE) 
{
    if (!is.numeric(design$variables[, x])) 
        stop(paste0("#############\n\n\n\n", x, "<U+4E0D><U+662F><U+8FDE><U+7EED><U+53D8><U+91CF>"))
    if (sum(meanSQse, meanPMse, ci) > 1) {
        if (do::cnOS()) 
            stop("meanSQse,meanPMse,ci: ", " <U+53EA><U+80FD><U+6307><U+5B9A>1<U+4E2A>")
        if (!do::cnOS()) 
            stop("meanSQse,meanPMse,ci: can only be one")
    }
    if (sum(meanSQse, meanPMse, ci) == 0) 
        meanSQse <- TRUE
    design <- eval(parse(text = sprintf("update(design,xxvvaalluuee = design$variables[,'%s'])", x)))
    if (length(by) == 1) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = paste0('~',design$variables[,'%s']))", 
            by)))
    }
    else if (length(by) >= 2) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = paste0_columns(design$variables[,c('%s')]))", 
            paste0(by, collapse = "','"))))
    }
    if (total | is.null(by)) {
        tr <- data.frame(svy_mean(design = design, x = "xxvvaalluuee", meanSQse = meanSQse, meanPMse = meanPMse, 
            geometric = c_geometric, ci = ci, remove.suffix = TRUE, round = round, na.rm = T), row.names = x, 
            check.names = FALSE)
        colnames(tr)[2] <- "total"
        tr[1, 1] <- x
        tr
        if (is.null(by)) 
            return(tr)
    }
    r <- svy_mean(design = design, x = "xxvvaalluuee", by = "ggrroouupp", meanSQse = meanSQse, meanPMse = meanPMse, 
        ci = ci, geometric = c_geometric, remove.suffix = TRUE, round = round)
    r$ggrroouupp <- do::knife_left(r$ggrroouupp, 1)
    r <- data.frame(drop_col(reshape2::dcast(r, 1 ~ ggrroouupp, value.var = "xxvvaalluuee"), 1), row.names = x, 
        check.names = FALSE)
    ux <- do::unique_no.NA(as.character(design$variables$ggrroouupp))
    len <- length(ux)
    if (len == 2) {
        if (is.null(pvalue)) {
            r$Pvalue <- "NULL"
        }
        else if (isTRUE(pvalue)) {
            p <- survey::svyttest(xxvvaalluuee ~ as.character(ggrroouupp), design)$p.value
            if (as.character(p) == "NaN") {
                p <- 99
            }
            else {
                r$Pvalue <- pvalue.digit(p, round)
            }
        }
        else if (isFALSE(pvalue)) {
            p <- survey::svyttest(xxvvaalluuee ~ as.character(ggrroouupp), design)$p.value
            r$Pvalue <- p
        }
    }
    else if (len >= 3) {
        if (is.null(pvalue)) {
            r$Pvalue <- "NULL"
        }
        else if (isTRUE(pvalue)) {
            p <- survey::regTermTest(survey::svyglm(xxvvaalluuee ~ ggrroouupp, design = design), "ggrroouupp")$p[1, 
                1]
            r$Pvalue <- pvalue.digit(p, round)
        }
        else if (isFALSE(pvalue)) {
            p <- survey::regTermTest(survey::svyglm(xxvvaalluuee ~ ggrroouupp, design = design), "ggrroouupp")$p[1, 
                1]
            r$Pvalue <- p
        }
    }
    else {
        if (do::cnOS()) 
            stop(paste("<U+53D8><U+91CF>", x, "<U+4E2D><U+7684><U+5206><U+7EC4><U+53EA><U+6709>", len, 
                "<U+4E2A>:", paste0(ux, collapse = ", ")))
        if (!do::cnOS()) 
            stop(paste("variable", x, "only have", len, "group:", paste0(ux, collapse = ", ")))
    }
    if (total) {
        r <- cbind(tr, r)
    }
    else {
        r <- cbind(variable = x, r)
    }
    row.names(r) <- NULL
    r
}
```

## `tb1.contineous.not.normal` [internal]

```r
function (design, x, by = NULL, total = FALSE, round = 2, pvalue = TRUE) 
{
    res <- lapply(x, function(i) {
        tb1.contineous.not.normal.i(design, i, by, total, round, pvalue = pvalue)
    })
    for (i in 1:length(res)) {
        res[[i]][, ncol(res[[i]])] <- as.character(res[[i]][, ncol(res[[i]])])
    }
    do.call(what = plyr::rbind.fill, res)
}
```

## `tb1.contineous.not.normal.i` [internal]

```r
function (design, x, by = NULL, total = FALSE, round = 2, pvalue = TRUE) 
{
    if (!is.numeric(design$variables[, x])) 
        stop(paste0("#############\n\n\n\n", x, "<U+4E0D><U+662F><U+8FDE><U+7EED><U+53D8><U+91CF>"))
    design <- eval(parse(text = sprintf("update(design,xxvvaalluuee = design$variables[,'%s'])", x)))
    if (length(by) == 1) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = design$variables[,'%s'])", by)))
    }
    else if (length(by) >= 2) {
        design <- eval(parse(text = sprintf("update(design,ggrroouupp = paste0_columns(design$variables[,c('%s')]))", 
            paste0(by, collapse = "','"))))
    }
    if (total | is.null(by)) {
        tr <- svy_quantile(design = design, x = "xxvvaalluuee", round = round)
        tr[1, 1] <- x
        colnames(tr)[2] <- "total"
        tr
        if (is.null(by)) 
            return(tr)
    }
    r <- svy_quantile(design = design, x = "xxvvaalluuee", by = "ggrroouupp", remove.suffix = TRUE, round = round)
    r
    r <- data.frame(drop_col(reshape2::dcast(r, 1 ~ ggrroouupp, value.var = "xxvvaalluuee"), 1), row.names = x, 
        check.names = FALSE)
    ux <- do::unique_no.NA(as.character(design$variables$ggrroouupp))
    len <- length(ux)
    if (len == 2) {
        if (is.null(pvalue)) {
            r$Pvalue <- "NULL"
        }
        else if (isTRUE(pvalue)) {
            p <- survey::svyranktest(xxvvaalluuee ~ as.character(ggrroouupp), design, test = "wilcoxon")$p.value
            r$Pvalue <- pvalue.digit(p, round)
        }
        else if (isFALSE(pvalue)) {
            p <- survey::svyranktest(xxvvaalluuee ~ as.character(ggrroouupp), design, test = "wilcoxon")$p.value
            r$Pvalue <- p
        }
    }
    else if (len >= 3) {
        if (is.null(pvalue)) {
            r$Pvalue <- "NULL"
        }
        else if (isFALSE(pvalue)) {
            p <- survey::svyranktest(xxvvaalluuee ~ as.character(ggrroouupp), design, test = "KruskalWallis")$p.value
            r$Pvalue <- pvalue.digit(p, round)
        }
        else if (isTRUE(pvalue)) {
            p <- survey::svyranktest(xxvvaalluuee ~ as.character(ggrroouupp), design, test = "KruskalWallis")$p.value
            r$Pvalue <- pvalue.digit(p, round)
        }
    }
    else {
        if (do::cnOS()) 
            stop(paste("<U+53D8><U+91CF>", x, "<U+4E2D><U+7684><U+5206><U+7EC4><U+53EA><U+6709>", len, 
                "<U+4E2A>:", paste0(ux, collapse = ", ")))
        if (!do::cnOS()) 
            stop(paste("variable", x, "only have", len, "group:", paste0(ux, collapse = ", ")))
    }
    if (total) {
        r <- cbind(tr, r)
    }
    else {
        r <- cbind(variable = x, r)
    }
    row.names(r) <- NULL
    r
}
```

## `tea.1day` [internal]

```r
function (years, day, unit = "gram", sweeten = FALSE, caffeinate = FALSE, green = FALSE, black = FALSE, 
    oolong = FALSE, iced = FALSE, hot = FALSE, normT = FALSE, leaf = FALSE, instant = FALSE, bottle = FALSE, 
    food.code = NULL) 
{
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d.iff <- iff.gram.kcl(years = years, day = day)
    fndds.food.code <- tea.food.code(years = years, food.code = food.code)
    fndds.food.code <- fndds.food.code[fndds.food.code$food.code %in% d.iff$food.code, ]
    ck <- (!d.iff$food.code %in% fndds.food.code$food.code) & !is.na(d.iff$food.code)
    d.iff$gram[ck] <- 0
    d.iff$kcal[ck] <- 0
    fndds.food.code$food.code <- as.numeric(fndds.food.code$food.code)
    d <- drop_col(dplyr::left_join(d.iff, fndds.food.code, c("Year", "food.code")), "seq.num")
    d$cup <- d$gram/d$portion.weight
    d$cup[grepl("oz", d$portion.description)] <- d$cup[grepl("oz", d$portion.description)]/6
    d <- d[, c("Year", "seqn", "gram", "kcal", "cup", "main.food.description")]
    d$cup[d$kcal %in% 0] <- 0
    ck.unsweeten <- lookl(d$main.food.description, "unsweet", NA2false = TRUE)
    d$tea.unsweeten.gram[d$gram >= 0] <- 0
    d$tea.unsweeten.kcal[d$gram >= 0] <- 0
    d$tea.unsweeten.cup[d$gram >= 0] <- 0
    d$tea.unsweeten.gram[ck.unsweeten] <- d$gram[ck.unsweeten]
    d$tea.unsweeten.kcal[ck.unsweeten] <- d$kcal[ck.unsweeten]
    d$tea.unsweeten.cup[ck.unsweeten] <- d$cup[ck.unsweeten]
    ck <- lookl(d$main.food.description, "sweet", NA2false = TRUE) & !ck.unsweeten
    d$tea.sweeten.gram[d$gram >= 0] <- 0
    d$tea.sweeten.kcal[d$gram >= 0] <- 0
    d$tea.sweeten.cup[d$gram >= 0] <- 0
    d$tea.sweeten.gram[ck] <- d$gram[ck]
    d$tea.sweeten.kcal[ck] <- d$kcal[ck]
    d$tea.sweeten.cup[ck] <- d$cup[ck]
    ck <- lookl(d$main.food.description, "decaffeinated", NA2false = TRUE)
    d$tea.decaffeinate.gram[d$gram >= 0] <- 0
    d$tea.decaffeinate.kcal[d$gram >= 0] <- 0
    d$tea.decaffeinate.cup[d$gram >= 0] <- 0
    d$tea.decaffeinate.gram[ck] <- d$gram[ck]
    d$tea.decaffeinate.kcal[ck] <- d$kcal[ck]
    d$tea.decaffeinate.cup[ck] <- d$cup[ck]
    ck <- lookl(d$main.food.description, "!~decaffeinated", NA2false = TRUE)
    d$tea.caffeinate.gram[d$gram >= 0] <- 0
    d$tea.caffeinate.kcal[d$gram >= 0] <- 0
    d$tea.caffeinate.cup[d$gram >= 0] <- 0
    d$tea.caffeinate.gram[ck] <- d$gram[ck]
    d$tea.caffeinate.kcal[ck] <- d$kcal[ck]
    d$tea.caffeinate.cup[ck] <- d$cup[ck]
    ck <- lookl(d$main.food.description, "green", NA2false = TRUE)
    d$tea.green.gram[d$gram >= 0] <- 0
    d$tea.green.kcal[d$gram >= 0] <- 0
    d$tea.green.cup[d$gram >= 0] <- 0
    d$tea.green.gram[ck] <- d$gram[ck]
    d$tea.green.kcal[ck] <- d$kcal[ck]
    d$tea.green.cup[ck] <- d$cup[ck]
    ck <- lookl(d$main.food.description, "black", NA2false = TRUE)
    d$tea.black.gram[d$gram >= 0] <- 0
    d$tea.black.kcal[d$gram >= 0] <- 0
    d$tea.black.cup[d$gram >= 0] <- 0
    d$tea.black.gram[ck] <- d$gram[ck]
    d$tea.black.kcal[ck] <- d$kcal[ck]
    d$tea.black.cup[ck] <- d$cup[ck]
    ck <- lookl(d$main.food.description, "oolong", NA2false = TRUE)
    d$tea.oolong.gram[d$gram >= 0] <- 0
    d$tea.oolong.kcal[d$gram >= 0] <- 0
    d$tea.oolong.cup[d$gram >= 0] <- 0
    d$tea.oolong.gram[ck] <- d$gram[ck]
    d$tea.oolong.kcal[ck] <- d$kcal[ck]
    d$tea.oolong.cup[ck] <- d$cup[ck]
    ck.iced <- lookl(d$main.food.description, "iced", NA2false = TRUE)
    d$tea.iced.gram[d$gram >= 0] <- 0
    d$tea.iced.kcal[d$gram >= 0] <- 0
    d$tea.iced.cup[d$gram >= 0] <- 0
    d$tea.iced.gram[ck.iced] <- d$gram[ck.iced]
    d$tea.iced.kcal[ck.iced] <- d$kcal[ck.iced]
    d$tea.iced.cup[ck.iced] <- d$cup[ck.iced]
    ck.hot <- lookl(d$main.food.description, "hot", NA2false = TRUE)
    d$tea.hot.gram[d$gram >= 0] <- 0
    d$tea.hot.kcal[d$gram >= 0] <- 0
    d$tea.hot.cup[d$gram >= 0] <- 0
    d$tea.hot.gram[ck.hot] <- d$gram[ck.hot]
    d$tea.hot.kcal[ck.hot] <- d$kcal[ck.hot]
    d$tea.hot.cup[ck.hot] <- d$cup[ck.hot]
    ck.normT <- !(ck.hot | ck.iced)
    d$tea.normT.gram[d$gram >= 0] <- 0
    d$tea.normT.kcal[d$gram >= 0] <- 0
    d$tea.normT.cup[d$gram >= 0] <- 0
    d$tea.normT.gram[ck.normT] <- d$gram[ck.normT]
    d$tea.normT.kcal[ck.normT] <- d$kcal[ck.normT]
    d$tea.normT.cup[ck.normT] <- d$cup[ck.normT]
    ck.leaf <- lookl(d$main.food.description, "leaf", NA2false = TRUE)
    d$tea.leaf.gram[d$gram >= 0] <- 0
    d$tea.leaf.kcal[d$gram >= 0] <- 0
    d$tea.leaf.cup[d$gram >= 0] <- 0
    d$tea.leaf.gram[ck.leaf] <- d$gram[ck.leaf]
    d$tea.leaf.kcal[ck.leaf] <- d$kcal[ck.leaf]
    d$tea.leaf.cup[ck.leaf] <- d$cup[ck.leaf]
    ck.instant <- lookl(d$main.food.description, "instant", NA2false = TRUE)
    d$tea.instant.gram[d$gram >= 0] <- 0
    d$tea.instant.kcal[d$gram >= 0] <- 0
    d$tea.instant.cup[d$gram >= 0] <- 0
    d$tea.instant.gram[ck.instant] <- d$gram[ck.instant]
    d$tea.instant.kcal[ck.instant] <- d$kcal[ck.instant]
    d$tea.instant.cup[ck.instant] <- d$cup[ck.instant]
    ck.bottle <- lookl(d$main.food.description, "bottle", NA2false = TRUE)
    d$tea.bottle.gram[d$gram >= 0] <- 0
    d$tea.bottle.kcal[d$gram >= 0] <- 0
    d$tea.bottle.cup[d$gram >= 0] <- 0
    d$tea.bottle.gram[ck.bottle] <- d$gram[ck.bottle]
    d$tea.bottle.kcal[ck.bottle] <- d$kcal[ck.bottle]
    d$tea.bottle.cup[ck.bottle] <- d$cup[ck.bottle]
    nms <- colnames(d)[do::left(colnames(d), 4) %in% "tea."]
    x <- c(unit, nms[do::right(nms, 4) %in% c(unit, paste0(".", unit))])
    var <- unit
    if (sweeten) 
        append(var) <- c(paste0("tea.sweeten.", unit), paste0("tea.unsweeten.", unit))
    if (caffeinate) 
        append(var) <- c(paste0("tea.caffeinate.", unit), paste0("tea.decaffeinate.", unit))
    if (green) 
        append(var) <- paste0("tea.", "green", ".", unit)
    if (black) 
        append(var) <- paste0("tea.", "black", ".", unit)
    if (oolong) 
        append(var) <- paste0("tea.", "oolong", ".", unit)
    if (iced) 
        append(var) <- paste0("tea.", "iced", ".", unit)
    if (hot) 
        append(var) <- paste0("tea.", "hot", ".", unit)
    if (normT) 
        append(var) <- paste0("tea.", "normT", ".", unit)
    if (leaf) 
        append(var) <- paste0("tea.", "leaf", ".", unit)
    if (instant) 
        append(var) <- paste0("tea.", "instant", ".", unit)
    if (bottle) 
        append(var) <- paste0("tea.", "bottle", ".", unit)
    d2 <- aggregate2(data = d, x = var, by = c("Year", "seqn"), fun = ".sum.nona")
    colnames(d2) <- do::Replace0(colnames(d2), paste0("\\.", unit))
    col_rename(d2) <- paste0(unit, ":tea.", unit)
    at <- unique(fndds.food.code[, c("food.code", "main.food.description")])
    row.names(at) <- NULL
    attr(d2, "food.code") <- at
    d2
}
```

## `tea.food.code` [internal]

```r
function (years, food.code = NULL) 
{
    (years <- prepare_years(years))
    (y1 <- set::and(years, prepare_years(2001:2010)))
    if (length(y1) > 0) {
        df1 <- unique(fndds.db.food.and.weight(start = 923, years = y1, seq.num = 1, cat = F))
    }
    else df1 = NULL
    (y2 <- set::and(years, prepare_years(2011)))
    if (length(y2) > 0) {
        d1 <- unique(fndds.db.food.and.weight(start = 923, years = y2, seq.num = 1, cat = F))
        d2 <- unique(fndds.db.food.and.weight(start = 923, years = y2, seq.num = 7, portion.description = "1 cup", 
            cat = F))
        df2 <- unique(rbind(d1, d2))
    }
    else df2 = NULL
    (y3 <- set::not(years, prepare_years(1999:2011)))
    if (length(y3) > 0) {
        d1 <- do.call(lapply(y3, function(i) fndds.db.food.and.weight(start = 923, years = i, seq.num = 1, 
            cat = F)), what = rbind)
        d2 <- do.call(lapply(y3, function(i) fndds.db.food.and.weight(start = 923, years = i, seq.num = 5:10, 
            portion.description = "no ice", cat = F)), what = rbind)
        df3 <- unique(rbind(d1, d2))
        df3 <- df3[order(df3$Year, df3$food.code, df3$seq.num), ]
        dup <- paste0(df3$Year, "-", df3$food.code)
        df3 <- df3[!duplicated(dup), ]
    }
    else df3 = NULL
    df <- rbind(df1, df2, df3)
    df$portion.weight <- as.numeric(df$portion.weight)
    df <- df[order(df$Year, df$food.code, df$portion.weight), ]
    dup <- duplicated(paste0(df$Year, "-", df$food.code))
    df <- df[!dup, ]
    if (!is.null(food.code)) 
        df <- df[df$food.code %in% food.code, ]
    df[!lookl(df$main.food.description, "bean beverage|corn beverage|lemonade"), ]
}
```

## `unique_no.NA` [internal]

```r
function (x) 
{
    x <- unique(x)
    x[!is.na(x)]
}
```

## `value.numbar` [exported]

```r
function (data) 
{
    if (is.matrix(data) | is.data.frame(data)) {
        do.call(lapply(1:ncol(data), function(i) {
            data.frame(variable = colnames(data)[i], n = length(do::unique_no.NA(as.character(data[, 
                i]))))
        }), what = rbind)
    }
    else {
        length(do::unique_no.NA(data))
    }
}
```

## `which.na` [internal]

```r
function (x) 
which(is.na(x))
```

## `write.yier` [exported]

```r
function (df, file = NULL, project = NULL, row.names = FALSE, root = "c") 
{
    if (is.null(file)) 
        file <- deparse(substitute(df))
    if (tolower(do::right(file, 4)) %in% c(".tsv", ".csv", ".xls")) 
        file <- do::knife_right(file, 4)
    if (tolower(do::right(file, 5)) %in% c(".xlsx")) 
        file <- do::knife_right(file, 5)
    if (is.null(project)) 
        project <- file
    lab <- data.frame(x = 1, y = 2, c = 4)
    colnames(lab) <- lab <- lab[-1, ]
    wb <- openxlsx::createWorkbook()
    openxlsx::addWorksheet(wb, "Sheet1", gridLines = FALSE)
    openxlsx::writeData(wb, sheet = 1, x = "<U+53D8><U+91CF><U+540D>", startCol = 1, startRow = 1)
    openxlsx::writeData(wb, sheet = 1, x = "<U+53D6><U+503C><U+7F16><U+7801>", startCol = 2, startRow = 1)
    openxlsx::writeData(wb, sheet = 1, x = "<U+610F><U+4E49>", startCol = 3, startRow = 1)
    openxlsx::addStyle(wb, sheet = 1, style = openxlsx::createStyle(borderStyle = "thin", border = c("top", 
        "bottom", "left", "right"), ), rows = 1, cols = 1:3)
    startRow = 2
    for (i in colnames(df)) {
        if (is.character(df[, i]) | is.factor(df[, i])) {
            labi <- data.frame(x1 = i, x2 = "", x3 = i)
            lab <- rbind(lab, labi)
            lv <- levels(df[, i])
            if (is.null(lv)) 
                lv <- unique(df[, i])
            lv <- lv[!is.na(lv)]
            if (length(lv) == 2) {
                sq <- 0:1
            }
            else {
                sq <- 1:length(lv)
            }
            df[, i] <- Recode(df[, i], paste0(lv, "::", sq))
            openxlsx::writeData(wb, sheet = 1, x = toupper(i), startCol = 1, startRow = startRow)
            openxlsx::writeData(wb, sheet = 1, x = i, startCol = 3, startRow = startRow)
            openxlsx::addStyle(wb, sheet = 1, style = openxlsx::createStyle(fgFill = "#fde9d9", borderStyle = "thin", 
                border = c("top", "bottom", "left", "right")), rows = startRow, cols = 1:3)
            startRow <- startRow + 1
            openxlsx::writeData(wb, sheet = 1, x = sq, startCol = 2, startRow = startRow)
            openxlsx::writeData(wb, sheet = 1, x = lv, startCol = 3, startRow = startRow)
            for (k in startRow:(startRow + length(lv) - 1)) {
                openxlsx::addStyle(wb, sheet = 1, style = openxlsx::createStyle(borderStyle = "thin", 
                  border = c("top", "bottom", "left", "right")), rows = k, cols = 1:3)
            }
            startRow <- startRow + length(lv)
        }
        else {
            openxlsx::writeData(wb, sheet = 1, x = toupper(i), startCol = 1, startRow = startRow)
            openxlsx::writeData(wb, sheet = 1, x = i, startCol = 3, startRow = startRow)
            openxlsx::addStyle(wb, sheet = 1, style = openxlsx::createStyle(fgFill = "#dce6f1", borderStyle = "thin", 
                border = c("top", "bottom", "left", "right"), ), rows = startRow, cols = 1)
            openxlsx::addStyle(wb, sheet = 1, style = openxlsx::createStyle(borderStyle = "thin", border = c("top", 
                "bottom", "left", "right"), ), rows = startRow, cols = 2:3)
            startRow <- startRow + 1
        }
    }
    openxlsx::writeData(wb, sheet = 1, x = "Thisisforend", startCol = 1, startRow = startRow)
    openxlsx::writeData(wb, sheet = 1, x = "Thisisforend", startCol = 3, startRow = startRow)
    if (do::cnOS()) {
        dir <- paste0(root, ":/EmpowerRCH/Analysis/", project)
        if (!dir.exists(dir)) 
            dir.create(dir, recursive = T, showWarnings = F)
    }
    else {
        dir <- sprintf("/Users/%s/Desktop/Empower4Mac/Analysis/%s", Sys.info()["user"], project)
        if (!dir.exists(dir)) 
            dir.create(dir, recursive = T, showWarnings = F)
    }
    message(dir)
    f2 <- paste0(dir, "/", file, ".txt")
    message(f2)
    data.table::fwrite(x = df, file = f2, row.names = row.names, sep = "\t", showProgress = TRUE)
    v.file <- paste0(dir, "/", file, "_variables.xlsx")
    message(v.file)
    openxlsx::saveWorkbook(wb, v.file, overwrite = TRUE)
}
```

## `youth.obesity` [exported]

```r
function (data, age = "age", sex = "sex", bmi = "bmi") 
{
    ck <- all(funique.noNA(data[, sex]) %in% c("male", "female"))
    if (!ck) 
        stop("code for sex must be male and female")
    data$obesity[!is.na(data[, age]) & !is.na(data[, sex]) & !is.na(data[, bmi])] <- "normal"
    data$obesity[data[, age] >= 2 & data[, age] < 2.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        18.41] <- "overweight"
    data$obesity[data[, age] >= 2.5 & data[, age] < 3 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        18.129999999999999] <- "overweight"
    data$obesity[data[, age] >= 3 & data[, age] < 3.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.890000000000001] <- "overweight"
    data$obesity[data[, age] >= 3.5 & data[, age] < 4 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.690000000000001] <- "overweight"
    data$obesity[data[, age] >= 4 & data[, age] < 4.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.550000000000001] <- "overweight"
    data$obesity[data[, age] >= 4.5 & data[, age] < 5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.469999999999999] <- "overweight"
    data$obesity[data[, age] >= 5 & data[, age] < 5.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.420000000000002] <- "overweight"
    data$obesity[data[, age] >= 5.5 & data[, age] < 6 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.449999999999999] <- "overweight"
    data$obesity[data[, age] >= 6 & data[, age] < 6.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.550000000000001] <- "overweight"
    data$obesity[data[, age] >= 6.5 & data[, age] < 7 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.710000000000001] <- "overweight"
    data$obesity[data[, age] >= 7 & data[, age] < 7.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        17.920000000000002] <- "overweight"
    data$obesity[data[, age] >= 7.5 & data[, age] < 8 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        18.16] <- "overweight"
    data$obesity[data[, age] >= 8 & data[, age] < 8.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        18.440000000000001] <- "overweight"
    data$obesity[data[, age] >= 8.5 & data[, age] < 9 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        18.760000000000002] <- "overweight"
    data$obesity[data[, age] >= 9 & data[, age] < 9.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.100000000000001] <- "overweight"
    data$obesity[data[, age] >= 9.5 & data[, age] < 10 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.460000000000001] <- "overweight"
    data$obesity[data[, age] >= 10 & data[, age] < 10.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.84] <- "overweight"
    data$obesity[data[, age] >= 10.5 & data[, age] < 11 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.199999999999999] <- "overweight"
    data$obesity[data[, age] >= 11 & data[, age] < 11.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.550000000000001] <- "overweight"
    data$obesity[data[, age] >= 11.5 & data[, age] < 12 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.890000000000001] <- "overweight"
    data$obesity[data[, age] >= 12 & data[, age] < 12.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        21.219999999999999] <- "overweight"
    data$obesity[data[, age] >= 12.5 & data[, age] < 13 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        21.559999999999999] <- "overweight"
    data$obesity[data[, age] >= 13 & data[, age] < 13.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        21.91] <- "overweight"
    data$obesity[data[, age] >= 13.5 & data[, age] < 14 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        22.27] <- "overweight"
    data$obesity[data[, age] >= 14 & data[, age] < 14.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        22.620000000000001] <- "overweight"
    data$obesity[data[, age] >= 14.5 & data[, age] < 15 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        22.960000000000001] <- "overweight"
    data$obesity[data[, age] >= 15 & data[, age] < 15.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        23.289999999999999] <- "overweight"
    data$obesity[data[, age] >= 15.5 & data[, age] < 16 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        23.600000000000001] <- "overweight"
    data$obesity[data[, age] >= 16 & data[, age] < 16.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        23.899999999999999] <- "overweight"
    data$obesity[data[, age] >= 16.5 & data[, age] < 17 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        24.190000000000001] <- "overweight"
    data$obesity[data[, age] >= 17 & data[, age] < 17.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        24.460000000000001] <- "overweight"
    data$obesity[data[, age] >= 17.5 & data[, age] < 18 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        24.73] <- "overweight"
    data$obesity[data[, age] == 18 & tolower(data[, sex]) == "male" & data[, bmi] >= 25] <- "overweight"
    data$obesity[data[, age] >= 2 & data[, age] < 2.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        18.02] <- "overweight"
    data$obesity[data[, age] >= 2.5 & data[, age] < 3 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.760000000000002] <- "overweight"
    data$obesity[data[, age] >= 3 & data[, age] < 3.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.559999999999999] <- "overweight"
    data$obesity[data[, age] >= 3.5 & data[, age] < 4 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.399999999999999] <- "overweight"
    data$obesity[data[, age] >= 4 & data[, age] < 4.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.280000000000001] <- "overweight"
    data$obesity[data[, age] >= 4.5 & data[, age] < 5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.190000000000001] <- "overweight"
    data$obesity[data[, age] >= 5 & data[, age] < 5.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.149999999999999] <- "overweight"
    data$obesity[data[, age] >= 5.5 & data[, age] < 6 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.199999999999999] <- "overweight"
    data$obesity[data[, age] >= 6 & data[, age] < 6.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.34] <- "overweight"
    data$obesity[data[, age] >= 6.5 & data[, age] < 7 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.530000000000001] <- "overweight"
    data$obesity[data[, age] >= 7 & data[, age] < 7.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        17.75] <- "overweight"
    data$obesity[data[, age] >= 7.5 & data[, age] < 8 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        18.030000000000001] <- "overweight"
    data$obesity[data[, age] >= 8 & data[, age] < 8.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        18.350000000000001] <- "overweight"
    data$obesity[data[, age] >= 8.5 & data[, age] < 9 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        18.690000000000001] <- "overweight"
    data$obesity[data[, age] >= 9 & data[, age] < 9.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.07] <- "overweight"
    data$obesity[data[, age] >= 9.5 & data[, age] < 10 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.449999999999999] <- "overweight"
    data$obesity[data[, age] >= 10 & data[, age] < 10.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.859999999999999] <- "overweight"
    data$obesity[data[, age] >= 10.5 & data[, age] < 11 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        20.289999999999999] <- "overweight"
    data$obesity[data[, age] >= 11 & data[, age] < 11.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        20.739999999999998] <- "overweight"
    data$obesity[data[, age] >= 11.5 & data[, age] < 12 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        21.199999999999999] <- "overweight"
    data$obesity[data[, age] >= 12 & data[, age] < 12.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        21.68] <- "overweight"
    data$obesity[data[, age] >= 12.5 & data[, age] < 13 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        22.140000000000001] <- "overweight"
    data$obesity[data[, age] >= 13 & data[, age] < 13.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        22.579999999999998] <- "overweight"
    data$obesity[data[, age] >= 13.5 & data[, age] < 14 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        22.98] <- "overweight"
    data$obesity[data[, age] >= 14 & data[, age] < 14.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        23.34] <- "overweight"
    data$obesity[data[, age] >= 14.5 & data[, age] < 15 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        23.66] <- "overweight"
    data$obesity[data[, age] >= 15 & data[, age] < 15.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        23.940000000000001] <- "overweight"
    data$obesity[data[, age] >= 15.5 & data[, age] < 16 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.170000000000002] <- "overweight"
    data$obesity[data[, age] >= 16 & data[, age] < 16.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.370000000000001] <- "overweight"
    data$obesity[data[, age] >= 16.5 & data[, age] < 17 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.539999999999999] <- "overweight"
    data$obesity[data[, age] >= 17 & data[, age] < 17.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.699999999999999] <- "overweight"
    data$obesity[data[, age] >= 17.5 & data[, age] < 18 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.850000000000001] <- "overweight"
    data$obesity[data[, age] == 18 & tolower(data[, sex]) == "female" & data[, bmi] >= 25] <- "overweight"
    data$obesity[data[, age] >= 2 & data[, age] < 2.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.09] <- "obesity"
    data$obesity[data[, age] >= 2.5 & data[, age] < 3 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.800000000000001] <- "obesity"
    data$obesity[data[, age] >= 3 & data[, age] < 3.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.57] <- "obesity"
    data$obesity[data[, age] >= 3.5 & data[, age] < 4 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.390000000000001] <- "obesity"
    data$obesity[data[, age] >= 4 & data[, age] < 4.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.289999999999999] <- "obesity"
    data$obesity[data[, age] >= 4.5 & data[, age] < 5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.260000000000002] <- "obesity"
    data$obesity[data[, age] >= 5 & data[, age] < 5.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.300000000000001] <- "obesity"
    data$obesity[data[, age] >= 5.5 & data[, age] < 6 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.469999999999999] <- "obesity"
    data$obesity[data[, age] >= 6 & data[, age] < 6.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        19.780000000000001] <- "obesity"
    data$obesity[data[, age] >= 6.5 & data[, age] < 7 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.23] <- "obesity"
    data$obesity[data[, age] >= 7 & data[, age] < 7.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        20.629999999999999] <- "obesity"
    data$obesity[data[, age] >= 7.5 & data[, age] < 8 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        21.09] <- "obesity"
    data$obesity[data[, age] >= 8 & data[, age] < 8.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        21.600000000000001] <- "obesity"
    data$obesity[data[, age] >= 8.5 & data[, age] < 9 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        22.170000000000002] <- "obesity"
    data$obesity[data[, age] >= 9 & data[, age] < 9.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        22.77] <- "obesity"
    data$obesity[data[, age] >= 9.5 & data[, age] < 10 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        23.390000000000001] <- "obesity"
    data$obesity[data[, age] >= 10 & data[, age] < 10.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        24] <- "obesity"
    data$obesity[data[, age] >= 10.5 & data[, age] < 11 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        24.57] <- "obesity"
    data$obesity[data[, age] >= 11 & data[, age] < 11.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        25.100000000000001] <- "obesity"
    data$obesity[data[, age] >= 11.5 & data[, age] < 12 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        25.579999999999998] <- "obesity"
    data$obesity[data[, age] >= 12 & data[, age] < 12.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        26.02] <- "obesity"
    data$obesity[data[, age] >= 12.5 & data[, age] < 13 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        26.43] <- "obesity"
    data$obesity[data[, age] >= 13 & data[, age] < 13.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        26.84] <- "obesity"
    data$obesity[data[, age] >= 13.5 & data[, age] < 14 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        27.25] <- "obesity"
    data$obesity[data[, age] >= 14 & data[, age] < 14.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        27.629999999999999] <- "obesity"
    data$obesity[data[, age] >= 14.5 & data[, age] < 15 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        27.98] <- "obesity"
    data$obesity[data[, age] >= 15 & data[, age] < 15.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        28.300000000000001] <- "obesity"
    data$obesity[data[, age] >= 15.5 & data[, age] < 16 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        28.600000000000001] <- "obesity"
    data$obesity[data[, age] >= 16 & data[, age] < 16.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        28.879999999999999] <- "obesity"
    data$obesity[data[, age] >= 16.5 & data[, age] < 17 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        29.140000000000001] <- "obesity"
    data$obesity[data[, age] >= 17 & data[, age] < 17.5 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        29.41] <- "obesity"
    data$obesity[data[, age] >= 17.5 & data[, age] < 18 & tolower(data[, sex]) == "male" & data[, bmi] >= 
        29.699999999999999] <- "obesity"
    data$obesity[data[, age] == 18 & tolower(data[, sex]) == "male" & data[, bmi] >= 30] <- "obesity"
    data$obesity[data[, age] >= 2 & data[, age] < 2.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.809999999999999] <- "obesity"
    data$obesity[data[, age] >= 2.5 & data[, age] < 3 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.550000000000001] <- "obesity"
    data$obesity[data[, age] >= 3 & data[, age] < 3.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.359999999999999] <- "obesity"
    data$obesity[data[, age] >= 3.5 & data[, age] < 4 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.23] <- "obesity"
    data$obesity[data[, age] >= 4 & data[, age] < 4.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.149999999999999] <- "obesity"
    data$obesity[data[, age] >= 4.5 & data[, age] < 5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.120000000000001] <- "obesity"
    data$obesity[data[, age] >= 5 & data[, age] < 5.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.170000000000002] <- "obesity"
    data$obesity[data[, age] >= 5.5 & data[, age] < 6 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.34] <- "obesity"
    data$obesity[data[, age] >= 6 & data[, age] < 6.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        19.649999999999999] <- "obesity"
    data$obesity[data[, age] >= 6.5 & data[, age] < 7 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        20.079999999999998] <- "obesity"
    data$obesity[data[, age] >= 7 & data[, age] < 7.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        20.510000000000002] <- "obesity"
    data$obesity[data[, age] >= 7.5 & data[, age] < 8 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        21.010000000000002] <- "obesity"
    data$obesity[data[, age] >= 8 & data[, age] < 8.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        21.57] <- "obesity"
    data$obesity[data[, age] >= 8.5 & data[, age] < 9 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        22.18] <- "obesity"
    data$obesity[data[, age] >= 9 & data[, age] < 9.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        22.809999999999999] <- "obesity"
    data$obesity[data[, age] >= 9.5 & data[, age] < 10 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        23.460000000000001] <- "obesity"
    data$obesity[data[, age] >= 10 & data[, age] < 10.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.109999999999999] <- "obesity"
    data$obesity[data[, age] >= 10.5 & data[, age] < 11 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        24.77] <- "obesity"
    data$obesity[data[, age] >= 11 & data[, age] < 11.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        25.420000000000002] <- "obesity"
    data$obesity[data[, age] >= 11.5 & data[, age] < 12 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        26.050000000000001] <- "obesity"
    data$obesity[data[, age] >= 12 & data[, age] < 12.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        26.670000000000002] <- "obesity"
    data$obesity[data[, age] >= 12.5 & data[, age] < 13 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        27.239999999999998] <- "obesity"
    data$obesity[data[, age] >= 13 & data[, age] < 13.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        27.760000000000002] <- "obesity"
    data$obesity[data[, age] >= 13.5 & data[, age] < 14 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        28.199999999999999] <- "obesity"
    data$obesity[data[, age] >= 14 & data[, age] < 14.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        28.57] <- "obesity"
    data$obesity[data[, age] >= 14.5 & data[, age] < 15 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        28.870000000000001] <- "obesity"
    data$obesity[data[, age] >= 15 & data[, age] < 15.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.109999999999999] <- "obesity"
    data$obesity[data[, age] >= 15.5 & data[, age] < 16 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.289999999999999] <- "obesity"
    data$obesity[data[, age] >= 16 & data[, age] < 16.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.43] <- "obesity"
    data$obesity[data[, age] >= 16.5 & data[, age] < 17 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.559999999999999] <- "obesity"
    data$obesity[data[, age] >= 17 & data[, age] < 17.5 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.690000000000001] <- "obesity"
    data$obesity[data[, age] >= 17.5 & data[, age] < 18 & tolower(data[, sex]) == "female" & data[, bmi] >= 
        29.84] <- "obesity"
    data$obesity[data[, age] == 18 & tolower(data[, sex]) == "female" & data[, bmi] >= 30] <- "obesity"
    data$obesity
}
```


