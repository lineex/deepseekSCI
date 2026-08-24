# Integrated supporting reference: nhanesr-function-reference/references/expressions-diag_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-diag_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `diag_`

## `diag_ACO` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    copd <- diag_COPD(years = years, Year = TRUE, cat = FALSE)
    asthma <- diag_Asthma(years = years, cat = FALSE)
    d <- dplyr::full_join(copd, asthma, "seqn")
    d$ACO[d$COPD == "yes" & d$Asthma == "yes"] <- "ACO"
    d$ACO[d$COPD == "yes" & d$Asthma == "no"] <- "COPD"
    d$ACO[d$COPD == "no" & d$Asthma == "yes"] <- "Asthma"
    d$ACO[d$COPD == "no" & d$Asthma == "no"] <- "no"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_ASCVD` [exported]

```r
function (data, years, early_ASCVD = FALSE, early_male = 55, early_female = 60, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("mcq|spx", "!~spxraw", years = years, cat = FALSE)
    d <- db_demo(nhs_read(tsv, "mcq160c:coronary.heart.disease", "mcq180c,mcd180c:coronary.heart.disease_age", 
        "mcq160d:angina", "mcq180d,mcd180d:angina_age", "mcq160e:heart.attack", "spq070e:heart.attack2", 
        "mcq180e,mcd180e:heart.attack_age", "mcq160f:stroke", "spq070d:stroke2", "mcq180f,mcd180f:stroke_age", 
        cat = FALSE, lower_cd = TRUE), sex = TRUE, lower_cd = TRUE)
    d$coronary.heart.disease_age <- do::Replace0(d$coronary.heart.disease_age, " .*")
    d$angina_age <- do::Replace0(d$angina_age, " .*")
    d$heart.attack_age <- do::Replace0(d$heart.attack_age, " .*")
    d$stroke_age <- do::Replace0(d$stroke_age, " .*")
    d[d == "yes"] <- 1
    d[d == "no"] <- 0
    to_numeric(d) <- colnames(d)
    if ("stroke2" %in% colnames(d)) {
        d$stroke2[!is.na(d$stroke2)] <- 1
        d$stroke2 <- as.numeric(d$stroke2)
        d$stroke <- ifelse(row.sums(d[, c("stroke", "stroke2"), drop = FALSE]) > 0, 1, 0)
        drop_col(d) <- "stroke2"
    }
    if ("heart.attack2" %in% colnames(d)) {
        d$heart.attack2[!is.na(d$heart.attack2)] <- 1
        d$heart.attack2 <- as.numeric(d$heart.attack2)
        d$heart.attack <- ifelse(row.sums(d[, c("heart.attack", "heart.attack2"), drop = FALSE]) > 0, 
            1, 0)
        drop_col(d) <- "heart.attack2"
    }
    d$ASCVD <- ifelse(row.sums(d[, c("coronary.heart.disease", "angina", "heart.attack", "stroke")]) >= 
        1, 1, 0)
    if (early_ASCVD) {
        nms <- which(do::right(colnames(d), 4) == "_age")
        for (i in nms) {
            ck <- (d[, i] < early_male & d$sex == "male") | (d[, i] < early_female & d$sex == "female")
            d[, i] <- ifelse(ck, 1, 0)
        }
        d$early_ASCVD <- ifelse(row.sums(d[, nms, drop = FALSE]) >= 1, 1, 0)
        d$ASCVD[d$ASCVD == 1] <- "ASCVD"
        d$ASCVD[d$ASCVD == 0] <- "no"
        d$ASCVD[d$early_ASCVD == 1] <- "early"
    }
    else {
        d$ASCVD[d$ASCVD == 1] <- "yes"
        d$ASCVD[d$ASCVD == 0] <- "no"
    }
    d <- d[, c("seqn", "Year", "ASCVD")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Anemia` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (demo <- nhs_tsv("demo", items = "demo", years = years, cat = FALSE))
    (hb_tsv <- nhs_tsv("lab25\\.|l25_b\\.|l25_c\\.|cbc", items = "lab", years = years, cat = FALSE))
    nr <- nhs_read(demo, "riagendr:sex", "ridageyr:age", hb_tsv, "lbxhgb:hb", cat = FALSE, psu_strat = F, 
        lower_cd = TRUE)
    nr <- diag_Pregnant(data = nr)
    nr$anemia[nr$age < 0.5] <- "age<0.5y"
    ck <- nr$age >= 0.5 & nr$age < 5
    severe <- 7
    Moderate <- 10
    Mild <- 11
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    ck <- nr$age >= 5 & nr$age < 12
    severe <- 8
    Moderate <- 11
    Mild <- 11.5
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    ck <- nr$age >= 12 & nr$age < 15
    severe <- 8
    Moderate <- 11
    Mild <- 12
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    ck <- nr$age >= 15 & nr$sex == "male"
    severe <- 8
    Moderate <- 11
    Mild <- 13
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    ck <- nr$age >= 15 & nr$sex == "female" & nr$Pregnant %in% "yes"
    severe <- 7
    Moderate <- 10
    Mild <- 11
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    ck <- nr$age >= 15 & nr$sex == "female" & (!nr$Pregnant %in% "yes")
    severe <- 8
    Moderate <- 11
    Mild <- 12
    nr$anemia[ck] <- ifelse(nr$hb[ck] < severe, "Severe", ifelse(nr$hb[ck] < Moderate, "Moderate", ifelse(nr$hb[ck] < 
        Mild, "Mild", "Non-Anaemia")))
    d <- nr[, c("seqn", "Year", "anemia")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Asthma` [exported]

```r
function (data, years, told = TRUE, drug = TRUE, cat = TRUE, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    mcq <- nhs_tsv("mcq", years = years, cat = FALSE)
    d <- nhs_read(mcq, "mcq010:told", cat = FALSE, lower_cd = TRUE)
    if ("told" %in% colnames(d)) {
        if (told | is.character(told)) {
            if (cat) 
                cat("\ntold")
            d$asthma_told <- ifelse(d$told == "yes", 1, 0)
        }
        if (is.character(told)) {
            col_rename(d) <- paste0("asthma_told:", told)
            var_told <- told
        }
        else if (isTRUE(told)) 
            var_told <- "asthma_told"
        else var_told <- c()
    }
    else {
        told <- FALSE
        var_told <- c()
    }
    if (drug | is.character(drug)) {
        if (cat) 
            cat("\ndrug")
        d <- Drug("antiasthmati", data = d, take_drug = "asthma_drug", dup.take.drug = "remove", yes.code = 1, 
            no.code = 0, other.code = 0)
        if (is.character(drug)) {
            col_rename(d) <- paste0("asthma_drug:", drug)
            var_drug <- drug
        }
        else if (isTRUE(drug)) 
            var_drug <- "asthma_drug"
        else var_drug <- c()
    }
    else var_drug <- c()
    d$Asthma <- ifelse(row.sums(d[, c(var_told, var_drug)]) > 0, 1, 0)
    if (!yes1) 
        yes1(d) <- c("Asthma", var_told, var_drug)
    var <- c("Year", "seqn", "Asthma")
    if (is.character(told)) 
        append(var) <- told
    if (is.character(drug)) 
        append(var) <- drug
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_CKD` [exported]

```r
function (data, years, ckd = c("A2", "G3a"), show_CKD = TRUE, show_prognosis = TRUE, show_ACR = FALSE, 
    show_eGFR = FALSE, eGFR_method = "CKD_EPI_Scr_2009", yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_urine.alb.cr(dex_eGFR(years = years, method = eGFR_method, Year = TRUE), uACR_mg.g = "uACR")
    bu_x <- d$uACR
    d$CKD_ACR[bu("[   , 30)")] <- "A1"
    d$CKD_ACR[bu("[ 30, 300]")] <- "A2"
    d$CKD_ACR[bu("(300 , )")] <- "A3"
    d$CKD_ACR <- factor(d$CKD_ACR, levels = c("A1", "A2", "A3"))
    bu_x <- d[, eGFR_method]
    d$CKD_eGFR[bu("[90 , )")] <- "G1"
    d$CKD_eGFR[bu("[60 , 90)")] <- "G2"
    d$CKD_eGFR[bu("[45 , 60)")] <- "G3a"
    d$CKD_eGFR[bu("[30 , 45)")] <- "G3b"
    d$CKD_eGFR[bu("[15 , 30)")] <- "G4"
    d$CKD_eGFR[bu("[ , 15)")] <- "G5"
    d$CKD_eGFR <- factor(d$CKD_eGFR, levels = c("G1", "G2", "G3a", "G3b", "G5", "G4"))
    ck <- d$CKD_ACR %in% "A1" & d$CKD_eGFR %in% c("G1", "G2")
    d$CKD_prognosis[ck] <- "low_risk"
    ck <- (d$CKD_ACR %in% "A1" & d$CKD_eGFR %in% c("G3a")) | (d$CKD_ACR %in% "A2" & d$CKD_eGFR %in% c("G1", 
        "G2"))
    d$CKD_prognosis[ck] <- "moderate_risk"
    ck <- (d$CKD_ACR %in% "A1" & d$CKD_eGFR %in% c("G3b")) | (d$CKD_ACR %in% "A2" & d$CKD_eGFR %in% c("G3a")) | 
        (d$CKD_ACR %in% "A3" & d$CKD_eGFR %in% c("G1", "G2"))
    d$CKD_prognosis[ck] <- "high_risk"
    ck <- (d$CKD_eGFR %in% c("G4", "G5")) | (d$CKD_ACR %in% "A2" & d$CKD_eGFR %in% c("G3b")) | (d$CKD_ACR %in% 
        "A3" & d$CKD_eGFR %in% c("G3a", "G3b"))
    d$CKD_prognosis[ck] <- "very_high_risk"
    d$CKD_prognosis <- factor(d$CKD_prognosis, levels = c("low_risk", "moderate_risk", "high_risk", "very_high_risk"))
    ckd <- do::Replace(toupper(do::Replace0(ckd, " ")), pattern = c("G3A:G3a", "G3B:G3b"))
    uk <- unique(do::left(ckd, 1))
    if (length(uk) == 1) {
        if (do::left(ckd, 1) == "A") {
            level <- levels(d$CKD_ACR)[which(levels(d$CKD_ACR) == ckd[1]):length(levels(d$CKD_ACR))]
            d$CKD <- ifelse((d$CKD_ACR) %=% level, 1, 0)
        }
        else if (do::left(ckd, 1) == "G") {
            level <- levels(d$CKD_eGFR)[which(levels(d$CKD_eGFR) == ckd[1]):length(levels(d$CKD_eGFR))]
            d$CKD <- ifelse((d$CKD_eGFR) %=% level, 1, 0)
        }
    }
    else if (length(uk) == 2) {
        G <- ckd[do::left(ckd, 1) == "G"]
        level <- levels(d$CKD_eGFR)[which(levels(d$CKD_eGFR) == G[1]):length(levels(d$CKD_eGFR))]
        d$CKD_G <- ifelse((d$CKD_eGFR) %=% level, 1, 0)
        no.level_G <- set::not(levels(d$CKD_eGFR), level)
        A <- ckd[do::left(ckd, 1) == "A"]
        level <- levels(d$CKD_ACR)[which(levels(d$CKD_ACR) == A[1]):length(levels(d$CKD_ACR))]
        d$CKD_A <- ifelse((d$CKD_ACR) %=% level, 1, 0)
        d$CKD <- ifelse(row.sums(d[, c("CKD_G", "CKD_A")]) > 0, 1, 0)
        no.level_A <- set::not(levels(d$CKD_ACR), level)
        if (length(no.level_G) > 0) 
            d$CKD[d$CKD_eGFR %=% no.level_G & is.na(d$CKD_ACR)] <- NA
        if (length(no.level_A) > 0) 
            d$CKD[d$CKD_ACR %=% no.level_A & is.na(d$CKD_eGFR)] <- NA
    }
    if (!yes1) 
        yes1(d) <- "CKD"
    var <- c("seqn", "Year")
    if (show_CKD) 
        var <- c(var, "CKD")
    if (show_prognosis) 
        var <- c(var, "CKD_prognosis")
    if (show_ACR) 
        var <- c(var, "CKD_ACR")
    if (show_eGFR) 
        var <- c(var, "CKD_eGFR")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_CKM` [exported]

```r
function (data, years, component = F, Year = F, join = "left") 
{
    years <- data_years(data, years)
    d0 <- db_demo(years = years, Year = T, ageyr = "age", eth1 = "eth", eth3 = T, sex = T, psu_strat = F) %>% 
        db_bodyMeasure(BMI_kg.m2 = "bmi", waist_circumference_cm = "waist") %>% db_HemalBiochemistry(HbA1c = T, 
        fast_glucose_mg.dl = "glu", fast_triglyceride_mg.dl = "tg", hdl_cholesterol_mg.dl = "hdl", wtsaf2yr = T, 
        wtsaf4yr = T) %>% diag_Hypertension(systolic = 130, diastolic = 80, cat = F) %>% diag_DM(cat = F) %>% 
        diag_CKD(eGFR_method = "CKD_EPI_Scr_2021") %>% dex_AHA.PREVENT(CVD_10yr.risk = T) %>% diag_ASCVD() %>% 
        diag_congestive.heart.failure()
    d <- d0[d0$age >= 20, ]
    d <- d[!is.na(d$wtsaf2yr), ]
    (tsv <- nhs_tsv("RXQ_RX", years = years, cat = F))
    di <- nhs_read(tsv, "rxdrsd1", nrows = 1, cat = F)
    if (is.character(di)) {
        d$Fibrillation <- "no"
    }
    else {
        d <- diag_Fibrillation(data = d)
    }
    if (!"Fibrillation" %in% colnames(d)) 
        d$Fibrillation <- "no"
    tsv <- nhs_tsv("lexab", years = years, cat = F)
    if (length(tsv) == 0) {
        d$PAD <- "no"
    }
    else {
        d <- diag_PAD(data = d)
    }
    if ("eth3" %in% colnames(d)) {
        ck <- !is.na(d$eth3)
        d$eth[ck] <- d$eth3[ck]
    }
    d$eth <- tolower(d$eth)
    d$sex <- tolower(d$sex)
    d$asia <- d$eth %in% "non-hispanic asian"
    d$male <- d$sex %in% "male"
    d$high_bmi <- with(d, (asia & bmi >= 23) | (!asia & bmi >= 25))
    d$high_wc <- with(d, (asia & male & waist >= 90) | (asia & !male & waist >= 80) | (!asia & male & 
        waist >= 102) | (!asia & !male & waist >= 88))
    d$low_hdl <- with(d, (male & hdl < 40) | (hdl < 50 & !male))
    d$high_tg <- with(d, tg >= 150)
    d$hp <- d$Hypertension %in% "yes"
    d$dm <- d$DM %in% "DM"
    d$pre_DM <- with(d, (HbA1c >= 5.7000000000000002 & HbA1c < 6.5) | (glu >= 100 & glu < 126))
    d$pre_DM[d$dm] <- F
    d$mets <- ifelse(row.sums(d[, c("high_wc", "low_hdl", "high_tg", "hp", "pre_DM")]) >= 3, T, F)
    d <- d %>% newVb("CKM", ASCVD %in% "yes" ~ "CKM 4", congestive.heart.failure %in% "yes" ~ "CKM 4", 
        Fibrillation %in% "yes" ~ "CKM 4", PAD %in% "yes" ~ "CKM 4", CKD_prognosis %in% "very_high_risk" ~ 
            "CKM 3", CVD_10yr.risk >= 20 ~ "CKM 3", tg >= 135 ~ "CKM 2", hp ~ "CKM 2", dm ~ "CKM 2", 
        mets ~ "CKM 2", CKD_prognosis %in% c("moderate_risk", "high_risk") ~ "CKM 2", high_bmi | high_wc | 
            pre_DM ~ "CKM 1", (!high_bmi) & (!high_wc) ~ "CKM 0")
    d <- d[!is.na(d$CKM), ]
    d$pre_DM <- ifelse(d$pre_DM, "yes", "no")
    d$mets <- ifelse(d$mets, "yes", "no")
    vars <- c("Year", "seqn", "CKM", "wtsaf2yr")
    if ("wtsaf4yr" %in% colnames(d)) 
        vars <- c(vars, "wtsaf4yr")
    if (component) {
        vari <- c("age", "sex", "eth", "bmi", "waist", "glu", "HbA1c", "tg", "hdl", "Hypertension", "DM", 
            "CKD_prognosis", "CVD_10yr.risk", "ASCVD", "congestive.heart.failure", "pre_DM", "mets")
        vars <- c(vars, vari)
    }
    d <- d[, vars]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_COPD` [exported]

```r
function (data, years, told = T, emphysema = TRUE, spx = TRUE, drug = TRUE, cat = TRUE, Year = FALSE, 
    yes1 = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (mcq <- nhs_tsv("mcq", years = years, cat = FALSE))
    (spx_tsv <- nhs_tsv("spx", years = years, cat = FALSE))
    d <- nhs_read(mcq, "mcq160o,mcq160p:told", "mcq160g:emphysema", "mcq160k:chronic", spx_tsv, "spxbfev1:fev1", 
        "spxbfvc:fvc", "spxbqfv1:qfv1-u", "spxbqfvc:qfvc-u", lower_cd = T, cat = FALSE)
    if ("told" %in% colnames(d)) {
        if (told | is.character(told)) {
            if (cat) 
                cat("\ntold")
            d$told <- ifelse(d$told == "yes", 1, 0)
        }
        if (is.character(told)) {
            col_rename(d) <- paste0("told:", told)
            var_told <- told
        }
        else if (isTRUE(told)) 
            var_told <- "told"
        else var_told <- c()
    }
    else {
        told <- FALSE
        var_told <- c()
    }
    if ("emphysema" %in% colnames(d)) {
        if (emphysema | is.character(emphysema)) {
            if (cat) 
                cat("\nemphysema")
            d$emphysema <- ifelse(d$emphysema == "yes", 1, 0)
        }
        if (is.character(emphysema)) {
            col_rename(d) <- paste0("emphysema:", emphysema)
            var_emphysema <- emphysema
        }
        else if (isTRUE(emphysema)) 
            var_emphysema <- "emphysema"
        else var_emphysema <- c()
    }
    else {
        emphysema <- FALSE
        var_emphysema <- c()
    }
    if ("fev1" %in% colnames(d)) {
        if (spx | is.character(spx)) {
            if (cat) 
                cat("\nspx")
            d$COPD_spx <- ifelse(d$fev1/d$fvc < 0.69999999999999996, 1, 0)
            qc <- d$qfv1 %in% c("a", "b") & d$qfvc %in% c("a", "b")
            d$COPD_spx[!qc] <- NA
        }
        if (is.character(spx)) {
            col_rename(d) <- paste0("COPD_spx:", spx)
            var_spx <- spx
        }
        else if (isTRUE(spx)) 
            var_spx <- "COPD_spx"
        else var_spx <- c()
    }
    else {
        spx <- FALSE
        var_spx <- c()
    }
    if (drug | is.character(drug)) {
        if (cat) 
            cat("\ndrug")
        d <- db_demo(diag_smoke(d), ageyr = "age")
        d11 <- Drug("selective phosphodiesterase-4 inhibitors|mast cell stabilizers|leukotriene modifiers|inhaled corticosteroids", 
            data = d, take_drug = "drug", remove.other = T, dup.take.drug = "remove", yes.code = 1, no.code = 0, 
            other.code = 0)
        if (!is.null(d11)) {
            d <- d11
            d$smoke <- ifelse(d$smoke == "never", 0, 1)
            d$chronic <- ifelse(d$chronic == "yes", 1, 0)
            d$other <- ifelse(row.sums(d[, c("smoke", "chronic")]) > 0, 1, 0)
            d$COPD_drug <- ifelse(row.sums(d[, c("drug", "other")]) >= 2, 1, 0)
            d$COPD_drug[d$age < 40] <- NA
            if (is.character(drug)) {
                col_rename(d) <- paste0("COPD_drug:", drug)
                var_drug <- drug
            }
            else if (isTRUE(drug)) 
                var_drug <- "COPD_drug"
            else var_drug <- c()
        }
        else {
            var_drug <- c()
        }
    }
    else var_drug <- c()
    d$COPD <- ifelse(row.sums(d[, c(var_told, var_emphysema, var_spx, var_drug), drop = FALSE]) >= 1, 
        1, 0)
    if (!yes1) 
        yes1(d) <- c("COPD", var_told, var_emphysema, var_spx, var_drug)
    var <- c("Year", "seqn", "COPD")
    if (is.character(emphysema)) 
        append(var) <- emphysema
    if (is.character(spx)) 
        append(var) <- spx
    if (is.character(drug)) 
        append(var) <- drug
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_CVD` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (mcq <- nhs_tsv("mcq", years = years, cat = FALSE))
    d <- diag_stroke(diag_heart.attack(nhs_read(mcq, "mcq160b", "mcq160c", "mcq160d", cat = FALSE, lower_cd = TRUE)))
    d[d == "yes"] <- 1
    d[d == "no"] <- 0
    to_numeric(d) <- colnames(d)
    d$CVD <- ifelse(row.sums(d[, -c(1, 2)]) > 0, "yes", "no")
    d <- d[, c("seqn", "Year", "CVD")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_DM` [exported]

```r
function (data, years, told = TRUE, HbA1c = TRUE, fast_glu = TRUE, OGTT2 = TRUE, rand_glu = TRUE, drug = TRUE, 
    DM1 = FALSE, cat = TRUE, Year = FALSE, join = "left", exclude_Pregnant = TRUE) 
{
    years <- data_years(data, years)
    diq <- nhs_tsv("diq", items = "question", cat = F, years = years)
    ghb <- nhs_tsv("lab10\\.|l10_b\\.|l10_c\\.|ghb", cat = F, items = "lab", years = years)
    gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu", cat = F, items = "Laboratory", years = years)
    biopro <- nhs_tsv("lab18\\.|l40_b\\.|l40_c\\.|biopro", cat = F, years = years)
    l10_2_b <- nhs_tsv("l10_2_b", items = "Laboratory", cat = F, years = years)
    l40_2_b <- nhs_tsv("l40_2_b", items = "Laboratory", cat = F, years = years)
    ogtt <- nhs_tsv("ogtt", items = "Laboratory", cat = F, years = years)
    d <- nhs_read(diq, "diq010:told", ghb, "lbxgh:HbA1c", gluam, "lbxglusi,lbdglusi:fglu", biopro, "lbdsglsi:glu1", 
        l10_2_b, "lb2glusi:glu2", l40_2_b, "lb2sglsi:glu3", ogtt, "lbdgltsi:ogtt2", cat = F, lower_cd = TRUE)
    if (cat) 
        message("Conditions for DM")
    if ("told" %in% colnames(d)) {
        if (isTRUE(told) | is.character(told)) {
            if (cat) 
                cat("\ntold")
            d$DM_told[d$told == "yes"] <- 1
            d$DM_told[d$told != "yes"] <- 0
        }
        if (is.character(told)) {
            d <- drop_col(d, "told")
            col_rename(d) <- paste0("DM_told:", told)
            var_told <- told
        }
        else if (isTRUE(told)) 
            var_told <- "DM_told"
        else var_told <- c()
    }
    else {
        told <- FALSE
        var_told <- c()
    }
    if ("HbA1c" %in% colnames(d)) {
        if (isTRUE(HbA1c) | is.character(HbA1c)) {
            if (cat) 
                cat("\nHbA1c")
            ck1 <- d$HbA1c >= 6.5
            ck0 <- d$HbA1c < 6.5
            d$DM_HbA1c[ck1] <- 1
            d$DM_HbA1c[ck0] <- 0
        }
        if (is.character(HbA1c)) {
            col_rename(d) <- paste0("DM_HbA1c:", HbA1c)
            var_HbA1c <- HbA1c
        }
        else if (isTRUE(HbA1c)) 
            var_HbA1c <- "DM_HbA1c"
        else var_HbA1c <- c()
    }
    else {
        HbA1c <- FALSE
        var_HbA1c <- c()
    }
    if ("fglu" %in% colnames(d)) {
        if (isTRUE(fast_glu) | is.character(fast_glu)) {
            if (cat) 
                cat("\nfast_glu")
            CK1 <- d$fglu >= 7
            CK0 <- d$fglu < 7
            d$DM_fast_glu[CK1] <- 1
            d$DM_fast_glu[CK0] <- 0
            d$IFG[d$fglu >= 6.1100000000000003 & d$fglu < 7] <- "IFG"
        }
        if (is.character(fast_glu)) {
            col_rename(d) <- paste0("DM_fast_glu:", fast_glu)
            var_fast_glu <- fast_glu
        }
        else if (isTRUE(fast_glu)) 
            var_fast_glu <- "DM_fast_glu"
        else var_fast_glu <- c()
    }
    else {
        fast_glu <- FALSE
        var_fast_glu <- c()
    }
    if (any(c("glu1", "glu2", "glu3") %in% colnames(d))) {
        if (isTRUE(rand_glu) | is.character(rand_glu)) {
            if (cat) 
                cat("\nrand_glu")
            if ("glu1" %in% colnames(d)) {
                d$DMrand1[d$glu1 >= 11.1] <- 1
                d$DMrand1[d$glu1 < 11.1] <- 0
            }
            if ("glu2" %in% colnames(d)) {
                d$DMrand2[d$glu2 >= 11.1] <- 1
                d$DMrand2[d$glu2 < 11.1] <- 0
            }
            if ("glu3" %in% colnames(d)) {
                d$DMrand3[d$glu3 >= 11.1] <- 1
                d$DMrand3[d$glu3 < 11.1] <- 0
            }
            d$DM_rand <- ifelse(row.sums(d[, grepl("DMrand", colnames(d)), drop = FALSE]) > 0, 1, 0)
        }
        if (is.character(rand_glu)) {
            col_rename(d) <- paste0("DM_rand:", rand_glu)
            var_rand_glu <- rand_glu
        }
        else if (isTRUE(rand_glu)) 
            var_rand_glu <- "DM_rand"
        else var_rand_glu <- c()
    }
    else {
        rand_glu <- FALSE
        var_rand_glu <- c()
    }
    if ("ogtt2" %in% colnames(d)) {
        if (isTRUE(OGTT2) | is.character(OGTT2)) {
            if (cat) 
                cat("\nOGTT2")
            d$DM_ogtt2[d$ogtt2 >= 11.1] <- 1
            d$DM_ogtt2[d$ogtt2 < 11.1] <- 0
            d$IGT[d$ogtt2 >= 7.7000000000000002 & d$ogtt2 < 11.1] <- "IGT"
        }
        if (is.character(OGTT2)) {
            col_rename(d) <- paste0("DM_ogtt2:", OGTT2)
            var_OGTT2 <- OGTT2
        }
        else if (isTRUE(OGTT2)) 
            var_OGTT2 <- "DM_ogtt2"
        else var_OGTT2 <- c()
    }
    else {
        OGTT2 <- FALSE
        var_OGTT2 <- c()
    }
    if (isTRUE(drug) | is.character(drug)) {
        if (cat) 
            cat("\nantidiabetic agents")
        d <- drug_anti.Diabetic(d, take_drug = "DMdrug", dup.take.drug = "remove", yes.code = 1, no.code = 0, 
            other.code = 0)
        d$DM_drug[d$DMdrug == 1] <- 1
        d$DM_drug[d$DMdrug != 1] <- 0
        if (is.character(drug)) {
            col_rename(d) <- paste0("DM_drug:", drug)
            var_drug <- drug
        }
        else if (isTRUE(drug)) 
            var_drug <- "DM_drug"
        else var_drug <- c()
    }
    else var_drug <- c()
    var_calculate <- c(var_told, var_HbA1c, var_fast_glu, var_OGTT2, var_rand_glu, var_drug)
    d$DM <- ifelse(row.sums(d[, set::and(var_calculate, colnames(d)), drop = FALSE]) > 0, "DM", "no")
    if ("IFG" %in% colnames(d)) {
        d$DM[d$DM %in% c(0, "no") & d$IFG %in% "IFG"] <- "IFG"
        ck_IFG <- d$DM %in% "IFG"
    }
    if ("IGT" %in% colnames(d)) {
        d$DM[d$DM %in% c(0, "no") & d$IGT %in% "IGT"] <- "IGT"
        if ("IFG" %in% colnames(d)) {
            d$DM[ck_IFG & d$DM %in% "IGT"] <- "IFG&IGT"
        }
    }
    if (DM1) {
        ck <- d$DM == "DM"
        d$DM[ck] <- 1
        d$DM[!ck] <- 0
    }
    if (!DM1) {
        value <- set::and(colnames(d), c(var_told, var_HbA1c, var_fast_glu, var_OGTT2, var_rand_glu, 
            var_drug))
        d1 <- d[, value]
        ck <- d1 == 1
        d1[ck] <- "DM"
        d1[!ck] <- "no"
        d[, value] <- d1
    }
    if (exclude_Pregnant) {
        d <- diag_Pregnant(d)
        d$DM[d$Pregnant == "yes"] <- NA
    }
    var <- c("seqn", "Year", "DM")
    if (is.character(told)) 
        append(var) <- told
    if (is.character(HbA1c)) 
        append(var) <- HbA1c
    if (is.character(fast_glu)) 
        append(var) <- fast_glu
    if (is.character(OGTT2)) 
        append(var) <- OGTT2
    if (is.character(rand_glu)) 
        append(var) <- rand_glu
    if (is.character(drug)) 
        append(var) <- drug
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Familial.Hypercholesterolemia` [exported]

```r
function (data, years, class = TRUE, score = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (mcq <- nhs_tsv("mcq", years = years, cat = FALSE))
    d <- db_demo(db_HemalBiochemistry(diag_PAD(diag_stroke(diag_heart.attack(diag_angina(diag_coronary.heart.disease(nhs_read(mcq, 
        "mcq300a:relative.early.heart.attack", "seqn", cat = FALSE, lower_cd = TRUE), coronary.heart.disease.Age = TRUE, 
        join = "full"), angina.Age = TRUE, join = "full"), heart.attack.Age = TRUE, join = "full"), stroke.Age = TRUE, 
        join = "full"), join = "full"), ldl_cholesterol_mmol.L = "ldl"), sex = TRUE, ageyr = "PAD.Age")
    if ("relative.early.heart.attack" %in% colnames(d)) {
        message("Family history")
        cat("First-degree relative with known premature heart attack or angina\n")
        d$FH_relative.early.heart.attack <- ifelse(d$relative.early.heart.attack == "yes", 1, 0)
    }
    message("Clinical history")
    cat("    premature coronary artery disease:\n")
    if ("coronary.heart.disease" %in% colnames(d)) {
        cat(crayon::blue("        coronary heart disease\n"))
        d$cli_cad_coronary.heart.disease <- ifelse(d$coronary.heart.disease == "yes", 0, 0)
        ck <- (d$coronary.heart.disease.Age < 55 & d$sex == "Male") | (d$coronary.heart.disease.Age < 
            60 & d$sex == "Female")
        d$cli_cad_coronary.heart.disease[ck] <- 1
    }
    if ("angina" %in% colnames(d)) {
        cat(crayon::blue("        angina\n"))
        d$cli_cad_angina <- ifelse(d$angina == "yes", 0, 0)
        ck <- (d$angina.Age < 55 & d$sex == "Male") | (d$angina.Age < 60 & d$sex == "Female")
        d$cli_cad_angina[ck] <- 1
    }
    if ("heart.attack" %in% colnames(d)) {
        cat(crayon::blue("        heart attack\n"))
        d$cli_cad_heart.attack <- ifelse(d$heart.attack == "yes", 0, 0)
        ck <- (d$heart.attack.Age < 55 & d$sex == "Male") | (d$heart.attack.Age < 60 & d$sex == "Female")
        d$cli_cad_heart.attack[ck] <- 1
    }
    d$FHcli_coronary.artery.disease <- ifelse(row.sums(d[, grepl("cli_cad_", colnames(d)), drop = FALSE]) >= 
        1, 2, 0)
    cat("    premature cerebral or peripheral vascular disease:\n")
    if ("stroke" %in% colnames(d)) {
        cat(crayon::blue("        stroke\n"))
        d$cli_vd_1_stroke <- ifelse(d$stroke == "yes", 0, 0)
        ck <- (d$stroke.Age < 55 & d$sex == "Male") | (d$stroke.Age < 60 & d$sex == "Female")
        d$cli_vd_1_stroke[ck] <- 1
    }
    if ("PAD" %in% colnames(d)) {
        cat(crayon::blue("        PAD\n"))
        d$cli_vd_2_PAD <- ifelse(d$PAD == "yes", 0, 0)
        ck <- (d$PAD.Age < 55 & d$sex == "Male") | (d$PAD.Age < 60 & d$sex == "Female")
        d$cli_vd_2_PAD[ck] <- 1
    }
    d$FHcli_vascular.disease <- ifelse(row.sums(d[, grepl("cli_vd_", colnames(d)), drop = FALSE]) >= 
        1, 1, 0)
    d$FH_cli <- d$FHcli_coronary.artery.disease
    d$FH_cli[d$FHcli_coronary.artery.disease < d$FHcli_vascular.disease] <- 1
    d$FH_cli[is.na(d$FH_cli)] <- d$FHcli_vascular.disease[is.na(d$FH_cli)]
    message("density lipoproteincholesterol")
    if ("ldl" %in% colnames(d)) {
        cat("        8.5<=  : 8\n")
        cat("        6.5-8.5: 5\n")
        cat("        5.0-6.5: 3\n")
        cat("        4.0-5.0: 1\n")
        cat("           <4.0: 0\n")
        bu_x <- d$ldl
        d$FH_LDL[bu("[8.5 ,    )")] <- 8
        d$FH_LDL[bu("[6.5 , 8.5)")] <- 5
        d$FH_LDL[bu("[5.0 , 6.5)")] <- 3
        d$FH_LDL[bu("[4.0 , 5.0)")] <- 1
        d$FH_LDL[bu("[    , 4.0)")] <- 0
    }
    d$FH_score <- row.sums(d[, grepl("FH_", colnames(d)), drop = FALSE])
    bu_x <- d$FH_score
    d$FH_class[bu("(8 ,  ]")] <- "definite"
    d$FH_class[bu("[6 , 8]")] <- "probable"
    d$FH_class[bu("[3 , 5]")] <- "possible"
    d$FH_class[bu("(  , 2]")] <- "no-possible"
    d <- d[, c("seqn", "Year", "FH_score", "FH_class")]
    if (!score) 
        d <- drop_col(d, "FH_score")
    if (!class) 
        d <- drop_col(d, "FH_class")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Fibrillation` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    diag_icd10("fibril", data = data, colname = "Fibrillation", Year = Year, years = years)
}
```

## `diag_Hyperlipidemia` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_demo(drug_anti.Hyperlipidemic(db_HemalBiochemistry(years = years, fast_triglyceride_mg.dl = "TG150", 
        fast_total_cholesterol_mg.dl = "TC200", ldl_cholesterol_mg.dl = "LDL130", hdl_cholesterol_mg.dl = "HDL4050", 
        Year = TRUE), take_drug = "lipdrug", dup.take.drug = "remove", yes.code = 1, no.code = 0, other.code = 0), 
        sex = TRUE, psu_strat = FALSE)
    if ("TG150" %in% colnames(d)) 
        d$TG150 <- ifelse(d$TG150 >= 150, 1, 0)
    if ("TC200" %in% colnames(d)) 
        d$TC200 <- ifelse(d$TC200 >= 200, 1, 0)
    if ("LDL130" %in% colnames(d)) 
        d$LDL130 <- ifelse(d$LDL130 >= 130, 1, 0)
    if ("HDL4050" %in% colnames(d)) {
        ck <- (d$sex == "Male" & d$HDL4050 < 40) | (d$sex == "Female" & d$HDL4050 < 50)
        d$HDL4050 <- ifelse(ck, 1, 0)
    }
    d <- drop_col(d, "sex")
    d$Hyperlipidemia <- ifelse(row.sums(d[, set::and(c("TG150", "TC200", "HDL4050", "LDL130", "lipdrug"), 
        colnames(d)), drop = F]) > 0, 1, 0)
    d <- d[, c("seqn", "Year", "Hyperlipidemia")]
    if (!yes1) 
        yes1(d) <- "Hyperlipidemia"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Hypertension` [exported]

```r
function (data, years, told = TRUE, drug = TRUE, bpx = TRUE, method = c("mean", "times"), systolic = 140, 
    diastolic = 90, n = 3, component = FALSE, yes1 = FALSE, cat = TRUE, Year = FALSE, join = "left") 
{
    method <- match.arg(method)
    years <- data_years(data, years)
    (bpx_tsv <- nhs_tsv("bpx", "!~bpx0_j|bpxo_j", years = years, cat = FALSE))
    (bpq <- nhs_tsv("bpq", years = years, cat = FALSE))
    d <- nhs_read(bpx_tsv, "bpxodi1,bpxdi1:bpxdi1", "bpxodi2,bpxdi2:bpxdi2", "bpxodi3,bpxdi3:bpxdi3", 
        "bpxodi4,bpxdi4:bpxdi4", "bpxosy1,bpxsy1:bpxsy1", "bpxosy2,bpxsy2:bpxsy2", "bpxosy3,bpxsy3:bpxsy3", 
        "bpxosy4,bpxsy4:bpxsy4", bpq, "bpq020", "bpq030", "bpq040a,bpq150:bpq040a", lower_cd = TRUE, 
        cat = FALSE)
    if (isTRUE(told) | is.character(told)) {
        if (cat) 
            cat("told")
        d$bpq <- ifelse(row.sums(d[, c("bpq020", "bpq030", "bpq040a")] == "yes") > 0, 1, 0)
    }
    if (is.character(told)) {
        col_rename(d) <- paste0("bpq:", told)
        var_told <- told
    }
    else if (isTRUE(told)) 
        var_told <- "bpq"
    else var_told <- c()
    if (isTRUE(drug) | is.character(drug)) {
        if (cat) 
            cat("\ndrug")
        tsv <- nhs_tsv("bpq", years = years, cat = F)
        if (isTRUE(drug)) 
            var_drug = "bp_drug"
        if (is.character(drug)) 
            var_drug = drug
        di <- nhs_read(tsv, paste0("bpq050a,bpq150:", var_drug), cat = F, Year = F, lower_cd = T)
        di[, var_drug] <- ifelse(di[, var_drug] == "yes", 1, 0)
        d <- dplyr::left_join(d, di, "seqn")
    }
    else {
        var_drug <- NULL
    }
    if (isTRUE(bpx) | is.character(bpx)) {
        if (all(c("bpxsy1", "bpxsy2", "bpxsy3") %in% colnames(d))) {
            if (cat) 
                cat("\nbpx")
            (syvar <- set::and(c("bpxsy1", "bpxsy2", "bpxsy3", "bpxsy4"), colnames(d)))
            (divay <- set::and(c("bpxdi1", "bpxdi2", "bpxdi3", "bpxdi4"), colnames(d)))
            sys <- d[, c(syvar)]
            dia <- d[, c(divay)]
            bp_meassure <- c()
            if (method == "times") {
                sys <- sys >= systolic
                dia <- dia >= diastolic
                sysdia <- cbind(sys, dia)
                for (i in 1:ncol(sys)) {
                  bpxi <- paste0(c("bpxsy", "bpxdi"), c(i, i))
                  eval(parse(text = sprintf("d$bpxtest%s <- ifelse(row.sums(sysdia[,bpxi])>0,1,0)", i)))
                }
                d$bpx <- ifelse(row.sums(d[, grepl("bpxtest", colnames(d))]) >= ifelse(length(syvar) == 
                  3, 2, n), 1, 0)
                if (component) 
                  bp_meassure <- c(divay, syvar)
            }
            else if (method == "mean") {
                zero4 <- row.sums(dia == 0) == length(syvar)
                dia[dia == 0] <- NA
                sys_number <- row.sums(!is.na(sys))
                dia_number <- row.sums(!is.na(dia))
                ck <- sys_number == 1
                d$bpxsar[ck] <- row.sums(sys[ck, ])
                ck <- dia_number == 1
                d$bpxdar[ck] <- row.sums(dia[ck, ])
                ck <- sys_number > 1
                d$bpxsar[ck] <- sapply(as.data.frame(t(sys[ck, ])), function(i) mean(do::complete.data(i)[-1]))
                ck <- dia_number > 1
                d$bpxdar[ck] <- sapply(as.data.frame(t(dia[ck, ])), function(i) mean(do::complete.data(i)[-1]))
                d$bpxdar[zero4] <- 0
                d$bpxdarck <- ifelse(d$bpxdar >= diastolic, 1, 0)
                d$bpxsarck <- ifelse(d$bpxsar >= systolic, 1, 0)
                d$bpx <- ifelse(row.sums(d[, c("bpxdarck", "bpxsarck")]) >= 1, 1, 0)
                if (component) 
                  bp_meassure <- c("bpxdar", "bpxsar")
            }
        }
        else bpx <- FALSE
    }
    if (is.character(bpx)) {
        col_rename(d) <- paste0("bpx:", bpx)
        var_bpx <- bpx
    }
    else if (isTRUE(bpx)) 
        var_bpx <- "bpx"
    else var_bpx <- c()
    d$Hypertension <- ifelse(row.sums(d[, c(var_told, var_drug, var_bpx), drop = FALSE]) > 0, 1, 0)
    if (!yes1) 
        yes1(d) <- c("Hypertension", var_told, var_drug, var_bpx)
    var_final <- c("seqn", "Year", "Hypertension")
    if (is.character(told)) 
        append(var_final) <- told
    if (is.character(drug)) 
        append(var_final) <- drug
    if (is.character(bpx)) 
        append(var_final) <- bpx
    if (component) 
        append(var_final) <- bp_meassure
    d <- d[, var_final]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_MAFLD` [exported]

```r
function (data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, CAP.cutoff = 248, above.equal = FALSE, 
    cat = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (cat) 
        cat("\nLiver steatosis [controlled attenuation parameter (CAP)]")
    tsv <- nhs_tsv("lux", cat = FALSE, years = years)
    if (length(tsv) == 0) {
        if (!missing(data)) 
            return(data)
        return()
    }
    d <- nhs_read(tsv, "luxcapm", cat = FALSE)
    d$steatosis <- ifelse(d$luxcapm > CAP.cutoff, 1, 0)
    if (above.equal) 
        d$steatosis <- ifelse(d$luxcapm >= CAP.cutoff, 1, 0)
    if (cat) 
        cat("\nBMI")
    d <- db_demo(db_bodyMeasure(d, BMI_kg.m2 = "BMI0", waist_circumference_cm = "waist"), eth3 = "eth")
    ck.Asian <- grepl("Asian", d$eth, TRUE)
    d$BMI <- ifelse(d$BMI0 >= 25, 1, 0)
    d$BMI[ck.Asian] <- ifelse(d$BMI0[ck.Asian] >= 23, 1, 0)
    if (cat) 
        cat("\nDM")
    d <- diag_DM(d, told = TRUE, drug = TRUE, HbA1c = FALSE, fast_glu = FALSE, OGTT2 = FALSE, rand_glu = FALSE, 
        cat = FALSE)
    d$DM <- ifelse(grepl("DM", d$DM), 1, 0)
    if (cat) 
        cat("\nmetabolic dysfunction")
    if (cat) 
        cat("\n    1.waist")
    d <- db_demo(d, sex = TRUE)
    d$sex <- tolower(d$sex)
    d$waist <- ifelse((d$sex == "male" & d$waist >= 102) | (d$sex == "female" & d$waist >= 88), 1, 0)
    d$waist[ck.Asian] <- ifelse((d$sex == "male" & d$waist >= 90) | (d$sex == "female" & d$waist >= 80), 
        1, 0)[ck.Asian]
    if (cat) 
        cat("\n    2.Hypertension")
    d <- diag_Hypertension(d, method = "mean", systolic = 130, diastolic = 85, cat = FALSE)
    d$Hypertension <- ifelse(d$Hypertension == "yes", 1, 0)
    if (cat) 
        cat("\n    3.TG")
    d <- drug_anti.Hyperlipidemic(db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "TG", hdl_cholesterol_mmol.L = "hdl", 
        hs_C_reactive_protein_mg.L = "hs_CRP"), take_drug = "lipid", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    d$TG <- ifelse(d$TG >= 1.7 | d$lipid == 1, 1, 0)
    if (cat) 
        cat("\n    4.HDL")
    d$hdl <- ifelse((d$sex == "male" & d$hdl < 1) | (d$sex == "female" & d$hdl < 1.3), 1, 0)
    d <- drug_niacin(d, take_drug = "niacin", dup.take.drug = "remove", yes.code = 1, no.code = 0, other.code = 0)
    d$hdl <- ifelse(d$hdl == 1 | d$niacin == 1, 1, 0)
    if (cat) 
        cat("\n    5.preDM")
    d <- diag_preDM(d, cat = F)
    d$preDM <- ifelse(d$preDM == "yes", 1, 0)
    if (cat) 
        cat("\n    6.HOMA")
    d <- dex_HOMA(d, IS = F, beta = F)
    d$HOMA_IR <- ifelse(d$HOMA_IR >= 2.5, 1, 0)
    if (cat) 
        cat("\n    7.hs_CRP")
    d$hs_CRP <- ifelse(d$hs_CRP > 2, 1, 0)
    met_var <- c("waist", "Hypertension", "TG", "hdl", "preDM", "HOMA_IR", "hs_CRP")
    ck <- (d$BMI0 < 25 & !ck.Asian) | (d$BMI0 < 23 & ck.Asian)
    d$metabolic.dysfunction <- ifelse(ck & row.sums(d[, met_var]) >= 2, 1, 0)
    d$second.condition <- ifelse(row.sums(d[, c("BMI", "DM", "metabolic.dysfunction")]) >= 1, 1, 0)
    d$MAFLD <- ifelse(row.sums(d[, c("steatosis", "second.condition")], na.rm = FALSE) == 2, "yes", "no")
    var <- c("seqn", "Year", "MAFLD")
    if (steatosis) 
        var <- c(var, "steatosis")
    if (second3) 
        var <- c(var, "BMI", "DM", "metabolic.dysfunction")
    if (met) 
        var <- c(var, met_var)
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_MAFLD.FLI` [exported]

```r
function (data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, cutoff.FLI = NULL, cat = TRUE, 
    Year = FALSE, join = "left") 
{
    if (is.null(cutoff.FLI)) 
        stop("<U+8BF7><U+9605><U+8BFB><U+6587><U+732E><U+FF0C><U+627E><U+5230>cutoff<U+7528><U+4E8E><U+8BCA><U+65AD><U+809D><U+7EA4><U+7EF4><U+5316><U+7684>cutoff<U+FF0C><U+5E76><U+8D4B><U+503C><U+7ED9>cutoff.FLI<U+FF0C><U+4F8B><U+5982>cutoff.FLI=60")
    years <- data_years(data, years)
    if (cat) 
        cat("\nLiver steatosis [controlled attenuation parameter (FLI)]")
    d <- dex_FLI(Year = T, years = years)
    d$steatosis <- ifelse(d$FLI >= cutoff.FLI, 1, 0)
    if (cat) 
        cat("\nBMI")
    d <- db_demo(db_bodyMeasure(d, BMI_kg.m2 = "BMI0", waist_circumference_cm = "waist"), eth3 = "eth")
    ck.Asian <- grepl("Asian", d$eth, TRUE)
    d$BMI <- ifelse(d$BMI0 >= 25, 1, 0)
    d$BMI[ck.Asian] <- ifelse(d$BMI0[ck.Asian] >= 23, 1, 0)
    if (cat) 
        cat("\nDM")
    d <- diag_DM(d, told = TRUE, drug = TRUE, HbA1c = FALSE, fast_glu = FALSE, OGTT2 = FALSE, rand_glu = FALSE, 
        cat = FALSE)
    d$DM <- ifelse(grepl("DM", d$DM), 1, 0)
    if (cat) 
        cat("\nmetabolic dysfunction")
    if (cat) 
        cat("\n    1.waist")
    d <- db_demo(d, sex = TRUE)
    d$sex <- tolower(d$sex)
    d$waist <- ifelse((d$sex == "male" & d$waist >= 102) | (d$sex == "female" & d$waist >= 88), 1, 0)
    d$waist[ck.Asian] <- ifelse((d$sex == "male" & d$waist >= 90) | (d$sex == "female" & d$waist >= 80), 
        1, 0)[ck.Asian]
    if (cat) 
        cat("\n    2.Hypertension")
    d <- diag_Hypertension(d, method = "mean", systolic = 130, diastolic = 85, cat = FALSE)
    d$Hypertension <- ifelse(d$Hypertension == "yes", 1, 0)
    if (cat) 
        cat("\n    3.TG")
    d <- drug_anti.Hyperlipidemic(db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "TG", hdl_cholesterol_mmol.L = "hdl", 
        hs_C_reactive_protein_mg.L = "hs_CRP"), take_drug = "lipid", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    d$TG <- ifelse(d$TG >= 1.7 | d$lipid == 1, 1, 0)
    if (cat) 
        cat("\n    4.HDL")
    d$hdl <- ifelse((d$sex == "male" & d$hdl < 1) | (d$sex == "female" & d$hdl < 1.3), 1, 0)
    d <- drug_niacin(d, take_drug = "niacin", dup.take.drug = "remove", yes.code = 1, no.code = 0, other.code = 0)
    d$hdl <- ifelse(d$hdl == 1 | d$niacin == 1, 1, 0)
    if (cat) 
        cat("\n    5.preDM")
    d <- diag_preDM(d, cat = F)
    d$preDM <- ifelse(d$preDM == "yes", 1, 0)
    if (cat) 
        cat("\n    6.HOMA")
    d <- dex_HOMA(d, IS = F, beta = F)
    d$HOMA_IR <- ifelse(d$HOMA_IR >= 2.5, 1, 0)
    if (cat) 
        cat("\n    7.hs_CRP")
    if ("hs_CRP" %in% colnames(d)) {
        d$hs_CRP <- ifelse(d$hs_CRP > 2, 1, 0)
    }
    else {
        d$hs_CRP <- 0
    }
    met_var <- c("waist", "Hypertension", "TG", "hdl", "preDM", "HOMA_IR", "hs_CRP")
    ck <- (d$BMI0 < 25 & !ck.Asian) | (d$BMI0 < 23 & ck.Asian)
    d$metabolic.dysfunction <- ifelse(ck & row.sums(d[, met_var]) >= 2, 1, 0)
    d$second.condition <- ifelse(row.sums(d[, c("BMI", "DM", "metabolic.dysfunction")]) >= 1, 1, 0)
    d$MAFLD <- ifelse(row.sums(d[, c("steatosis", "second.condition")], na.rm = FALSE) == 2, "yes", "no")
    var <- c("seqn", "Year", "MAFLD")
    if (steatosis) 
        var <- c(var, "steatosis")
    if (second3) 
        var <- c(var, "BMI", "DM", "metabolic.dysfunction")
    if (met) 
        var <- c(var, met_var)
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_MAFLD.usFLI` [exported]

```r
function (data, years, steatosis = FALSE, second3 = FALSE, met = FALSE, cutoff.usFLI = NULL, cat = TRUE, 
    Year = FALSE, join = "left") 
{
    if (is.null(cutoff.usFLI)) 
        stop("<U+8BF7><U+9605><U+8BFB><U+6587><U+732E><U+FF0C><U+627E><U+5230>cutoff<U+7528><U+4E8E><U+8BCA><U+65AD><U+809D><U+7EA4><U+7EF4><U+5316><U+7684>cutoff<U+FF0C><U+5E76><U+8D4B><U+503C><U+7ED9>cutoff.usFLI<U+FF0C><U+4F8B><U+5982>cutoff.usFLI=60")
    years <- data_years(data, years)
    if (cat) 
        cat("\nLiver steatosis [controlled attenuation parameter (usFLI)]")
    d <- dex_usFLI(Year = T, years = years)
    d$steatosis <- ifelse(d$usFLI >= cutoff.usFLI, 1, 0)
    if (cat) 
        cat("\nBMI")
    d <- db_demo(db_bodyMeasure(d, BMI_kg.m2 = "BMI0", waist_circumference_cm = "waist"), eth3 = "eth")
    ck.Asian <- grepl("Asian", d$eth, TRUE)
    d$BMI <- ifelse(d$BMI0 >= 25, 1, 0)
    d$BMI[ck.Asian] <- ifelse(d$BMI0[ck.Asian] >= 23, 1, 0)
    if (cat) 
        cat("\nDM")
    d <- diag_DM(d, told = TRUE, drug = TRUE, HbA1c = FALSE, fast_glu = FALSE, OGTT2 = FALSE, rand_glu = FALSE, 
        cat = FALSE)
    d$DM <- ifelse(grepl("DM", d$DM), 1, 0)
    if (cat) 
        cat("\nmetabolic dysfunction")
    if (cat) 
        cat("\n    1.waist")
    d <- db_demo(d, sex = TRUE)
    d$sex <- tolower(d$sex)
    d$waist <- ifelse((d$sex == "male" & d$waist >= 102) | (d$sex == "female" & d$waist >= 88), 1, 0)
    d$waist[ck.Asian] <- ifelse((d$sex == "male" & d$waist >= 90) | (d$sex == "female" & d$waist >= 80), 
        1, 0)[ck.Asian]
    if (cat) 
        cat("\n    2.Hypertension")
    d <- diag_Hypertension(d, method = "mean", systolic = 130, diastolic = 85, cat = FALSE)
    d$Hypertension <- ifelse(d$Hypertension == "yes", 1, 0)
    if (cat) 
        cat("\n    3.TG")
    d <- drug_anti.Hyperlipidemic(db_HemalBiochemistry(d, fast_triglyceride_mmol.L = "TG", hdl_cholesterol_mmol.L = "hdl", 
        hs_C_reactive_protein_mg.L = "hs_CRP"), take_drug = "lipid", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    d$TG <- ifelse(d$TG >= 1.7 | d$lipid == 1, 1, 0)
    if (cat) 
        cat("\n    4.HDL")
    d$hdl <- ifelse((d$sex == "male" & d$hdl < 1) | (d$sex == "female" & d$hdl < 1.3), 1, 0)
    d <- drug_niacin(d, take_drug = "niacin", dup.take.drug = "remove", yes.code = 1, no.code = 0, other.code = 0)
    d$hdl <- ifelse(d$hdl == 1 | d$niacin == 1, 1, 0)
    if (cat) 
        cat("\n    5.preDM")
    d <- diag_preDM(d, cat = F)
    d$preDM <- ifelse(d$preDM == "yes", 1, 0)
    if (cat) 
        cat("\n    6.HOMA")
    d <- dex_HOMA(d, IS = F, beta = F)
    d$HOMA_IR <- ifelse(d$HOMA_IR >= 2.5, 1, 0)
    if (cat) 
        cat("\n    7.hs_CRP")
    d$hs_CRP <- ifelse(d$hs_CRP > 2, 1, 0)
    met_var <- c("waist", "Hypertension", "TG", "hdl", "preDM", "HOMA_IR", "hs_CRP")
    ck <- (d$BMI0 < 25 & !ck.Asian) | (d$BMI0 < 23 & ck.Asian)
    d$metabolic.dysfunction <- ifelse(ck & row.sums(d[, met_var]) >= 2, 1, 0)
    d$second.condition <- ifelse(row.sums(d[, c("BMI", "DM", "metabolic.dysfunction")]) >= 1, 1, 0)
    d$MAFLD <- ifelse(row.sums(d[, c("steatosis", "second.condition")], na.rm = FALSE) == 2, "yes", "no")
    var <- c("seqn", "Year", "MAFLD")
    if (steatosis) 
        var <- c(var, "steatosis")
    if (second3) 
        var <- c(var, "BMI", "DM", "metabolic.dysfunction")
    if (met) 
        var <- c(var, met_var)
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_MASLD.FLI` [exported]

```r
function (data, years, cutoff.FLI = NULL, Year = FALSE, join = "left") 
{
    if (is.null(cutoff.FLI)) 
        stop("<U+8BF7><U+9605><U+8BFB><U+6587><U+732E><U+FF0C><U+627E><U+5230>cutoff<U+7528><U+4E8E><U+8BCA><U+65AD><U+809D><U+7EA4><U+7EF4><U+5316><U+7684>cutoff<U+FF0C><U+5E76><U+8D4B><U+503C><U+7ED9>cutoff.FLI<U+FF0C><U+4F8B><U+5982>cutoff.FLI=60")
    years <- data_years(data, years)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    version <- 1
    (file <- paste0(get_config_path(), "/attach/diag_MASLD.FLI~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        download.file("http://146.56.250.62:3838/data/nhanes-attach/diag_MASLD.FLI~~version-1.txt", file)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    d$steatosis <- ifelse(d$FLI >= cutoff.FLI, 1, 0)
    d <- d %>% mutate(MASLD = case_when(steatosis %in% 1 & cc %in% 1 & oc %in% 0 ~ "MASLD", steatosis %in% 
        1 & cc %in% 1 & oc %in% 1 ~ "MetALD or other combination aetiology", steatosis %in% 1 & cc %in% 
        0 & oc %in% 0 ~ "Cryptogenic SLD", steatosis %in% 1 & cc %in% 0 & oc %in% 1 ~ "Other specific aetiology SLD", 
        steatosis %in% 0 ~ "no", TRUE ~ NA))
    d <- d[, c("Year", "seqn", "MASLD")]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `diag_MASLD.cap` [exported]

```r
function (data, years, cutoff.cap = 248, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    d <- create_diag_MASLD.cap()
    Yu <- paste0(unique(d$Year), collapse = ", ")
    d <- d[d$Year %in% years, ]
    if (nrow(d) == 0) 
        stop(paste0("diag_MASLD.cap", tmcn::toUTF8("<U+4EC5><U+652F><U+6301><U+5E74><U+4EFD>:"), Yu))
    d$steatosis <- ifelse(d$luxcapm >= cutoff.cap, 1, 0)
    d <- d %>% mutate(MASLD = case_when(steatosis %in% 1 & cc %in% 1 & oc %in% 0 ~ "MASLD", steatosis %in% 
        1 & cc %in% 1 & oc %in% 1 ~ "MetALD or other combination aetiology", steatosis %in% 1 & cc %in% 
        0 & oc %in% 0 ~ "Cryptogenic SLD", steatosis %in% 1 & cc %in% 0 & oc %in% 1 ~ "Other specific aetiology SLD", 
        steatosis %in% 0 ~ "no", TRUE ~ NA))
    d <- d[, c("Year", "seqn", "MASLD")]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `diag_MASLD.usFLI` [exported]

```r
function (data, years, cutoff.usFLI = 30, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    version <- 1
    (file <- paste0(get_config_path(), "/attach/diag_MASLD.usFLI~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        download.file("http://146.56.250.62:3838/data/nhanes-attach/diag_MASLD.usFLI~~version-1.txt", 
            file)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    d$steatosis <- ifelse(d$usFLI >= cutoff.usFLI, 1, 0)
    d <- d %>% mutate(MASLD = case_when(steatosis %in% 1 & cc %in% 1 & oc %in% 0 ~ "MASLD", steatosis %in% 
        1 & cc %in% 1 & oc %in% 1 ~ "MetALD or other combination aetiology", steatosis %in% 1 & cc %in% 
        0 & oc %in% 0 ~ "Cryptogenic SLD", steatosis %in% 1 & cc %in% 0 & oc %in% 1 ~ "Other specific aetiology SLD", 
        steatosis %in% 0 ~ "no", TRUE ~ NA))
    d <- d[, c("Year", "seqn", "MASLD")]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `diag_MetS` [exported]

```r
function (data, years, methods = c("ATP", "IDF2006", "IDF2009", "Harm"), component = FALSE, yes1 = FALSE, 
    join = "left", Year = FALSE, cat = TRUE) 
{
    methods <- match.arg(methods)
    years <- data_years(data, years)
    if (cat) 
        cat("Loading data\n\n")
    if (methods == "ATP") {
        demo <- nhs_tsv("demo", years = years, cat = FALSE)
        gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu", items = "Laboratory", years = years, cat = FALSE)
        hdl <- nhs_tsv("lab13\\.|l13_b|l13_c|hdl", years = years, cat = FALSE)
        tg <- nhs_tsv("lab18\\.|l40_b|l40_c|biopro", years = years, cat = FALSE)
        bmx <- nhs_tsv("bmx", years = years, cat = FALSE)
        (bpx <- nhs_tsv("bpx", "!~bpxo_j", years = years, cat = FALSE))
        n0 <- diag_Pregnant(db_HemalBiochemistry(nhs_read(demo, "riagendr:sex", "ridageyr:age", "ridreth1", 
            bmx, "bmxwaist:waist", "bmxht:height", bpx, "bpxdi1,bpxodi1:bpxdi1", "bpxdi2,bpxodi2:bpxdi2", 
            "bpxdi3,bpxodi3:bpxdi3", "bpxdi4:bpxdi4", "bpxsy1,bpxosy1:bpxsy1", "bpxsy2,bpxosy2:bpxsy2", 
            "bpxsy3,bpxosy3:bpxsy3", "bpxsy4:bpxsy4", lower_cd = TRUE, cat = FALSE), fast_triglyceride_mmol.L = "tg", 
            hdl_cholesterol_mmol.L = "hdl", fast_glucose_mmol.L = "glucose"))
        dibpvar <- set::and(colnames(n0), c("bpxdi1", "bpxdi2", "bpxdi3", "bpxdi4"))
        sibpvar <- set::and(colnames(n0), c("bpxsy1", "bpxsy2", "bpxsy3", "bpxsy4"))
        n0 <- n0[n0$age >= 10, ]
        n0 <- n0[!n0$Pregnant %in% "yes", ]
        if (cat) 
            cat(crayon::red("ATP3\n"))
        if (any(n0$age >= 16)) {
            if (cat) 
                cat(crayon::blue(">=16 years old\n"))
            nr <- n0[n0$age >= 16, ]
            if (cat) 
                cat("    Glucose\n")
            n1 <- drug_anti.Diabetic(nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            n1$glucose <- ifelse(n1$glucose >= 5.5999999999999996, 1, 0)
            nr$glucose <- row.sums(n1[, c("drug", "glucose")])
            nr$glucose <- ifelse(nr$glucose == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "glucose")])) == 2
            nr$glucose[ck] <- NA
            if (cat) 
                cat("    HDL cholesterol\n")
            n1 <- Drug("niacin", data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            ck <- (nr$sex == "male" & n1$hdl < 1) | (nr$sex == "female" & n1$hdl < 1.3)
            n1$hdl[ck] <- 1
            n1$hdl[!ck] <- 0
            nr$hdl <- row.sums(n1[, c("drug", "hdl")])
            nr$hdl <- ifelse(nr$hdl == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "hdl")])) == 2
            nr$hdl[ck] <- NA
            if (cat) 
                cat("    Triglycerides\n")
            n1 <- Drug("fibrate", data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            n1$tg <- ifelse(n1$tg > 1.7, 1, 0)
            nr$tg <- row.sums(n1[, c("drug", "tg")])
            nr$tg <- ifelse(nr$tg == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "tg")])) == 2
            nr$tg[ck] <- NA
            if (cat) 
                cat("    Obesity(Waist)\n")
            ck <- (nr$sex == "male" & nr$waist >= 102) | (nr$sex == "female" & nr$waist >= 88)
            nr$waist <- ifelse(ck, 1, 0)
            if (cat) 
                cat("    Hypertension\n")
            bpx <- nr[, dibpvar] >= 85
            dk <- ifelse(row.sums(bpx) > 0, 1, 0)
            dk[row.sums(is.na(bpx)) == length(dibpvar)] <- NA
            bpx <- nr[, sibpvar] >= 130
            sk <- ifelse(row.sums(bpx) > 0, 1, 0)
            sk[row.sums(is.na(bpx)) == length(sibpvar)] <- NA
            nr$bpx <- ifelse((dk + sk) == 2, 1, 0)
            nr <- drop_col(nr, c(sibpvar, dibpvar))
            n1 <- drug_anti.Hypertensive(data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            nr$bpx <- row.sums(n1[, c("drug", "bpx")])
            nr$bpx <- ifelse(nr$bpx == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "bpx")])) == 2
            nr$bpx[ck] <- NA
            nr$MetS_ATP <- ifelse(row.sums(nr[, c("glucose", "hdl", "tg", "waist", "bpx")]) >= 3, "yes", 
                "no")
            tb <- table(nr$MetS_ATP, useNA = "i")
            if (cat) 
                cat(paste0("  MetS: ", paste0(paste0(names(tb), ":", tb), collapse = ", ")), "\n")
            if (component) {
                d <- nr[, c("seqn", "Year", "MetS_ATP", "glucose", "hdl", "tg", "waist", "bpx")]
                col_rename(d) <- c("glucose:MetS.glucose", "hdl:MetS.hdl", "tg:MetS.tg", "waist:MetS.obesity", 
                  "bpx:MetS.hypertension")
            }
            else {
                d <- nr[, c("seqn", "Year", "MetS_ATP")]
            }
        }
        if (any(n0$age < 16)) {
            if (cat) 
                cat(crayon::blue("10-16 years old\n"))
            nr <- n0[n0$age < 16 & n0$age >= 10, ]
            if (cat) 
                cat("    Glucose\n")
            n1 <- diag_DM(nr, cat = FALSE)
            nr$glucose <- ifelse(n1$DM %=% c("DM", "IFG", "IGT"), 1, 0)
            if (cat) 
                cat("    HDL cholesterol\n")
            Q <- quantile(nr$hdl, 0.050000000000000003, na.rm = TRUE)
            nr$hdl <- ifelse(nr$hdl < Q, 1, 0)
            if (cat) 
                cat("    Triglycerides\n")
            nr <- n0[n0$age < 16, ]
            Q <- quantile(nr$tg, 0.94999999999999996, na.rm = TRUE)
            nr$tg <- ifelse(nr$tg > Q, 1, 0)
            if (cat) 
                cat("    Blood Pressure(adjusted by sex, age and height)\n")
            cutoff <- list(boy_sys = data.frame(`10` = c(115, 116, 117, 119, 121, 122, 123), `11` = c(117, 
                118, 119, 121, 123, 124, 125), `12` = c(119, 120, 122, 123, 125, 127, 127), `13` = c(121, 
                122, 124, 126, 128, 129, 130), `14` = c(124, 125, 127, 128, 130, 132, 132), `15` = c(126, 
                127, 129, 131, 133, 134, 135), check.names = FALSE), boy_dia = data.frame(`10` = c(77, 
                78, 79, 80, 81, 81, 82), `11` = c(78, 78, 79, 80, 81, 82, 82), `12` = c(78, 79, 80, 81, 
                82, 82, 83), `13` = c(79, 79, 80, 81, 82, 83, 83), `14` = c(80, 80, 81, 82, 83, 84, 84), 
                `15` = c(81, 81, 82, 83, 84, 85, 85), check.names = FALSE), girl_sys = data.frame(`10` = c(116, 
                116, 117, 119, 120, 121, 122), `11` = c(118, 118, 119, 121, 122, 123, 124), `12` = c(119, 
                120, 121, 123, 124, 125, 126), `13` = c(121, 122, 123, 124, 126, 127, 128), `14` = c(123, 
                123, 125, 126, 127, 129, 129), `15` = c(124, 125, 126, 127, 129, 130, 131), check.names = FALSE), 
                girl_dia = data.frame(`10` = c(77, 77, 77, 78, 79, 80, 80), `11` = c(78, 78, 78, 79, 
                  80, 81, 81), `12` = c(79, 79, 79, 80, 81, 82, 82), `13` = c(80, 80, 80, 81, 82, 83, 
                  83), `14` = c(81, 81, 81, 82, 83, 84, 84), `15` = c(82, 82, 82, 83, 84, 85, 85), check.names = FALSE))
            for (sexi in c("male", "female")) {
                for (bpi in c("sys", "dia")) {
                  jk <- cutoff[[paste0(ifelse(sexi == "male", "boy_", "girl_"), bpi)]]
                  if (bpi == "sys") 
                    bpvar <- sibpvar
                  else bpvar <- dibpvar
                  for (agei in 10:15) {
                    ck <- nr$sex == sexi & nr$age == agei
                    Q <- quantile(nr$height[ck], c(0.050000000000000003, 0.10000000000000001, 0.25, 0.5, 
                      0.75, 0.90000000000000002, 0.94999999999999996), na.rm = TRUE)
                    for (i in 1:8) {
                      if (i == 1) {
                        ck2 <- ck & nr$height <= Q[1] & !is.na(nr$height)
                        if (bpi == "sys") {
                          nr$sysck[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$sysck[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                        else {
                          nr$diack[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$diack[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                      }
                      else if (i <= 7) {
                        ck2 <- ck & nr$height <= Q[i] & nr$height > Q[i - 1] & !is.na(nr$height)
                        if (bpi == "sys") {
                          nr$sysck[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$sysck[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                        else {
                          nr$diack[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$diack[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                      }
                      else {
                        ck2 <- ck & nr$height > Q[7] & !is.na(nr$height)
                        if (bpi == "sys") {
                          nr$sysck[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$sysck[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                        else {
                          nr$diack[ck2] <- ifelse(row.sums(nr[ck2, bpvar] >= jk[i, as.character(agei)]) > 
                            0, 1, 0)
                          nr$diack[ck2][row.sums(is.na(nr[ck2, bpvar])) == length(dibpvar)] <- NA
                        }
                      }
                    }
                  }
                }
            }
            nr$bpx <- ifelse(row.sums(nr[, c("sysck", "diack")]) > 0, 1, 0)
            nr$bpx[row.sums(is.na(nr[, c("sysck", "diack")])) == 2] <- NA
            nr <- drop_col(nr, c(dibpvar, sibpvar))
            nr$MetS_ATP <- ifelse(row.sums(nr[, c("glucose", "hdl", "tg", "bpx")]) >= 3, "yes", "no")
            tb <- table(nr$MetS_ATP, useNA = "i")
            if (cat) 
                cat(paste0("  MetS: ", paste0(paste0(names(tb), ":", tb), collapse = ", ")), "\n")
            if (component) {
                d2 <- nr[, c("seqn", "Year", "MetS_ATP", "glucose", "hdl", "tg", "bpx")]
                col_rename(d2) <- c("glucose:MetS.glucose", "hdl:MetS.hdl", "tg:MetS.tg", "bpx:MetS.hypertension")
            }
            else {
                d2 <- nr[, c("seqn", "Year", "MetS_ATP")]
            }
            if (any(n0$age >= 16)) {
                d <- plyr::rbind.fill(d, d2)
            }
            else {
                d <- d2
            }
        }
        return_data(data, d, Year, key = "seqn", join = join)
    }
    else if (methods == "IDF2006") {
        d <- diag_DM(drug_niacin(drug_anti.Hyperlipidemic(diag_Hypertension(db_HemalBiochemistry(db_bodyMeasure(db_demo(years = years, 
            Year = TRUE, sex = TRUE, psu_strat = FALSE, lower_cd = TRUE), waist_circumference_cm = "wc", 
            BMI_kg.m2 = "bmi"), fast_triglyceride_mmol.L = "tg", hdl_cholesterol_mmol.L = "hdl", fast_glucose_mmol.L = "glu"), 
            systolic = 130, diastolic = 85, cat = FALSE), take_drug = "drug.lipid", yes.code = 1, no.code = 0, 
            other.code = 0), take_drug = "drug.niacin", yes.code = 1, no.code = 0, other.code = 0), cat = FALSE)
        ck <- (d$bmi > 30) | (d$sex == "male" & d$wc >= 94) | (d$sex == "female" & d$wc >= 80)
        d$centerobesity <- ifelse(ck, 1, 0)
        ck <- (d$drug.lipid == 1) | (d$tg >= 1.7)
        d$IDF_tg <- ifelse(ck, 1, 0)
        ck <- (d$drug.niacin == 1) | (d$sex == "male" & d$hdl < 1.03) | (d$sex == "female" & d$hdl < 
            1.29)
        d$IDF_hdl <- ifelse(ck, 1, 0)
        d$IDF_hb <- ifelse(d$Hypertension == "yes", 1, 0)
        ck <- (d$glu >= 5.5999999999999996) | (d$DM == "DM")
        d$IDF_glu <- ifelse(ck, 1, 0)
        d$plus2 <- ifelse(row.sums(d[, do::left(colnames(d), 4) == "IDF_"]) >= 2, 1, 0)
        d$MetS_IDF.2006 <- ifelse(row.sums(d[, c("centerobesity", "plus2")]) >= 2, "yes", "no")
        if (yes1) 
            d$MetS_IDF.2006 <- ifelse(row.sums(d[, c("centerobesity", "plus2")]) >= 2, 1, 0)
        var <- c("seqn", "Year", "MetS_IDF.2006")
        if (component) {
            var <- c(var, "bmi", "wc", "glu", "tg", "hdl", "Hypertension", "drug.lipid", "drug.niacin", 
                "DM")
        }
        d <- select_col(d, var)
        return_data(data, d, Year, key = "seqn", join = join)
    }
    else if (methods == "IDF2009") {
        demo <- nhs_tsv("demo", years = years, cat = FALSE)
        gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu", items = "Laboratory", years = years, cat = FALSE)
        hdl <- nhs_tsv("lab13\\.|l13_b|l13_c|hdl", years = years, cat = FALSE)
        tg <- nhs_tsv("lab18\\.|l40_b|l40_c|biopro", years = years, cat = FALSE)
        bmx <- nhs_tsv("bmx", years = years, cat = FALSE)
        bpx <- nhs_tsv("bpx", "!~bpxo", years = years, cat = FALSE)
        n0 <- diag_Pregnant(db_HemalBiochemistry(nhs_read(demo, "riagendr:sex", "ridageyr:age", "ridreth1", 
            bmx, "bmxwaist:waist", "bmxht:height", bpx, "bpxdi1,bpxodi1:bpxdi1", "bpxdi2,bpxodi2:bpxdi2", 
            "bpxdi3,bpxodi3:bpxdi3", "bpxdi4:bpxdi4", "bpxsy1,bpxosy1:bpxsy1", "bpxsy2,bpxosy2:bpxsy2", 
            "bpxsy3,bpxosy3:bpxsy3", "bpxsy4:bpxsy4", lower_cd = TRUE, cat = FALSE), fast_triglyceride_mmol.L = "tg", 
            hdl_cholesterol_mmol.L = "hdl", fast_glucose_mmol.L = "glucose"))
        dibpvar <- set::and(colnames(n0), c("bpxdi1", "bpxdi2", "bpxdi3", "bpxdi4"))
        sibpvar <- set::and(colnames(n0), c("bpxsy1", "bpxsy2", "bpxsy3", "bpxsy4"))
        n0 <- n0[n0$age >= 10, ]
        n0 <- n0[!n0$Pregnant %in% "yes", ]
        if (cat) 
            cat(crayon::red("IDF\n"))
        if (any(n0$age >= 16)) {
            if (cat) 
                cat(crayon::blue(">=16 years old\n"))
            nr <- n0[n0$age >= 16, ]
            if (cat) 
                cat("    Glucose\n")
            n1 <- diag_DM(nr, cat = FALSE)
            n1$DM[!is.na(n1$DM) & n1$DM != "DM"] <- 0
            n1$DM[n1$DM == "DM"] <- 1
            n1$DM <- as.numeric(n1$DM)
            n1$glucose <- ifelse(n1$glucose >= 5.5999999999999996, 1, 0)
            nr$glucose <- row.sums(n1[, c("DM", "glucose")])
            nr$glucose <- ifelse(nr$glucose == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("DM", "glucose")])) == 2
            nr$glucose[ck] <- NA
            if (cat) 
                cat("    HDL cholesterol\n")
            n1 <- Drug("niacin", data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            ck <- (nr$sex == "male" & n1$hdl < 1) | (nr$sex == "female" & n1$hdl < 1.3)
            n1$hdl[ck] <- 1
            n1$hdl[!ck] <- 0
            nr$hdl <- row.sums(n1[, c("drug", "hdl")])
            nr$hdl <- ifelse(nr$hdl == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "hdl")])) == 2
            nr$hdl[ck] <- NA
            if (cat) 
                cat("    Triglycerides\n")
            n1 <- Drug("fibrate", data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            n1$tg <- ifelse(n1$tg > 1.7, 1, 0)
            nr$tg <- row.sums(n1[, c("drug", "tg")])
            nr$tg <- ifelse(nr$tg == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "tg")])) == 2
            nr$tg[ck] <- NA
            if (cat) 
                cat("    Obesity(Waist)\n")
            ck <- (nr$sex == "male" & nr$waist >= 94) | (nr$sex == "female" & nr$waist >= 80)
            nr$waist <- ifelse(ck, 1, 0)
            if (cat) 
                cat("    Hypertension\n")
            bpx <- nr[, dibpvar] >= 85
            dk <- ifelse(row.sums(bpx) > 0, 1, 0)
            dk[row.sums(is.na(bpx)) == length(dibpvar)] <- NA
            bpx <- nr[, sibpvar] >= 130
            sk <- ifelse(row.sums(bpx) > 0, 1, 0)
            sk[row.sums(is.na(bpx)) == length(dibpvar)] <- NA
            nr$bpx <- ifelse((dk + sk) == 2, 1, 0)
            nr <- drop_col(nr, c(dibpvar, sibpvar))
            n1 <- drug_anti.Hypertensive(data = nr, take_drug = "drug", dup.take.drug = "remove", yes.code = 1, 
                no.code = 0, other.code = 0)
            nr$bpx <- row.sums(n1[, c("drug", "bpx")])
            nr$bpx <- ifelse(nr$bpx == 0, 0, 1)
            ck <- row.sums(is.na(n1[, c("drug", "bpx")])) == 2
            nr$bpx[ck] <- NA
            nr$MetS_IDF.2009 <- ifelse(row.sums(nr[, c("glucose", "hdl", "tg", "waist", "bpx")]) >= 3, 
                "yes", "no")
            tb <- table(nr$MetS_IDF.2009, useNA = "i")
            if (cat) 
                cat(paste0("  MetS: ", paste0(paste0(names(tb), ":", tb), collapse = ", ")), "\n")
            if (component) {
                d <- nr[, c("seqn", "Year", "MetS_IDF.2009", "glucose", "hdl", "tg", "waist", "bpx")]
                col_rename(d) <- c("glucose:MetS.glucose", "hdl:MetS.hdl", "tg:MetS.tg", "waist:MetS.obesity", 
                  "bpx:MetS.hypertension")
            }
            else {
                d <- nr[, c("seqn", "Year", "MetS_IDF.2009")]
            }
        }
        if (any(n0$age < 16)) {
            if (cat) 
                cat(crayon::blue("10-16 years old\n"))
            nr <- n0[n0$age < 16 & n0$age >= 10, ]
            if (cat) 
                cat("    Glucose\n")
            nr$glucose <- ifelse(nr$glucose > 5.5999999999999996, 1, 0)
            if (cat) 
                cat("    HDL cholesterol\n")
            nr$hdl <- ifelse(nr$hdl < 1.03, 1, 0)
            if (cat) 
                cat("    Triglycerides\n")
            nr$tg <- ifelse(nr$tg >= 1.7, 1, 0)
            if (cat) 
                cat("    Obesity(Waist,Ethnic-specific, BY ridreth1)\n")
            eth <- unique(nr$ridreth1)
            for (i in eth) {
                ck <- nr$ridreth1 == i
                Q <- quantile(nr$waist[ck], 0.90000000000000002, na.rm = T)
                nr$waist[ck] <- ifelse(nr$waist[ck] >= Q, 1, 0)
            }
            if (cat) 
                cat("    Blood Pressure\n")
            bpx <- nr[, dibpvar] >= 85
            dk <- ifelse(row.sums(bpx) > 0, 1, 0)
            dk[row.sums(is.na(bpx)) == length(dibpvar)] <- NA
            bpx <- nr[, sibpvar] >= 135
            sk <- ifelse(row.sums(bpx) > 0, 1, 0)
            sk[row.sums(is.na(bpx)) == length(dibpvar)] <- NA
            nr$bpx <- ifelse((dk + sk) > 0, 1, 0)
            nr$bpx[(is.na(dk) + is.na(sk)) == 2] <- NA
            nr$MetS_IDF.2009 <- ifelse(row.sums(nr[, c("glucose", "hdl", "tg", "waist", "bpx")]) >= 2, 
                "yes", "no")
            nr$MetS_IDF.2009[row.sums(is.na(nr[, c("glucose", "hdl", "tg", "waist", "bpx")])) == 5] <- NA
            tb <- table(nr$MetS_IDF.2009, useNA = "i")
            if (cat) 
                cat(paste0("  MetS: ", paste0(paste0(names(tb), ":", tb), collapse = ", ")), "\n")
            if (component) {
                d2 <- nr[, c("seqn", "Year", "MetS_IDF.2009", "glucose", "hdl", "tg", "waist", "bpx")]
                col_rename(d2) <- c("glucose:MetS.glucose", "hdl:MetS.hdl", "tg:MetS.tg", "waist:MetS.obesity", 
                  "bpx:MetS.hypertension")
            }
            else {
                d2 <- nr[, c("seqn", "Year", "MetS_IDF.2009")]
            }
            if (any(n0$age >= 16)) {
                d <- rbind(d, d2)
            }
            else {
                d <- d2
            }
        }
        return_data(data, d, Year, key = "seqn", join = join)
    }
    else if (methods == "Harm") {
        d <- drug_niacin(drug_fibrates(diag_Hypertension(db_HemalBiochemistry(db_bodyMeasure(db_demo(years = years, 
            Year = TRUE, sex = TRUE, lower_cd = TRUE), waist_circumference_cm = "wc"), fast_triglyceride_mmol.L = "tg", 
            hdl_cholesterol_mmol.L = "hdl", fast_glucose_mg.dl = "glu"), told = FALSE, drug = TRUE, bpx = TRUE, 
            method = "mean", systolic = 130, diastolic = 85, yes1 = 1, cat = FALSE), take_drug = "fibrate", 
            yes.code = 1, no.code = 0, other.code = 0), take_drug = "niacin", yes.code = 1, no.code = 0, 
            other.code = 0)
        ck <- (d$sex == "male" & d$wc >= 102) | (d$sex == "female" & d$wc >= 88)
        d$wc <- ifelse(ck, 1, 0)
        d$tg <- ifelse(d$tg >= 1.7, 1, 0)
        d$tg <- ifelse(row.sums(d[, c("tg", "fibrate")]) >= 1, 1, 0)
        drop_col(d) <- "fibrate"
        ck <- (d$sex == "male" & d$hdl <= 1) | (d$sex == "female" & d$hdl <= 1.3)
        d$hdl <- ifelse(ck, 1, 0)
        d$hdl <- ifelse(row.sums(d[, c("hdl", "niacin")]) >= 1, 1, 0)
        drop_col(d) <- "niacin"
        d$glu <- ifelse(d$glu >= 100, 1, 0)
        d$MetS_Harm <- ifelse(row.sums(d[, c("wc", "tg", "hdl", "Hypertension", "glu")]) >= 3, 1, 0)
        if (!yes1) 
            yes1(d) <- "MetS_Harm"
        if (component) {
            d <- d[, c("seqn", "Year", "MetS_Harm", "glu", "hdl", "tg", "wc", "Hypertension")]
            col_rename(d) <- c("glu:MetS.glucose", "hdl:MetS.hdl", "tg:MetS.tg", "wc:MetS.wc", "Hypertension:MetS.hypertension")
        }
        else {
            d <- d[, c("seqn", "Year", "MetS_Harm")]
        }
        return_data(data, d, Year, key = "seqn", join = join)
    }
}
```

## `diag_NAFLD` [exported]

```r
function (data, years, cap.cutoff = 248, colname = "Nonalcoholic.fatty.liver.disease", Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("lux", cat = FALSE, years = years)
    tsv0(tsv)
    d <- diag_viral.hepatitis(diag_alcohol.associated.liver.disease(nhs_read(tsv, "luxcapm", cat = FALSE), 
        yes1 = TRUE), yes1 = TRUE)
    head(d)
    d$steatosis[d$luxcapm <= cap.cutoff] <- 0
    d$steatosis[d$luxcapm > cap.cutoff] <- 1
    d$ex <- ifelse(row.sums(d[, c("alcohol.associated.liver.disease", "viral.hepatitis")]) > 0, 1, 0)
    d$steatosis[d$ex == 1 & !is.na(d$steatosis)] <- 0
    col_rename(d) <- paste0("steatosis:", colname)
    d <- d[, c("seqn", "Year", colname)]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_OSAS.3` [exported]

```r
function (data, years, Year = FALSE, join = "left", component = F) 
{
    years <- data_years(data, years)
    d <- db_slq(years = years, how_often_do_you_snore = "snore", how_often_do_you_snort_or_stop_breathing = "stop.breath", 
        how_often_feel_overly_sleepy_during_day = "sleepy", Year = T)
    d$snore <- Recode(d$snore, "never::0", "rarely (1-2 nights/week)::0", "rarely - 1-2 nights a week::0", 
        "occasionally (3-4 nights/week)::1", "occasionally - 3-4 nights a week::1", "frequently (5 or more nights/week)::1", 
        "frequently - 5 or more nights a week::1", "NA::", to.numeric = TRUE)
    d$stop.breath <- Recode(d$stop.breath, "never::0", "rarely (1-2 nights/week)::0", "rarely - 1-2 nights a week::0", 
        "occasionally (3-4 nights/week)::1", "occasionally - 3-4 nights a week::1", "frequently - 5 or more nights a week::1", 
        "frequently (5 or more nights/week)::1", "NA::", to.numeric = TRUE)
    d$sleepy <- Recode(d$sleepy, "never::0", "rarely (1 time a month)::0", "rarely - 1 time a month::0", 
        "sometimes (2-4 times a month)::1", "sometimes - 2-4 times a month::1", "often (5-15 times a month)::1", 
        "often- 5-15 times a month::1", "almost always - 16-30 times a month::1", "almost always (16-30 times a month)::1", 
        "NA::", to.numeric = TRUE)
    d$OSAS.3 <- ifelse(row.sums(d[, c("snore", "stop.breath", "sleepy")]) >= 1, "yes", "no")
    var2 <- c("seqn", "Year", "OSAS.3")
    if (component) 
        var2 <- c(var2, "snore", "stop.breath", "sleepy")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_OSAS.3a` [exported]

```r
function (data, years, Year = FALSE, join = "left", component = F) 
{
    years <- data_years(data, years)
    d <- db_slq(years = 2005:2008, how_often_do_you_snore = "snore", how_often_do_you_snort_or_stop_breathing = "stop.breath", 
        how_often_feel_overly_sleepy_during_day = "sleepy", sleep_disorder_sleep_apnea = "apnea", Year = T)
    d$snore <- Recode(d$snore, "never::0", "rarely (1-2 nights/week)::0", "occasionally (3-4 nights/week)::1", 
        "frequently (5 or more nights/week)::1", "NA::", to.numeric = TRUE)
    d$stop.breath <- Recode(d$stop.breath, "never::0", "rarely (1-2 nights/week)::0", "occasionally (3-4 nights/week)::1", 
        "frequently (5 or more nights/week)::1", "NA::", to.numeric = TRUE)
    d$sleepy <- Recode(d$sleepy, "never::0", "rarely (1 time a month)::0", "sometimes (2-4 times a month)::1", 
        "almost always (16-30 times a month)::1", "often (5-15 times a month)::1", "NA::", to.numeric = TRUE)
    d$OSAS.3a <- ifelse(row.sums(d[, c("snore", "stop.breath", "sleepy")]) >= 1, "yes", "no")
    var2 <- c("seqn", "Year", "OSAS.3a")
    if (component) 
        var2 <- c(var2, "snore", "stop.breath", "sleepy")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_OSAS.3ha` [exported]

```r
function (data, years, Year = FALSE, join = "left", component = F) 
{
    years <- data_years(data, years)
    d <- diag_Hypertension(db_slq(years = 2005:2008, how_often_do_you_snore = "snore", how_often_do_you_snort_or_stop_breathing = "stop.breath", 
        how_often_feel_overly_sleepy_during_day = "sleepy", sleep_disorder_sleep_apnea = "apnea", Year = T), 
        cat = F)
    d$snore <- Recode(d$snore, "never::0", "rarely (1-2 nights/week)::0", "occasionally (3-4 nights/week)::1", 
        "frequently (5 or more nights/week)::1", "NA::", to.numeric = TRUE)
    d$stop.breath <- Recode(d$stop.breath, "never::0", "rarely (1-2 nights/week)::0", "occasionally (3-4 nights/week)::1", 
        "frequently (5 or more nights/week)::1", "NA::", to.numeric = TRUE)
    d$sleepy <- Recode(d$sleepy, "never::0", "rarely (1 time a month)::0", "sometimes (2-4 times a month)::1", 
        "almost always (16-30 times a month)::1", "often (5-15 times a month)::1", "NA::", to.numeric = TRUE)
    d$Hypertension <- Recode(d$Hypertension, "no::0", "yes::1", to.numeric = TRUE)
    d$OSAS.3ha <- ifelse(row.sums(d[, c("snore", "stop.breath", "sleepy", "Hypertension")]) >= 2, "high-risk", 
        "low-risk")
    d$OSAS.3ha[!is.na(d$apnea)] <- "high-risk"
    var2 <- c("seqn", "Year", "OSAS.3ha")
    if (component) 
        var2 <- c(var2, "snore", "stop.breath", "sleepy", "Hypertension", "apnea")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_OSAS.MAP` [exported]

```r
function (data, years, Year = FALSE, join = "left", component = F) 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_demo(db_slq(years = c(2005:2008, 2015:2018), how_often_do_you_snore = "snore", 
        how_often_do_you_snort_or_stop_breathing = "stop.breath", Year = T), ageyr = "age", sex = "sex"), 
        BMI_kg.m2 = "bmi")
    d <- d[d$Year %in% years, ]
    if (nrow(d) == 0) 
        stop(tmcn::toUTF8("<U+672C><U+5E74><U+6CA1><U+6709><U+6570><U+636E>"))
    d$snore <- Recode(d$snore, "never::0", "rarely (1-2 nights/week)::2", "rarely - 1-2 nights a week::2", 
        "occasionally (3-4 nights/week)::3", "occasionally - 3-4 nights a week::3", "frequently (5 or more nights/week)::4", 
        "frequently - 5 or more nights a week::4", "NA::", to.numeric = TRUE)
    d$stop.breath <- Recode(d$stop.breath, "never::0", "rarely (1-2 nights/week)::2", "rarely - 1-2 nights a week::2", 
        "occasionally (3-4 nights/week)::3", "occasionally - 3-4 nights a week::3", "frequently - 5 or more nights a week::4", 
        "frequently (5 or more nights/week)::4", "NA::", to.numeric = TRUE)
    d$sex <- Recode(d$sex, "Female::0", "Male::1", to.numeric = TRUE)
    index <- row.sums(d[, c("snore", "stop.breath")], na.rm = F)/2
    x <- -8.1600000000000001 + 1.2989999999999999 * index + 0.16300000000000001 * d$bmi - 0.028000000000000001 * 
        index * d$bmi + 0.032000000000000001 * d$age + 1.278 * d$sex
    d$OSAS.MAP <- exp(x)/(1 + exp(x))
    var2 <- c("seqn", "Year", "OSAS.MAP")
    if (component) 
        var2 <- c(var2, "snore", "stop.breath", "age", "sex", "bmi")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Overactive.bladder` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("kiq_u", years = years, cat = F)
    d <- nhs_read(tsv, "kiq044:uui0", "kiq045,kiq450:uui", "kiq480:nocturia", cat = F, lower_cd = T)
    d$uui[tolower(d$uui0) %in% "no"] <- "Never"
    d$uui <- Recode(d$uui, "Never::0", "a few times a year?::1", "a few times a month, or::1", "less than once a month::1", 
        "a few times a month::1", "a few times a week::2", "a few times a week, or::2", "every day::3", 
        "every day and/or night?::3", "every day and/or night::3", "NA::", to.numeric = TRUE)
    d$nocturia <- Recode(d$nocturia, "0::0", "1::1", "2::2", "3::3", "4::3", "5 or more?::3", "5 or more::3", 
        "NA::", to.numeric = TRUE)
    d$Overactive.bladder <- ifelse(d$nocturia + d$uui >= 3, "yes", "no")
    d$Overactive.bladder.count <- as.numeric(!is.na(d$nocturia)) + as.numeric(!is.na(d$uui))
    d <- d[, c("Year", "seqn", "Overactive.bladder", "Overactive.bladder.count", "uui", "nocturia")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_PAD` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- dex_ABPI(years = years, Year = TRUE)
    d$PAD <- ifelse(row.sums(d[, c("left_abpi", "right_abpi")] < 0.90000000000000002) >= 1, 1, 0)
    if (!yes1) 
        yes1(d) <- "PAD"
    d <- d[, c("Year", "seqn", "PAD")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_PHQ9` [exported]

```r
function (data, years, cut, na0 = FALSE, score = FALSE, dpq = FALSE, varLabel = FALSE, cat = T) 
{
    years = data_years(data, years)
    tsv <- nhs_tsv("dpq", items = "q", years = prepare_years(years), cat = FALSE)
    if (length(tsv) == 0) {
        if (do::cnOS()) 
            stop(paste0(paste0(years, collapse = ","), tmcn::toUTF8(" <U+5E74><U+6CA1><U+6709>PHQ-9<U+95EE><U+5377>")))
        if (!do::cnOS()) 
            stop(paste0(paste0(years, collapse = ","), " years have no PHQ-9"))
    }
    dpq_var <- c("dpq010", "dpq020", "dpq030", "dpq040", "dpq050", "dpq060", "dpq070", "dpq080", "dpq090")
    dpq_data <- nhs_read(tsv, dpq_var, varLabel = varLabel, codebook = FALSE, cat = FALSE)
    for (i in dpq_var) dpq_data[dpq_data[, i] > 3 & !is.na(dpq_data[, i]), i] <- NA
    qhpscore <- row.sums(dpq_data[, dpq_var])
    depression <- rep(NA, length(qhpscore))
    allanswer <- rep(NA, length(qhpscore))
    if (missing(cut)) 
        cut <- c(5, 10, 15, 20)
    (cut <- do::increase(cut[!cut %in% c(0, 27)]))
    if (length(cut) == 0) 
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5207><U+70B9><U+4E0D><U+80FD><U+662F>0<U+6216>27"))
        else stop("The cut point cannot be 0 or 27")
    for (i in 1:length(cut)) {
        if (i == 1) {
            cuti <- list(c(0, cut[i] - 1))
        }
        else {
            cuti <- c(cuti, list(c(cut[i - 1], cut[i] - 1)))
        }
        if (i == length(cut)) 
            cuti <- c(cuti, list(c(cut[i], 27)))
    }
    cuti
    pb <- txtProgressBar(max = length(qhpscore), width = 30, style = 3)
    for (i in 1:length(qhpscore)) {
        if (i == 1) 
            level <- c()
        setTxtProgressBar(pb, i)
        (dpi <- qhpscore[i])
        dpq_data[i, dpq_var]
        (answer <- row.sums(!is.na(dpq_data[i, dpq_var])))
        allanswer[i] <- answer
        if (answer == 0) 
            (next)(i)
        ck <- sapply(cuti, function(j) dpi %in% j[1]:j[2])
        (cut <- cuti[ck][[1]])
        (possible <- dpi:(dpi + 3 * (9 - answer)))
        (ck <- all(possible %in% (cut[1]:cut[2])))
        leveli <- sprintf("[%s,%s]", cut[1], cut[2])
        if (!leveli %in% level) 
            level <- c(level, leveli)
        if (ck) {
            depression[i] <- leveli
        }
        else {
            if (na0) 
                depression[i] <- leveli
        }
    }
    depression <- factor(depression, levels = level)
    if (cat) {
        cat("\n\n")
        print(table(answer = allanswer, depression, useNA = "i"))
    }
    if (score) 
        data_phq9 <- data.frame(seqn = dpq_data$seqn, Year = dpq_data$Year, PHQ9 = depression, answer = allanswer, 
            score = qhpscore, dpq_data[, c(-1, -2)])
    if (!score) 
        data_phq9 <- data.frame(seqn = dpq_data$seqn, Year = dpq_data$Year, PHQ9 = depression)
    if (!dpq) 
        data_phq9 <- data_phq9[, !colnames(data_phq9) %in% dpq_var]
    if (missing(data)) 
        return(data_phq9)
    data <- dplyr::left_join(data, data_phq9[, !colnames(data_phq9) %in% "Year"], "seqn")
    return(data)
}
```

## `diag_Parkinson` [exported]

```r
function (data, years, Year = FALSE, yes1 = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- drug_anti.parkinson(years = years, Year = TRUE, take_drug = "Parkinson", dup.take.drug = "remove", 
        yes.code = 1, no.code = 0, other.code = 0)
    if (!yes1) 
        yes1(d) <- "Parkinson"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Pregnant` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    demo <- nhs_tsv("demo", items = "demo", years = years, cat = FALSE)
    seq <- nhs_tsv("seq", items = "exam", years = years, cat = FALSE)
    rhq <- nhs_tsv("rhq", items = "q", years = years, cat = FALSE)
    uc <- nhs_tsv("uc\\.|uc_b|uc_c|ucpreg", years = years, cat = FALSE)
    d <- nhs_read(demo, "ridexprg:prg", seq, "seq060:seq", rhq, "rhq140,rhq141,rhd143:rhq", uc, "urxpreg", 
        psu_strat = F, lower_cd = TRUE, cat = FALSE)
    if ("prg" %in% colnames(d)) {
        d$prg.new <- Recode(d$prg, "sp not pregnant at exam::0", "yes, positive lab pregnancy test or self-reported pregnant at exam::1", 
            "cannot ascertain if sp is pregnant at exam::0", "the participant was not pregnant at exam::0", 
            "cannot ascertain if the participant is pregnant at exam::0", "NA::", to.numeric = T)
    }
    if ("seq" %in% colnames(d)) {
        d$seq.new <- Recode(d$seq, "no::0", "yes::1", "NA::", to.numeric = T)
    }
    if ("rhq" %in% colnames(d)) {
        d$rhq.new <- Recode(d$rhq, "no::0", "yes::1", "NA::", to.numeric = T)
    }
    if ("urxpreg" %in% colnames(d)) {
        d$urxpreg.new <- Recode(d$urxpreg, "negative::0", "positive::1", "not done::0", "none::0", "invalid::0", 
            "NA::", to.numeric = T)
    }
    ck <- colnames(d)[do::right(colnames(d), 4) == ".new"]
    d$Pregnant <- ifelse(row.sums(d[, ck, drop = FALSE]) > 0, 1, 0)
    if (!yes1) 
        yes1(d) <- "Pregnant"
    d <- d[, c("seqn", "Year", "Pregnant")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_RMetS` [exported]

```r
function (data, years, component = F, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_blood.pressure(db_HemalBiochemistry(db_bodyMeasure(BMI_kg.m2 = "BMI_kg.m2", years = years, 
        Year = TRUE), fast_total_cholesterol_mg.dl = "TC_mg.dl"), bpx = FALSE)
    head(d)
    d$score_bmi <- ifelse(d$BMI_kg.m2 < 22, 1, 0)
    d$score_tc <- ifelse(d$TC_mg.dl < 160, 1, 0)
    d$score_bpxsar <- ifelse(d$bpxsar > 90 & d$bpxsar < 120, 1, 0)
    d$score_bpxdar <- ifelse(d$bpxdar > 60 & d$bpxdar < 70, 1, 0)
    d$bp <- ifelse(row.sums(d[, c("score_bpxdar", "score_bpxsar")]) >= 2, 1, 0)
    d$andor <- ifelse(row.sums(d[, c("bp", "score_tc")]) >= 1, 1, 0)
    d$RMetS <- ifelse(row.sums(d[, c("andor", "score_bmi")]) >= 2, 1, 0)
    if (component) {
        d <- d[, c("Year", "seqn", "RMetS", "BMI_kg.m2", "TC_mg.dl", "bpxsar", "bpxdar")]
    }
    else {
        d <- d[, c("seqn", "Year", "RMetS")]
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Resistant.hypertension` [exported]

```r
function (data, years, systolic = 140, diastolic = 90, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- drug_anti.Hypertensive(diag_Hypertension(years = years, Year = TRUE, told = TRUE, drug = TRUE, 
        bpx = "bpx", method = "mean", cat = FALSE, systolic = systolic, diastolic = diastolic), take_drug = "drug", 
        DrugNumber = "n")
    d$Hypertension[d$drug == "yes" & d$n >= 3 & d$bpx == "yes"] <- "Resistant"
    d$Hypertension[d$Hypertension == "yes"] <- "Hypertension"
    d <- d[, c("seqn", "Year", "Hypertension")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_Retinal.Emboli` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("opxret", cat = T)
    d <- nhs_read(tsv, "opddholl:left.eye", "opdsholl:right.eye", "opduholl:worse.eye", cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_alcohol.associated.liver.disease` [exported]

```r
function (data, years, yes1 = FALSE, colname = "alcohol.associated.liver.disease", Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- diag_alcohol.user(db_HemalBiochemistry(Ast = T, Alt = T, years = years, Year = TRUE))
    d$alcohol.user <- ifelse(d$alcohol.user %in% c("heavy", "moderate", "mild"), 1, 0)
    d$Alt <- ifelse(d$Alt > 19, 1, 0)
    d$Ast <- ifelse(d$Ast > 29, 1, 0)
    d$Alt_Ast <- ifelse(row.sums(d[, c("Ast", "Alt")]) > 0, 1, 0)
    d$alcohol.associated.liver.disease <- ifelse(row.sums(d[, c("alcohol.user", "Alt_Ast")]) > 1, 1, 
        0)
    if (!yes1) 
        yes1(d) <- "alcohol.associated.liver.disease"
    col_rename(d) <- paste0("diag_alcohol.associated.liver.disease:", colname)
    d <- d[, c("seqn", "Year", colname)]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_alcohol.user` [exported]

```r
function (data, years, mild = c(1, 2), moderate = c(2, 3), heavy = c(3, 4), binge = TRUE, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    (tsv <- nhs_tsv("alq", "!~alqy", years = years, cat = F))
    d <- diag_binge(db_demo(nhs_read(tsv, "alq110,alq111:onelife.less12", "alq100,ald100,alq101:Oneyear12", 
        "alq120q,alq121:drink.past12month", "alq130:drinks.day", lower_cd = TRUE, cat = F), sex = TRUE, 
        psu_strat = FALSE, lower_cd = TRUE))
    d$drinks.day <- as.numeric(do::Replace0(d$drinks.day, " .*"))
    ck <- d$onelife.less12 %in% "no"
    d$alcohol.user[ck] <- "never"
    (ck1 <- (d$Oneyear12 %in% "yes") & (d$drink.past12month %in% c(0, "never in the last year")))
    (ck2 <- (d$onelife.less12 %in% "yes") & (d$drink.past12month %in% c(0, "never in the last year")))
    if (length(ck1) == 0 & length(ck2) == 0) {
    }
    else if (length(ck1) > 0 & length(ck2) == 0) {
        d$alcohol.user[ck1] <- "former"
    }
    else if (length(ck2) > 0 & length(ck1) == 0) {
        d$alcohol.user[ck2] <- "former"
    }
    else if (length(ck1) > 0 & length(ck2) > 0) {
        d$alcohol.user[ck1 | ck2] <- "former"
    }
    if (!is.null(mild)) {
        ck_mild <- (d$sex == "female" & d$drinks.day <= mild[1] & d$drinks.day > 0) | (d$sex == "male" & 
            d$drinks.day <= mild[2] & d$drinks.day > 0)
        d$alcohol.user[ck_mild] <- "mild"
    }
    if (!is.null(moderate)) {
        ck_moderate <- (d$sex == "female" & d$drinks.day >= moderate[1]) | (d$sex == "male" & d$drinks.day >= 
            moderate[2])
        d$alcohol.user[ck_moderate] <- "moderate"
    }
    if (!is.null(heavy)) {
        ck_heavy <- (d$sex == "female" & d$drinks.day >= heavy[1]) | (d$sex == "male" & d$drinks.day >= 
            heavy[2])
        d$alcohol.user[ck_heavy] <- "heavy"
    }
    if (binge) {
        d$alcohol.user[d$binge >= 5] <- "heavy"
        d$alcohol.user[d$binge >= 2 & d$binge < 5 & !d$alcohol.user %in% "heavy"] <- "moderate"
    }
    d <- d[, c("seqn", "Year", "alcohol.user")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_angina` [exported]

```r
function (data, years, angina = TRUE, angina.Age = FALSE, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    mcq <- nhs_tsv("mcq", years = years, cat = FALSE)
    d <- nhs_read(mcq, "mcq160d:angina", "mcq180d,mcd180d:angina.Age", cat = FALSE, lower_cd = TRUE)
    if (yes1) 
        d$angina <- ifelse(d$angina == "yes", 1, 0)
    d$angina.Age <- as.numeric(do::Replace0(d$angina.Age, " .*"))
    if (isFALSE(angina)) 
        d <- drop_col(d, "angina")
    if (isFALSE(angina.Age)) 
        d <- drop_col(d, "angina.Age")
    if (is.character(angina)) 
        col_rename(d) <- paste0("angina:", angina)
    if (is.character(angina.Age)) 
        col_rename(d) <- paste0("angina.Age:", angina.Age)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_arthritis` [exported]

```r
function (data, years, arthritis = FALSE, arghritis_age = FALSE, arghritis_type = FALSE, rheumatoid_arthritis, 
    psoriatic_arthritis, osteoarthritis_or_degenerative_arthritis, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    mcq <- nhs_tsv("mcq", years = years, cat = FALSE)
    d <- nhs_read(mcq, "mcq160a:arthritis", "mcq180a,mcd180a:arghritis_age", "mcq190,mcq191,mcq195:arghritis_type", 
        lower_cd = TRUE, cat = FALSE)
    if (!missing(rheumatoid_arthritis)) {
        d$Rheumatoid_arthritis <- d$arghritis_type
        d$Rheumatoid_arthritis[!d$Rheumatoid_arthritis %=% "rheumatoid arthritis"] <- "other"
        d$Rheumatoid_arthritis[d$arthritis %=% "no"] <- "no"
        if (is.character(rheumatoid_arthritis)) 
            col_rename(d) <- paste0("rheumatoid_arthritis:", rheumatoid_arthritis)
    }
    if (!missing(psoriatic_arthritis)) {
        d$psoriatic_arthritis <- d$arghritis_type
        d$psoriatic_arthritis[!d$psoriatic_arthritis %=% "psoriatic arthritis"] <- "other"
        d$psoriatic_arthritis[d$arthritis %=% "no"] <- "no"
        if (is.character(psoriatic_arthritis)) 
            col_rename(d) <- paste0("psoriatic_arthritis:", psoriatic_arthritis)
    }
    if (!missing(osteoarthritis_or_degenerative_arthritis)) {
        d$osteoarthritis_or_degenerative_arthritis <- d$arghritis_type
        d$osteoarthritis_or_degenerative_arthritis[!d$osteoarthritis_or_degenerative_arthritis %=% c("osteoarthritis", 
            "osteoarthritis or degenerative arthritis")] <- "other"
        d$osteoarthritis_or_degenerative_arthritis[d$arthritis %=% "no"] <- "no"
        if (is.character(osteoarthritis_or_degenerative_arthritis)) 
            col_rename(d) <- paste0("osteoarthritis_or_degenerative_arthritis:", osteoarthritis_or_degenerative_arthritis)
    }
    if (!arthritis) 
        d <- drop_col(d, "arthritis")
    if (!arghritis_age) 
        d <- drop_col(d, "arghritis_age")
    if (!arghritis_type) 
        d <- drop_col(d, "arghritis_type")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_atopic` [exported]

```r
function (data, cut.off = 0.34999999999999998, component = F, Year = F) 
{
    d <- db_IgE(alternaria_ku.l = "alternaria", aspergillus_ku.l = "aspergillus", bermuda.grass_ku.l = "bermuda.grass", 
        birch_ku.l = "birch", cat_ku.l = "cat", cockroach_ku.l = "cockroach", dog_ku.l = "dog", dust.farinae_ku.l = "dust.dermatophagoides.farinae", 
        dust.pteronyssinus_ku.l = "dust.dermatophatoides.pteronyssinus", mouse_ku.l = "mouse", oak_ku.l = "oak", 
        ragweed_ku.l = "ragweed", rat_ku.l = "rat", thistle_ku.l = "thistle", rye.grass_ku.l = "rye.grass", 
        egg_ku.l = "egg", milk_ku.l = "milk", peanut_ku.l = "peanut", shrimp_ku.l = "shrimp")
    comp <- c("alternaria", "aspergillus", "bermuda.grass", "birch", "cat", "cockroach", "dog", "dust.dermatophagoides.farinae", 
        "dust.dermatophatoides.pteronyssinus", "mouse", "oak", "ragweed", "rat", "thistle", "rye.grass", 
        "egg", "milk", "peanut", "shrimp")
    for (i in comp) {
        d[, paste0("AT_", i)] <- as.numeric(d[, i] >= cut.off)
    }
    di <- d[, paste0("AT_", comp)]
    d$atopic <- ifelse(row.sums(di) >= 1, "yes", "no")
    d$atopic_count <- ncol(di) - do::NA.row.sums(di)
    var2 <- c("Year", "seqn", "atopic", "atopic_count")
    if (component) 
        var2 <- c(var2, comp)
    d[, var2]
}
```

## `diag_binge` [exported]

```r
function (data, years, month = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    alq <- nhs_tsv("alq", "!~alqy", years = years, cat = FALSE)
    d <- nhs_read(alq, "alq140q,alq141q,alq142:binge_times", "alq140u,alq141u:binge_unit", cat = FALSE, 
        lower_cd = TRUE)
    d$binge_times <- Recode(d$binge_times, "never in the last year::0-year", "every day::1-day", "nearly every day::1-day", 
        "once a week::1-week", "2 times a week::2-week", "3 to 4 times a week::3.5-week", "once a month::1-month", 
        "2 to 3 times a month::2.5-month", "1 to 2 times in the last year::1.5-year", "3 to 6 times in the last year::4.5-year", 
        "7 to 11 times in the last year::9-year")
    ck <- lookl(d$binge_times, "-") & !is.na(d$binge_times)
    if (any(ck)) {
        cki <- d$binge_times[ck]
        ckdf <- do::col_split(cki, "-")
        d$binge_times[ck] <- ckdf[, 1]
        d$binge_unit[ck] <- ckdf[, 2]
    }
    d$binge_times <- as.numeric(d$binge_times)
    if (month) {
        ck <- d$binge_unit %in% "day"
        d$binge[ck] <- d$binge_times[ck] * 30
        ck <- d$binge_unit %in% "week"
        d$binge[ck] <- d$binge_times[ck]/7 * 30
        ck <- d$binge_unit %in% "year"
        d$binge[ck] <- d$binge_times[ck]/365 * 30
        d$binge <- janitor::round_half_up(d$binge, 1)
        var <- c("seqn", "Year", "binge")
    }
    else {
        var <- c("seqn", "Year", "binge_times", "binge_unit")
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_congestive.heart.failure` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    mcq <- nhs_tsv("mcq", years = years, cat = FALSE)
    d <- nhs_read(mcq, "mcq160b:congestive.heart.failure", cat = FALSE, lower_cd = TRUE)
    if (yes1) 
        d$congestive.heart.failure <- ifelse(d$congestive.heart.failure == "yes", 1, 0)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_coronary.heart.disease` [exported]

```r
function (data, years, coronary.heart.disease = TRUE, coronary.heart.disease.Age = FALSE, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("mcq", years = years, cat = FALSE)
    d <- nhs_read(tsv, "mcq160c:coronary.heart.disease", "mcq180c,mcd180c:coronary.heart.disease.Age", 
        cat = FALSE, lower_cd = TRUE)
    d$coronary.heart.disease.Age <- do::Replace0(d$coronary.heart.disease.Age, " .*")
    d$coronary.heart.disease.Age <- as.numeric(d$coronary.heart.disease.Age)
    if (isFALSE(coronary.heart.disease)) 
        d <- drop_col(d, "coronary.heart.disease")
    if (is.character(coronary.heart.disease)) 
        col_rename(d) <- paste0("coronary.heart.disease:", coronary.heart.disease)
    if (isFALSE(coronary.heart.disease.Age)) 
        d <- drop_col(d, "coronary.heart.disease.Age")
    if (is.character(coronary.heart.disease.Age)) 
        col_rename(d) <- paste0("coronary.heart.disease.Age:", coronary.heart.disease.Age)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_epilepsy` [exported]

```r
function (data, years, yes1 = FALSE, take_drug = FALSE, DrugNumber = FALSE, drugname = FALSE, remove.other = TRUE, 
    dup.take.drug = c("paste", "remove", "keep"), Year = FALSE, join = "left") 
{
    dup.take.drug <- dup.take.drug[1]
    years <- data_years(data, years)
    tsv <- nhs_tsv("rxq_rx", years = years, cat = FALSE)
    tsv0(tsv)
    d <- nhs_read(tsv, "rxduse,rxd030:take_drug", "rxddrug,rxd240b:Drug", "rxdrsc1", "rxdrsc2", "rxdrsc3", 
        lower_cd = TRUE, cat = FALSE)
    ck <- lookl(d[, c("rxdrsc1", "rxdrsc2", "rxdrsc3")], "G40")
    d$take_drug[d$take_drug == "yes" & !ck] <- "other"
    d$epilepsy <- ifelse(ck, 1, 0)
    if (!yes1) 
        yes1(d) <- "epilepsy"
    if (isTRUE(take_drug) | is.character(take_drug) | isTRUE(DrugNumber) | is.character(DrugNumber) | 
        isTRUE(drugname) | is.character(drugname)) {
        if (remove.other) {
            (ck <- which((d$seqn %in% unique(d$seqn[ck])) & d$take_drug == "other"))
            length(ck)
            if (length(ck) > 0) 
                d <- d[-ck, ]
        }
        else {
            d$seqn[ck] <- paste0(d$seqn[ck], "-yes")
        }
        d$DrugNumber <- 0
        d$DrugNumber[d$take_drug %in% c("yes", "other")] <- 1
        d <- d[, c("seqn", "Year", "epilepsy", "take_drug", "DrugNumber", "Drug")]
        if (dup.take.drug == "paste" & any(anyDuplicated(d$seqn))) {
            seqn <- unique(d$seqn[duplicated(d$seqn)])
            for (i in seqn) {
                n <- which(d$seqn %in% i)
                d$DrugNumber[n] <- length(n)
                d[n, "Drug"] <- paste0(d[n, "Drug"], collapse = ";;;")
                d <- d[-n[-1], ]
            }
        }
        else if (dup.take.drug == "remove") {
            ck <- !duplicated(paste0(d$seqn, d$take_drug))
            d <- d[ck, ]
        }
        if (isFALSE(take_drug)) 
            d <- drop_col(d, "take_drug")
        if (is.character(take_drug)) 
            col_rename(d) <- paste0("take_drug:", take_drug)
        if (isFALSE(DrugNumber)) 
            d <- drop_col(d, "DrugNumber")
        if (is.character(DrugNumber)) 
            col_rename(d) <- paste0("DrugNumber:", DrugNumber)
        if (isFALSE(drugname)) 
            d <- drop_col(d, "Drug")
        if (is.character(drugname)) 
            col_rename(d) <- paste0("Drug:", drugname)
    }
    else {
        (ck <- which((d$seqn %in% unique(d$seqn[ck])) & d$take_drug == "other"))
        length(ck)
        if (length(ck) > 0) 
            d <- d[-ck, ]
        ck <- !duplicated(paste0(d$seqn, d$epilepsy))
        d <- d[ck, ]
        d <- d[, c("seqn", "Year", "epilepsy")]
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_heart.attack` [exported]

```r
function (data, years, heart.attack = TRUE, heart.attack.Age = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("mcq|spx", years = years, cat = FALSE)
    d <- nhs_read(tsv, "mcq160e:heart.attack", "spq070e", "mcq180e,mcd180e:heart.attack.Age", lower_cd = T, 
        cat = FALSE)
    if ("heart.attack.Age" %in% colnames(d)) 
        d$heart.attack.Age <- as.numeric(do::Replace0(d$heart.attack.Age, " .*"))
    d[d == "yes"] <- 1
    d[d == "no"] <- 0
    d$heart.attack <- as.numeric(d$heart.attack)
    if ("spq070e" %in% colnames(d)) {
        d$spq070e[!is.na(d$spq070e)] <- 1
        d$spq070e <- as.numeric(d$spq070e)
    }
    d$heart.attack <- ifelse(row.sums(d[, -c(1, 2), drop = FALSE]) > 0, "yes", "no")
    d <- d[, set::and(c("seqn", "Year", "heart.attack", "heart.attack.Age"), colnames(d))]
    if (isFALSE(heart.attack)) 
        d <- drop_col(d, "heart.attack")
    if (isFALSE(heart.attack.Age)) 
        d <- drop_col(d, "heart.attack.Age")
    if (is.character(heart.attack)) 
        col_rename(d) <- paste0("heart.attack:", heart.attack)
    if (is.character(heart.attack.Age)) 
        col_rename(d) <- paste0("heart.attack.Age:", heart.attack.Age)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_hypoparathyroidism` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_HemalBiochemistry(nhs_read(nhs_tsv("l11_c|pth_d", cat = F, years = years), "lbxpt21:parathyroid_hormone_pg.ml", 
        cat = F), years = years, calcium_albumin_corrected_mmol.L = "cCa")
    d$parathyroid_hormone_pg.ml <- ifelse(d$parathyroid_hormone_pg.ml < 50, 1, 0)
    d$cCa <- ifelse(d$cCa < 2.1200000000000001, 1, 0)
    d$hypoparathyroidism <- ifelse(row.sums(d[, c("parathyroid_hormone_pg.ml", "cCa")]) >= 2, 1, 0)
    d <- d[, c("seqn", "Year", "hypoparathyroidism")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_icd10` [exported]

```r
function (..., data, years, Year = FALSE, join = "left", colname = "target", yes1 = FALSE, icd10 = FALSE) 
{
    h0 <- c(...)
    years <- data_years(data, years)
    tsv <- nhs_tsv("RXQ_RX", years = years, cat = F)
    d <- nhs_read(tsv, "rxdrsd1", nrows = 1, cat = F)
    tsv0(d)
    tsv <- nhs_tsv("RXQ_RX", years = d$Year, cat = F)
    d <- nhs_read(tsv, cat = F)
    target1 <- paste_dcn.icn(d, "rxdrsc")
    target2 <- paste_dcn.icn(d, "rxdrsd")
    target <- paste0(target1, ";", target2)
    ck <- lookl(target, h0)
    d$target <- ifelse(ck, 1, 0)
    if (!yes1) 
        yes1(d) <- "target"
    d$target[nchar(target) == 0] <- NA
    if (icd10) {
        d$icd10.code <- target1
        d$icd10.desc <- target2
        d <- unique(d[, c("seqn", "Year", "target", "icd10.code", "icd10.desc")])
    }
    else {
        d <- unique(d[, c("seqn", "Year", "target")])
    }
    dup <- unique(d$seqn[duplicated(d$seqn)])
    for (i in 1:length(dup)) {
        ck <- which(d$seqn %in% dup[i])
        if (all(d$target[ck] %in% "no")) {
            d <- d[-ck[-1], ]
        }
        else if (all(d$target[ck] %in% "yes")) {
        }
        else {
            d <- d[-(ck[d$target[ck] %in% "no"]), ]
        }
    }
    colnames(d)[3] <- colname
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_infertility` [exported]

```r
function (data, years, infertility_care = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("rhq", years = years, cat = F)
    d <- nhs_read(tsv, "rhq074:infertility", "rhq076:infertility_care", lower_cd = TRUE, cat = FALSE, 
        Year = TRUE)
    tsv0(d)
    d$infertility[d$infertility_care == "yes"] <- "yes"
    if (!infertility_care) 
        d <- drop_col(d, "infertility_care")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_mFried.frailty` [exported]

```r
function (data = NULL, all = FALSE, years, Fried.frailty, Fried.frailty_count, weakness, low.pa, exhaustion, 
    slow.walking.speed, weight.change, Year = F, join = "left") 
{
    ck <- all(miss(Fried.frailty), miss(Fried.frailty_count), miss(weakness), miss(low.pa), miss(exhaustion), 
        miss(slow.walking.speed), miss(weight.change))
    if (all) {
        if (ck) {
            Fried.frailty <- TRUE
            Fried.frailty_count <- TRUE
            weakness <- TRUE
            low.pa <- TRUE
            exhaustion <- TRUE
            slow.walking.speed <- TRUE
            weight.change <- TRUE
        }
        else {
            if (miss(Fried.frailty)) 
                Fried.frailty <- TRUE
            if (miss(Fried.frailty_count)) 
                Fried.frailty_count <- TRUE
            if (miss(weakness)) 
                weakness <- TRUE
            if (miss(low.pa)) 
                low.pa <- TRUE
            if (miss(exhaustion)) 
                exhaustion <- TRUE
            if (miss(slow.walking.speed)) 
                slow.walking.speed <- TRUE
            if (miss(weight.change)) 
                weight.change <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(Fried.frailty)) 
                Fried.frailty <- FALSE
            if (miss(Fried.frailty_count)) 
                Fried.frailty_count <- FALSE
            if (miss(weakness)) 
                weakness <- FALSE
            if (miss(low.pa)) 
                low.pa <- FALSE
            if (miss(exhaustion)) 
                exhaustion <- FALSE
            if (miss(slow.walking.speed)) 
                slow.walking.speed <- FALSE
            if (miss(weight.change)) 
                weight.change <- FALSE
        }
    }
    if (isTRUE(Fried.frailty)) 
        Fried.frailty = "Fried.frailty"
    if (isTRUE(Fried.frailty_count)) 
        Fried.frailty_count = "Fried.frailty_count"
    if (isTRUE(weakness)) 
        weakness = "weakness"
    if (isTRUE(low.pa)) 
        low.pa = "low.pa"
    if (isTRUE(exhaustion)) 
        exhaustion = "exhaustion"
    if (isTRUE(slow.walking.speed)) 
        slow.walking.speed = "slow.walking.speed"
    if (isTRUE(weight.change)) 
        weight.change = "weight.change"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "Year", "Year"), "seqn", "seqn"), Fried.frailty, "Fried.frailty"), Fried.frailty_count, "Fried.frailty_count"), 
        weakness, "weakness"), low.pa, "low.pa"), exhaustion, "exhaustion"), slow.walking.speed, "slow.walking.speed"), 
        weight.change, "weight.change")
    years <- data_years(data, years)
    pfq <- nhs_tsv("pfq")
    paq <- nhs_tsv("paq", "!~iaf|paqy")
    dpq <- nhs_tsv("dpq")
    whq <- nhs_tsv("whq", "!~mec")
    d <- nhs_read(pfq, "pfq061e-u", "pfq061h-u", paq, "pad680-u", dpq, "dpq040-u", whq, "whd020", "whd050", 
        "whq060", cat = F)
    d$weakness <- ifelse(d$pfq061e %in% c(2, 3, 4), 1, 0)
    d$weakness[is.na(d$pfq061e)] <- NA
    d$low.pa <- ifelse(d$pad680 %in% c(2, 3), 1, 0)
    d$low.pa[is.na(d$pad680)] <- NA
    d$exhaustion <- ifelse(d$dpq040 %in% c(2, 3), 1, 0)
    d$exhaustion[is.na(d$dpq040)] <- NA
    d$slow.walking.speed <- ifelse(d$pfq061h %in% c(2, 3, 4), 1, 0)
    d$slow.walking.speed[is.na(d$pfq061h)] <- NA
    unique(d$whd020)
    unique(d$whd050)
    d$weight.change <- d$whd020 - d$whd050
    d$weight.change[tolower(d$whq060) %in% "yes"] <- NA
    d$weight.change <- ifelse(d$weight.change <= 10, 1, 0)
    ags <- c("weakness", "low.pa", "exhaustion", "slow.walking.speed", "weight.change")
    d <- d[, c("Year", "seqn", ags)]
    d$FRI <- row.sums(d[, ags])
    d$Fried.frailty <- ifelse(d$FRI >= 3, "Frail", ifelse(d$FRI >= 1, "prefaril", "robust"))
    d$Fried.frailty_count <- length(ags) - do::NA.row.sums(d[, ags])
    d <- d[, c("Year", "seqn", "Fried.frailty", "Fried.frailty_count", ags)]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `diag_osteoporosis` [exported]

```r
function (data, years, fem.neck.mean = 0.85999999999999999, fem.neck.sd = 0.12, lum.mean = 1.0640000000000001, 
    lum.sd = 0.106, Tscore = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_dxxfem(years = years, Year = TRUE, femoral_neck_bmd_g.cm2 = "fem_neck")
    d <- db_dxx(d, lumbar_spine_bmd_g.cm2 = "lum", join = "full")
    d$Year <- NULL
    d <- db_demo(d, ageyr = T, Year = T, join = "inner", psu_strat = F)
    d$ageyr <- NULL
    d$T_fem.neck <- (d$fem_neck - fem.neck.mean)/fem.neck.sd
    d$T_lum <- (d$lum - lum.mean)/lum.sd
    d$osteoporosis[d$T_fem.neck > -1] <- "normal"
    d$osteoporosis[d$T_lum > -1] <- "normal"
    d$osteoporosis[d$T_fem.neck <= -1 & d$T_fem.neck > -2.5] <- "osteopenia"
    d$osteoporosis[d$T_lum <= -1 & d$T_lum > -2.5] <- "osteopenia"
    d$osteoporosis[d$T_fem.neck <= -2.5] <- "osteoporosis"
    d$osteoporosis[d$T_lum <= -2.5] <- "osteoporosis"
    var <- c("seqn", "Year", "osteoporosis")
    if (Tscore) 
        append(var) <- c("T_fem.neck", "T_lum")
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_periodontitis` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("ohxp", years = years, cat = FALSE)
    if (length(tsv) == 0) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+8FD9><U+4E9B><U+5E74><U+4EFD><U+6CA1><U+6709>ohxp"))
        if (!do::cnOS()) 
            stop("no ohxp files in this year cycle")
    }
    d <- nhs_read(tsv, cat = FALSE)
    (pcla <- do::increase(colnames(d)[grepl("[0-9]{2}pc|[0-9]{2}la", colnames(d))]))
    d = d[, c("Year", "seqn", pcla)]
    ohd <- set::grep_and(pcla, "ohd")
    if (length(ohd) > 0) {
        for (i in ohd) {
            ix <- do::Replace(i, "ohd", "ohx")
            if (ix %in% pcla) {
                d[is.na(d[, ix]), ix] <- d[is.na(d[, ix]), i]
                d <- drop_col(d, i)
            }
            else {
                colnames(d)[colnames(d) == i] <- ix
            }
        }
    }
    (pcla <- do::increase(colnames(d)[grepl("[0-9]{2}pc|[0-9]{2}la", colnames(d))]))
    t <- stringi::stri_extract(pcla, regex = "[0-9]{2}")
    pcla <- paste0("t", t, "_", do::Replace0(pcla, ".*[0-9]{2}"))
    colnames(d)[-c(1, 2)] <- pcla
    for (i in 1:ncol(d)) {
        d[tolower(d[, i]) %in% "cannot be assessed", i] <- NA
        d[tolower(d[, i]) %in% "calculation cannot be determined", i] <- NA
    }
    to_numeric(d) <- colnames(d)
    la <- d[, grepl("_la", colnames(d))]
    ck <- la >= 4
    la[ck] <- 1
    la[!ck] <- 0
    d[, grepl("_la", colnames(d))] <- la
    pc <- d[, grepl("_pc", colnames(d))]
    ck <- pc >= 5
    pc[ck] <- 1
    pc[!ck] <- 0
    d[, grepl("_pc", colnames(d))] <- pc
    t <- unique(t)
    for (i in t) {
        var <- set::grep_and(colnames(d), paste0("t", i, "_"))
        ck <- ifelse(row.sums(d[, var]) >= 1, 1, 0)
        eval(parse(text = sprintf("d$t%s <- ck", i)))
        d <- drop_col(d, var)
    }
    d$count <- row.sums(d[, paste0("t", t)])
    d$periodontitis <- ifelse(d$count >= 2, "yes", "no")
    d <- d[, c("Year", "seqn", "count", "periodontitis")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_periodontitis_CDC.AAP` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("ohxp", years = years, cat = )
    tsv0(tsv)
    d <- nhs_read(tsv, cat = FALSE, lower_cd = TRUE)
    (pcla <- do::increase(colnames(d)[grepl("[0-9]{2}pc|[0-9]{2}la", colnames(d))]))
    d = d[, c("Year", "seqn", pcla)]
    ohd <- set::grep_and(pcla, "ohd")
    if (length(ohd) > 0) {
        for (i in ohd) {
            ix <- do::Replace(i, "ohd", "ohx")
            if (ix %in% pcla) {
                d[is.na(d[, ix]), ix] <- d[is.na(d[, ix]), i]
                d <- drop_col(d, i)
            }
            else {
                colnames(d)[colnames(d) == i] <- ix
            }
        }
    }
    (pcla <- do::increase(colnames(d)[grepl("[0-9]{2}pc|[0-9]{2}la", colnames(d))]))
    t <- stringi::stri_extract(pcla, regex = "[0-9]{2}")
    pcla <- paste0("t", t, "_", do::Replace0(pcla, ".*[0-9]{2}"))
    colnames(d)[-c(1, 2)] <- pcla
    d <- d[, set::grep_not_or(colnames(d), c("lam", "lal", "pcm", "pcl"))]
    for (i in 1:ncol(d)) {
        d[tolower(d[, i]) %in% "cannot be assessed", i] <- NA
        d[tolower(d[, i]) %in% "calculation cannot be determined", i] <- NA
    }
    to_numeric(d) <- colnames(d)
    d$periodontitis_CDC.AAP[!is.na(row.sums(d[, -c(1, 2)]))] <- "no"
    ck_la <- grepl("_la", colnames(d))
    la <- d[, ck_la]
    ck_la3 <- la >= 3
    la[ck_la3] <- 1
    la[!ck_la3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(la)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(la)))
        (wh <- which(tooth %in% i))
        la[, wh[1]] <- ifelse(row.sums(la[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            la <- la[, -wh[-1]]
    }
    la$la2 <- ifelse(row.sums(la) >= 2, 1, 0)
    ck_pc <- grepl("_pc", colnames(d))
    pc <- d[, ck_pc]
    ck_pc3 <- pc >= 4
    pc[ck_pc3] <- 1
    pc[!ck_pc3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(pc)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(pc)))
        (wh <- which(tooth %in% i))
        pc[, wh[1]] <- ifelse(row.sums(pc[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            pc <- pc[, -wh[-1]]
    }
    la$pc2 <- ifelse(row.sums(pc) >= 2, 1, 0)
    pc5 <- d[, ck_pc]
    la$pc5 <- ifelse(row.sums(pc5 >= 5) >= 1, 1, 0)
    la$lapc <- ifelse(row.sums(la[, c("la2", "pc2")]) >= 2, 1, 0)
    ck <- row.sums(la[, c("lapc", "pc5")]) >= 1
    d$periodontitis_CDC.AAP[ck] <- "mild"
    ck_la <- grepl("_la", colnames(d))
    la <- d[, ck_la]
    ck_la3 <- la >= 4
    la[ck_la3] <- 1
    la[!ck_la3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(la)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(la)))
        (wh <- which(tooth %in% i))
        la[, wh[1]] <- ifelse(row.sums(la[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            la <- la[, -wh[-1]]
    }
    la$la2 <- ifelse(row.sums(la) >= 2, 1, 0)
    ck_pc <- grepl("_pc", colnames(d))
    pc <- d[, ck_pc]
    ck_pc3 <- pc >= 5
    pc[ck_pc3] <- 1
    pc[!ck_pc3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(pc)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(pc)))
        (wh <- which(tooth %in% i))
        pc[, wh[1]] <- ifelse(row.sums(pc[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            pc <- pc[, -wh[-1]]
    }
    la$pc2 <- ifelse(row.sums(pc) >= 2, 1, 0)
    ck <- row.sums(la[, c("la2", "pc2")]) >= 1
    d$periodontitis_CDC.AAP[ck] <- "moderate"
    ck_la <- grepl("_la", colnames(d))
    la <- d[, ck_la]
    ck_la3 <- la >= 6
    la[ck_la3] <- 1
    la[!ck_la3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(la)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(la)))
        (wh <- which(tooth %in% i))
        la[, wh[1]] <- ifelse(row.sums(la[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            la <- la[, -wh[-1]]
    }
    la$la2 <- ifelse(row.sums(la) >= 2, 1, 0)
    ck_pc <- grepl("_pc", colnames(d))
    pc <- d[, ck_pc]
    ck_pc3 <- pc >= 5
    pc[ck_pc3] <- 1
    pc[!ck_pc3] <- 0
    (tooth <- gsub("[a-z_]", "", colnames(pc)))
    for (i in unique(tooth)) {
        (tooth <- gsub("[a-z_]", "", colnames(pc)))
        (wh <- which(tooth %in% i))
        pc[, wh[1]] <- ifelse(row.sums(pc[, wh]) >= 1, 1, 0)
        if (length(wh) > 1) 
            pc <- pc[, -wh[-1]]
    }
    la$pc2 <- ifelse(row.sums(pc) >= 1, 1, 0)
    ck <- row.sums(la[, c("la2", "pc2")]) >= 2
    d$periodontitis_CDC.AAP[ck] <- "severe"
    d <- d[, c("seqn", "Year", "periodontitis_CDC.AAP")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_preDM` [exported]

```r
function (data, years, Year = FALSE, cat = TRUE, join = "left") 
{
    years <- data_years(data, years)
    ghb <- nhs_tsv("lab10\\.|l10_b\\.|l10_c\\.|ghb", items = "lab", cat = FALSE, years = years)
    gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu", items = "Laboratory", cat = FALSE, years = years)
    ogtt <- nhs_tsv("ogtt", items = "Laboratory", cat = FALSE, years = years)
    diq <- nhs_tsv("diq", years = years, cat = FALSE)
    d <- nhs_read(ghb, "lbxgh:HbA1c", gluam, "lbxglusi,lbdglusi:fglu", ogtt, "lbdgltsi:ogtt2", diq, "diq160:told", 
        cat = FALSE, lower_cd = TRUE)
    var2 <- c("Year", "seqn")
    if ("told" %=% colnames(d)) {
        if (cat) 
            cat("\ntold")
        ck <- d$told == "yes"
        d$told[ck] <- 1
        d$told[!ck] <- 0
        to_numeric(d) <- "told"
        var2 <- c(var2, "told")
    }
    if ("HbA1c" %=% colnames(d)) {
        if (cat) 
            cat("\nHbA1c: 5.7-6.5")
        ck <- d$HbA1c >= 5.7000000000000002 & d$HbA1c < 6.5
        d$HbA1c[ck] <- 1
        d$HbA1c[!ck] <- 0
        var2 <- c(var2, "HbA1c")
    }
    if ("fglu" %=% colnames(d)) {
        if (cat) 
            cat("\nFPG: 5.6-7.0")
        ck <- d$fglu > 5.5999999999999996 & d$fglu < 7
        d$fglu[ck] <- 1
        d$fglu[!ck] <- 0
        var2 <- c(var2, "fglu")
    }
    if ("ogtt2" %=% colnames(d)) {
        if (cat) 
            cat("\nOGTT2: 7.8-11.0")
        ck <- d$ogtt2 > 7.7999999999999998 & d$ogtt2 < 11
        d$ogtt2[ck] <- 1
        d$ogtt2[!ck] <- 0
        var2 <- c(var2, "ogtt2")
    }
    d$preDM <- ifelse(row.sums(d[, var2[-c(1, 2)], drop = FALSE]) >= 1, "yes", "no")
    d <- d[, c("Year", "seqn", "preDM")]
    d <- diag_DM(d, cat = FALSE)
    d$preDM[d$DM == "DM"] <- "DM"
    d <- d[, c("seqn", "Year", "preDM")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_sarcopenia` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    mgx <- nhs_tsv("mgx", years = years, cat = FALSE)
    if (length(mgx) == 0) 
        stop("no mgx file in this year")
    mg_var <- c("mgxh1t1", "mgxh1t2", "mgxh1t3", "mgxh2t1", "mgxh2t2", "mgxh2t3")
    d1 <- db_bodyMeasure(db_demo(nhs_read(mgx, mg_var, cat = FALSE), sex = TRUE), BMI_kg.m2 = "BMI")
    d1$Max <- row.max(d1[, mg_var])
    d1$Max_bmi <- d1$Max/d1$BMI
    d1$mg_score <- ifelse((d1$sex == "Male" & d1$Max_bmi < 1) | (d1$sex == "Female" & d1$Max_bmi < 0.56000000000000005), 
        1, 0)
    dxx <- nhs_tsv("dxx_", years = unique(d1$Year), cat = FALSE)
    dxx_var <- c("dxdlale", "dxdrale", "dxdllle", "dxdrlle")
    d2 <- nhs_read(dxx, dxx_var, Year = FALSE, cat = FALSE)
    d2$ALM <- row.sums(d2[, dxx_var])
    d2$ALM <- d2$ALM/1000
    d <- dplyr::inner_join(d1, d2, "seqn")
    d$ALM_bmi <- d$ALM/d$BMI
    d$ALM_score <- ifelse((d$sex == "Male" & d$ALM_bmi < 0.78900000000000003) | (d$sex == "Female" & 
        d$ALM_bmi < 0.51200000000000001), 1, 0)
    d$sarcopenia <- ifelse(row.sums(d[, c("mg_score", "ALM_score")]) == 2, 1, 0)
    d$sarcopenia[(d$mg_score %in% 1 & is.na(d$ALM_score)) | (d$ALM_score %in% 1 & is.na(d$mg_score))] <- NA
    if (!yes1) 
        d$sarcopenia <- ifelse(d$sarcopenia == 1, "yes", "no")
    d <- d[, c("seqn", "Year", "sarcopenia")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_sarcopenia_low.muscle` [exported]

```r
function (data, years, yes1 = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (dxx <- nhs_tsv("dxx_", years = years, cat = FALSE))
    dxx_var <- c("dxdlale", "dxdrale", "dxdllle", "dxdrlle")
    d <- db_bodyMeasure(db_demo(db_dxx(left_arm_lean_excl_bmc_g = "dxdlale", right_arm_lean_excl_bmc_g = "dxdrale", 
        left_leg_lean_excl_bmc_g = "dxdllle", right_leg_lean_excl_bmc_g = "dxdrlle", years = years, Year = T), 
        sex = TRUE), BMI_kg.m2 = "BMI")
    d$ALM <- row.sums(d[, dxx_var])
    d$ALM <- d$ALM/1000
    d$ALM_bmi <- d$ALM/d$BMI
    d$low.muscle <- ifelse((d$sex == "Male" & d$ALM_bmi < 0.78900000000000003) | (d$sex == "Female" & 
        d$ALM_bmi < 0.51200000000000001), 1, 0)
    if (!yes1) 
        d$low.muscle <- ifelse(d$low.muscle == 1, "yes", "no")
    d <- d[, c("seqn", "Year", "low.muscle")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_smoke` [exported]

```r
function (data, years, smoke = T, start_age = F, quit_years = F, smoking_years = F, pack_years = F, cigarettes_per_day_when_quit = F, 
    avg_cigarettes_per_day_past_30_days = F, anyone.smoke.in.home = F, days.used.nicotine.stop.smoking.aid_past5days = F, 
    never = "never", former = "former", now = "now", Year = FALSE, join = "left") 
{
    seqn = "seqn"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        Year, "Year"), seqn, "seqn"), smoke, "smoke"), start_age, "start_age"), quit_years, "quit_years"), 
        smoking_years, "smoking_years"), pack_years, "pack_years"), cigarettes_per_day_when_quit, "cigarettes_per_day_when_quit"), 
        avg_cigarettes_per_day_past_30_days, "avg_cigarettes_per_day_past_30_days"), anyone.smoke.in.home, 
        "anyone.smoke.in.home"), days.used.nicotine.stop.smoking.aid_past5days, "days.used.nicotine.stop.smoking.aid_past5days")
    if (isTRUE(seqn)) 
        seqn = "seqn"
    if (isTRUE(smoke)) 
        smoke = "smoke"
    if (isTRUE(start_age)) 
        start_age = "start_age"
    if (isTRUE(quit_years)) 
        quit_years = "quit_years"
    if (isTRUE(smoking_years)) 
        smoking_years = "smoking_years"
    if (isTRUE(pack_years)) 
        pack_years = "pack_years"
    if (isTRUE(cigarettes_per_day_when_quit)) 
        cigarettes_per_day_when_quit = "cigarettes_per_day_when_quit"
    if (isTRUE(avg_cigarettes_per_day_past_30_days)) 
        avg_cigarettes_per_day_past_30_days = "avg_cigarettes_per_day_past_30_days"
    if (isTRUE(anyone.smoke.in.home)) 
        anyone.smoke.in.home = "anyone.smoke.in.home"
    if (isTRUE(days.used.nicotine.stop.smoking.aid_past5days)) 
        days.used.nicotine.stop.smoking.aid_past5days = "days.used.nicotine.stop.smoking.aid_past5days"
    years <- data_years(data, years)
    version <- 2
    (file <- paste0(get_config_path(), "/attach/diag_smoke~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        create_diag_smoke(version)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    d$smoke <- ifelse(d$smoke == "never", never, ifelse(d$smoke == "former", former, now))
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `diag_stroke` [exported]

```r
function (data, years, stroke = TRUE, stroke.Age = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("mcq|spx", years = years, cat = FALSE)
    d <- nhs_read(tsv, "mcq160f:stroke", "spq070d", "mcq180f,mcd180f:stroke.Age", lower_cd = T, cat = FALSE)
    d[d == "yes"] <- 1
    d[d == "no"] <- 0
    d$stroke <- as.numeric(d$stroke)
    if ("spq070d" %in% colnames(d)) {
        d$spq070d[!is.na(d$spq070d)] <- 1
        d$spq070d <- as.numeric(d$spq070d)
    }
    d$stroke <- ifelse(row.sums(d[, -c(1, 2, ncol(d)), drop = FALSE]) > 0, "yes", "no")
    d <- d[, set::and(c("seqn", "Year", "stroke", "stroke.Age"), colnames(d))]
    if (isFALSE(stroke)) 
        d <- drop_col(d, "stroke")
    if (isFALSE(stroke.Age)) 
        d <- drop_col(d, "stroke.Age")
    if (is.character(stroke)) 
        col_rename(d) <- paste0("stroke:", stroke)
    if (is.character(stroke.Age)) 
        col_rename(d) <- paste0("stroke.Age:", stroke.Age)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_viral.hepatitis` [exported]

```r
function (data, years, HBV = TRUE, HCV = TRUE, Year = FALSE, yes1 = FALSE, colname = "viral.hepatitis", 
    join = "left") 
{
    years <- data_years(data, years)
    hv <- nhs_tsv("lab02|l02_b|l02_c|sshcvr_c|hepbd|sshepc_h|hepc", years = years, cat = FALSE)
    d <- nhs_read(hv, "lbdhbg:HBV", "lbxhcr,sshcvrna:HCV_rna", "lbdhcv,lbdhci:HCV_body", lower_cd = TRUE, 
        cat = FALSE)
    d$HBV_score <- ifelse(lookl(d$HBV, "positive"), 1, 0)
    d$HCV_rna_score <- ifelse(lookl(d$HCV_rna, "positive"), 1, 0)
    d$HCV_body_score <- ifelse(lookl(d$HCV_body, "positive"), 1, 0)
    d$HCV_score <- ifelse(row.sums(d[, c("HCV_body_score", "HCV_rna_score")]) > 0, 1, 0)
    var <- c()
    if (HBV) 
        var <- c(var, "HBV_score")
    if (HCV) 
        var <- c(var, "HCV_score")
    d$viral.hepatitis <- ifelse(row.sums(d[, var, drop = FALSE]) > 0, 1, 0)
    if (!yes1) 
        yes1(d) <- "viral.hepatitis"
    col_rename(d) <- paste0("viral.hepatitis:", colname)
    d <- d[, c("seqn", "Year", colname)]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_youth.hypertension` [exported]

```r
function (data, years, levels = c("90th", "50th", "95th", "95th+"), Year = FALSE, join = "left") 
{
    levels <- match.arg(levels)
    if (levels == "95th+") 
        levels <- "95th+12mmHg"
    levels <- c(levels, "Height(cm)")
    years <- data_years(data, years)
    rule <- structure(list(sex = c("male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
        "male", "male", "male", "male", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
        "female", "female", "female", "female", "female", "female", "female", "female"), age = c("1", 
        "1", "1", "1", "1", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3", "4", "4", "4", "4", "4", 
        "5", "5", "5", "5", "5", "6", "6", "6", "6", "6", "7", "7", "7", "7", "7", "8", "8", "8", "8", 
        "8", "9", "9", "9", "9", "9", "10", "10", "10", "10", "10", "11", "11", "11", "11", "11", "12", 
        "12", "12", "12", "12", "13", "13", "13", "13", "13", "14", "14", "14", "14", "14", "15", "15", 
        "15", "15", "15", "16", "16", "16", "16", "16", "17", "17", "17", "17", "17", "1", "1", "1", 
        "1", "1", "2", "2", "2", "2", "2", "3", "3", "3", "3", "3", "4", "4", "4", "4", "4", "5", "5", 
        "5", "5", "5", "6", "6", "6", "6", "6", "7", "7", "7", "7", "7", "8", "8", "8", "8", "8", "9", 
        "9", "9", "9", "9", "10", "10", "10", "10", "10", "11", "11", "11", "11", "11", "12", "12", "12", 
        "12", "12", "13", "13", "13", "13", "13", "14", "14", "14", "14", "14", "15", "15", "15", "15", 
        "15", "16", "16", "16", "16", "16", "17", "17", "17", "17", "17"), levels = c("Height(cm)", "50th", 
        "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", 
        "50th", "90th", "95th", "95th+12mmHg", "Height(cm)", "50th", "90th", "95th", "95th+12mmHg"), 
        sys1 = c("77.2", "85", "98", "102", "114", "86.1", "87", "100", "104", "116", "92.5", "88", "101", 
            "106", "118", "98.5", "90", "102", "107", "119", "104.4", "91", "103", "107", "119", "110.3", 
            "93", "105", "108", "120", "116.1", "94", "106", "110", "122", "121.4", "95", "107", "111", 
            "123", "126", "96", "107", "112", "124", "130.2", "97", "108", "112", "124", "134.7", "99", 
            "110", "114", "126", "140.3", "101", "113", "116", "128", "147", "103", "115", "119", "131", 
            "153.8", "105", "119", "123", "135", "159", "108", "123", "127", "139", "162.1", "111", "126", 
            "130", "142", "163.8", "114", "128", "132", "144", "75.4", "84", "98", "101", "113", "84.9", 
            "87", "101", "104", "116", "91", "88", "102", "106", "118", "97.2", "89", "103", "107", "119", 
            "103.6", "90", "104", "108", "120", "110", "92", "105", "109", "121", "115.9", "92", "106", 
            "109", "121", "121", "93", "107", "110", "122", "125.3", "95", "108", "112", "124", "129.7", 
            "96", "109", "113", "125", "135.6", "98", "111", "115", "127", "142.8", "102", "114", "118", 
            "130", "148.1", "104", "116", "121", "133", "150.6", "105", "118", "123", "135", "151.7", 
            "105", "118", "124", "136", "152.1", "106", "119", "124", "136", "152.4", "107", "120", "125", 
            "137"), sys2 = c("78.3", "85", "99", "102", "114", "87.4", "87", "100", "105", "117", "93.9", 
            "89", "102", "106", "118", "100.2", "90", "103", "107", "119", "106.2", "92", "104", "108", 
            "120", "112.2", "93", "105", "109", "121", "118", "94", "107", "110", "122", "123.5", "96", 
            "108", "112", "124", "128.3", "97", "108", "112", "124", "132.7", "98", "109", "113", "125", 
            "137.3", "99", "111", "114", "126", "143", "101", "114", "117", "129", "150", "104", "116", 
            "120", "132", "156.9", "106", "120", "125", "137", "162", "110", "124", "129", "141", "165", 
            "112", "127", "131", "143", "166.5", "115", "129", "133", "145", "76.6", "85", "99", "102", 
            "114", "86.3", "87", "101", "105", "117", "92.4", "89", "103", "106", "118", "98.8", "90", 
            "104", "108", "120", "105.3", "91", "105", "109", "121", "111.8", "92", "106", "109", "121", 
            "117.8", "93", "106", "110", "122", "123", "94", "107", "111", "123", "127.6", "95", "108", 
            "112", "124", "132.2", "97", "110", "114", "126", "138.3", "99", "112", "116", "128", "145.5", 
            "102", "115", "119", "131", "150.6", "105", "117", "122", "134", "153", "106", "118", "123", 
            "135", "154", "106", "119", "124", "136", "154.5", "107", "120", "125", "137", "154.7", "108", 
            "121", "125", "137"), sys3 = c("80.2", "86", "99", "103", "115", "89.6", "88", "101", "105", 
            "117", "96.3", "89", "102", "107", "119", "102.9", "91", "104", "108", "120", "109.1", "93", 
            "105", "109", "121", "115.3", "94", "106", "110", "122", "121.4", "95", "108", "111", "123", 
            "127", "97", "109", "112", "124", "132.1", "98", "109", "113", "125", "136.7", "99", "111", 
            "114", "126", "141.5", "101", "112", "116", "128", "147.5", "102", "115", "118", "130", "154.9", 
            "105", "118", "122", "134", "162", "109", "123", "127", "139", "166.9", "112", "126", "131", 
            "143", "169.6", "114", "128", "133", "145", "170.9", "116", "130", "134", "146", "78.6", 
            "86", "99", "102", "114", "88.6", "88", "102", "106", "118", "94.9", "89", "104", "107", 
            "119", "101.4", "91", "105", "109", "121", "108.2", "92", "106", "109", "121", "114.9", "93", 
            "107", "110", "122", "121.1", "94", "107", "111", "123", "126.5", "95", "108", "112", "124", 
            "131.3", "97", "109", "113", "125", "136.3", "98", "111", "114", "126", "142.8", "101", "113", 
            "117", "129", "149.9", "104", "116", "120", "132", "154.7", "106", "119", "123", "135", "156.9", 
            "107", "120", "124", "136", "157.9", "107", "121", "125", "137", "158.4", "108", "122", "125", 
            "137", "158.7", "109", "123", "126", "138"), sys4 = c("82.4", "86", "100", "103", "115", 
            "92.1", "89", "102", "106", "118", "99", "90", "103", "107", "119", "105.9", "92", "105", 
            "108", "120", "112.4", "94", "106", "109", "121", "118.9", "95", "107", "111", "123", "125.1", 
            "97", "109", "112", "124", "131", "98", "110", "114", "126", "136.3", "99", "110", "115", 
            "127", "141.3", "100", "112", "116", "128", "146.4", "102", "114", "118", "130", "152.7", 
            "104", "117", "121", "133", "160.3", "108", "121", "125", "137", "167.5", "111", "126", "130", 
            "142", "172.2", "113", "128", "132", "144", "174.6", "115", "129", "134", "146", "175.8", 
            "117", "131", "135", "147", "80.8", "86", "100", "103", "115", "91.1", "89", "103", "106", 
            "118", "97.6", "90", "104", "108", "120", "104.5", "92", "106", "109", "121", "111.5", "93", 
            "107", "110", "122", "118.4", "94", "108", "111", "123", "124.9", "95", "109", "112", "124", 
            "130.6", "97", "110", "113", "125", "135.6", "98", "111", "114", "126", "141", "99", "112", 
            "116", "128", "147.8", "102", "114", "118", "130", "154.8", "105", "118", "122", "134", "159.2", 
            "107", "121", "124", "136", "161.3", "108", "122", "125", "137", "162.3", "108", "122", "126", 
            "138", "162.8", "109", "123", "127", "139", "163.0", "110", "124", "127", "139"), sys5 = c("84.6", 
            "87", "100", "104", "116", "94.7", "89", "103", "107", "119", "101.8", "91", "104", "108", 
            "120", "108.9", "93", "105", "109", "121", "115.7", "95", "107", "110", "122", "122.4", "96", 
            "109", "112", "124", "128.9", "98", "110", "114", "126", "135.1", "99", "111", "115", "127", 
            "140.7", "100", "112", "116", "128", "145.9", "101", "113", "118", "130", "151.3", "103", 
            "116", "120", "132", "157.9", "106", "119", "124", "136", "165.7", "110", "124", "128", "140", 
            "172.7", "112", "127", "132", "144", "177.2", "114", "129", "134", "146", "179.5", "115", 
            "131", "135", "147", "180.7", "117", "132", "137", "149", "83", "87", "101", "104", "116", 
            "93.7", "90", "104", "107", "119", "100.5", "91", "105", "109", "121", "107.6", "93", "107", 
            "110", "122", "114.9", "94", "108", "111", "123", "122.1", "96", "109", "112", "124", "128.8", 
            "97", "110", "113", "125", "134.7", "98", "111", "115", "127", "140.1", "99", "112", "116", 
            "128", "145.8", "101", "113", "117", "129", "152.8", "104", "116", "120", "132", "159.6", 
            "107", "120", "124", "136", "163.7", "108", "122", "126", "138", "165.7", "109", "123", "126", 
            "138", "166.7", "109", "123", "127", "139", "167.1", "109", "124", "127", "139", "167.4", 
            "110", "124", "128", "140"), sys6 = c("86.7", "88", "101", "105", "117", "97.1", "90", "103", 
            "107", "119", "104.3", "92", "105", "109", "121", "111.5", "94", "106", "110", "122", "118.6", 
            "96", "108", "111", "123", "125.6", "97", "110", "113", "125", "132.4", "98", "111", "115", 
            "127", "138.8", "99", "112", "116", "128", "144.7", "101", "113", "118", "130", "150.1", 
            "102", "115", "120", "132", "155.8", "104", "117", "123", "135", "162.6", "108", "121", "126", 
            "138", "170.5", "111", "126", "130", "142", "177.4", "113", "128", "133", "145", "181.6", 
            "114", "130", "135", "147", "183.8", "116", "131", "136", "148", "184.9", "118", "133", "138", 
            "150", "84.9", "88", "102", "105", "117", "96", "91", "105", "108", "120", "103.1", "92", 
            "106", "110", "122", "110.5", "94", "108", "111", "123", "118.1", "95", "109", "112", "124", 
            "125.6", "97", "110", "113", "125", "132.5", "98", "111", "114", "126", "138.5", "99", "112", 
            "116", "128", "144.1", "100", "113", "117", "129", "150.2", "102", "115", "119", "131", "157.3", 
            "105", "118", "123", "135", "163.8", "108", "122", "125", "137", "167.8", "108", "123", "126", 
            "138", "169.7", "109", "123", "127", "139", "170.6", "109", "123", "127", "139", "171.1", 
            "110", "124", "128", "140", "171.3", "110", "125", "128", "140"), sys7 = c("87.9", "88", 
            "101", "105", "117", "98.5", "91", "104", "108", "120", "105.8", "92", "105", "109", "121", 
            "113.2", "94", "107", "110", "122", "120.3", "96", "108", "112", "124", "127.5", "98", "110", 
            "114", "126", "134.5", "99", "111", "116", "128", "141", "100", "112", "117", "129", "147.1", 
            "101", "114", "119", "131", "152.7", "103", "116", "121", "133", "158.6", "106", "118", "124", 
            "136", "165.5", "109", "122", "128", "140", "173.4", "112", "126", "131", "143", "180.1", 
            "113", "129", "134", "146", "184.2", "114", "130", "135", "147", "186.4", "116", "132", "137", 
            "149", "187.5", "118", "134", "138", "150", "86.1", "88", "102", "105", "117", "97.4", "91", 
            "106", "109", "121", "104.6", "93", "107", "110", "122", "112.2", "94", "108", "112", "124", 
            "120", "96", "110", "113", "125", "127.7", "97", "111", "114", "126", "134.7", "99", "112", 
            "115", "127", "140.9", "100", "113", "117", "129", "146.6", "101", "114", "118", "130", "152.8", 
            "103", "116", "120", "132", "160", "106", "120", "124", "136", "166.4", "108", "122", "126", 
            "138", "170.2", "109", "123", "127", "139", "172.1", "109", "123", "127", "139", "173", "109", 
            "124", "128", "140", "173.4", "110", "124", "128", "140", "173.7", "111", "125", "128", "140"), 
        dia1 = c("77.2", "40", "52", "54", "66", "86.1", "43", "55", "57", "69", "92.5", "45", "58", 
            "60", "72", "98.5", "48", "60", "63", "75", "104.4", "51", "63", "66", "78", "110.3", "54", 
            "66", "69", "81", "116.1", "56", "68", "71", "83", "121.4", "57", "69", "72", "84", "126", 
            "57", "70", "74", "86", "130.2", "59", "72", "76", "88", "134.7", "61", "74", "77", "89", 
            "140.3", "61", "75", "78", "90", "147", "61", "74", "78", "90", "153.8", "60", "74", "77", 
            "89", "159", "61", "75", "78", "90", "162.1", "63", "77", "80", "92", "163.8", "65", "78", 
            "81", "93", "75.4", "41", "54", "59", "71", "84.9", "45", "58", "62", "74", "91", "48", "60", 
            "64", "76", "97.2", "50", "62", "66", "78", "103.6", "52", "64", "68", "80", "110", "54", 
            "67", "70", "82", "115.9", "55", "68", "72", "84", "121", "56", "69", "72", "84", "125.3", 
            "57", "71", "74", "86", "129.7", "58", "72", "75", "87", "135.6", "60", "74", "76", "88", 
            "142.8", "61", "75", "78", "90", "148.1", "62", "75", "79", "91", "150.6", "63", "76", "80", 
            "92", "151.7", "64", "76", "80", "92", "152.1", "64", "76", "80", "92", "152.4", "64", "76", 
            "80", "92"), dia2 = c("78.3", "40", "52", "54", "66", "87.4", "43", "55", "58", "70", "93.9", 
            "46", "58", "61", "73", "100.2", "49", "61", "64", "76", "106.2", "51", "64", "67", "79", 
            "112.2", "54", "66", "70", "82", "118", "56", "68", "71", "83", "123.5", "57", "70", "73", 
            "85", "128.3", "58", "71", "74", "86", "132.7", "60", "73", "76", "88", "137.3", "61", "74", 
            "78", "90", "143", "62", "75", "78", "90", "150", "60", "74", "78", "90", "156.9", "60", 
            "74", "78", "90", "162", "62", "76", "79", "91", "165", "64", "78", "81", "93", "166.5", 
            "66", "79", "82", "94", "76.6", "42", "55", "59", "71", "86.3", "46", "58", "63", "75", "92.4", 
            "48", "61", "65", "77", "98.8", "51", "63", "67", "79", "105.3", "52", "65", "69", "81", 
            "111.8", "54", "67", "71", "83", "117.8", "55", "68", "72", "84", "123", "56", "70", "73", 
            "85", "127.6", "58", "71", "74", "86", "132.2", "59", "73", "75", "87", "138.3", "60", "74", 
            "77", "89", "145.5", "61", "75", "78", "90", "150.6", "62", "75", "79", "91", "153", "63", 
            "76", "80", "92", "154", "64", "76", "80", "92", "154.5", "64", "76", "80", "92", "154.7", 
            "64", "76", "80", "92"), dia3 = c("80.2", "40", "53", "55", "67", "89.6", "44", "56", "58", 
            "70", "96.3", "46", "59", "61", "73", "102.9", "49", "62", "65", "77", "109.1", "52", "65", 
            "68", "80", "115.3", "55", "67", "70", "82", "121.4", "57", "69", "72", "84", "127", "58", 
            "70", "73", "85", "132.1", "59", "72", "75", "87", "136.7", "61", "74", "77", "89", "141.5", 
            "62", "75", "78", "90", "147.5", "62", "75", "78", "90", "154.9", "61", "74", "78", "90", 
            "162", "62", "75", "79", "91", "166.9", "64", "78", "81", "93", "169.6", "66", "79", "83", 
            "95", "170.9", "67", "80", "84", "96", "78.6", "42", "56", "60", "72", "88.6", "47", "59", 
            "63", "75", "94.9", "49", "61", "65", "77", "101.4", "51", "64", "68", "80", "108.2", "53", 
            "66", "70", "82", "114.9", "55", "68", "72", "84", "121.1", "56", "69", "73", "85", "126.5", 
            "57", "71", "74", "86", "131.3", "59", "72", "75", "87", "136.3", "59", "73", "76", "88", 
            "142.8", "60", "74", "77", "89", "149.9", "61", "75", "78", "90", "154.7", "63", "75", "79", 
            "91", "156.9", "64", "76", "80", "92", "157.9", "64", "76", "80", "92", "158.4", "65", "76", 
            "80", "92", "158.7", "65", "77", "80", "92"), dia4 = c("82.4", "41", "53", "55", "67", "92.1", 
            "44", "56", "59", "71", "99", "47", "59", "62", "74", "105.9", "50", "62", "66", "78", "112.4", 
            "53", "65", "69", "81", "118.9", "56", "68", "71", "83", "125.1", "58", "70", "73", "85", 
            "131", "59", "71", "74", "86", "136.3", "60", "73", "76", "88", "141.3", "62", "74", "77", 
            "89", "146.4", "63", "75", "78", "90", "152.7", "62", "75", "78", "90", "160.3", "62", "75", 
            "78", "90", "167.5", "64", "77", "81", "93", "172.2", "65", "79", "83", "95", "174.6", "67", 
            "80", "84", "96", "175.8", "68", "81", "85", "97", "80.8", "43", "56", "60", "72", "91.1", 
            "48", "60", "64", "76", "97.6", "50", "62", "66", "78", "104.5", "53", "65", "69", "81", 
            "111.5", "55", "67", "71", "83", "118.4", "56", "69", "72", "84", "124.9", "57", "70", "73", 
            "85", "130.6", "59", "72", "74", "86", "135.6", "60", "73", "75", "87", "141", "60", "73", 
            "76", "88", "147.8", "61", "74", "77", "89", "154.8", "62", "75", "78", "90", "159.2", "64", 
            "76", "79", "91", "161.3", "65", "76", "80", "92", "162.3", "65", "77", "81", "93", "162.8", 
            "66", "77", "81", "93", "163.0", "66", "77", "81", "93"), dia5 = c("84.6", "41", "54", "56", 
            "68", "94.7", "45", "57", "60", "72", "101.8", "48", "60", "63", "75", "108.9", "51", "63", 
            "67", "79", "115.7", "54", "66", "70", "82", "122.4", "57", "68", "72", "84", "128.9", "58", 
            "70", "73", "85", "135.1", "59", "72", "75", "87", "140.7", "61", "74", "76", "88", "145.9", 
            "63", "75", "78", "90", "151.3", "63", "75", "78", "90", "157.9", "62", "75", "78", "90", 
            "165.7", "63", "76", "80", "92", "172.7", "65", "78", "82", "94", "177.2", "66", "80", "84", 
            "96", "179.5", "68", "81", "85", "97", "180.7", "69", "82", "86", "98", "83", "44", "57", 
            "61", "73", "93.7", "49", "61", "65", "77", "100.5", "51", "63", "67", "79", "107.6", "54", 
            "66", "70", "82", "114.9", "56", "68", "72", "84", "122.1", "57", "70", "73", "85", "128.8", 
            "58", "71", "74", "86", "134.7", "60", "72", "75", "87", "140.1", "60", "73", "75", "87", 
            "145.8", "61", "73", "76", "88", "152.8", "62", "74", "77", "89", "159.6", "64", "76", "79", 
            "91", "163.7", "65", "76", "80", "92", "165.7", "66", "77", "81", "93", "166.7", "66", "77", 
            "82", "94", "167.1", "66", "78", "82", "94", "167.4", "66", "78", "82", "94"), dia6 = c("86.7", 
            "42", "54", "57", "69", "97.1", "46", "58", "61", "73", "104.3", "49", "61", "64", "76", 
            "111.5", "52", "64", "67", "79", "118.6", "55", "67", "70", "82", "125.6", "57", "69", "72", 
            "84", "132.4", "59", "71", "74", "86", "138.8", "60", "72", "75", "87", "144.7", "62", "74", 
            "77", "89", "150.1", "63", "75", "78", "90", "155.8", "63", "76", "78", "90", "162.6", "63", 
            "76", "79", "91", "170.5", "64", "77", "81", "93", "177.4", "66", "79", "83", "95", "181.6", 
            "67", "81", "85", "97", "183.8", "69", "82", "86", "98", "184.9", "70", "82", "86", "98", 
            "84.9", "45", "58", "62", "74", "96", "50", "62", "66", "78", "103.1", "53", "64", "68", 
            "80", "110.5", "55", "67", "70", "82", "118.1", "57", "69", "73", "85", "125.6", "58", "71", 
            "74", "86", "132.5", "59", "72", "74", "86", "138.5", "61", "73", "75", "87", "144.1", "61", 
            "73", "75", "87", "150.2", "61", "73", "76", "88", "157.3", "63", "75", "77", "89", "163.8", 
            "65", "76", "79", "91", "167.8", "65", "76", "80", "92", "169.7", "66", "77", "81", "93", 
            "170.6", "67", "78", "82", "94", "171.1", "67", "78", "82", "94", "171.3", "66", "78", "82", 
            "94"), dia7 = c("87.9", "42", "54", "57", "69", "98.5", "46", "58", "61", "73", "105.8", 
            "49", "61", "64", "76", "113.2", "52", "64", "68", "80", "120.3", "55", "67", "71", "83", 
            "127.5", "58", "69", "73", "85", "134.5", "59", "71", "74", "86", "141", "60", "73", "75", 
            "87", "147.1", "62", "74", "77", "89", "152.7", "64", "76", "78", "90", "158.6", "63", "76", 
            "78", "90", "165.5", "63", "76", "79", "91", "173.4", "65", "77", "81", "93", "180.1", "67", 
            "80", "84", "96", "184.2", "68", "81", "85", "97", "186.4", "69", "82", "86", "98", "187.5", 
            "70", "83", "87", "99", "86.1", "46", "58", "62", "74", "97.4", "51", "62", "66", "78", "104.6", 
            "53", "65", "69", "81", "112.2", "55", "67", "71", "83", "120", "57", "70", "73", "85", "127.7", 
            "59", "71", "74", "86", "134.7", "60", "72", "75", "87", "140.9", "61", "73", "75", "87", 
            "146.6", "61", "73", "75", "87", "152.8", "62", "73", "76", "88", "160", "64", "75", "77", 
            "89", "166.4", "65", "76", "79", "91", "170.2", "66", "76", "81", "93", "172.1", "66", "77", 
            "82", "94", "173", "67", "78", "82", "94", "173.4", "67", "78", "82", "94", "173.7", "67", 
            "78", "82", "94")), row.names = c("2", "3", "4", "5", "6", "8", "9", "10", "11", "12", "14", 
        "15", "16", "17", "18", "20", "21", "22", "23", "24", "26", "27", "28", "29", "30", "32", "33", 
        "34", "35", "36", "38", "39", "40", "41", "42", "44", "45", "46", "47", "48", "50", "51", "52", 
        "53", "54", "56", "57", "58", "59", "60", "62", "63", "64", "65", "66", "68", "69", "70", "71", 
        "72", "74", "75", "76", "77", "78", "80", "81", "82", "83", "84", "86", "87", "88", "89", "90", 
        "92", "93", "94", "95", "96", "98", "99", "100", "101", "102", "25", "31", "43", "55", "61", 
        "85", "91", "103", "111", "121", "141", "151", "161", "171", "181", "201", "211", "221", "231", 
        "241", "261", "271", "281", "291", "301", "321", "331", "341", "351", "361", "381", "391", "401", 
        "411", "421", "441", "451", "461", "471", "481", "501", "511", "521", "531", "541", "561", "571", 
        "581", "591", "601", "621", "631", "641", "651", "661", "681", "691", "701", "711", "721", "741", 
        "751", "761", "771", "781", "801", "811", "821", "831", "841", "861", "871", "881", "891", "901", 
        "921", "931", "941", "951", "961", "981", "991", "1001", "1011", "1021"), class = "data.frame")
    d <- db_blood.pressure(db_bodyMeasure(db_demo(years = years, Year = T, ageyr = "age", sex = TRUE, 
        lower_cd = T, psu_strat = F), height_cm = "height"), dar = TRUE)
    d <- d[d$age < 18, ]
    for (sexi in c("male", "female")) {
        for (bpi in c("sys", "dia")) {
            for (agei in 1:17) {
                Q <- as.numeric(rule[rule$sex == sexi & rule$age == agei & rule$levels == "Height(cm)", 
                  paste0(bpi, 1:7)])
                cutoff <- as.numeric(rule[rule$sex == sexi & rule$age == agei & rule$levels == set::not(levels, 
                  "Height(cm)"), paste0(bpi, 1:7)])
                for (i in 1:8) {
                  if (i == 1) {
                    ck <- d$sex == sexi & d$age == agei & d$height <= Q[1] & !is.na(d$height)
                    d[ck, paste0(bpi, "ck")] <- ifelse(d[ck, sprintf("bpx%sar", do::left(bpi, 1))] >= 
                      cutoff[i], 1, 0)
                  }
                  else if (i <= 7) {
                    ck <- d$sex == sexi & d$age == agei & d$height > Q[i - 1] & d$height <= Q[i] & !is.na(d$height)
                    d[ck, paste0(bpi, "ck")] <- ifelse(d[ck, sprintf("bpx%sar", do::left(bpi, 1))] >= 
                      cutoff[i], 1, 0)
                  }
                  else {
                    ck <- d$sex == sexi & d$age == agei & d$height > Q[7] & !is.na(d$height)
                    d[ck, paste0(bpi, "ck")] <- ifelse(d[ck, sprintf("bpx%sar", do::left(bpi, 1))] >= 
                      cutoff[7], 1, 0)
                  }
                }
            }
        }
    }
    d$youth.hypertension <- ifelse(row.sums(d[, c("sysck", "diack")]) > 0, "yes", "no")
    d <- d[, c("Year", "seqn", "youth.hypertension")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_youth.obesity` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_bodyMeasure(db_demo(years = years, Year = TRUE, ageyr = "age", sex = "sex", lower_cd = TRUE), 
        BMI_kg.m2 = "bmi")
    d <- d[d$age <= 18, ]
    d$obesity <- youth.obesity(d)
    d <- d[, c("seqn", "Year", "obesity")]
    return_data(data, d, Year, key = "seqn", join = join)
}
```


