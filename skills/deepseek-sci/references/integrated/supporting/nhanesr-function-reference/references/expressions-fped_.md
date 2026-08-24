# Integrated supporting reference: nhanesr-function-reference/references/expressions-fped_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-fped_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `fped_`

## `fped_download` [exported]

```r
function () 
{
    url <- sprintf(do::attr_href(set::grep_and(rvest::html_elements(xml2::read_html("https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fped-databases/"), 
        xpath = "//a[@href]"), c("FPED_", "sas.exe", "DR"))), fmt = "https://www.ars.usda.gov%s")
    fpeddir <- paste0(get_config_path(), "/fped")
    if (!dir.exists(fpeddir)) 
        dir.create(fpeddir, recursive = TRUE)
    url <- c(url, "https://www.ars.usda.gov/ARSUserFiles/80400530/foodlink/Mypyr_iff.exe", "https://www.ars.usda.gov/ARSUserFiles/80400530/foodlink/Mypyr_tot.exe", 
        "https://www.ars.usda.gov/ARSUserFiles/80400530/apps/MPED_2.EXE", "https://www.fns.usda.gov/sites/default/files/healthy_eating_index/cnppmyp_v1nhanes0304_wjfrt.sas7bdat", 
        "https://www.fns.usda.gov/sites/default/files/healthy_eating_index/cnppmyp_v1NHANES9900_wjfrt-SPSS.zip", 
        "https://www.fns.usda.gov/sites/default/files/healthy_eating_index/cnppmypyrequivdb_v1_wjfrt-SPSS.zip")
    for (i in 1:length(url)) {
        fi <- do::Replace0(tolower(do::file.name(url[i])), ".exe", ".sas7bdat", ".zip")
        ext <- ifelse(fi == "cnppmyp_v1nhanes0304_wjfrt", ".sas7bdat", ".zip")
        (destfile <- paste0(get_config_path(), "/fped/", fi, ext))
        cat(crayon::red(paste0(i, "/", length(url))), fi, "\n")
        nullcon <- file(nullfile(), open = "wb")
        sink(nullcon, type = "message")
        wait <- TRUE
        while (wait) {
            download <- tryCatch(download.file(url[i], destfile, mode = "wb"), error = function(e) "e", 
                warning = function(w) "w")
            wait <- ifelse(download == "e" | download == "w", TRUE, FALSE)
        }
        sink(type = "message")
        close(nullcon)
    }
    "https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/mypyramid-equivalents-product-downloads/"
    "https://www.ars.usda.gov/ARSUserFiles/80400530/apps/MPED_2.EXE"
    if (do::cnOS()) 
        cat(paste0(tmcn::toUTF8("\n<U+5DF2><U+6210><U+529F><U+4E0B><U+8F7D>"), i, tmcn::toUTF8("<U+4E2A>FPED<U+6587><U+4EF6>,<U+8BF7><U+52A0><U+538B><U+540E><U+518D><U+4F7F><U+7528>")))
    if (do::cnOS()) 
        cat(tmcn::toUTF8("\n\n<U+4E0B><U+8F7D><U+5730><U+5740>:"), fpeddir)
    if (!do::cnOS()) 
        cat(paste0("\nSuccessfully download ", i, " FPED files. Please unzip them before use\n\nPath of FPED:", 
            fpeddir))
}
```

## `fped_occasion` [exported]

