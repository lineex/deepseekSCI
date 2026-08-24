# Integrated supporting reference: nhanesr-function-reference/references/expressions-dex_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-dex_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `dex_`

## `dex_ABPI` [exported]

```r
function (data, years, left_abpi = TRUE, right_abpi = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    abpi <- nhs_tsv("lexab", cat = FALSE, years = years)
    tsv0(abpi)
    d <- nhs_read(abpi, "lexlabpi:left_abpi", "lexrabpi:right_abpi", cat = FALSE)
    if (!left_abpi) 
        d <- drop_col(d, "left_abpi")
    if (!right_abpi) 
        d <- drop_col(d, "right_abpi")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_ABSI` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(years = years, waist_circumference_cm = "wc", BMI_kg.m2 = "bmi", height_cm = "height", 
        Year = TRUE)
    d$height <- d$height/100
    d$wc <- d$wc/100
    d$ABSI <- d$wc/(d$bmi^(2/3) * d$height^(1/2))
    d <- d[, c("seqn", "Year", "ABSI")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_AHA.PREVENT` [exported]

```r
function (data, years, CVD_10yr.risk = F, ASCVD_10yr.risk = F, HF_10yr.risk = F, component = F, Year = F, 
    join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(years = years, Year = T, ageyr = "age", sex = T, psu_strat = F) %>% db_HemalBiochemistry(fast_total_cholesterol_mg.dl = "tc", 
        hdl_cholesterol_mg.dl = "HDL") %>% db_blood.pressure(bpx = F, dar = T) %>% diag_DM(cat = F) %>% 
        diag_smoke() %>% diag_Hypertension(told = F, drug = "hp.drug", bpx = F, cat = F) %>% db_bodyMeasure(BMI_kg.m2 = "BMI")
    d <- d[d$age >= 30, ]
    d$female <- tolower(d$sex) %in% "female"
    d = Drug("statin", "!~nystatin|octreotide", data = d, take_drug = "tatin", remove.other = T)
    d$tatin <- ifelse(d$tatin %in% "yes", 1, 0)
    d <- dex_eGFR(d, method = "CKD_EPI_Scr_2021")
    colnames(d)[ncol(d)] <- "eGFR"
    colnames(d)[colnames(d) == "bpxsar"] <- "SBP"
    d$diabetes <- ifelse(d$DM %in% "DM", 1, 0)
    d$current_smoker <- ifelse(d$smoke %in% "now", 1, 0)
    d$hp.drug <- ifelse(d$hp.drug %in% "no", 1, 0)
    exp_fun <- function(x) {
        round(round(exp(x)/(1 + exp(x)), 6) * 100, 2)
    }
    d$tc <- (d$tc - 45) * 0.025860000000000001
    d$HDL <- d$HDL * 0.025860000000000001
    d[d$female, "CVD_10yr.risk"] <- with(d[d$female, ], -3.307728 + 0.79393290000000005 * (age - 55)/10 + 
        0.0305239 * (tc - 3.5) - 0.16068569999999999 * (HDL - 1.3)/0.29999999999999999 - 0.23940030000000001 * 
        (pmin(SBP, 110) - 110)/20 + 0.36007800000000001 * (pmax(SBP, 110) - 130)/20 + 0.86676039999999999 * 
        (diabetes) + 0.53607389999999999 * (current_smoker) + 0.60459169999999995 * (pmin(eGFR, 60) - 
        60)/-15 + 0.043376900000000003 * (pmax(eGFR, 60) - 90)/-15 + 0.31516719999999998 * (hp.drug) - 
        0.14776549999999999 * (tatin) - 0.066361199999999995 * (hp.drug) * (pmax(SBP, 110) - 130)/20 + 
        0.1197879 * (tatin) * (tc - 3.5) - 0.081971500000000003 * (age - 55)/10 * (tc - 3.5) + 0.0306769 * 
        (age - 55)/10 * (HDL - 1.3)/0.29999999999999999 - 0.094634800000000005 * (age - 55)/10 * (pmax(SBP, 
        110) - 130)/20 - 0.27056999999999998 * (age - 55)/10 * (diabetes) - 0.078714999999999993 * (age - 
        55)/10 * (current_smoker) - 0.1637806 * (age - 55)/10 * (pmin(eGFR, 60) - 60)/-15) %>% exp_fun()
    d[!d$female, "CVD_10yr.risk"] <- with(d[!d$female, ], -3.0311680000000001 + 0.7688528 * (age - 55)/10 + 
        0.0736174 * (tc - 3.5) - 0.095443100000000003 * (HDL - 1.3)/0.29999999999999999 - 0.43473450000000002 * 
        (pmin(SBP, 110) - 110)/20 + 0.3362658 * (pmax(SBP, 110) - 130)/20 + 0.76928569999999996 * (diabetes) + 
        0.4386871 * (current_smoker) + 0.53789790000000004 * (pmin(eGFR, 60) - 60)/-15 + 0.016482699999999999 * 
        (pmax(eGFR, 60) - 90)/-15 + 0.288879 * (hp.drug) - 0.13373489999999999 * (tatin) - 0.0475924 * 
        (hp.drug) * (pmax(SBP, 110) - 130)/20 + 0.15027299999999999 * (tatin) * (tc - 3.5) - 0.051787399999999997 * 
        (age - 55)/10 * (tc - 3.5) + 0.019116899999999999 * (age - 55)/10 * (HDL - 1.3)/0.29999999999999999 - 
        0.1049477 * (age - 55)/10 * (pmax(SBP, 110) - 130)/20 - 0.2251948 * (age - 55)/10 * (diabetes) - 
        0.089506699999999995 * (age - 55)/10 * (current_smoker) - 0.15437020000000001 * (age - 55)/10 * 
        (pmin(eGFR, 60) - 60)/-15) %>% exp_fun()
    d[d$female, "ASCVD_10yr.risk"] <- with(d[d$female, ], (HDL - 1.3)/0.29999999999999999 - 0.083535799999999993 * 
        (pmin(SBP, 110) - 110)/20 + 0.35928520000000003 * (pmax(SBP, 110) - 130)/20 + 0.83485849999999995 * 
        (diabetes) + 0.48310779999999998 * (current_smoker) + 0.4864619 * (pmin(eGFR, 60) - 60)/-15 + 
        0.039777899999999998 * (pmax(eGFR, 60) - 90)/-15 + 0.22653090000000001 * (hp.drug) - 0.059237400000000003 * 
        (tatin) - 0.039576199999999999 * (hp.drug) * (pmax(SBP, 110) - 130)/20 + 0.084442299999999998 * 
        (tatin) * (tc - 3.5) - 0.056783899999999998 * (age - 55)/10 * (tc - 3.5) + 0.0325692 * (age - 
        55)/10 * (HDL - 1.3)/0.29999999999999999 - 0.1035985 * (age - 55)/10 * (pmax(SBP, 110) - 130)/20 - 
        0.2417542 * (age - 55)/10 * (diabetes) - 0.079114199999999996 * (age - 55)/10 * (current_smoker) - 
        0.1671492 * (age - 55)/10 * (pmin(eGFR, 60) - 60)/-15) %>% exp_fun()
    d[!d$female, "ASCVD_10yr.risk"] <- with(d[!d$female, ], -3.5006550000000001 + 0.70998470000000002 * 
        (age - 55)/10 + 0.16586629999999999 * (tc - 3.5) - 0.1144285 * (HDL - 1.3)/0.29999999999999999 - 
        0.28372120000000001 * (pmin(SBP, 110) - 110)/20 + 0.3239977 * (pmax(SBP, 110) - 130)/20 + 0.71895969999999998 * 
        (diabetes) + 0.39569729999999997 * (current_smoker) + 0.36900749999999999 * (pmin(eGFR, 60) - 
        60)/-15 + 0.020361899999999999 * (pmax(eGFR, 60) - 90)/-15 + 0.20365220000000001 * (hp.drug) - 
        0.086558099999999999 * (tatin) - 0.032291599999999997 * (hp.drug) * (pmax(SBP, 110) - 130)/20 + 
        0.114563 * (tatin) * (tc - 3.5) - 0.030000499999999999 * (age - 55)/10 * (tc - 3.5) + 0.023274699999999999 * 
        (age - 55)/10 * (HDL - 1.3)/0.29999999999999999 - 0.092702400000000004 * (age - 55)/10 * (pmax(SBP, 
        110) - 130)/20 - 0.20185249999999999 * (age - 55)/10 * (diabetes) - 0.097052700000000006 * (age - 
        55)/10 * (current_smoker) - 0.1217081 * (age - 55)/10 * (pmin(eGFR, 60) - 60)/-15) %>% exp_fun()
    d[d$female, "HF_10yr.risk"] <- with(d[d$female, ], -4.3104089999999999 + 0.8998235 * (age - 55)/10 - 
        0.45597710000000002 * (pmin(SBP, 110) - 110)/20 + 0.35765049999999998 * (pmax(SBP, 110) - 130)/20 + 
        1.038346 * (diabetes) + 0.58391599999999999 * (current_smoker) - 0.0072294000000000004 * (pmin(BMI, 
        30) - 25)/5 + 0.2997706 * (pmax(BMI, 30) - 30)/5 + 0.74516380000000004 * (pmin(eGFR, 60) - 60)/-15 + 
        0.0557087 * (pmax(eGFR, 60) - 90)/-15 + 0.35344419999999999 * (hp.drug) - 0.098151100000000005 * 
        (hp.drug) * (pmax(SBP, 110) - 130)/20 - 0.094666299999999995 * (age - 55)/10 * (pmax(SBP, 110) - 
        130)/20 - 0.35810409999999998 * (age - 55)/10 * (diabetes) - 0.1159453 * (age - 55)/10 * (current_smoker) - 
        0.0038779999999999999 * (pmax(BMI, 30) - 30)/5 - 0.18842890000000001 * (age - 55)/10 * (pmin(eGFR, 
        60) - 60)/-15) %>% exp_fun()
    d[!d$female, "HF_10yr.risk"] <- with(d[!d$female, ], -3.9463910000000002 + 0.89726419999999996 * 
        (age - 55)/10 - 0.68114660000000005 * (pmin(SBP, 110) - 110)/20 + 0.36344609999999999 * (pmax(SBP, 
        110) - 130)/20 + 0.92377600000000004 * (diabetes) + 0.50237359999999998 * (current_smoker) - 
        0.048584099999999998 * (pmin(BMI, 30) - 25)/5 + 0.37269289999999999 * (pmax(BMI, 30) - 30)/5 + 
        0.69269170000000002 * (pmin(eGFR, 60) - 60)/-15 + 0.025182699999999999 * (pmax(eGFR, 60) - 90)/-15 + 
        0.29809219999999997 * (hp.drug) - 0.049773100000000001 * (hp.drug) * (pmax(SBP, 110) - 130)/20 - 
        0.12892010000000001 * (age - 55)/10 * (pmax(SBP, 110) - 130)/20 - 0.30409239999999998 * (age - 
        55)/10 * (diabetes) - 0.14016880000000001 * (age - 55)/10 * (current_smoker) + 0.0068126000000000003 * 
        (pmax(BMI, 30) - 30)/5 - 0.17977779999999999 * (age - 55)/10 * (pmin(eGFR, 60) - 60)/-15) %>% 
        exp_fun()
    d <- d[, c("Year", "seqn", "CVD_10yr.risk", "ASCVD_10yr.risk", "HF_10yr.risk", "age", "sex", "tc", 
        "HDL", "SBP", "bpxdar", "DM", "smoke", "Hypertension", "hp.drug", "BMI", "female", "tatin", "eGFR", 
        "diabetes", "current_smoker")]
    d$tatin <- ifelse(d$tatin %in% 1, "yes", "no")
    d$diabetes <- ifelse(d$DM %in% 1, "yes", "no")
    d$current_smoker <- ifelse(d$smoke %in% 1, "yes", "no")
    d$hp.drug <- ifelse(d$hp.drug %in% 1, "yes", "no")
    vars <- c("Year", "seqn")
    if (!isFALSE(CVD_10yr.risk)) 
        vars <- c(vars, "CVD_10yr.risk")
    if (!isFALSE(ASCVD_10yr.risk)) 
        vars <- c(vars, "ASCVD_10yr.risk")
    if (!isFALSE(HF_10yr.risk)) 
        vars <- c(vars, "HF_10yr.risk")
    if (component) {
        vars <- c(vars, "age", "sex", "tc", "HDL", "SBP", "bpxdar", "DM", "hp.drug", "BMI", "tatin", 
            "eGFR", "diabetes", "current_smoker")
    }
    d <- d[, vars]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_AIP` [exported]

```r
function (data = NULL, years, weight = FALSE, Year = FALSE, join = "left", cat = TRUE) 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(years = years, Year = TRUE, fast_triglyceride_mmol.L = "tg", hdl_cholesterol_mmol.L = "hdl", 
        wtsaf2yr = TRUE, wtsaf4yr = TRUE)
    d$AIP <- log10(d$tg/d$hdl)
    var2 <- c("seqn", "Year", "AIP")
    if (weight) {
        if (all(c("1999-2000", "2001-2002") %in% d$Year) & length(unique(d$Year)) == 2) {
            if (cat) 
                cat("wtsaf4yr for lipid was chosen")
            col_rename(d) <- "wtsaf4yr:wtsaf4yr"
            d <- drop_col(d, "wtsaf2yr")
            append(var2) <- "wtsaf4yr"
        }
        else if (all(c("1999-2000", "2001-2002") %in% d$Year) & length(unique(d$Year)) > 2) {
            if (cat) 
                cat("wtsaf4yr for lipid was chosen in 1999-2000 and 2001-2002")
            if (cat) 
                cat("\nwtsaf4yr for lipid was chosen in the others")
            col_rename(d) <- "wtsaf2yr:wtsaf2yr"
            d$wtsaf2yr[d$Year %in% c("1999-2000", "2001-2002")] <- d$wtsaf4yr[d$Year %in% c("1999-2000", 
                "2001-2002")]
            append(var2) <- "wtsaf2yr"
            d <- drop_col(d, "wtsaf4yr")
        }
        else {
            if (cat) 
                cat("wtsaf2yr for lipid was chosen")
            col_rename(d) <- "wtsaf2yr:wtsaf2yr"
            append(var2) <- "wtsaf2yr"
            d <- drop_col(d, "wtsaf4yr")
        }
    }
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_ASCVD.h10yr` [exported]

```r
function (data, years, age = "[40,79]", restrict.Race = TRUE, component = FALSE, weight = FALSE, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    d <- db_ogtt(diag_DM(diag_smoke(drug_anti.Hypertensive(db_blood.pressure(db_HemalBiochemistry(db_demo(years = years, 
        Year = TRUE, psu_strat = F, lower_cd = TRUE, sex = T, eth1 = "eth", ageyr = "age", ), fast_total_cholesterol_mg.dl = "tc", 
        hdl_cholesterol_mg.dl = "hdl", wtsaf2yr = TRUE, wtsaf4yr = TRUE), dar = TRUE, bpx = FALSE), take_drug = "hb.drug", 
        yes.code = 1, other.code = 0, no.code = 0), now = 1, former = 0, never = 0), told = TRUE, drug = T, 
        rand_glu = F, HbA1c = T, fast_glu = T, OGTT2 = T, DM1 = 1, cat = F), ogtt_subsample_2_year_mec_weight = "wtsog2yr")
    if (restrict.Race) 
        d <- d[d$eth %in% "non-hispanic white", ]
    d <- d[bu(d$age, age), ]
    d <- drop_row(d, is.na(age) | is.na(tc) | is.na(hb.drug) | is.na(hdl) | is.na(bpxsar) | is.na(smoke) | 
        is.na(DM), cat = F)
    ln.age <- log(d$age)
    ln.tc <- log(d$tc)
    ln.hdl <- log(d$hdl)
    ln.sar <- log(d$bpxsar)
    smoke <- d$smoke
    dm <- as.numeric(d$DM)
    hbp.coef <- ifelse(d$hb.drug == 1, 2.0190000000000001, 1.9570000000000001)
    score <- ln.age * -29.798999999999999 + ln.age^2 * 4.8840000000000003 + ln.tc * 13.539999999999999 + 
        ln.age * ln.tc * -3.1139999999999999 + ln.hdl * -13.577999999999999 + ln.age * ln.hdl * 3.149 + 
        ln.sar * hbp.coef + smoke * 7.5739999999999998 + ln.age * smoke * -1.665 + dm * 0.66100000000000003
    ck <- d$sex == "female"
    d$ASCVD.10risk[ck] <- 1 - 0.96650000000000003^exp(score[ck] - (-29.18))
    hbp.coef <- ifelse(d$hb.drug == 1, 1.7969999999999999, 1.764)
    score <- ln.age * 12.343999999999999 + ln.tc * 11.853 + ln.age * ln.tc * -2.6640000000000001 + ln.hdl * 
        -7.9900000000000002 + ln.age * ln.hdl * 1.7689999999999999 + ln.sar * hbp.coef + smoke * 7.8369999999999997 + 
        ln.age * smoke * -1.7949999999999999 + dm * 0.65800000000000003
    ck <- d$sex == "male"
    d$ASCVD.10risk[ck] <- 1 - 0.91439999999999999^exp(score[ck] - 61.18)
    d$ASCVD.10risk <- round(d$ASCVD.10risk, 7)
    var <- c("seqn", "Year", "ASCVD.10risk")
    if (component) 
        var <- c(var, "age", "tc", "hdl", "bpxsar", "smoke", "DM")
    if (weight) {
        ogtt.years <- prepare_years(nhs_tsv("ogtt", cat = F))
        if (all(unique(d$Year) %in% ogtt.years)) {
            wt.select <- "wtsog2yr"
        }
        else {
            col_rename(d) <- c("wtsaf2yr:wtsaf2yr", "wtsaf4yr:wtsaf4yr")
            if (all(c("1999-2000", "2001-2002") %in% unique(d$Year))) {
                if (length(unique(d$Year)) == 2) {
                  wt.select <- "wtsaf4yr"
                }
                else {
                  wt.select <- c("wtsaf2yr", "wtsaf4yr")
                }
            }
            else {
                wt.select <- "wtsaf2yr"
            }
        }
        var <- c(var, wt.select)
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_BARD` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- diag_DM(db_HemalBiochemistry(db_bodyMeasure(BMI_kg.m2 = "bmi", years = years, Year = TRUE), 
        Alt = TRUE, Ast = TRUE), cat = FALSE, told = TRUE, HbA1c = F, fast_glu = F, OGTT2 = F, rand_glu = F, 
        drug = T)
    d$bmi <- ifelse(d$bmi >= 28, 1, 0)
    d$aar <- d$Ast/d$Alt
    d$DM <- ifelse(d$DM %in% c("DM", "GDM"), 1, 0)
    d$BARD <- row.sums(d[, c("bmi", "aar", "DM")])
    d <- d[, c("Year", "seqn", "BARD")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_BRI` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(years = years, waist_circumference_cm = "wc", height_cm = "height", Year = TRUE)
    d$height <- d$height/100
    d$wc <- d$wc/100
    d$BRI <- 364.19999999999999 - 365.5 * sqrt(1 - (d$wc/(2 * pi)/(0.5 * d$height))^2)
    d <- d[, c("seqn", "Year", "BRI")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_BiologicalAge` [exported]

```r
function (data, biomarkers = NULL, by = NULL) 
{
    if (!"age" %in% colnames(data)) 
        stop("age was not found in data")
    data$datasseeqqnn <- 1:nrow(data)
    biomarkers <- set::not(biomarkers, "age")
    vars <- c("datasseeqqnn", "age", biomarkers, by)
    ck <- complete.cases(data[, vars])
    if (!all(ck)) 
        stop(tmcn::toUTF8("biomarkers<U+4E2D><U+6709><U+7F3A><U+5931><U+503C>"))
    d <- data[ck, vars]
    if (is.null(by)) {
        d <- BA.i(d, biomarkers)
    }
    else {
        group <- paste0_columns(d[, by, drop = FALSE], collapse = ";;;")
        gu <- unique(group)
        gu <- gu[!is.na(gu)]
        d <- do.call(lapply(gu, function(i) {
            di <- d[group %in% i, ]
            BA.i(di, biomarkers)
        }), what = rbind)
    }
    drop_col(dplyr::left_join(data, d, "datasseeqqnn"), "datasseeqqnn")
}
```

## `dex_CALLY` [exported]

```r
function (data, years, all = FALSE, CALLY = T, crp, alb, lym, Year = F, join = "left") 
{
    ck <- all(miss(crp), miss(alb), miss(lym), miss(CALLY))
    if (all) {
        if (ck) {
            crp <- TRUE
            alb <- TRUE
            lym <- TRUE
            CALLY <- TRUE
        }
        else {
            if (miss(crp)) 
                crp <- TRUE
            if (miss(alb)) 
                alb <- TRUE
            if (miss(lym)) 
                lym <- TRUE
            if (miss(CALLY)) 
                CALLY <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(crp)) 
                crp <- FALSE
            if (miss(alb)) 
                alb <- FALSE
            if (miss(lym)) 
                lym <- FALSE
            if (miss(CALLY)) 
                CALLY <- FALSE
        }
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "seqn", "seqn"), CALLY, "CALLY"), crp, "crp"), alb, "alb"), lym, "lym")
    if (isTRUE(crp)) 
        crp = "crp"
    if (isTRUE(alb)) 
        alb = "alb"
    if (isTRUE(lym)) 
        lym = "lym"
    if (isTRUE(CALLY)) 
        CALLY = "CALLY"
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(C_reactive_protein_mg.dl = "crp", Year = T, years = years) %>% db_HemalBiochemistry(albumin_g.L = "alb") %>% 
        db_cbc(lymphocyte_number_1000cells.ul = "lym")
    d$CALLY <- d$alb * d$lym/d$crp
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_CCI` [exported]

```r
function (data, years, cci_number = FALSE, Year = FALSE, join = "left") 
{
    diabetes = 1
    diabetes_retinopathy = 2
    Kidney_failure = 2
    Kidney_stones = 2
    heart_failure = 1
    stroke = 1
    liver_disease = 2
    arthritis = 1
    bladder_cancer = 2
    bone_cancer = 2
    brain_cancer = 2
    breast_cancer = 2
    cervical_cancer = 2
    colon_cancer = 2
    esophageal_cancer = 2
    gallbladder_cancer = 2
    kidney_cancer = 2
    Tracheal_carcinoma = 2
    leukemia = 2
    liver_cancer = 2
    lung_cancer = 2
    lymphoma = 2
    melanoma = 2
    oral_cancer = 2
    never_cancer = 2
    ovarian_cancer = 2
    pancreatic_cancer = 2
    prostate_cancer = 2
    rectal_cancer = 2
    skin_cancer = 2
    unknown_skin_cancer = 2
    soft_tissue_cancer = 2
    stomach_cancer = 2
    testicular_cancer = 2
    thyroid_cancer = 2
    uterine_cancer = 2
    other_cancer = 2
    years <- data_years(data, years)
    diq <- nhs_tsv("diq", years = years, cat = FALSE)
    kiq <- nhs_tsv("kiq", "!~kiq_p", years = years, cat = FALSE)
    mcq <- nhs_tsv("mcq", years = years, cat = FALSE)
    spx <- nhs_tsv("spx", years = years, cat = FALSE)
    d <- nhs_read(diq, "diq080:diabetes_retinopathy", kiq, "kiq020,kiq022:Kidney_failure", "kiq026:Kidney_stones", 
        mcq, "mcq160b:heart_failure", "mcq160f:stroke", "mcq160l:liver_disease", "mcq500:liver_disease.1", 
        "mcq160a:arthritis", "mcq240a:bladder_cancer", "mcq240c:bone_cancer", "mcq240d:brain_cancer", 
        "mcq240e:breast_cancer", "mcq240f:cervical_cancer", "mcq240g:colon_cancer", "mcq240h:esophageal_cancer", 
        "mcq240i:gallbladder_cancer", "mcq240j:kidney_cancer", "mcq240k:Tracheal_carcinoma", "mcq240l:leukemia", 
        "mcq240m:liver_cancer", "mcq240n:lung_cancer", "mcq240o:lymphoma", "mcq240p:melanoma", "mcq240q:oral_cancer", 
        "mcq240r:never_cancer", "mcq240s:ovarian_cancer", "mcq240t:pancreatic_cancer", "mcq240u:prostate_cancer", 
        "mcq240v:rectal_cancer", "mcq240w:skin_cancer", "mcq240x:unknown_skin_cancer", "mcq240y:soft_tissue_cancer", 
        "mcq240z:stomach_cancer", "mcq240aa:testicular_cancer", "mcq240bb:thyroid_cancer", "mcq240cc:uterine_cancer", 
        "mcq240dd:other_cancer", spx, "spq070d:stroke.1", refuse_dontknow_toNA = TRUE, lower_cd = TRUE, 
        years = years, cat = FALSE)
    d <- diag_DM(d, cat = FALSE, told = F, drug = F, HbA1c = T, fast_glu = T, OGTT2 = T, rand_glu = T)
    colnames(d)[colnames(d) == "DM"] <- "diabetes"
    d$diabetes <- ifelse(d$diabetes == "DM" | d$diabetes == "GDM", "yes", "no")
    if ("liver_disease.1" %in% colnames(d) & "liver_disease" %in% colnames(d)) {
        d$liver_disease[is.na(d$liver_disease)] <- d$liver_disease.1[is.na(d$liver_disease)]
    }
    if ("stroke.1" %in% colnames(d) & "stroke" %in% colnames(d)) {
        d$stroke[d$stroke.1 > 0] <- "yes"
    }
    d <- drop_col(d, "liver_disease.1", "stroke.1")
    disease <- c("diabetes", "diabetes_retinopathy", "Kidney_failure", "Kidney_stones", "heart_failure", 
        "stroke", "liver_disease", "arthritis")
    for (i in disease) {
        if (i %in% colnames(d)) {
            eval(parse(text = sprintf("d[,i] <- ifelse(d[,i] == 1 | d[,i] == \"yes\" ,%s,0)", i)))
        }
    }
    cancer <- c("bladder_cancer", "bone_cancer", "brain_cancer", "breast_cancer", "cervical_cancer", 
        "colon_cancer", "esophageal_cancer", "gallbladder_cancer", "kidney_cancer", "Tracheal_carcinoma", 
        "leukemia", "liver_cancer", "lung_cancer", "lymphoma", "melanoma", "oral_cancer", "never_cancer", 
        "ovarian_cancer", "pancreatic_cancer", "prostate_cancer", "rectal_cancer", "skin_cancer", "unknown_skin_cancer", 
        "soft_tissue_cancer", "stomach_cancer", "testicular_cancer", "thyroid_cancer", "uterine_cancer", 
        "other_cancer")
    for (i in cancer) {
        if (i %in% colnames(d)) {
            d[, i] <- as.numeric(do::Replace0(d[, i], " .*"))
            eval(parse(text = sprintf("d[,i] <- ifelse(d[,i] >0,%s,0)", i)))
        }
    }
    d$CCI <- row.sums(d[, set::not(colnames(d), "seqn", "Year")])
    var <- c("seqn", "Year", "CCI")
    if (cci_number) {
        di <- d[, set::not(colnames(d), "seqn", "Year", "CCI")]
        di[di >= 0] <- 1
        d$cci_number <- row.sums(di)
        var <- c(var, "cci_number")
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_CDAI` [exported]

```r
function (data, years, day = 1, both2days = T, component = FALSE, Year = FALSE, join = "left", round = 3) 
{
    years <- data_years(data, years)
    d <- db_demo(db_carotenoid(db_drtot(years = years, Year = TRUE, vitamin_A_rae_mcg = "vit_A", vitamin_C_mg = "vit_C", 
        vitamin_E_as_alpha_tocopherol_mg = "vit_E", selenium_mcg = "Se", zinc_mg = "Zinc", day = day, 
        fun = "mean", both2days = both2days), day = day, fun = "mean", both2days = both2days, ds = F, 
        all.5 = F), sex = T)
    if (!missing(data)) 
        d <- d[d$seqn %in% data$seqn, ]
    x <- c("vit_A", "vit_C", "vit_E", "Zinc", "Se", "carotenoid")
    ck.m <- tolower(d$sex) %in% "male"
    ck.fm <- tolower(d$sex) %in% "female"
    for (i in x) {
        d[ck.m, "i"] <- (d[ck.m, i] - mean(d[ck.m, i], na.rm = TRUE))/sd(d[ck.m, i], na.rm = TRUE)
        d[ck.fm, "i"] <- (d[ck.fm, i] - mean(d[ck.fm, i], na.rm = TRUE))/sd(d[ck.fm, i], na.rm = TRUE)
        colnames(d)[ncol(d)] <- paste0("cdai_", i)
    }
    d$CDAI <- round(rowSums(d[, lookl(colnames(d), "cdai_")]), round)
    var <- c("seqn", "Year", "CDAI")
    if (component) 
        append(var) <- x
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_CMDS` [exported]

```r
function (data, years, weight = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    diq <- nhs_tsv("diq", items = "question", cat = FALSE, years = years)
    d <- db_ogtt(drug_anti.Hyperlipidemic(db_HemalBiochemistry(diag_Hypertension(db_demo(db_bodyMeasure(nhs_read(diq, 
        "diq010:told", Year = TRUE, cat = F, lower_cd = T), waist_circumference_cm = "wc"), sex = "sex", 
        psu_strat = F, lower_cd = TRUE), told = FALSE, method = "mean", systolic = 130, diastolic = 85, 
        cat = FALSE), hdl_cholesterol_mg.dl = "hdl", fast_triglyceride_mg.dl = "tg", fast_glucose_mg.dl = "glu", 
        wtsaf2yr = TRUE, wtsaf4yr = TRUE), take_drug = "lipid", remove.other = TRUE, no.code = 0, yes.code = 1, 
        other.code = 0), two_hour_glucose_ogtt_mg.dl = "ogtt2", ogtt_subsample_2_year_mec_weight = "wtsog2yr")
    d <- Drug("niacin", data = d, take_drug = "niacin", yes.code = 1, no.code = 0, other.code = 0, remove.other = TRUE)
    d$Hypertension <- ifelse(d$Hypertension == "yes", 1, 0)
    ck <- (d$sex == "male" & d$wc >= 112) | (d$sex == "female" & d$wc >= 88)
    d$s1.wc <- ifelse(ck, 1, 0)
    d$s1.hbp <- d$Hypertension
    ck <- (d$sex == "male" & d$hdl < 40) | (d$sex == "female" & d$hdl < 50)
    d$hdl <- ifelse(ck, 1, 0)
    d$s1.hdl <- ifelse(row.sums(d[, c("hdl", "niacin")]) >= 1, 1, 0)
    d$tg <- ifelse(d$tg >= 150, 1, 0)
    d$s1.tg <- ifelse(row.sums(d[, c("tg", "lipid")]) >= 1, 1, 0)
    d$s1 <- ifelse(row.sums(d[, c("s1.wc", "s1.hbp", "s1.hdl", "s1.tg")]) %=% c(1, 2), 1, 0)
    d$s2.a <- ifelse(row.sums(d[, c("s1.wc", "s1.hbp", "s1.hdl", "s1.tg")]) >= 1, 1, 0)
    d$s2.b <- ifelse(d$glu >= 100, 1, 0)
    if ("ogtt2" %in% colnames(d)) 
        d$s2.c <- ifelse(d$ogtt2 >= 140, 1, 0)
    d$s2 <- ifelse(row.sums(select_col(d, c("s2.a", "s2.b", "s2.c"))) == 1, 2, 0)
    d$s3 <- ifelse(row.sums(select_col(d, c("s2.a", "s2.b", "s2.c"))) == 2, 3, 0)
    d <- diag_CVD(drug_anti.Diabetic(d, take_drug = "dm.drug", remove.other = TRUE, other.code = 0, yes.code = 1, 
        no.code = 0))
    ck <- d$glu >= 126 | d$dm.drug == 1 | d$told == "yes"
    if ("ogtt2" %in% colnames(d)) 
        ck <- ck | d$ogtt2 >= 200
    d$s4.t2dm <- ifelse(ck, 1, 0)
    d$s4.cvd <- ifelse(d$CVD == "yes", 1, 0)
    d$s4 <- ifelse(row.sums(d[, c("s4.cvd", "s4.t2dm")]) >= 1, 4, 1)
    d$cmds <- row.max(d[, c("s1", "s2", "s3", "s4")])
    ogtt.years <- prepare_years(nhs_tsv("ogtt", cat = F))
    var <- c("seqn", "Year", "cmds")
    if (weight) {
        if (all(unique(d$Year) %in% ogtt.years)) {
            wt.select <- "wtsog2yr"
        }
        else {
            col_rename(d) <- c("wtsaf2yr:wtsaf2yr", "wtsaf4yr:wtsaf4yr")
            if (all(c("1999-2000", "2001-2002") %in% unique(d$Year))) {
                if (length(unique(d$Year)) == 2) {
                  wt.select <- "wtsaf4yr"
                }
                else {
                  wt.select <- c("wtsaf2yr", "wtsaf4yr")
                }
            }
            else {
                wt.select <- "wtsaf2yr"
            }
        }
        var <- c(var, wt.select)
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_CMI` [exported]

```r
function (data, years, CMI, tg_mmol.L, hdl_mmol.L, WHtR, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    all = FALSE
    seqn = T
    ck <- all(missing(seqn), missing(CMI), missing(tg_mmol.L), missing(hdl_mmol.L), missing(WHtR))
    if (all) {
        if (ck) {
            seqn <- TRUE
            CMI <- TRUE
            tg_mmol.L <- TRUE
            hdl_mmol.L <- TRUE
            WHtR <- TRUE
        }
        else {
            if (missing(seqn)) 
                seqn <- TRUE
            if (missing(CMI)) 
                CMI <- TRUE
            if (missing(tg_mmol.L)) 
                tg_mmol.L <- TRUE
            if (missing(hdl_mmol.L)) 
                hdl_mmol.L <- TRUE
            if (missing(WHtR)) 
                WHtR <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (missing(seqn)) 
                seqn <- FALSE
            if (missing(CMI)) 
                CMI <- FALSE
            if (missing(tg_mmol.L)) 
                tg_mmol.L <- FALSE
            if (missing(hdl_mmol.L)) 
                hdl_mmol.L <- FALSE
            if (missing(WHtR)) 
                WHtR <- FALSE
        }
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        seqn, "seqn"), CMI, "CMI"), tg_mmol.L, "tg_mmol.L"), hdl_mmol.L, "hdl_mmol.L"), WHtR, "WHtR")
    if (isTRUE(seqn)) 
        seqn = "seqn"
    if (isTRUE(CMI)) 
        CMI = "CMI"
    if (isTRUE(tg_mmol.L)) 
        tg_mmol.L = "tg_mmol.L"
    if (isTRUE(hdl_mmol.L)) 
        hdl_mmol.L = "hdl_mmol.L"
    if (isTRUE(WHtR)) 
        WHtR = "WHtR"
    version <- 2
    (file <- paste0(get_config_path(), "/attach/dex_CMI~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        create_dex_CMI(version)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    d <- d[, c("Year", do::Replace0(var2, ":.*")), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_CONUT` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(Year = T, years = years, albumin_g.dl = T, fast_total_cholesterol_mg.dl = T) %>% 
        db_cbc(lymphocyte_number_1000cells.ul = T)
    d$lymphocyte <- d$lymphocyte_number_1000cells.ul * 1000
    range(d$albumin_g.dl, na.rm = T)
    range(d$lymphocyte_number_1000cells.ul, na.rm = T)
    range(d$fast_total_cholesterol_mg.dl, na.rm = T)
    d <- d %>% mutate(alb.score = case_when(albumin_g.dl < 2.5 ~ 6, albumin_g.dl < 3 ~ 4, albumin_g.dl < 
        3.5 ~ 2, albumin_g.dl >= 3.5 ~ 0), lym.score = case_when(lymphocyte < 800 ~ 3, lymphocyte < 1200 ~ 
        2, lymphocyte < 1600 ~ 1, lymphocyte >= 1600 ~ 0), chol.score = case_when(fast_total_cholesterol_mg.dl < 
        100 ~ 3, fast_total_cholesterol_mg.dl < 140 ~ 2, fast_total_cholesterol_mg.dl < 180 ~ 1, fast_total_cholesterol_mg.dl >= 
        180 ~ 0), CONUT = alb.score + lym.score + chol.score, CONUT.level = case_when(CONUT >= 9 ~ "severe", 
        CONUT >= 5 ~ "moderate", CONUT >= 2 ~ "light", CONUT >= 0 ~ "normal"))
    d$CONUT.count <- 3 - do::NA.row.sums(d[, c("albumin_g.dl", "lymphocyte_number_1000cells.ul", "fast_total_cholesterol_mg.dl")])
    d <- d[, c("Year", "seqn", "CONUT", "CONUT.level", "CONUT.count")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_DASH.Mellen` [exported]

```r
function (data, years, day = 1, both2days = T, component = F, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_drtot(years = years, energy_kcal = "kcal", total_sfat_g = "sfat_g", total_fat_g = "tfat_g", 
        protein_g = T, cholesterol_mg = T, dietary_fiber_g = "fiber_g", magnesium_mg = T, calcium_mg = T, 
        potassium_mg = T, sodium_mg = T, Year = T, day = day, fun = "mean", both2days = both2days)
    d$sfat_g_per <- d$sfat_g * 9/d$kcal * 100
    d$tfat_g_per <- d$tfat_g * 9/d$kcal * 100
    d$protein_g_per <- d$protein_g * 4/d$kcal * 100
    d$cholesterol_mg1000 <- d$cholesterol_mg/d$kcal * 1000
    d$fiber_g <- d$fiber_g/d$kcal * 1000
    d$magnesium_mg1000 <- d$magnesium_mg/d$kcal * 1000
    d$calcium_mg1000 <- d$calcium_mg/d$kcal * 1000
    d$potassium_mg1000 <- d$potassium_mg/d$kcal * 1000
    d$sodium_mg1000 <- d$sodium_mg/d$kcal * 1000
    d$sfat_score <- ifelse(d$sfat_g_per <= 6, 1, ifelse(d$sfat_g_per <= 11, 0.5, 0))
    d$tfat_score <- ifelse(d$tfat_g_per <= 27, 1, ifelse(d$tfat_g_per <= 32, 0.5, 0))
    d$protein_score <- ifelse(d$protein_g_per >= 18, 1, ifelse(d$protein_g_per >= 16.5, 0.5, 0))
    d$cholesterol_score <- ifelse(d$cholesterol_mg1000 <= 71.400000000000006, 1, ifelse(d$cholesterol_mg1000 <= 
        107.09999999999999, 0.5, 0))
    d$fiber_score <- ifelse(d$fiber_g >= 14.800000000000001, 1, ifelse(d$fiber_g >= 9.5, 0.5, 0))
    d$magnesium_score <- ifelse(d$magnesium_mg1000 >= 238, 1, ifelse(d$magnesium_mg1000 >= 158, 0.5, 
        0))
    d$calcium_score <- ifelse(d$calcium_mg1000 >= 590, 1, ifelse(d$calcium_mg1000 >= 402, 0.5, 0))
    d$potassium_score <- ifelse(d$potassium_mg1000 >= 2238, 1, ifelse(d$potassium_mg1000 >= 1534, 0.5, 
        0))
    d$sodium_score <- ifelse(d$sodium_mg1000 <= 1143, 1, ifelse(d$sodium_mg1000 <= 1286, 0.5, 0))
    d$DASH.Mellen <- rowSums(d[, grepl("_score", colnames(d))])
    var2 <- c("seqn", "Year", "DASH.Mellen")
    if (component) 
        var2 <- c(var2, "kcal", "protein_g", "fiber_g", "tfat_g", "sfat_g", "cholesterol_mg", "calcium_mg", 
            "magnesium_mg", "sodium_mg", "potassium_mg")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_DII` [exported]

```r
function (data, years, day = 1, rawComponet = FALSE, both2days = F, cat = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    pb <- txtProgressBar(max = 4, width = 30, style = 3)
    setTxtProgressBar(pb = pb, value = 1)
    dt <- db_drtot(carbohydrate_g = "carbohydrates", protein_g = "protein", total_fat_g = "tfat", alcohol_g = "alcohol", 
        dietary_fiber_g = "fibre", cholesterol_mg = "cholesterol", total_sfat_g = "saturated_fat", total_mfat_g = "MUFA", 
        total_pfat_g = "PUFA", pfa_20.5_g = "n3_1", pfa_22.5_g = "n3_2", pfa_22.6_g = "n3_3", pfa_18.2_g = "n6_1", 
        pfa_18.3_g = "n6_2", pfa_18.4_g = "n6_3", pfa_20.4_g = "n6_4", niacin_mg = "niacin", vitamin_A_rae_mcg = "vitamin_A", 
        thiamin_vitamin_B1_mg = "thiamin", riboflavin_vitamin_B2_mg = "riboflavin", vitamin_B6_mg = "vb6", 
        vitamin_B12_mcg = "vb12", vitamin_C_mg = "vitamin_C", vitamin_D_d2_d3_mcg = "vitamin_D", vitamin_E_as_alpha_tocopherol_mg = "vitamin_E", 
        iron_mg = "Fe", magnesium_mg = "Mg", zinc_mg = "zinc", selenium_mcg = "selenium", folic_acid_mcg = "folic_acid", 
        beta_carotene_mcg = "b_carotene", caffeine_mg = "caffeine", energy_kcal = "energy", years = years, 
        Year = T, day = day, fun = "mean", both2days = both2days)
    if (!missing(data)) 
        dt <- dt[dt$seqn %in% data$seqn, ]
    setTxtProgressBar(pb = pb, value = 2)
    dt <- dt[, !sapply(dt, function(i) all(is.na(i))), drop = FALSE]
    dtnames <- colnames(dt)
    if ("caffeine" %in% colnames(dt)) 
        dt$caffeine <- dt$caffeine/1000
    setTxtProgressBar(pb = pb, value = 3)
    ck <- do::left(colnames(dt), 3) == "n3_"
    colnames(dt)[ck]
    if (any(ck)) {
        n3 <- row.sums(dt[, ck, drop = FALSE])
        dt <- dt[, !ck]
        dt$"n-3_fatty_acids" <- n3
    }
    ck <- do::left(colnames(dt), 3) == "n6_"
    if (any(ck)) {
        n6 <- row.sums(dt[, ck, drop = FALSE])
        dt <- dt[, !ck]
        dt$"n-6_fatty_acids" <- n6
    }
    for (i in 3:ncol(dt)) dt[, i] <- dii(colnames(dt)[i], dt[, i])
    dii <- row.sums(dt[, -c(1:2)])
    dt$dii <- dii
    setTxtProgressBar(pb = pb, value = 4)
    if (cat) 
        cat(crayon::red("\n\ndietary inflammatory index components\n\n"))
    i = 0
    food <- c()
    if ("carbohydrates" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(crayon::red(i, ":"), do::equal_length("carbohydrates", nchar = 22)))
    }
    if ("protein" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("protein", 
            nchar = 22)))
    }
    if ("tfat" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("total fat", 
            nchar = 22)))
    }
    if ("alcohol" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("alcohol", 
            nchar = 22)))
    }
    if ("fibre" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("fibre", 
            nchar = 22)))
    }
    if ("cholesterol" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("cholesterol", 
            nchar = 22)))
    }
    if ("saturated_fat" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("saturated fat", 
            nchar = 22)))
    }
    if ("MUFA" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("MUFA", 
            nchar = 22)))
    }
    if ("PUFA" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("PUFA", 
            nchar = 22)))
    }
    if ("n-3_fatty_acids" %in% colnames(dt)) {
        i = i + 1
        food <- paste0(food, paste0("\n", crayon::red(i, ":"), "n-3 fatty acids\n"))
    }
    if ("n3_1" %in% dtnames) 
        food <- paste0(food, "            eicosapentaenoic(20:5),\n")
    if ("n3_2" %in% dtnames) 
        food <- paste0(food, "            docosapentaenoic(22:5),\n")
    if ("n3_3" %in% dtnames) 
        food <- paste0(food, "            docosahexaenoic(22:6)\n")
    if ("n-6_fatty_acids" %in% colnames(dt)) {
        i = i + 1
        food <- paste0(food, paste0("\n", crayon::red(i, ":"), "n-6 fatty acids"))
    }
    if ("n6_1" %in% dtnames) 
        food <- paste0(food, "\n            octadecadienoic(18:2)")
    if ("n6_2" %in% dtnames) 
        food <- paste0(food, "            octadecatrienoic(18:3),\n")
    if ("n6_3" %in% dtnames) 
        food <- paste0(food, "            octadecatetraenoic(18:4),\n")
    if ("n6_4" %in% dtnames) 
        food <- paste0(food, "            eicosatetraenoic(20:4),\n")
    if ("niacin" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("niacin", 
            nchar = 22)))
    }
    if ("vitamin_A" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin A", 
            nchar = 22)))
    }
    if ("thiamin" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("thiamin(vitamin B1)", 
            nchar = 22)))
    }
    if ("riboflavin" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("riboflavin(vitamin B2)", 
            nchar = 22)))
    }
    if ("vb6" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin B6", 
            nchar = 22)))
    }
    if ("vb12" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin B12", 
            nchar = 22)))
    }
    if ("vitamin_C" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin C", 
            nchar = 22)))
    }
    if ("vitamin_D" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin D", 
            nchar = 22)))
    }
    if ("vitamin_E" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("vitamin E", 
            nchar = 22)))
    }
    if ("Fe" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("Fe", 
            nchar = 22)))
    }
    if ("Mg" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("Mg", 
            nchar = 22)))
    }
    if ("zinc" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("zinc", 
            nchar = 22)))
    }
    if ("selenium" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("selenium", 
            nchar = 22)))
    }
    if ("folic_acid" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("folic acid", 
            nchar = 22)))
    }
    if ("b_carotene" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("beta-carotene", 
            nchar = 22)))
    }
    if ("caffeine" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("caffeine", 
            nchar = 22)))
    }
    if ("energy" %in% dtnames) {
        i = i + 1
        food <- paste0(food, paste0(ifelse(i%%3 == 0, "\n", "      "), crayon::red(i, ":"), do::equal_length("energy", 
            nchar = 22)))
    }
    if (cat) 
        cat(food)
    if (!rawComponet) 
        dt <- dt[, c("Year", "seqn", "dii")]
    return_data(data, dt, Year, key = "seqn", join = join)
}
```

## `dex_DI_GM` [exported]

```r
function (data, years, day = 1, score = F, component = F, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::and(prepare_years(c(2007:2019)), years)
    suppressPackageStartupMessages(library(dplyr, quietly = T, warn.conflicts = F))
    suppressPackageStartupMessages(library(openxlsx, quietly = T, warn.conflicts = F))
    fdcd <- paste0(get_config_path(), "/attach/DI_GM_foodcode.xlsx")
    fn <- getSheetNames(fdcd)
    iff <- db_driff(grams = T, years = years, day = day, fun = "mean", both2days = F)
    iff <- iff[, c("seqn", "food.code", "grams")]
    for (i in 1:length(fn)) {
        fdcd_i <- read.xlsx(fdcd, i)$foodcode
        ck <- iff$food.code %in% fdcd_i
        iff[, fn[i]] <- iff$grams
        iff[!ck, fn[i]] <- 0
    }
    iff[is.na(iff)] <- 0
    food <- aggregate_sum(iff, x = fn, by = "seqn")
    whole_grains = db_fped(g_whole = "whole_grans", g_refined = "refined_grains", dietary = "tot", day = day, 
        years = years)
    fat_fiber <- db_drtot(total_fat_g = "fat", dietary_fiber_g = "fiber", energy_kcal = "energy", years = 2007:2020, 
        Year = T)
    pm <- db_dr.ProcessedMeat(pf_curedmeat = "processed_meat", total_redmeat = "red_meat")
    d <- Inner_Join(food, whole_grains, fat_fiber, pm)
    d <- db_demo(d, ageyr = "age", sex = T)
    d <- d[d$age >= 2, ]
    fn1 <- c("avocado", "broccoli", "chickpea", "coffee", "cranberry", "Fermented_dairy", "fiber", "green_tea", 
        "soybean", "whole_grans")
    fn2 <- c("fat", "refined_grains", "processed_meat", "red_meat")
    d <- d[, c("seqn", "Year", "energy", "sex", fn1, fn2)]
    for (i in set::not(c(fn1, fn2), "fat")) {
        di <- d[d[, i] > 0, c("Year", "sex", i)]
        di <- group_cal(di, median_vars = paste0(i, ":", i, "_median"), bys = c("sex", "Year"))
        d <- left_join(d, di, c("sex", "Year"))
    }
    for (i in fn1) {
        d[, paste0("score_", i)] <- ifelse(d[, i] >= d[, paste0(i, "_median")], 1, 0)
    }
    for (i in set::not(fn2, "fat")) {
        d[, paste0("score_", i)] <- ifelse(d[, i] >= d[, paste0(i, "_median")], 0, 1)
    }
    d <- d[d$energy > 0, ]
    d$score_fat <- ifelse(d$fat * 9/d$energy >= 0.40000000000000002, 0, 1)
    (score_var <- colnames(d)[grepl("score_", colnames(d))])
    d$DI_GM <- rowSums(d[, score_var])
    compo <- c(fn1, fn2)
    d <- d[, c("seqn", "Year", "DI_GM", compo, score_var)]
    var2 <- c("seqn", "Year", "DI_GM")
    if (score) 
        var2 <- c(var2, score_var)
    if (component) 
        var2 <- c(var2, compo)
    d <- d[!is.na(d$Year), var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_FIB.4` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv0(years)
    d <- db_cbc(db_HemalBiochemistry(db_demo(ageyr = "age", years = years, Year = TRUE), Ast = "Ast", 
        Alt = "Alt"), Platelet_count_1000cells.uL = "plt")
    d$FIB.4 <- (d$age * d$Ast)/(d$plt * sqrt(d$Alt))
    d <- d[, c("seqn", "Year", "FIB.4")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_FLI` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_HemalBiochemistry(years = years, Year = TRUE, fast_triglyceride_mg.dl = "tg", 
        gamma_glutamyl_transferase_13u.l_iu.l = "ggt"), waist_circumference_cm = "wc", BMI_kg.m2 = "bmi")
    d$FLI <- with(d, (exp(0.95299999999999996 * log(tg) + 0.13900000000000001 * bmi + 0.71799999999999997 * 
        log(ggt) + 0.052999999999999999 * wc - 15.744999999999999))/(1 + exp(0.95299999999999996 * log(tg) + 
        0.13900000000000001 * bmi + 0.71799999999999997 * log(ggt) + 0.052999999999999999 * wc - 15.744999999999999)) * 
        100)
    d <- d[, c("seqn", "Year", "FLI")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_FS` [exported]

```r
function (data, years, Year = FALSE, join = "left", weight = FALSE) 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(db_cbc(db_demo(years = years, Year = TRUE, ageyr = "age"), Platelet_count_1000cells.uL = "plt"), 
        gamma_glutamyl_transferase_13u.l_iu.l = "ggtp", fast_total_cholesterol_mg.dl = "tc", wtsaf2yr = TRUE, 
        wtsaf4yr = TRUE)
    d$plt <- log(d$plt) * (-3.1309999999999998)
    d$ggtp <- log(d$ggtp) * 0.78100000000000003
    d$age <- log(d$age) * 3.4670000000000001
    d$tc <- d$tc * (-0.014)
    d$FS <- row.sums(d[, c("plt", "ggtp", "age", "tc")], na.rm = FALSE) + 7.8109999999999999
    var <- c("seqn", "Year", "FS")
    if (weight) {
        col_rename(d) <- c("wtsaf2yr:wtsaf2yr", "wtsaf4yr:wtsaf4yr")
        if (all(c("1999-2000", "2001-2002") %in% unique(d$Year))) {
            if (length(unique(d$Year)) == 2) {
                wt.select <- "wtsaf4yr"
            }
            else {
                wt.select <- c("wtsaf2yr", "wtsaf4yr")
            }
        }
        else {
            wt.select <- "wtsaf2yr"
        }
        var <- c(var, wt.select)
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_FSI` [exported]

```r
function (data, years, Year = FALSE, join = "left", weight = FALSE) 
{
    years <- data_years(data, years)
    d <- diag_DM(diag_Hypertension(db_HemalBiochemistry(db_bodyMeasure(db_demo(years = years, ageyr = "age", 
        sex = TRUE, Year = TRUE, psu_strat = FALSE, lower_cd = TRUE), BMI_kg.m2 = "bmi"), fast_triglyceride_mg.dl = "tg", 
        Alt = "alt", Ast = "ast", wtsaf2yr = TRUE, wtsaf4yr = TRUE), cat = F), OGTT2 = FALSE, cat = FALSE)
    head(d)
    d$age <- d$age * 0.010999999999999999
    d$sex <- ifelse(d$sex %in% "female", -0.14599999999999999, 0)
    d$bmi <- 0.17299999999999999 * d$bmi
    d$tg <- 0.0070000000000000001 * d$tg
    d$Hypertension <- ifelse(d$Hypertension == "yes", 0.59299999999999997, 0)
    d$DM <- ifelse(d$DM == "yes", 0.78900000000000003, 0)
    d$alt.ast <- ifelse(d$alt/d$ast >= 1.3300000000000001, 1.1000000000000001, 0)
    d$FSI <- row.sums(d[, c("age", "sex", "bmi", "tg", "Hypertension", "DM", "alt.ast")], na.rm = FALSE) - 
        7.9809999999999999
    var <- c("seqn", "Year", "FSI")
    if (weight) {
        col_rename(d) <- c("wtsaf2yr:wtsaf2yr", "wtsaf4yr:wtsaf4yr")
        if (all(c("1999-2000", "2001-2002") %in% unique(d$Year))) {
            if (length(unique(d$Year)) == 2) {
                wt.select <- "wtsaf4yr"
            }
            else {
                wt.select <- c("wtsaf2yr", "wtsaf4yr")
            }
        }
        else {
            wt.select <- "wtsaf2yr"
        }
        var <- c(var, wt.select)
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_Frailty` [exported]

```r
function (data, years, component = FALSE) 
{
    years <- data_years(data, years)
    (demo <- nhs_tsv("demo", years = years, cat = FALSE))
    (pfq <- nhs_tsv("pfq", years = years, cat = FALSE))
    (dpq <- c(nhs_tsv("ciq", "dep", years = years, cat = FALSE), nhs_tsv("dpq", years = years, cat = FALSE)))
    (mcq <- nhs_tsv("mcq", years = years, cat = FALSE))
    (bpq <- nhs_tsv("bpq", years = years, cat = FALSE))
    (diq <- nhs_tsv("diq", years = years, cat = FALSE))
    (kiq <- nhs_tsv("kiq\\.|kiq_u", years = years, cat = FALSE))
    (bmx <- nhs_tsv("bmx", years = years, cat = FALSE))
    (huq <- nhs_tsv("huq", years = years, cat = FALSE))
    (ghb <- nhs_tsv("lab10\\.|l10_b|l10_c|ghb", years = years, cat = FALSE))
    (rbc <- nhs_tsv("lab25\\.|l25_b|l25_c|cbc", years = years, cat = FALSE))
    (rxq_rx <- nhs_tsv("rxq_rx", years = years, cat = FALSE))
    nr <- nhs_read(demo, "riagendr:sex", pfq, "pfq056,pfq057:Experience_confusion_memory_problems", "pfq060a,pfq061a:money_manage", 
        "pfq060b,pfq061b:walking_for_a_quarter_mile", "pfq060c,pfq061c:walking_up_ten_steps", "pfq060d,pfq061d:stoop_crouch_kneel", 
        "pfq060e,pfq061e:lifting_carry", "pfq060f,pfq061f:house_chore", "pfq060g,pfq061g:preparing_meals", 
        "pfq060i,pfq061i:standingup_from_armless_chair", "pfq060j,pfq061j:getting_in_and_out_of_bed", 
        "pfq060k,pfq061k:using_fork_knife_drinking", "pfq060l,pfq061l:dressing_yourself", "pfq060m,pfq061m:standing_for_long_periods", 
        "pfq060p,pfq061p:grasp_holding_small_objects", "pfq060r,pfq061r:attending_social_event", "pfq060s,pfq061s:leisure_activity_at_home_difficulty", 
        "pfq061t:push_or_pull_large_objects", dpq, "dpq010,ciqd009:little_interest_in_doing_things", 
        "ciqd008", "dpq020,ciqd002:feeling_down_depressed_or_hopeless", "ciqd001", "dpq030,ciqd026:Trouble_sleeping_or_sleeping_too_much", 
        "ciqd025", "dpq040:Feeling_tired_or_having_little_energy", "dpq050,ciqd019:Poor_appetite_or_overeating", 
        "ciqd022", "dpq060,ciqd029:Feeling_bad_about_yourself", "dpq070,ciqd043:Trouble_concentrating_on_things", 
        mcq, "mcq160a:arthritis", "mcq160i,mcd160m,mcq160m:thyroid", "mcq160k,mcq160p:chronic_bronchitis", 
        "mcq220:cancer", "mcq160b:Congestive_heart_failure", "mcq160c:Coronary_heart_disease", "mcq160d:angina", 
        "mcq160e:heart_attack", "mcq160f:stroke", bpq, "bpq020:high_blood_pressure", diq, "diq010:diabetes", 
        kiq, "kiq020,kiq022:weak_kidneys", "kiq040,kiq050:urinary_leakage", huq, "huq010:general_health_condition", 
        "huq020:health_compared_1_year_ago", "huq070,hud070,huq071:overnight_hospital_patient", "huq050,huq051:times_receive_healthcare_over_past_year", 
        bmx, "bmxbmi", ghb, "lbxgh:glycohemoglobin", rbc, "lbxrbcsi:rbc", "lbxhgb:Hemoglobin", "lbxrdw:Red_cell_distribution_width", 
        "lbxlypct:Lymphocyte_percent", "lbxnepct:segmented_neutrophils_percent", lower_cd = TRUE, cat = FALSE, 
        psu_strat = FALSE)
    x <- nhs_read(rxq_rx, "rxd295,rxdcount:prescribed_medications", cat = FALSE, psu_strat = FALSE)[, 
        c("seqn", "prescribed_medications")]
    x <- aggregate(x = x$prescribed_medications, by = list(seqn = x$seqn), sum, na.rm = TRUE)
    colnames(x)[2] <- "prescribed_medications"
    nr <- dplyr::left_join(nr, x, "seqn")
    p1 <- c("Experience_confusion_memory_problems", "money_manage", "walking_for_a_quarter_mile", "walking_up_ten_steps", 
        "stoop_crouch_kneel", "lifting_carry", "house_chore", "preparing_meals", "standingup_from_armless_chair", 
        "getting_in_and_out_of_bed", "using_fork_knife_drinking", "dressing_yourself", "standing_for_long_periods", 
        "grasp_holding_small_objects", "attending_social_event", "leisure_activity_at_home_difficulty", 
        "push_or_pull_large_objects")
    p1d <- nr[, set::and(p1, colnames(nr))]
    p1d[p1d == "no"] <- 0
    p1d[p1d == "yes"] <- 1
    p1d <- do::Replace(p1d, " {2,}", " ")
    p1d[p1d == "do not do this activity"] <- NA
    p1d[p1d == "no difficulty"] <- 0
    p1d[p1d == "some difficulty"] <- 0.33000000000000002
    p1d[p1d == "much difficulty"] <- 0.66000000000000003
    p1d[p1d == "unable to do"] <- 1
    nr[, p1] <- p1d
    p2 <- c("little_interest_in_doing_things", "ciqd008", "feeling_down_depressed_or_hopeless", "ciqd001", 
        "Trouble_sleeping_or_sleeping_too_much", "ciqd025", "Feeling_tired_or_having_little_energy", 
        "Poor_appetite_or_overeating", "ciqd022", "Feeling_bad_about_yourself", "Trouble_concentrating_on_things")
    p2d <- nr[, colnames(nr) %in% p2]
    if ("ciqd008" %in% colnames(p2d)) 
        p2d$little_interest_in_doing_things[p2d$ciqd008 == "no"] <- "0"
    if ("ciqd001" %in% colnames(p2d)) 
        p2d$feeling_down_depressed_or_hopeless[p2d$ciqd001 == "no"] <- "0"
    if ("ciqd025" %in% colnames(p2d)) 
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$ciqd025 == "no"] <- "0"
    if ("ciqd022" %in% colnames(p2d)) 
        p2d$Poor_appetite_or_overeating[p2d$ciqd022 == "no"] <- "0"
    if ("ciqd022" %in% colnames(p2d)) 
        p2d$Poor_appetite_or_overeating[p2d$ciqd022 == "yes"] <- "1"
    p2d[p2d == "no"] <- 0
    p2d[p2d == "not at all"] <- 0
    p2d[p2d == "yes"] <- 1
    if (!is.null(p2d$little_interest_in_doing_things)) {
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "every day"] = "1.00"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "most days"] = "0.75"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "about half the days"] = "0.50"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "less than half the days"] = "0.25"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "nearly every day"] = "1.00"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "more than half the days"] = "0.66"
        p2d$little_interest_in_doing_things[p2d$little_interest_in_doing_things == "several days"] = "0.33"
    }
    if (!is.null(p2d$feeling_down_depressed_or_hopeless)) {
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "every day"] = "1.00"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "most days"] = "0.75"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "about half the days"] = "0.50"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "less than half the days"] = "0.25"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "nearly every day"] = "1.00"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "more than half the days"] = "0.66"
        p2d$feeling_down_depressed_or_hopeless[p2d$feeling_down_depressed_or_hopeless == "several days"] = "0.33"
    }
    if (!is.null(p2d$Trouble_sleeping_or_sleeping_too_much)) {
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "every night"] <- 1
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "nearly every night"] <- 0.66000000000000003
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "less often"] <- 0.33000000000000002
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "nearly every day"] <- 1
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "more than half the days"] <- 0.66000000000000003
        p2d$Trouble_sleeping_or_sleeping_too_much[p2d$Trouble_sleeping_or_sleeping_too_much == "several days"] <- 0.33000000000000002
    }
    if (!is.null(p2d$Feeling_tired_or_having_little_energy)) {
        p2d$Feeling_tired_or_having_little_energy[p2d$Feeling_tired_or_having_little_energy == "nearly every day"] <- 1
        p2d$Feeling_tired_or_having_little_energy[p2d$Feeling_tired_or_having_little_energy == "more than half the days"] <- 0.66000000000000003
        p2d$Feeling_tired_or_having_little_energy[p2d$Feeling_tired_or_having_little_energy == "several days"] <- 0.33000000000000002
    }
    if (!is.null(p2d$Poor_appetite_or_overeating)) {
        p2d$Poor_appetite_or_overeating[p2d$Poor_appetite_or_overeating == "nearly every day"] <- 1
        p2d$Poor_appetite_or_overeating[p2d$Poor_appetite_or_overeating == "more than half the days"] <- 0.66000000000000003
        p2d$Poor_appetite_or_overeating[p2d$Poor_appetite_or_overeating == "several days"] <- 0.33000000000000002
    }
    if (!is.null(p2d$Feeling_bad_about_yourself)) {
        p2d$Feeling_bad_about_yourself[p2d$Feeling_bad_about_yourself == "nearly every day"] <- 1
        p2d$Feeling_bad_about_yourself[p2d$Feeling_bad_about_yourself == "more than half the days"] <- 0.66000000000000003
        p2d$Feeling_bad_about_yourself[p2d$Feeling_bad_about_yourself == "several days"] <- 0.33000000000000002
    }
    if (!is.null(p2d$Trouble_concentrating_on_things)) {
        p2d$Trouble_concentrating_on_things[p2d$Trouble_concentrating_on_things == "nearly every day"] <- 1
        p2d$Trouble_concentrating_on_things[p2d$Trouble_concentrating_on_things == "more than half the days"] <- 0.66000000000000003
        p2d$Trouble_concentrating_on_things[p2d$Trouble_concentrating_on_things == "several days"] <- 0.33000000000000002
    }
    nr[, colnames(nr) %in% p2] <- p2d
    nr <- drop_col(nr, c("ciqd008", "ciqd001", "ciqd025", "ciqd022"))
    p3 <- c("arthritis", "thyroid", "chronic_bronchitis", "cancer", "Congestive_heart_failure", "Coronary_heart_disease", 
        "angina", "heart_attack", "stroke", "high_blood_pressure", "diabetes", "weak_kidneys", "urinary_leakage")
    p3d <- nr[, p3]
    p3d[p3d == "no"] <- 0
    p3d[p3d == "not at all"] <- 0
    p3d[p3d == "borderline"] <- 0.5
    p3d[p3d == "yes"] <- 1
    p3d$urinary_leakage[p3d$urinary_leakage == "greatly"] = "1.00"
    p3d$urinary_leakage[p3d$urinary_leakage == "very much"] = "0.75"
    p3d$urinary_leakage[p3d$urinary_leakage == "somewhat"] = "0.50"
    p3d$urinary_leakage[p3d$urinary_leakage == "only a little"] = "0.25"
    nr[, p3] <- p3d
    p4 <- c("general_health_condition", "health_compared_1_year_ago", "overnight_hospital_patient", "times_receive_healthcare_over_past_year", 
        "prescribed_medications")
    p4d <- nr[, p4]
    p4d$general_health_condition <- ifelse(p4d$general_health_condition %in% c("excellent", "very good", 
        "good"), 0, 1)
    p4d$health_compared_1_year_ago <- ifelse(p4d$health_compared_1_year_ago %in% "worse, or", 1, 0)
    p4d$overnight_hospital_patient <- ifelse(p4d$overnight_hospital_patient == "yes", 1, 0)
    do::increase(do::unique_no.NA(p4d$times_receive_healthcare_over_past_year))
    p4d$times_receive_healthcare_over_past_year[p4d$times_receive_healthcare_over_past_year == "none"] <- 0
    p4d$times_receive_healthcare_over_past_year <- as.numeric(do::Replace0(p4d$times_receive_healthcare_over_past_year, 
        " {0,}[a-z].*"))
    p4d$times_receive_healthcare_over_past_year <- ifelse(p4d$times_receive_healthcare_over_past_year == 
        0, 0, ifelse(p4d$times_receive_healthcare_over_past_year <= 4 & p4d$times_receive_healthcare_over_past_year, 
        0.5, 1))
    p4d$prescribed_medications <- ifelse(p4d$prescribed_medications >= 5, 1, 0.5)
    p4d$prescribed_medications[is.na(p4d$prescribed_medications)] <- 0
    nr[, p4] <- p4d
    nr$bmxbmi <- ifelse(nr$bmxbmi < 18.5 & nr$bmxbmi >= 30, 1, ifelse(nr$bmxbmi >= 25 & nr$bmxbmi < 30, 
        0.5, 0))
    nr$glycohemoglobin <- ifelse(nr$glycohemoglobin > 5.7000000000000002, 1, 0)
    ck0 <- (nr$sex == "male" & nr$rbc >= 4.7000000000000002 & nr$rbc < 6.0999999999999996) | (nr$sex == 
        "female" & nr$rbc >= 4.2000000000000002 & nr$rbc < 5.4000000000000004)
    nr$rbc <- ifelse(ck0, 0, 1)
    ck0 <- (nr$sex == "male" & nr$Hemoglobin >= 13.5 & nr$Hemoglobin < 18) | (nr$sex == "female" & nr$Hemoglobin >= 
        12 & nr$Hemoglobin < 16)
    nr$Hemoglobin <- ifelse(ck0, 0, 1)
    nr$Red_cell_distribution_width <- ifelse(nr$Red_cell_distribution_width >= 11.6 & nr$Red_cell_distribution_width < 
        14.6, 0, 1)
    nr$Lymphocyte_percent <- ifelse(nr$Lymphocyte_percent >= 20 & nr$Lymphocyte_percent < 40, 0, 1)
    nr$segmented_neutrophils_percent <- ifelse(nr$segmented_neutrophils_percent >= 40 & nr$segmented_neutrophils_percent < 
        80, 0, 1)
    nr <- drop_col(nr, "sex", "rxddrgid")
    for (i in 3:ncol(nr)) {
        x <- tryCatch(as.numeric(nr[, i]), warning = function(w) "e")
        if (x[!is.na(x)][1] == "e") 
            stop()
        nr[, i] <- x
    }
    p7 <- c("Experience_confusion_memory_problems", "money_manage", "walking_for_a_quarter_mile", "walking_up_ten_steps", 
        "stoop_crouch_kneel", "lifting_carry", "house_chore", "preparing_meals", "standingup_from_armless_chair", 
        "getting_in_and_out_of_bed", "using_fork_knife_drinking", "dressing_yourself", "standing_for_long_periods", 
        "grasp_holding_small_objects", "attending_social_event", "leisure_activity_at_home_difficulty", 
        "little_interest_in_doing_things", "feeling_down_depressed_or_hopeless", "Trouble_sleeping_or_sleeping_too_much", 
        "Poor_appetite_or_overeating", "Feeling_bad_about_yourself", "Trouble_concentrating_on_things", 
        "arthritis", "thyroid", "chronic_bronchitis", "cancer", "Congestive_heart_failure", "Coronary_heart_disease", 
        "angina", "heart_attack", "stroke", "high_blood_pressure", "diabetes", "weak_kidneys", "urinary_leakage", 
        "general_health_condition", "health_compared_1_year_ago", "overnight_hospital_patient", "times_receive_healthcare_over_past_year", 
        "prescribed_medications", "bmxbmi", "glycohemoglobin", "rbc", "Hemoglobin", "Red_cell_distribution_width", 
        "Lymphocyte_percent", "segmented_neutrophils_percent", "push_or_pull_large_objects", "Feeling_tired_or_having_little_energy")
    p7d <- nr[, set::and(colnames(nr), p7)]
    nr$frailty_number <- row.sums(!is.na(p7d))
    nr$frailty_score <- row.sums(p7d)/nr$frailty_number
    if (!component) 
        nr <- drop_col(nr, p7)
    if (missing(data)) {
        data <- nr
    }
    else {
        data0 <- nr[, !colnames(nr) %in% "Year"]
        data <- dplyr::left_join(data, data0, "seqn")
    }
    return(data)
}
```

## `dex_GNRI` [exported]

```r
function (data, years, cut, method = c("22", "105", "wlo")) 
{
    method <- as.character(method)
    method <- match.arg(method)
    years <- data_years(data, years)
    (demo <- nhs_tsv("demo", items = "demo", years = years, cat = FALSE))
    (bm <- nhs_tsv("bmx", items = "exam", years = years, cat = FALSE))
    (biopro <- nhs_tsv("lab18\\.|l40_b\\.|l40_c\\.|biopro", items = "lab", years = years, cat = FALSE))
    data0 <- nhs_read(demo, "riagendr:sex", bm, "bmxwt:weight", "bmxht:height", biopro, "lbxsal:alb", 
        lower_cd = TRUE, cat = FALSE)
    IBW <- rep(NA, length(data0$sex))
    if (method == "105") {
        IBW <- data0$height - 105
    }
    else if (method == "22") {
        ck <- data0$sex == "male"
        IBW[ck] <- ((data0$height[ck]/100)^2) * 22
        IBW[!ck] <- ((data0$height[!ck]/100 - 0.10000000000000001)^2) * 22
    }
    else if (method == "wlo") {
        ck <- data0$sex == "male"
        IBW[ck] <- data0$height[ck] - 100 - (data0$height[ck] - 150)/4
        IBW[!ck] <- data0$height[!ck] - 100 - (data0$height[!ck] - 150)/2.5
    }
    data0$GNRI_1 <- 1.4890000000000001 * data0$alb * 10
    data0$GNRI_2 <- 41.700000000000003 * data0$weight/IBW
    data0$GNRI <- row.sums(data0[, c("GNRI_1", "GNRI_2")])
    data0 <- data0[, c("Year", "seqn", "GNRI_1", "GNRI_2", "GNRI")]
    if (!missing(cut)) {
        (cut <- do::increase(cut))
        min <- min(data0$GNRI, na.rm = TRUE)
        max <- max(data0$GNRI, na.rm = TRUE)
        if (any(min(cut) < min, max(cut) > max)) {
            if (do::cnOS()) 
                stop(paste0(tmcn::toUTF8("cut<U+5FC5><U+987B><U+5728>"), floor(min), "~", ceiling(max), 
                  tmcn::toUTF8("<U+4E4B><U+95F4>")))
            if (!do::cnOS()) 
                stop(paste0("cut must between ", floor(min), " ~ ", ceiling(max)))
        }
        for (i in 1:length(cut)) {
            if (i == 1) {
                cuti <- list(c(floor(min(data0$GNRI, na.rm = TRUE)), cut[i]))
            }
            else {
                cuti <- c(cuti, list(c(cut[i - 1], cut[i])))
            }
            if (i == length(cut)) 
                cuti <- c(cuti, list(c(cut[i], ceiling(max(data0$GNRI, na.rm = TRUE)))))
        }
        cuti
        data0$GNRI_class <- NA
        group <- c()
        for (i in 1:length(cuti)) {
            if (i < length(cuti)) {
                ck3 <- data0$GNRI >= cuti[[i]][1] & data0$GNRI < cuti[[i]][2]
                group <- c(group, sprintf("[%s,%s)", cuti[[i]][1], cuti[[i]][2]))
                data0$GNRI_class[ck3] <- sprintf("[%s,%s)", cuti[[i]][1], cuti[[i]][2])
            }
            else if (i == length(cuti)) {
                ck1 <- data0$GNRI_1 >= cuti[[i]][1]
                ck2 <- data0$GNRI_2 >= cuti[[i]][1]
                ck3 <- data0$GNRI >= cuti[[i]][1]
                group <- c(group, sprintf("[%s,%s]", cuti[[i]][1], cuti[[i]][2]))
                data0$GNRI_class[ck1 | ck2 | ck3] <- sprintf("[%s,%s]", cuti[[i]][1], cuti[[i]][2])
            }
        }
        data0$GNRI_class <- factor(data0$GNRI_class, group)
    }
    if (missing(data)) {
        data <- data0
    }
    else {
        data0 <- data0[, !colnames(data0) %in% "Year"]
        data <- dplyr::left_join(data, data0, "seqn")
    }
    return(data)
}
```

## `dex_GPS` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(albumin_g.L = "alb", C_reactive_protein_mg.dl = "crp", years = 1999:2010)
    d$crp <- d$crp * 10
    d$GPS[d$crp <= 10 & d$alb >= 35] <- 0
    d$GPS[d$crp > 10 | d$alb < 35] <- 1
    d$GPS[d$crp > 10 & d$alb < 35] <- 2
    d$mGPS[d$crp <= 10] <- 0
    d$mGPS[d$crp > 10 & d$alb >= 35] <- 1
    d$mGPS[d$crp > 10 & d$alb < 35] <- 2
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_HEI` [exported]

```r
function (data, years, version = c("2015", "2010"), method = c("ssum", "pratio"), dietary = c("tot", 
    "iff"), day = 1, both2days = F, varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, 
    seed = NULL) 
{
    version <- as.character(version)
    version <- match.arg(version)
    dietary <- match.arg(dietary)
    method <- match.arg(method)
    if (!all(day %in% c(1, 2))) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("day<U+5FC5><U+987B><U+662F>1<U+6216><U+8005>2"))
        if (!do::cnOS()) 
            stop("day must be 1 or 2")
    }
    if (!missing(data)) {
        seqn <- unique(data$seqn)
    }
    else {
        seqn <- NULL
    }
    years <- data_years(data, years)
    if (version == 2015 & method == "ssum") {
        if (all(c(1, 2) %in% day)) {
            hei <- hei_2015_PerPerson_ssum(both2days = both2days, years = years, dietary = dietary, varLabel = varLabel, 
                energy = energy, component = component, density = density)
        }
        else {
            hei <- hei_2015_PerDay_ssum(years = years, day = day, dietary = dietary, varLabel = varLabel, 
                energy = energy, component = component, density = density)
        }
    }
    if (version == 2010 & method == "ssum") {
        if (all(c(1, 2) %in% day)) {
            hei <- hei_2010_PerPerson_ssum(both2days = both2days, years = years, dietary = dietary, varLabel = varLabel, 
                energy = energy, component = component, density = density)
        }
        else {
            hei <- hei_2010_PerDay_ssum(years = years, day = day, dietary = dietary, varLabel = varLabel, 
                energy = energy, component = component, density = density)
        }
    }
    if (version == 2015 & method == "pratio") {
        if (all(c(1, 2) %in% day)) {
            hei <- hei_2015_PerPerson_pratio(seqn = seqn, years = years, dietary = dietary, seed = seed)
        }
        else {
            hei <- hei_2015_PerDay_pratio(seqn = seqn, years = years, day = day, dietary = dietary, seed = seed)
        }
        return(hei)
    }
    if (version == 2010 & method == "pratio") {
        if (all(c(1, 2) %in% day)) {
            hei <- hei_2010_PerPerson_pratio(seqn = seqn, years = years, dietary = dietary, seed = seed)
        }
        else {
            hei <- hei_2010_PerDay_pratio(seqn = seqn, years = years, day = day, dietary = dietary, seed = seed)
        }
        return(hei)
    }
    if (!missing(data)) {
        if (dietary == "iff") 
            join <- c("seqn", "line")
        else join <- "seqn"
        colnames(data) <- rename_line(colnames(data))
        join <- set::and(join, colnames(data), colnames(hei))
        data <- dplyr::left_join(data, hei, join)
        return(data)
    }
    return(hei)
}
```