```r
function (data, years, day = 1, fun = c("sum", "mean"), occasion = c("Breakfast", "Lunch", "Dinner"), 
    f_citmlb = FALSE, f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, 
    v_redor_tomato = FALSE, v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, 
    v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, 
    g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, 
    pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, 
    pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, 
    add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, Year = FALSE, join = "left", 
    cat = TRUE) 
{
    if (isTRUE(f_citmlb)) 
        f_citmlb = "f_citmlb"
    if (isTRUE(f_other)) 
        f_other = "f_other"
    if (isTRUE(f_whole)) 
        f_whole = "f_whole"
    if (isTRUE(f_juice)) 
        f_juice = "f_juice"
    if (isTRUE(f_total)) 
        f_total = "f_total"
    if (isTRUE(v_drkgr)) 
        v_drkgr = "v_drkgr"
    if (isTRUE(v_redor_tomato)) 
        v_redor_tomato = "v_redor_tomato"
    if (isTRUE(v_redor_other)) 
        v_redor_other = "v_redor_other"
    if (isTRUE(v_redor_total)) 
        v_redor_total = "v_redor_total"
    if (isTRUE(v_starchy_potato)) 
        v_starchy_potato = "v_starchy_potato"
    if (isTRUE(v_starchy_other)) 
        v_starchy_other = "v_starchy_other"
    if (isTRUE(v_starchy_total)) 
        v_starchy_total = "v_starchy_total"
    if (isTRUE(v_other)) 
        v_other = "v_other"
    if (isTRUE(v_total)) 
        v_total = "v_total"
    if (isTRUE(v_legumes)) 
        v_legumes = "v_legumes"
    if (isTRUE(g_whole)) 
        g_whole = "g_whole"
    if (isTRUE(g_refined)) 
        g_refined = "g_refined"
    if (isTRUE(g_total)) 
        g_total = "g_total"
    if (isTRUE(d_milk)) 
        d_milk = "d_milk"
    if (isTRUE(d_yogurt)) 
        d_yogurt = "d_yogurt"
    if (isTRUE(d_cheese)) 
        d_cheese = "d_cheese"
    if (isTRUE(d_total)) 
        d_total = "d_total"
    if (isTRUE(pf_meat)) 
        pf_meat = "pf_meat"
    if (isTRUE(pf_curedmeat)) 
        pf_curedmeat = "pf_curedmeat"
    if (isTRUE(pf_organ)) 
        pf_organ = "pf_organ"
    if (isTRUE(pf_poult)) 
        pf_poult = "pf_poult"
    if (isTRUE(pf_seafd_hi)) 
        pf_seafd_hi = "pf_seafd_hi"
    if (isTRUE(pf_seafd_low)) 
        pf_seafd_low = "pf_seafd_low"
    if (isTRUE(pf_mps_total)) 
        pf_mps_total = "pf_mps_total"
    if (isTRUE(pf_eggs)) 
        pf_eggs = "pf_eggs"
    if (isTRUE(pf_soy)) 
        pf_soy = "pf_soy"
    if (isTRUE(pf_nutsds)) 
        pf_nutsds = "pf_nutsds"
    if (isTRUE(pf_legumes)) 
        pf_legumes = "pf_legumes"
    if (isTRUE(pf_total)) 
        pf_total = "pf_total"
    if (isTRUE(add_sugars)) 
        add_sugars = "add_sugars"
    if (isTRUE(oils)) 
        oils = "oils"
    if (isTRUE(solid_fats)) 
        solid_fats = "solid_fats"
    if (isTRUE(a_drinks)) 
        a_drinks = "a_drinks"
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c()), 
        f_citmlb, "f_citmlb"), f_other, "f_other"), f_whole, "f_whole"), f_juice, "f_juice"), f_total, 
        "f_total"), v_drkgr, "v_drkgr"), v_redor_tomato, "v_redor_tomato"), v_redor_other, "v_redor_other"), 
        v_redor_total, "v_redor_total"), v_starchy_potato, "v_starchy_potato"), v_starchy_other, "v_starchy_other"), 
        v_starchy_total, "v_starchy_total"), v_other, "v_other"), v_total, "v_total"), v_legumes, "v_legumes"), 
        g_whole, "g_whole"), g_refined, "g_refined"), g_total, "g_total"), d_milk, "d_milk"), d_yogurt, 
        "d_yogurt"), d_cheese, "d_cheese"), d_total, "d_total"), pf_meat, "pf_meat"), pf_curedmeat, "pf_curedmeat"), 
        pf_organ, "pf_organ"), pf_poult, "pf_poult"), pf_seafd_hi, "pf_seafd_hi"), pf_seafd_low, "pf_seafd_low"), 
        pf_mps_total, "pf_mps_total"), pf_eggs, "pf_eggs"), pf_soy, "pf_soy"), pf_nutsds, "pf_nutsds"), 
        pf_legumes, "pf_legumes"), pf_total, "pf_total"), add_sugars, "add_sugars"), oils, "oils"), solid_fats, 
        "solid_fats"), a_drinks, "a_drinks")
    (var2 <- do::Replace0(var, ":.*"))
    years <- data_years(data, years)
    if (cat) 
        cat("\nload data")
    iff <- nhs_tsv("xiff|1iff", years = years, cat = FALSE)
    d <- nhs_read(iff, "drd030,drd030z,dr1_030z:eating.occasion.name", cat = FALSE)
    d <- drop_col(d, "drdifdcd", "dr1ifdcd", "dr1mc")
    if (cat) 
        cat("\nfped")
    d <- db_fped(data = d, day = day, dietary = "iff", fun = fun, f_citmlb = f_citmlb, f_other = f_other, 
        f_whole = f_whole, f_juice = f_juice, f_total = f_total, v_drkgr = v_drkgr, v_redor_tomato = v_redor_tomato, 
        v_redor_other = v_redor_other, v_redor_total = v_redor_total, v_starchy_potato = v_starchy_potato, 
        v_starchy_other = v_starchy_other, v_starchy_total = v_starchy_total, v_other = v_other, v_total = v_total, 
        v_legumes = v_legumes, g_whole = g_whole, g_refined = g_refined, g_total = g_total, d_milk = d_milk, 
        d_yogurt = d_yogurt, d_cheese = d_cheese, d_total = d_total, pf_meat = pf_meat, pf_curedmeat = pf_curedmeat, 
        pf_organ = pf_organ, pf_poult = pf_poult, pf_seafd_hi = pf_seafd_hi, pf_seafd_low = pf_seafd_low, 
        pf_mps_total = pf_mps_total, pf_eggs = pf_eggs, pf_soy = pf_soy, pf_nutsds = pf_nutsds, pf_legumes = pf_legumes, 
        pf_total = pf_total, add_sugars = add_sugars, oils = oils, solid_fats = solid_fats, a_drinks = a_drinks)
    d$eating.occasion.name <- tolower(d$eating.occasion.name)
    if (cat) 
        cat("\noccasion select")
    occasion <- tolower(occasion)
    d <- eval(parse(text = sprintf("select_row(d,eating.occasion.name %s c('%s'),cat=cat)", "%in%", paste0(occasion, 
        collapse = "','"))))
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    if (cat) 
        cat("\nCombine")
    for (i in 1:length(var2)) {
        if (i == 1) {
            di <- aggregate(x = d[, var2[i]], by = list(Year = d$Year, seqn = d$seqn, eating.occasion.name = d$eating.occasion.name), 
                FUN = ".sum.nona")
            colnames(di)[ncol(di)] <- var2[i]
            d2 <- di
        }
        else {
            di <- aggregate(x = d[, var2[i]], by = list(Year = d$Year, seqn = d$seqn, eating.occasion.name = d$eating.occasion.name), 
                FUN = ".sum.nona")
            colnames(di)[ncol(di)] <- var2[i]
            d2 <- dplyr::full_join(d2, di[, c("seqn", "eating.occasion.name", var2[i])], c("seqn", "eating.occasion.name"))
        }
    }
    d <- d2[order(d2$Year, d2$seqn, d2$eating.occasion.name), ]
    row.names(d) <- NULL
    head(d)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `fped_read` [exported]

```r
function (years, day = c("1", "2"), dietary = c("tot", "iff"), version = c("2010", "2015"), fun = c("sum", 
    "mean"), cat = FALSE) 
{
    day <- as.character(day)
    dietary <- match.arg(dietary)
    version <- as.character(version)
    version <- match.arg(version)
    if (length(day) == 1) {
        fped <- fped_readi(years, day, dietary, version, cat)
    }
    else if (length(day) == 2) {
        fun <- match.arg(fun)
        if (dietary == "iff") 
            join <- c("seqn", "food.code")
        else join <- "seqn"
        fped1 <- fped_readi(years, "1", dietary, version, cat)
        fped2 <- fped_readi(years, "2", dietary, version, cat)
        fped <- dplyr::full_join(fped1, fped2, join)
        choice <- set::not(colnames(fped2), join)
        for (i in choice) {
            which <- which(colnames(fped) %in% paste0(i, c(".x", ".y")))
            if (fun == "sum") {
                fped$last <- row.sums(fped[, which])
            }
            else if (fun == "mean") {
                fped$last <- row.means(fped[, which])
            }
            fped <- fped[, -which]
            colnames(fped)[ncol(fped)] <- i
        }
    }
    return(fped)
}
```

## `fped_read.g` [internal]

```r
function (years, day = c("1", "2"), fun = c("sum", "mean"), cat = FALSE) 
{
    day <- as.character(day)
    if (length(day) == 1) {
        fped <- fped_readi(years, day, "iff", cat = cat)
    }
    else if (length(day) == 2) {
        fun <- match.arg(fun)
        join <- c("seqn", "line")
        fped1 <- fped_readi(years, "1", "iff", cat = cat)
        fped2 <- fped_readi(years, "2", "iff", cat = cat)
        fped <- dplyr::inner_join(fped1, fped2, join)
        choice <- set::not(colnames(fped2), join)
        for (i in choice) {
            which <- which(colnames(fped) %in% paste0(i, c(".x", ".y")))
            if (fun == "sum") {
                fped$last <- row.sums(fped[, which])
            }
            else if (fun == "mean") {
                fped$last <- row.means(fped[, which])
            }
            fped <- fped[, -which]
            colnames(fped)[ncol(fped)] <- i
        }
    }
    return(fped)
}
```

## `fped_readi` [internal]

```r
function (years, day = c("1", "2"), dietary = c("tot", "iff"), version = c("2010", "2015"), cat = FALSE) 
{
    dietary <- dietary[1]
    day <- day[1]
    version <- version[1]
    fpeddir <- paste0(get_config_path(), "/fped")
    years <- prepare_years(years)
    mped <- data.frame()
    mpedfile <- c()
    if (dietary == "iff") 
        join <- c("seqn", "food.code")
    else join <- "seqn"
    var <- c(join, "ridageyr", "rstz", "f_total", "f_citmlb", "f_other", "v_drkgr", "v_tomato", "v_dpyel", 
        "v_potato", "v_starcy", "v_other", "v_total", "legumes", "g_whl", "g_nwhl", "g_total", "d_milk", 
        "d_yogurt", "d_cheese", "d_total", "m_meat", "m_frank", "m_organ", "m_poult", "m_fish_hi", "m_fish_lo", 
        "m_mpf", "m_egg", "m_soy", "m_nutsd", "add_sug", "discfat_oil", "discfat_sol", "a_bev")
    if ("1999-2000" %in% years) {
        mfile <- list.files(fpeddir, sprintf("pyr_%s.sas7bdat", dietary), recursive = TRUE, full.names = TRUE)
        mpedfile <- c(mpedfile, do::file.name(mfile))
        mped <- as.data.frame(haven::read_sas(mfile))
        colnames(mped) <- tolower(colnames(mped))
        mped$drddrstz <- ifelse(is.na(mped$drddrstz), mped$drddrsts, mped$drddrstz)
        mped <- drop_col(mped, "drddrsts")
        colnames(mped) <- rename_line(colnames(mped))
        colnames(mped) <- rename_rstz(colnames(mped))
        colnames(mped) <- rename_fdcd(colnames(mped), "food.code")
        mped <- mped[, var]
        seqn <- nhs_read(nhs_tsv("demo", years = 1999, cat = FALSE), "seqn", cat = FALSE)$seqn
        mped <- mped[mped$seqn %in% seqn, ]
        wjfrt <- as.data.frame(haven::read_spss(list.files(fpeddir, "cnppmyp_v1NHANES9900_wjfrt.sav", 
            full.names = TRUE)))
        colnames(wjfrt) <- tolower(colnames(wjfrt))
        colnames(wjfrt)[colnames(wjfrt) %in% "foodcode"] <- "food.code"
        isna <- is.na(wjfrt$food.code)
        wjfrt$food.code <- format(wjfrt$food.code, width = 8)
        wjfrt$food.code[isna] <- NA
        wjfrt$food.code <- as.numeric(wjfrt$food.code)
        iff <- nhs_read(nhs_tsv("drxiff", years = 1999, cat = FALSE), "seqn", cat = FALSE, Year = FALSE)
        jfrt <- dplyr::inner_join(iff, wjfrt, "food.code")
        colnames(jfrt)[colnames(jfrt) == "frtjuice"] <- "f_juice"
        colnames(jfrt)[colnames(jfrt) == "wholefrt"] <- "f_whole"
        if (dietary == "tot") {
            f_juice <- aggregate(jfrt$f_juice, list(seqn = jfrt$seqn), sum)
            colnames(f_juice)[2] <- "f_juice"
            f_whole <- aggregate(jfrt$f_whole, list(seqn = jfrt$seqn), sum)
            colnames(f_whole)[2] <- "f_whole"
            jfrt <- dplyr::inner_join(f_whole, f_juice, "seqn")
        }
        else {
            mped <- group_cal(d = mped, bys = c("seqn", "food.code"), max_vars = c("rstz", "ridageyr"), 
                sum_vars = set::not(colnames(mped), "seqn", "food.code", "ridageyr", "rstz"))
            jfrt <- group_cal(d = jfrt, bys = c("seqn", "food.code"), sum_vars = c("f_juice", "f_whole"))
        }
        mped <- dplyr::inner_join(mped, jfrt, join)
        mped$f_whole <- mped$f_citmlb + mped$f_other
        mped$f_total <- mped$f_citmlb + mped$f_other + mped$f_juice
    }
    if ("2001-2002" %in% years) {
        mfile <- list.files(fpeddir, sprintf("pyr_%s.sas7bdat", dietary), recursive = TRUE, full.names = TRUE)
        mpedfile <- unique(c(mpedfile, do::file.name(mfile)))
        mped01 <- as.data.frame(haven::read_sas(mfile))
        colnames(mped01) <- tolower(colnames(mped01))
        mped01$drddrstz <- ifelse(is.na(mped01$drddrstz), mped01$drddrsts, mped01$drddrstz)
        mped01 <- drop_col(mped01, "drddrsts")
        colnames(mped01)[colnames(mped01) == "drddrstz"] <- "rstz"
        colnames(mped01) <- rename_fdcd(colnames(mped01), "food.code")
        colnames(mped01)[colnames(mped01) == "fdcd"] <- "food.code"
        mped01 <- mped01[, var]
        seqn <- nhs_read(nhs_tsv("demo", years = 2001, cat = FALSE), "seqn", cat = FALSE)$seqn
        mped01 <- mped01[mped01$seqn %in% seqn, ]
        wjfrt <- as.data.frame(haven::read_spss(list.files(fpeddir, "cnppmypyrequivdb_v1_wjfrt.sav", 
            full.names = TRUE)))
        colnames(wjfrt) <- tolower(colnames(wjfrt))
        isna <- is.na(wjfrt$foodcode)
        wjfrt$food.code <- format(wjfrt$foodcode, width = 8)
        wjfrt$food.code[isna] <- NA
        iff <- nhs_read(nhs_tsv("drxiff", years = 2001, cat = FALSE), "seqn", cat = FALSE, Year = FALSE)
        colnames(iff)[colnames(iff) == "drxiline"] <- "line"
        wjfrt$food.code <- as.numeric(wjfrt$food.code)
        jfrt <- dplyr::inner_join(iff, wjfrt, "food.code")
        jfrt <- drop_col(jfrt, "drdifdcd", "foodname", "foodcode", "line")
        colnames(jfrt)[colnames(jfrt) == "frtjuice"] <- "f_juice"
        colnames(jfrt)[colnames(jfrt) == "wholefrt"] <- "f_whole"
        if (dietary == "tot") {
            f_juice <- aggregate(jfrt$f_juice, list(seqn = jfrt$seqn), sum)
            colnames(f_juice)[2] <- "f_juice"
            f_whole <- aggregate(jfrt$f_whole, list(seqn = jfrt$seqn), sum)
            colnames(f_whole)[2] <- "f_whole"
            jfrt <- dplyr::inner_join(f_whole, f_juice, "seqn")
        }
        else {
            mped01 <- group_cal(d = mped01, bys = c("seqn", "food.code"), max_vars = c("rstz", "ridageyr"), 
                sum_vars = set::not(colnames(mped01), "seqn", "food.code", "ridageyr", "rstz"))
            jfrt <- group_cal(d = jfrt, bys = c("seqn", "food.code"), sum_vars = c("f_juice", "f_whole"))
        }
        mped01 <- dplyr::inner_join(mped01, jfrt, join)
        mped01$f_whole <- mped01$f_citmlb + mped01$f_other
        mped01$f_total <- mped01$f_citmlb + mped01$f_other + mped01$f_juice
        mped <- rbind(mped, mped01)
    }
    if ("2003-2004" %in% years) {
        mped03 <- fped0304(day = day, dietary = dietary)
        mped <- rbind(mped, mped03)
    }
    var <- c(join, "ridageyr", "rstz", "f_citmlb", "f_other", "f_whole", "f_juice", "f_total", "v_drkgr", 
        "v_redor_tomato", "v_redor_other", "v_redor_total", "v_starchy_potato", "v_starchy_other", "v_starchy_total", 
        "v_other", "v_total", "v_legumes", "g_whole", "g_refined", "g_total", "d_milk", "d_yogurt", "d_cheese", 
        "d_total", "pf_meat", "pf_curedmeat", "pf_organ", "pf_poult", "pf_seafd_hi", "pf_seafd_low", 
        "pf_mps_total", "pf_eggs", "pf_soy", "pf_nutsds", "pf_legumes", "pf_total", "add_sugars", "oils", 
        "solid_fats", "a_drinks")
    if (nrow(mped) > 0) {
        colnames(mped)[colnames(mped) == "v_tomato"] <- "v_redor_tomato"
        colnames(mped)[colnames(mped) == "v_dpyel"] <- "v_redor_other"
        mped$v_redor_total <- mped$v_redor_other + mped$v_redor_tomato
        colnames(mped)[colnames(mped) == "v_potato"] <- "v_starchy_potato"
        colnames(mped)[colnames(mped) == "v_starcy"] <- "v_starchy_other"
        mped$v_starchy_total <- mped$v_starchy_other + mped$v_starchy_potato
        colnames(mped)[colnames(mped) == "legumes"] <- "v_legumes"
        colnames(mped)[colnames(mped) == "g_whl"] <- "g_whole"
        colnames(mped)[colnames(mped) == "g_nwhl"] <- "g_refined"
        colnames(mped)[colnames(mped) == "m_meat"] <- "pf_meat"
        colnames(mped)[colnames(mped) == "m_frank"] <- "pf_curedmeat"
        colnames(mped)[colnames(mped) == "m_organ"] <- "pf_organ"
        colnames(mped)[colnames(mped) == "m_poult"] <- "pf_poult"
        colnames(mped)[colnames(mped) == "m_fish_hi"] <- "pf_seafd_hi"
        colnames(mped)[colnames(mped) == "m_fish_lo"] <- "pf_seafd_low"
        colnames(mped)[colnames(mped) == "m_mpf"] <- "pf_mps_total"
        colnames(mped)[colnames(mped) == "m_egg"] <- "pf_eggs"
        colnames(mped)[colnames(mped) == "m_soy"] <- "pf_soy"
        colnames(mped)[colnames(mped) == "m_nutsd"] <- "pf_nutsds"
        mped$pf_legumes <- mped$v_legumes * 4
        mped$pf_total <- mped$pf_mps_total + mped$pf_eggs + mped$pf_soy + mped$pf_nutsds
        colnames(mped)[colnames(mped) == "add_sug"] <- "add_sugars"
        colnames(mped)[colnames(mped) == "discfat_oil"] <- "oils"
        colnames(mped)[colnames(mped) == "discfat_sol"] <- "solid_fats"
        colnames(mped)[colnames(mped) == "a_bev"] <- "a_drinks"
        mped <- mped[, var]
    }
    if (any(!years %in% prepare_years(1999:2004))) {
        (years2 <- sapply(years, function(i) do::Replace0(do::knife_left(i, 2), "-[0-9]{2}")))
        (pattern <- paste0("fped_dr", day, dietary, "_", years2, ".sas7bdat"))
        if (cat) 
            cat(paste0(paste0(c(mpedfile, pattern), collapse = "\n")), "\n")
        (fped <- list.files(path = fpeddir, pattern = paste0(pattern, collapse = "|"), ignore.case = TRUE, 
            full.names = TRUE, recursive = TRUE))
        x <- do.call(lapply(fped, function(i) {
            x <- haven::read_sas(i)
            colnames(x) <- do::Replace0(tolower(colnames(x)), "dr1t_", "dr2t_", "dr1i_", "dr2i_")
            colnames(x)[colnames(x) %in% c("dr1iline", "dr2iline")] <- "line"
            colnames(x)[colnames(x) %in% c("dr1drstz", "dr2drstz")] <- "rstz"
            colnames(x) <- rename_fdcd(colnames(x))
            x$f_whole <- x$f_citmlb + x$f_other
            x <- as.data.frame(x[, var])
            if (dietary == "iff") {
                ct <- kit::countOccur(x[, c("seqn", "food.code")])
                ct <- ct[ct$Count > 1, ]
                ck <- x$seqn %in% ct$seqn & x$food.code %in% ct$food.code
                di <- x[ck, ]
                di <- group_cal(d = di, max_vars = c("ridageyr", "rstz"), bys = c("seqn", "food.code"), 
                  sum_vars = set::not(colnames(di), "seqn", "food.code", "ridageyr", "rstz"))
                x <- rbind(x[!ck, colnames(di)], di)
            }
            x
        }), what = plyr::rbind.fill)
        mped <- rbind(mped, x)
    }
    if (version == "2010") {
        mped$seaplant <- mped$pf_seafd_hi + mped$pf_seafd_low + mped$pf_nutsds + mped$pf_soy
        mped$addsugc <- 16 * mped$add_sugars
        mped$solfatc <- mped$solid_fats * 9
    }
    else if (version == "2015") {
        mped$vtotalleg <- mped$v_total + mped$v_legumes
        mped$vdrkgrleg <- mped$v_drkgr + mped$v_legumes
        mped$pfallprotleg <- mped$pf_total + mped$pf_legumes
        mped$pfseaplantleg <- mped$pf_seafd_hi + mped$pf_seafd_low + mped$pf_nutsds + mped$pf_soy + mped$pf_legumes
    }
    mped <- mped[mped$ridageyr >= 2 & mped$rstz == 1, ]
    mped <- drop_col(mped, "rstz", "ridageyr")
    return(mped)
}
```