## `dex_HOMA` [exported]

```r
function (data, years, IR = TRUE, IS = TRUE, beta = TRUE, fglu = FALSE, finsulin = FALSE, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data = data, years = years)
    (gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu", items = "Laboratory", years = years, cat = FALSE))
    (ins <- nhs_tsv("ins", items = "Laboratory", years = years, cat = FALSE))
    nr <- nhs_read(gluam, "lbxglusi,lbdglusi:fglu", "lbxin:finsulin", ins, "lbxin:finsulin", cat = FALSE)
    nr$HOMA_IR <- nr$fglu * nr$finsulin/22.5
    nr$HOMA_IS <- 22.5/(nr$fglu * nr$finsulin)
    nr$HOMA_beta <- 20 * nr$finsulin/(nr$fglu - 3.5)
    colnames <- c("seqn", "Year")
    if (fglu) 
        colnames <- c(colnames, "fglu")
    if (finsulin) 
        colnames <- c(colnames, "finsulin")
    if (IR) 
        colnames <- c(colnames, "HOMA_IR")
    if (IS) 
        colnames <- c(colnames, "HOMA_IS")
    if (beta) 
        colnames <- c(colnames, "HOMA_beta")
    d <- nr[, colnames]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_HSI` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- diag_DM(db_demo(db_bodyMeasure(db_HemalBiochemistry(years = years, Alt = TRUE, Ast = TRUE, Year = TRUE), 
        BMI_kg.m2 = "BMI"), sex = TRUE), cat = FALSE, told = T, drug = T, HbA1c = F, fast_glu = F, OGTT2 = F, 
        rand_glu = F)
    d$sex <- tolower(d$sex)
    d$sex <- ifelse(d$sex == "female", 2, 0)
    d$DM <- ifelse(d$DM %in% c("DM", "GDM"), 2, 0)
    d$ratio <- d$Alt/d$Ast * 8
    d$HSI <- row.sums(d[, c("ratio", "BMI", "sex", "DM")])
    d <- d[, c("Year", "seqn", "HSI")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_HeartAge` [exported]

```r
function (data, years, CVD.10yr.risk = FALSE, component = FALSE, points_var = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d1 <- diag_DM(diag_smoke(db_blood.pressure(db_HemalBiochemistry(db_demo(ageyr = "age", sex = T, lower_cd = T, 
        years = years, Year = T, psu_strat = F), hdl_cholesterol_mg.dl = "hdl", fast_total_cholesterol_mg.dl = "tc"), 
        bpx = F, dar = T)), cat = F)
    tsv <- nhs_tsv("bpq", years = years, cat = F)
    d2 <- nhs_read(tsv, "bpq040a:treatBP", cat = F, Year = F, lower_cd = T)
    d <- Full_Join(d1, d2, cat = F)
    d$sbp_no_treat <- d$bpxsar
    d$sbp_no_treat[d$treatBP %in% "yes"] <- NA
    d$sbp_treat[d$treatBP %in% "yes"] <- d$bpxsar[d$treatBP %in% "yes"]
    col_rename(d) <- c("DM:diabetic", "smoke:smoker")
    d$smoker <- Recode(d$smoker, "former::no", "now::yes", "never::no", "NA::")
    d$diabetic <- Recode(d$diabetic, "DM::yes", "no::", "IGT::no", "IFG::no", "NA::")
    (tb <- rbind(cvd.points.women.table(), cvd.points.men.table()))
    tb[, -1] <- do::Replace(do::Replace(do::Replace(tb[, -1], ">=", "x >= "), "<", "x < "), "<U+2013>", 
        " <= x & x <= ")
    for (i in 1:nrow(tb)) {
        (cdt <- tb[i, -1])
        (ck.sex <- d$sex %in% cdt$sex)
        for (k in 2:ncol(cdt)) {
            (ci <- cdt[, k])
            (x <- d[, colnames(cdt)[k]])
            if (ci %in% c("yes", "no")) {
                d <- add_col(d, paste0("points_", colnames(cdt)[k]), tb$points[i], ck.sex & x %in% ci)
            }
            else if (nchar(ci) > 0) {
                d <- add_col(d, paste0("points_", colnames(cdt)[k]), tb$points[i], ck.sex & eval(parse(text = ci)))
            }
        }
    }
    var1 <- c("seqn", "Year", "HeartAge", "CVD.Points", "CVD.Points.count")
    var2 <- c("sex", "age", "hdl", "tc", "sbp_no_treat", "sbp_treat", "smoker", "diabetic")
    (var3 <- set::grep_and(colnames(d), "points_"))
    d$CVD.Points <- row.sums(d[, var3])
    d$CVD.Points.count <- length(var3) - do::NA.row.sums(d[, var3])
    hat <- HeartAge.table()
    d$CVD.Points2 <- d$CVD.Points
    d$CVD.Points2[d$CVD.Points < 1 & d$sex == "female"] <- "<1"
    d$CVD.Points2[d$CVD.Points >= 15 & d$sex == "female"] <- ">=15"
    d$CVD.Points2[d$CVD.Points < 0 & d$sex == "male"] <- "<0"
    d$CVD.Points2[d$CVD.Points >= 17 & d$sex == "male"] <- ">=17"
    for (i in c("male", "female")) {
        (hati <- hat[hat$sex %in% i, ])
        for (j in 1:nrow(hati)) {
            ck <- d$sex %in% i & d$CVD.Points2 %in% hati$points[j]
            d$HeartAge[ck] <- hati$HeartAge[j]
        }
    }
    ck <- d$sex == "female"
    d$age2[ck] <- log(d$age[ck]) * 2.3288799999999998
    d$tc2[ck] <- log(d$tc[ck]) * 1.2090399999999999
    d$hdl2[ck] <- log(d$hdl[ck]) * (-0.70833000000000002)
    d$bpxsar2[ck & d$treatBP %in% "no"] <- log(d$bpxsar[ck & d$treatBP %in% "no"]) * 2.7615699999999999
    d$bpxsar2[ck & d$treatBP %in% "yes"] <- log(d$bpxsar[ck & d$treatBP %in% "yes"]) * 2.8226300000000002
    d$smoke2[ck] <- ifelse(d$smoker[ck] == "yes", 1, 0) * 0.52873000000000003
    d$diabetic2[ck] <- ifelse(d$diabetic[ck] == "yes", 1, 0) * 0.69154000000000004
    d$bxb[ck] <- 26.193100000000001
    d$root[ck] <- 0.95011999999999996
    ck <- d$sex == "male"
    d$age2[ck] <- log(d$age[ck]) * 3.0611700000000002
    d$tc2[ck] <- log(d$tc[ck]) * 1.1236999999999999
    d$hdl2[ck] <- log(d$hdl[ck]) * (-0.93262999999999996)
    d$bpxsar2[ck & d$treatBP %in% "no"] <- log(d$bpxsar[ck & d$treatBP %in% "no"]) * 1.93303
    d$bpxsar2[ck & d$treatBP %in% "yes"] <- log(d$bpxsar[ck & d$treatBP %in% "yes"]) * 1.99881
    d$smoke2[ck] <- ifelse(d$smoker[ck] == "yes", 1, 0) * 0.65451000000000004
    d$diabetic2[ck] <- ifelse(d$diabetic[ck] == "yes", 1, 0) * 0.57367000000000001
    d$bxb[ck] <- 23.9802
    d$root[ck] <- 0.88936000000000004
    diff <- d$age2 + d$tc2 + d$hdl2 + d$bpxsar2 + d$smoke2 + d$diabetic2 - d$bxb
    d$CVD.10yr.risk <- 1 - d$root^exp(diff)
    if (CVD.10yr.risk) 
        var1 <- c(var1, "CVD.10yr.risk")
    if (component) 
        var1 <- c(var1, var2)
    if (points_var) 
        var1 <- c(var1, var3)
    d <- d[, var1]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_LAP` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(db_bodyMeasure(db_demo(years = years, sex = "sex", Year = TRUE, lower_cd = TRUE, 
        ageyr = "age", psu_strat = FALSE), waist_circumference_cm = "wc"), fast_triglyceride_mmol.L = "tg")
    d <- d[d$age >= 18, ]
    d <- drop_row(drop_row(drop_row(drop_row(d, is.na(wc)), is.na(tg)), sex == "male" & wc < 65), sex == 
        "female" & wc < 58)
    d$LAP <- (d$wc - ifelse(d$sex == "male", 65, 58)) * d$tg
    d <- d[, c("seqn", "Year", "LAP")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_LC9` [exported]

```r
function (data, years, day = 1, componet = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d1 <- dex_LE8(Year = F, componet = T, day = day)
    d2 <- diag_PHQ9(score = T, cat = F)
    d <- Inner_Join(d1, d2, cat = F)
    d <- d[!is.na(d$PHQ9), ]
    d$score_PHQ9 <- d$score
    d[, c("score", "PHQ9", "answer")] <- NULL
    d <- d %>% newVb("score_PHQ9", score_PHQ9 >= 0 & score_PHQ9 <= 4 ~ 100, score_PHQ9 >= 5 & score_PHQ9 <= 
        9 ~ 75, score_PHQ9 >= 10 & score_PHQ9 <= 14 ~ 50, score_PHQ9 >= 15 & score_PHQ9 <= 19 ~ 25, score_PHQ9 >= 
        20 & score_PHQ9 <= 27 ~ 0)
    component <- c("score_hei", "score_pa", "score_smoke", "score_sleep", "score_bmi", "score_non.hdl", 
        "score_glucose", "score_bp", "score_PHQ9")
    d$LC9 <- row.sums(d[, component])/9
    d$LC9_count <- 9 - do::NA.row.sums(d[, component])
    d <- d[, c("seqn", "Year", "LC9", "LC9_count", "score_hei", "score_pa", "score_smoke", "score_sleep", 
        "score_bmi", "score_non.hdl", "score_glucose", "score_bp", "score_PHQ9")]
    d <- d[d$Year %in% years, ]
    var2 <- c("seqn", "Year", "LC9", "LC9_count")
    if (componet) 
        var2 <- c(var2, "score_hei", "score_pa", "score_smoke", "score_sleep", "score_bmi", "score_non.hdl", 
            "score_glucose", "score_bp", "score_PHQ9")
    d <- d[, var2]
    row.names(d) <- NULL
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_LE8` [exported]

```r
function (data, years, day = 1, componet = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    version <- 2
    (file <- paste0(get_config_path(), "/attach/dex_LE8~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        download.file(sprintf("http://146.56.250.62:3838/data/nhanes-attach/dex_LE8~~version-%s.txt", 
            version), file)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    if (length(day) == 1) {
        heiq <- quantile(d$hei.day1, c(0.94999999999999996, 0.75, 0.5, 0.25))
        d$score_hei <- ifelse(d$hei.day1 >= heiq["95%"], 100, ifelse(d$hei.day1 >= heiq["75%"], 80, ifelse(d$hei.day1 >= 
            heiq["50%"], 50, ifelse(d$hei.day1 >= heiq["25%"], 25, 0))))
    }
    else {
        heiq <- quantile(d$hei.day12, c(0.94999999999999996, 0.75, 0.5, 0.25))
        d$score_hei <- ifelse(d$hei.day12 >= heiq["95%"], 100, ifelse(d$hei.day12 >= heiq["75%"], 80, 
            ifelse(d$hei.day12 >= heiq["50%"], 50, ifelse(d$hei.day12 >= heiq["25%"], 25, 0))))
    }
    d$LE8 <- row.means(d[, c("score_hei", "score_pa", "score_smoke", "score_sleep", "score_bmi", "score_non.hdl", 
        "score_glucose", "score_bp")])
    d$LE8.count <- 8 - do::NA.row.sums(d[, c("score_hei", "score_pa", "score_smoke", "score_sleep", "score_bmi", 
        "score_non.hdl", "score_glucose", "score_bp")])
    var2 <- c("seqn", "Year", "LE8", "LE8.count")
    if (componet) 
        var2 <- c(var2, "score_hei", "score_pa", "score_smoke", "score_sleep", "score_bmi", "score_non.hdl", 
            "score_glucose", "score_bp")
    d <- d[, var2]
    row.names(d) <- NULL
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_LS7` [exported]

```r
function (data, years, count = FALSE, component_score = FALSE, component_raw = FALSE, hei_version = 2010, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- LS7_Michelle(years, hei_version, count, component_score, component_raw)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_MAO` [exported]

```r
function (data, years, Year = FALSE, yes1 = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(diag_MetS(methods = "Harm", years = years, Year = TRUE, yes1 = TRUE, cat = FALSE), 
        BMI_kg.m2 = "BMI")
    d$BMI <- ifelse(d$BMI >= 30, 1, 0)
    d$MAO[d$BMI == 1 & d$MetS_Harm == 1] <- 1
    d$MAO[d$BMI == 1 & d$MetS_Harm == 0] <- 0
    if (!yes1) 
        yes1(d) <- "MAO"
    d <- d[, c("seqn", "Year", "MAO")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_METS.IR` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_HemalBiochemistry(fast_glucose_mg.dl = "glu", fast_triglyceride_mg.dl = "tg", 
        hdl_cholesterol_mg.dl = "hdl", years = years, Year = TRUE), BMI_kg.m2 = "BMI")
    d$METS.IR <- (log(2 * d$glu + d$tg) * d$BMI)/log(d$hdl)
    d <- d[, c("seqn", "Year", "METS.IR")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_METS.VF` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(dex_METS.IR(dex_WHtR(years = years, Year = TRUE), join = "inner"), ageyr = "age", sex = "sex", 
        psu_strat = FALSE, lower_cd = TRUE)
    d$sex <- ifelse(d$sex == "male", 1, 0)
    d$METS.VF <- suppressWarnings(4.4660000000000002 + 0.010999999999999999 * (log(d$METS.IR))^3 + 3.2389999999999999 * 
        (log(d$WHtR))^3 + 0.31900000000000001 * d$sex + 0.59399999999999997 * log(d$age))
    d <- d[, c("seqn", "Year", "METS.VF")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_MHO` [exported]

```r
function (data, years, Year = FALSE, yes1 = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- data_years(data, years)
    d <- db_bodyMeasure(diag_MetS(methods = "Harm", years = years, Year = TRUE, yes1 = TRUE, cat = FALSE), 
        BMI_kg.m2 = "BMI")
    d$BMI <- ifelse(d$BMI >= 30, 1, 0)
    d$MHO[d$BMI == 1 & d$MetS_Harm == 0] <- 1
    d$MHO[d$BMI == 1 & d$MetS_Harm == 1] <- 0
    if (!yes1) 
        yes1(d) <- "MHO"
    d <- d[, c("seqn", "Year", "MHO")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_MMII` [exported]

```r
function (data = NULL, years, MMII = T, component = F, Year = F, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(c(), "Year", "Year"), "seqn", "seqn"), 
        MMII, "MMII")
    years <- data_years(data, years)
    tsv <- nhs_tsv("lab06|l06_b|uhg_|_uhg", "!~lab06hm", cat = F)
    d1 <- nhs_read(tsv, "urxuhg:mercury", cat = F)
    tsv <- nhs_tsv("lab06hm|l06hm_|uhm_|um_|_um", cat = F)
    d2 <- nhs_read(tsv, "urducd,urxucd:cadmium", "urxuco:cobalt", "urxumo:molybdenum", "urxupb:lead", 
        "urxutu:tungsten", Year = F, cat = F)
    tsv <- c(nhs_tsv("lab06hm|l06hm_|uhm_|um_|_um", years = 1999:2003, cat = F), tsv <- nhs_tsv("alb_cr", 
        cat = F))
    d3 <- nhs_read(tsv, "urxucr", Year = F, cat = F)
    d <- Left_Join(d1, d2, d3)
    d$mercury[tolower(d$mercury) %in% "fill value of limit of detection"] <- sqrt(0.080000000000000002)
    d$cobalt[tolower(d$cobalt) %in% "fill value of limit of detection"] <- sqrt(0.040000000000000001)
    d$molybdenum[tolower(d$molybdenum) %in% "fill value of limit of detection"] <- sqrt(0.91000000000000003)
    hm <- c("mercury", "cadmium", "cobalt", "molybdenum", "lead", "tungsten", "urxucr")
    for (i in hm) {
        d[, i] <- as.numeric(d[, i])
        d <- d[!is.na(d[, i]), ]
    }
    hm <- c("mercury", "cadmium", "cobalt", "molybdenum", "lead", "tungsten")
    for (i in hm) {
        d <- d[!is.infinite(log(d[, i]/d$urxucr)), ]
        d[, i] <- as.numeric(scale(log(d[, i]/d$urxucr)))
    }
    d$MMII <- d$mercury * -0.070234000000000005 + d$cadmium * 0.25630799999999998 + d$cobalt * -0.048007000000000001 + 
        d$molybdenum * -0.15942500000000001 + d$lead * -0.074817999999999996 + d$tungsten * 0.039472
    d <- d[!is.na(d$MMII), ]
    d <- d[, c("Year", "seqn", "MMII", hm)]
    d <- d[d$Year %in% years, ]
    if (component) 
        var2 <- c(var2, hm)
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_MQI` [exported]

```r
function (data, years, MQI.total = TRUE, MQI.app = FALSE, MQI.arm = FALSE, ASM = FALSE, ASMI = FALSE, 
    Year = FALSE, QC = TRUE, GF.dominant = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(db_muscle.strength(gs_t1_h1.kg = "h1t1", gs_t2_h1.kg = "h1t2", gs_t3_h1.kg = "h1t3", 
        gs_t1_h2.kg = "h2t1", gs_t2_h2.kg = "h2t2", gs_t3_h2.kg = "h2t3", dominant_hand = "dominant", 
        begin_test_hand = "begin.hand", combined_grip_strength_kg = "gs.total", Year = TRUE, years = years), 
        eth3 = "eth", sex = "sex", lower_cd = TRUE)
    d$eth <- Recode(d$eth, "non-hispanic black::", "non-hispanic white::", "mexican american::mexican hispanic", 
        "other race - including multi-racial::others", "non-hispanic asian::", "other hispanic::")
    head(d)
    d$h1 <- row.max(d[, c("h1t1", "h1t2", "h1t3")])
    d$h2 <- row.max(d[, c("h2t1", "h2t2", "h2t3")])
    head(d)
    d <- drop_col(d, c("h1t1", "h1t2", "h1t3", "h2t1", "h2t2", "h2t3"))
    ck <- d$begin.hand %in% "left"
    d$gs.left <- ifelse(ck, d$h1, d$h2)
    d$gs.right <- ifelse(!ck, d$h1, d$h2)
    d <- drop_col(d, c("begin.hand", "h1", "h2"))
    head(d)
    d <- db_dxx(d, left_arm_lean_excl_bmc_g = "asm.left.arm", right_arm_lean_excl_bmc_g = "asm.right.arm", 
        left_leg_lean_excl_bmc_g = "asm.left.leg", right_leg_lean_excl_bmc_g = "asm.right.leg")
    d$asm.left.arm <- d$asm.left.arm/1000
    d$asm.right.arm <- d$asm.right.arm/1000
    d$asm.left.leg <- d$asm.left.leg/1000
    d$asm.right.leg <- d$asm.right.leg/1000
    d$ASM <- row.sums(d[, c("asm.left.arm", "asm.left.leg", "asm.right.arm", "asm.right.leg")])
    head(d)
    ck <- lookl(d$dominant, "left", NA2false = TRUE)
    d$GF.dominant[ck] <- d$gs.left[ck]
    d$MQI.arm[ck] <- d$gs.left[ck]/d$asm.left.arm[ck]
    ck <- lookl(d$dominant, "right", NA2false = TRUE)
    d$GF.dominant[ck] <- d$gs.right[ck]
    d$MQI.arm[ck] <- d$gs.right[ck]/d$asm.right.arm[ck]
    ck <- lookl(d$dominant, "both", NA2false = TRUE)
    df <- data.frame(x1 = d$gs.left[ck]/d$asm.left.arm[ck], x2 = d$gs.right[ck]/d$asm.right.arm[ck])
    d$GF.dominant[ck] <- row.max(df)[ck]
    d$MQI.arm[ck] <- row.max(df)
    head(d)
    ck <- (d$sex %in% "male") & (d$eth %in% "mexican hispanic")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 10, "extremely low", ifelse(d$MQI.arm[ck] < 11.6, "low", 
        "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "other hispanic")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 9.8000000000000007, "extremely low", ifelse(d$MQI.arm[ck] < 
        11.199999999999999, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic white")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 10.199999999999999, "extremely low", ifelse(d$MQI.arm[ck] < 
        11.699999999999999, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic black")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 7.4000000000000004, "extremely low", ifelse(d$MQI.arm[ck] < 
        9.8000000000000007, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic asian")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 8.3000000000000007, "extremely low", ifelse(d$MQI.arm[ck] < 
        10.800000000000001, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "others")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 8.4000000000000004, "extremely low", ifelse(d$MQI.arm[ck] < 
        10.4, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "mexican hispanic")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 10.800000000000001, "extremely low", ifelse(d$MQI.arm[ck] < 
        12.6, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "other hispanic")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 10.1, "extremely low", ifelse(d$MQI.arm[ck] < 12.199999999999999, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic white")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 11.9, "extremely low", ifelse(d$MQI.arm[ck] < 13.199999999999999, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic black")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 8.9000000000000004, "extremely low", ifelse(d$MQI.arm[ck] < 
        11.4, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic asian")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 10.1, "extremely low", ifelse(d$MQI.arm[ck] < 12.699999999999999, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "others")
    d$MQIc.arm[ck] <- ifelse(d$MQI.arm[ck] < 11.300000000000001, "extremely low", ifelse(d$MQI.arm[ck] < 
        12.9, "low", "normal"))
    ck <- lookl(d$dominant, "left", NA2false = TRUE)
    d$MQI.app[ck] <- d$gs.left[ck]/d$ASM[ck]
    ck <- lookl(d$dominant, "right", NA2false = TRUE)
    d$MQI.app[ck] <- d$gs.right[ck]/d$ASM[ck]
    ck <- lookl(d$dominant, "both", NA2false = TRUE)
    df <- data.frame(x1 = d$gs.left[ck]/d$ASM[ck], x2 = d$gs.right[ck]/d$ASM[ck])
    d$MQI.app[ck] <- row.max(df)
    head(d)
    ck <- (d$sex %in% "male") & (d$eth %in% "mexican hispanic")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.5, "extremely low", ifelse(d$MQI.app[ck] < 1.8, "low", 
        "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "other hispanic")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.5, "extremely low", ifelse(d$MQI.app[ck] < 1.7, "low", 
        "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic white")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.5, "extremely low", ifelse(d$MQI.app[ck] < 1.7, "low", 
        "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic black")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.1000000000000001, "extremely low", ifelse(d$MQI.app[ck] < 
        1.3999999999999999, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic asian")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.1000000000000001, "extremely low", ifelse(d$MQI.app[ck] < 
        1.5, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "others")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.1000000000000001, "extremely low", ifelse(d$MQI.app[ck] < 
        1.5, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "mexican hispanic")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.5, "extremely low", ifelse(d$MQI.app[ck] < 1.7, "low", 
        "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "other hispanic")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.3, "extremely low", ifelse(d$MQI.app[ck] < 1.6000000000000001, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic white")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.5, "extremely low", ifelse(d$MQI.app[ck] < 1.7, "low", 
        "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic black")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.2, "extremely low", ifelse(d$MQI.app[ck] < 1.5, "low", 
        "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic asian")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.3, "extremely low", ifelse(d$MQI.app[ck] < 1.6000000000000001, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "others")
    d$MQIc.app[ck] <- ifelse(d$MQI.app[ck] < 1.3999999999999999, "extremely low", ifelse(d$MQI.app[ck] < 
        1.6000000000000001, "low", "normal"))
    d$MQI.total <- d$gs.total/d$ASM
    ck <- (d$sex %in% "male") & (d$eth %in% "mexican hispanic")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 3.1000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.6000000000000001, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "other hispanic")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.8999999999999999, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2999999999999998, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic white")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 3.1000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2999999999999998, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic black")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 3.1000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.5, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "non-hispanic asian")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.1000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        2.7999999999999998, "low", "normal"))
    ck <- (d$sex %in% "male") & (d$eth %in% "others")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.6000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2000000000000002, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "mexican hispanic")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 3, "extremely low", ifelse(d$MQI.total[ck] < 3.3999999999999999, 
        "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "other hispanic")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.6000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2000000000000002, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic white")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 3.1000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.3999999999999999, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic black")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.2999999999999998, "extremely low", ifelse(d$MQI.total[ck] < 
        2.8999999999999999, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "non-hispanic asian")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.6000000000000001, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2000000000000002, "low", "normal"))
    ck <- (d$sex %in% "female") & (d$eth %in% "others")
    d$MQIc.total[ck] <- ifelse(d$MQI.total[ck] < 2.7999999999999998, "extremely low", ifelse(d$MQI.total[ck] < 
        3.2000000000000002, "low", "normal"))
    var2 <- c("Year", "seqn")
    if (QC) {
        append(var2) <- c("grip_test_status", "ever_had_surgery_on_hands_or_wrists", "recent_pain_aching_stiffness_right_hand", 
            "recent_pain_aching_stiffness_left_hand", "dxx_exam_status")
    }
    if (MQI.arm) 
        append(var2) <- c("MQI.arm", "MQIc.arm")
    if (MQI.app) 
        append(var2) <- c("MQI.app", "MQIc.app")
    if (MQI.total) 
        append(var2) <- c("MQI.total", "MQIc.total")
    if (ASM) 
        append(var2) <- "ASM"
    if (ASMI) {
        append(var2) <- "ASMI"
        d <- db_bodyMeasure(d, height_cm = "height")
        d$ASMI <- d$ASM/(d$height/100)/(d$height/100)
    }
    if (GF.dominant) 
        append(var2) <- "GF.dominant"
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_MgDS` [exported]

```r
function (data, years, component = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    data0 <- dex_eGFR(method = "CKD_EPI_Scr_2009", years = years, Year = TRUE)
    data0$CKD_EPI_Scr_2009 <- ifelse(data0$CKD_EPI_Scr_2009 < 60, 2, ifelse(data0$CKD_EPI_Scr_2009 < 
        90, 1, 0))
    data0 <- Drug(data = data0, "diuretic", take_drug = "score_diuretic", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    data0 <- Drug(data = data0, "proton pump inhibitor", take_drug = "score_ppi", dup.take.drug = "remove", 
        yes.code = 1, no.code = 0, other.code = 0)
    demo <- nhs_read(nhs_tsv("demo", years = years, cat = FALSE), "riagendr", cat = FALSE, Year = FALSE, 
        lower_cd = TRUE)
    fped <- fped_read(years = years, day = c(1, 2), cat = F, fun = "mean", dietary = "tot")[, c("seqn", 
        "a_drinks")]
    col_rename(fped) <- "a_drinks:score_drinks"
    data0 <- dplyr::inner_join(data0, fped, "seqn")
    data0 <- dplyr::inner_join(data0, demo, "seqn")
    ck1 <- (data0$riagendr == "female" & data0$score_drinks > 1) | (data0$riagendr == "male" & data0$score_drinks > 
        2)
    data0$score_drinks <- ifelse(ck1, 1, 0)
    colnames(data0)[colnames(data0) == "CKD_EPI_Scr_2009"] <- "score_eGFR"
    data0 <- data0[, c("seqn", "Year", "score_eGFR", "score_diuretic", "score_ppi", "score_drinks")]
    data0$MgDS <- row.sums(data0[, c("score_eGFR", "score_diuretic", "score_ppi", "score_drinks")])
    var2 <- c("seqn", "Year", "MgDS")
    if (component) 
        var2 <- c(var2, "score_eGFR", "score_diuretic", "score_ppi", "score_drinks")
    d <- data0[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_Muscle.strength` [exported]

```r
function (data, years, activity = FALSE, times = FALSE, MET = FALSE, week = TRUE, Year = FALSE, join = "left") 
{
    if (isFALSE(activity) & isFALSE(times) & isFALSE(MET)) {
        if (!missing(data)) 
            return(data)
        return()
    }
    years <- data_years(data, years)
    paq <- nhs_tsv("paq", "!~ia|paqy", years = years, cat = FALSE)
    d <- nhs_read(paq, "pad440:Muscle.strength", "pad460:times_Muscle.strength", lower_cd = TRUE, cat = FALSE)
    ck00 <- tsv0(d, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    if (week) {
        ck <- d$times_Muscle.strength < 30 & !is.na(d$times_Muscle.strength)
        d$times_Muscle.strength[ck] <- d$times_Muscle.strength[ck]/30 * 7
        d$times_Muscle.strength[d$times_Muscle.strength >= 30] <- 7
    }
    d$MET_Muscle.strength <- d$times_Muscle.strength * 4
    var <- c("seqn", "Year")
    if (activity) 
        var <- c(var, "Muscle.strength")
    if (times) 
        var - c(var, "times_Muscle.strength")
    if (MET) 
        var <- c(var, "MET_Muscle.strength")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_NAFLD.LFS` [exported]

```r
function (data, years, Year = FALSE, Mets = c("IDF2006", "ATP", "IDF2009", "Harm"), join = "left", cat = TRUE, 
    component = FALSE) 
{
    years <- data_years(data, years)
    Mets <- match.arg(Mets)
    d <- db_HemalBiochemistry(diag_DM(diag_MetS(methods = Mets, yes1 = TRUE, years = years, Year = T, 
        cat = cat), cat = cat, DM1 = TRUE), fast_insulin_uu.ml = "fsInsulin", Ast = "ast", Alt = "alt")
    d$DM <- as.numeric(d$DM)
    colnames(d)[do::left(colnames(d), 5) == "MetS_"] <- "MetS"
    d$MetS[d$MetS == "yes"] <- 1
    d$MetS[d$MetS == "no"] <- 0
    d$MetS <- as.numeric(d$MetS)
    d$NAFLD.LFS <- -2.8900000000000001 + 1.1799999999999999 * d$MetS + 0.45000000000000001 * d$DM * 2 + 
        0.14999999999999999 * d$fsInsulin + 0.040000000000000001 * d$ast - 0.93999999999999995 * d$ast/d$alt
    var2 <- c("Year", "seqn", "NAFLD.LFS")
    if (component) 
        var2 <- c(var2, c("DM", "fsInsulin", "alt", "ast", "MetS"))
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_NFS` [exported]

```r
function (data, years, Year = FALSE, join = "left", weight = FALSE) 
{
    years <- data_years(data, years)
    d <- db_cbc(db_HemalBiochemistry(diag_DM(db_bodyMeasure(db_demo(years = years, Year = TRUE, ageyr = "age"), 
        BMI_kg.m2 = "bmi"), OGTT2 = FALSE, cat = FALSE), Ast = "ast", Alt = "alt", albumin_g.dl = "alb", 
        wtsaf2yr = TRUE, wtsaf4yr = TRUE), Platelet_count_1000cells.uL = "plt")
    d$age <- 0.036999999999999998 * d$age
    d$bmi <- 0.094 * d$bmi
    d$DM <- ifelse(d$DM %=% c("DM", "IFG"), 1.1299999999999999, 0)
    d$ast.alt <- 0.98999999999999999 * (d$ast/d$alt)
    d$plt <- -0.012999999999999999 * d$plt
    d$alb <- -0.66000000000000003 * d$alb
    d$NFS <- row.sums(d[, c("age", "bmi", "DM", "ast.alt", "plt", "alb")], na.rm = FALSE) - 1.675
    var <- c("seqn", "Year", "NFS")
    if (weight) {
        col_rename(d) <- c("wtsaf2yr:wtsaf2yr", "wtsaf4yr:wtsaf4yr")
        if (all(c("1999-2000", "2001-2002") %in% unique(d$Year))) {
            if (length(unique(d$Year)) == 2) {
                wt.select <- "wtsaf4yr"
            }
            else {
                wt.select <- c("wtsaf2yr", "wtsaf4yr")
            }
        }
        else {
            wt.select <- "wtsaf2yr"
        }
        var <- c(var, wt.select)
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_NLR` [exported]

```r
function (data = NULL, all = FALSE, years, NLR, Year = F, join = "left") 
{
    ck <- all(miss(NLR))
    if (all) {
        if (ck) {
            NLR <- TRUE
        }
        else {
            if (miss(NLR)) 
                NLR <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(NLR)) 
                NLR <- FALSE
        }
    }
    if (isTRUE(NLR)) 
        NLR = "NLR"
    var2 <- variable_formula(variable_formula(variable_formula(c(), "Year", "Year"), "seqn", "seqn"), 
        NLR, "NLR")
    years <- data_years(data, years)
    d <- db_cbc(Segmented_neutrophils_number_1000cells.ul = "neu", lymphocyte_number_1000cells.ul = "lym", 
        Year = T)
    d$NLR <- d$neu/d$lym
    d <- d[, c("Year", "seqn", "NLR")]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_NPS` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_cbc(db_HemalBiochemistry(years = years, Year = TRUE, albumin_g.dl = "alb", fast_total_cholesterol_mg.dl = "hdl"), 
        lymphocyte_number_1000cells.ul = "lym", Monocyte_number_1000cells.ul = "mono", Segmented_neutrophils_number_1000cells.ul = "neu")
    d$alb <- ifelse(d$alb >= 4, 0, 1)
    d$hdl <- ifelse(d$hdl > 180, 0, 1)
    d$lmr <- ifelse(d$lym/d$mono > 4.4400000000000004, 0, 1)
    d$nlr <- ifelse(d$neu/d$lym < 2.96, 0, 1)
    d$NPS <- row.sums(d[, c("alb", "hdl", "lmr", "nlr")])
    d$NPS.count <- 4 - do::NA.row.sums(d[, c("alb", "hdl", "lmr", "nlr")])
    d <- d[, c("seqn", "Year", "NPS", "NPS.count")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_OBS` [exported]

```r
function (data, years, day = c(1, 2), OBS.dietary = FALSE, OBS.lifestyle = FALSE, component = FALSE, 
    score = FALSE, Year = FALSE, join = "left", cat = T) 
{
    years <- data_years(data, years)
    if (cat) 
        cat("dietary\n")
    d1 <- db_drtot(years = years, Year = T, fun = "mean", day = day, dietary_fiber_g = T, carotene_re.1999 = T, 
        alpha_carotene_mcg = T, beta_carotene_mcg = T, riboflavin_vitamin_B2_mg = "riboflavin_mg", niacin_mg = T, 
        vitamin_B6_mg = T, total_folate_mcg = T, vitamin_B12_mcg = T, vitamin_C_mg = T, vitamin_E_as_alpha_tocopherol_mg = "vitamin_E_ATE_mg", 
        calcium_mg = T, magnesium_mg = T, zinc_mg = T, copper_mg = T, selenium_mcg = T, iron_mg = T, 
        alcohol_g = T, total_fat_g = T)
    if (cat) 
        cat("BMI\n")
    d2 <- db_bodyMeasure(years = years, BMI_kg.m2 = T)
    if (cat) 
        cat("Physical Activity\n")
    d3 <- dex_PhysicalActivity(all.5 = T, MET = T, total_MET = T, years = years)
    d4 <- db_demo(sex = T, lower_cd = T, years = years, psu_strat = F)
    if (cat) 
        cat("cotinine\n")
    (tsv <- nhs_tsv("lab06|l06_b|cot", "!~hm|ucot", items = "lab", cat = F, years = years))
    d5 <- nhs_read(tsv, "lbxcot:cotinine_ng.ml", cat = F, Year = F)
    d <- Full_Join(d1, d2, d3, d4, d5)
    d$carotene_RE <- d$alpha_carotene_mcg/24 + d$beta_carotene_mcg/12
    if ("carotene_re.1999" %in% colnames(d)) 
        d$carotene_RE[d$Year %in% "1999-2000"] <- d$carotene_re.1999[d$Year %in% "1999-2000"]
    (x2 <- OBS.score.table())
    (x2 <- x2[row.names(x2) %in% colnames(d), ])
    if (cat) 
        cat(paste0(tmcn::toUTF8("<U+6700><U+7EC8><U+7528><U+4E8E><U+8BA1><U+7B97>OBS<U+7684><U+53C2><U+6570><U+6709>: "), 
            nrow(x2), tmcn::toUTF8("<U+4E2A>\n")))
    for (i in row.names(x2)) {
        for (j in colnames(x2)) {
            (xij <- x2[i, j])
            if (xij == "None") 
                (next)(j)
            (ck.sex <- d$sex %in% do::Replace0(j, "-.*"))
            (xi <- d[, i])
            (ck.index <- eval(parse(text = xij)))
            ck.index[is.na(ck.index)] <- FALSE
            ck <- ck.sex & ck.index
            d <- add_col(d, paste0("score_", i), as.numeric(do::Replace0(j, ".*-")), ck)
        }
    }
    (score_vars <- colnames(d)[grepl("score_", colnames(d))])
    (var.obs.dietary <- set::not(score_vars, c("score_PA_total_MET", "score_alcohol_g", "score_BMI_kg.m2", 
        "score_cotinine_ng.ml")))
    d$OBS.dietary <- row.sums(d[, var.obs.dietary])
    d$OBS.dietary.count <- length(var.obs.dietary) - do::NA.row.sums(d[, var.obs.dietary])
    d$OBS.lifestyle <- row.sums(d[, c("score_PA_total_MET", "score_alcohol_g", "score_BMI_kg.m2", "score_cotinine_ng.ml")])
    d$OBS.lifestyle.count <- 4 - do::NA.row.sums(d[, c("PA_total_MET", "alcohol_g", "BMI_kg.m2", "cotinine_ng.ml")])
    d$OBS <- row.sums(d[, score_vars])
    d$OBS_count <- length(score_vars) - do::NA.row.sums(d[, score_vars])
    (var2 <- c("Year", "seqn", "OBS", "OBS_count"))
    if (OBS.dietary) 
        var2 <- c(var2, "OBS.dietary", "OBS.dietary.count")
    if (OBS.lifestyle) 
        var2 <- c(var2, "OBS.lifestyle", "OBS.lifestyle.count")
    if (component) 
        var2 <- c(var2, row.names(x2))
    if (score) 
        var2 <- c(var2, score_vars)
    d2 <- d[, var2]
    return_data(data, d2, Year, key = "seqn", join = join)
}
```

## `dex_PAiaf` [exported]

```r
function (data, years, activity = FALSE, level = FALSE, times = FALSE, duration = FALSE, mets = FALSE, 
    weight_type = FALSE, PA_iaf = FALSE, Year = FALSE, week = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (paq <- nhs_tsv("paqi", years = years, cat = FALSE))
    if (length(paq) == 0) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+8FD9><U+4E9B><U+5E74><U+4EFD><U+6CA1><U+6709>Physical Activity - Individual Activities"))
        if (!do::cnOS()) 
            stop("no Physical Activity - Individual Activities in this year cycle")
    }
    d <- nhs_read(paq, "padactiv:activity", "padlevel:level", "padtimes:times", "paddurat:duration", 
        "padmets:mets", "paaquex:weight_type", lower_cd = TRUE, cat = FALSE)
    if (week) {
        ck <- d$times < 30 & !is.na(d$times)
        d$times[ck] <- d$times[ck]/30 * 7
        d$times[d$times >= 30] <- 7
    }
    d$PA_iaf <- d$times * d$duration * d$mets
    MET_PAiaf <- aggregate(d$PA_iaf, list(seqn = d$seqn), FUN = sum)
    colnames(MET_PAiaf)[2] <- "MET_PAiaf"
    d <- dplyr::left_join(d, MET_PAiaf, "seqn")
    var <- c("Year", "seqn")
    if (activity) 
        var <- c(var, "activity")
    if (level) 
        var <- c(var, "level")
    if (times) 
        var <- c(var, "times")
    if (duration) 
        var <- c(var, "duration")
    if (mets) 
        var <- c(var, "mets")
    if (weight_type) 
        var <- c(var, "weight_type")
    if (PA_iaf) 
        var <- c(var, "PA_iaf")
    var <- c(var, "MET_PAiaf")
    d <- unique(d[, var])
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_PLF` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(diag_MetS(years = years, methods = "IDF2006", Year = TRUE, cat = FALSE, 
        component = TRUE), fast_insulin_uu.ml = "insulin", Ast = "ast", Alt = "alt")
    d <- d[, c("seqn", "Year", "MetS_IDF.2006", "DM", "insulin", "ast", "alt")]
    d$MetS_IDF.2006 <- ifelse(d$MetS_IDF.2006 == "yes", 0.28199999999999997, 0)
    d$DM <- ifelse(d$DM == "DM", 2 * 0.078, 0)
    d$insulin <- 0.52500000000000002 * log10(d$insulin)
    d$ast.alt <- -0.45400000000000001 * log10(d$ast/d$alt)
    d$ast <- 0.52100000000000002 * log10(d$ast)
    d$PLF <- 10^(row.sums(d[, c("MetS_IDF.2006", "DM", "insulin", "ast", "ast.alt")], na.rm = FALSE) - 
        0.80500000000000005)
    d <- d[, c("seqn", "Year", "PLF")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_PLR` [exported]

```r
function (data = NULL, all = FALSE, years, PLR = T, Year = F, join = "left") 
{
    ck <- all(miss(PLR))
    if (all) {
        if (ck) {
            PLR <- TRUE
        }
        else {
            if (miss(PLR)) 
                PLR <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(PLR)) 
                PLR <- FALSE
        }
    }
    if (isTRUE(PLR)) 
        PLR = "PLR"
    var2 <- variable_formula(variable_formula(variable_formula(c(), "Year", "Year"), "seqn", "seqn"), 
        PLR, "PLR")
    years <- data_years(data, years)
    d <- db_cbc(Platelet_count_1000cells.uL = "plt", lymphocyte_number_1000cells.ul = "lym", Year = T)
    d$PLR <- d$plt/d$lym
    d <- d[, c("Year", "seqn", "PLR")]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_PRAL.NEAP` [exported]

```r
function (data, years, day = 1, both2days = TRUE, fun = c("mean", "sum", "alone"), Year = FALSE, join = "left", 
    component = FALSE) 
{
    years <- data_years(data, years)
    fun <- match.arg(fun)
    d <- db_drtot(years = years, Year = TRUE, day = day, both2days = both2days, fun = fun, protein_g = TRUE, 
        phosphorus_mg = TRUE, potassium_mg = TRUE, magnesium_mg = TRUE, calcium_mg = TRUE)
    d$PRAL <- 0.48880000000000001 * d$protein_g + 0.036600000000000001 * d$phosphorus_mg - 0.020500000000000001 * 
        d$potassium_mg - 0.0263 * d$magnesium_mg - 0.012500000000000001 * d$calcium_mg
    d$NEAP <- (54.5 * d$protein_g/(d$potassium_mg/39)) - 10.199999999999999
    var <- c("seqn", "Year", "PRAL", "NEAP")
    if (component) 
        var <- c(var, "protein_g", "calcium_mg", "phosphorus_mg", "magnesium_mg", "potassium_mg")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_PhysicalActivity` [exported]

```r
function (data, years, all.5 = FALSE, walk_bicycle = FALSE, Tasks.HomeYard = FALSE, Muscle.strength = FALSE, 
    WorkActivity = FALSE, RecreationalActivity = FALSE, activity = FALSE, time = FALSE, MET = FALSE, 
    week = TRUE, direction = c("m", "v", "no"), total_time, total_MET, component = FALSE, Year = FALSE, 
    join = "left") 
{
    if (all.5) {
        walk_bicycle = TRUE
        Tasks.HomeYard = TRUE
        Muscle.strength = TRUE
        WorkActivity = TRUE
        RecreationalActivity = TRUE
    }
    if (isTRUE(time) & missing(total_time)) 
        total_time <- TRUE
    if (missing(total_time)) 
        total_time <- FALSE
    if (isTRUE(MET) & missing(total_MET)) 
        total_MET <- TRUE
    if (missing(total_MET)) 
        total_MET <- FALSE
    years <- data_years(data, years)
    d <- data.frame(seqn = 1)[-1, , drop = FALSE]
    if (walk_bicycle) {
        d0 <- dex_walk_bicycle(years = years, Year = all(!"Year" %in% colnames(d), Year), activity = activity, 
            time = time, MET = MET, week = week)
        if (!is.null(d0)) 
            d <- dplyr::full_join(d, d0, "seqn")
    }
    if (Tasks.HomeYard) {
        d0 <- dex_Tasks.HomeYard(years = years, Year = all(!"Year" %in% colnames(d), Year), activity = activity, 
            time = time, MET = MET, week = week)
        if (!is.null(d0)) 
            d <- dplyr::full_join(d, d0, "seqn")
    }
    if (Muscle.strength) {
        d0 <- dex_Muscle.strength(years = years, Year = all(!"Year" %in% colnames(d), Year), activity = activity, 
            times = FALSE, MET = MET, week = week)
        if (!is.null(d0)) 
            d <- dplyr::full_join(d, d0, "seqn")
    }
    if (WorkActivity) {
        d0 <- dex_WorkActivity(years = years, Year = all(!"Year" %in% colnames(d), Year), activity = activity, 
            time = time, MET = MET, direction = direction)
        if (!is.null(d0)) 
            d <- dplyr::full_join(d, d0, "seqn")
    }
    if (RecreationalActivity) {
        d0 <- dex_RecreationalActivity(years = years, Year = all(!"Year" %in% colnames(d), Year), activity = activity, 
            time = time, MET = MET, direction = direction)
        if (!is.null(d0)) 
            d <- dplyr::full_join(d, d0, "seqn")
    }
    d[d == "unable to do activity"] <- "no"
    if (total_time) {
        timevar <- set::grep_and(colnames(d), "time_")
        if (length(timevar) > 0) 
            d$PA_total_time <- round(row.sums(d[, timevar, drop = FALSE]), 3)
    }
    if (total_MET) {
        metvar <- set::grep_and(colnames(d), "MET_")
        if (length(metvar) > 0) 
            d$PA_total_MET <- round(row.sums(d[, metvar, drop = FALSE]), 3)
    }
    if (!component) 
        d <- d[, set::grep_not_or(colnames(d), c("time_", "MET_")), drop = FALSE]
    if (!missing(data)) 
        d <- drop_col(d, "Year")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_RecreationalActivity` [exported]

```r
function (data, years, activity = FALSE, time = FALSE, MET = FALSE, direction = c("m", "v", "no"), Year = FALSE, 
    join = "left") 
{
    direction <- match.arg(direction)
    if (isFALSE(activity) & isFALSE(time) & isFALSE(MET)) {
        if (do::cnOS()) 
            tmcn::toUTF8("<U+5FC5><U+987B><U+6307><U+5B9A><U+662F><U+5426><U+63D0><U+53D6>PA<U+6216><U+8005><U+662F>PA<U+7684><U+5EA6><U+91CF>,<U+5373><U+65F6><U+95F4>time<U+6216><U+8005>MET")
        if (!do::cnOS()) 
            stop("Must specify whether to extract PA or a measure of PA, i.e. time or MET")
    }
    years <- data_years(data, years)
    paq <- nhs_tsv("paq\\.|paq_", years = years, cat = FALSE)
    d <- nhs_read(paq, "paq650:vigorous", "paq655:v_days", "pad660:v_minute", "paq665:moderate", "paq670:m_days", 
        "pad675:m_minute", lower_cd = TRUE, cat = FALSE)
    ck00 <- tsv0(d, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    d$vigorous <- as.numeric(Recode(d$vigorous, "no::0", "yes::2"))
    d$moderate <- as.numeric(Recode(d$moderate, "no::0", "yes::1"))
    d$recreational.activity <- row.sums(d[, c("vigorous", "moderate")])
    d$recreational.activity[d$recreational.activity > 2] <- "both"
    d$recreational.activity[d$recreational.activity == "2"] <- "vigorous"
    d$recreational.activity[d$recreational.activity == "1"] <- "moderate"
    d$recreational.activity[d$recreational.activity == "0"] <- "no"
    d$v_time <- d$v_days * d$v_minute
    d$MET_v <- d$v_time * 8
    d$m_time <- d$m_days * d$m_minute
    d$MET_m <- d$m_time * 4
    d$MET_recreational.activity <- row.sums(d[, c("MET_v", "MET_m")])
    if (direction == "m" & time) {
        d$v_time <- d$v_time * 8/4
        d$time_recreational.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    else if (direction == "v" & time) {
        d$m_time <- d$m_time * 4/8
        d$time_recreational.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    else if (direction == "no" & time) {
        d$time_recreational.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    var <- c("seqn", "Year")
    if (activity) 
        var <- c(var, "recreational.activity")
    if (time) 
        var <- c(var, "time_recreational.activity")
    if (MET) 
        var <- c(var, "MET_recreational.activity")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_SARC.F` [exported]

```r
function (data, years, component = F, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::and(years, prepare_years(1999:2004))
    tsv0(years, msg.CN = tmcn::toUTF8("<U+4EC5><U+5728>1999-2004<U+5E74><U+6709><U+6570><U+636E>"), msg.EN = "data only exists in 1999-2004")
    pfq <- nhs_tsv("pfq", years = years, cat = F)
    paq <- nhs_tsv("baq", years = years, cat = F)
    d <- db_demo(nhs_read(pfq, "pfq060e,pfq061e:difficult.lift", "pfq060h,pfq061h:difficult.walk", "pfq060i,pfq061i:difficult.standup", 
        "pfq060c,pfq061c:difficult.climb", paq, "baq010:dizzy.balance.falling", "baq020a:dizzy", "baq020b:balance", 
        "baq020c:falling", lower_cd = T, cat = F), ageyr = "age")
    d <- d[d$age >= 60, ]
    d$difficult.lift.new <- Recode(d$difficult.lift, "no difficulty::0", "some difficulty::1", "much difficulty::2", 
        "unable to do::2", "do not do this activity::NA", "NA::", to.numeric = TRUE)
    d$difficult.walk.new <- Recode(d$difficult.walk, "no difficulty::0", "some difficulty::1", "unable to do::2", 
        "much difficulty::2", "do not do this activity::NA", "NA::", to.numeric = TRUE)
    d$difficult.standup.new <- Recode(d$difficult.standup, "no difficulty::0", "some difficulty::1", 
        "much difficulty::2", "unable to do::2", "do not do this activity::NA", "NA::", to.numeric = TRUE)
    d$difficult.climb.new <- Recode(d$difficult.climb, "no difficulty::0", "some difficulty::1", "much difficulty::2", 
        "unable to do::2", "do not do this activity::NA", "NA::", to.numeric = TRUE)
    d$dizzy[d$dizzy %in% "yes"] <- "dizzy"
    d$balance[d$balance %in% "yes"] <- "balance"
    d$falling[d$falling %in% "yes"] <- "falling"
    bf <- paste0(d$dizzy.balance.falling, "~~", d$dizzy, "~~", d$balance, "~~", d$falling)
    d$bf.new <- Recode(bf, "yes~~no~~balance~~falling::2", "yes~~dizzy~~balance~~falling::2", "yes~~dizzy~~no~~falling::2", 
        "yes~~NA~~balance~~falling::2", "yes~~dizzy~~NA~~falling::2", "yes~~NA~~NA~~falling::2", "yes~~no~~no~~falling::2", 
        "yes~~dizzy~~balance~~no::1", "yes~~no~~balance~~no::1", "yes~~no~~balance~~NA::1", "yes~~NA~~balance~~no::1", 
        "yes~~dizzy~~no~~no::0", "yes~~no~~no~~no::0", "no~~NA~~NA~~NA::0", "yes~~dizzy~~NA~~no::NA", 
        "yes~~dizzy~~NA~~NA::NA", "NA~~NA~~NA~~NA::NA", to.numeric = T)
    d$SARC.F <- row.sums(d[, endsWith(colnames(d), ".new")])
    d$SARC.F.count <- 5 - do::NA.row.sums(d[, endsWith(colnames(d), ".new")])
    d$SARC.F.4 <- ifelse(d$SARC.F >= 4, ">=4", "<4")
    ii <- which(d$SARC.F.4 == "<4" & d$SARC.F.count < 5)
    for (i in ii) {
        range <- d$SARC.F[i] + 0:((5 - d$SARC.F.count[i]) * 2)
        if (!all(range < 4)) 
            d$SARC.F.4[i] <- NA
    }
    var2 <- c("Year", "seqn", "SARC.F", "SARC.F.count", "SARC.F.4")
    if (component) 
        var2 <- c(var2, "difficult.lift", "difficult.walk", "difficult.standup", "difficult.climb", "dizzy.balance.falling", 
            "dizzy", "balance", "falling")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_SDoH` [exported]

```r
function (data, years, score = F, component = F, Year = F, join = "left") 
{
    years <- data_years(data, years)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    version <- 1
    (file <- paste0(get_config_path(), "/attach/dex_SDoH~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        download.file(sprintf("http://146.56.250.62:3838/data/nhanes-attach/dex_SDoH~~version-%s.txt", 
            version), file)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    compo <- c("Employment", "PIR", "Food.security", "Education", "Access.to.healthcare", "Health.insurance", 
        "Housing.instability", "Marital.status")
    score.var <- c("score_Employment", "score_PIR", "score_Food.security", "score_Education", "score_Access.to.healthcare", 
        "score_Health.insurance", "score_Housing.instability", "score_Marital.status")
    d <- d[d$Year %in% years, ]
    if (!score) 
        d <- d[, set::not(colnames(d), score.var)]
    if (!component) 
        d <- d[, set::not(colnames(d), compo)]
    d <- delet_masc(d)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_SHR` [exported]

```r
function (data = NULL, years, SHR = T, glucose_mg.dL = F, HbA1c = F, Year = F, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "Year", "Year"), "seqn", "seqn"), SHR, "SHR"), glucose_mg.dL, "glucose_mg.dL"), HbA1c, "HbA1c")
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(years = years, fast_glucose_mg.dl = "glucose_mg.dL", HbA1c = T, Year = T)
    d$SHR <- d$glucose_mg.dL/(1.5900000000000001 * d$HbA1c - 2.5899999999999999)
    d <- d[!is.na(d$SHR), ]
    d <- d[, c("Year", "seqn", "SHR", "glucose_mg.dL", "HbA1c")]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_SII` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_cbc(Platelet_count_1000cells.uL = "plt", Segmented_neutrophils_number_1000cells.ul = "neu", 
        lymphocyte_number_1000cells.ul = "lym", years = years, Year = T)
    d$SII <- d$plt * d$neu/d$lym
    d <- d[, c("seqn", "Year", "SII")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_Tasks.HomeYard` [exported]

```r
function (data, years, activity = FALSE, time = FALSE, MET = FALSE, week = TRUE, direction = c("m", "v", 
    "no"), Year = FALSE, join = "left") 
{
    direction <- match.arg(direction)
    if (isFALSE(activity) & isFALSE(time) & isFALSE(MET)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5FC5><U+987B><U+6307><U+5B9A><U+662F><U+5426><U+63D0><U+53D6>PA<U+6216><U+8005><U+662F>PA<U+7684><U+5EA6><U+91CF>,<U+5373><U+65F6><U+95F4>time<U+6216><U+8005>MET"))
        if (!do::cnOS()) 
            stop("Must specify whether to extract PA or a measure of PA, i.e. time or MET")
    }
    years <- data_years(data, years)
    paq <- nhs_tsv("paq", "!~ia|paqy", years = years, cat = FALSE)
    d <- nhs_read(paq, "paq100:Tasks.HomeYard", "pad120:times_Tasks.HomeYard", "pad160:minutes_Tasks.HomeYard", 
        lower_cd = TRUE, cat = FALSE)
    ck00 <- tsv0(d, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    if (week) {
        d$times_Tasks.HomeYard <- d$times_Tasks.HomeYard/30 * 7
    }
    d$time_Tasks.HomeYard <- d$times_Tasks.HomeYard * d$minutes_Tasks.HomeYard
    d$MET_Tasks.HomeYard <- round(d$time_Tasks.HomeYard * 4.5, 2)
    if (direction == "v" & time) {
        d$time_Tasks.HomeYard <- d$time_Tasks.HomeYard * 4.5/8
    }
    else if (direction == "m" & time) {
        d$time_Tasks.HomeYard <- d$time_Tasks.HomeYard * 4.5/4
    }
    var <- c("seqn", "Year")
    if (activity) 
        var <- c(var, "Tasks.HomeYard")
    if (time) 
        var <- c(var, "time_Tasks.HomeYard")
    if (MET) 
        var <- c(var, "MET_Tasks.HomeYard")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_TyG` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(years = years, fast_triglyceride_mg.dl = "ftrig", fast_glucose_mg.dl = "fglu", 
        Year = TRUE)
    d$TyG <- log(d$ftrig * d$fglu/2)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_VAI` [exported]

```r
function (data, years) 
{
    years <- data_years(data, years)
    (demo <- nhs_tsv("demo", years = years, cat = FALSE))
    (bmx <- nhs_tsv("bmx", years = years, cat = FALSE))
    (trigly <- nhs_tsv("lab13am|l13am_b|l13am_c|trigly", years = years, cat = FALSE))
    (hdl <- nhs_tsv("lab13\\.|l13_b|l13_c|hdl", years = years, cat = FALSE))
    nr <- nhs_read(demo, "riagendr:sex", bmx, "bmxwaist:waist", "bmxbmi:bmi", trigly, "lbdtrsi:TG", hdl, 
        "lbdhdlsi,lbdhddsi:HDL", lower_cd = TRUE, cat = FALSE)
    ck <- nr$sex == "male" & !is.na(nr$sex)
    nr$VAI[ck] <- (nr$waist[ck]/(39.68 + (1.8799999999999999 * nr$bmi[ck]))) * (nr$TG[ck]/1.03) * (1.3100000000000001/nr$HDL[ck])
    ck <- nr$sex == "female" & !is.na(nr$sex)
    nr$VAI[ck] <- (nr$waist[ck]/(36.579999999999998 + (1.8899999999999999 * nr$bmi[ck]))) * (nr$TG[ck]/0.81000000000000005) * 
        (1.52/nr$HDL[ck])
    data0 <- nr[, c("seqn", "Year", "VAI")]
    if (missing(data)) {
        data <- data0
    }
    else {
        data0 <- data0[, !colnames(data0) %in% "Year"]
        data <- as.data.frame(dplyr::left_join(data, data0, "seqn"))
    }
    return(data)
}
```

## `dex_VAT` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(dex_METS.IR(dex_WHR(years = years, Year = TRUE), join = "inner"), sex = TRUE, ageyr = "age", 
        psu_strat = FALSE, lower_cd = TRUE)
    d$sex <- ifelse(d$sex == "male", 1, 0)
    d$VAT.dex <- suppressWarnings(exp(4.4660000000000002) + 0.010999999999999999 * (log(d$METS.IR))^3 + 
        3.2389999999999999 * log(d$WHR)^3 + 0.31900000000000001 * d$sex + 0.59399999999999997 * log(d$age))
    d <- d[, c("seqn", "Year", "VAT.dex")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_WHR` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(years = years, waist_circumference_cm = "wt", hip_circumference_cm = "hip", Year = TRUE)
    if (is.null(d$hip)) {
        stop(tmcn::toUTF8("<U+8BE5><U+5E74><U+4EFD><U+6CA1><U+6709><U+6570><U+636E>"))
    }
    d$WHR <- d$wt/d$hip
    d <- d[, c("seqn", "Year", "WHR")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_WHtR` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(years = years, waist_circumference_cm = "wt", height_cm = "ht", Year = TRUE)
    d$WHtR <- d$wt/d$ht
    d <- d[, c("seqn", "Year", "WHtR")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_WorkActivity` [exported]

```r
function (data, years, activity = FALSE, time = FALSE, MET = FALSE, direction = c("m", "v", "no"), Year = FALSE, 
    join = "left") 
{
    direction <- match.arg(direction)
    if (isFALSE(activity) & isFALSE(time) & isFALSE(MET)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5FC5><U+987B><U+6307><U+5B9A><U+662F><U+5426><U+63D0><U+53D6>PA<U+6216><U+8005><U+662F>PA<U+7684><U+5EA6><U+91CF>,<U+5373><U+65F6><U+95F4>time<U+6216><U+8005>MET"))
        if (!do::cnOS()) 
            stop("Must specify whether to extract PA or a measure of PA, i.e. time or MET")
    }
    years <- data_years(data, years)
    paq <- nhs_tsv("paq\\.|paq_", cat = FALSE, years = years)
    d <- nhs_read(paq, "paq605:vigorous", "paq610:v_days", "pad615:v_minute", "paq620:moderate", "paq625:m_days", 
        "pad630:m_minute", lower_cd = TRUE, cat = FALSE)
    ck00 <- tsv0(d, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    if (is.character(d)) {
        if (!missing(data)) 
            return(data)
        return()
    }
    d$vigorous <- as.numeric(Recode(d$vigorous, "no::0", "yes::2"))
    d$moderate <- as.numeric(Recode(d$moderate, "no::0", "yes::1"))
    d$work.activity <- row.sums(d[, c("vigorous", "moderate")])
    d$work.activity[d$work.activity > 2] <- "both"
    d$work.activity[d$work.activity == "2"] <- "vigorous"
    d$work.activity[d$work.activity == "1"] <- "moderate"
    d$work.activity[d$work.activity == "0"] <- "no"
    d$v_time <- d$v_days * d$v_minute
    d$MET_v <- d$v_time * 8
    d$m_time <- d$m_days * d$m_minute
    d$MET_m <- d$m_time * 4
    d$MET_work.activity <- row.sums(d[, c("MET_v", "MET_m")])
    if (direction == "m" & time) {
        d$v_time <- d$v_time * 2
        d$time_work.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    else if (direction == "v" & time) {
        d$m_time <- d$m_time * 1/2
        d$time_work.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    else if (direction == "no" & time) {
        d$time_work.activity <- row.sums(d[, c("m_time", "v_time")])
    }
    var <- c("seqn", "Year")
    if (activity) 
        var <- c(var, "work.activity")
    if (time) 
        var <- c(var, "time_work.activity")
    if (MET) 
        var <- c(var, "MET_work.activity")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_YJP` [exported]

```r
function (data, years, cut = 4, Year = FALSE, cat = TRUE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_HemalBiochemistry(years = 1999, Year = TRUE, Ast = "ast", Alt = "alt", gamma_glutamyl_transferase_13u.l_iu.l = "ggtp", 
        fast_triglyceride_mg.dl = "tg"), BMI_kg.m2 = "bmi")
    d$alt.ast <- ifelse(d$alt/d$ast > 1.5, 1, 0)
    d$ggtp <- ifelse(d$ggtp > 50, 1, 0)
    d$tg <- ifelse(d$tg > 150, 1, 0)
    d$bmi <- ifelse(d$bmi >= 25, 3, ifelse(d$bmi < 23, 0, 2))
    di <- d[, c("alt.ast", "ggtp", "tg", "bmi")]
    count <- 4 - do::NA.row.sums(di)
    di$YJP.score <- row.sums(di)
    di$count <- count
    for (i in 1:nrow(di)) {
        if (di$count[i] == 0) {
            di$YJP.class[i] <- NA
        }
        else {
            (ps <- YJP.ps(dii = di[i, ]))
            if (ps[1] >= cut) {
                di$YJP.class[i] <- "yes"
            }
            else if (ps[2] < cut) {
                di$YJP.class[i] <- "no"
            }
            else {
                di$YJP.class[i] <- NA
            }
        }
    }
    d$YJP.score <- di$YJP.score
    d$YJP.class <- di$YJP.class
    if (!missing(data)) {
        d <- select_row(d, d$seqn %in% data$seqn, cat = FALSE)
        if (cat) 
            print(table(class = d$YJP.class, score = d$YJP.score, useNA = "i"))
    }
    d <- d[, c("seqn", "Year", "YJP.score", "YJP.class")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_ZJU` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(db_bodyMeasure(db_HemalBiochemistry(years = years, fast_glucose_mmol.L = "fast_glucose", 
        fast_triglyceride_mmol.L = "fast_triglyceride", Alt = TRUE, Ast = TRUE, Year = TRUE), BMI_kg.m2 = "BMI"), 
        sex = TRUE)
    d$sex <- tolower(d$sex)
    d$sex <- ifelse(d$sex == "female", 2, 0)
    d$ratio <- d$Alt/d$Ast * 3
    d$ZJU <- rowSums(d[, c("BMI", "fast_glucose", "fast_triglyceride", "ratio", "sex")])
    d <- d[, c("Year", "seqn", "ZJU")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_animal.protein` [internal]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_fped(pf_meat = TRUE, pf_curedmeat = TRUE, pf_organ = TRUE, pf_poult = TRUE, pf_seafd_hi = TRUE, 
        pf_seafd_low = TRUE, pf_eggs = TRUE, d_total = TRUE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_body.fat.percentage` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_demo(years = years, Year = T, ageyr = "age", sex = "sex", lower_cd = T), BMI_kg.m2 = "BMI")
    d$sex <- Recode(d$sex, "female::1", "male::0", to.numeric = T)
    d$body.fat.percentage <- with(d, -44.988 + (0.503 * age) + (10.689 * sex) + (3.1720000000000002 * 
        BMI) - (0.025999999999999999 * BMI^2) + (0.18099999999999999 * BMI * sex) - (0.02 * BMI * age) - 
        (0.0050000000000000001 * BMI^2 * sex) + (0.00021000000000000001 * BMI^2 * age))
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_eGDR` [exported]

```r
function (data = NULL, all = FALSE, years, eGDR = T, Year = F, join = "left") 
{
    ck <- all(miss(eGDR))
    if (all) {
        if (ck) {
            eGDR <- TRUE
        }
        else {
            if (miss(eGDR)) 
                eGDR <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(eGDR)) 
                eGDR <- FALSE
        }
    }
    if (isTRUE(eGDR)) 
        eGDR = "eGDR"
    var2 <- variable_formula(variable_formula(variable_formula(c(), "Year", "Year"), "seqn", "seqn"), 
        eGDR, "eGDR")
    years <- data_years(data, years)
    d <- db_bodyMeasure(waist_circumference_cm = "wc", Year = T, years = years)
    d <- diag_Hypertension(d, years = years)
    d <- db_HemalBiochemistry(d, HbA1c = T, years = years)
    d$Hypertension <- Recode(d$Hypertension, "yes::1", "no::0", "NA::", to.numeric = T)
    d$eGDR <- 21.158000000000001 - 0.089999999999999997 * d$wc - 3.407 * d$Hypertension - 0.55100000000000005 * 
        d$HbA1c
    d <- d[, c("Year", "seqn", "eGDR")]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_eGFR` [exported]

```r
function (data, years, method = "CKD_EPI_Scr_2009", Year = FALSE, join = "left") 
{
    allmethod <- c("Cockcroft_Gault", "MDRD_1999", "MDRD_2000", "MDRD_2007", "CKD_EPI_Scr_2021", "CKD_EPI_Scr_2009", 
        "CKD_EPI_SCysC_2012", "CKD_EPI_Scr_SCysC_2012", "Schwartz", "BIS1_Scr", "BIS2_Scr_SCysC", "FAS_age", 
        "FAS_height")
    left <- set::not(method, allmethod)
    if (length(left) > 0) {
        if (do::cnOS()) 
            stop(paste0(tmcn::toUTF8("<U+4EE5><U+4E0B><U+65B9><U+6CD5><U+4E0D><U+6B63><U+786E>: "), paste0(left, 
                collapse = ", ")))
        if (!do::cnOS()) 
            stop(paste0("The following method is not right: ", paste0(left, collapse = ", ")))
    }
    years <- data_years(data, years)
    (demo <- nhs_tsv("demo", items = "demo", years = years, cat = FALSE))
    (bm <- nhs_tsv("bmx", items = "exam", years = years, cat = FALSE))
    (biopro <- nhs_tsv("lab18\\.|l40_b\\.|l40_c\\.|biopro", items = "lab", years = years, cat = FALSE))
    (cyst <- nhs_tsv("sscyst_", items = "lab", years = years, cat = FALSE))
    data0 <- nhs_read(demo, "ridageyr:age", "riagendr:sex", "ridreth1:eth1", "ridreth2:eth2", "ridreth3:eth3", 
        bm, "bmxwt:weight", "bmxht:height", biopro, "lbxscr,lbdscr:scr", "lbxsal:alb", "lbxsbu:bun", 
        cyst, "sscypc:SCysC", lower_cd = TRUE, cat = FALSE, Year = TRUE)
    if ("1999-2000" %in% data0$Year) 
        data0$scr[data0$Year %in% "1999-2000"] <- 1.0129999999999999 * data0$scr[data0$Year %in% "1999-2000"] + 
            0.14699999999999999
    if ("2005-2006" %in% data0$Year) 
        data0$scr[data0$Year %in% "2005-2006"] <- 0.97799999999999998 * data0$scr[data0$Year %in% "2005-2006"] - 
            0.016
    if ("eth1" %in% colnames(data0)) {
        data0$eth1 <- as.numeric(Recode(data0$eth1, "non-hispanic black::1", "non-hispanic white::0", 
            "other race - including multi-racial::0", "mexican american::0", "other hispanic::0"))
    }
    else {
        data0$eth1 <- NA
    }
    if ("eth2" %in% colnames(data0)) {
        data0$eth2 <- as.numeric(Recode(data0$eth2, "non-hispanic black::1", "non-hispanic white::0", 
            "other race - including multi-racial::0", "mexican american::0", "other hispanic::0"))
    }
    else {
        data0$eth2 <- NA
    }
    if ("eth3" %in% colnames(data0)) {
        data0$eth3 <- as.numeric(Recode(data0$eth3, "non-hispanic white::0", "mexican american::0", "non-hispanic asian::0", 
            "non-hispanic black::1", "other race - including multi-racial::0", "other hispanic::0"))
    }
    else {
        data0$eth3 <- NA
    }
    data0$black <- ifelse(row.sums(data0[, c("eth1", "eth2", "eth3")]) > 0, "black", "no")
    if ("Cockcroft_Gault" %in% method) {
        data0$Cockcroft_Gault <- (140 - data0$age) * data0$weight/(72 * data0$scr) * ifelse(data0$sex == 
            "female", 0.84999999999999998, 1)
    }
    if ("MDRD_1999" %in% method) {
        data0$MDRD_1999 <- 170 * (data0$scr^-0.999) * (data0$age^-0.17599999999999999) * (data0$bun^-0.17000000000000001) * 
            (data0$alb^0.13800000000000001) * ifelse(data0$sex == "female", 0.76200000000000001, 1)^ifelse(data0$black == 
            "black", 1.8100000000000001, 1)
    }
    if ("MDRD_2000" %in% method) {
        data0$MDRD_2000 <- 186 * (data0$scr^-1.1539999999999999) * (data0$age^-0.20300000000000001) * 
            ifelse(data0$sex == "female", 0.74199999999999999, 1)^ifelse(data0$black == "black", 1.21, 
                1)
    }
    if ("MDRD_2007" %in% method) {
        data0$MDRD_2007 <- 175 * (data0$scr^-1.1539999999999999) * (data0$age^-0.20300000000000001) * 
            ifelse(data0$sex == "female", 0.74199999999999999, 1) * ifelse(data0$black == "black", 1.21, 
            1)
    }
    if ("CKD_EPI_Scr_2021" %in% method) {
        a <- ifelse(data0$sex == "female", 0.69999999999999996, 0.90000000000000002)
        c <- ifelse(data0$sex == "female", 1.012, 1)
        b <- rep(NA, nrow(data0))
        b[data0$sex == "female" & data0$scr <= 0.69999999999999996] <- -0.24099999999999999
        b[data0$sex == "female" & data0$scr > 0.69999999999999996] <- -1.2
        b[data0$sex == "male" & data0$scr <= 0.90000000000000002] <- -0.30199999999999999
        b[data0$sex == "male" & data0$scr > 0.90000000000000002] <- -1.2
        data0$CKD_EPI_Scr_2021 <- 142 * (data0$scr/a)^b * 0.99380000000000002^data0$age * c
    }
    if ("CKD_EPI_Scr_2009" %in% method) {
        a <- rep(NA, length(data0$black))
        a[data0$black == "black" & data0$sex == "female"] <- 166
        a[data0$black == "black" & data0$sex == "male"] <- 163
        a[data0$black != "black" & data0$sex == "female"] <- 144
        a[data0$black != "black" & data0$sex == "male"] <- 141
        b <- ifelse(data0$sex == "female", 0.69999999999999996, 0.90000000000000002)
        c <- rep(NA, length(data0$black))
        c[data0$sex == "female" & data0$scr <= 0.69999999999999996] <- -0.32900000000000001
        c[data0$sex == "female" & data0$scr > 0.69999999999999996] <- -1.2090000000000001
        c[data0$sex == "male" & data0$scr <= 0.90000000000000002] <- -0.41099999999999998
        c[data0$sex == "male" & data0$scr > 0.90000000000000002] <- -1.2090000000000001
        data0$CKD_EPI_Scr_2009 <- a * ((data0$scr/b)^c) * (0.99299999999999999^data0$age)
    }
    if ("CKD_EPI_SCysC_2012" %in% method) {
        if ("SCysC" %in% colnames(data0)) {
            a <- ifelse(data0$SCysC <= 0.80000000000000004, -0.499, -1.3280000000000001)
            female <- ifelse(data0$sex == "female", 0.93200000000000005, 1)
            data0$CKD_EPI_SCysC_2012 <- 133 * ((data0$SCysC/0.80000000000000004)^a) * (0.996^data0$age) * 
                female
        }
        else {
            if (do::cnOS()) 
                message(tmcn::toUTF8("<U+5F53><U+524D><U+6570><U+636E><U+6CA1><U+6709><U+80F1><U+6291><U+7D20>C"))
            if (!do::cnOS()) 
                message("There is no cystatin C in the current data")
        }
    }
    if ("CKD_EPI_Scr_SCysC_2012" %in% method) {
        if ("SCysC" %in% colnames(data0)) {
            a <- ifelse(data0$sex == "female", 130, 135)
            b <- ifelse(data0$sex == "female", 0.69999999999999996, 0.90000000000000002)
            c <- rep(NA, length(data0$sex))
            c[data0$sex == "female" & data0$scr <= 0.69999999999999996] <- -0.248
            c[data0$sex == "female" & data0$scr > 0.69999999999999996] <- -0.60099999999999998
            c[data0$sex == "male" & data0$scr <= 0.90000000000000002] <- -0.20699999999999999
            c[data0$sex == "male" & data0$scr > 0.90000000000000002] <- -0.60099999999999998
            d <- ifelse(data0$SCysC <= 0.80000000000000004, -0.375, -0.71099999999999997)
            black <- ifelse(data0$black == "black", 1.0800000000000001, 1)
            data0$CKD_EPI_Scr_SCysC_2012 <- a * ((data0$scr/b)^c) * ((data0$SCysC/0.80000000000000004)^d) * 
                (0.995^data0$age) * black
        }
        else {
            if (do::cnOS()) 
                message(tmcn::toUTF8("<U+5F53><U+524D><U+6570><U+636E><U+6CA1><U+6709><U+80F1><U+6291><U+7D20>C"))
            if (!do::cnOS()) 
                message("There is no cystatin C in the current data")
        }
    }
    if ("Schwartz" %in% method) {
        if ("SCysC" %in% colnames(data0)) {
            data0$Schwartz <- 39.799999999999997 * ((data0$height/100/data0$scr)^0.45600000000000002) * 
                ((1.8/data0$SCysC)^0.41799999999999998) * ((30/data0$bun)^0.079000000000000001) * ifelse(data0$sex == 
                "male", 1.0760000000000001, 1) * ((data0$height/100/1.3999999999999999)^0.17899999999999999)
        }
        else {
            if (do::cnOS()) 
                message(tmcn::toUTF8("<U+5F53><U+524D><U+6570><U+636E><U+6CA1><U+6709><U+80F1><U+6291><U+7D20>C"))
            if (!do::cnOS()) 
                message("There is no cystatin C in the current data")
        }
    }
    if ("BIS1_Scr" %in% method) {
        data0$BIS1_Scr <- 3736 * (data0$scr^-0.87) * (data0$age^-0.94999999999999996) * ifelse(data0$sex == 
            "female", 0.81999999999999995, 1)
    }
    if ("BIS2_Scr_SCysC" %in% method) {
        if ("SCysC" %in% colnames(data0)) {
            data0$BIS2_Scr_SCysC <- 767 * (data0$SCysC^-0.60999999999999999) * (data0$scr^-0.40000000000000002) * 
                (data0$age^-0.56999999999999995) * ifelse(data0$sex == "female", 0.87, 1)
        }
        else {
            if (do::cnOS()) 
                message(tmcn::toUTF8("<U+5F53><U+524D><U+6570><U+636E><U+6CA1><U+6709><U+80F1><U+6291><U+7D20>C"))
            if (!do::cnOS()) 
                message("There is no cystatin C in the current data")
        }
    }
    if ("FAS_age" %in% method) {
        data0$FAS_age <- eGFR_FAS_age(data0, "scr")
    }
    if ("FAS_height" %in% method) {
        data0$FAS_height <- eGFR_FAS_height(data0, "scr")
    }
    var <- c("seqn", "Year", method)
    d <- data0[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_ePWV` [exported]

```r
function (data, years, Year = FALSE, join = "left", component = F) 
{
    years <- data_years(data, years)
    d <- db_blood.pressure(db_demo(years = years, ageyr = "age", Year = TRUE, psu_strat = F), bpx = F, 
        dar = T, join = "right")
    d$MAP <- d$bpxdar + 0.40000000000000002 * (d$bpxsar - d$bpxdar)
    d$ePWV <- with(d, 9.5869999999999997 - 0.40200000000000002 * age + 4.5599999999999996 * (10^-3) * 
        (age^2) - 2.621 * (10^-5) * (age^2) * MAP + 3.1760000000000002 * (10^-3) * age * MAP - 1.8320000000000001 * 
        (10^-2) * MAP)
    var <- c("seqn", "Year", "ePWV")
    if (component) 
        append(var) <- c("age", "MAP")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_fasting.time` [exported]

```r
function (data = NULL, years, day = 1, fasting.time = T, Year = F, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(c(), "Year", "Year"), "seqn", "seqn"), 
        fasting.time, "fasting.time")
    years <- data_years(data, years)
    d <- db_driff(time_of_eating_occasion_hh.mm = "time", Year = T, energy_kcal = "kcal", day = day)
    d <- d[, c("Year", "seqn", "time", "kcal")]
    d <- d[d$kcal >= 50 & !is.na(d$kcal), ]
    d_min <- group_min(d, vars = "time", bys = c("Year", "seqn"))
    d_max <- group_max(d, vars = "time", bys = c("Year", "seqn"))
    d <- inner_join(d_min, d_max, c("Year", "seqn"))
    d$fasting.time <- (24 * 60 * 60 - (as.numeric(d$time.y) - as.numeric(d$time.x)))/60/60
    d <- d[, c("Year", "seqn", "fasting.time")]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_fat.mass` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_demo(years = years, sex = TRUE, ageyr = "age", eth1 = "eth", Year = TRUE), 
        height_cm = "height", Weight_kg = "Weight", waist_circumference_cm = "wc")
    d$eth <- Recode(d$eth, "Non-Hispanic Black::black", "Non-Hispanic White::hispanic", "Other Race - Including Multi-Racial::other", 
        "Mexican American::mexican", "Other Hispanic::hispanic")
    b <- ifelse(d$sex == "Male", -18.591999999999999, 11.817)
    age <- ifelse(d$sex == "Male", -0.0089999999999999993, 0.041000000000000002)
    height <- ifelse(d$sex == "Male", -0.080000000000000002, -0.19900000000000001)
    weight <- ifelse(d$sex == "Male", 0.22600000000000001, 0.60999999999999999)
    wc <- ifelse(d$sex == "Male", 0.38700000000000001, 0.043999999999999997)
    eth <- rep(NA, nrow(d))
    eth[d$sex == "Male" & d$eth == "mexican"] <- 0.080000000000000002
    eth[d$sex == "Female" & d$eth == "mexican"] <- 0.38
    eth[d$sex == "Male" & d$eth == "hispanic"] <- -0.188
    eth[d$sex == "Female" & d$eth == "hispanic"] <- 0.070000000000000007
    eth[d$sex == "Male" & d$eth == "black"] <- -0.48299999999999998
    eth[d$sex == "Female" & d$eth == "black"] <- -1.1799999999999999
    eth[d$sex == "Male" & d$eth == "other"] <- 1.05
    eth[d$sex == "Female" & d$eth == "other"] <- 0.32500000000000001
    d$fatmass <- b + age * d$age + height * d$height + weight * d$Weight + wc * d$wc + eth
    d <- d[, c("seqn", "Year", "fatmass")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_fii` [exported]

```r
function (data = NULL, all = FALSE, day = 1, years, Year = F, join = "left") 
{
    years <- data_years(data, years)
    d <- db_driff(Year = T, grams = T, years = years, day = day, fun = "mean")
    d <- d[, c("Year", "seqn", "food.code", "grams")]
    file <- paste0(get_config_path(), "/attach/fii.xlsx")
    if (!file.exists(file)) 
        stop("<U+8BF7><U+5230><U+5148><U+4E0B><U+8F7D>fii<U+8BA1><U+7B97><U+8868><U+683C>")
    fiicd <- openxlsx::read.xlsx(file)
    fiicd <- fiicd[, c("Food_code", "FII")]
    colnames(fiicd)[colnames(fiicd) == "Food_code"] <- "food.code"
    d <- inner_join(d, fiicd, "food.code")
    d$fii <- d$grams/100 * d$FII
    d <- aggregate_sum(d, "fii", c("Year", "seqn"), na.rm = T)
    d <- d[!is.na(d$fii), ]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `dex_high.quality.carbohydrate` [internal]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_fped(day = 1, dietary = "tot", years = 1999, g_whole = TRUE, f_whole = TRUE, v_legumes = TRUE, 
        v_drkgr = TRUE, v_redor_other = TRUE, v_redor_tomato = TRUE, v_redor_total = TRUE, v_other = TRUE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_lean.mass` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_demo(years = years, sex = TRUE, ageyr = "age", eth1 = "eth", Year = TRUE), 
        height_cm = "height", Weight_kg = "Weight", waist_circumference_cm = "wc")
    d$eth <- Recode(d$eth, "Non-Hispanic Black::black", "Non-Hispanic White::hispanic", "Other Race - Including Multi-Racial::other", 
        "Mexican American::mexican", "Other Hispanic::hispanic")
    b <- ifelse(d$sex == "Male", 19.363, -10.683)
    age <- ifelse(d$sex == "Male", 0.001, -0.039)
    height <- ifelse(d$sex == "Male", 0.064000000000000001, 0.186)
    weight <- ifelse(d$sex == "Male", 0.75600000000000001, 0.38300000000000001)
    wc <- ifelse(d$sex == "Male", -0.36599999999999999, -0.042999999999999997)
    eth <- rep(NA, nrow(d))
    eth[d$sex == "Male" & d$eth == "mexican"] <- -0.066000000000000003
    eth[d$sex == "Female" & d$eth == "mexican"] <- -0.35899999999999999
    eth[d$sex == "Male" & d$eth == "hispanic"] <- 0.23100000000000001
    eth[d$sex == "Female" & d$eth == "hispanic"] <- -0.058999999999999997
    eth[d$sex == "Male" & d$eth == "black"] <- 0.432
    eth[d$sex == "Female" & d$eth == "black"] <- 1.085
    eth[d$sex == "Male" & d$eth == "other"] <- -1.0069999999999999
    eth[d$sex == "Female" & d$eth == "other"] <- -0.34000000000000002
    d$leanmass <- b + age * d$age + height * d$height + weight * d$Weight + wc * d$wc + eth
    d <- d[, c("seqn", "Year", "leanmass")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_low.qulity.carbohydrate` [internal]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_fped(day = 1, dietary = "tot", years = 1999, g_refined = TRUE, add_sugars = TRUE, f_juice = TRUE, 
        v_starchy_potato = TRUE, v_starchy_other = TRUE)
}
```

## `dex_phenoAge` [exported]

```r
function (data, years, component = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::and(prepare_years(1999:2009), years)
    d <- db_demo(db_cbc(db_HemalBiochemistry(years = years, albumin_g.L = T, creatinine_umol.L = T, refrige_glucose_mmol.L = T, 
        C_reactive_protein_mg.dl = T, alkaline_phosphatase_u.L = T, Year = T), Lymphocyte_percent = T, 
        Mean_cell_volume_fL = T, Red_cell_distribution_width = T, wbc_1000cells.ul = T), ageyr = "age", 
        psu_strat = F)
    xb <- -0.033599999999999998 * d$albumin_g.L + 0.0094999999999999998 * d$creatinine_umol.L + 0.1953 * 
        d$refrige_glucose_mmol.L + 0.095399999999999999 * log(d$C_reactive_protein_mg.dl) + -0.012 * 
        d$Lymphocyte_percent + 0.026800000000000001 * d$Mean_cell_volume_fL + 0.3306 * d$Red_cell_distribution_width + 
        0.0019 * d$alkaline_phosphatase_u.L + 0.055399999999999998 * d$wbc_1000cells.ul + 0.080399999999999999 * 
        d$age + -19.906700000000001
    d$phynotypicage <- 141.5 + log(-0.0055300000000000002 * log(exp(-1.5171399999999999 * exp(xb)/0.0076927000000000002)))/0.091649999999999995
    var2 <- c("Year", "seqn", "phynotypicage")
    if (component) 
        var2 <- c(var2, c("refrige_glucose_mmol.L", "alkaline_phosphatase_u.L", "albumin_g.L", "creatinine_umol.L", 
            "C_reactive_protein_mg.dl", "wbc_1000cells.ul", "Lymphocyte_percent", "Mean_cell_volume_fL", 
            "Red_cell_distribution_width", "age"))
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_plant.protein` [internal]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_fped(g_whole = TRUE, g_refined = TRUE, pf_nutsds = TRUE, pf_soy = TRUE, pf_legumes = TRUE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_ulb` [exported]

```r
function (data, years, component = FALSE, weight = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (tsv <- nhs_tsv("slq", years = years, cat = F))
    tsv0(tsv)
    d <- dex_PhysicalActivity(dex_HEI(db_demo(db_Alcohol.drinks(diag_smoke(nhs_read(tsv, "sld010h,sld012:sleep.hours", 
        years = years, Year = TRUE, cat = F))), sex = TRUE, lower_cd = TRUE, psu_strat = F), version = 2015, 
        day = 1, dietary = "tot", component = F, energy = F), walk_bicycle = TRUE, Tasks.HomeYard = ifelse(any(years %in% 
        prepare_years(1999:2005)), T, F), Muscle.strength = ifelse(any(years %in% prepare_years(1999:2005)), 
        T, F), WorkActivity = ifelse(any(years %in% set::not(prepare_years(), prepare_years(1999:2005))), 
        T, F), RecreationalActivity = ifelse(any(years %in% set::not(prepare_years(), prepare_years(1999:2005))), 
        T, F), time = TRUE, total_time = TRUE, direction = "no", week = TRUE)
    if (weight) 
        d <- db_drtot(data = d, day = 1, wtdrd1 = TRUE)
    d$smoke <- as.numeric(Recode(d$smoke, "never::0", "former::1", "now::1", "NA::"))
    ck <- (d$sex == "male" & d$drinks.day >= 4) | (d$sex == "female" & d$drinks.day >= 5)
    d$drinks.day <- ifelse(ck, 1, 0)
    d$hei2015 <- ifelse(d$hei2015_total_score < 50, 1, 0)
    d$PA_total_time <- ifelse(d$PA_total_time > 150, 1, 0)
    d$sleep.hours <- ifelse(d$sleep.hours < 7 | d$sleep.hours > 9, 1, 0)
    head(d)
    var <- c("smoke", "drinks.day", "hei2015", "PA_total_time", "sleep.hours")
    d$ulb <- row.sums(d[, var])
    d$ulb.count <- ncol(d[, var]) - do::NA.row.sums(d[, var])
    key <- c("seqn", "Year", "ulb", "ulb.count")
    if (weight) 
        append(key) <- "wtdrd1"
    if (component) 
        append(key) <- var
    d <- d[, key]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_usFLI` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(db_bodyMeasure(db_demo(eth1 = "eth", ageyr = "age", psu_strat = FALSE, 
        years = years, Year = TRUE), waist_circumference_cm = "wc"), gamma_glutamyl_transferase_13u.l_iu.l = "ggt", 
        fast_insulin_pmol.L = "insulin", fast_glucose_mg.dl = "glu")
    d$eth <- Recode(d$eth, "Non-Hispanic Black::e1", "Mexican American::e2", "Non-Hispanic White::e3", 
        "Other Race - Including Multi-Racial::e3", "Other Hispanic::e3")
    d$eth <- Recode(d$eth, "e1::-0.8073", "e2::0.3458", "e3::0", to.numeric = T)
    a <- exp(d$eth + 0.0092999999999999992 * d$age + 0.61509999999999998 * log(d$ggt) + 0.024899999999999999 * 
        d$wc + 1.1792 * log(d$insulin) + 0.82420000000000004 * log(d$glu) - 14.7812)
    d$usFLI <- a/(1 + a) * 100
    d <- d[, c("seqn", "Year", "usFLI")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_walk_bicycle` [exported]

```r
function (data, years, activity = FALSE, time = FALSE, MET = FALSE, week = TRUE, direction = c("m", "v", 
    "no"), Year = FALSE, join = "left") 
{
    direction <- match.arg(direction)
    if (isFALSE(activity) & isFALSE(time) & isFALSE(MET)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5FC5><U+987B><U+6307><U+5B9A><U+662F><U+5426><U+63D0><U+53D6>PA<U+6216><U+8005><U+662F>PA<U+7684><U+5EA6><U+91CF>,<U+5373><U+65F6><U+95F4>time<U+6216><U+8005>MET"))
        if (!do::cnOS()) 
            stop("Must specify whether to extract PA or a measure of PA, i.e. time or MET")
    }
    years <- data_years(data, years)
    (paq <- nhs_tsv("paq", "!~ia|paqy", years = years, cat = FALSE))
    d <- nhs_read(paq, "pad020,paq635:walk_bicycle", "paq050q:times06", "paq050u:units06", "pad080:wbminute06", 
        "paq640:wbdays07", "pad645:wbminute07", lower_cd = TRUE, cat = FALSE)
    ck00 <- tsv0(d, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    if ("times06" %in% colnames(d)) {
        if (week) {
            ck <- d$units06 %in% "day"
            d$time_walk_bicycle[ck] <- d$wbminute06[ck] * 7
            ck <- d$units06 %in% "week"
            ck6 <- d$times06 <= 6 & ck
            ck7 <- d$times06 >= 7 & ck
            d$time_walk_bicycle[ck6] <- d$wbminute06[ck6] * d$times06[ck6]
            d$time_walk_bicycle[ck7] <- d$wbminute06[ck7] * 7
            ck <- d$units06 %in% "month"
            ck29 <- d$times06 <= 29 & ck
            ck30 <- d$times06 >= 30 & ck
            d$time_walk_bicycle[ck29] <- d$wbminute06[ck29] * d$times06[ck29]/30 * 7
            d$time_walk_bicycle[ck30] <- d$wbminute06[ck30] * 7
        }
        else {
            d$time_walk_bicycle <- d$times06 * d$wbminute06
        }
        y <- unique(d$Year[!is.na(d$times06)])
        d$MET_walk_bicycle[d$Year %in% y] <- round(d$time_walk_bicycle * 4, 2)[d$Year %in% y]
        colnames(d)[colnames(d) == "units06"] <- "unit_walk_bicycle"
    }
    if ("wbdays07" %in% colnames(d)) {
        y <- unique(d$Year[!is.na(d$wbdays07)])
        d$wbminute07 <- d$wbdays07 * d$wbminute07
        d$MET_walk_bicycle[d$Year %in% y] <- (d$wbminute07 * 4)[d$Year %in% y]
        d$time_walk_bicycle[d$Year %in% y] <- d$wbminute07[d$Year %in% y]
        d$unit_walk_bicycle[d$Year %in% y] <- "week"
    }
    if (direction == "v") 
        d$time_walk_bicycle <- d$time_walk_bicycle * 1/2
    var <- c("seqn", "Year")
    if (activity) 
        var <- c(var, "walk_bicycle")
    if (time) {
        var <- c(var, "time_walk_bicycle")
        if (!week) 
            var <- c(var, "unit_walk_bicycle")
    }
    if (MET) 
        var <- c(var, "MET_walk_bicycle")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```


