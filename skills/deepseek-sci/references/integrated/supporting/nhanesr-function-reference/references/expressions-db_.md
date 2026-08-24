# Integrated supporting reference: nhanesr-function-reference/references/expressions-db_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-db_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `db_`

## `db_Alcohol.drinks` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    alq <- nhs_tsv("alq", "!~alqy", years = years, cat = FALSE)
    d <- nhs_read(alq, "alq130", lower_cd = TRUE, cat = FALSE)
    col_rename(d) <- "alq130:drinks.day"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_DSD` [exported]

```r
function (..., data, supplement_name = TRUE, supplement_type = TRUE, ingredient_name = TRUE, ingredient_unit = TRUE, 
    ingredient_category = TRUE, blend_flag = TRUE, blend_component_name = TRUE, blend_component_category = TRUE, 
    Year = FALSE, join = "left") 
{
    dsbi <- nhs_read(nhs_tsv("dsbi", cat = F)[1], lower_cd = T, cat = F, Year = F, varLabel = F)
    dsii <- nhs_read(nhs_tsv("dsii", cat = F)[1], lower_cd = T, cat = F, Year = F, varLabel = F)
    dspi <- nhs_read(nhs_tsv("dspi", cat = F)[1], lower_cd = T, cat = F, Year = F, varLabel = F)
    d <- drop_row(select_col(drop_col(dplyr::full_join(dplyr::full_join(dsbi, dsii, c("dsdiid", "dsdingr")), 
        dspi, c("dsdpid", "dsdsupp")), "dsdingid", "dsdbcid", "dsdiid", "dsdbid", "dsdoper", "dsdpid", 
        "dsdsrce", "dsdpreid", "dsdorgid", "dsdprdt", "dsdsgpf", "dsdseqf", "dsdlinrf", "dsdcntv", "dsdcntm", 
        "dsdcnta", "dsdcntb", "dsdcnto", "dsdservq", "dsdservu"), "dsdsupid", "dsdsupp", "dsdtype", "dsdingr", 
        "dsdqty", "dsdunit", "dsdcat", "dsdblflg", "dsdbcnam", "dsdbccat", "dsdprdt", "dsdservq", "dsdservu", 
        "dsdsgpf", "dsdseqf", "dsdlinrf", "dsdcntv", "dsdcntm", "dsdcnta", "dsdcntb", "dsdcnto"), is.na(dsdsupid), 
        cat = F)
    h0 <- c(...)
    if (!is.null(h0)) 
        d <- d[lookl(d$dsdingr, h0), ]
    d <- drop_row(d, is.na(d$dsdingr), cat = F)
    d <- expss::drop_all_labels(d)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "dsdsupid", "dsdsupid"), supplement_name, "dsdsupp"), supplement_type, "dsdtype"), ingredient_name, 
        "dsdingr"), "ingredient_quantity", "dsdqty"), ingredient_unit, "dsdunit"), ingredient_category, 
        "dsdcat"), blend_flag, "dsdblflg"), blend_component_name, "dsdbcnam"), blend_component_category, 
        "dsdbccat")
    d <- select_col(d, do::Replace0(var2, ":.*"))
    row.names(d) <- NULL
    col_rename(d) <- var2
    d <- unique(d)
    d$ingredient_quantity <- round(d$ingredient_quantity, 3)
    d$dsdsupid <- as.character(d$dsdsupid)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_EVD68` [exported]

```r
function (data = NULL, all = FALSE, years, wt_y2, wt_y4, d68_frm, d68_frmq, d68_953, d68_953q, d68_087, 
    d68_087q, Year = F, join = "left") 
{
    ck <- all(miss(wt_y2), miss(wt_y4), miss(d68_frm), miss(d68_frmq), miss(d68_953), miss(d68_953q), 
        miss(d68_087), miss(d68_087q))
    if (all) {
        if (ck) {
            wt_y2 <- TRUE
            wt_y4 <- TRUE
            d68_frm <- TRUE
            d68_frmq <- TRUE
            d68_953 <- TRUE
            d68_953q <- TRUE
            d68_087 <- TRUE
            d68_087q <- TRUE
        }
        else {
            if (miss(wt_y2)) 
                wt_y2 <- TRUE
            if (miss(wt_y4)) 
                wt_y4 <- TRUE
            if (miss(d68_frm)) 
                d68_frm <- TRUE
            if (miss(d68_frmq)) 
                d68_frmq <- TRUE
            if (miss(d68_953)) 
                d68_953 <- TRUE
            if (miss(d68_953q)) 
                d68_953q <- TRUE
            if (miss(d68_087)) 
                d68_087 <- TRUE
            if (miss(d68_087q)) 
                d68_087q <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(wt_y2)) 
                wt_y2 <- FALSE
            if (miss(wt_y4)) 
                wt_y4 <- FALSE
            if (miss(d68_frm)) 
                d68_frm <- FALSE
            if (miss(d68_frmq)) 
                d68_frmq <- FALSE
            if (miss(d68_953)) 
                d68_953 <- FALSE
            if (miss(d68_953q)) 
                d68_953q <- FALSE
            if (miss(d68_087)) 
                d68_087 <- FALSE
            if (miss(d68_087q)) 
                d68_087q <- FALSE
        }
    }
    if (isTRUE(wt_y2)) 
        wt_y2 = "wt_y2"
    if (isTRUE(wt_y4)) 
        wt_y4 = "wt_y4"
    if (isTRUE(d68_frm)) 
        d68_frm = "d68_frm"
    if (isTRUE(d68_frmq)) 
        d68_frmq = "d68_frmq"
    if (isTRUE(d68_953)) 
        d68_953 = "d68_953"
    if (isTRUE(d68_953q)) 
        d68_953q = "d68_953q"
    if (isTRUE(d68_087)) 
        d68_087 = "d68_087"
    if (isTRUE(d68_087q)) 
        d68_087q = "d68_087q"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "Year", "Year"), "seqn", "seqn"), wt_y2, "wtssevd2"), wt_y4, "wtssevd4"), d68_frm, "ssevfrm"), 
        d68_frmq, "ssevfrmq"), d68_953, "ssev953"), d68_953q, "ssev953q"), d68_087, "ssev087"), d68_087q, 
        "ssev087q")
    years <- data_years(data, years)
    tsv <- nhs_tsv("ssev")
    d <- nhs_read(tsv)
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `db_FoodCD` [exported]

```r
function (data, short = TRUE, long = TRUE, lower_cd = FALSE) 
{
    years <- unique(data$Year)
    fcd <- nhs_tsv("drxfcd", years = years, cat = FALSE)
    fcdvar <- "drxfdcd"
    if (short) 
        fcdvar <- c(fcdvar, "drxfcsd")
    if (long) 
        fcdvar <- c(fcdvar, "drxfcld")
    if (isFALSE(short) & isFALSE(long)) 
        return(data)
    n0 <- nhs_read(fcd, fcdvar, cat = FALSE, lower_cd = lower_cd)
    n0 <- drop_col(n0, "Year")
    if (all(c("dr1ifdcd", "dr2ifdcd") %in% colnames(data))) {
        data <- dplyr::left_join(data, n0, c(dr1ifdcd = "drxfdcd"))
        data <- dplyr::left_join(data, n0, c(dr2ifdcd = "drxfdcd"), suffix = c("_1", "_2"))
    }
    else if ("dr1ifdcd" %in% colnames(data)) {
        data <- dplyr::left_join(data, n0, c(dr1ifdcd = "drxfdcd"))
    }
    else if ("dr2ifdcd" %in% colnames(data)) {
        data <- dplyr::left_join(data, n0, c(dr2ifdcd = "drxfdcd"))
    }
    else {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5FC5><U+987B><U+662F>iff<U+6570><U+636E>"))
        if (!do::cnOS()) 
            stop("must be iff data")
    }
    return(data)
}
```

## `db_HemalBiochemistry` [exported]

```r
function (data, years, fast_glucose_mg.dl = FALSE, fast_glucose_mmol.L = FALSE, refrige_glucose_mg.dl = FALSE, 
    refrige_glucose_mmol.L = FALSE, fast_insulin_uu.ml = FALSE, fast_insulin_pmol.L = FALSE, HbA1c = FALSE, 
    Alt = FALSE, Ast = FALSE, bilirubin_total_mg.dl = FALSE, bilirubin_total_umol.L = FALSE, alkaline_phosphatase_u.L = FALSE, 
    protein_total_g.dl = FALSE, protein_total_g.L = FALSE, albumin_g.L = FALSE, albumin_g.dl = FALSE, 
    globulin_g.dl = FALSE, globulin_g.L = FALSE, gamma_glutamyl_transferase_13u.l_iu.l = FALSE, creatinine_mg.dl = FALSE, 
    creatinine_umol.L = FALSE, uric_acid_mg.dl = FALSE, uric_acid_umol.L = FALSE, blood_urea_nitrogen_mg.dl = FALSE, 
    blood_urea_nitrogen_mmol.L = FALSE, sodium_mmol.L = FALSE, phosphorus_mg.dl = FALSE, phosphorus_mmol.L = FALSE, 
    calcium_total_mg.dl = FALSE, calcium_total_mmol.L = FALSE, calcium_albumin_corrected_mg.dl = FALSE, 
    calcium_albumin_corrected_mmol.L = FALSE, potassium_mmol.L = FALSE, iron_ug.dl = FALSE, iron_umol.L = FALSE, 
    chloride_mmol.L = FALSE, osmolality_mosm.kg = FALSE, bicarbonate_mmol.L = FALSE, fast_triglyceride_mg.dl = FALSE, 
    fast_triglyceride_mmol.L = FALSE, refrige_triglycerides_mg.dl = FALSE, refrige_triglycerides_mmol.L = FALSE, 
    fast_total_cholesterol_mg.dl = FALSE, fast_total_cholesterol_mmol.L = FALSE, refrige_total_cholesterol_mg.dl = FALSE, 
    refrige_total_cholesterol_mmol.L = FALSE, hdl_cholesterol_mmol.L = FALSE, hdl_cholesterol_mg.dl = FALSE, 
    hdl_cholesterol_direct_mg.dl = FALSE, hdl_cholesterol_direct_mmol.L = FALSE, ldl_cholesterol_mmol.L = FALSE, 
    ldl_cholesterol_mg.dl = FALSE, creatine_phosphokinase_cpk_iu.L = FALSE, follicle_stimulating_hormone_iu.L = FALSE, 
    follicle_stimulating_hormone_miu.ml = FALSE, luteinizing_hormone_iu.L = FALSE, luteinizing_hormone_miu.ml = FALSE, 
    ldh_lactate_dehydrogenase_u.L = FALSE, C_reactive_protein_mg.dl = FALSE, hs_C_reactive_protein_mg.L = FALSE, 
    Year = FALSE, join = "left", wtsaf2yr = FALSE, wtsaf4yr = FALSE, all = FALSE) 
{
    if (all) {
        if (isFALSE(fast_glucose_mg.dl)) 
            fast_glucose_mg.dl <- TRUE
        if (isFALSE(fast_glucose_mmol.L)) 
            fast_glucose_mmol.L <- TRUE
        if (isFALSE(refrige_glucose_mg.dl)) 
            refrige_glucose_mg.dl <- TRUE
        if (isFALSE(refrige_glucose_mmol.L)) 
            refrige_glucose_mmol.L <- TRUE
        if (isFALSE(fast_insulin_uu.ml)) 
            fast_insulin_uu.ml <- TRUE
        if (isFALSE(fast_insulin_pmol.L)) 
            fast_insulin_pmol.L <- TRUE
        if (isFALSE(HbA1c)) 
            HbA1c <- TRUE
        if (isFALSE(Alt)) 
            Alt <- TRUE
        if (isFALSE(Ast)) 
            Ast <- TRUE
        if (isFALSE(bilirubin_total_mg.dl)) 
            bilirubin_total_mg.dl <- TRUE
        if (isFALSE(bilirubin_total_umol.L)) 
            bilirubin_total_umol.L <- TRUE
        if (isFALSE(alkaline_phosphatase_u.L)) 
            alkaline_phosphatase_u.L <- TRUE
        if (isFALSE(protein_total_g.dl)) 
            protein_total_g.dl <- TRUE
        if (isFALSE(protein_total_g.L)) 
            protein_total_g.L <- TRUE
        if (isFALSE(albumin_g.L)) 
            albumin_g.L <- TRUE
        if (isFALSE(albumin_g.dl)) 
            albumin_g.dl <- TRUE
        if (isFALSE(globulin_g.dl)) 
            globulin_g.dl <- TRUE
        if (isFALSE(globulin_g.L)) 
            globulin_g.L <- TRUE
        if (isFALSE(gamma_glutamyl_transferase_13u.l_iu.l)) 
            gamma_glutamyl_transferase_13u.l_iu.l <- TRUE
        if (isFALSE(creatinine_mg.dl)) 
            creatinine_mg.dl <- TRUE
        if (isFALSE(creatinine_umol.L)) 
            creatinine_umol.L <- TRUE
        if (isFALSE(uric_acid_mg.dl)) 
            uric_acid_mg.dl <- TRUE
        if (isFALSE(uric_acid_umol.L)) 
            uric_acid_umol.L <- TRUE
        if (isFALSE(blood_urea_nitrogen_mg.dl)) 
            blood_urea_nitrogen_mg.dl <- TRUE
        if (isFALSE(blood_urea_nitrogen_mmol.L)) 
            blood_urea_nitrogen_mmol.L <- TRUE
        if (isFALSE(sodium_mmol.L)) 
            sodium_mmol.L <- TRUE
        if (isFALSE(phosphorus_mg.dl)) 
            phosphorus_mg.dl <- TRUE
        if (isFALSE(phosphorus_mmol.L)) 
            phosphorus_mmol.L <- TRUE
        if (isFALSE(calcium_total_mg.dl)) 
            calcium_total_mg.dl <- TRUE
        if (isFALSE(calcium_total_mmol.L)) 
            calcium_total_mmol.L <- TRUE
        if (isFALSE(calcium_albumin_corrected_mg.dl)) 
            calcium_albumin_corrected_mg.dl <- TRUE
        if (isFALSE(calcium_albumin_corrected_mmol.L)) 
            calcium_albumin_corrected_mmol.L <- TRUE
        if (isFALSE(potassium_mmol.L)) 
            potassium_mmol.L <- TRUE
        if (isFALSE(iron_ug.dl)) 
            iron_ug.dl <- TRUE
        if (isFALSE(iron_umol.L)) 
            iron_umol.L <- TRUE
        if (isFALSE(chloride_mmol.L)) 
            chloride_mmol.L <- TRUE
        if (isFALSE(osmolality_mosm.kg)) 
            osmolality_mosm.kg <- TRUE
        if (isFALSE(bicarbonate_mmol.L)) 
            bicarbonate_mmol.L <- TRUE
        if (isFALSE(fast_triglyceride_mg.dl)) 
            fast_triglyceride_mg.dl <- TRUE
        if (isFALSE(fast_triglyceride_mmol.L)) 
            fast_triglyceride_mmol.L <- TRUE
        if (isFALSE(refrige_triglycerides_mg.dl)) 
            refrige_triglycerides_mg.dl <- TRUE
        if (isFALSE(refrige_triglycerides_mmol.L)) 
            refrige_triglycerides_mmol.L <- TRUE
        if (isFALSE(fast_total_cholesterol_mg.dl)) 
            fast_total_cholesterol_mg.dl <- TRUE
        if (isFALSE(fast_total_cholesterol_mmol.L)) 
            fast_total_cholesterol_mmol.L <- TRUE
        if (isFALSE(refrige_total_cholesterol_mg.dl)) 
            refrige_total_cholesterol_mg.dl <- TRUE
        if (isFALSE(refrige_total_cholesterol_mmol.L)) 
            refrige_total_cholesterol_mmol.L <- TRUE
        if (isFALSE(hdl_cholesterol_mmol.L)) 
            hdl_cholesterol_mmol.L <- TRUE
        if (isFALSE(hdl_cholesterol_mg.dl)) 
            hdl_cholesterol_mg.dl <- TRUE
        if (isFALSE(hdl_cholesterol_direct_mg.dl)) 
            hdl_cholesterol_direct_mg.dl <- TRUE
        if (isFALSE(hdl_cholesterol_direct_mmol.L)) 
            hdl_cholesterol_direct_mmol.L <- TRUE
        if (isFALSE(ldl_cholesterol_mmol.L)) 
            ldl_cholesterol_mmol.L <- TRUE
        if (isFALSE(ldl_cholesterol_mg.dl)) 
            ldl_cholesterol_mg.dl <- TRUE
        if (isFALSE(creatine_phosphokinase_cpk_iu.L)) 
            creatine_phosphokinase_cpk_iu.L <- TRUE
        if (isFALSE(follicle_stimulating_hormone_iu.L)) 
            follicle_stimulating_hormone_iu.L <- TRUE
        if (isFALSE(follicle_stimulating_hormone_miu.ml)) 
            follicle_stimulating_hormone_miu.ml <- TRUE
        if (isFALSE(luteinizing_hormone_iu.L)) 
            luteinizing_hormone_iu.L <- TRUE
        if (isFALSE(luteinizing_hormone_miu.ml)) 
            luteinizing_hormone_miu.ml <- TRUE
        if (isFALSE(ldh_lactate_dehydrogenase_u.L)) 
            ldh_lactate_dehydrogenase_u.L <- TRUE
        if (isFALSE(C_reactive_protein_mg.dl)) 
            C_reactive_protein_mg.dl <- TRUE
        if (isFALSE(hs_C_reactive_protein_mg.L)) 
            hs_C_reactive_protein_mg.L <- TRUE
    }
    years <- data_years(data, years)
    var <- c()
    d <- data.frame()
    drop_calcium_total_mg.dl <- FALSE
    drop_albumin_g.dl <- FALSE
    if (!isFALSE(calcium_albumin_corrected_mg.dl)) {
        if (isTRUE(calcium_albumin_corrected_mg.dl)) 
            calcium_albumin_corrected_mg.dl = "calcium_albumin_corrected_mg.dl"
        if (isFALSE(calcium_total_mg.dl)) {
            drop_calcium_total_mg.dl <- TRUE
            calcium_total_mg.dl <- "calcium_total_mg.dl"
        }
        else {
            drop_calcium_total_mg.dl <- FALSE
            if (isTRUE(calcium_total_mg.dl)) 
                calcium_total_mg.dl <- "calcium_total_mg.dl"
        }
        if (isFALSE(albumin_g.dl)) {
            drop_albumin_g.dl <- TRUE
            albumin_g.dl <- "albumin_g.dl"
        }
        else {
            drop_albumin_g.dl <- FALSE
            if (isTRUE(albumin_g.dl)) 
                albumin_g.dl <- "albumin_g.dl"
        }
    }
    drop_calcium_total_mmol.L <- FALSE
    drop_albumin_g.L <- FALSE
    if (!isFALSE(calcium_albumin_corrected_mmol.L)) {
        if (isTRUE(calcium_albumin_corrected_mmol.L)) 
            calcium_albumin_corrected_mmol.L = "calcium_albumin_corrected_mmol.L"
        if (isFALSE(calcium_total_mmol.L)) {
            drop_calcium_total_mmol.L <- TRUE
            calcium_total_mmol.L <- "calcium_total_mmol.L"
        }
        else {
            drop_calcium_total_mmol.L <- FALSE
            if (isTRUE(calcium_total_mmol.L)) 
                calcium_total_mmol.L <- "calcium_total_mmol.L"
        }
        if (isFALSE(albumin_g.L)) {
            drop_albumin_g.L <- TRUE
            albumin_g.L <- "albumin_g.L"
        }
        else {
            drop_albumin_g.L <- FALSE
            if (isTRUE(albumin_g.L)) 
                albumin_g.L <- "albumin_g.L"
        }
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(var, 
        fast_glucose_mg.dl, "lbxglu"), fast_glucose_mmol.L, "lbxglusi,lbdglusi"), refrige_glucose_mg.dl, 
        "lbxsgl"), refrige_glucose_mmol.L, "lbdsglsi"), fast_insulin_uu.ml, "lbxin"), fast_insulin_pmol.L, 
        "lbxinsi,lbdinsi"), HbA1c, "lbxgh"), Alt, "lbxsatsi"), Ast, "lbxsassi"), bilirubin_total_mg.dl, 
        "lbdstb,lbxstb"), bilirubin_total_umol.L, "lbdstbsi"), alkaline_phosphatase_u.L, "lbdsapsi,lbxsapsi"), 
        protein_total_g.dl, "lbxstp"), protein_total_g.L, "lbdstpsi"), albumin_g.L, "lbdsalsi"), albumin_g.dl, 
        "lbxsal"), globulin_g.dl, "lbxsgb"), globulin_g.L, "lbdsgbsi"), gamma_glutamyl_transferase_13u.l_iu.l, 
        "lbxsgtsi"), creatinine_mg.dl, "lbdscr,lbxscr"), creatinine_umol.L, "lbdscrsi"), uric_acid_mg.dl, 
        "lbxsua"), uric_acid_umol.L, "lbdsuasi"), blood_urea_nitrogen_mg.dl, "lbxsbu"), blood_urea_nitrogen_mmol.L, 
        "lbdsbusi"), sodium_mmol.L, "lbxsnasi"), phosphorus_mg.dl, "lbdsph,lbxsph"), phosphorus_mmol.L, 
        "lbdsphsi"), calcium_total_mg.dl, "lbxsca"), calcium_total_mmol.L, "lbdscasi"), potassium_mmol.L, 
        "lbxsksi"), iron_ug.dl, "lbxsir"), iron_umol.L, "lbdsirsi"), chloride_mmol.L, "lbxsclsi"), osmolality_mosm.kg, 
        "lbxsossi"), bicarbonate_mmol.L, "lbxsc3si"), fast_triglyceride_mg.dl, "lbxtr"), fast_triglyceride_mmol.L, 
        "lbdtrsi"), refrige_triglycerides_mg.dl, "lbxstr"), refrige_triglycerides_mmol.L, "lbdstrsi"), 
        fast_total_cholesterol_mg.dl, "lbxtc"), fast_total_cholesterol_mmol.L, "lbdtcsi"), refrige_total_cholesterol_mg.dl, 
        "lbxsch"), refrige_total_cholesterol_mmol.L, "lbdschsi"), hdl_cholesterol_mmol.L, "lbdhdlsi,lbdhddsi"), 
        hdl_cholesterol_mg.dl, "lbdhdl,lbxhdd,lbdhdd"), hdl_cholesterol_direct_mg.dl, "lbdhdd,lbxhdd"), 
        hdl_cholesterol_direct_mmol.L, "lbdhddsi"), ldl_cholesterol_mmol.L, "lbdldlsi"), ldl_cholesterol_mg.dl, 
        "lbdldl"), creatine_phosphokinase_cpk_iu.L, "lbxsck"), follicle_stimulating_hormone_iu.L, "lbdfshsi"), 
        follicle_stimulating_hormone_miu.ml, "lbxfsh"), luteinizing_hormone_iu.L, "lbdlhsi"), luteinizing_hormone_miu.ml, 
        "lbxlh"), ldh_lactate_dehydrogenase_u.L, "lbdsldsi,lbxsldsi"), C_reactive_protein_mg.dl, "lbxcrp"), 
        hs_C_reactive_protein_mg.L, "lbxhscrp")
    if (!is.null(var2)) {
        (gluam <- nhs_tsv("lab10am|l10am_b|l10am_c|glu|ins|lab13am|l13am_b|l13am_c|trigly|lab18|l40_b|l40_c|biopro", 
            items = "Laboratory", years = years, cat = FALSE))
        (lipid <- nhs_tsv("lab13|l13_b|l13_c|tchol_|p_tchol|hdl", years = years, cat = FALSE))
        (ghb <- nhs_tsv("lab10\\.|l10_b|l10_c|ghb", years = years, cat = FALSE))
        (crp <- nhs_tsv("lab11|l11_b|l11_c|crp", cat = FALSE, years = years))
        tsv <- unique(c(gluam, lipid, ghb, crp))
        di <- nhs_read(tsv, var2, cat = FALSE)
        if (nrow(d) == 0) {
            d <- di
        }
        else {
            d <- dplyr::full_join(d, di, "seqn")
        }
    }
    else {
        d <- NULL
    }
    if (!is.null(d)) {
        if (!isFALSE(calcium_albumin_corrected_mmol.L)) {
            d$xxxxxxxxxx <- d[, calcium_total_mmol.L] - 0.025000000000000001 * d[, albumin_g.L] + 1
            d <- col_rename(d, paste0("xxxxxxxxxx:", calcium_albumin_corrected_mmol.L))
        }
        if (drop_calcium_total_mmol.L) 
            d <- drop_col(d, calcium_total_mmol.L)
        if (drop_albumin_g.L) 
            d <- drop_col(d, albumin_g.L)
        if (!isFALSE(calcium_albumin_corrected_mg.dl)) {
            d$xxxxxxxxxx <- d[, calcium_total_mg.dl] - d[, albumin_g.dl] + 4
            d <- col_rename(d, paste0("xxxxxxxxxx:", calcium_albumin_corrected_mg.dl))
        }
        if (drop_calcium_total_mg.dl) 
            d <- drop_col(d, calcium_total_mg.dl)
        if (drop_albumin_g.dl) 
            d <- drop_col(d, albumin_g.dl)
    }
    if (wtsaf2yr | wtsaf4yr) {
        (tsv <- nhs_tsv("lab13am|l13am_b|l13am_c|trigly", cat = FALSE, years = years))
        d2 <- nhs_read(tsv, "wtsaf2yr:wtsaf2yr", "wtsafprp:wtsaf2yr", "wtsaf4yr:wtsaf4yr", nhs_tsv("glu", 
            years = 2021, cat = F), "wtsaf2yr", cat = F)
        if (!wtsaf2yr) 
            d2 <- drop_col(d2, "wtsaf2yr")
        if (!wtsaf4yr) 
            d2 <- drop_col(d2, "wtsaf4yr")
        if (is.null(d)) {
            d <- d2
        }
        else {
            d <- dplyr::left_join(d, d2, "seqn")
        }
    }
    if (is.character(d)) 
        return(d)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_IgE` [exported]

```r
function (all = FALSE, respondent.sequence.number, sIgE_ku.l, sIgE_cmt, dust.farinae_ku.l, dust.farinae_cmt, 
    dust.pteronyssinus_ku.l, dust.pteronyssin_cmt, cat_ku.l, cat_cmt, dog_ku.l, dog_cmt, cockroach_ku.l, 
    cockroach_cmt, alternaria_ku.l, alternaria_cmt, peanut_ku.l, peanut_cmt, egg_ku.l, egg_cmt, milk_ku.l, 
    milk_cmt, ragweed_ku.l, ragweed_cmt, rye.grass_ku.l, rye.grass_cmt, bermuda.grass_ku.l, bermuda.grass_cmt, 
    oak_ku.l, oak_cmt, birch_ku.l, birch_cmt, shrimp_ku.l, shrimp_cmt, aspergillus_ku.l, aspergillus_cmt, 
    thistle_ku.l, thistle_cmt, mouse_ku.l, mouse_cmt, rat_ku.l, rat_cmt, join = "left") 
{
    seqn <- "seqn"
    if (all) {
        if (missing(seqn)) 
            seqn <- TRUE
        if (missing(sIgE_ku.l)) 
            sIgE_ku.l <- TRUE
        if (missing(sIgE_cmt)) 
            sIgE_cmt <- TRUE
        if (missing(dust.farinae_ku.l)) 
            dust.farinae_ku.l <- TRUE
        if (missing(dust.farinae_cmt)) 
            dust.farinae_cmt <- TRUE
        if (missing(dust.pteronyssinus_ku.l)) 
            dust.pteronyssinus_ku.l <- TRUE
        if (missing(dust.pteronyssin_cmt)) 
            dust.pteronyssin_cmt <- TRUE
        if (missing(cat_ku.l)) 
            cat_ku.l <- TRUE
        if (missing(cat_cmt)) 
            cat_cmt <- TRUE
        if (missing(dog_ku.l)) 
            dog_ku.l <- TRUE
        if (missing(dog_cmt)) 
            dog_cmt <- TRUE
        if (missing(cockroach_ku.l)) 
            cockroach_ku.l <- TRUE
        if (missing(cockroach_cmt)) 
            cockroach_cmt <- TRUE
        if (missing(alternaria_ku.l)) 
            alternaria_ku.l <- TRUE
        if (missing(alternaria_cmt)) 
            alternaria_cmt <- TRUE
        if (missing(peanut_ku.l)) 
            peanut_ku.l <- TRUE
        if (missing(peanut_cmt)) 
            peanut_cmt <- TRUE
        if (missing(egg_ku.l)) 
            egg_ku.l <- TRUE
        if (missing(egg_cmt)) 
            egg_cmt <- TRUE
        if (missing(milk_ku.l)) 
            milk_ku.l <- TRUE
        if (missing(milk_cmt)) 
            milk_cmt <- TRUE
        if (missing(ragweed_ku.l)) 
            ragweed_ku.l <- TRUE
        if (missing(ragweed_cmt)) 
            ragweed_cmt <- TRUE
        if (missing(rye.grass_ku.l)) 
            rye.grass_ku.l <- TRUE
        if (missing(rye.grass_cmt)) 
            rye.grass_cmt <- TRUE
        if (missing(bermuda.grass_ku.l)) 
            bermuda.grass_ku.l <- TRUE
        if (missing(bermuda.grass_cmt)) 
            bermuda.grass_cmt <- TRUE
        if (missing(oak_ku.l)) 
            oak_ku.l <- TRUE
        if (missing(oak_cmt)) 
            oak_cmt <- TRUE
        if (missing(birch_ku.l)) 
            birch_ku.l <- TRUE
        if (missing(birch_cmt)) 
            birch_cmt <- TRUE
        if (missing(shrimp_ku.l)) 
            shrimp_ku.l <- TRUE
        if (missing(shrimp_cmt)) 
            shrimp_cmt <- TRUE
        if (missing(aspergillus_ku.l)) 
            aspergillus_ku.l <- TRUE
        if (missing(aspergillus_cmt)) 
            aspergillus_cmt <- TRUE
        if (missing(thistle_ku.l)) 
            thistle_ku.l <- TRUE
        if (missing(thistle_cmt)) 
            thistle_cmt <- TRUE
        if (missing(mouse_ku.l)) 
            mouse_ku.l <- TRUE
        if (missing(mouse_cmt)) 
            mouse_cmt <- TRUE
        if (missing(rat_ku.l)) 
            rat_ku.l <- TRUE
        if (missing(rat_cmt)) 
            rat_cmt <- TRUE
    }
    else {
        if (missing(seqn)) 
            seqn <- FALSE
        if (missing(sIgE_ku.l)) 
            sIgE_ku.l <- FALSE
        if (missing(sIgE_cmt)) 
            sIgE_cmt <- FALSE
        if (missing(dust.farinae_ku.l)) 
            dust.farinae_ku.l <- FALSE
        if (missing(dust.farinae_cmt)) 
            dust.farinae_cmt <- FALSE
        if (missing(dust.pteronyssinus_ku.l)) 
            dust.pteronyssinus_ku.l <- FALSE
        if (missing(dust.pteronyssin_cmt)) 
            dust.pteronyssin_cmt <- FALSE
        if (missing(cat_ku.l)) 
            cat_ku.l <- FALSE
        if (missing(cat_cmt)) 
            cat_cmt <- FALSE
        if (missing(dog_ku.l)) 
            dog_ku.l <- FALSE
        if (missing(dog_cmt)) 
            dog_cmt <- FALSE
        if (missing(cockroach_ku.l)) 
            cockroach_ku.l <- FALSE
        if (missing(cockroach_cmt)) 
            cockroach_cmt <- FALSE
        if (missing(alternaria_ku.l)) 
            alternaria_ku.l <- FALSE
        if (missing(alternaria_cmt)) 
            alternaria_cmt <- FALSE
        if (missing(peanut_ku.l)) 
            peanut_ku.l <- FALSE
        if (missing(peanut_cmt)) 
            peanut_cmt <- FALSE
        if (missing(egg_ku.l)) 
            egg_ku.l <- FALSE
        if (missing(egg_cmt)) 
            egg_cmt <- FALSE
        if (missing(milk_ku.l)) 
            milk_ku.l <- FALSE
        if (missing(milk_cmt)) 
            milk_cmt <- FALSE
        if (missing(ragweed_ku.l)) 
            ragweed_ku.l <- FALSE
        if (missing(ragweed_cmt)) 
            ragweed_cmt <- FALSE
        if (missing(rye.grass_ku.l)) 
            rye.grass_ku.l <- FALSE
        if (missing(rye.grass_cmt)) 
            rye.grass_cmt <- FALSE
        if (missing(bermuda.grass_ku.l)) 
            bermuda.grass_ku.l <- FALSE
        if (missing(bermuda.grass_cmt)) 
            bermuda.grass_cmt <- FALSE
        if (missing(oak_ku.l)) 
            oak_ku.l <- FALSE
        if (missing(oak_cmt)) 
            oak_cmt <- FALSE
        if (missing(birch_ku.l)) 
            birch_ku.l <- FALSE
        if (missing(birch_cmt)) 
            birch_cmt <- FALSE
        if (missing(shrimp_ku.l)) 
            shrimp_ku.l <- FALSE
        if (missing(shrimp_cmt)) 
            shrimp_cmt <- FALSE
        if (missing(aspergillus_ku.l)) 
            aspergillus_ku.l <- FALSE
        if (missing(aspergillus_cmt)) 
            aspergillus_cmt <- FALSE
        if (missing(thistle_ku.l)) 
            thistle_ku.l <- FALSE
        if (missing(thistle_cmt)) 
            thistle_cmt <- FALSE
        if (missing(mouse_ku.l)) 
            mouse_ku.l <- FALSE
        if (missing(mouse_cmt)) 
            mouse_cmt <- FALSE
        if (missing(rat_ku.l)) 
            rat_ku.l <- FALSE
        if (missing(rat_cmt)) 
            rat_cmt <- FALSE
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        seqn, "seqn"), sIgE_ku.l, "lbxige"), sIgE_cmt, "lbdigelc"), dust.farinae_ku.l, "lbxid2"), dust.farinae_cmt, 
        "lbdid2lc"), dust.pteronyssinus_ku.l, "lbxid1"), dust.pteronyssin_cmt, "lbdid1lc"), cat_ku.l, 
        "lbxie1"), cat_cmt, "lbdie1lc"), dog_ku.l, "lbxie5"), dog_cmt, "lbdie5lc"), cockroach_ku.l, "lbxii6"), 
        cockroach_cmt, "lbdii6lc"), alternaria_ku.l, "lbxim6"), alternaria_cmt, "lbdim6lc"), peanut_ku.l, 
        "lbxf13"), peanut_cmt, "lbdf13lc"), egg_ku.l, "lbxif1"), egg_cmt, "lbdif1lc"), milk_ku.l, "lbxif2"), 
        milk_cmt, "lbdif2lc"), ragweed_ku.l, "lbxiw1"), ragweed_cmt, "lbdiw1lc"), rye.grass_ku.l, "lbxig5"), 
        rye.grass_cmt, "lbdig5lc"), bermuda.grass_ku.l, "lbxig2"), bermuda.grass_cmt, "lbdig2lc"), oak_ku.l, 
        "lbxit7"), oak_cmt, "lbdit7lc"), birch_ku.l, "lbxit3"), birch_cmt, "lbdit3lc"), shrimp_ku.l, 
        "lbxf24"), shrimp_cmt, "lbdf24lc"), aspergillus_ku.l, "lbxim3"), aspergillus_cmt, "lbdim3lc"), 
        thistle_ku.l, "lbxw11"), thistle_cmt, "lbdw11lc"), mouse_ku.l, "lbxe72"), mouse_cmt, "lbde72lc"), 
        rat_ku.l, "lbxe74"), rat_cmt, "lbde74lc")
    tsv <- nhs_tsv("al_ige", cat = F)
    d <- nhs_read(tsv, var2, cat = F)
    d
}
```

## `db_MCD` [exported]

```r
function (data, lower_cd = FALSE) 
{
    years <- unique(data$Year)
    mcd <- nhs_tsv("drxmcd", years = years, cat = FALSE)
    n0 <- nhs_read(mcd, cat = FALSE, lower_cd = lower_cd)
    n0 <- drop_col(n0, "Year")
    if (all(c("dr1mc", "dr2mc") %in% colnames(data))) {
        data <- dplyr::left_join(data, n0, c(dr1mc = "drxmc"))
        data <- dplyr::left_join(data, n0, c(dr2mc = "drxmc"), suffix = c("_1", "_2"))
    }
    else if ("dr1mc" %in% colnames(data)) {
        data <- dplyr::left_join(data, n0, c(dr1mc = "drxmc"))
    }
    else if ("dr2mc" %in% colnames(data)) {
        data <- dplyr::left_join(data, n0, c(dr2mc = "drxmc"))
    }
    else {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+5FC5><U+987B><U+662F>iff<U+6570><U+636E>"))
        if (!do::cnOS()) 
            stop("must be iff data")
    }
    return(data)
}
```

## `db_Menopause` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (rhq <- nhs_tsv("rhq", years = years, cat = FALSE))
    d <- nhs_read(rhq, "rhd042,rhd043:menopause", lower_cd = TRUE, cat = FALSE)
    if (is.character(d)) 
        stop(tmcn::toUTF8("<U+8BE5><U+5E74><U+4EFD><U+6CA1><U+6709><U+7EDD><U+7ECF><U+6570><U+636E>"))
    d$menopause[!grepl("menop", d$menopause) & !is.na(d$menopause)] <- "no"
    d$menopause[grepl("menop", d$menopause) & !is.na(d$menopause)] <- "yes"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_PbCd` [exported]

```r
function (data, years, blood_cadmium_ug.l, blood_cadmium_umol.l, blood_cadmium_comment_code, blood_lead_ug.dl, 
    blood_lead_umol.l, blood_lead_comment_code, blood_mercury_total_ug.l, blood_mercury_total_umol.l, 
    blood_mercury_total_comment_code, blood_manganese_ug.l, blood_manganese_umol.l, blood_manganese_comment_code, 
    blood_selenium_ug.l, blood_selenium_umol.l, blood_selenium_comment_code, weight = FALSE, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("pbcd", years = years, cat = FALSE)
    if (length(tsv) == 0) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+6240><U+67E5><U+5E74><U+4EFD><U+4E2D><U+6CA1><U+6709>pbcd<U+6587><U+4EF6>"))
        if (!do::cnOS()) 
            stop("No pbcd data file in these years")
    }
    blood_wtsh2yr <- ifelse(weight, "PbCd_weight", FALSE)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        blood_cadmium_ug.l, "lbxbcd"), blood_cadmium_umol.l, "lbdbcdsi"), blood_cadmium_comment_code, 
        "lbdbcdlc"), blood_lead_ug.dl, "lbxbpb"), blood_lead_umol.l, "lbdbpbsi"), blood_lead_comment_code, 
        "lbdbpblc"), blood_mercury_total_ug.l, "lbxthg"), blood_mercury_total_umol.l, "lbdthgsi"), blood_mercury_total_comment_code, 
        "lbdthglc"), blood_manganese_ug.l, "lbxbmn"), blood_manganese_umol.l, "lbdbmnsi"), blood_manganese_comment_code, 
        "lbdbmnlc"), blood_selenium_ug.l, "lbxbse"), blood_selenium_umol.l, "lbdbsesi"), blood_selenium_comment_code, 
        "lbdbselc"), blood_wtsh2yr, "wtsh2yr")
    if (is.null(var)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+6CA1><U+6709><U+6307><U+5B9A><U+8981><U+60F3><U+63D0><U+53D6><U+7684><U+6570><U+636E>"))
        if (!do::cnOS()) 
            stop("No data specified to extract")
    }
    d <- nhs_read(tsv, var, cat = FALSE)
    if (weight) {
        d <- db_demo(d, wtmec2yr = TRUE, psu_strat = F)
        if ("PbCd_weight" %in% colnames(d)) {
            d$PbCd_weight[is.na(d$PbCd_weight)] <- d$wtmec2yr[is.na(d$PbCd_weight)]
        }
        else {
            d$PbCd_weight <- d$wtmec2yr
        }
        d <- drop_col(d, "wtmec2yr")
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_alpha.rb` [exported]

```r
function (data, join = "left", Year = F) 
{
    dir <- list.files(get_config_path(), "OralMicrobiome", ignore.case = T, full.names = T)
    file <- list.files(dir, "dada2rb-alpha", full.names = T, ignore.case = T)
    d <- data.table::fread(file, data.table = F, check.names = F)
    colnames(d)[1] <- "seqn"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_alpha.rsv` [exported]

```r
function (data, join = "left", Year = F) 
{
    dir <- list.files(get_config_path(), "OralMicrobiome", ignore.case = T, full.names = T)
    file <- list.files(dir, "dada2rsv-alpha", full.names = T, ignore.case = T)
    d <- data.table::fread(file, data.table = F, check.names = F)
    colnames(d)[1] <- "seqn"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_aux` [exported]

```r
function (data, years, self_reported_better_ear = FALSE, self_reported_better_ear2 = FALSE, excessive_cerumen_left_ear = FALSE, 
    impacted_cerumen_left_ear = FALSE, otoscopy_left_ear = FALSE, collapsing_ear_canals_left_ear = FALSE, 
    other_ear_exam_abnormality_left = FALSE, normal_otoscopy_right_ear = FALSE, excessive_cerumen_right_ear = FALSE, 
    impacted_cerumen_right_ear = FALSE, collapsing_ear_canals_right_ear = FALSE, comment_other_ear_exam_abnormality_right = FALSE, 
    tympanic_right_middle_ear_pressure_dapa = FALSE, tympanic_right_physical_volume_cc = FALSE, tympanic_right_width = FALSE, 
    tympanic_right_compliance = FALSE, tympanic_left_middle_ear_pressure_dapa = FALSE, tympanic_left_physical_volume_cc = FALSE, 
    tympanic_left_width = FALSE, tympanic_left_compliance = FALSE, which_ear_tested_first = FALSE, audio_test_mode = FALSE, 
    frequency_switch_to_manual_mode_left = FALSE, frequency_switch_to_manual_mode_right = FALSE, right_threshold_1000hz_db = FALSE, 
    right_threshold_500hz_db = FALSE, right_threshold_1000hz_2nd_read_db = FALSE, right_threshold_2000hz_db = FALSE, 
    right_threshold_3000hz_db = FALSE, right_threshold_4000hz_db = FALSE, right_threshold_6000hz_db = FALSE, 
    right_threshold_8000hz_db = FALSE, left_threshold_1000hz_db = FALSE, left_threshold_500hz_db = FALSE, 
    left_threshold_1000hz_2nd_read_db = FALSE, left_threshold_2000hz_db = FALSE, left_threshold_3000hz_db = FALSE, 
    left_threshold_4000hz_db = FALSE, left_threshold_6000hz_db = FALSE, left_threshold_8000hz_db = FALSE, 
    right_retest_threshold_1000hz_db = FALSE, right_retest_threshold_500hz_db = FALSE, right_retest_threshold_1000hz_2nd_read = FALSE, 
    right_retest_threshold_2000hz_db = FALSE, right_retest_threshold_3000hz_db = FALSE, right_retest_threshold_4000hz_db = FALSE, 
    right_retest_threshold_6000hz_db = FALSE, right_retest_threshold_8000hz_db = FALSE, left_retest_threshold_1000hz_db = FALSE, 
    left_retest_threshold_500hz_db = FALSE, left_retest_threshold_1000_2nd_read = FALSE, left_retest_threshold_2000hz_db = FALSE, 
    left_retest_threshold_3000hz_db = FALSE, left_retest_threshold_4000hz_db = FALSE, left_retest_threshold_6000hz_db = FALSE, 
    left_retest_threshold_8000hz_db = FALSE, left_ear_quality_code = FALSE, right_ear_quality_code = FALSE, 
    tympanogram_type_right_ear = FALSE, tympanogram_type_left_ear = FALSE, weight = FALSE, cat = TRUE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("aux1|aux\\.|aux_", years = years, cat = F)
    if (isTRUE(self_reported_better_ear)) 
        self_reported_better_ear <- "self_reported_better_ear"
    self_reported_better_ear2 <- ifelse(!isFALSE(self_reported_better_ear), "self_reported_better_ear2", 
        FALSE)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "exam_status", "auaexsts"), "problem_have_ear_tube", "auq010"), "problem_have_ear_tube_2", "auq011"), 
        "problem_had_cold_sinus_or_earache", "auq020"), "problem_exposed_loud_noise_music", "auq030,auq031"), 
        self_reported_better_ear, "auq050"), self_reported_better_ear2, "auq051"), excessive_cerumen_left_ear, 
        "auxloexc"), impacted_cerumen_left_ear, "auxloimc"), otoscopy_left_ear, "auxotspl"), collapsing_ear_canals_left_ear, 
        "auxlocol"), other_ear_exam_abnormality_left, "audloabc"), normal_otoscopy_right_ear, "auxrotsp"), 
        excessive_cerumen_right_ear, "auxroexc"), impacted_cerumen_right_ear, "auxroimc"), collapsing_ear_canals_right_ear, 
        "auxrocol"), comment_other_ear_exam_abnormality_right, "audroabc"), tympanic_right_middle_ear_pressure_dapa, 
        "auxtmepr"), tympanic_right_physical_volume_cc, "auxtpvr"), tympanic_right_width, "auxtwidr"), 
        tympanic_right_compliance, "auxtcomr"), tympanic_left_middle_ear_pressure_dapa, "auxtmepl"), 
        tympanic_left_physical_volume_cc, "auxtpvl"), tympanic_left_width, "auxtwidl"), tympanic_left_compliance, 
        "auxtcoml"), which_ear_tested_first, "auaear"), audio_test_mode, "auamode"), frequency_switch_to_manual_mode_left, 
        "auafmanl"), frequency_switch_to_manual_mode_right, "auafmanr"), right_threshold_1000hz_db, "auxu1k1r"), 
        right_threshold_500hz_db, "auxu500r"), right_threshold_1000hz_2nd_read_db, "auxu1k2r"), right_threshold_2000hz_db, 
        "auxu2kr"), right_threshold_3000hz_db, "auxu3kr"), right_threshold_4000hz_db, "auxu4kr"), right_threshold_6000hz_db, 
        "auxu6kr"), right_threshold_8000hz_db, "auxu8kr"), left_threshold_1000hz_db, "auxu1k1l"), left_threshold_500hz_db, 
        "auxu500l"), left_threshold_1000hz_2nd_read_db, "auxu1k2l"), left_threshold_2000hz_db, "auxu2kl"), 
        left_threshold_3000hz_db, "auxu3kl"), left_threshold_4000hz_db, "auxu4kl"), left_threshold_6000hz_db, 
        "auxu6kl"), left_threshold_8000hz_db, "auxu8kl"), right_retest_threshold_1000hz_db, "auxr1k1r"), 
        right_retest_threshold_500hz_db, "auxr5cr"), right_retest_threshold_1000hz_2nd_read, "auxr1k2r"), 
        right_retest_threshold_2000hz_db, "auxr2kr"), right_retest_threshold_3000hz_db, "auxr3kr"), right_retest_threshold_4000hz_db, 
        "auxr4kr"), right_retest_threshold_6000hz_db, "auxr6kr"), right_retest_threshold_8000hz_db, "auxr8kr"), 
        left_retest_threshold_1000hz_db, "auxr1k1l"), left_retest_threshold_500hz_db, "auxr5cl"), left_retest_threshold_1000_2nd_read, 
        "auxr1k2l"), left_retest_threshold_2000hz_db, "auxr2kl"), left_retest_threshold_3000hz_db, "auxr3kl"), 
        left_retest_threshold_4000hz_db, "auxr4kl"), left_retest_threshold_6000hz_db, "auxr6kl"), left_retest_threshold_8000hz_db, 
        "auxr8kl"), left_ear_quality_code, "aualeqc"), right_ear_quality_code, "auareqc"), tympanogram_type_right_ear, 
        "auatymtr"), tympanogram_type_left_ear, "auatymtl")
    if (weight) {
        var2 <- variable_formula(variable_formula(var2, "wtsau2yr", "wtsau2yr"), "wtsau4yr", "wtsau4yr")
    }
    d <- nhs_read(tsv, var2, lower_cd = TRUE, cat = F)
    d[d == "could not obtain"] <- NA
    d[d == "no response"] <- NA
    to_numeric(d) <- colnames(d)
    if (weight) {
        d <- db_demo(d, psu_strat = FALSE, wtmec2yr = TRUE)
        if (all(prepare_years(1999:2001) %in% d$Year)) {
            d$aux_weight[d$Year %in% prepare_years(1999:2001)] <- d$wtsau4yr[d$Year %in% prepare_years(1999:2001)]
            d$aux_weight[d$Year %in% prepare_years(2003)] <- d$wtsau2yr[d$Year %in% prepare_years(2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
            if (do::cnOS() & cat) 
                message(tmcn::toUTF8("<U+6CE8><U+610F>:<U+6240><U+63D0><U+53D6><U+7684><U+6570><U+636E><U+4E2D><U+5305><U+542B><U+4E86>1999-2000<U+548C>2001-2002<U+8FD9>4<U+5E74>,<U+8BA1><U+7B97><U+5408><U+5E76><U+6743><U+91CD><U+65F6><U+5BF9><U+8FD9>4<U+5E74><U+91C7><U+7528>2/n"))
            if (!do::cnOS() & cat) 
                message("Note: The extracted data includes the four years of 1999-2000 and 2001-2002, and these four years are used when calculating the combined weight.")
        }
        else {
            d$aux_weight[d$Year %in% prepare_years(1999:2003)] <- d$wtsau2yr[d$Year %in% prepare_years(1999:2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
        }
    }
    if ("self_reported_better_ear2" %in% colnames(d)) {
        ck <- is.na(d[, self_reported_better_ear])
        d[ck, self_reported_better_ear] <- d[ck, "self_reported_better_ear2"]
        drop_col(d) <- "self_reported_better_ear2"
    }
    d <- d[d$exam_status %in% c("complete", "partial"), ]
    problem <- colnames(d)[do::left(colnames(d), 8) == "problem_"]
    if (length(problem) > 0) {
        for (i in problem) {
            d <- d[!d[, i] %in% "yes", ]
            drop_col(d) <- i
        }
    }
    for (i in 1:ncol(d)) {
        ck <- any(lookl(d[, i], "\\(checkbox [un]{0,}checked\\)"))
        if (is.na(ck)) 
            (next)(i)
        if (ck) {
            d[, i] <- stringr::str_replace_all(d[, i], " {0,}\\(checkbox [un]{0,}checked\\) {0,}", "")
        }
    }
    drop_col(d) <- c("wtsau2yr", "wtsau2yr")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_auxar1` [exported]

```r
function (data, years, left = FALSE, right = FALSE, khz1 = FALSE, khz2 = FALSE, right_1khz = FALSE, right_2khz = FALSE, 
    left_1khz = FALSE, left_2khz = FALSE, weight = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::and(years, prepare_years(1999:2012))
    tsv0(years)
    tsv <- nhs_tsv("auxar", years = years, cat = F)
    d <- nhs_read(tsv, cat = FALSE, nrows = 1)
    var <- c()
    if (left) 
        append(var) <- colnames(d)[do::left(colnames(d), 4) == "auxl"]
    if (right) 
        append(var) <- colnames(d)[do::left(colnames(d), 4) == "auxr"]
    if (khz1) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxlr1", "auxrr1")]
    if (khz2) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxlr2", "auxrr2")]
    if (left_1khz) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxlr1")]
    if (right_1khz) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxrr1")]
    if (left_2khz) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxlr2")]
    if (right_2khz) 
        append(var) <- colnames(d)[do::left(colnames(d), 6) %in% c("auxrr2")]
    var <- unique(var)
    if (weight) {
        var <- variable_formula(variable_formula(var, "wtsau2yr", "wtsau2yr"), "wtsau4yr", "wtsau4yr")
    }
    tsv <- nhs_tsv("auxar", years = years)
    d <- nhs_read(tsv, var, cat = FALSE)
    if (weight) {
        d <- db_demo(d, psu_strat = FALSE, wtmec2yr = TRUE)
        if (all(prepare_years(1999:2001) %in% d$Year)) {
            d$aux_weight[d$Year %in% prepare_years(1999:2001)] <- d$wtsau4yr[d$Year %in% prepare_years(1999:2001)]
            d$aux_weight[d$Year %in% prepare_years(2003)] <- d$wtsau2yr[d$Year %in% prepare_years(2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
            if (do::cnOS() & cat) 
                message(tmcn::toUTF8("<U+6CE8><U+610F>:<U+6240><U+63D0><U+53D6><U+7684><U+6570><U+636E><U+4E2D><U+5305><U+542B><U+4E86>1999-2000<U+548C>2001-2002<U+8FD9>4<U+5E74>,<U+8BA1><U+7B97><U+5408><U+5E76><U+6743><U+91CD><U+65F6><U+5BF9><U+8FD9>4<U+5E74><U+91C7><U+7528>2/n"))
            if (!do::cnOS() & cat) 
                message("Note: The extracted data includes the four years of 1999-2000 and 2001-2002, and these four years are used when calculating the combined weight.")
        }
        else {
            d$aux_weight[d$Year %in% prepare_years(1999:2003)] <- d$wtsau2yr[d$Year %in% prepare_years(1999:2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
        }
    }
    drop_col(d) <- c("wtsau2yr", "wtsau2yr")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_auxar2` [exported]

```r
function (data, years, ear_tested = FALSE, sound_stimulus_level = FALSE, detected = FALSE, time = FALSE, 
    compliance = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::not(years, prepare_years(1999:2012))
    tsv0(years)
    var <- variable_formula(variable_formula(variable_formula(c(), ear_tested, "rfxsear"), sound_stimulus_level, 
        "rfxlevel"), detected, "rfxrfxdc")
    if (time) {
        append(var) <- c("rfxt001", "rfxt002", "rfxt003", "rfxt004", "rfxt005", "rfxt006", "rfxt007", 
            "rfxt008", "rfxt009", "rfxt010", "rfxt011", "rfxt012", "rfxt013", "rfxt014", "rfxt015", "rfxt016", 
            "rfxt017", "rfxt018", "rfxt019", "rfxt020", "rfxt021", "rfxt022", "rfxt023", "rfxt024", "rfxt025", 
            "rfxt026", "rfxt027", "rfxt028", "rfxt029", "rfxt030", "rfxt031", "rfxt032", "rfxt033", "rfxt034", 
            "rfxt035", "rfxt036", "rfxt037", "rfxt038", "rfxt039", "rfxt040", "rfxt041", "rfxt042", "rfxt043", 
            "rfxt044", "rfxt045", "rfxt046", "rfxt047", "rfxt048", "rfxt049", "rfxt050", "rfxt051", "rfxt052", 
            "rfxt053", "rfxt054", "rfxt055", "rfxt056", "rfxt057", "rfxt058", "rfxt059", "rfxt060", "rfxt061", 
            "rfxt062", "rfxt063", "rfxt064", "rfxt065", "rfxt066", "rfxt067", "rfxt068", "rfxt069", "rfxt070", 
            "rfxt071", "rfxt072", "rfxt073", "rfxt074", "rfxt075", "rfxt076", "rfxt077", "rfxt078", "rfxt079", 
            "rfxt080", "rfxt081", "rfxt082", "rfxt083", "rfxt084", "rfxt085", "rfxt086", "rfxt087", "rfxt088", 
            "rfxt089", "rfxt090", "rfxt091", "rfxt092", "rfxt093", "rfxt094", "rfxt095", "rfxt096", "rfxt097", 
            "rfxt098", "rfxt099", "rfxt100", "rfxt101", "rfxt102", "rfxt103", "rfxt104", "rfxt105", "rfxt106", 
            "rfxt107", "rfxt108", "rfxt109", "rfxt110", "rfxt111", "rfxt112", "rfxt113", "rfxt114", "rfxt115", 
            "rfxt116", "rfxt117", "rfxt118", "rfxt119", "rfxt120", "rfxt121", "rfxt122", "rfxt123", "rfxt124", 
            "rfxt125", "rfxt126", "rfxt127", "rfxt128", "rfxt129", "rfxt130", "rfxt131", "rfxt132", "rfxt133", 
            "rfxt134", "rfxt135", "rfxt136", "rfxt137", "rfxt138", "rfxt139", "rfxt140", "rfxt141", "rfxt142", 
            "rfxt143", "rfxt144", "rfxt145", "rfxt146", "rfxt147", "rfxt148", "rfxt149", "rfxt150", "rfxt151", 
            "rfxt152", "rfxt153", "rfxt154", "rfxt155", "rfxt156", "rfxt157", "rfxt158", "rfxt159", "rfxt160", 
            "rfxt161", "rfxt162", "rfxt163", "rfxt164", "rfxt165", "rfxt166", "rfxt167", "rfxt168", "rfxt169", 
            "rfxt170")
    }
    if (compliance) {
        append(var) <- c("rfxc001", "rfxc002", "rfxc003", "rfxc004", "rfxc005", "rfxc006", "rfxc007", 
            "rfxc008", "rfxc009", "rfxc010", "rfxc011", "rfxc012", "rfxc013", "rfxc014", "rfxc015", "rfxc016", 
            "rfxc017", "rfxc018", "rfxc019", "rfxc020", "rfxc021", "rfxc022", "rfxc023", "rfxc024", "rfxc025", 
            "rfxc026", "rfxc027", "rfxc028", "rfxc029", "rfxc030", "rfxc031", "rfxc032", "rfxc033", "rfxc034", 
            "rfxc035", "rfxc036", "rfxc037", "rfxc038", "rfxc039", "rfxc040", "rfxc041", "rfxc042", "rfxc043", 
            "rfxc044", "rfxc045", "rfxc046", "rfxc047", "rfxc048", "rfxc049", "rfxc050", "rfxc051", "rfxc052", 
            "rfxc053", "rfxc054", "rfxc055", "rfxc056", "rfxc057", "rfxc058", "rfxc059", "rfxc060", "rfxc061", 
            "rfxc062", "rfxc063", "rfxc064", "rfxc065", "rfxc066", "rfxc067", "rfxc068", "rfxc069", "rfxc070", 
            "rfxc071", "rfxc072", "rfxc073", "rfxc074", "rfxc075", "rfxc076", "rfxc077", "rfxc078", "rfxc079", 
            "rfxc080", "rfxc081", "rfxc082", "rfxc083", "rfxc084", "rfxc085", "rfxc086", "rfxc087", "rfxc088", 
            "rfxc089", "rfxc090", "rfxc091", "rfxc092", "rfxc093", "rfxc094", "rfxc095", "rfxc096", "rfxc097", 
            "rfxc098", "rfxc099", "rfxc100", "rfxc101", "rfxc102", "rfxc103", "rfxc104", "rfxc105", "rfxc106", 
            "rfxc107", "rfxc108", "rfxc109", "rfxc110", "rfxc111", "rfxc112", "rfxc113", "rfxc114", "rfxc115", 
            "rfxc116", "rfxc117", "rfxc118", "rfxc119", "rfxc120", "rfxc121", "rfxc122", "rfxc123", "rfxc124", 
            "rfxc125", "rfxc126", "rfxc127", "rfxc128", "rfxc129", "rfxc130", "rfxc131", "rfxc132", "rfxc133", 
            "rfxc134", "rfxc135", "rfxc136", "rfxc137", "rfxc138", "rfxc139", "rfxc140", "rfxc141", "rfxc142", 
            "rfxc143", "rfxc144", "rfxc145", "rfxc146", "rfxc147", "rfxc148", "rfxc149", "rfxc150", "rfxc151", 
            "rfxc152", "rfxc153", "rfxc154", "rfxc155", "rfxc156", "rfxc157", "rfxc158", "rfxc159", "rfxc160", 
            "rfxc161", "rfxc162", "rfxc163", "rfxc164", "rfxc165", "rfxc166", "rfxc167", "rfxc168", "rfxc169", 
            "rfxc170")
    }
    tsv <- nhs_tsv("auxar", years = years, cat = FALSE)
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_auxtym1` [exported]

```r
function (data, years, left = FALSE, right = FALSE, weight = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::and(years, prepare_years(1999:2012))
    tsv0(years)
    var <- c()
    if (right) {
        append(var) <- c("audtyr01", "audtyr02", "audtyr03", "audtyr04", "audtyr05", "audtyr06", "audtyr07", 
            "audtyr08", "audtyr09", "audtyr10", "audtyr11", "audtyr12", "audtyr13", "audtyr14", "audtyr15", 
            "audtyr16", "audtyr17", "audtyr18", "audtyr19", "audtyr20", "audtyr21", "audtyr22", "audtyr23", 
            "audtyr24", "audtyr25", "audtyr26", "audtyr27", "audtyr28", "audtyr29", "audtyr30", "audtyr31", 
            "audtyr32", "audtyr33", "audtyr34", "audtyr35", "audtyr36", "audtyr37", "audtyr38", "audtyr39", 
            "audtyr40", "audtyr41", "audtyr42", "audtyr43", "audtyr44", "audtyr45", "audtyr46", "audtyr47", 
            "audtyr48", "audtyr49", "audtyr50", "audtyr51", "audtyr52", "audtyr53", "audtyr54", "audtyr55", 
            "audtyr56", "audtyr57", "audtyr58", "audtyr59", "audtyr60", "audtyr61", "audtyr62", "audtyr63", 
            "audtyr64", "audtyr65", "audtyr66", "audtyr67", "audtyr68", "audtyr69", "audtyr70", "audtyr71", 
            "audtyr72", "audtyr73", "audtyr74", "audtyr75", "audtyr76", "audtyr77", "audtyr78", "audtyr79", 
            "audtyr80", "audtyr81", "audtyr82", "audtyr83", "audtyr84")
    }
    if (left) {
        append(var) <- c("audtyl01", "audtyl02", "audtyl03", "audtyl04", "audtyl05", "audtyl06", "audtyl07", 
            "audtyl08", "audtyl09", "audtyl10", "audtyl11", "audtyl12", "audtyl13", "audtyl14", "audtyl15", 
            "audtyl16", "audtyl17", "audtyl18", "audtyl19", "audtyl20", "audtyl21", "audtyl22", "audtyl23", 
            "audtyl24", "audtyl25", "audtyl26", "audtyl27", "audtyl28", "audtyl29", "audtyl30", "audtyl31", 
            "audtyl32", "audtyl33", "audtyl34", "audtyl35", "audtyl36", "audtyl37", "audtyl38", "audtyl39", 
            "audtyl40", "audtyl41", "audtyl42", "audtyl43", "audtyl44", "audtyl45", "audtyl46", "audtyl47", 
            "audtyl48", "audtyl49", "audtyl50", "audtyl51", "audtyl52", "audtyl53", "audtyl54", "audtyl55", 
            "audtyl56", "audtyl57", "audtyl58", "audtyl59", "audtyl60", "audtyl61", "audtyl62", "audtyl63", 
            "audtyl64", "audtyl65", "audtyl66", "audtyl67", "audtyl68", "audtyl69", "audtyl70", "audtyl71", 
            "audtyl72", "audtyl73", "audtyl74", "audtyl75", "audtyl76", "audtyl77", "audtyl78", "audtyl79", 
            "audtyl80", "audtyl81", "audtyl82", "audtyl83", "audtyl84")
    }
    if (weight) {
        var <- variable_formula(variable_formula(var, "wtsau2yr", "wtsau2yr"), "wtsau4yr", "wtsau4yr")
    }
    tsv <- nhs_tsv("auxtym", years = years, cat = FALSE)
    d <- nhs_read(tsv, var, cat = FALSE)
    if (weight) {
        d <- db_demo(d, psu_strat = FALSE, wtmec2yr = TRUE)
        if (all(prepare_years(1999:2001) %in% d$Year)) {
            d$aux_weight[d$Year %in% prepare_years(1999:2001)] <- d$wtsau4yr[d$Year %in% prepare_years(1999:2001)]
            d$aux_weight[d$Year %in% prepare_years(2003)] <- d$wtsau2yr[d$Year %in% prepare_years(2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
            if (do::cnOS() & cat) 
                message(tmcn::toUTF8("<U+6CE8><U+610F>:<U+6240><U+63D0><U+53D6><U+7684><U+6570><U+636E><U+4E2D><U+5305><U+542B><U+4E86>1999-2000<U+548C>2001-2002<U+8FD9>4<U+5E74>,<U+8BA1><U+7B97><U+5408><U+5E76><U+6743><U+91CD><U+65F6><U+5BF9><U+8FD9>4<U+5E74><U+91C7><U+7528>2/n"))
            if (!do::cnOS() & cat) 
                message("Note: The extracted data includes the four years of 1999-2000 and 2001-2002, and these four years are used when calculating the combined weight.")
        }
        else {
            d$aux_weight[d$Year %in% prepare_years(1999:2003)] <- d$wtsau2yr[d$Year %in% prepare_years(1999:2003)]
            d$aux_weight[!d$Year %in% prepare_years(1999:2003)] <- d$wtmec2yr[!d$Year %in% prepare_years(1999:2003)]
        }
    }
    drop_col(d) <- c("wtsau2yr", "wtsau2yr")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_auxtym2` [exported]

```r
function (data, years, ear_tested = FALSE, pressure = FALSE, admittance = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::not(years, prepare_years(1999:2012))
    tsv0(years)
    var <- variable_formula(c(), ear_tested, "tyxpear")
    if (pressure) {
        append(var) <- c("tyxp001", "tyxp002", "tyxp003", "tyxp004", "tyxp005", "tyxp006", "tyxp007", 
            "tyxp008", "tyxp009", "tyxp010", "tyxp011", "tyxp012", "tyxp013", "tyxp014", "tyxp015", "tyxp016", 
            "tyxp017", "tyxp018", "tyxp019", "tyxp020", "tyxp021", "tyxp022", "tyxp023", "tyxp024", "tyxp025", 
            "tyxp026", "tyxp027", "tyxp028", "tyxp029", "tyxp030", "tyxp031", "tyxp032", "tyxp033", "tyxp034", 
            "tyxp035", "tyxp036", "tyxp037", "tyxp038", "tyxp039", "tyxp040", "tyxp041", "tyxp042", "tyxp043", 
            "tyxp044", "tyxp045", "tyxp046", "tyxp047", "tyxp048", "tyxp049", "tyxp050", "tyxp051", "tyxp052", 
            "tyxp053", "tyxp054", "tyxp055", "tyxp056", "tyxp057", "tyxp058", "tyxp059", "tyxp060", "tyxp061", 
            "tyxp062", "tyxp063", "tyxp064", "tyxp065", "tyxp066", "tyxp067", "tyxp068", "tyxp069", "tyxp070", 
            "tyxp071", "tyxp072", "tyxp073", "tyxp074", "tyxp075", "tyxp076", "tyxp077", "tyxp078", "tyxp079", 
            "tyxp080", "tyxp081", "tyxp082", "tyxp083", "tyxp084", "tyxp085", "tyxp086", "tyxp087", "tyxp088", 
            "tyxp089", "tyxp090", "tyxp091", "tyxp092", "tyxp093", "tyxp094", "tyxp095", "tyxp096", "tyxp097", 
            "tyxp098", "tyxp099", "tyxp100", "tyxp101", "tyxp102", "tyxp103", "tyxp104", "tyxp105", "tyxp106", 
            "tyxp107", "tyxp108", "tyxp109", "tyxp110", "tyxp111", "tyxp112", "tyxp113", "tyxp114", "tyxp115", 
            "tyxp116", "tyxp117", "tyxp118", "tyxp119", "tyxp120", "tyxp121", "tyxp122", "tyxp123", "tyxp124", 
            "tyxp125", "tyxp126", "tyxp127", "tyxp128", "tyxp129", "tyxp130", "tyxp131", "tyxp132", "tyxp133", 
            "tyxp134", "tyxp135", "tyxp136", "tyxp137", "tyxp138", "tyxp139", "tyxp140", "tyxp141", "tyxp142", 
            "tyxp143", "tyxp144", "tyxp145", "tyxp146", "tyxp147", "tyxp148", "tyxp149", "tyxp150", "tyxp151", 
            "tyxp152", "tyxp153", "tyxp154", "tyxp155", "tyxp156", "tyxp157", "tyxp158", "tyxp159", "tyxp160", 
            "tyxp161", "tyxp162", "tyxp163", "tyxp164", "tyxp165", "tyxp166", "tyxp167", "tyxp168", "tyxp169", 
            "tyxp170", "tyxp171", "tyxp172", "tyxp173", "tyxp174", "tyxp175", "tyxp176", "tyxp177", "tyxp178", 
            "tyxp179", "tyxp180", "tyxp181", "tyxp182", "tyxp183", "tyxp184", "tyxp185", "tyxp186", "tyxp187", 
            "tyxp188", "tyxp189", "tyxp190", "tyxp191", "tyxp192", "tyxp193", "tyxp194", "tyxp195", "tyxp196", 
            "tyxp197", "tyxp198", "tyxp199", "tyxp200", "tyxp201", "tyxp202", "tyxp203", "tyxp204", "tyxp205", 
            "tyxp206", "tyxp207", "tyxp208", "tyxp209", "tyxp210", "tyxp211", "tyxp212", "tyxp213", "tyxp214", 
            "tyxp215", "tyxp216", "tyxp217", "tyxp218", "tyxp219", "tyxp220", "tyxp221", "tyxp222", "tyxp223", 
            "tyxp224", "tyxp225", "tyxp226", "tyxp227", "tyxp228", "tyxp229", "tyxp230", "tyxp231", "tyxp232", 
            "tyxp233", "tyxp234", "tyxp235", "tyxp236", "tyxp237", "tyxp238", "tyxp239", "tyxp240", "tyxp241", 
            "tyxp242", "tyxp243", "tyxp244", "tyxp245", "tyxp246", "tyxp247", "tyxp248", "tyxp249", "tyxp250", 
            "tyxp251", "tyxp252", "tyxp253", "tyxp254", "tyxp255", "tyxp256")
    }
    if (admittance) {
        append(var) <- c("tyxa001", "tyxa002", "tyxa003", "tyxa004", "tyxa005", "tyxa006", "tyxa007", 
            "tyxa008", "tyxa009", "tyxa010", "tyxa011", "tyxa012", "tyxa013", "tyxa014", "tyxa015", "tyxa016", 
            "tyxa017", "tyxa018", "tyxa019", "tyxa020", "tyxa021", "tyxa022", "tyxa023", "tyxa024", "tyxa025", 
            "tyxa026", "tyxa027", "tyxa028", "tyxa029", "tyxa030", "tyxa031", "tyxa032", "tyxa033", "tyxa034", 
            "tyxa035", "tyxa036", "tyxa037", "tyxa038", "tyxa039", "tyxa040", "tyxa041", "tyxa042", "tyxa043", 
            "tyxa044", "tyxa045", "tyxa046", "tyxa047", "tyxa048", "tyxa049", "tyxa050", "tyxa051", "tyxa052", 
            "tyxa053", "tyxa054", "tyxa055", "tyxa056", "tyxa057", "tyxa058", "tyxa059", "tyxa060", "tyxa061", 
            "tyxa062", "tyxa063", "tyxa064", "tyxa065", "tyxa066", "tyxa067", "tyxa068", "tyxa069", "tyxa070", 
            "tyxa071", "tyxa072", "tyxa073", "tyxa074", "tyxa075", "tyxa076", "tyxa077", "tyxa078", "tyxa079", 
            "tyxa080", "tyxa081", "tyxa082", "tyxa083", "tyxa084", "tyxa085", "tyxa086", "tyxa087", "tyxa088", 
            "tyxa089", "tyxa090", "tyxa091", "tyxa092", "tyxa093", "tyxa094", "tyxa095", "tyxa096", "tyxa097", 
            "tyxa098", "tyxa099", "tyxa100", "tyxa101", "tyxa102", "tyxa103", "tyxa104", "tyxa105", "tyxa106", 
            "tyxa107", "tyxa108", "tyxa109", "tyxa110", "tyxa111", "tyxa112", "tyxa113", "tyxa114", "tyxa115", 
            "tyxa116", "tyxa117", "tyxa118", "tyxa119", "tyxa120", "tyxa121", "tyxa122", "tyxa123", "tyxa124", 
            "tyxa125", "tyxa126", "tyxa127", "tyxa128", "tyxa129", "tyxa130", "tyxa131", "tyxa132", "tyxa133", 
            "tyxa134", "tyxa135", "tyxa136", "tyxa137", "tyxa138", "tyxa139", "tyxa140", "tyxa141", "tyxa142", 
            "tyxa143", "tyxa144", "tyxa145", "tyxa146", "tyxa147", "tyxa148", "tyxa149", "tyxa150", "tyxa151", 
            "tyxa152", "tyxa153", "tyxa154", "tyxa155", "tyxa156", "tyxa157", "tyxa158", "tyxa159", "tyxa160", 
            "tyxa161", "tyxa162", "tyxa163", "tyxa164", "tyxa165", "tyxa166", "tyxa167", "tyxa168", "tyxa169", 
            "tyxa170", "tyxa171", "tyxa172", "tyxa173", "tyxa174", "tyxa175", "tyxa176", "tyxa177", "tyxa178", 
            "tyxa179", "tyxa180", "tyxa181", "tyxa182", "tyxa183", "tyxa184", "tyxa185", "tyxa186", "tyxa187", 
            "tyxa188", "tyxa189", "tyxa190", "tyxa191", "tyxa192", "tyxa193", "tyxa194", "tyxa195", "tyxa196", 
            "tyxa197", "tyxa198", "tyxa199", "tyxa200", "tyxa201", "tyxa202", "tyxa203", "tyxa204", "tyxa205", 
            "tyxa206", "tyxa207", "tyxa208", "tyxa209", "tyxa210", "tyxa211", "tyxa212", "tyxa213", "tyxa214", 
            "tyxa215", "tyxa216", "tyxa217", "tyxa218", "tyxa219", "tyxa220", "tyxa221", "tyxa222", "tyxa223", 
            "tyxa224", "tyxa225", "tyxa226", "tyxa227", "tyxa228", "tyxa229", "tyxa230", "tyxa231", "tyxa232", 
            "tyxa233", "tyxa234", "tyxa235", "tyxa236", "tyxa237", "tyxa238", "tyxa239", "tyxa240", "tyxa241", 
            "tyxa242", "tyxa243", "tyxa244", "tyxa245", "tyxa246", "tyxa247", "tyxa248", "tyxa249", "tyxa250", 
            "tyxa251", "tyxa252", "tyxa253", "tyxa254", "tyxa255", "tyxa256")
    }
    tsv <- nhs_tsv("auxtym", years = years, cat = FALSE)
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_auxwbr` [exported]

```r
function (data, years, ear_tested = FALSE, frequency = FALSE, absorbance = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("auxwbr", years = years, cat = FALSE)
    tsv0(tsv)
    var <- variable_formula(c(), ear_tested, "wbxfear")
    if (frequency) {
        append(var) <- c("wbxf001", "wbxf002", "wbxf003", "wbxf004", "wbxf005", "wbxf006", "wbxf007", 
            "wbxf008", "wbxf009", "wbxf010", "wbxf011", "wbxf012", "wbxf013", "wbxf014", "wbxf015", "wbxf016", 
            "wbxf017", "wbxf018", "wbxf019", "wbxf020", "wbxf021", "wbxf022", "wbxf023", "wbxf024", "wbxf025", 
            "wbxf026", "wbxf027", "wbxf028", "wbxf029", "wbxf030", "wbxf031", "wbxf032", "wbxf033", "wbxf034", 
            "wbxf035", "wbxf036", "wbxf037", "wbxf038", "wbxf039", "wbxf040", "wbxf041", "wbxf042", "wbxf043", 
            "wbxf044", "wbxf045", "wbxf046", "wbxf047", "wbxf048", "wbxf049", "wbxf050", "wbxf051", "wbxf052", 
            "wbxf053", "wbxf054", "wbxf055", "wbxf056", "wbxf057", "wbxf058", "wbxf059", "wbxf060", "wbxf061", 
            "wbxf062", "wbxf063", "wbxf064", "wbxf065", "wbxf066", "wbxf067", "wbxf068", "wbxf069", "wbxf070", 
            "wbxf071", "wbxf072", "wbxf073", "wbxf074", "wbxf075", "wbxf076", "wbxf077", "wbxf078", "wbxf079", 
            "wbxf080", "wbxf081", "wbxf082", "wbxf083", "wbxf084", "wbxf085", "wbxf086", "wbxf087", "wbxf088", 
            "wbxf089", "wbxf090", "wbxf091", "wbxf092", "wbxf093", "wbxf094", "wbxf095", "wbxf096", "wbxf097", 
            "wbxf098", "wbxf099", "wbxf100", "wbxf101", "wbxf102", "wbxf103", "wbxf104", "wbxf105", "wbxf106", 
            "wbxf107")
    }
    if (absorbance) {
        append(var) <- c("wbxa001", "wbxa002", "wbxa003", "wbxa004", "wbxa005", "wbxa006", "wbxa007", 
            "wbxa008", "wbxa009", "wbxa010", "wbxa011", "wbxa012", "wbxa013", "wbxa014", "wbxa015", "wbxa016", 
            "wbxa017", "wbxa018", "wbxa019", "wbxa020", "wbxa021", "wbxa022", "wbxa023", "wbxa024", "wbxa025", 
            "wbxa026", "wbxa027", "wbxa028", "wbxa029", "wbxa030", "wbxa031", "wbxa032", "wbxa033", "wbxa034", 
            "wbxa035", "wbxa036", "wbxa037", "wbxa038", "wbxa039", "wbxa040", "wbxa041", "wbxa042", "wbxa043", 
            "wbxa044", "wbxa045", "wbxa046", "wbxa047", "wbxa048", "wbxa049", "wbxa050", "wbxa051", "wbxa052", 
            "wbxa053", "wbxa054", "wbxa055", "wbxa056", "wbxa057", "wbxa058", "wbxa059", "wbxa060", "wbxa061", 
            "wbxa062", "wbxa063", "wbxa064", "wbxa065", "wbxa066", "wbxa067", "wbxa068", "wbxa069", "wbxa070", 
            "wbxa071", "wbxa072", "wbxa073", "wbxa074", "wbxa075", "wbxa076", "wbxa077", "wbxa078", "wbxa079", 
            "wbxa080", "wbxa081", "wbxa082", "wbxa083", "wbxa084", "wbxa085", "wbxa086", "wbxa087", "wbxa088", 
            "wbxa089", "wbxa090", "wbxa091", "wbxa092", "wbxa093", "wbxa094", "wbxa095", "wbxa096", "wbxa097", 
            "wbxa098", "wbxa099", "wbxa100", "wbxa101", "wbxa102", "wbxa103", "wbxa104", "wbxa105", "wbxa106", 
            "wbxa107")
    }
    if (phase) {
        append(var) <- c("wbxp001", "wbxp002", "wbxp003", "wbxp004", "wbxp005", "wbxp006", "wbxp007", 
            "wbxp008", "wbxp009", "wbxp010", "wbxp011", "wbxp012", "wbxp013", "wbxp014", "wbxp015", "wbxp016", 
            "wbxp017", "wbxp018", "wbxp019", "wbxp020", "wbxp021", "wbxp022", "wbxp023", "wbxp024", "wbxp025", 
            "wbxp026", "wbxp027", "wbxp028", "wbxp029", "wbxp030", "wbxp031", "wbxp032", "wbxp033", "wbxp034", 
            "wbxp035", "wbxp036", "wbxp037", "wbxp038", "wbxp039", "wbxp040", "wbxp041", "wbxp042", "wbxp043", 
            "wbxp044", "wbxp045", "wbxp046", "wbxp047", "wbxp048", "wbxp049", "wbxp050", "wbxp051", "wbxp052", 
            "wbxp053", "wbxp054", "wbxp055", "wbxp056", "wbxp057", "wbxp058", "wbxp059", "wbxp060", "wbxp061", 
            "wbxp062", "wbxp063", "wbxp064", "wbxp065", "wbxp066", "wbxp067", "wbxp068", "wbxp069", "wbxp070", 
            "wbxp071", "wbxp072", "wbxp073", "wbxp074", "wbxp075", "wbxp076", "wbxp077", "wbxp078", "wbxp079", 
            "wbxp080", "wbxp081", "wbxp082", "wbxp083", "wbxp084", "wbxp085", "wbxp086", "wbxp087", "wbxp088", 
            "wbxp089", "wbxp090", "wbxp091", "wbxp092", "wbxp093", "wbxp094", "wbxp095", "wbxp096", "wbxp097", 
            "wbxp098", "wbxp099", "wbxp100", "wbxp101", "wbxp102", "wbxp103", "wbxp104", "wbxp105", "wbxp106", 
            "wbxp107")
    }
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_beta.rsv.braycurtis` [exported]

```r
function (data, join = "left", Year = F) 
{
    dir <- list.files(get_config_path(), "OralMicrobiome", ignore.case = T, full.names = T)
    file <- list.files(dir, "dada2rsv-braycurtis-beta", full.names = T, ignore.case = T)
    d <- data.table::fread(file, data.table = F, check.names = F)
    colnames(d)[1] <- "seqn"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_beta.rsv.unwunifrac` [exported]

```r
function (data, join = "left", Year = F) 
{
    dir <- list.files(get_config_path(), "OralMicrobiome", ignore.case = T, full.names = T)
    (file <- list.files(dir, "dada2rsv-unwunifrac-beta", full.names = T, ignore.case = T))
    d <- data.table::fread(file, data.table = F, check.names = F)
    colnames(d)[1] <- "seqn"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_beta.rsv.wunifrac` [exported]

```r
function (data, join = "left", Year = F) 
{
    dir <- list.files(get_config_path(), "OralMicrobiome", ignore.case = T, full.names = T)
    (file <- list.files(dir, "dada2rsv-wunifrac-beta", full.names = T, ignore.case = T))
    d <- data.table::fread(file, data.table = F, check.names = F)
    colnames(d)[1] <- "seqn"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_blood.pressure` [exported]

```r
function (data, years, bpx = TRUE, dar = TRUE, n = 4, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    (bpxtsv <- nhs_tsv("bpx", "!~bpxo_j", years = years, cat = FALSE))
    bpxvar <- c("bpxdi1,bpxodi1:bpxdi1", "bpxdi2,bpxodi2:bpxdi2", "bpxdi3,bpxodi3:bpxdi3", "bpxdi4", 
        "bpxsy1,bpxosy1:bpxsy1", "bpxsy2,bpxosy2:bpxsy2", "bpxsy3,bpxosy3:bpxsy3", "bpxsy4")
    d <- nhs_read(bpxtsv, bpxvar, cat = FALSE)
    if (dar) {
        ck2019 <- d$Year %in% prepare_years(2019:2021)
        if (any(ck2019)) 
            d$bpxsar[ck2019] <- row.means(d[ck2019, c("bpxsy1", "bpxsy2", "bpxsy3")])
        if (any(ck2019)) 
            d$bpxdar[ck2019] <- row.means(d[ck2019, c("bpxdi1", "bpxdi2", "bpxdi3")])
        if (!all(ck2019)) {
            sys <- d[!ck2019, c("bpxsy1", "bpxsy2", "bpxsy3", "bpxsy4")]
            dia <- d[!ck2019, c("bpxdi1", "bpxdi2", "bpxdi3", "bpxdi4")]
            zero4 <- row.sums(dia == 0) >= n
            dia[dia == 0] <- NA
            sys_number <- row.sums(!is.na(sys))
            dia_number <- row.sums(!is.na(dia))
            ck <- sys_number == 1
            d[!ck2019, "bpxsar"][ck] <- row.sums(sys[ck, ])
            ck <- dia_number == 1
            d[!ck2019, "bpxdar"][ck] <- row.sums(dia[ck, ])
            ck <- sys_number > 1
            d[!ck2019, "bpxsar"][ck] <- sapply(as.data.frame(t(sys[ck, ])), function(i) mean(do::complete.data(i)[-1]))
            ck <- dia_number > 1
            d[!ck2019, "bpxdar"][ck] <- sapply(as.data.frame(t(dia[ck, ])), function(i) mean(do::complete.data(i)[-1]))
            d[!ck2019, "bpxdar"][zero4] <- 0
        }
    }
    if (!bpx) 
        d <- drop_col(d, strsplit(bpxvar, ",|:") %>% unlist())
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_bodyMeasure` [exported]

```r
function (data, years, head_circumference_cm, arm_circumference_cm, upper_arm_length_cm, triceps_skinfold_mm, 
    subscapular_skinfold_mm, sagittal_abdominal_diameter_1st_cm, sagittal_abdominal_diameter_2nd_cm, 
    sagittal_abdominal_diameter_3rd_cm, sagittal_abdominal_diameter_4th_cm, average_sagittal_abdominal_diameter_cm, 
    waist_circumference_cm, hip_circumference_cm, thigh_circumference_cm, upper_leg_length_cm, maximal_calf_circumference_cm, 
    height_cm, recumbent_length_cm, Weight_kg, BMI_kg.m2, BMI_Category_Children.Adolescents, Year = FALSE, 
    join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("bmx", years = years, cat = FALSE)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        height_cm, "bmxht"), upper_arm_length_cm, "bmxarml"), arm_circumference_cm, "bmxarmc"), triceps_skinfold_mm, 
        "bmxtri"), subscapular_skinfold_mm, "bmxsub"), recumbent_length_cm, "bmxrecum"), upper_leg_length_cm, 
        "bmxleg"), thigh_circumference_cm, "bmxthicr"), head_circumference_cm, "bmxhead"), maximal_calf_circumference_cm, 
        "bmxcalf"), Weight_kg, "bmxwt"), BMI_kg.m2, "bmxbmi"), BMI_Category_Children.Adolescents, "bmdbmic"), 
        hip_circumference_cm, "bmxhip"), average_sagittal_abdominal_diameter_cm, "bmdavsad"), sagittal_abdominal_diameter_1st_cm, 
        "bmxsad1"), sagittal_abdominal_diameter_2nd_cm, "bmxsad2"), sagittal_abdominal_diameter_3rd_cm, 
        "bmxsad3"), sagittal_abdominal_diameter_4th_cm, "bmxsad4"), waist_circumference_cm, "bmxwaist")
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_carotenoid` [exported]

```r
function (data, years, day = 1, both2days = TRUE, fun = "mean", all.5 = TRUE, component = FALSE, ds = TRUE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (ds) 
        years <- set::not(prepare_years(1999:2006))
    d <- db_drtot(years = years, Year = TRUE, day = day, fun = fun, both2days = both2days, alpha_carotene_mcg = "a_carotene", 
        beta_carotene_mcg = "b_carotene", beta_cryptoxanthin_mcg = "b_cryptoxanthin", lycopene_mcg = "dr.lycopene", 
        lutein_zeaxanthin_mcg = "dr.luten.zeaxanthin")
    var2 <- c("seqn", "Year", "carotenoid")
    if (component) 
        append(var2) <- c("a_carotene", "b_carotene", "b_cryptoxanthin", "dr.lycopene", "dr.luten.zeaxanthin")
    if (ds) {
        d <- drop_row(d, d$Year %in% prepare_years(1999:2006), subtitle.space = "    ", title = ifelse(do::cnOS(), 
            tmcn::toUTF8("<U+56E0><U+4E3A>ds<U+4E3A>TRUE,<U+6240><U+4EE5><U+4E22><U+6389><U+4E86>2006<U+53CA><U+5E74><U+4EE5><U+524D><U+7684><U+6570><U+636E>"), 
            "Because ds is TRUE, the data before 2006 is discarded"))
        d <- db_dstot(d, day = day, fun = fun, both2days = both2days, lycopene_mcg = "ds.lycopene", lutein_zeaxanthin_mcg = "ds.luten.zeaxanthin")
        d$lycopene <- row.sums(d[, c("dr.lycopene", "ds.lycopene")])
        d$luten.zeaxanthin <- row.sums(d[, c("dr.luten.zeaxanthin", "ds.luten.zeaxanthin")])
        if (component) 
            append(var2) <- c("ds.lycopene", "ds.luten.zeaxanthin")
    }
    else {
        d$lycopene <- d$dr.lycopene
        d$luten.zeaxanthin <- d$dr.luten.zeaxanthin
    }
    d$carotenoid <- row.sums(d[, c("a_carotene", "b_carotene", "b_cryptoxanthin", "lycopene", "luten.zeaxanthin")], 
        na.rm = ifelse(all.5, FALSE, TRUE))
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_cbc` [exported]

```r
function (data, years, wbc_1000cells.ul, Lymphocyte_percent, Monocyte_percent, Segmented_neutrophils_percent, 
    Eosinophils_percent, Basophils_percent, lymphocyte_number_1000cells.ul, Monocyte_number_1000cells.ul, 
    Segmented_neutrophils_number_1000cells.ul, Eosinophils_number_1000cells.ul, Basophils_number_1000cells.ul, 
    Red_blood_cell_count_MillionCells.uL, hemoglobin_g.dl, hematocrit, Mean_cell_volume_fL, Mean_cell_hemoglobin_pg, 
    Mean_cell_hemoglobin_concentration_g.dL, Red_cell_distribution_width, Platelet_count_1000cells.uL, 
    Mean_platelet_volume_fL, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("lab25|l25_b|l25_c|cbc", cat = FALSE, years = years)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        wbc_1000cells.ul, "lbxwbcsi"), Lymphocyte_percent, "lbxlypct"), Monocyte_percent, "lbxmopct"), 
        Segmented_neutrophils_percent, "lbxnepct"), Eosinophils_percent, "lbxeopct"), Basophils_percent, 
        "lbxbapct"), lymphocyte_number_1000cells.ul, "lbdlymno"), Monocyte_number_1000cells.ul, "lbdmono"), 
        Segmented_neutrophils_number_1000cells.ul, "lbdneno"), Eosinophils_number_1000cells.ul, "lbdeono"), 
        Basophils_number_1000cells.ul, "lbdbano"), Red_blood_cell_count_MillionCells.uL, "lb2rbcsi,lbxrbcsi"), 
        hemoglobin_g.dl, "lbxhgb"), hematocrit, "lbxhct"), Mean_cell_volume_fL, "lbxmcvsi"), Mean_cell_hemoglobin_pg, 
        "lbxmchsi"), Mean_cell_hemoglobin_concentration_g.dL, "lbxmc"), Red_cell_distribution_width, 
        "lbxrdw"), Platelet_count_1000cells.uL, "lbxpltsi"), Mean_platelet_volume_fL, "lbxmpsi")
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_cfq` [exported]

```r
function (data, years, all = F, cfq_status = FALSE, language = FALSE, cerad_completion_status = FALSE, 
    cerad_reason_not_complete = FALSE, cerad_score_trial_1_recall = FALSE, cerad_score_trial_2_recall = FALSE, 
    cerad_score_trial_3_recall = FALSE, cerad_score_delayed_recall = FALSE, cerad_intrusion_word_count_trial_1 = FALSE, 
    cerad_intrusion_word_count_trial_2 = FALSE, cerad_intrusion_word_count_trial_3 = FALSE, cerad_intrusion_word_count_recall = FALSE, 
    animal_fluency_sample_practice_pretest = FALSE, animal_fluency_reason_not_done = FALSE, animal_fluency_score_total = FALSE, 
    digit_symbol_sample_practice_pretest = FALSE, digit_symbol_reason_not_done = FALSE, digit_symbol_score = FALSE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (all) {
        cfq_status = "cfq_status"
        language = "language"
        cerad_completion_status = "cerad_completion_status"
        cerad_reason_not_complete = "cerad_reason_not_complete"
        cerad_score_trial_1_recall = "cerad_score_trial_1_recall"
        cerad_score_trial_2_recall = "cerad_score_trial_2_recall"
        cerad_score_trial_3_recall = "cerad_score_trial_3_recall"
        cerad_score_delayed_recall = "cerad_score_delayed_recall"
        cerad_intrusion_word_count_trial_1 = "cerad_intrusion_word_count_trial_1"
        cerad_intrusion_word_count_trial_2 = "cerad_intrusion_word_count_trial_2"
        cerad_intrusion_word_count_trial_3 = "cerad_intrusion_word_count_trial_3"
        cerad_intrusion_word_count_recall = "cerad_intrusion_word_count_recall"
        animal_fluency_sample_practice_pretest = "animal_fluency_sample_practice_pretest"
        animal_fluency_reason_not_done = "animal_fluency_reason_not_done"
        animal_fluency_score_total = "animal_fluency_score_total"
        digit_symbol_sample_practice_pretest = "digit_symbol_sample_practice_pretest"
        digit_symbol_reason_not_done = "digit_symbol_reason_not_done"
        digit_symbol_score = "digit_symbol_score"
    }
    tsv <- nhs_tsv("cfq", years = years, cat = F)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        cfq_status, "cfastat"), language, "cfalang"), cerad_completion_status, "cfdccs"), cerad_reason_not_complete, 
        "cfdcrnc"), cerad_score_trial_1_recall, "cfdcst1"), cerad_score_trial_2_recall, "cfdcst2"), cerad_score_trial_3_recall, 
        "cfdcst3"), cerad_score_delayed_recall, "cfdcsr"), cerad_intrusion_word_count_trial_1, "cfdcit1"), 
        cerad_intrusion_word_count_trial_2, "cfdcit2"), cerad_intrusion_word_count_trial_3, "cfdcit3"), 
        cerad_intrusion_word_count_recall, "cfdcir"), animal_fluency_sample_practice_pretest, "cfdapp"), 
        animal_fluency_reason_not_done, "cfdarnc"), animal_fluency_score_total, "cfdast"), digit_symbol_sample_practice_pretest, 
        "cfddpp,cfd030"), digit_symbol_reason_not_done, "cfddrnc,cfd040"), digit_symbol_score, "cfdds,cfdright")
    if (length(tsv) == 0) 
        stop("no data in these years")
    d <- nhs_read(tsv, var2, cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_coffee` [exported]

```r
function (data, years, day = 1, fun = c("mean", "alone", "sum"), both2days = TRUE, unit = c("gram", "kcal", 
    "cup"), caffeinate = FALSE, sweeten = FALSE, fat = FALSE, milk = FALSE, cappuccino = FALSE, cuban = FALSE, 
    espresso = FALSE, frappuccino = FALSE, latte = FALSE, macchiato = FALSE, mexican = FALSE, mocha = FALSE, 
    turkish = FALSE, Year = FALSE, join = "left", food.code = NULL) 
{
    unit <- match.arg(unit)
    fun <- match.arg(fun)
    unit <- unit[1]
    fun <- fun[1]
    if (length(day) == 1) {
        d <- coffee.1day(years = years, unit = unit, day = day, caffeinate = caffeinate, sweeten = sweeten, 
            fat = fat, milk = milk, brewed = brewed, cappuccino = cappuccino, cuban = cuban, espresso = espresso, 
            frappuccino = frappuccino, latte = latte, macchiato = macchiato, mexican = mexican, mocha = mocha, 
            turkish = turkish, food.code = food.code)
        at <- attr(d, "food.code")
    }
    else {
        d1 <- coffee.1day(years = years, unit = unit, day = 1, caffeinate = caffeinate, sweeten = sweeten, 
            fat = fat, milk = milk, brewed = brewed, cappuccino = cappuccino, cuban = cuban, espresso = espresso, 
            frappuccino = frappuccino, latte = latte, macchiato = macchiato, mexican = mexican, mocha = mocha, 
            turkish = turkish, food.code = food.code)
        at1 <- attr(d1, "food.code")
        d2 <- coffee.1day(years = years, unit = unit, day = 2, caffeinate = caffeinate, sweeten = sweeten, 
            fat = fat, milk = milk, brewed = brewed, cappuccino = cappuccino, cuban = cuban, espresso = espresso, 
            frappuccino = frappuccino, latte = latte, macchiato = macchiato, mexican = mexican, mocha = mocha, 
            turkish = turkish, food.code = food.code)
        at2 <- attr(d2, "food.code")
        at <- unique(rbind(at1, at2))
        row.names(at) <- NULL
        head(d1)
        head(d2)
        d <- dplyr::left_join(d1, d2, c("seqn", "Year"), suffix = c(".d1", ".d2"))
        head(d)
        (commen <- unique(do::knife_right(set::grep_or(colnames(d), c("\\.d1", "\\.d2")), 3)))
        if (fun %in% c("sum", "mean")) {
            for (i in commen) {
                c12 <- paste0(i, c(".d1", ".d2"))
                cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                d$xx <- cal
                ck <- d$Year %in% c("1999-2000", "2001-2002")
                d$xx[ck] <- row.means(d[ck, c12])
                colnames(d)[ncol(d)] <- i
                d <- drop_col(d, c12)
            }
        }
    }
    d <- return_data(data, d, Year, key = "seqn", join = join)
    attr(d, "food.code") <- at
    d
}
```

## `db_coffee.time` [exported]

```r
function (data = NULL, years, day = 1, Year = F, join = "left") 
{
    years <- data_years(data, years)
    if (1 %in% day) {
        d <- db_driff(grams = T, Year = T, day = 1, years = years, time_of_eating_occasion_hh.mm = "time")
        d1 <- d[, c("Year", "seqn", "food.code", "time")]
        d1$n <- 1
        d1$n[do::left(d1$food.code, 3) != 921] <- 0
        d1$time2 <- as.numeric(d1$time)
        d1 <- d1 %>% newVb("period", time2 >= 3600 * 4 & time2 < 3600 * 12 ~ "morning", time2 >= 3600 * 
            12 & time2 < 3600 * 17 ~ "afternoon", TRUE ~ "evening")
        d1 <- group_sum(d = d1, bys = c("Year", "seqn", "period"), vars = "n")
    }
    if (2 %in% day) {
        d <- db_driff(grams = T, Year = T, day = 2, years = years, time_of_eating_occasion_hh.mm = "time")
        d2 <- d[, c("Year", "seqn", "food.code", "time")]
        d2$n <- 1
        d2$n[do::left(d2$food.code, 3) != 921] <- 0
        d2$time2 <- as.numeric(d2$time)
        d2 <- d2 %>% newVb("period", time2 >= 3600 * 4 & time2 < 3600 * 12 ~ "morning", time2 >= 3600 * 
            12 & time2 < 3600 * 17 ~ "afternoon", TRUE ~ "evening")
        d2 <- group_sum(d = d2, bys = c("Year", "seqn", "period"), vars = "n")
    }
    if (length(day) == 1) {
        if (day == 1) {
            d <- d1
        }
        else {
            d <- d2
        }
        d <- reshape2::dcast(data = d, Year + seqn ~ period, value.var = "n")
    }
    else {
        d <- full_join(d1, d2, c("Year", "seqn", "period"))
        d$n <- row.means(d[, c("n.x", "n.y")])
        d <- reshape2::dcast(data = d, Year + seqn ~ period, value.var = "n")
    }
    return_data(data, d, Year, key = "seqn", join)
}
```

## `db_demo` [exported]

```r
function (data, years, ageyr, agemth, sex, eth1, eth2, eth3, military, country_of_birth, citizenship, 
    time_in_US, edu, in_school, marital, household_size, family_size, annual_household_income, annual_family_income, 
    poverty, status, exam_month, wtint2yr, wtint4yr, wtmec2yr, wtmec4yr, psu_strat = TRUE, Year = FALSE, 
    join = "left", lower_cd = FALSE) 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("demo", years = years, cat = FALSE)
    if (!missing(edu)) {
        if (isFALSE(edu)) {
            eduname <- "edu"
        }
        else if (isTRUE(edu)) {
            eduname <- "edu"
        }
        else if (edu == "-u" & nchar(edu) == 2) {
            eduname <- "edu"
        }
        else if (edu == "-u" & nchar(edu) > 2) {
            edu <- "-u"
            eduname <- do::knife_right(edu, 2)
        }
        else if (is.character(edu)) {
            eduname <- edu
            edu <- TRUE
        }
    }
    var <- c()
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(var, 
        ageyr, "ridageyr"), agemth, "ridagemn"), sex, "riagendr"), eth1, "ridreth1"), eth2, "ridreth2"), 
        eth3, "ridreth3"), edu, "dmdeduc2"), edu, "dmdeduc3"), military, "dmqmilit,dmqmiliz"), country_of_birth, 
        "dmdborn,dmdborn2,dmdborn4"), citizenship, "dmdcitzn"), time_in_US, "dmdyrsus"), in_school, "dmdschol"), 
        marital, "dmdmartl,dmdmartz"), household_size, "dmdhhsiz"), family_size, "dmdfmsiz"), annual_household_income, 
        "indhhinc,indhhin2"), annual_family_income, "indfminc,indfmin2"), poverty, "indfmpir"), status, 
        "ridstatr"), exam_month, "ridexmon"), wtint2yr, "wtint2yr,wtintprp"), wtint4yr, "wtint4yr"), 
        wtmec2yr, "wtmec2yr,wtmecprp"), wtmec4yr, "wtmec4yr")
    var2 <- var
    var < var2
    var[var %in% c("dmdeduc2:edu", "dmdeduc3:edu")] <- c("dmdeduc2", "dmdeduc3")
    var[var %in% c("dmdeduc2:edu-u", "dmdeduc3:edu-u")] <- c("dmdeduc2-u", "dmdeduc3-u")
    d <- nhs_read(tsv, var, cat = FALSE, Year = TRUE, psu_strat = psu_strat, lower_cd = lower_cd)
    if (all(c("dmdeduc2", "dmdeduc3") %in% colnames(d))) {
        d$edu <- ifelse(is.na(d$dmdeduc2), d$dmdeduc3, d$dmdeduc2)
        d <- drop_col(d, "dmdeduc2", "dmdeduc3")
        colnames(d)[colnames(d) == "edu"] <- eduname
    }
    else if ("dmdeduc2" %in% colnames(d)) {
        colnames(d)[colnames(d) == "dmdeduc2"] <- eduname
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dnmepi` [exported]

```r
function (data, all = FALSE, xy_estimation, horvathage, hannumage, skinbloodage, phenoage, gdf15mort, 
    b2mmort, cystatincmort, timp1mort, admmort, pai1mort, leptinmort, packyrsmort, crpmort, loga1cmort, 
    grimagemort, grimage2mort, horvathtelo, yangcell, zhangage, linage, weidnerage, vidalbraloage, dunedinpoam, 
    cd8tpp, cd4tpp, nkcell, bcell, monopp, neupp, wtdn4yr, join = "left") 
{
    seqn <- T
    ck <- all(missing(seqn), missing(xy_estimation), missing(horvathage), missing(hannumage), missing(skinbloodage), 
        missing(phenoage), missing(gdf15mort), missing(b2mmort), missing(cystatincmort), missing(timp1mort), 
        missing(admmort), missing(pai1mort), missing(leptinmort), missing(packyrsmort), missing(crpmort), 
        missing(loga1cmort), missing(grimagemort), missing(grimage2mort), missing(horvathtelo), missing(yangcell), 
        missing(zhangage), missing(linage), missing(weidnerage), missing(vidalbraloage), missing(dunedinpoam), 
        missing(cd8tpp), missing(cd4tpp), missing(nkcell), missing(bcell), missing(monopp), missing(neupp), 
        missing(wtdn4yr))
    if (all) {
        if (ck) {
            seqn <- TRUE
            xy_estimation <- TRUE
            horvathage <- TRUE
            hannumage <- TRUE
            skinbloodage <- TRUE
            phenoage <- TRUE
            gdf15mort <- TRUE
            b2mmort <- TRUE
            cystatincmort <- TRUE
            timp1mort <- TRUE
            admmort <- TRUE
            pai1mort <- TRUE
            leptinmort <- TRUE
            packyrsmort <- TRUE
            crpmort <- TRUE
            loga1cmort <- TRUE
            grimagemort <- TRUE
            grimage2mort <- TRUE
            horvathtelo <- TRUE
            yangcell <- TRUE
            zhangage <- TRUE
            linage <- TRUE
            weidnerage <- TRUE
            vidalbraloage <- TRUE
            dunedinpoam <- TRUE
            cd8tpp <- TRUE
            cd4tpp <- TRUE
            nkcell <- TRUE
            bcell <- TRUE
            monopp <- TRUE
            neupp <- TRUE
            wtdn4yr <- TRUE
        }
        else {
            if (missing(seqn)) 
                seqn <- TRUE
            if (missing(xy_estimation)) 
                xy_estimation <- TRUE
            if (missing(horvathage)) 
                horvathage <- TRUE
            if (missing(hannumage)) 
                hannumage <- TRUE
            if (missing(skinbloodage)) 
                skinbloodage <- TRUE
            if (missing(phenoage)) 
                phenoage <- TRUE
            if (missing(gdf15mort)) 
                gdf15mort <- TRUE
            if (missing(b2mmort)) 
                b2mmort <- TRUE
            if (missing(cystatincmort)) 
                cystatincmort <- TRUE
            if (missing(timp1mort)) 
                timp1mort <- TRUE
            if (missing(admmort)) 
                admmort <- TRUE
            if (missing(pai1mort)) 
                pai1mort <- TRUE
            if (missing(leptinmort)) 
                leptinmort <- TRUE
            if (missing(packyrsmort)) 
                packyrsmort <- TRUE
            if (missing(crpmort)) 
                crpmort <- TRUE
            if (missing(loga1cmort)) 
                loga1cmort <- TRUE
            if (missing(grimagemort)) 
                grimagemort <- TRUE
            if (missing(grimage2mort)) 
                grimage2mort <- TRUE
            if (missing(horvathtelo)) 
                horvathtelo <- TRUE
            if (missing(yangcell)) 
                yangcell <- TRUE
            if (missing(zhangage)) 
                zhangage <- TRUE
            if (missing(linage)) 
                linage <- TRUE
            if (missing(weidnerage)) 
                weidnerage <- TRUE
            if (missing(vidalbraloage)) 
                vidalbraloage <- TRUE
            if (missing(dunedinpoam)) 
                dunedinpoam <- TRUE
            if (missing(cd8tpp)) 
                cd8tpp <- TRUE
            if (missing(cd4tpp)) 
                cd4tpp <- TRUE
            if (missing(nkcell)) 
                nkcell <- TRUE
            if (missing(bcell)) 
                bcell <- TRUE
            if (missing(monopp)) 
                monopp <- TRUE
            if (missing(neupp)) 
                neupp <- TRUE
            if (missing(wtdn4yr)) 
                wtdn4yr <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (missing(seqn)) 
                seqn <- FALSE
            if (missing(xy_estimation)) 
                xy_estimation <- FALSE
            if (missing(horvathage)) 
                horvathage <- FALSE
            if (missing(hannumage)) 
                hannumage <- FALSE
            if (missing(skinbloodage)) 
                skinbloodage <- FALSE
            if (missing(phenoage)) 
                phenoage <- FALSE
            if (missing(gdf15mort)) 
                gdf15mort <- FALSE
            if (missing(b2mmort)) 
                b2mmort <- FALSE
            if (missing(cystatincmort)) 
                cystatincmort <- FALSE
            if (missing(timp1mort)) 
                timp1mort <- FALSE
            if (missing(admmort)) 
                admmort <- FALSE
            if (missing(pai1mort)) 
                pai1mort <- FALSE
            if (missing(leptinmort)) 
                leptinmort <- FALSE
            if (missing(packyrsmort)) 
                packyrsmort <- FALSE
            if (missing(crpmort)) 
                crpmort <- FALSE
            if (missing(loga1cmort)) 
                loga1cmort <- FALSE
            if (missing(grimagemort)) 
                grimagemort <- FALSE
            if (missing(grimage2mort)) 
                grimage2mort <- FALSE
            if (missing(horvathtelo)) 
                horvathtelo <- FALSE
            if (missing(yangcell)) 
                yangcell <- FALSE
            if (missing(zhangage)) 
                zhangage <- FALSE
            if (missing(linage)) 
                linage <- FALSE
            if (missing(weidnerage)) 
                weidnerage <- FALSE
            if (missing(vidalbraloage)) 
                vidalbraloage <- FALSE
            if (missing(dunedinpoam)) 
                dunedinpoam <- FALSE
            if (missing(cd8tpp)) 
                cd8tpp <- FALSE
            if (missing(cd4tpp)) 
                cd4tpp <- FALSE
            if (missing(nkcell)) 
                nkcell <- FALSE
            if (missing(bcell)) 
                bcell <- FALSE
            if (missing(monopp)) 
                monopp <- FALSE
            if (missing(neupp)) 
                neupp <- FALSE
            if (missing(wtdn4yr)) 
                wtdn4yr <- FALSE
        }
    }
    if (isTRUE(seqn)) 
        seqn = "seqn"
    if (isTRUE(xy_estimation)) 
        xy_estimation = "xy_estimation"
    if (isTRUE(horvathage)) 
        horvathage = "horvathage"
    if (isTRUE(hannumage)) 
        hannumage = "hannumage"
    if (isTRUE(skinbloodage)) 
        skinbloodage = "skinbloodage"
    if (isTRUE(phenoage)) 
        phenoage = "phenoage"
    if (isTRUE(gdf15mort)) 
        gdf15mort = "gdf15mort"
    if (isTRUE(b2mmort)) 
        b2mmort = "b2mmort"
    if (isTRUE(cystatincmort)) 
        cystatincmort = "cystatincmort"
    if (isTRUE(timp1mort)) 
        timp1mort = "timp1mort"
    if (isTRUE(admmort)) 
        admmort = "admmort"
    if (isTRUE(pai1mort)) 
        pai1mort = "pai1mort"
    if (isTRUE(leptinmort)) 
        leptinmort = "leptinmort"
    if (isTRUE(packyrsmort)) 
        packyrsmort = "packyrsmort"
    if (isTRUE(crpmort)) 
        crpmort = "crpmort"
    if (isTRUE(loga1cmort)) 
        loga1cmort = "loga1cmort"
    if (isTRUE(grimagemort)) 
        grimagemort = "grimagemort"
    if (isTRUE(grimage2mort)) 
        grimage2mort = "grimage2mort"
    if (isTRUE(horvathtelo)) 
        horvathtelo = "horvathtelo"
    if (isTRUE(yangcell)) 
        yangcell = "yangcell"
    if (isTRUE(zhangage)) 
        zhangage = "zhangage"
    if (isTRUE(linage)) 
        linage = "linage"
    if (isTRUE(weidnerage)) 
        weidnerage = "weidnerage"
    if (isTRUE(vidalbraloage)) 
        vidalbraloage = "vidalbraloage"
    if (isTRUE(dunedinpoam)) 
        dunedinpoam = "dunedinpoam"
    if (isTRUE(cd8tpp)) 
        cd8tpp = "cd8tpp"
    if (isTRUE(cd4tpp)) 
        cd4tpp = "cd4tpp"
    if (isTRUE(nkcell)) 
        nkcell = "nkcell"
    if (isTRUE(bcell)) 
        bcell = "bcell"
    if (isTRUE(monopp)) 
        monopp = "monopp"
    if (isTRUE(neupp)) 
        neupp = "neupp"
    if (isTRUE(wtdn4yr)) 
        wtdn4yr = "wtdn4yr"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        seqn, "seqn"), xy_estimation, "xy_estimation"), horvathage, "horvathage"), hannumage, "hannumage"), 
        skinbloodage, "skinbloodage"), phenoage, "phenoage"), gdf15mort, "gdf15mort"), b2mmort, "b2mmort"), 
        cystatincmort, "cystatincmort"), timp1mort, "timp1mort"), admmort, "admmort"), pai1mort, "pai1mort"), 
        leptinmort, "leptinmort"), packyrsmort, "packyrsmort"), crpmort, "crpmort"), loga1cmort, "loga1cmort"), 
        grimagemort, "grimagemort"), grimage2mort, "grimage2mort"), horvathtelo, "horvathtelo"), yangcell, 
        "yangcell"), zhangage, "zhangage"), linage, "linage"), weidnerage, "weidnerage"), vidalbraloage, 
        "vidalbraloage"), dunedinpoam, "dunedinpoam"), cd8tpp, "cd8tpp"), cd4tpp, "cd4tpp"), nkcell, 
        "nkcell"), bcell, "bcell"), monopp, "monopp"), neupp, "neupp"), wtdn4yr, "wtdn4yr")
    tsv <- nhs_tsv("dnmepi", cat = F)
    d <- nhs_read(tsv, var2, cat = FALSE, Year = F)
    Year <- F
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.ProcessedMeat` [exported]

```r
function (data, all = FALSE, years, day = 1, Year = F, pf_meat, pf_curedmeat, cured_redmeat, total_redmeat, 
    pf_poult, unproc_poultry, cured_poultry, nug_pat_fil, total_proc_poultry, total_poultry, red_and_cured_1, 
    red_and_processed_2, join = "left") 
{
    seqn = "seqn"
    ck <- all(missing(seqn), missing(pf_meat), missing(pf_curedmeat), missing(pf_poult), missing(cured_redmeat), 
        missing(cured_poultry), missing(nug_pat_fil), missing(unproc_poultry), missing(total_redmeat), 
        missing(total_poultry), missing(total_proc_poultry), missing(red_and_cured_1), missing(red_and_processed_2))
    if (all) {
        if (ck) {
            seqn <- TRUE
            pf_meat <- TRUE
            pf_curedmeat <- TRUE
            pf_poult <- TRUE
            cured_redmeat <- TRUE
            cured_poultry <- TRUE
            nug_pat_fil <- TRUE
            unproc_poultry <- TRUE
            total_redmeat <- TRUE
            total_poultry <- TRUE
            total_proc_poultry <- TRUE
            red_and_cured_1 <- TRUE
            red_and_processed_2 <- TRUE
        }
        else {
            if (missing(seqn)) 
                seqn <- TRUE
            if (missing(pf_meat)) 
                pf_meat <- TRUE
            if (missing(pf_curedmeat)) 
                pf_curedmeat <- TRUE
            if (missing(pf_poult)) 
                pf_poult <- TRUE
            if (missing(cured_redmeat)) 
                cured_redmeat <- TRUE
            if (missing(cured_poultry)) 
                cured_poultry <- TRUE
            if (missing(nug_pat_fil)) 
                nug_pat_fil <- TRUE
            if (missing(unproc_poultry)) 
                unproc_poultry <- TRUE
            if (missing(total_redmeat)) 
                total_redmeat <- TRUE
            if (missing(total_poultry)) 
                total_poultry <- TRUE
            if (missing(total_proc_poultry)) 
                total_proc_poultry <- TRUE
            if (missing(red_and_cured_1)) 
                red_and_cured_1 <- TRUE
            if (missing(red_and_processed_2)) 
                red_and_processed_2 <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (missing(seqn)) 
                seqn <- FALSE
            if (missing(pf_meat)) 
                pf_meat <- FALSE
            if (missing(pf_curedmeat)) 
                pf_curedmeat <- FALSE
            if (missing(pf_poult)) 
                pf_poult <- FALSE
            if (missing(cured_redmeat)) 
                cured_redmeat <- FALSE
            if (missing(cured_poultry)) 
                cured_poultry <- FALSE
            if (missing(nug_pat_fil)) 
                nug_pat_fil <- FALSE
            if (missing(unproc_poultry)) 
                unproc_poultry <- FALSE
            if (missing(total_redmeat)) 
                total_redmeat <- FALSE
            if (missing(total_poultry)) 
                total_poultry <- FALSE
            if (missing(total_proc_poultry)) 
                total_proc_poultry <- FALSE
            if (missing(red_and_cured_1)) 
                red_and_cured_1 <- FALSE
            if (missing(red_and_processed_2)) 
                red_and_processed_2 <- FALSE
        }
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "seqn", "seqn"), "Year", "Year"), pf_meat, "pf_meat"), pf_curedmeat, "pf_curedmeat"), cured_redmeat, 
        "cured_redmeat"), total_redmeat, "total_redmeat"), pf_poult, "pf_poult"), unproc_poultry, "unproc_poultry"), 
        cured_poultry, "cured_poultry"), nug_pat_fil, "nug_pat_fil"), total_proc_poultry, "total_proc_poultry"), 
        total_poultry, "total_poultry"), red_and_cured_1, "red_and_cured_1"), red_and_processed_2, "red_and_processed_2")
    if (isTRUE(seqn)) 
        seqn = "seqn"
    if (isTRUE(pf_meat)) 
        pf_meat = "pf_meat"
    if (isTRUE(pf_curedmeat)) 
        pf_curedmeat = "pf_curedmeat"
    if (isTRUE(pf_poult)) 
        pf_poult = "pf_poult"
    if (isTRUE(cured_redmeat)) 
        cured_redmeat = "cured_redmeat"
    if (isTRUE(cured_poultry)) 
        cured_poultry = "cured_poultry"
    if (isTRUE(nug_pat_fil)) 
        nug_pat_fil = "nug_pat_fil"
    if (isTRUE(unproc_poultry)) 
        unproc_poultry = "unproc_poultry"
    if (isTRUE(total_redmeat)) 
        total_redmeat = "total_redmeat"
    if (isTRUE(total_poultry)) 
        total_poultry = "total_poultry"
    if (isTRUE(total_proc_poultry)) 
        total_proc_poultry = "total_proc_poultry"
    if (isTRUE(red_and_cured_1)) 
        red_and_cured_1 = "red_and_cured_1"
    if (isTRUE(red_and_processed_2)) 
        red_and_processed_2 = "red_and_processed_2"
    years <- data_years(data, years)
    version <- 1
    (file <- paste0(get_config_path(), "/attach/db_dr.ProcessedMeat_day", day, "~~version-", version, 
        ".txt"))
    if (all(file.exists(file))) {
        if (length(day) == 1) {
            d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
                ""))
        }
        else {
            d1 <- data.table::fread(file[1], data.table = F, showProgress = F, na.strings = c(NA_character_, 
                ""))
            d2 <- data.table::fread(file[2], data.table = F, showProgress = F, na.strings = c(NA_character_, 
                ""))
            d <- rbind(d1, d2)
            d <- aggregate_mean(d, by = c("seqn", "Year"), x = set::not(colnames(d), c("seqn", "Year")))
        }
    }
    else {
        stop("<U+8BF7><U+66F4><U+65B0><U+6570><U+636E>")
    }
    d <- d[d$Year %in% years, ]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `db_dr.alcoh.beverages` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    code <- c(93101000, 93102000, 93102100, 93102200, 93102300, 93106000, 93106010, 93106100, 93106500, 
        93201000, 93202000, 93301000, 93301010, 93301020, 93301030, 93301031, 93301032, 93301040, 93301045, 
        93301050, 93301060, 93301070, 93301075, 93301080, 93301083, 93301085, 93301090, 93301100, 93301110, 
        93301111, 93301115, 93301120, 93301125, 93301130, 93301132, 93301135, 93301136, 93301139, 93301140, 
        93301141, 93301142, 93301150, 93301160, 93301170, 93301181, 93301182, 93301183, 93301184, 93301190, 
        93301191, 93301200, 93301205, 93301211, 93301213, 93301214, 93301215, 93301216, 93301217, 93301218, 
        93301230, 93301240, 93301250, 93301270, 93301275, 93301280, 93301290, 93301310, 93301320, 93301330, 
        93301340, 93301360, 93301370, 93301400, 93301450, 93301500, 93301510, 93301550, 93301600, 93302000, 
        93302100, 93401010, 93401020, 93401030, 93401100, 93402000, 93403000, 93404000, 93404550, 93404560, 
        93405000, 93406000, 93501000, 93502000, 93502100, 93503000, 93504000, 93504100, 93505000, 93505100)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% code] <- 0
    d$grams[!d$food.code %in% code] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::alcoh.beverages_kcal", "grams::alcoh.beverages_grams")
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "alcoh.beverages_kcal")
    if (grams) 
        var2 <- c(var2, "alcoh.beverages_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.apple` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    code <- c(63101000, 63101110, 63101120, 63101130, 63101140, 63101150, 63101210, 63101310, 63101320, 
        63101330, 63101410, 63101420, 63101500, 63401060, 64101010, 64104010, 64104030)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% code] <- 0
    d$grams[!d$food.code %in% code] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::apple_kcal", "grams::apple_grams")
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "apple_kcal")
    if (grams) 
        var2 <- c(var2, "apple_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.bananas` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    code <- c(63107010, 63107050, 63107070, 63107080, 63107090, 63107110, 63107210, 63107310, 63107410, 
        63401990, 63402045)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% code] <- 0
    d$grams[!d$food.code %in% code] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::bananas_kcal", "grams::bananas_grams")
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "bananas_kcal")
    if (grams) 
        var2 <- c(var2, "bananas_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.fdcd` [exported]

```r
function (data, years, Year = FALSE, lower = T) 
{
    years <- data_years(data, years)
    d <- NULL
    if (any(years %in% prepare_years(1999:2001))) {
        d1 <- nhs_read(nhs_tsv("fmt", years = years, cat = F), lower_cd = F, cat = F)[, c("Year", "start", 
            "label")]
        col_rename(d1) <- c("start:food.code")
        d <- rbind(d, d1)
        d1 <- NULL
        years <- set::not(years, prepare_years(1999:2001))
    }
    if (length(years) > 0) {
        d1 <- nhs_read(nhs_tsv("fcd", years = years, cat = F), lower_cd = F, cat = F)[, c("Year", "food.code", 
            "drxfcld")]
        col_rename(d1) <- c("drxfcld:label")
        d <- rbind(d, d1)
        d1 <- NULL
    }
    if (!missing(data)) {
        dplyr::left_join(data, d, c("Year", "food.code"))
    }
    else {
        d
    }
}
```

## `db_dr.iceCream` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    code <- c(11459990, 11460000, 11460100, 11460150, 11460160, 11460170, 11460190, 11460200, 11460250, 
        11460300, 11460400, 11460410, 11460420, 11460430, 11460440, 11461000, 11461200, 11461250, 11461260, 
        11461270, 11461280, 13110000, 13110100, 13110110, 13110120, 13110130, 13110140, 13110200, 13110210, 
        13110220, 13110310, 13110320, 13110330, 13120050, 13120100, 13120110, 13120120, 13120121, 13120130, 
        13120140, 13120300, 13120310, 13120400, 13120500, 13120550, 13120700, 13120710, 13120720, 13120730, 
        13120740, 13120750, 13120760, 13120770, 13120780, 13120790, 13121000, 13121100, 13121200, 13121300, 
        13121400, 13121500, 13122100, 13122500, 13126000, 13127000, 13127010, 13130100, 13130300, 13130310, 
        13130320, 13130330, 13130340, 13130590, 13130600, 13130610, 13130620, 13130630, 13130640, 13130700, 
        13135000, 13135010, 13136000, 13140100, 13140110, 13140450, 13140500, 13140550, 13140570, 13140575, 
        13140580, 13140600, 13140630, 13140650, 13140660, 13140670, 13140680, 13140700, 13140710, 13140900, 
        13142000, 13150000, 13160150, 13160160, 13160400, 13160410, 13160420, 13161000, 13161500, 13161520, 
        13161600, 13161630, 13170000, 41480000, 41480010, 56205200, 56205230, 56205240, 11460500, 11460510, 
        11461210, 11461220, 11461300, 11461320, 13110102, 13110112, 13110460, 13110470, 13120510, 13120735, 
        13120775, 13120782, 13120784, 13120786, 13120788, 13120792, 13121120, 13140000, 13140115, 13142100, 
        13142110)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% code] <- 0
    d$grams[!d$food.code %in% code] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::iceCream_kcal", "grams::iceCream_grams")
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "iceCream_kcal")
    if (grams) 
        var2 <- c(var2, "iceCream_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.live.microbes` [exported]

```r
function (data, years, grams_Lo, grams_Med, grams_Hi, Year, join = "left") 
{
    years <- data_years(data, years)
    seqn = T
    all = FALSE
    ck <- all(missing(Year), missing(seqn), missing(grams_Lo), missing(grams_Med), missing(grams_Hi))
    if (all) {
        if (ck) {
            Year <- TRUE
            seqn <- TRUE
            grams_Lo <- TRUE
            grams_Med <- TRUE
            grams_Hi <- TRUE
        }
        else {
            if (missing(Year)) 
                Year <- TRUE
            if (missing(seqn)) 
                seqn <- TRUE
            if (missing(grams_Lo)) 
                grams_Lo <- TRUE
            if (missing(grams_Med)) 
                grams_Med <- TRUE
            if (missing(grams_Hi)) 
                grams_Hi <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (missing(Year)) 
                Year <- FALSE
            if (missing(seqn)) 
                seqn <- FALSE
            if (missing(grams_Lo)) 
                grams_Lo <- FALSE
            if (missing(grams_Med)) 
                grams_Med <- FALSE
            if (missing(grams_Hi)) 
                grams_Hi <- FALSE
        }
    }
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        Year, "Year"), seqn, "seqn"), grams_Lo, "grams_Lo"), grams_Med, "grams_Med"), grams_Hi, "grams_Hi")
    if (is.character(Year)) 
        Year = TRUE
    if (isTRUE(seqn)) 
        seqn = "seqn"
    if (isTRUE(grams_Lo)) 
        grams_Lo = "grams_Lo"
    if (isTRUE(grams_Med)) 
        grams_Med = "grams_Med"
    if (isTRUE(grams_Hi)) 
        grams_Hi = "grams_Hi"
    version <- 1
    (file <- paste0(get_config_path(), "/attach/db_dr.live.microbes~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        create_db_dr.live.microbes(version)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    d <- d[d$Year %in% years, ]
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    row.names(d) <- NULL
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.milk` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    milk.whole <- c(11111000, 11111100, 11111150, 11114350, 11115300, 11116000, 11121100, 11210050, 11211050, 
        11220000, 11511100, 11513100, 11513355, 11513381, 11513391, 11513500, 11513801, 11513851, 11514110, 
        11514320, 11519050)
    milk.nonFat <- c(11111170, 11113000, 11114320, 11115000, 11120000, 11121300, 11212050, 11511000, 
        11511300, 11511610, 11512020, 11512110, 11513300, 11513370, 11513384, 11513394, 11513700, 11513804, 
        11513854, 11514100, 11514140, 11514310, 11514350, 11519205)
    milk.reducedFat <- c(11100000, 11112110, 11112130, 11114330, 11115200, 11211400, 11511200, 11512010, 
        11512100, 11513000, 11513150, 11513350, 11513360, 11513380, 11513382, 11513390, 11513392, 11513400, 
        11513550, 11513800, 11513802, 11513850, 11513852, 11514120, 11514330, 11519040, 11519105, 11526000)
    milk.lowFat <- c(11111160, 11112120, 11112210, 11114300, 11115100, 11115400, 11121210, 11511400, 
        11511550, 11511600, 11511700, 11513200, 11513365, 11513383, 11513393, 11513600, 11513803, 11513853, 
        11514130, 11514340, 11519200, 11519210)
    milk.substitutes <- c(11300100, 11320000, 11320100, 11320200, 11321000, 11321100, 11321200, 11340000, 
        11350000, 11350010, 11350020, 11350030, 11360000, 11370000, 11512030, 11512120, 11513310, 11513375, 
        11513385, 11513395, 11513750, 11513805, 11513855, 11514150, 11514360, 11519215, 42401010, 42402010)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$milk.whole_kcal <- d$energy_kcal
    d$milk.whole_kcal[!d$food.code %in% milk.whole] <- 0
    d$milk.nonFat_kcal <- d$energy_kcal
    d$milk.nonFat_kcal[!d$food.code %in% milk.nonFat] <- 0
    d$milk.reducedFat_kcal <- d$energy_kcal
    d$milk.reducedFat_kcal[!d$food.code %in% milk.reducedFat] <- 0
    d$milk.lowFat_kcal <- d$energy_kcal
    d$milk.lowFat_kcal[!d$food.code %in% milk.lowFat] <- 0
    d$milk.substitutes_kcal <- d$energy_kcal
    d$milk.substitutes_kcal[!d$food.code %in% milk.substitutes] <- 0
    d$milk.whole_grams <- d$grams
    d$milk.whole_grams[!d$food.code %in% milk.whole] <- 0
    d$milk.nonFat_grams <- d$grams
    d$milk.nonFat_grams[!d$food.code %in% milk.nonFat] <- 0
    d$milk.reducedFat_grams <- d$grams
    d$milk.reducedFat_grams[!d$food.code %in% milk.reducedFat] <- 0
    d$milk.lowFat_grams <- d$grams
    d$milk.lowFat_grams[!d$food.code %in% milk.lowFat] <- 0
    d$milk.substitutes_grams <- d$energy_kcal
    d$milk.substitutes_grams[!d$food.code %in% milk.substitutes] <- 0
    d <- aggregate_sum(data = d, x = c("milk.whole_kcal", "milk.whole_grams", "milk.nonFat_kcal", "milk.nonFat_grams", 
        "milk.reducedFat_kcal", "milk.reducedFat_grams", "milk.lowFat_kcal", "milk.lowFat_grams", "milk.substitutes_kcal", 
        "milk.substitutes_grams"), by = c("seqn", "Year"))
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "milk.whole_kcal", "milk.nonFat_kcal", "milk.reducedFat_kcal", "milk.lowFat_kcal", 
            "milk.substitutes_kcal")
    if (grams) 
        var2 <- c(var2, "milk.whole_grams", "milk.nonFat_grams", "milk.reducedFat_grams", "milk.lowFat_grams", 
            "milk.substitutes_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.nuts` [exported]

```r
function (data, years, day = 1, kcal = FALSE, grams = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    code <- c(42100050, 42100100, 42101000, 42101110, 42101120, 42101130, 42101300, 42101350, 42102000, 
        42104000, 42104050, 42104100, 42104105, 42104110, 42104500, 42105000, 42106000, 42106020, 42107000, 
        42109100, 42110000, 42110050, 42110100, 42110110, 42110120, 42110150, 42110160, 42110300, 42111000, 
        42111030, 42111040, 42111100, 42111110, 42111200, 42111205, 42111210, 42111500, 42112000, 42112100, 
        42112200, 42112210, 42112300, 42113000, 42114130, 42114140, 42114142, 42114145, 42116000, 42116050, 
        42116100, 42200500, 42200510, 42200600, 42201000, 42202000, 42202010, 42202100, 42202130, 42202150, 
        42202200, 42203000, 42203100, 42500000, 42500100, 42501000, 42501500, 42502100, 43101050, 43101100, 
        43101150, 43102000, 43102100, 43102300, 43102400, 43103000, 43103300, 43104000, 43107000, 43108010)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% code] <- 0
    d$grams[!d$food.code %in% code] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::nuts_kcal", "grams::nuts_grams")
    var2 <- c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "nuts_kcal")
    if (grams) 
        var2 <- c(var2, "nuts_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dr.ssb` [exported]

```r
function (data, years, day = 1, kcal = F, grams = F, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    ssb <- c(11551050, 11553100, 11553110, 11553120, 11553130, 42404010, 64134015, 64134020, 64134025, 
        64134030, 64134100, 64134200, 64200100, 64201010, 64201500, 64202010, 64203020, 64204010, 64205010, 
        64210010, 64213010, 64215010, 64221010, 78101100, 78101110, 78101115, 78101118, 78101120, 78101125, 
        78101130, 92101820, 92102450, 92121000, 92121001, 92121010, 92121020, 92121030, 92121040, 92121041, 
        92121050, 92130000, 92130001, 92130005, 92130006, 92130020, 92130021, 92130030, 92130031, 92305040, 
        92305050, 92305090, 92305110, 92305910, 92305920, 92306100, 92308000, 92308010, 92308030, 92308040, 
        92308500, 92308510, 92308530, 92308540, 92400000, 92400100, 92410110, 92410210, 92410250, 92410310, 
        92410315, 92410320, 92410340, 92410350, 92410360, 92410370, 92410390, 92410400, 92410410, 92410420, 
        92410510, 92410520, 92410550, 92410560, 92410610, 92410620, 92410710, 92410720, 92410810, 92410820, 
        92411510, 92411520, 92411610, 92411620, 92432000, 92433000, 92510610, 92510650, 92510720, 92510730, 
        92510955, 92510960, 92511000, 92511015, 92511250, 92512040, 92512050, 92512090, 92512110, 92513000, 
        92530410, 92530510, 92530610, 92530950, 92531030, 92541010, 92542000, 92550030, 92550035, 92550040, 
        92550110, 92550200, 92550350, 92550360, 92550370, 92550380, 92550405, 92552020, 92552030, 92582100, 
        92582110, 92610020, 92610030, 92611010, 92611100, 92612010, 92613010, 92613510, 92801000, 92802000, 
        92803000, 92804000, 94100100, 94100200, 94100300, 95101000, 95101010, 95102000, 95103000, 95103010, 
        95104000, 95105000, 95106000, 95106010, 95110000, 95110010, 95110020, 95120000, 95120010, 95120020, 
        95120050, 95310200, 95310400, 95310500, 95310550, 95310555, 95310560, 95310600, 95310700, 95310750, 
        95310800, 95311000, 95312400, 95312410, 95312500, 95312550, 95312555, 95312560, 95312600, 95312700, 
        95312800, 95312900, 95312905, 95313200, 95320200, 95320500, 95321000, 95322200, 95322500, 95323000, 
        95330100, 95330500, 95342000)
    d <- db_driff(years = years, Year = T, day = day, both2days = F, fun = "mean", energy_kcal = T, grams = T)
    d$energy_kcal[!d$food.code %in% ssb] <- 0
    d$grams[!d$food.code %in% ssb] <- 0
    d$grams[d$energy_kcal %in% 0] <- 0
    d <- aggregate_sum(data = d, x = c("energy_kcal", "grams"), by = c("seqn", "Year"))
    col_rename(d) <- c("energy_kcal::ssb_kcal", "grams::ssb_grams")
    var2 = c("seqn", "Year")
    if (kcal) 
        var2 <- c(var2, "ssb_kcal")
    if (grams) 
        var2 <- c(var2, "ssb_grams")
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_driff` [exported]

```r
function (data, years, day = 1, both2days = FALSE, fun = "mean", NA20 = F, wtdrd1 = FALSE, wtdr2d = FALSE, 
    wtdr4yr = FALSE, rstz = FALSE, breast_fed_infant = FALSE, day_of_week = FALSE, combination_food_number = FALSE, 
    combination_food_type = FALSE, time_of_eating_occasion_hh.mm = FALSE, meal_name = FALSE, source_of_food = FALSE, 
    eaten_at_home = FALSE, grams = FALSE, energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, 
    total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_sfat_g = FALSE, total_mfat_g = FALSE, 
    total_pfat_g = FALSE, cholesterol_mg = FALSE, vitamin_E_as_alpha_tocopherol_mg = FALSE, added_alpha_tocopherol_vitamin_E_mg = FALSE, 
    retinol_mcg = FALSE, vitamin_A_rae_mcg = FALSE, alpha_carotene_mcg = FALSE, beta_carotene_mcg = FALSE, 
    beta_cryptoxanthin_mcg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_B1_mg = FALSE, 
    riboflavin_vitamin_B2_mg = FALSE, niacin_mg = FALSE, vitamin_B6_mg = FALSE, total_folate_mcg = FALSE, 
    folic_acid_mcg = FALSE, food_folate_mcg = FALSE, folate_dfe_mcg = FALSE, vitamin_B12_mcg = FALSE, 
    added_vitamin_B12_mcg = FALSE, vitamin_C_mg = FALSE, vitamin_K_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, 
    magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, 
    selenium_mcg = FALSE, caffeine_mg = FALSE, theobromine_mg = FALSE, alcohol_g = FALSE, moisture_g = FALSE, 
    sfa_4.0_butanoic_g = FALSE, sfa_6.0_hexanoic_g = FALSE, sfa_8.0_octanoic_g = FALSE, sfa_10.0_decanoic_g = FALSE, 
    sfa_12.0_dodecanoic_g = FALSE, sfa_14.0_tetradecanoic_g = FALSE, sfa_16.0_hexadecanoic_g = FALSE, 
    sfa_18.0_octadecanoic_g = FALSE, mfa_16.1_hexadecenoic_g = FALSE, mfa_18.1_octadecenoic_g = FALSE, 
    mfa_20.1_eicosenoic_g = FALSE, mfa_22.1_docosenoic_g = FALSE, pfa_18.2_octadecadienoic_g = FALSE, 
    pfa_18.3_octadecatrienoic_g = FALSE, pfa_18.4_octadecatetraenoic_g = FALSE, pfa_20.4_eicosatetraenoic_g = FALSE, 
    pfa_20.5_eicosapentaenoic_g = FALSE, pfa_22.5_docosapentaenoic_g = FALSE, pfa_22.6_docosahexaenoic_g = FALSE, 
    total_choline_mg = FALSE, number_of_days = FALSE, vitamin_D_d2_d3_mcg = FALSE, Year = FALSE, join = "left", 
    group_sum = FALSE) 
{
    years <- data_years(data, years)
    if (isTRUE(time_of_eating_occasion_hh.mm)) 
        time_of_eating_occasion_hh.mm <- "time_of_eating_occasion_hh.mm"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        wtdrd1, "wtdrd1,wtdrd1pp"), wtdr4yr, "wtdr4yr"), wtdr2d, "wtdr2d,wtdr2dpp"), rstz, "drddrsts,drddrstz,dr1drstz,dr2drstz"), 
        breast_fed_infant, "drabf,drabf"), day_of_week, "drdday,dr1day,dr2day"), combination_food_number, 
        "drxccmnm,dr1ccmnm,dr2ccmnm"), combination_food_type, "drdccmty,drdccmtz,dr1ccmtx,dr2ccmtx"), 
        time_of_eating_occasion_hh.mm, "drd020,dr1_020,dr2_020"), meal_name, "drd030,drd030z,dr1_030z,dr2_030z"), 
        source_of_food, "dr1fs,dr2fs"), eaten_at_home, "drd040,drd040z,dr1_040z,dr2_040z"), grams, "drxigrms,dr1igrms,dr2igrms"), 
        energy_kcal, "drxikcal,dr1ikcal,dr2ikcal"), protein_g, "drxiprot,dr1iprot,dr2iprot"), carbohydrate_g, 
        "drxicarb,dr1icarb,dr2icarb"), total_sugars_g, "drxisugr,dr1isugr,dr2isugr"), dietary_fiber_g, 
        "drxifibe,dr1ifibe,dr2ifibe"), total_fat_g, "drxitfat,dr1itfat,dr2itfat"), total_sfat_g, "drxisfat,dr1isfat,dr2isfat"), 
        total_mfat_g, "drximfat,dr1imfat,dr2imfat"), total_pfat_g, "drxipfat,dr1ipfat,dr2ipfat"), cholesterol_mg, 
        "drxichol,dr1ichol,dr2ichol"), vitamin_E_as_alpha_tocopherol_mg, "drxiff,drxiatoc,dr1iatoc,dr2iatoc"), 
        added_alpha_tocopherol_vitamin_E_mg, "dr1iatoa,dr2iatoa"), retinol_mcg, "drxiret,dr1iret,dr2iret"), 
        vitamin_A_rae_mcg, "drxivare,drxivara,dr1ivara,dr2ivara"), alpha_carotene_mcg, "drxiacar,dr1iacar,dr2iacar"), 
        beta_carotene_mcg, "drxibcar,dr1ibcar,dr2ibcar"), beta_cryptoxanthin_mcg, "drxicryp,dr1icryp,dr2icryp"), 
        lycopene_mcg, "drxilyco,dr1ilyco,dr2ilyco"), lutein_zeaxanthin_mcg, "drxilz,dr1ilz,dr2ilz"), 
        thiamin_vitamin_B1_mg, "drxivb1,dr1ivb1,dr2ivb1"), riboflavin_vitamin_B2_mg, "drxivb2,dr1ivb2,dr2ivb2"), 
        niacin_mg, "drxiniac,dr1iniac,dr2iniac"), vitamin_B6_mg, "drxivb6,dr1ivb6,dr2ivb6"), total_folate_mcg, 
        "drxifola,dr1ifola,dr2ifola"), folic_acid_mcg, "drxifa,dr1ifa,dr2ifa"), food_folate_mcg, "drxiff,dr1iff,dr2iff"), 
        folate_dfe_mcg, "drxifdfe,dr1ifdfe,dr2ifdfe"), vitamin_B12_mcg, "drxivb12,dr1ivb12,dr2ivb12"), 
        added_vitamin_B12_mcg, "dr1ib12a,dr2ib12a"), vitamin_C_mg, "drxivc,dr1ivc,dr2ivc"), vitamin_K_mcg, 
        "drxivk,dr1ivk,dr2ivk"), calcium_mg, "drxicalc,dr1icalc,dr2icalc"), phosphorus_mg, "drxiphos,dr1iphos,dr2iphos"), 
        magnesium_mg, "drximagn,dr1imagn,dr2imagn"), iron_mg, "drxiiron,dr1iiron,dr2iiron"), zinc_mg, 
        "drxizinc,dr1izinc,dr2izinc"), copper_mg, "drxicopp,dr1icopp,dr2icopp"), sodium_mg, "drdisodi,dr1isodi,dr2isodi"), 
        potassium_mg, "drxipota,dr1ipota,dr2ipota"), selenium_mcg, "drxisele,dr1isele,dr2isele"), caffeine_mg, 
        "drxicaff,dr1icaff,dr2icaff"), theobromine_mg, "drxitheo,dr1itheo,dr2itheo"), alcohol_g, "drxialco,dr1ialco,dr2ialco"), 
        moisture_g, "drxiwate,drximois,dr1imois,dr2imois"), sfa_4.0_butanoic_g, "drxis040,dr1is040,dr2is040"), 
        sfa_6.0_hexanoic_g, "drxis060,dr1is060,dr2is060"), sfa_8.0_octanoic_g, "drxis080,dr1is080,dr2is080"), 
        sfa_10.0_decanoic_g, "drxis100,dr1is100,dr2is100"), sfa_12.0_dodecanoic_g, "drxis120,dr1is120,dr2is120"), 
        sfa_14.0_tetradecanoic_g, "drxis140,dr1is140,dr2is140"), sfa_16.0_hexadecanoic_g, "drxis160,dr1is160,dr2is160"), 
        sfa_18.0_octadecanoic_g, "drxis180,dr1is180,dr2is180"), mfa_16.1_hexadecenoic_g, "drxim161,dr1im161,dr2im161"), 
        mfa_18.1_octadecenoic_g, "drxim181,dr1im181,dr2im181"), mfa_20.1_eicosenoic_g, "drxim201,dr1im201,dr2im201"), 
        mfa_22.1_docosenoic_g, "drxim221,dr1im221,dr2im221"), pfa_18.2_octadecadienoic_g, "drxip182,dr1ip182,dr2ip182"), 
        pfa_18.3_octadecatrienoic_g, "drxip183,dr1ip183,dr2ip183"), pfa_18.4_octadecatetraenoic_g, "drxip184,dr1ip184,dr2ip184"), 
        pfa_20.4_eicosatetraenoic_g, "drxip204,dr1ip204,dr2ip204"), pfa_20.5_eicosapentaenoic_g, "drxip205,dr1ip205,dr2ip205"), 
        pfa_22.5_docosapentaenoic_g, "drxip225,dr1ip225,dr2ip225"), pfa_22.6_docosahexaenoic_g, "drxip226,dr1ip226,dr2ip226"), 
        total_choline_mg, "dr1ichl,dr2ichl"), number_of_days, "dr1dbih,dr2dbih"), vitamin_D_d2_d3_mcg, 
        "dr1ivd,dr2ivd")
    if (is.null(var2)) 
        stop("no variable was specified")
    if (length(day) == 1) {
        (tsv <- nhs_tsv(sprintf("drxiff|dr%siff", day), years = years, cat = FALSE))
        d <- nhs_read(tsv, var2, cat = FALSE) %>% drop_col("line")
        if (is.character(d)) 
            return(d)
        col_rename(d) <- c("drddrsts,drddrstz,dr1drstz,dr2drstz:rstz")
        if (group_sum) {
            ct <- kit::countOccur(d[, c("seqn", "food.code")])
            ct <- ct[ct$Count > 1, ]
            ck <- d$seqn %in% ct$seqn & d$food.code %in% ct$food.code
            di <- d[ck, ]
            di <- group_sum(di, bys = c("seqn", "Year", "food.code"), vars = set::not(colnames(di), "seqn", 
                "food.code", "dr1mc", "dr2mc", "Year"))
            d <- rbind(d[!ck, colnames(di)], di)
        }
    }
    else {
        tsv <- nhs_tsv(sprintf("drxiff|dr%siff", 1), years = years, cat = FALSE)
        d1 <- nhs_read(tsv, var2, cat = FALSE) %>% drop_col("line")
        col_rename(d1) <- c("drddrsts,drddrstz,dr1drstz,dr2drstz:rstz")
        if (group_sum) {
            ct <- kit::countOccur(d1[, c("seqn", "food.code")])
            ct <- ct[ct$Count > 1, ]
            ck <- d1$seqn %in% ct$seqn & d1$food.code %in% ct$food.code
            di <- d1[ck, ]
            di <- group_sum(di, bys = c("seqn", "Year", "food.code"), vars = set::not(colnames(di), "seqn", 
                "food.code", "dr1mc", "dr2mc", "Year"))
            d1 <- rbind(d1[!ck, colnames(di)], di)
        }
        tsv <- nhs_tsv(sprintf("drxiff|dr%siff", 2), years = years, cat = FALSE)
        d2 <- nhs_read(tsv, var2, cat = FALSE) %>% drop_col("line")
        col_rename(d2) <- c("drddrsts,drddrstz,dr1drstz,dr2drstz:rstz")
        if (group_sum) {
            ct <- kit::countOccur(d2[, c("seqn", "food.code")])
            ct <- ct[ct$Count > 1, ]
            ck <- d2$seqn %in% ct$seqn & d2$food.code %in% ct$food.code
            di <- d2[ck, ]
            di <- group_sum(di, bys = c("seqn", "food.code", "Year"), vars = set::not(colnames(di), "seqn", 
                "food.code", "dr1mc", "dr2mc", "Year"))
            d2 <- rbind(d2[!ck, colnames(di)], di)
        }
        commen <- set::not(set::and(do::numeric.nms(d1), do::numeric.nms(d2)), "seqn", "food.code", "dr1mc", 
            "dr2mc")
        d <- dplyr::full_join(d1, d2, c("seqn", "food.code"), suffix = c(".d1", ".d2"))
        d$Year <- ifelse(is.na(d$Year.d1), d$Year.d2, d$Year.d1)
        d$Year.d1 <- NULL
        d$Year.d2 <- NULL
        if (length(commen) > 0) {
            if (fun %in% c("sum", "mean")) {
                for (i in commen) {
                  (c12 <- paste0(i, c(".d1", ".d2")))
                  if (NA20) {
                    dna20 <- d[, c12]
                    dna20[is.na(dna20)] <- 0
                    d[, c12] <- dna20
                  }
                  cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                  d$xx <- cal
                  ck <- d$Year %in% c("1999-2000", "2001-2002")
                  d$xx[ck] <- row.means(d[ck, c12])
                  colnames(d)[ncol(d)] <- i
                  d <- drop_col(d, c12)
                }
                d <- d[do::NA.row.sums(d[, commen, drop = F]) < length(commen), ]
            }
        }
    }
    if (!isFALSE(vitamin_A_rae_mcg) & "1999-2000" %in% d$Year) {
        (ck <- d$Year %in% "1999-2000")
        if (isTRUE(vitamin_A_rae_mcg)) 
            vitamin_A_rae_mcg <- "vitamin_A_rae_mcg"
        d[ck, c("seqn", "food.code", vitamin_A_rae_mcg)] <- vitaminAE19999(d[ck, c("seqn", "line")], 
            VitA = TRUE)
    }
    if (!isFALSE(vitamin_E_as_alpha_tocopherol_mg) & "1999-2000" %in% d$Year) {
        (ck <- d$Year %in% "1999-2000")
        if (isTRUE(vitamin_E_as_alpha_tocopherol_mg)) 
            vitamin_E_as_alpha_tocopherol_mg <- "vitamin_E_as_alpha_tocopherol_mg"
        d[ck, c("seqn", "food.code", vitamin_E_as_alpha_tocopherol_mg)] <- vitaminAE19999(d[ck, c("seqn", 
            "line")], VitE = TRUE)
    }
    if (!isFALSE(time_of_eating_occasion_hh.mm)) {
        if (isTRUE(time_of_eating_occasion_hh.mm)) 
            time_of_eating_occasion_hh.mm <- "time_of_eating_occasion_hh.mm"
        if (time_of_eating_occasion_hh.mm %in% colnames(d)) {
            d[, time_of_eating_occasion_hh.mm] <- hms::as_hms(d[, time_of_eating_occasion_hh.mm])
        }
        if (paste0(time_of_eating_occasion_hh.mm, ".d1") %in% colnames(d)) {
            d[, paste0(time_of_eating_occasion_hh.mm, ".d1")] <- hms::as_hms(d[, paste0(time_of_eating_occasion_hh.mm, 
                ".d1")])
        }
        if (paste0(time_of_eating_occasion_hh.mm, ".d2") %in% colnames(d)) {
            d[, paste0(time_of_eating_occasion_hh.mm, ".d2")] <- hms::as_hms(d[, paste0(time_of_eating_occasion_hh.mm, 
                ".d2")])
        }
    }
    d <- kit::funique(d)
    key <- "seqn"
    if (!missing(data)) {
        if ("food.code" %in% colnames(data)) 
            key <- c("seqn", "food.code")
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_drtot` [exported]

```r
function (data, years, day = 1, fun = c("mean", "sum", "alone"), wtdrd1 = FALSE, wtdr4yr = FALSE, wtdr2d = FALSE, 
    rstz = FALSE, breast_fed_infant = FALSE, day_of_week = FALSE, foods_number = FALSE, diet_on_special = FALSE, 
    diet_wllh = FALSE, diet_lowfat = FALSE, diet_lowsalt = FALSE, diet_lowsugar = FALSE, diet_lowfiber = FALSE, 
    diet_highfiber = FALSE, diet_diabetic = FALSE, diet_weightgain = FALSE, diet_lowcarbohydrate = FALSE, 
    diet_highprotein = FALSE, diet_glutenfree = FALSE, diet_kidney = FALSE, diet_otherspecial = FALSE, 
    energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, 
    total_fat_g = FALSE, total_sfat_g = FALSE, total_mfat_g = FALSE, total_pfat_g = FALSE, cholesterol_mg = FALSE, 
    vitamin_A_rae_mcg = FALSE, retinol_mcg = FALSE, carotene_re.1999 = FALSE, alpha_carotene_mcg = FALSE, 
    beta_carotene_mcg = FALSE, beta_cryptoxanthin_mcg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, 
    thiamin_vitamin_B1_mg = FALSE, riboflavin_vitamin_B2_mg = FALSE, niacin_mg = FALSE, vitamin_B6_mg = FALSE, 
    total_folate_mcg = FALSE, folic_acid_mcg = FALSE, food_folate_mcg = FALSE, folate_dfe_mcg = FALSE, 
    total_choline_mg = FALSE, vitamin_B12_mcg = FALSE, added_vitamin_B12_mcg = FALSE, vitamin_C_mg = FALSE, 
    vitamin_D_d2_d3_mcg = FALSE, vitamin_E_as_alpha_tocopherol_mg = FALSE, added_alpha_tocopherol_vitamin_E_mg = FALSE, 
    vitamin_K_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, 
    zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, 
    caffeine_mg = FALSE, theobromine_mg = FALSE, alcohol_g = FALSE, moisture_g = FALSE, sfa_4.0_butanoic_g = FALSE, 
    sfa_6.0_hexanoic_g = FALSE, sfa_8.0_g = FALSE, sfa_10.0_g = FALSE, sfa_12.0_g = FALSE, sfa_14.0_g = FALSE, 
    sfa_16.0_g = FALSE, sfa_18.0_g = FALSE, mfa_16.1_g = FALSE, mfa_18.1_g = FALSE, mfa_20.1_g = FALSE, 
    mfa_22.1_g = FALSE, pfa_18.2_g = FALSE, pfa_18.3_g = FALSE, pfa_18.4_g = FALSE, pfa_20.4_g = FALSE, 
    pfa_20.5_g = FALSE, pfa_22.5_g = FALSE, pfa_22.6_g = FALSE, compare_to_usual = FALSE, water_total_plain_g = FALSE, 
    water_total_tap_g = FALSE, water_total_bottled_g = FALSE, water_plain_carbonated_g = FALSE, water_tap_source = FALSE, 
    salt_type = FALSE, salt_added_frequency = FALSE, salt_used_in_preparation = FALSE, salt_used_at_table_yesterday = FALSE, 
    shellfish = FALSE, clams = FALSE, clams_times = FALSE, crabs = FALSE, crabs_times = FALSE, crayfish = FALSE, 
    crayfish_times = FALSE, lobsters = FALSE, lobsters_times = FALSE, mussels = FALSE, mussels_times = FALSE, 
    oysters = FALSE, oysters_times = FALSE, scallops = FALSE, scallops_times = FALSE, shrimp = FALSE, 
    shrimp_times = FALSE, other_shellfish = FALSE, other_shellfish_times = FALSE, unknown_shellfish = FALSE, 
    unknown_shellfish_times = FALSE, refused_shellfish = FALSE, fish = FALSE, breaded_fish = FALSE, breaded_fish_times = FALSE, 
    tuna = FALSE, tuna_times = FALSE, bass = FALSE, bass_times = FALSE, catfish = FALSE, catfish_times = FALSE, 
    cod = FALSE, cod_times = FALSE, flatfish = FALSE, flatfish_times = FALSE, haddock = FALSE, haddock_times = FALSE, 
    mackerel = FALSE, mackerel_times = FALSE, perch = FALSE, perch_times = FALSE, pike = FALSE, pike_times = FALSE, 
    pollock = FALSE, pollock_times = FALSE, porgy = FALSE, porgy_times = FALSE, salmon = FALSE, salmon_times = FALSE, 
    sardines = FALSE, sardines_times = FALSE, sea_bass = FALSE, sea_bass_times = FALSE, shark = FALSE, 
    shark_times = FALSE, swordfish = FALSE, swordfish_times = FALSE, trout = FALSE, trout_times = FALSE, 
    walleye = FALSE, walleye_times = FALSE, other_fish = FALSE, other_fish_times = FALSE, unknown_fish = FALSE, 
    unknown_fish_times = FALSE, refused_fish = FALSE, Year = FALSE, both2days = TRUE, join = "left") 
{
    years <- data_years(data, years)
    day <- as.numeric(day)
    fun <- match.arg(fun)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        wtdrd1, "wtdrd1,wtdrd1pp"), wtdr4yr, "wtdr4yr"), wtdr2d, "wtdr2d,wtdr2dpp"), rstz, "drddrsts,drddrstz,dr1drstz,dr2drstz"), 
        day_of_week, "drdday,dr1day,dr2day"), foods_number, "drxtnumf,dr1tnumf,dr2tnumf"), breast_fed_infant, 
        "drabf"), diet_on_special, "drqsdiet"), diet_wllh, "drqsdt1"), diet_lowfat, "drqsdt2"), diet_lowsalt, 
        "drqsdt3"), diet_lowsugar, "drqsdt4"), diet_lowfiber, "drqsdt5"), diet_highfiber, "drqsdt6"), 
        diet_diabetic, "drqsdt7"), diet_weightgain, "drqsdt8"), diet_lowcarbohydrate, "drqsdt9"), diet_highprotein, 
        "drqsdt10"), diet_glutenfree, "drqsdt11"), diet_kidney, "drqsdt12"), diet_otherspecial, "drqsdt91"), 
        energy_kcal, "drxtkcal,dr1tkcal,dr2tkcal"), protein_g, "drxtprot,dr1tprot,dr2tprot"), carbohydrate_g, 
        "drxtcarb,dr1tcarb,dr2tcarb"), total_sugars_g, "drxtsugr,dr1tsugr,dr2tsugr"), dietary_fiber_g, 
        "drxtfibe,dr1tfibe,dr2tfibe"), total_fat_g, "drxttfat,dr1ttfat,dr2ttfat"), total_sfat_g, "drxtsfat,dr1tsfat,dr2tsfat"), 
        total_mfat_g, "drxtmfat,dr1tmfat,dr2tmfat"), total_pfat_g, "drxtpfat,dr1tpfat,dr2tpfat"), cholesterol_mg, 
        "drxtchol,dr1tchol,dr2tchol"), vitamin_A_rae_mcg, "drxtvare,drxtvara,dr1tvara,dr2tvara"), retinol_mcg, 
        "drxtret,dr1tret,dr2tret"), carotene_re.1999, "drxtcaro"), alpha_carotene_mcg, "drxtacar,dr1tacar,dr2tacar"), 
        beta_carotene_mcg, "drxtbcar,dr1tbcar,dr2tbcar"), beta_cryptoxanthin_mcg, "drxtcryp,dr1tcryp,dr2tcryp"), 
        lycopene_mcg, "drxtlyco,dr1tlyco,dr2tlyco"), lutein_zeaxanthin_mcg, "drxtlz,dr1tlz,dr2tlz"), 
        thiamin_vitamin_B1_mg, "drxtvb1,dr1tvb1,dr2tvb1"), riboflavin_vitamin_B2_mg, "drxtvb2,dr1tvb2,dr2tvb2"), 
        niacin_mg, "drxtniac,dr1tniac,dr2tniac"), vitamin_B6_mg, "drxtvb6,dr1tvb6,dr2tvb6"), total_folate_mcg, 
        "drxtfola,dr1tfola,dr2tfola"), folic_acid_mcg, "drxtfa,dr1tfa,dr2tfa"), food_folate_mcg, "drxtff,dr1tff,dr2tff"), 
        folate_dfe_mcg, "drxtfdfe,dr1tfdfe,dr2tfdfe"), total_choline_mg, "dr1tchl,dr2tchl"), vitamin_B12_mcg, 
        "drxtvb12,dr1tvb12,dr2tvb12"), added_vitamin_B12_mcg, "dr1tb12a,dr2tb12a"), vitamin_C_mg, "drxtvc,dr1tvc,dr2tvc"), 
        vitamin_D_d2_d3_mcg, "dr1tvd,dr2tvd"), vitamin_E_as_alpha_tocopherol_mg, "drxtve,drxtatoc,dr1tatoc,dr2tatoc"), 
        added_alpha_tocopherol_vitamin_E_mg, "dr1tatoa,dr2tatoa"), vitamin_K_mcg, "drxtvk,dr1tvk,dr2tvk"), 
        calcium_mg, "drxtcalc,dr1tcalc,dr2tcalc"), phosphorus_mg, "drxtphos,dr1tphos,dr2tphos"), magnesium_mg, 
        "drxtmagn,dr1tmagn,dr2tmagn"), iron_mg, "drxtiron,dr1tiron,dr2tiron"), zinc_mg, "drxtzinc,dr1tzinc,dr2tzinc"), 
        copper_mg, "drxtcopp,dr1tcopp,dr2tcopp"), sodium_mg, "drdtsodi,dr1tsodi,dr2tsodi"), potassium_mg, 
        "drxtpota,dr1tpota,dr2tpota"), selenium_mcg, "drxtsele,dr1tsele,dr2tsele"), caffeine_mg, "drxtcaff,dr1tcaff,dr2tcaff"), 
        theobromine_mg, "drxttheo,dr1ttheo,dr2ttheo"), alcohol_g, "dr1ialco,dr1talco,dr2ialco,dr2talco,drxialco,drxtalco"), 
        moisture_g, "drxtwate,drxtmois,dr1tmois,dr2tmois"), sfa_4.0_butanoic_g, "drxts040,dr1ts040,dr2ts040"), 
        sfa_6.0_hexanoic_g, "drxts060,dr1ts060,dr2ts060"), sfa_8.0_g, "drxts080,dr1ts080,dr2ts080"), 
        sfa_10.0_g, "drxts100,dr1ts100,dr2ts100"), sfa_12.0_g, "drxts120,dr1ts120,dr2ts120"), sfa_14.0_g, 
        "drxts140,dr1ts140,dr2ts140"), sfa_16.0_g, "drxts160,dr1ts160,dr2ts160"), sfa_18.0_g, "drxts180,dr1ts180,dr2ts180"), 
        mfa_16.1_g, "drxtm161,dr1tm161,dr2tm161"), mfa_18.1_g, "drxtm181,dr1tm181,dr2tm181"), mfa_20.1_g, 
        "drxtm201,dr1tm201,dr2tm201"), mfa_22.1_g, "drxtm221,dr1tm221,dr2tm221"), pfa_18.2_g, "drxtp182,dr1tp182,dr2tp182"), 
        pfa_18.3_g, "drxtp183,dr1tp183,dr2tp183"), pfa_18.4_g, "drxtp184,dr1tp184,dr2tp184"), pfa_20.4_g, 
        "drxtp204,dr1tp204,dr2tp204"), pfa_20.5_g, "drxtp205,dr1tp205,dr2tp205"), pfa_22.5_g, "drxtp225,dr1tp225,dr2tp225"), 
        pfa_22.6_g, "drxtp226,dr1tp226,dr2tp226"), compare_to_usual, "drq300,drd300,dr1_300,dr2_300"), 
        water_total_plain_g, "drd320gw,dr1_320,dr1_320z,dr2_320,dr2_320z"), water_total_tap_g, "drd330gw,dr1_330,dr1_330z,dr2_330,dr2_330z"), 
        water_total_bottled_g, "dr1bwatr,dr1bwatz,dr2bwatr,dr2bwatz"), water_plain_carbonated_g, "drdcwatr,dr1cwatr,dr2cwatr"), 
        water_tap_source, "dr1tws,dr1twsz,dr2tws,dr2twsz"), salt_type, "dbq095,dbq095z,dr2sky"), salt_added_frequency, 
        "dbd100"), salt_used_in_preparation, "drqsprep"), salt_used_at_table_yesterday, "dr1sty,dr2sty"), 
        shellfish, "drq340,drd340"), clams, "drd350a"), clams_times, "drq350aq,drd350aq"), crabs, "drd350b"), 
        crabs, "drq350bq,drd350bq"), crayfish, "drd350c"), crayfish_times, "drq350cq,drd350cq"), lobsters, 
        "drd350d"), lobsters_times, "drq350dq,drd350dq"), mussels, "drd350e"), mussels_times, "drd350eq,drq350eq"), 
        oysters, "drd350f"), oysters_times, "drq350fq,drd350fq"), scallops, "drd350g"), scallops_times, 
        "drq350gq,drd350gq"), shrimp, "drd350h"), shrimp_times, "drq350hq,drd350hq"), other_shellfish, 
        "drd350i"), other_shellfish_times, "drq350iq,drd350iq"), unknown_shellfish, "drd350j"), unknown_shellfish_times, 
        "drq350jq,drd350jq"), refused_shellfish, "drd350k"), fish, "drq360,drd360"), breaded_fish, "drd370a"), 
        breaded_fish_times, "drq370aq,drd370aq"), tuna, "drd370b"), tuna_times, "drq370bq,drd370bq"), 
        bass, "drd370c"), bass_times, "drq370cq,drd370cq"), catfish, "drd370d"), catfish_times, "drq370dq,drd370dq"), 
        cod, "drd370e"), cod_times, "drq370eq,drd370eq"), flatfish, "drd370f"), flatfish_times, "drq370fq,drd370fq"), 
        haddock, "drd370g"), haddock_times, "drq370gq,drd370gq"), mackerel, "drd370h"), mackerel_times, 
        "drq370hq,drd370hq"), perch, "drd370i"), perch_times, "drq370iq,drd370iq"), pike, "drd370j"), 
        pike_times, "drq370jq,drd370jq"), pollock, "drd370k"), pollock_times, "drq370kq,drd370kq"), porgy, 
        "drd370l"), porgy_times, "drq370lq,drd370lq"), salmon, "drd370m"), salmon_times, "drq370mq,drd370mq"), 
        sardines, "drd370n"), sardines_times, "drq370nq,drd370nq"), sea_bass, "drd370o"), sea_bass_times, 
        "drq370oq,drd370oq"), shark, "drd370p"), shark_times, "drq370pq,drd370pq"), swordfish, "drd370q"), 
        swordfish_times, "drq370qq,drd370qq"), trout, "drd370r"), trout_times, "drq370rq,drd370rq"), 
        walleye, "drd370s"), walleye_times, "drq370sq,drd370sq"), other_fish, "drd370t"), other_fish_times, 
        "drq370tq,drd370tq"), unknown_fish, "drd370u"), unknown_fish_times, "drq370uq,drd370uq"), refused_fish, 
        "drd370v")
    if (length(day) == 1) {
        tsv <- nhs_tsv(sprintf("dr%stot|drxtot", day), years = years, cat = FALSE)
        d <- nhs_read(tsv, var2, cat = FALSE)
    }
    else {
        (tsv1 <- nhs_tsv("dr1tot|drxtot", years = years, cat = FALSE))
        d1 <- nhs_read(tsv1, var2, cat = FALSE)
        head(d1)
        tsv0(d1)
        (tsv2 <- nhs_tsv("dr2tot|drxtot", years = years, cat = FALSE))
        d2 <- nhs_read(tsv2, set::grep_not_or(var2, c("drddrsts", "drddrstz", "dr1drstz", "dr2drstz")), 
            cat = FALSE, Year = FALSE)
        head(d2)
        d2 <- drop_col(d2, "wtdrd1", "wtdr2d", "wtdr4yr", "drddrsts", "drabf")
        commen <- set::not(set::and(do::numeric.nms(d1), do::numeric.nms(d2)), "seqn")
        d <- dplyr::full_join(d1, d2, "seqn", suffix = c(".d1", ".d2"))
        if (length(commen) > 0) {
            if (fun %in% c("sum", "mean")) {
                for (i in commen) {
                  c12 <- paste0(i, c(".d1", ".d2"))
                  cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                  d$xx <- cal
                  ck <- d$Year %in% c("1999-2000", "2001-2002")
                  d$xx[ck] <- row.means(d[ck, c12])
                  colnames(d)[ncol(d)] <- i
                  d <- drop_col(d, c12)
                }
            }
        }
    }
    if (!isFALSE(vitamin_A_rae_mcg) & "1999-2000" %in% d$Year) {
        (ck <- d$Year %in% "1999-2000")
        if (isTRUE(vitamin_A_rae_mcg)) 
            vitamin_A_rae_mcg <- "vitamin_A_rae_mcg"
        dv <- vitaminAE19999(d[ck, "seqn", drop = FALSE], VitA = TRUE, dietary = "tot")
        d[ck, c("seqn", vitamin_A_rae_mcg)] <- dplyr::left_join(d[ck, "seqn", drop = FALSE], dv, "seqn")
    }
    if (!isFALSE(vitamin_E_as_alpha_tocopherol_mg) & "1999-2000" %in% d$Year) {
        (ck <- d$Year %in% "1999-2000")
        if (isTRUE(vitamin_E_as_alpha_tocopherol_mg)) 
            vitamin_E_as_alpha_tocopherol_mg <- "vitamin_E_as_alpha_tocopherol_mg"
        dv <- vitaminAE19999(d[ck, "seqn", drop = FALSE], VitE = TRUE, dietary = "tot")
        d[ck, c("seqn", vitamin_E_as_alpha_tocopherol_mg)] <- dplyr::left_join(d[ck, "seqn", drop = FALSE], 
            dv, "seqn")
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_ds.manganese` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    dsd <- db_DSD("manganese", supplement_name = F, blend_component_category = F, blend_component_name = F, 
        blend_flag = F, supplement_type = F, ingredient_category = F)
    dsd <- drop_row(dsd, dsd$ingredient_unit %in% c("trace", "unknown"), cat = F)
    d1 <- db_dsids.30(years = years, dosage_form = "form", quantity_of_supplement_taken_daily = "daily", 
        Year = T)
    d <- dplyr::left_join(d1, dsd, "dsdsupid")
    d <- drop_row(d, is.na(d$daily), cat = F)
    ck <- d$form %in% "grams"
    d$manganese <- d$daily * d$ingredient_quantity
    d$manganese[ck] <- d$daily[ck]
    d$manganese[!is.na(d$daily) & is.na(d$manganese)] <- 0
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d <- aggregate2(d, "manganese", c("seqn", "Year"), ".sum.nona")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_ds.melatonin` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    years <- set::not(years, prepare_years(c(1999, 2017)))
    dsd <- db_DSD("melatonin", supplement_name = F, blend_component_category = F, blend_component_name = F, 
        blend_flag = F, supplement_type = F, ingredient_category = F)
    dsd <- select_row(dsd, dsd$ingredient_unit %in% c("gm", "mg"), cat = F)
    ck <- dsd$ingredient_unit %in% "gm"
    dsd$ingredient_quantity[ck] <- dsd$ingredient_quantity[ck] * 1000
    d1 <- db_dsids.30(years = years, quantity_of_supplement_taken_daily = "daily", Year = T)
    d1$dsdsupid <- do::Replace0(d1$dsdsupid, " ")
    d <- dplyr::left_join(d1, dsd, "dsdsupid")
    d$melatonin <- d$daily * d$ingredient_quantity
    d$melatonin[!is.na(d$daily) & is.na(d$melatonin)] <- 0
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d <- aggregate2(d, "melatonin", c("seqn", "Year"), ".sum.nona")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_ds.silicon` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    dsd <- db_DSD("silic", "!~trisilicate", supplement_name = F, blend_component_category = F, blend_component_name = F, 
        blend_flag = F, supplement_type = F, ingredient_category = F)
    dsd <- select_row(dsd, dsd$ingredient_unit %in% c("gm", "mg"), cat = F)
    ck <- dsd$ingredient_unit %in% "gm"
    dsd$ingredient_quantity[ck] <- dsd$ingredient_quantity[ck] * 1000
    d1 <- db_dsids.30(years = years, quantity_of_supplement_taken_daily = "daily", Year = T)
    d <- dplyr::left_join(d1, dsd, "dsdsupid")
    d$silicon <- d$daily * d$ingredient_quantity
    ck.silica <- lookl(d$ingredient_name, "silica", NA2false = T)
    d$silicon[ck.silica] <- d$silicon[ck.silica] * (28/60)
    head(d)
    d$silicon[!is.na(d$daily) & is.na(d$silicon)] <- 0
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d <- aggregate2(d, "silicon", c("seqn", "Year"), ".sum.nona")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_ds.zinc` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    dsd <- db_DSD("zinc", supplement_name = F, blend_component_category = F, blend_component_name = F, 
        blend_flag = F, supplement_type = F, ingredient_category = F)
    dsd <- select_row(dsd, dsd$ingredient_unit %in% "mg", cat = F)
    d1 <- db_dsids.30(years = years, quantity_of_supplement_taken_daily = "daily", Year = T)
    d <- dplyr::left_join(d1, dsd, "dsdsupid")
    d$zinc <- d$daily * d$ingredient_quantity
    head(d)
    d$zinc[!is.na(d$daily) & is.na(d$zinc)] <- 0
    d <- aggregate_sum(d, "zinc", c("seqn", "Year"))
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dsids` [exported]

```r
function (data, years, day = 1, fun = c("mean", "sum", "alone"), both2days = TRUE, supplement_name = FALSE, 
    wtdrd1 = FALSE, wtdr2d = FALSE, rstz = FALSE, day_of_week = FALSE, location_supplement_originally_recorded = FALSE, 
    language = FALSE, antacid_containing_calcium.magnesium = FALSE, matching_code = FALSE, reported_serving_size.label_serving_size = FALSE, 
    energy_kcal = FALSE, protein_g = FALSE, carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, 
    total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monounsaturated_fatty_acids_g = FALSE, 
    total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, 
    thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, 
    folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, vitamin_b12_mcg = FALSE, 
    vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, 
    magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, 
    selenium_mcg = FALSE, caffeine_mg = FALSE, iodine_mcg = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (is.character(wtdrd1)) 
        wtdrd1 = TRUE
    if (is.character(wtdr2d)) 
        wtdr2d = TRUE
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "dsdsupid", "dsdpid,dsdsupid"), supplement_name, "dsdsupp"), wtdrd1, "wtdrd1"), wtdr2d, "wtdr2d"), 
        rstz, "dr1drstz,dr2drstz"), day_of_week, "dr1day,dr2day"), location_supplement_originally_recorded, 
        "ds1loc,ds2loc"), language, "dr1lang,dr2lang"), antacid_containing_calcium.magnesium, "ds1anta,ds2anta"), 
        matching_code, "ds1mtch,ds2mtch"), reported_serving_size.label_serving_size, "ds1actss,ds2actss"), 
        energy_kcal, "ds1ikcal,ds2ikcal"), protein_g, "ds1iprot,ds2iprot"), carbohydrate_g, "ds1icarb,ds2icarb"), 
        total_sugars_g, "ds1isugr,ds2isugr"), dietary_fiber_g, "ds1ifibe,ds2ifibe"), total_fat_g, "ds1itfat,ds2itfat"), 
        total_saturated_fatty_acids_g, "ds1isfat,ds2isfat"), total_monounsaturated_fatty_acids_g, "ds1imfat,ds2imfat"), 
        total_polyunsaturated_fatty_acids_g, "ds1ipfat,ds2ipfat"), cholesterol_mg, "ds1ichol,ds2ichol"), 
        lycopene_mcg, "ds1ilyco,ds2ilyco"), lutein_zeaxanthin_mcg, "ds1ilz,ds2ilz"), thiamin_vitamin_b1_mg, 
        "ds1ivb1,ds2ivb1"), riboflavin_vitamin_b2_mg, "ds1ivb2,ds2ivb2"), niacin_mg, "ds1iniac,ds2iniac"), 
        vitamin_b6_mg, "ds1ivb6,ds2ivb6"), folic_acid_mcg, "ds1ifa,ds2ifa"), folate_dfe_mcg, "ds1ifdfe,ds2ifdfe"), 
        total_choline_mg, "ds1ichl,ds2ichl"), vitamin_b12_mcg, "ds1ivb12,ds2ivb12"), vitamin_c_mg, "ds1ivc,ds2ivc"), 
        vitamin_k_mcg, "ds1ivk,ds2ivk"), vitamin_d_d2_d3_mcg, "ds1ivd,ds2ivd"), calcium_mg, "ds1icalc,ds2icalc"), 
        phosphorus_mg, "ds1iphos,ds2iphos"), magnesium_mg, "ds1imagn,ds2imagn"), iron_mg, "ds1iiron,ds2iiron"), 
        zinc_mg, "ds1izinc,ds2izinc"), copper_mg, "ds1icopp,ds2icopp"), sodium_mg, "ds1isodi,ds2isodi"), 
        potassium_mg, "ds1ipota,ds2ipota"), selenium_mcg, "ds1isele,ds2isele"), caffeine_mg, "ds1icaff,ds2icaff"), 
        iodine_mcg, "ds1iiodi,ds2iiodi")
    if (length(day) == 1) {
        tsv <- nhs_tsv(sprintf("ds%sids", day), years = years, cat = F)
        d <- nhs_read(tsv, var2, cat = F, lower_cd = T)
    }
    else if (length(day) == 2) {
        tsv <- nhs_tsv("ds1ids", years = years, cat = F)
        d1 <- nhs_read(tsv, var2, cat = F, lower_cd = T)
        tsv <- nhs_tsv("ds2ids", years = years, cat = F)
        d2 <- nhs_read(tsv, var2, cat = F, lower_cd = T)
        if (wtdrd1) 
            d2 <- drop_col(d2, "wtdrd1")
        if (wtdr2d) 
            d2 <- drop_col(d2, "wtdr2d")
        d <- dplyr::full_join(d1, d2, c("Year", "seqn"), suffix = c(".d1", ".d2"))
        commen <- unique(do::knife_right(set::grep_and(set::not(do::numeric.nms(d), "seqn"), "\\.d1|\\.d2"), 
            3))
        if (length(common) > 0) {
            if (fun %in% c("sum", "mean")) {
                for (i in commen) {
                  c12 <- paste0(i, c(".d1", ".d2"))
                  cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                  d$xx <- cal
                  colnames(d)[ncol(d)] <- i
                  d <- drop_col(d, c12)
                }
            }
        }
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dsids.30` [exported]

```r
function (data, years, supplement_name = FALSE, was_container_seen = FALSE, matching_code = FALSE, antacid_calcium_supplement_or_both = FALSE, 
    how_long_supplement_taken_days = FALSE, days_supplement_taken_past_30_days = FALSE, quantity_of_supplement_taken_daily = FALSE, 
    dosage_form = FALSE, reported_serving_size.label_serving_size = FALSE, antacid_reported_as_a_dietary_supplement = FALSE, 
    energy_kcal = FALSE, carbohydrate_g = FALSE, protein_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, 
    total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, total_monounsaturated_fatty_acids_g = FALSE, 
    total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, lycopene_ug = FALSE, lutein_zeaxanthin_ug = FALSE, 
    thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, niacin_mg = FALSE, vitamin_b6_mg = FALSE, 
    folic_acid_ug = FALSE, folate_dfe_ug = FALSE, total_choline_mg = FALSE, vitamin_b12_ug = FALSE, vitamin_c_mg = FALSE, 
    vitamin_k_ug = FALSE, vitamin_d_d2_d3_ug = FALSE, calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, 
    iron_mg = FALSE, zinc_mg = FALSE, copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_ug = FALSE, 
    caffeine_mg = FALSE, iodine_ug = FALSE, reported_product_during_day_1 = FALSE, reported_product_during_day_2 = FALSE, 
    took_product_on_own_or_doctor_advised = FALSE, for_good_bowel.colon_health = FALSE, for_prostate_health = FALSE, 
    for_mental_health = FALSE, to_prevent_health_problems = FALSE, to_improve_my_overall_health = FALSE, 
    for_teeth_prevent_cavities = FALSE, to_supplement_my_diet_food_not_enough = FALSE, to_stay_healthy = FALSE, 
    to_prevent_colds_boost_immune_system = FALSE, for_heart_health_cholesterol = FALSE, for_eye_health = FALSE, 
    for_healthy_joints_arthritis = FALSE, for_skin_health_dry_skin = FALSE, for_weight_loss = FALSE, 
    for_bone_health = FALSE, to_get_more_energy = FALSE, for_pregnancy = FALSE, for_anemia_such_as_low_iron = FALSE, 
    other_specify = FALSE, to_maintain_blood_sugar_diabetes = FALSE, for_healthy_hair_and_nails = FALSE, 
    for_kidney_and_bladder_health = FALSE, for_respiratory_health_asthma = FALSE, for_allergies = FALSE, 
    currently_breastfeeding = FALSE, to_improve_digestion = FALSE, for_menopause_hot_flashes = FALSE, 
    for_muscle_related_issues = FALSE, to_improve_sleep = FALSE, for_nervous_system_health = FALSE, for_relaxation_decrease_stress = FALSE, 
    for_liver_health_detoxification = FALSE, for_antioxidants = FALSE, for_word_of_mouth_advertisement = FALSE, 
    for_thyroid_health_gout = FALSE, to_build_muscle.weight_gain = FALSE, for_low_levels_in_blood = FALSE, 
    for_support_after_surgery = FALSE, for_headaches_and_dizziness = FALSE, to_build_muscle = FALSE, 
    for_fluid.water_balance = FALSE, for_inflammation = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "dsdsupid", "dsdsupid"), supplement_name, "dsdsupp"), was_container_seen, "dsd070"), matching_code, 
        "dsdmtch"), antacid_calcium_supplement_or_both, "rxq215a"), how_long_supplement_taken_days, "dsd090"), 
        days_supplement_taken_past_30_days, "dsd103"), quantity_of_supplement_taken_daily, "dsd122q"), 
        dosage_form, "dsd122u"), reported_serving_size.label_serving_size, "dsdactss"), antacid_reported_as_a_dietary_supplement, 
        "dsdanta"), energy_kcal, "dsqikcal"), carbohydrate_g, "dsqicarb"), protein_g, "dsqiprot"), total_sugars_g, 
        "dsqisugr"), dietary_fiber_g, "dsqifibe"), total_fat_g, "dsqitfat"), total_saturated_fatty_acids_g, 
        "dsqisfat"), total_monounsaturated_fatty_acids_g, "dsqimfat"), total_polyunsaturated_fatty_acids_g, 
        "dsqipfat"), cholesterol_mg, "dsqichol"), lycopene_ug, "dsqilyco"), lutein_zeaxanthin_ug, "dsqilz"), 
        thiamin_vitamin_b1_mg, "dsqivb1"), riboflavin_vitamin_b2_mg, "dsqivb2"), niacin_mg, "dsqiniac"), 
        vitamin_b6_mg, "dsqivb6"), folic_acid_ug, "dsqifa"), folate_dfe_ug, "dsqifdfe"), total_choline_mg, 
        "dsqichl"), vitamin_b12_ug, "dsqivb12"), vitamin_c_mg, "dsqivc"), vitamin_k_ug, "dsqivk"), vitamin_d_d2_d3_ug, 
        "dsqivd"), calcium_mg, "dsqicalc"), phosphorus_mg, "dsqiphos"), magnesium_mg, "dsqimagn"), iron_mg, 
        "dsqiiron"), zinc_mg, "dsqizinc"), copper_mg, "dsqicopp"), sodium_mg, "dsqisodi"), potassium_mg, 
        "dsqipota"), selenium_ug, "dsqisele"), caffeine_mg, "dsqicaff"), iodine_ug, "dsqiiodi"), reported_product_during_day_1, 
        "dsdday1"), reported_product_during_day_2, "dsdday2"), took_product_on_own_or_doctor_advised, 
        "dsq124"), for_good_bowel.colon_health, "dsq128a"), for_prostate_health, "dsq128b"), for_mental_health, 
        "dsq128c"), to_prevent_health_problems, "dsq128d"), to_improve_my_overall_health, "dsq128e"), 
        for_teeth_prevent_cavities, "dsq128f"), to_supplement_my_diet_food_not_enough, "dsq128g"), to_stay_healthy, 
        "dsq128h"), to_prevent_colds_boost_immune_system, "dsq128i"), for_heart_health_cholesterol, "dsq128j"), 
        for_eye_health, "dsq128k"), for_healthy_joints_arthritis, "dsq128l"), for_skin_health_dry_skin, 
        "dsq128m"), for_weight_loss, "dsq128n"), for_bone_health, "dsq128o"), to_get_more_energy, "dsq128p"), 
        for_pregnancy, "dsq128q"), for_anemia_such_as_low_iron, "dsq128r"), other_specify, "dsq128s"), 
        to_maintain_blood_sugar_diabetes, "dsd128t"), for_healthy_hair_and_nails, "dsd128u"), for_kidney_and_bladder_health, 
        "dsd128v"), for_respiratory_health_asthma, "dsd128w"), for_allergies, "dsd128x"), currently_breastfeeding, 
        "dsd128y"), to_improve_digestion, "dsd128z"), for_menopause_hot_flashes, "dsd128aa"), for_muscle_related_issues, 
        "dsd128bb"), to_improve_sleep, "dsd128cc"), for_nervous_system_health, "dsd128ee"), for_relaxation_decrease_stress, 
        "dsd128dd"), for_liver_health_detoxification, "dsd128ff"), for_antioxidants, "dsd128gg"), for_word_of_mouth_advertisement, 
        "dsd128hh"), for_thyroid_health_gout, "dsd128ii"), to_build_muscle.weight_gain, "dsd128jj"), 
        for_low_levels_in_blood, "dsd128kk"), for_support_after_surgery, "dsd128ll"), for_headaches_and_dizziness, 
        "dsd128mm"), to_build_muscle, "dsq128nn"), for_inflammation, "dsd128oo"), for_fluid.water_balance, 
        "dsd128pp")
    (tsv <- nhs_tsv("dsqfile2|dsq2|dsqids", years = years, cat = F))
    d <- nhs_read(tsv, var2, lower_cd = T, cat = F)
    col_rename(d) <- "dsdsupid:dsdsupid"
    d$dsdsupid <- format(d$dsdsupid, width = 10)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dstot` [exported]

```r
function (data, years, day = 1, fun = c("mean", "sum", "alone"), both2days = TRUE, wtdrd1 = FALSE, wtdr2d = FALSE, 
    rstz = FALSE, number_of_days_of_intake = FALSE, day_of_week = FALSE, language = FALSE, main_respondent_for_this_interview = FALSE, 
    helped_in_responding_for_this_interview = FALSE, any_dietary_supplements_taken = FALSE, number_of_dietary_supplements_reported = FALSE, 
    any_antacids_taken = FALSE, number_of_antacids_reported = FALSE, energy_kcal = FALSE, protein_g = FALSE, 
    carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, 
    total_monounsaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, 
    lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, thiamin_vitamin_b1_mg = FALSE, riboflavin_vitamin_b2_mg = FALSE, 
    niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, 
    vitamin_b12_mcg = FALSE, vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, 
    calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, 
    copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, 
    number_of_days_bw_intake_and_hh_interview = FALSE, iodine_mcg = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    if (is.character(wtdrd1)) 
        wtdrd1 = TRUE
    if (is.character(wtdr2d)) 
        wtdr2d = TRUE
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        wtdrd1, "wtdrd1"), wtdr2d, "wtdr2d"), rstz, "dr1drstz,dr2drstz"), day_of_week, "dr1day,dr2day"), 
        language, "dr1lang,dr2lang"), main_respondent_for_this_interview, "dr1mnrsp,dr1mresp,dr2mnrsp,"), 
        helped_in_responding_for_this_interview, "dr1helpd,dr1help,dr2helpd,dr2help"), any_dietary_supplements_taken, 
        "ds1ds,ds2ds"), number_of_dietary_supplements_reported, "ds1dscnt,ds2dscnt"), any_antacids_taken, 
        "ds1an,ds2an"), number_of_antacids_reported, "ds1ancnt,ds2ancnt"), energy_kcal, "ds1tkcal,ds2tkcal"), 
        protein_g, "ds1tprot,ds2tprot"), carbohydrate_g, "ds1tcarb,ds2tcarb"), total_sugars_g, "ds1tsugr,ds2tsugr"), 
        dietary_fiber_g, "ds1tfibe,ds2tfibe"), total_fat_g, "ds1ttfat,ds2ttfat"), total_saturated_fatty_acids_g, 
        "ds1tsfat,ds2tsfat"), total_monounsaturated_fatty_acids_g, "ds1tmfat,ds2tmfat"), total_polyunsaturated_fatty_acids_g, 
        "ds1tpfat,ds2tpfat"), cholesterol_mg, "ds1tchol,ds2tchol"), lycopene_mcg, "ds1tlyco,ds2tlyco"), 
        lutein_zeaxanthin_mcg, "ds1tlz,ds2tlz"), thiamin_vitamin_b1_mg, "ds1tvb1,ds2tvb1"), riboflavin_vitamin_b2_mg, 
        "ds1tvb2,ds2tvb2"), niacin_mg, "ds1tniac,ds2tniac"), vitamin_b6_mg, "ds1tvb6,ds2tvb6"), folic_acid_mcg, 
        "ds1tfa,ds2tfa"), folate_dfe_mcg, "ds1tfdfe,ds2tfdfe"), total_choline_mg, "ds1tchl,ds2tchl"), 
        vitamin_b12_mcg, "ds1tvb12,ds2tvb12"), vitamin_c_mg, "ds1tvc,ds2tvc"), vitamin_k_mcg, "ds1tvk,ds2tvk"), 
        vitamin_d_d2_d3_mcg, "ds1tvd,ds2tvd"), calcium_mg, "ds1tcalc,ds2tcalc"), phosphorus_mg, "ds1tphos,ds2tphos"), 
        magnesium_mg, "ds1tmagn,ds2tmagn"), iron_mg, "ds1tiron,ds2tiron"), zinc_mg, "ds1tzinc,ds2tzinc"), 
        copper_mg, "ds1tcopp,ds2tcopp"), sodium_mg, "ds1tsodi,ds2tsodi"), potassium_mg, "ds1tpota,ds2tpota"), 
        selenium_mcg, "ds1tsele,ds2tsele"), caffeine_mg, "ds1tcaff,ds2tcaff"), number_of_days_bw_intake_and_hh_interview, 
        "dr1dbih,dr2dbih"), iodine_mcg, "ds1tiodi,ds2tiodi")
    if (length(day) == 1) {
        tsv <- nhs_tsv(sprintf("ds%stot", day), years = years, cat = F)
        d <- nhs_read(tsv, var2, cat = F)
    }
    else if (length(day) == 2) {
        tsv <- nhs_tsv("ds1tot", years = years, cat = F)
        d1 <- nhs_read(tsv, var2, cat = F)
        tsv <- nhs_tsv("ds2tot", years = years, cat = F)
        d2 <- nhs_read(tsv, var2, cat = F)
        if (wtdrd1) 
            d2 <- drop_col(d2, "wtdrd1")
        if (wtdr2d) 
            d2 <- drop_col(d2, "wtdr2d")
        d <- dplyr::full_join(d1, d2, c("Year", "seqn"), suffix = c(".d1", ".d2"))
        commen <- unique(do::knife_right(set::grep_and(set::not(do::numeric.nms(d), "seqn"), "\\.d1|\\.d2"), 
            3))
        if (length(commen) > 0) {
            if (fun %in% c("sum", "mean")) {
                for (i in commen) {
                  c12 <- paste0(i, c(".d1", ".d2"))
                  cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                  d$xx <- cal
                  colnames(d)[ncol(d)] <- i
                  d <- drop_col(d, c12)
                }
            }
        }
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dstot.30` [exported]

```r
function (data, years, any_dietary_supplements_taken = FALSE, total_number_of_dietary_supplements_taken = FALSE, 
    any_antacids_taken = FALSE, total_number_of_antacids_taken = FALSE, energy_kcal = FALSE, protein_g = FALSE, 
    carbohydrate_g = FALSE, total_sugars_g = FALSE, dietary_fiber_g = FALSE, total_fat_g = FALSE, total_saturated_fatty_acids_g = FALSE, 
    total_monosaturated_fatty_acids_g = FALSE, total_polyunsaturated_fatty_acids_g = FALSE, cholesterol_mg = FALSE, 
    lycopene_mcg = FALSE, lutein_zeaxanthin_mcg = FALSE, vitamin_b1_thiamin_mg = FALSE, vitamin_b2_riboflavin_mg = FALSE, 
    niacin_mg = FALSE, vitamin_b6_mg = FALSE, folic_acid_mcg = FALSE, folate_dfe_mcg = FALSE, total_choline_mg = FALSE, 
    vitamin_b12_mcg = FALSE, vitamin_c_mg = FALSE, vitamin_k_mcg = FALSE, vitamin_d_d2_d3_mcg = FALSE, 
    calcium_mg = FALSE, phosphorus_mg = FALSE, magnesium_mg = FALSE, iron_mg = FALSE, zinc_mg = FALSE, 
    copper_mg = FALSE, sodium_mg = FALSE, potassium_mg = FALSE, selenium_mcg = FALSE, caffeine_mg = FALSE, 
    iodine_mcg = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        any_dietary_supplements_taken, "dsd010"), total_number_of_dietary_supplements_taken, "dsdcount"), 
        any_antacids_taken, "dsd010an"), total_number_of_antacids_taken, "dsdancnt"), energy_kcal, "dsqtkcal"), 
        protein_g, "dsqtprot"), carbohydrate_g, "dsqtcarb"), total_sugars_g, "dsqtsugr"), dietary_fiber_g, 
        "dsqtfibe"), total_fat_g, "dsqttfat"), total_saturated_fatty_acids_g, "dsqtsfat"), total_monosaturated_fatty_acids_g, 
        "dsqtmfat"), total_polyunsaturated_fatty_acids_g, "dsqtpfat"), cholesterol_mg, "dsqtchol"), lycopene_mcg, 
        "dsqtlyco"), lutein_zeaxanthin_mcg, "dsqtlz"), vitamin_b1_thiamin_mg, "dsqtvb1"), vitamin_b2_riboflavin_mg, 
        "dsqtvb2"), niacin_mg, "dsqtniac"), vitamin_b6_mg, "dsqtvb6"), folic_acid_mcg, "dsqtfa"), folate_dfe_mcg, 
        "dsqtfdfe"), total_choline_mg, "dsqtchl"), vitamin_b12_mcg, "dsqtvb12"), vitamin_c_mg, "dsqtvc"), 
        vitamin_k_mcg, "dsqtvk"), vitamin_d_d2_d3_mcg, "dsqtvd"), calcium_mg, "dsqtcalc"), phosphorus_mg, 
        "dsqtphos"), magnesium_mg, "dsqtmagn"), iron_mg, "dsqtiron"), zinc_mg, "dsqtzinc"), copper_mg, 
        "dsqtcopp"), sodium_mg, "dsqtsodi"), potassium_mg, "dsqtpota"), selenium_mcg, "dsqtsele"), caffeine_mg, 
        "dsqtcaff"), iodine_mcg, "dsqtiodi")
    tsv <- nhs_tsv("dsqtot", cat = F, years = years)
    d <- nhs_read(tsv, var2, cat = F, Year = TRUE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dxx` [exported]

```r
function (data, years, head_area_cm2 = FALSE, head_bmc_g = FALSE, head_bmd_g.cm2 = FALSE, head_fat_g = FALSE, 
    head_lean_excl_bmc_g = FALSE, head_lean_incl_bmc_g = FALSE, head_total_g = FALSE, head_percent_fat = FALSE, 
    left_arm_area_cm2 = FALSE, left_arm_bmc_g = FALSE, left_arm_bmd_g.cm2 = FALSE, left_arm_fat_g = FALSE, 
    left_arm_lean_excl_bmc_g = FALSE, left_arm_lean_incl_bmc_g = FALSE, left_arm_total_g = FALSE, left_arm_percent_fat = FALSE, 
    left_leg_area_cm2 = FALSE, left_leg_bmc_g = FALSE, left_leg_bmd_g.cm2 = FALSE, left_leg_fat_g = FALSE, 
    left_leg_lean_excl_bmc_g = FALSE, left_leg_lean_incl_bmc_g = FALSE, left_leg_total_g = FALSE, left_leg_percent_fat = FALSE, 
    right_arm_area_cm2 = FALSE, right_arm_bmc_g = FALSE, right_arm_bmd_g.cm2 = FALSE, right_arm_fat_g = FALSE, 
    right_arm_lean_excl_bmc_g = FALSE, right_arm_lean_incl_bmc_g = FALSE, right_arm_total_g = FALSE, 
    right_arm_percent_fat = FALSE, right_leg_area_cm2 = FALSE, right_leg_bmc_g = FALSE, right_leg_bmd_g.cm2 = FALSE, 
    right_leg_fat_g = FALSE, right_leg_lean_excl_bmc_g = FALSE, right_leg_lean_incl_bmc_g = FALSE, right_leg_total_g = FALSE, 
    right_leg_percent_fat = FALSE, left_ribs_area_cm2 = FALSE, left_ribs_bmc_g = FALSE, left_ribs_bmd_g.cm2 = FALSE, 
    right_ribs_area_cm2 = FALSE, right_ribs_bmc_g = FALSE, right_ribs_bmd_g.cm2 = FALSE, thoracic_spine_area_cm2 = FALSE, 
    thoracic_spine_bmc_g = FALSE, thoracic_spine_bmd_g.cm2 = FALSE, lumbar_spine_area_cm2 = FALSE, lumbar_spine_bmc_g = FALSE, 
    lumbar_spine_bmd_g.cm2 = FALSE, pelvis_area_cm2 = FALSE, pelvis_bmc_g = FALSE, pelvis_bmd_g.cm2 = FALSE, 
    trunk_bone_area_cm2 = FALSE, trunk_bmc_g = FALSE, trunk_bone_bmd_g.cm2 = FALSE, trunk_fat_g = FALSE, 
    trunk_lean_excl_bmc_g = FALSE, trunk_lean_incl_bmc_g = FALSE, trunk_totalg = FALSE, trunk_percent_fat = FALSE, 
    subtotal_area_cm2 = FALSE, subtotal_bmc_g = FALSE, subtotal_bmd_g.cm2 = FALSE, subtotal_fat_g = FALSE, 
    subtotal_lean_excl_bmc_g = FALSE, subtotal_lean_incl_bmc_g = FALSE, subtotal_total_excl_head_g = FALSE, 
    subtotal_percent_fat = FALSE, total_area_cm2 = FALSE, total_bmc_g = FALSE, total_bmd_g.cm2 = FALSE, 
    total_fat_g = FALSE, total_lean_excl_bmc_g = FALSE, total_lean_incl_bmc_g = FALSE, total_lean_plus_fat_g = FALSE, 
    total_percent_fat = FALSE, mult.fun = c("mean", "median", "unique"), Year = FALSE, join = "left") 
{
    mult.fun <- match.arg(mult.fun)
    years <- data_years(data, years)
    tsv <- nhs_tsv("dxx\\.|dxx_", "!~dxx_2", years = years, cat = FALSE)
    tsv0(tsv)
    head_imputation_indicator = FALSE
    head_bone_invalidity_code = FALSE
    head_tissue_invalidity_code = FALSE
    left_arm_imputation_indicator = FALSE
    left_arm_bone_invalidity_code = FALSE
    left_arm_tissue_invalidity_code = FALSE
    left_leg_imputation_indicator = FALSE
    left_leg_bone_invalidity_code = FALSE
    left_leg_tissue_invalidity_code = FALSE
    right_arm_imputation_indicator = FALSE
    right_arm_bone_invalidity_code = FALSE
    right_arm_tissue_invalidity_code = FALSE
    right_leg_imputation_indicator = FALSE
    right_leg_bone_invalidity_code = FALSE
    right_leg_tissue_invalidity_code = FALSE
    left_ribs_imputation_indicator = FALSE
    right_ribs_imputation_indicator = FALSE
    thoracic_spine_imputation_indicator = FALSE
    lumbar_spine_imputation_indicator = FALSE
    pelvis_imputation_indicator = FALSE
    trunk_imputation_indicator = FALSE
    trunk_bone_invalidity_code = FALSE
    trunk_tissue_invalidity_code = FALSE
    if (!isFALSE(head_area_cm2) | !isFALSE(head_bmc_g) | !isFALSE(head_bmd_g.cm2) | !isFALSE(head_fat_g) | 
        !isFALSE(head_lean_excl_bmc_g) | !isFALSE(head_lean_incl_bmc_g) | !isFALSE(head_total_g) | !isFALSE(head_percent_fat)) {
        head_imputation_indicator = "-u"
        head_bone_invalidity_code = "-u"
        head_tissue_invalidity_code = "-u"
    }
    if (!isFALSE(left_arm_area_cm2) | !isFALSE(left_arm_bmc_g) | !isFALSE(left_arm_bmd_g.cm2) | !isFALSE(left_arm_fat_g) | 
        !isFALSE(left_arm_lean_excl_bmc_g) | !isFALSE(left_arm_lean_incl_bmc_g) | !isFALSE(left_arm_total_g) | 
        !isFALSE(left_arm_percent_fat)) {
        left_arm_imputation_indicator = "-u"
        left_arm_bone_invalidity_code = "-u"
        left_arm_tissue_invalidity_code = "-u"
    }
    if (!isFALSE(left_leg_area_cm2) | !isFALSE(left_leg_bmc_g) | !isFALSE(left_leg_bmd_g.cm2) | !isFALSE(left_leg_fat_g) | 
        !isFALSE(left_leg_lean_excl_bmc_g) | !isFALSE(left_leg_lean_incl_bmc_g) | !isFALSE(left_leg_total_g) | 
        !isFALSE(left_leg_percent_fat)) {
        left_leg_imputation_indicator = "-u"
        left_leg_bone_invalidity_code = "-u"
        left_leg_tissue_invalidity_code = "-u"
    }
    if (!isFALSE(right_arm_area_cm2) | !isFALSE(right_arm_bmc_g) | !isFALSE(right_arm_bmd_g.cm2) | !isFALSE(right_arm_fat_g) | 
        !isFALSE(right_arm_lean_excl_bmc_g) | !isFALSE(right_arm_lean_incl_bmc_g) | !isFALSE(right_arm_total_g) | 
        !isFALSE(right_arm_percent_fat)) {
        right_arm_imputation_indicator = "-u"
        right_arm_bone_invalidity_code = "-u"
        right_arm_tissue_invalidity_code = "-u"
    }
    if (!isFALSE(right_leg_area_cm2) | !isFALSE(right_leg_bmc_g) | !isFALSE(right_leg_bmd_g.cm2) | !isFALSE(right_leg_fat_g) | 
        !isFALSE(right_leg_lean_excl_bmc_g) | !isFALSE(right_leg_lean_incl_bmc_g) | !isFALSE(right_leg_total_g) | 
        !isFALSE(right_leg_percent_fat)) {
        right_leg_imputation_indicator = "-u"
        right_leg_bone_invalidity_code = "-u"
        right_leg_tissue_invalidity_code = "-u"
    }
    if (!isFALSE(left_ribs_area_cm2) | !isFALSE(left_ribs_bmc_g) | !isFALSE(left_ribs_bmd_g.cm2)) {
        left_ribs_imputation_indicator = "-u"
    }
    if (!isFALSE(right_ribs_area_cm2) | !isFALSE(right_ribs_bmc_g) | !isFALSE(right_ribs_bmd_g.cm2)) {
        right_ribs_imputation_indicator = "-u"
    }
    if (!isFALSE(thoracic_spine_area_cm2) | !isFALSE(thoracic_spine_bmc_g) | !isFALSE(thoracic_spine_bmd_g.cm2)) {
        thoracic_spine_imputation_indicator = "-u"
    }
    if (!isFALSE(lumbar_spine_area_cm2) | !isFALSE(lumbar_spine_bmc_g) | !isFALSE(lumbar_spine_bmd_g.cm2)) {
        lumbar_spine_imputation_indicator = "-u"
    }
    if (!isFALSE(pelvis_area_cm2) | !isFALSE(pelvis_bmc_g) | !isFALSE(pelvis_bmd_g.cm2)) {
        pelvis_imputation_indicator = "-u"
    }
    if (!isFALSE(trunk_bone_area_cm2) | !isFALSE(trunk_bmc_g) | !isFALSE(trunk_bone_bmd_g.cm2) | !isFALSE(trunk_fat_g) | 
        !isFALSE(trunk_lean_excl_bmc_g) | !isFALSE(trunk_lean_incl_bmc_g) | !isFALSE(trunk_totalg) | 
        !isFALSE(trunk_percent_fat)) {
        trunk_imputation_indicator = "-u"
        trunk_bone_invalidity_code = "-u"
        trunk_tissue_invalidity_code = "-u"
    }
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "dxx_exam_status", "dxaexsts"), head_imputation_indicator, "dxihe"), head_bone_invalidity_code, 
        "dxahebv"), head_area_cm2, "dxxhea"), head_bmc_g, "dxxhebmc"), head_bmd_g.cm2, "dxxhebmd"), head_tissue_invalidity_code, 
        "dxahetv"), head_fat_g, "dxxhefat"), head_lean_excl_bmc_g, "dxdhele"), head_lean_incl_bmc_g, 
        "dxxheli"), head_total_g, "dxdhetot"), head_percent_fat, "dxdhepf"), left_arm_imputation_indicator, 
        "dxila"), left_arm_bone_invalidity_code, "dxalabv"), left_arm_area_cm2, "dxxlaa"), left_arm_bmc_g, 
        "dxxlabmc"), left_arm_bmd_g.cm2, "dxxlabmd"), left_arm_tissue_invalidity_code, "dxalatv"), left_arm_fat_g, 
        "dxxlafat"), left_arm_lean_excl_bmc_g, "dxdlale"), left_arm_lean_incl_bmc_g, "dxxlali"), left_arm_total_g, 
        "dxdlatot"), left_arm_percent_fat, "dxdlapf"), left_leg_imputation_indicator, "dxill"), left_leg_bone_invalidity_code, 
        "dxallbv"), left_leg_area_cm2, "dxxlla"), left_leg_bmc_g, "dxxllbmc"), left_leg_bmd_g.cm2, "dxxllbmd"), 
        left_leg_tissue_invalidity_code, "dxalltv"), left_leg_fat_g, "dxxllfat"), left_leg_lean_excl_bmc_g, 
        "dxdllle"), left_leg_lean_incl_bmc_g, "dxxllli"), left_leg_total_g, "dxdlltot"), left_leg_percent_fat, 
        "dxdllpf"), right_arm_imputation_indicator, "dxira"), right_arm_bone_invalidity_code, "dxarabv"), 
        right_arm_area_cm2, "dxxraa"), right_arm_bmc_g, "dxxrabmc"), right_arm_bmd_g.cm2, "dxxrabmd"), 
        right_arm_tissue_invalidity_code, "dxaratv"), right_arm_fat_g, "dxxrafat"), right_arm_lean_excl_bmc_g, 
        "dxdrale"), right_arm_lean_incl_bmc_g, "dxxrali"), right_arm_total_g, "dxdratot"), right_arm_percent_fat, 
        "dxdrapf"), right_leg_imputation_indicator, "dxirl"), right_leg_bone_invalidity_code, "dxarlbv"), 
        right_leg_area_cm2, "dxxrla"), right_leg_bmc_g, "dxxrlbmc"), right_leg_bmd_g.cm2, "dxxrlbmd"), 
        right_leg_tissue_invalidity_code, "dxarltv"), right_leg_fat_g, "dxxrlfat"), right_leg_lean_excl_bmc_g, 
        "dxdrlle"), right_leg_lean_incl_bmc_g, "dxxrlli"), right_leg_total_g, "dxdrltot"), right_leg_percent_fat, 
        "dxdrlpf"), left_ribs_imputation_indicator, "dxilr"), left_ribs_area_cm2, "dxxlra"), left_ribs_bmc_g, 
        "dxxlrbmc"), left_ribs_bmd_g.cm2, "dxxlrbmd"), right_ribs_imputation_indicator, "dxirr"), right_ribs_area_cm2, 
        "dxxrra"), right_ribs_bmc_g, "dxxrrbmc"), right_ribs_bmd_g.cm2, "dxxrrbmd"), thoracic_spine_imputation_indicator, 
        "dxits"), thoracic_spine_area_cm2, "dxxtsa"), thoracic_spine_bmc_g, "dxxtsbmc"), thoracic_spine_bmd_g.cm2, 
        "dxxtsbmd"), lumbar_spine_imputation_indicator, "dxils"), lumbar_spine_area_cm2, "dxxlsa"), lumbar_spine_bmc_g, 
        "dxxlsbmc"), lumbar_spine_bmd_g.cm2, "dxxlsbmd"), pelvis_imputation_indicator, "dxipe"), pelvis_area_cm2, 
        "dxxpea"), pelvis_bmc_g, "dxxpebmc"), pelvis_bmd_g.cm2, "dxxpebmd"), trunk_imputation_indicator, 
        "dxitr"), trunk_bone_invalidity_code, "dxatrbv"), trunk_bone_area_cm2, "dxdtra"), trunk_bmc_g, 
        "dxdtrbmc"), trunk_bone_bmd_g.cm2, "dxdtrbmd"), trunk_tissue_invalidity_code, "dxatrtv"), trunk_fat_g, 
        "dxxtrfat"), trunk_lean_excl_bmc_g, "dxdtrle"), trunk_lean_incl_bmc_g, "dxxtrli"), trunk_totalg, 
        "dxdtrtot"), trunk_percent_fat, "dxdtrpf"), subtotal_area_cm2, "dxdsta"), subtotal_bmc_g, "dxdstbmc"), 
        subtotal_bmd_g.cm2, "dxdstbmd"), subtotal_fat_g, "dxdstfat"), subtotal_lean_excl_bmc_g, "dxdstle"), 
        subtotal_lean_incl_bmc_g, "dxdstli"), subtotal_total_excl_head_g, "dxdsttot"), subtotal_percent_fat, 
        "dxdstpf"), total_area_cm2, "dxdtoa"), total_bmc_g, "dxdtobmc"), total_bmd_g.cm2, "dxdtobmd"), 
        total_fat_g, "dxdtofat"), total_lean_excl_bmc_g, "dxdtole"), total_lean_incl_bmc_g, "dxdtoli"), 
        total_lean_plus_fat_g, "dxdtotot"), total_percent_fat, "dxdtopf")
    d <- nhs_read(tsv, var, lower_cd = TRUE, cat = FALSE)
    (vcd <- set::grep_and(colnames(d), "_invalidity_code"))
    if (length(vcd) > 0) {
        for (i in vcd) d <- d[d[, i] == 0 & !is.na(d[, i]), ]
        drop_col(d) <- vcd
    }
    ii <- set::grep_and(colnames(d), "_imputation_indicator")
    if (length(ii) > 0) 
        drop_col(d) <- ii
    if ("_mult_" %in% colnames(d) & mult.fun != "unique") {
        years <- unique(d$Year[!is.na(d[, "_mult_"])])
        drop_col(d) <- "_mult_"
        dleft <- unique(d[d$Year %in% years, c("seqn", "Year")])
        for (i in colnames(d)) {
            if (i %in% c("seqn", "Year")) 
                (next)(i)
            if (is.numeric(d[, i])) {
                di <- eval(parse(text = sprintf("aggregate(d$%s,list(seqn=d$seqn),%s)", i, mult.fun)))
                colnames(di)[2] <- i
            }
            else {
                di <- unique(d[, c("seqn", i)])
            }
            dleft <- dplyr::left_join(dleft, di, "seqn")
        }
        d <- rbind(dleft, d[!d$Year %in% years, ])
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dxxag` [exported]

```r
function (data, years, android_fat_mass = FALSE, android_lean_mass = FALSE, android_total_mass = FALSE, 
    gynoid_fat_mass = FALSE, gynoid_lean_mass = FALSE, gynoid_total_mass = FALSE, android_to_gynoid_ratio = FALSE, 
    android_percent_fat = FALSE, gynoid_percent_fat = FALSE, subcutaneous_fat_area = FALSE, subcutaneous_fat_mass = FALSE, 
    subcutaneous_fat_volume = FALSE, total_abdominal_fat_area = FALSE, total_abdominal_fat_mass = FALSE, 
    total_abdominal_fat_volume = FALSE, visceral_adipose_tissue_area = FALSE, visceral_adipose_tissue_mass = FALSE, 
    visceral_adipose_tissue_volume = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("dxxag", years = years, cat = FALSE)
    tsv0(tsv)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "scan_status-u", "dxatrst,dxxagst"), android_fat_mass, "dxxanfm"), android_lean_mass, "dxxanlm"), 
        android_total_mass, "dxxantom"), gynoid_fat_mass, "dxxgyfm"), gynoid_lean_mass, "dxxgylm"), gynoid_total_mass, 
        "dxxgytom"), android_to_gynoid_ratio, "dxxagrat"), android_percent_fat, "dxxapfat"), gynoid_percent_fat, 
        "dxxgpfat"), subcutaneous_fat_area, "dxxsata"), subcutaneous_fat_mass, "dxxsatm"), subcutaneous_fat_volume, 
        "dxxsatv"), total_abdominal_fat_area, "dxxtata"), total_abdominal_fat_mass, "dxxtatm"), total_abdominal_fat_volume, 
        "dxxtatv"), visceral_adipose_tissue_area, "dxxvfata"), visceral_adipose_tissue_mass, "dxxvfatm"), 
        visceral_adipose_tissue_volume, "dxxvfatv")
    var2 <- var
    var <- var2
    d <- nhs_read(tsv, var, cat = FALSE)
    d <- d[d$scan_status == 1, ]
    drop_col(d) <- "scan_status"
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dxxfem` [exported]

```r
function (data, years, total_femur_area_cm2 = FALSE, total_femur_bmc_g = FALSE, total_femur_bmd_g.cm2 = FALSE, 
    femoral_neck_area_cm2 = FALSE, femoral_neck_bmc_g = FALSE, femoral_neck_bmd_g.cm2 = FALSE, trochanter_area_cm2 = FALSE, 
    trochanter_bmc_g = FALSE, trochanter_bmd_g.cm2 = FALSE, intertrochanter_area_cm2 = FALSE, intertrochanter_bmc_g = FALSE, 
    intertrochanter_bmd_g.cm2 = FALSE, ward_triangle_area_cm2 = FALSE, ward_triangle_bmc_g = FALSE, ward_triangle_bmd_g.cm2 = FALSE, 
    calculated_k_for_femur = FALSE, calculated_do_for_femur = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("dxxfem", years = years, cat = FALSE)
    tsv0(tsv)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "scan_status-u", "dxafmrst"), "invalidity_code-u", "dxxfmbcc"), total_femur_bmd_g.cm2, "dxxofbmd"), 
        total_femur_bmc_g, "dxxofbmc"), total_femur_area_cm2, "dxxofa"), femoral_neck_bmd_g.cm2, "dxxnkbmd"), 
        femoral_neck_bmc_g, "dxxnkbmc"), femoral_neck_area_cm2, "dxxnka"), trochanter_bmd_g.cm2, "dxxtrbmd"), 
        trochanter_bmc_g, "dxxtrbmc"), trochanter_area_cm2, "dxxtra"), intertrochanter_bmd_g.cm2, "dxxinbmd"), 
        intertrochanter_bmc_g, "dxxinbmc"), intertrochanter_area_cm2, "dxxina"), ward_triangle_bmd_g.cm2, 
        "dxxwdbmd"), ward_triangle_bmc_g, "dxxwdbmc"), ward_triangle_area_cm2, "dxxwda"), calculated_k_for_femur, 
        "dxafmrk"), calculated_do_for_femur, "dxafmrd0")
    d <- nhs_read(tsv, var, cat = FALSE)
    d <- d[d$scan_status == 1 & d$invalidity_code == 0, ]
    drop_col(d) <- c("scan_status", "invalidity_code")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_dxxspn` [exported]

```r
function (data, years, total_spine_area_cm2 = FALSE, total_spine_bmc_g = FALSE, total_spine_bmd_g.cm2 = FALSE, 
    l1_area_cm2 = FALSE, l1_bmc_g = FALSE, l1_bmd_g.cm2 = FALSE, l2_area_cm2 = FALSE, l2_bmc_g = FALSE, 
    l2_bmd_g.cm2 = FALSE, l3_area_cm2 = FALSE, l3_bmc_g = FALSE, l3_bmd_g.cm2 = FALSE, l4_area_cm2 = FALSE, 
    l4_bmc_g = FALSE, l4_bmd_g.cm2 = FALSE, calculated_k_for_spine = FALSE, calculated_d0_for_spine = FALSE, 
    total_trabecular_bone_score = FALSE, l1_tbs = FALSE, l2_tbs = FALSE, l3_tbs = FALSE, l4_tbs = FALSE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("dxxspn", years = years, cat = FALSE)
    tsv0(tsv)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "scan_status-u", "dxaspnst"), "invalidity_code-u", "dxxosbcc"), total_spine_bmd_g.cm2, "dxxosbmd"), 
        total_spine_bmc_g, "dxxosbmc"), total_spine_area_cm2, "dxxosa"), l1_area_cm2, "dxxl1a"), l1_bmc_g, 
        "dxxl1bmc"), l1_bmd_g.cm2, "dxxl1bmd"), l2_area_cm2, "dxxl2a"), l2_bmc_g, "dxxl2bmc"), l2_bmd_g.cm2, 
        "dxxl2bmd"), l3_area_cm2, "dxxl3a"), l3_bmc_g, "dxxl3bmc"), l3_bmd_g.cm2, "dxxl3bmd"), l4_area_cm2, 
        "dxxl4a"), l4_bmc_g, "dxxl4bmc"), l4_bmd_g.cm2, "dxxl4bmd"), calculated_k_for_spine, "dxaspnk"), 
        calculated_d0_for_spine, "dxaspnd0"), total_trabecular_bone_score, "dxxtotbs"), l1_tbs, "dxxl1tbs"), 
        l2_tbs, "dxxl2tbs"), l3_tbs, "dxxl3tbs"), l4_tbs, "dxxl4tbs")
    d <- nhs_read(tsv, var, cat = FALSE)
    d <- d[d$scan_status == 1 & d$invalidity_code == 0, ]
    drop_col(d) <- c("scan_status", "invalidity_code")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_eating.occasion` [exported]

```r
function (years, day = 1) 
{
    iff <- nhs_tsv(sprintf("xiff|%siff", day[1]), years = years, cat = FALSE)
    d <- nhs_read(iff, sprintf("drd030,drd030z,dr%s_030z:eating.occasion.name", day[1]), cat = FALSE)
    freq_count(d, "eating.occasion.name")
}
```

## `db_flavonoids` [exported]

```r
function (data, years, dietary = c("tot", "iff"), day = 1, fun = c("mean", "sum", "alone"), Daidzein_mg = FALSE, 
    Genistein_mg = FALSE, Glycitein_mg = FALSE, Cyanidin_mg = FALSE, Petunidin_mg = FALSE, Delphinidin_mg = FALSE, 
    Malvidin_mg = FALSE, Pelargonidin_mg = FALSE, Peonidin_mg = FALSE, Catechin_mg = FALSE, Epigallocatechin_mg = FALSE, 
    Epicatechin_mg = FALSE, Epicatechin_3_gallate_mg = FALSE, Epigallocatechin_3_gallate_mg = FALSE, 
    Theaflavin_mg = FALSE, Thearubigins_mg = FALSE, Eriodictyol_mg = FALSE, Hesperetin_mg = FALSE, Naringenin_mg = FALSE, 
    Apigenin_mg = FALSE, Luteolin_mg = FALSE, Isorhamnetin_mg = FALSE, Kaempferol_mg = FALSE, Myricetin_mg = FALSE, 
    Quercetin_mg = FALSE, Theaflavin_3_3_digallate_mg = FALSE, Theaflavin_3q_gallate_mg = FALSE, Theaflavin_3_gallate_mg = FALSE, 
    Gallocatechin_mg = FALSE, Subtotal_Catechins_mg = FALSE, Total_Isoflavones_mg = FALSE, Total_Anthocyanidins_mg = FALSE, 
    Total_Flavan_3_ols_mg = FALSE, Total_Flavanones_mg = FALSE, Total_Flavones_mg = FALSE, Total_Flavonols_mg = FALSE, 
    Total_Sum_of_all_29_flavonoids_mg = FALSE, both2days = TRUE, join = "left", Year = FALSE) 
{
    dietary <- match.arg(dietary)
    fun <- match.arg(fun)
    years <- data_years(data, years)
    (years <- set::and(prepare_years(years), prepare_years(c(2007, 2010, 2018))))
    (fl <- list.files(get_Flavonoids_path(), "\\.sas7bdat", full.names = TRUE))
    (pt <- sapply(years, function(i) paste0(do::right(strsplit(i, "-")[[1]], 2), collapse = "|")))
    (fl <- fl[grepl(paste0(pt, collapse = "|"), fl)])
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "seqn", "seqn"), "line", "dr1iline,dr2iline"), Daidzein_mg, "dr1t_fl710,dr2t_fl710,dr1i_fl710,dr2i_fl710"), 
        Genistein_mg, "dr1t_fl711,dr2t_fl711,dr1i_fl711,dr2i_fl711"), Glycitein_mg, "dr1t_fl712,dr2t_fl712,dr1i_fl712,dr2i_fl712"), 
        Cyanidin_mg, "dr1t_fl731,dr2t_fl731,dr1i_fl731,dr2i_fl731"), Petunidin_mg, "dr1t_fl740,dr2t_fl740,dr1i_fl740,dr2i_fl740"), 
        Delphinidin_mg, "dr1t_fl741,dr2t_fl741,dr1i_fl741,dr2i_fl741"), Malvidin_mg, "dr1t_fl742,dr2t_fl742,dr1i_fl742,dr2i_fl742"), 
        Pelargonidin_mg, "dr1t_fl743,dr2t_fl743,dr1i_fl743,dr2i_fl743"), Peonidin_mg, "dr1t_fl745,dr2t_fl745,dr1i_fl745,dr2i_fl745"), 
        Catechin_mg, "dr1t_fl749,dr2t_fl749,dr1i_fl749,dr2i_fl749"), Epigallocatechin_mg, "dr1t_fl750,dr2t_fl750,dr1i_fl750,dr2i_fl750"), 
        Epicatechin_mg, "dr1t_fl751,dr2t_fl751,dr1i_fl751,dr2i_fl751"), Epicatechin_3_gallate_mg, "dr1t_fl752,dr2t_fl752,dr1i_fl752,dr2i_fl752"), 
        Epigallocatechin_3_gallate_mg, "dr1t_fl753,dr2t_fl753,dr1i_fl753,dr2i_fl753"), Theaflavin_mg, 
        "dr1t_fl755,dr2t_fl755,dr1i_fl755,dr2i_fl755"), Thearubigins_mg, "dr1t_fl756,dr2t_fl756,dr1i_fl756,dr2i_fl756"), 
        Eriodictyol_mg, "dr1t_fl758,dr2t_fl758,dr1i_fl758,dr2i_fl758"), Hesperetin_mg, "dr1t_fl759,dr2t_fl759,dr1i_fl759,dr2i_fl759"), 
        Naringenin_mg, "dr1t_fl762,dr2t_fl762,dr1i_fl762,dr2i_fl762"), Apigenin_mg, "dr1t_fl770,dr2t_fl770,dr1i_fl770,dr2i_fl770"), 
        Luteolin_mg, "dr1t_fl773,dr2t_fl773,dr1i_fl773,dr2i_fl773"), Isorhamnetin_mg, "dr1t_fl785,dr2t_fl785,dr1i_fl785,dr2i_fl785"), 
        Kaempferol_mg, "dr1t_fl786,dr2t_fl786,dr1i_fl786,dr2i_fl786"), Myricetin_mg, "dr1t_fl788,dr2t_fl788,dr1i_fl788,dr2i_fl788"), 
        Quercetin_mg, "dr1t_fl789,dr2t_fl789,dr1i_fl789,dr2i_fl789"), Theaflavin_3_3_digallate_mg, "dr1t_fl791,dr2t_fl791,dr1i_fl791,dr2i_fl791"), 
        Theaflavin_3q_gallate_mg, "dr1t_fl792,dr2t_fl792,dr1i_fl792,dr2i_fl792"), Theaflavin_3_gallate_mg, 
        "dr1t_fl793,dr2t_fl793,dr1i_fl793,dr2i_fl793"), Gallocatechin_mg, "dr1t_fl794,dr2t_fl794,dr1i_fl794,dr2i_fl794"), 
        Subtotal_Catechins_mg, "dr1t_fl_catechin,dr2t_fl_catechin,dr1i_fl_catechin,dr2i_fl_catechin"), 
        Total_Isoflavones_mg, "dr1t_fl_iso,dr2t_fl_iso,dr1i_fl_iso,dr2i_fl_iso"), Total_Anthocyanidins_mg, 
        "dr1t_fl_antho,dr2t_fl_antho,dr1i_fl_antho,dr2i_fl_antho"), Total_Flavan_3_ols_mg, "dr1t_fl_3_ols,dr2t_fl_3_ols,dr1i_fl_3_ols,dr2i_fl_3_ols"), 
        Total_Flavanones_mg, "dr1t_fl_nones,dr2t_fl_nones,dr1i_fl_nones,dr2i_fl_nones"), Total_Flavones_mg, 
        "dr1t_fl_ones,dr2t_fl_ones,dr1i_fl_ones,dr2i_fl_ones"), Total_Flavonols_mg, "dr1t_fl_ols,dr2t_fl_ols,dr1i_fl_ols,dr2i_fl_ols"), 
        Total_Sum_of_all_29_flavonoids_mg, "dr1t_fl_total,dr2t_fl_total,dr1i_fl_total,dr2i_fl_total")
    if (length(day) == 1) {
        ck <- lookl(do::file.name(fl), paste0(sprintf("flav_dr%s%s_", day, rep(dietary, length(day))), 
            collapse = "|"))
        (fl <- fl[ck])
        d <- do.call(lapply(fl, function(i) {
            d1 <- as.data.frame(drop_col(haven::read_sas(i), "sddsrvyr", "dr1drstz", "dr2drstz"))
            select_col(col_rename(d1, var2), do::Replace0(var2, ".*: {0,}"))
        }), what = plyr::rbind.fill)
    }
    else if (length(day) == 2) {
        ck <- lookl(do::file.name(fl), paste0(sprintf("flav_dr%s%s_", 1, rep(dietary, length(day))), 
            collapse = "|"))
        (f1 <- fl[ck])
        d1 <- do.call(lapply(f1, function(i) {
            select_col(col_rename(drop_col(as.data.frame(haven::read_sas(i)), "sddsrvyr", "dr1drstz", 
                "dr2drstz"), var2), do::Replace0(var2, ".*: {0,}"))
        }), what = plyr::rbind.fill)
        if (dietary == "iff") {
            (tsv <- nhs_tsv(sprintf("drxiff|dr%siff", 1), years = c(2007, 2009, 2017), cat = FALSE))
            d1iff <- nhs_read(tsv, cat = FALSE)
            d1iff <- d1iff[, c("seqn", "line", "food.code")]
            d1 <- dplyr::left_join(d1, d1iff, c("seqn", "line"))
            d1$line <- NULL
            d1 <- d1[, unique(c("seqn", "food.code", colnames(d1)))]
            d1 <- group_sum(d1, set::not(colnames(d1), c("seqn", "food.code")), c("seqn", "food.code"))
        }
        ck <- lookl(do::file.name(fl), paste0(sprintf("flav_dr%s%s_", 2, rep(dietary, length(day))), 
            collapse = "|"))
        (f2 <- fl[ck])
        d2 <- do.call(lapply(f2, function(i) {
            di <- col_rename(as.data.frame(drop_col(haven::read_sas(i), "sddsrvyr", "dr1drstz", "dr2drstz")), 
                var2)
            select_col(di, do::Replace0(var2, ".*: {0,}"))
        }), what = plyr::rbind.fill)
        if (dietary == "iff") {
            (tsv <- nhs_tsv(sprintf("drxiff|dr%siff", 2), years = c(2007, 2009, 2017), cat = FALSE))
            d2iff <- nhs_read(tsv, cat = FALSE)
            d2iff <- d2iff[, c("seqn", "line", "food.code")]
            d2 <- dplyr::left_join(d2, d2iff, c("seqn", "line"))
            d2$line <- NULL
            d2 <- d2[, unique(c("seqn", "food.code", colnames(d2)))]
            d2 <- group_sum(d2, set::not(colnames(d2), c("seqn", "food.code")), c("seqn", "food.code"))
        }
        if (dietary == "iff") 
            key = c("seqn", "food.code")
        else key = "seqn"
        d <- dplyr::full_join(d1, d2, key, suffix = c(".d1", ".d2"))
        if (fun %in% c("sum", "mean")) {
            commen <- set::not(set::and(colnames(d1), colnames(d2)), key)
            for (i in commen) {
                c12 <- paste0(i, c(".d1", ".d2"))
                cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                d$xx <- cal
                colnames(d)[ncol(d)] <- i
                d <- drop_col(d, c12)
            }
        }
    }
    d <- expss::drop_all_labels(d)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_flxcln` [exported]

```r
function (data, years, central_incisor = FALSE, lateral_incisor = FALSE, cuspid = FALSE, bicuspid1 = FALSE, 
    bicuspid2 = FALSE, molar1 = FALSE, molar2 = FALSE, Year = FALSE, join = "left", lower_cd = TRUE) 
{
    var <- c()
    if (central_incisor) 
        append(var) <- c("fcx09di,ohx09di:ci_up_lt", "fcx24di,ohx24di:ci_lw_lt", "fcx08di,ohx08di:ci_up_rt", 
            "fcx25di,ohx25di:ci_lw_rt")
    if (lateral_incisor) 
        append(var) <- c("fcx10di,ohx10di:li_up_lt", "fcx23di,ohx23di:li_lw_lt", "fcx07di,ohx07di:li_up_rt", 
            "fcx26di,ohx26di:li_lw_rt")
    if (cuspid) 
        append(var) <- c("fcx11di,ohx11di:c_up_lt", "fcx22di,ohx22di:c_lw_lt", "fcx06di,ohx06di:c_up_rt", 
            "fcx27di,ohx27di:c_lw_rt")
    if (bicuspid1) 
        append(var) <- c("fcx21di,ohx21di:b1_lw_lt", "fcx12di,ohx12di:b1_up_lt", "fcx05di,ohx05di:b1_up_rt", 
            "fcx28di,ohx28di:b1_lw_rt")
    if (bicuspid2) 
        append(var) <- c("fcx13di,ohx13di:b2_up_lt", "fcx20di,ohx20di:b2_lw_lt", "fcx04di,ohx04di:b2_up_rt", 
            "fcx29di,ohx29di:b2_lw_rt")
    if (molar1) 
        append(var) <- c("fcx14di,ohx14di:m1_up_lt", "fcx19di,ohx19di:m1_lw_lt", "fcx03di,ohx03di:m1_up_rt", 
            "fcx30di,ohx30di:m1_lw_rt")
    if (molar2) 
        append(var) <- c("fcx15di,ohx15di:m2_up_lt", "fcx18di,ohx18di:m2_lw_lt", "fcx02di,ohx02di:m2_up_rt", 
            "fcx31di,ohx31di:m2_lw_rt")
    years <- data_years(data, years)
    tsv <- nhs_tsv("flxcln", years = years, cat = F)
    tsv0(tsv)
    d <- nhs_read(tsv, var, cat = F, lower_cd = lower_cd)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_fndds` [exported]

```r
function (data, years, files, Year = FALSE, join = "left", nrow = Inf) 
{
    years <- data_years(data, years)
    fndds <- paste0(get_config_path(), "/fndds")
    tsv <- set::grep_or(set::grep_not_or(set::grep_or(list.files(fndds, "tsv", full.names = TRUE, recursive = TRUE), 
        prepare_years(years)), "FNDDSRecCount"), files)
    tsv
    tsv0(tsv)
    years.all <- do::Replace0(tsv, paste0(get_config_path(), "/fndds/FNDDS_"), "_ACCESS.*")
    (years.u <- unique(years.all))
    for (j in 1:length(years.u)) {
        if (j == 1) {
            res <- lapply(1:length(years.u), function(i) NULL)
            names(res) <- years.u
        }
        yeari <- years.u[j]
        fj <- tsv[years.all == yeari]
        (nt <- do::Replace0(do::file.name(fj), ".tsv"))
        names(fj) <- nt
        order <- c("MainFoodDesc", "AddFoodDesc", "FoodWeights", "FoodSubcodeLinks", "SubcodeDesc", "FoodPortionDesc", 
            "FNDDSNutVal", "MoistAdjust", "NutDesc", "FNDDSIngred", "IngredNutVal", "DerivDesc")
        (fj <- fj[set::and(order, nt)])
        names(fj) <- NULL
        key <- c("food.code", "portion.code", "nutrient.code", "subcode", "derivation.code", "ingredient.code")
        for (i in 1:length(fj)) {
            (fji <- fj[i])
            di <- drop_col(data.table::fread(fji, data.table = FALSE, nrows = nrow), "Year", "start.date", 
                "end.date")
            fjc <- do::Replace(fji, "\\.tsv", ".codebook")
            if (file.exists(fjc)) {
                ci <- data.table::fread(fjc, data.table = FALSE)
                for (iv in unique(ci$variable)) {
                  code <- ci$code[ci$variable %in% iv]
                  label <- ci$label[ci$variable %in% iv]
                  for (k in 1:length(code)) {
                    di[di[, iv] %in% code[k], iv] <- label[k]
                  }
                }
            }
            col_rename(di) <- c("fortification.identifier.code:fortification.identifier", "wweia.category.number:wweia.category.code")
            for (k in 1:ncol(di)) {
                di[, k] <- tolower(di[, k])
            }
            if (is.null(res[[yeari]])) {
                res[[yeari]] <- di
            }
            else {
                (kl <- set::and(colnames(res[[yeari]]), key))
                (kr <- set::and(colnames(di), key))
                (klr <- set::and(kl, kr))
                by <- sprintf(paste0(paste0("'", klr, "'='", klr, "'"), collapse = ", "), fmt = "c(%s)")
                eval(parse(text = sprintf("res[[yeari]] <- dplyr::full_join(res[[yeari]],di,by=%s)", 
                  by)))
            }
            if (i == length(fj)) 
                fj <- do::complete.data(fj)
        }
    }
    for (i in 1:length(res)) {
        ri <- res[[i]]
        if (is.data.frame(ri)) {
            ri$Year <- names(res)[i]
            res[[i]] <- ri
        }
    }
    res <- do.call(plyr::rbind.fill, res)
    res <- res[, unique(c("Year", colnames(res)))]
    if ("food.code" %in% colnames(res)) {
        isna <- is.na(res$food.code)
        res$food.code <- format(res$food.code, width = 8)
        res$food.code[isna] <- NA
    }
    return_data(data, res, Year, key = "seqn", join = join)
}
```

## `db_fped` [exported]

```r
function (data, years, day = c("1", "2"), dietary = c("tot", "iff"), version = c("2015", "2010"), fun = c("sum", 
    "mean"), f_citmlb = FALSE, f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, 
    v_redor_tomato = FALSE, v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, 
    v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, 
    g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, 
    pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, 
    pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, 
    add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, seaplant = FALSE, addsugc = FALSE, 
    solfatc = FALSE, vtotalleg = FALSE, vdrkgrleg = FALSE, pfallprotleg = FALSE, pfseaplantleg = FALSE, 
    Year = F, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c()), 
        Year, "Year"), f_citmlb, "f_citmlb"), f_other, "f_other"), f_whole, "f_whole"), f_juice, "f_juice"), 
        f_total, "f_total"), v_drkgr, "v_drkgr"), v_redor_tomato, "v_redor_tomato"), v_redor_other, "v_redor_other"), 
        v_redor_total, "v_redor_total"), v_starchy_potato, "v_starchy_potato"), v_starchy_other, "v_starchy_other"), 
        v_starchy_total, "v_starchy_total"), v_other, "v_other"), v_total, "v_total"), v_legumes, "v_legumes"), 
        g_whole, "g_whole"), g_refined, "g_refined"), g_total, "g_total"), d_milk, "d_milk"), d_yogurt, 
        "d_yogurt"), d_cheese, "d_cheese"), d_total, "d_total"), pf_meat, "pf_meat"), pf_curedmeat, "pf_curedmeat"), 
        pf_organ, "pf_organ"), pf_poult, "pf_poult"), pf_seafd_hi, "pf_seafd_hi"), pf_seafd_low, "pf_seafd_low"), 
        pf_mps_total, "pf_mps_total"), pf_eggs, "pf_eggs"), pf_soy, "pf_soy"), pf_nutsds, "pf_nutsds"), 
        pf_legumes, "pf_legumes"), pf_total, "pf_total"), add_sugars, "add_sugars"), oils, "oils"), solid_fats, 
        "solid_fats"), a_drinks, "a_drinks"), seaplant, "seaplant"), addsugc, "addsugc"), solfatc, "solfatc"), 
        vtotalleg, "vtotalleg"), vdrkgrleg, "vdrkgrleg"), pfallprotleg, "pfallprotleg"), pfseaplantleg, 
        "pfseaplantleg")
    if (is.null(var2)) 
        return()
    (years <- data_years(data, years))
    day <- as.character(day)
    dietary <- match.arg(dietary)
    version <- as.character(version)
    version <- match.arg(version)
    if (dietary == "iff") 
        key <- c("seqn", "food.code")
    else key <- "seqn"
    d <- lapply(years, function(i) {
        d <- fped_read(i, day, dietary, version, fun, FALSE)
        if (nrow(d) == 0) 
            return()
        cbind(Year = i, d)
    }) %>% do.call(what = plyr::rbind.fill)
    col_rename(d) <- var2
    d <- d[, c(key, do::Replace0(var2, ".*:")), drop = FALSE]
    return_data(data, d, Year, key = key, join = join)
}
```

## `db_fped.g` [internal]

```r
function (data, years, day = c("1", "2"), dietary = c("tot", "iff"), fun = c("mean", "sum"), f_citmlb = FALSE, 
    f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, v_redor_tomato = FALSE, 
    v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, 
    v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, 
    g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, 
    pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, 
    pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, 
    add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
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
    if (is.null(var2)) 
        return()
    years <- data_years(data, years)
    day <- as.character(day)
    dietary <- match.arg(dietary)
    fun <- match.arg(fun)
    d <- fped_read(years, day, "iff", 2010, "sum", FALSE)
    d1 <- db_driff(years = years, grams = T, day = day, fun = fun)
    d1 <- aggregate_sum(d1, x = "grams", by = c("seqn", "food.code"))
    d <- dplyr::left_join(d, d1, c("seqn", "food.code"))
    d$f_citmlb[d$f_citmlb > 0] <- d$grams[d$f_citmlb > 0]
    d$f_other[d$f_other > 0] <- d$grams[d$f_other > 0]
    d$f_whole <- d$f_citmlb + d$f_other
    d$f_juice[d$f_juice > 0] <- d$grams[d$f_juice > 0]
    d$f_total <- d$f_citmlb + d$f_other + d$f_juice
    ck <- d$f_total > 0 & d$f_citmlb == 0 & d$f_juice == 0 & d$f_other == 0
    d$f_total[ck] <- d$grams[ck]
    d$v_drkgr[d$v_drkgr > 0] <- d$grams[d$v_drkgr > 0]
    d$v_redor_tomato[d$v_redor_tomato > 0] <- d$grams[d$v_redor_tomato > 0]
    d$v_redor_other[d$v_redor_other > 0] <- d$grams[d$v_redor_other > 0]
    d$v_redor_total <- d$v_redor_tomato + d$v_redor_other
    ck <- d$v_redor_total > 0 & d$v_redor_tomato == 0 & d$v_redor_other == 0
    d$v_redor_total[ck] <- d$grams[ck]
    d$v_starchy_potato[d$v_starchy_potato > 0] <- d$grams[d$v_starchy_potato > 0]
    d$v_starchy_other[d$v_starchy_other > 0] <- d$grams[d$v_starchy_other > 0]
    d$v_starchy_total <- d$v_starchy_potato + d$v_starchy_other
    ck <- d$v_starchy_total > 0 & d$v_starchy_potato == 0 & d$v_starchy_other == 0
    d$v_starchy_total[ck] <- d$grams[ck]
    d$v_other[d$v_other > 0] <- d$grams[d$v_other > 0]
    d$v_total <- d$v_drkgr + d$v_redor_tomato + d$v_redor_other + d$v_starchy_potato + d$v_starchy_other + 
        d$v_other
    ck <- d$v_total > 0 & d$v_drkgr == 0 & d$v_redor_tomato == 0 & d$v_redor_other == 0 & d$v_starchy_potato == 
        0 & d$v_starchy_other == 0 & d$v_other == 0
    d$v_total[ck] <- d$grams[ck]
    d$v_legumes[d$v_legumes > 0] <- d$grams[d$v_legumes > 0]
    d$g_whole[d$g_whole > 0] <- d$grams[d$g_whole > 0]
    d$g_refined[d$g_refined > 0] <- d$grams[d$g_refined > 0]
    d$g_total <- d$g_whole + d$g_refined
    ck <- d$g_total > 0 & d$g_whole == 0 & d$g_refined == 0
    d$g_total[ck] <- d$grams[ck]
    d$d_milk[d$d_milk > 0] <- d$grams[d$d_milk > 0]
    d$d_yogurt[d$d_yogurt > 0] <- d$grams[d$d_yogurt > 0]
    d$d_cheese[d$d_cheese > 0] <- d$grams[d$d_cheese > 0]
    d$d_total <- d$d_milk + d$d_yogurt + d$d_cheese
    ck <- d$d_total > 0 & d$d_milk == 0 & d$d_yogurt == 0 & d$d_cheese == 0
    d$d_total[ck] <- d$grams[ck]
    d$pf_meat[d$pf_meat > 0] <- d$grams[d$pf_meat > 0]
    d$pf_curedmeat[d$pf_curedmeat > 0] <- d$grams[d$pf_curedmeat > 0]
    d$pf_organ[d$pf_organ > 0] <- d$grams[d$pf_organ > 0]
    d$pf_poult[d$pf_poult > 0] <- d$grams[d$pf_poult > 0]
    d$pf_seafd_hi[d$pf_seafd_hi > 0] <- d$grams[d$pf_seafd_hi > 0]
    d$pf_seafd_low[d$pf_seafd_low > 0] <- d$grams[d$pf_seafd_low > 0]
    d$pf_mps_total <- d$pf_meat + d$pf_curedmeat + d$pf_organ + d$pf_poult + d$pf_seafd_hi + d$pf_seafd_low
    ck <- d$pf_mps_total > 0 & d$pf_meat == 0 & d$pf_curedmeat == 0 & d$pf_organ == 0 & d$pf_poult == 
        0 & d$pf_seafd_hi == 0 & d$pf_seafd_low == 0
    d$pf_mps_total[ck] <- d$grams[ck]
    d$pf_eggs[d$pf_eggs > 0] <- d$grams[d$pf_eggs > 0]
    d$pf_soy[d$pf_soy > 0] <- d$grams[d$pf_soy > 0]
    d$pf_nutsds[d$pf_nutsds > 0] <- d$grams[d$pf_nutsds > 0]
    d$pf_legumes <- d$v_legumes * 4
    d$pf_total <- d$pf_meat + d$pf_curedmeat + d$pf_organ + d$pf_poult + d$pf_seafd_hi + d$pf_seafd_low + 
        d$pf_eggs + d$pf_soy + d$pf_nutsds
    ck <- d$pf_total > 0 & d$pf_meat == 0 & d$pf_curedmeat == 0 & d$pf_organ == 0 & d$pf_poult == 0 & 
        d$pf_seafd_hi == 0 & d$pf_seafd_low == 0 & d$pf_eggs + d$pf_soy == 0 & d$pf_nutsds == 0
    d$pf_total[ck] <- d$grams[ck]
    d$add_sugars[d$add_sugars > 0] <- d$grams[d$add_sugars > 0]
    d$oils[d$oils > 0] <- d$grams[d$oils > 0]
    d$solid_fats[d$solid_fats > 0] <- d$grams[d$solid_fats > 0]
    d$a_drinks[d$a_drinks > 0] <- d$grams[d$a_drinks > 0]
    col_rename(d) <- var2
    var2 <- do::Replace0(var2, ".*:")
    if (dietary == "tot") {
        key = "seqn"
        var2 <- unique(c("grams", var2))
        d <- d[, c("seqn", var2)]
        d <- aggregate_sum(data = d, x = var2, by = "seqn")
    }
    else {
        (var2 <- unique(c("grams", var2)))
        d <- d[, c("seqn", "food.code", var2)]
        if (!missing(data)) {
            if ("food.code" %in% colnames(data)) {
                key <- c("seqn", "food.code")
            }
            else {
                key <- "seqn"
            }
        }
        else {
            key <- c("seqn", "food.code")
        }
    }
    return_data(data, d, FALSE, key = key, join = join)
}
```

## `db_fped.kcal` [internal]

```r
function (data, years, day = c("1", "2"), dietary = c("tot", "iff"), fun = c("mean", "sum"), f_citmlb = FALSE, 
    f_other = FALSE, f_whole = FALSE, f_juice = FALSE, f_total = FALSE, v_drkgr = FALSE, v_redor_tomato = FALSE, 
    v_redor_other = FALSE, v_redor_total = FALSE, v_starchy_potato = FALSE, v_starchy_other = FALSE, 
    v_starchy_total = FALSE, v_other = FALSE, v_total = FALSE, v_legumes = FALSE, g_whole = FALSE, g_refined = FALSE, 
    g_total = FALSE, d_milk = FALSE, d_yogurt = FALSE, d_cheese = FALSE, d_total = FALSE, pf_meat = FALSE, 
    pf_curedmeat = FALSE, pf_organ = FALSE, pf_poult = FALSE, pf_seafd_hi = FALSE, pf_seafd_low = FALSE, 
    pf_mps_total = FALSE, pf_eggs = FALSE, pf_soy = FALSE, pf_nutsds = FALSE, pf_legumes = FALSE, pf_total = FALSE, 
    add_sugars = FALSE, oils = FALSE, solid_fats = FALSE, a_drinks = FALSE, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
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
    if (is.null(var2)) 
        return()
    years <- data_years(data, years)
    day <- as.character(day)
    dietary <- match.arg(dietary)
    d <- fped_read(years, day, "iff", 2010, fun, FALSE)
    d1 <- drop_col(db_driff(years = years, energy_kcal = "kcal"), "food.code")
    d <- dplyr::left_join(d, d1, c("seqn", "line"))
    d$f_citmlb[d$f_citmlb > 0] <- d$kcal[d$f_citmlb > 0]
    d$f_other[d$f_other > 0] <- d$kcal[d$f_other > 0]
    d$f_whole <- d$f_citmlb + d$f_other
    d$f_juice[d$f_juice > 0] <- d$kcal[d$f_juice > 0]
    d$f_total <- d$f_citmlb + d$f_other + d$f_juice
    ck <- d$f_total > 0 & d$f_citmlb == 0 & d$f_juice == 0 & d$f_other == 0
    d$f_total[ck] <- d$kcal[ck]
    d$v_drkgr[d$v_drkgr > 0] <- d$kcal[d$v_drkgr > 0]
    d$v_redor_tomato[d$v_redor_tomato > 0] <- d$kcal[d$v_redor_tomato > 0]
    d$v_redor_other[d$v_redor_other > 0] <- d$kcal[d$v_redor_other > 0]
    d$v_redor_total <- d$v_redor_tomato + d$v_redor_other
    ck <- d$v_redor_total > 0 & d$v_redor_tomato == 0 & d$v_redor_other == 0
    d$v_redor_total[ck] <- d$kcal[ck]
    d$v_starchy_potato[d$v_starchy_potato > 0] <- d$kcal[d$v_starchy_potato > 0]
    d$v_starchy_other[d$v_starchy_other > 0] <- d$kcal[d$v_starchy_other > 0]
    d$v_starchy_total <- d$v_starchy_potato + d$v_starchy_other
    ck <- d$v_starchy_total > 0 & d$v_starchy_potato == 0 & d$v_starchy_other == 0
    d$v_starchy_total[ck] <- d$kcal[ck]
    d$v_other[d$v_other > 0] <- d$kcal[d$v_other > 0]
    d$v_total <- d$v_drkgr + d$v_redor_tomato + d$v_redor_other + d$v_starchy_potato + d$v_starchy_other + 
        d$v_other
    ck <- d$v_total > 0 & d$v_drkgr == 0 & d$v_redor_tomato == 0 & d$v_redor_other == 0 & d$v_starchy_potato == 
        0 & d$v_starchy_other == 0 & d$v_other == 0
    d$v_total[ck] <- d$kcal[ck]
    d$v_legumes[d$v_legumes > 0] <- d$kcal[d$v_legumes > 0]
    d$g_whole[d$g_whole > 0] <- d$kcal[d$g_whole > 0]
    d$g_refined[d$g_refined > 0] <- d$kcal[d$g_refined > 0]
    d$g_total <- d$g_whole + d$g_refined
    ck <- d$g_total > 0 & d$g_whole == 0 & d$g_refined == 0
    d$g_total[ck] <- d$kcal[ck]
    d$d_milk[d$d_milk > 0] <- d$kcal[d$d_milk > 0]
    d$d_yogurt[d$d_yogurt > 0] <- d$kcal[d$d_yogurt > 0]
    d$d_cheese[d$d_cheese > 0] <- d$kcal[d$d_cheese > 0]
    d$d_total <- d$d_milk + d$d_yogurt + d$d_cheese
    ck <- d$d_total > 0 & d$d_milk == 0 & d$d_yogurt == 0 & d$d_cheese == 0
    d$d_total[ck] <- d$kcal[ck]
    d$pf_meat[d$pf_meat > 0] <- d$kcal[d$pf_meat > 0]
    d$pf_curedmeat[d$pf_curedmeat > 0] <- d$kcal[d$pf_curedmeat > 0]
    d$pf_organ[d$pf_organ > 0] <- d$kcal[d$pf_organ > 0]
    d$pf_poult[d$pf_poult > 0] <- d$kcal[d$pf_poult > 0]
    d$pf_seafd_hi[d$pf_seafd_hi > 0] <- d$kcal[d$pf_seafd_hi > 0]
    d$pf_seafd_low[d$pf_seafd_low > 0] <- d$kcal[d$pf_seafd_low > 0]
    d$pf_mps_total <- d$pf_meat + d$pf_curedmeat + d$pf_organ + d$pf_poult + d$pf_seafd_hi + d$pf_seafd_low
    ck <- d$pf_mps_total > 0 & d$pf_meat == 0 & d$pf_curedmeat == 0 & d$pf_organ == 0 & d$pf_poult == 
        0 & d$pf_seafd_hi == 0 & d$pf_seafd_low == 0
    d$pf_mps_total[ck] <- d$kcal[ck]
    d$pf_eggs[d$pf_eggs > 0] <- d$kcal[d$pf_eggs > 0]
    d$pf_soy[d$pf_soy > 0] <- d$kcal[d$pf_soy > 0]
    d$pf_nutsds[d$pf_nutsds > 0] <- d$kcal[d$pf_nutsds > 0]
    d$pf_legumes <- d$v_legumes * 4
    d$pf_total <- d$pf_meat + d$pf_curedmeat + d$pf_organ + d$pf_poult + d$pf_seafd_hi + d$pf_seafd_low + 
        d$pf_eggs + d$pf_soy + d$pf_nutsds
    ck <- d$pf_total > 0 & d$pf_meat == 0 & d$pf_curedmeat == 0 & d$pf_organ == 0 & d$pf_poult == 0 & 
        d$pf_seafd_hi == 0 & d$pf_seafd_low == 0 & d$pf_eggs + d$pf_soy == 0 & d$pf_nutsds == 0
    d$pf_total[ck] <- d$kcal[ck]
    d$add_sugars[d$add_sugars > 0] <- d$kcal[d$add_sugars > 0]
    d$oils[d$oils > 0] <- d$kcal[d$oils > 0]
    d$solid_fats[d$solid_fats > 0] <- d$kcal[d$solid_fats > 0]
    d$a_drinks[d$a_drinks > 0] <- d$kcal[d$a_drinks > 0]
    col_rename(d) <- var2
    var2 <- do::Replace0(var2, ".*:")
    if (dietary == "tot") {
        key = "seqn"
        var2 <- c("kcal", var2)
        d <- d[, c("seqn", var2)]
        d <- aggregate2(data = d, x = var2, by = "seqn", fun = "sum")
    }
    else {
        var2 <- c("kcal", var2)
        d <- d[, c("seqn", "line", var2)]
        if (!missing(data)) {
            if ("line" %in% colnames(data)) {
                key <- c("seqn", "line")
            }
            else {
                key <- "seqn"
            }
        }
        else {
            key <- "seqn"
        }
    }
    return_data(data, d, FALSE, key = key, join = join)
}
```

## `db_hormone` [exported]

```r
function (data, years, testosterone_ng.dl = FALSE, free_testosterone_ng.dl = FALSE, bioavailable_testosterone_ng.dl = FALSE, 
    sex_hormone_binding_globulin_nmol.l = FALSE, estradiol_pg.ml = FALSE, androstanedione_glucuronide_ng.ml = FALSE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- NULL
    ck1 <- any(!isFALSE(testosterone_ng.dl), !isFALSE(sex_hormone_binding_globulin_nmol.l), !isFALSE(estradiol_pg.ml), 
        !isFALSE(androstanedione_glucuronide_ng.ml))
    if (ck1) {
        ck0 <- !isFALSE(free_testosterone_ng.dl) | !isFALSE(bioavailable_testosterone_ng.dl)
        if (ck0) {
            if (isFALSE(testosterone_ng.dl)) {
                drop_testo <- TRUE
                testosterone_ng.dl <- "testosterone_ng.dl"
            }
            else {
                drop_testo <- FALSE
            }
            if (isFALSE(sex_hormone_binding_globulin_nmol.l)) {
                drop_shbg <- TRUE
                sex_hormone_binding_globulin_nmol.l <- "sex_hormone_binding_globulin_nmol.l"
            }
            else {
                drop_shbg <- FALSE
            }
        }
        if (isTRUE(sex_hormone_binding_globulin_nmol.l)) 
            sex_hormone_binding_globulin_nmol.l <- "sex_hormone_binding_globulin_nmol.l"
        if (isTRUE(testosterone_ng.dl)) 
            testosterone_ng.dl <- "testosterone_ng.dl"
        (tsv <- nhs_tsv("sschl|tst", cat = F, items = "Laboratory", years = years))
        var2 <- variable_formula(variable_formula(variable_formula(variable_formula(c(), testosterone_ng.dl, 
            "sstesto,lbxtst"), sex_hormone_binding_globulin_nmol.l, "ssshbg,lbxshbg"), estradiol_pg.ml, 
            "ssse2,lbxest"), androstanedione_glucuronide_ng.ml, "ss3adlg")
        d <- nhs_read(tsv, var2, cat = F)
        (ck.y <- d$Year %in% prepare_years(1999:2003))
        if (testosterone_ng.dl %in% colnames(d) & any(ck.y)) {
            d[ck.y, testosterone_ng.dl] <- d[ck.y, testosterone_ng.dl] * 100
        }
        if (ck0) {
            shbg <- d[, sex_hormone_binding_globulin_nmol.l]
            testosterone <- d[, testosterone_ng.dl]
            (h <- shbg * 10^-9)
            (t <- testosterone/288.39999999999998 * 10 * 10^-9)
            a <- 23.43 * 10^9
            (b <- (h - t) * 10^9 + 23.43)
            (c <- -t)
            (s <- (-b + sqrt(b^2 - 4 * a * c))/(2 * a))
            (ft <- s/(10^-9) * 10 * 288.39999999999998/100)
            (BioT <- 23.43 * ft)
            if (isTRUE(free_testosterone_ng.dl)) 
                d$free_testosterone_ng.dl <- ft
            if (is.character(free_testosterone_ng.dl)) {
                d$nnnxxxxx <- ft
                colnames(d)[ncol(d)] <- free_testosterone_ng.dl
            }
            if (isTRUE(bioavailable_testosterone_ng.dl)) 
                d$bioavailable_testosterone_ng.dl <- BioT
            if (is.character(bioavailable_testosterone_ng.dl)) {
                d$nnnxxxxx <- BioT
                colnames(d)[ncol(d)] <- bioavailable_testosterone_ng.dl
            }
            if (drop_shbg) 
                d <- drop_col(d, "sex_hormone_binding_globulin_nmol.l")
            if (drop_testo) 
                d <- drop_col(d, "testosterone_ng.dl")
        }
    }
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_mango` [exported]

```r
function (data, years, day = 1, fun = c("mean", "alone", "sum"), both2days = TRUE, food.code = NULL, 
    Year = FALSE, join = "left") 
{
    if (length(day) == 1) {
        d <- nhs.iff.food.code(years = years, day = day, food.code = fndds.db.food("mango", start = 6, 
            years = years, food.code = food.code, cat = F))
        col_rename(d) <- c("grms:mango.grms", "kcal:mango.kcal")
        attr.fd <- attr(d, "food.code")
    }
    else {
        d1 <- nhs.iff.food.code(years = years, day = 1, food.code = fndds.db.food("mango", start = 6, 
            years = years, food.code = food.code, cat = F))
        attr.fd <- attr(d1, "food.code")
        d2 <- nhs.iff.food.code(years = years, day = 2, food.code = fndds.db.food("mango", start = 6, 
            years = years, food.code = food.code, cat = F))
        head(d1)
        head(d2)
        d <- dplyr::left_join(d1, d2, c("seqn", "Year"), suffix = c(".d1", ".d2"))
        head(d)
        (commen <- unique(do::knife_right(set::grep_or(colnames(d), c(".d1", ".d2")), 3)))
        fun = fun[1]
        if (fun %in% c("sum", "mean")) {
            for (i in commen) {
                c12 <- paste0(i, c(".d1", ".d2"))
                cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                d$xx <- cal
                ck <- d$Year %in% c("1999-2000", "2001-2002")
                d$xx[ck] <- row.means(d[ck, c12])
                colnames(d)[ncol(d)] <- i
                d <- drop_col(d, c12)
            }
        }
    }
    df <- return_data(data, d, Year, key = "seqn", join = join)
    attr(df, "food.code") <- attr.fd
    df
}
```

## `db_mort` [exported]

```r
function (data, years, varLabel = TRUE, codebook = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- do.call(lapply(years, function(i) mort_read(years = i, varLabel = varLabel, codebook = codebook)), 
        what = plyr::rbind.fill)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_muscle.strength` [exported]

```r
function (data, years, grip_test_status = TRUE, ever_had_surgery_on_hands_or_wrists = TRUE, recent_pain_aching_stiffness_right_hand = TRUE, 
    recent_pain_aching_stiffness_left_hand = TRUE, dominant_hand = FALSE, index_finger_90_degree = FALSE, 
    testing_position = FALSE, hassigned_for_practice_trial = FALSE, begin_test_hand = FALSE, gs_t1_h1.kg = FALSE, 
    gs_t1_h1_effort = FALSE, gs_t1_h2.kg = FALSE, gs_t1_h2_effort = FALSE, gs_t2_h1.kg = FALSE, gs_t2_h1_effort = FALSE, 
    gs_t2_h2.kg = FALSE, gs_t2_h2_effort = FALSE, gs_t3_h1.kg = FALSE, gs_t3_h1_effort = FALSE, gs_t3_h2.kg = FALSE, 
    gs_t3_h2_effort = FALSE, combined_grip_strength_kg = FALSE, Year = FALSE, join = "left") 
{
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        grip_test_status, "mgdexsts"), ever_had_surgery_on_hands_or_wrists, "mgd050"), recent_pain_aching_stiffness_right_hand, 
        "mgq070"), recent_pain_aching_stiffness_left_hand, "mgq100"), dominant_hand, "mgd130"), index_finger_90_degree, 
        "mgq90dg"), testing_position, "mgdseat"), hassigned_for_practice_trial, "mgaphand"), begin_test_hand, 
        "mgathand"), gs_t1_h1.kg, "mgxh1t1"), gs_t1_h1_effort, "mgxh1t1e"), gs_t1_h2.kg, "mgxh2t1"), 
        gs_t1_h2_effort, "mgxh2t1e"), gs_t2_h1.kg, "mgxh1t2"), gs_t2_h1_effort, "mgxh1t2e"), gs_t2_h2.kg, 
        "mgxh2t2"), gs_t2_h2_effort, "mgxh2t2e"), gs_t3_h1.kg, "mgxh1t3"), gs_t3_h1_effort, "mgxh1t3e"), 
        gs_t3_h2.kg, "mgxh2t3"), gs_t3_h2_effort, "mgxh2t3e"), combined_grip_strength_kg, "mgdcgsz")
    years <- data_years(data, years)
    tsv <- nhs_tsv("mgx", years = years, cat = F)
    tsv0(tsv)
    d <- nhs_read(tsv, var2, lower_cd = TRUE, cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_nova` [exported]

```r
function (data = NULL, all = FALSE, day = 1, years, unprocessed_minimal.grams, ingredients.grams, processed.grams, 
    ultra_processed.grams, unprocessed_minimal.kcal, ingredients.kcal, processed.kcal, ultra_processed.kcal, 
    Year = F, join = "left") 
{
    ck <- all(miss(ingredients.grams), miss(processed.grams), miss(ultra_processed.grams), miss(unprocessed_minimal.grams), 
        miss(ingredients.kcal), miss(processed.kcal), miss(ultra_processed.kcal), miss(unprocessed_minimal.kcal))
    if (all) {
        if (ck) {
            ingredients.grams <- TRUE
            processed.grams <- TRUE
            ultra_processed.grams <- TRUE
            unprocessed_minimal.grams <- TRUE
            ingredients.kcal <- TRUE
            processed.kcal <- TRUE
            ultra_processed.kcal <- TRUE
            unprocessed_minimal.kcal <- TRUE
        }
        else {
            if (miss(ingredients.grams)) 
                ingredients.grams <- TRUE
            if (miss(processed.grams)) 
                processed.grams <- TRUE
            if (miss(ultra_processed.grams)) 
                ultra_processed.grams <- TRUE
            if (miss(unprocessed_minimal.grams)) 
                unprocessed_minimal.grams <- TRUE
            if (miss(ingredients.kcal)) 
                ingredients.kcal <- TRUE
            if (miss(processed.kcal)) 
                processed.kcal <- TRUE
            if (miss(ultra_processed.kcal)) 
                ultra_processed.kcal <- TRUE
            if (miss(unprocessed_minimal.kcal)) 
                unprocessed_minimal.kcal <- TRUE
        }
    }
    else {
        if (ck) {
            return()
        }
        else {
            if (miss(ingredients.grams)) 
                ingredients.grams <- FALSE
            if (miss(processed.grams)) 
                processed.grams <- FALSE
            if (miss(ultra_processed.grams)) 
                ultra_processed.grams <- FALSE
            if (miss(unprocessed_minimal.grams)) 
                unprocessed_minimal.grams <- FALSE
            if (miss(ingredients.kcal)) 
                ingredients.kcal <- FALSE
            if (miss(processed.kcal)) 
                processed.kcal <- FALSE
            if (miss(ultra_processed.kcal)) 
                ultra_processed.kcal <- FALSE
            if (miss(unprocessed_minimal.kcal)) 
                unprocessed_minimal.kcal <- FALSE
        }
    }
    if (isTRUE(ingredients.grams)) 
        ingredients.grams = "ingredients.grams"
    if (isTRUE(processed.grams)) 
        processed.grams = "processed.grams"
    if (isTRUE(ultra_processed.grams)) 
        ultra_processed.grams = "ultra_processed.grams"
    if (isTRUE(unprocessed_minimal.grams)) 
        unprocessed_minimal.grams = "unprocessed_minimal.grams"
    if (isTRUE(ingredients.kcal)) 
        ingredients.kcal = "ingredients.kcal"
    if (isTRUE(processed.kcal)) 
        processed.kcal = "processed.kcal"
    if (isTRUE(ultra_processed.kcal)) 
        ultra_processed.kcal = "ultra_processed.kcal"
    if (isTRUE(unprocessed_minimal.kcal)) 
        unprocessed_minimal.kcal = "unprocessed_minimal.kcal"
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        "Year", "Year"), "seqn", "seqn"), ingredients.grams, "ingredients.grams"), processed.grams, "processed.grams"), 
        ultra_processed.grams, "ultra_processed.grams"), unprocessed_minimal.grams, "unprocessed_minimal.grams"), 
        ingredients.kcal, "ingredients.kcal"), processed.kcal, "processed.kcal"), ultra_processed.kcal, 
        "ultra_processed.kcal"), unprocessed_minimal.kcal, "unprocessed_minimal.kcal")
    years <- data_years(data, years)
    nova <- openxlsx::read.xlsx(paste0(get_config_path(), "/attach/NOVAclass.xlsx"))
    d <- db_driff(day = day, years = years, energy_kcal = "kcal", grams = T, Year = T, fun = "mean", 
        NA20 = T) %>% db_dr.fdcd()
    d$food <- stringr::str_to_lower(d$label)
    di <- left_join(d, nova, "food")
    d <- group_sum(di, vars = c("grams", "kcal"), bys = c("Year", "seqn", "class"))
    d$class <- Recode(d$class, "<U+6700><U+5C11><U+52A0><U+5DE5><U+98DF><U+7269>::unprocessed_minimal", 
        "<U+70F9><U+996A><U+914D><U+6599>::ingredients", "<U+52A0><U+5DE5><U+98DF><U+7269>::processed", 
        "<U+8D85><U+52A0><U+5DE5><U+98DF><U+7269>::ultra_processed", to.numeric = FALSE)
    d1 <- reshape2::dcast(d, Year + seqn ~ class, value.var = "grams")
    d2 <- reshape2::dcast(d, Year + seqn ~ class, value.var = "kcal")
    colnames(d1)[-c(1, 2)] <- paste0(colnames(d1)[-c(1, 2)], ".grams")
    colnames(d2)[-c(1, 2)] <- paste0(colnames(d2)[-c(1, 2)], ".kcal")
    d <- full_join(d1, d2, c("Year", "seqn"))
    di <- d[d$seqn == 44183, c("Year", "seqn", "ingredients.kcal", "processed.kcal", "ultra_processed.kcal", 
        "unprocessed_minimal.kcal")]
    di <- db_drtot(di, years = 2007, energy_kcal = T, day = day)
    d <- d[, do::Replace0(var2, ":.*"), drop = F]
    d <- col_rename(d, var2)
    return_data(data, d, Year, key = "seqn", join)
}
```

## `db_ogtt` [exported]

```r
function (data, years, ogtt_subsample_2_year_mec_weight = FALSE, two_hour_glucose_ogtt_mg.dl = FALSE, 
    two_hour_glucose_ogtt_mmol.l = FALSE, total_length_of_food_fast_hours = FALSE, total_length_of_food_fast_minutes = FALSE, 
    glucose_challenge_administer_time_in_min = FALSE, time_from_fast_glucose_challenge_min = FALSE, time_from_fasting_glucose_ogtt_min = FALSE, 
    time_from_glucose_challenge_ogtt_min = FALSE, amount_of_glucose_challenge_drank = FALSE, incomplete_ogtt_comment_code = FALSE, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        ogtt_subsample_2_year_mec_weight, "wtsog2yr"), two_hour_glucose_ogtt_mg.dl, "lbxglt"), two_hour_glucose_ogtt_mmol.l, 
        "lbdgltsi"), total_length_of_food_fast_hours, "phafsthr"), total_length_of_food_fast_minutes, 
        "phafstmn"), glucose_challenge_administer_time_in_min, "gtdscmmn"), time_from_fast_glucose_challenge_min, 
        "gtddr1mn"), time_from_fasting_glucose_ogtt_min, "gtdbl2mn"), time_from_glucose_challenge_ogtt_min, 
        "gtddr2mn"), amount_of_glucose_challenge_drank, "gtxdrank"), incomplete_ogtt_comment_code, "gtdcode")
    (tsv <- nhs_tsv("ogtt", years = years, cat = F))
    ck00 <- tsv0(tsv, T, data)
    if (!is.null(ck00)) {
        if (is.character(ck00)) 
            return()
        if (is.data.frame(ck00)) 
            return(ck00)
    }
    d <- nhs_read(tsv, var, cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_ohxden` [exported]

```r
function (data, years, exam_status = FALSE, dental_implant = FALSE, dental_restoration = FALSE, dental_sealant = FALSE, 
    root_cary = FALSE, other_root_lesion = FALSE, root_restoration = FALSE, other_root_restoration = FALSE, 
    dental_decay = FALSE, edentulous = FALSE, tooth_condition = FALSE, coronal_cary_tooth = FALSE, coronal_cary_surface = FALSE, 
    coronal_caries_2nd_restoration_sc = FALSE, coronal_caries_2nd_restoration_tc = FALSE, sealants = FALSE, 
    foc = FALSE, label = FALSE, Year = FALSE, join = "left") 
{
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        exam_status, "ohaexsts,ohdexsts"), dental_implant, "ohximp"), root_cary, "ohxrcar"), other_root_lesion, 
        "ohxrcar"), root_restoration, "ohxrres"), other_root_restoration, "ohxrreso"), dental_decay, 
        "ohxdecay"), dental_restoration, "ohxrest"), dental_sealant, "ohxseal"), edentulous, "ohxeden")
    if (tooth_condition) {
        if (label) {
            append(var) <- c("ohx09tc,ohd09tc,ohx09htc:ci_lt_up", "ohx24tc,ohd24tc,ohx24htc:ci_lt_lw", 
                "ohx08tc,ohd08tc,ohx08htc:ci_rt_up", "ohx25tc,ohd25tc,ohx25htc:ci_rt_lw", "ohx10tc,ohd10tc,ohx10htc:li_lt_up", 
                "ohx23tc,ohd23tc,ohx23htc:li_lt_lw", "ohx07tc,ohd07tc,ohx07htc:li_rt_up", "ohx26tc,ohd26tc,ohx26htc:li_rt_lw", 
                "ohx11tc,ohd11tc,ohx11htc:c_lt_up", "ohx22tc,ohd22tc,ohx22htc:c_lt_lw", "ohx06tc,ohd06tc,ohx06htc:c_rt_up", 
                "ohx27tc,ohd27tc,ohx27htc:c_rt_lw", "ohx12tc,ohd12tc,ohx12htc:b1_lt_up", "ohx21tc,ohd21tc,ohx21htc:b1_lt_lw", 
                "ohx05tc,ohd05tc,ohx05htc:b1_rt_up", "ohx28tc,ohd28tc,ohx28htc:b1_rt_lw", "ohx13tc,ohd13tc,ohx13htc:b2_lt_up", 
                "ohx20tc,ohd20tc,ohx20htc:b2_lt_lw", "ohx04tc,ohd04tc,ohx04htc:b2_rt_up", "ohx29tc,ohd29tc,ohx29htc:b2_rt_lw", 
                "ohx14tc,ohd14tc,ohx14htc:m1_lt_up", "ohx19tc,ohd19tc,ohx19htc:m1_lt_lw", "ohx03tc,ohd03tc,ohx03htc:m1_rt_up", 
                "ohx30tc,ohd30tc,ohx30htc:m1_rt_lw", "ohx15tc,ohd15tc,ohx15htc:m2_lt_up", "ohx18tc,ohd18tc,ohx18htc:m2_lt_lw", 
                "ohx02tc,ohd02tc,ohx02htc:m2_rt_up", "ohx31tc,ohd31tc,ohx31htc:m2_rt_lw", "ohx16tc,ohd16tc,ohx16htc:m3_lt_up", 
                "ohx17tc,ohd17tc,ohx17htc:m3_lt_lw", "ohx01tc,ohd01tc,ohx01htc:m3_rt_up", "ohx32tc,ohd32tc,ohx32htc:m3_rt_lw")
        }
        else {
            append(var) <- c("ohx09tc,ohd09tc,ohx09htc:ohx09tc", "ohx24tc,ohd24tc,ohx24htc:ohx24tc", 
                "ohx08tc,ohd08tc,ohx08htc:ohx08tc", "ohx25tc,ohd25tc,ohx25htc:ohx25tc", "ohx10tc,ohd10tc,ohx10htc:ohx10tc", 
                "ohx23tc,ohd23tc,ohx23htc:ohx23tc", "ohx07tc,ohd07tc,ohx07htc:ohx07tc", "ohx26tc,ohd26tc,ohx26htc:ohx26tc", 
                "ohx11tc,ohd11tc,ohx11htc:ohx11tc", "ohx22tc,ohd22tc,ohx22htc:ohx22tc", "ohx06tc,ohd06tc,ohx06htc:ohx06tc", 
                "ohx27tc,ohd27tc,ohx27htc:ohx27tc", "ohx12tc,ohd12tc,ohx12htc:ohx12tc", "ohx21tc,ohd21tc,ohx21htc:ohx21tc", 
                "ohx05tc,ohd05tc,ohx05htc:ohx05tc", "ohx28tc,ohd28tc,ohx28htc:ohx28tc", "ohx13tc,ohd13tc,ohx13htc:ohx13tc", 
                "ohx20tc,ohd20tc,ohx20htc:ohx20tc", "ohx04tc,ohd04tc,ohx04htc:ohx04tc", "ohx29tc,ohd29tc,ohx29htc:ohx29tc", 
                "ohx14tc,ohd14tc,ohx14htc:ohx14tc", "ohx19tc,ohd19tc,ohx19htc:ohx19tc", "ohx03tc,ohd03tc,ohx03htc:ohx03tc", 
                "ohx30tc,ohd30tc,ohx30htc:ohx30tc", "ohx15tc,ohd15tc,ohx15htc:ohx15tc", "ohx18tc,ohd18tc,ohx18htc:ohx18tc", 
                "ohx02tc,ohd02tc,ohx02htc:ohx02tc", "ohx31tc,ohd31tc,ohx31htc:ohx31tc", "ohx16tc,ohd16tc,ohx16htc:ohx16tc", 
                "ohx17tc,ohd17tc,ohx17htc:ohx17tc", "ohx01tc,ohd01tc,ohx01htc:ohx01tc", "ohx32tc,ohd32tc,ohx32htc:ohx32tc")
        }
    }
    if (coronal_cary_tooth) {
        if (label) {
            append(var) <- c("ohx09ctc,ohd09ctc:cor.cary.tc_ci_lt_up", "ohx24ctc,ohd24ctc:cor.cary.tc_ci_lt_lw", 
                "ohd08ctc,ohx08ctc:cor.cary.tc_ci_rt_up", "ohx25ctc,ohd25ctc:cor.cary.tc_ci_rt_lw", "ohx10ctc,ohd10ctc:cor.cary.tc_li_lt_up", 
                "ohx23ctc,ohd23ctc:cor.cary.tc_li_lt_lw", "ohd07ctc,ohx07ctc:cor.cary.tc_li_rt_up", "ohx26ctc,ohd26ctc:cor.cary.tc_li_rt_lw", 
                "ohx11ctc,ohd11ctc:cor.cary.tc_c_lt_up", "ohx22ctc,ohd22ctc:cor.cary.tc_c_lt_lw", "ohx06ctc,ohd06ctc:cor.cary.tc_c_rt_up", 
                "ohx27ctc,ohd27ctc:cor.cary.tc_c_rt_lw", "ohx12ctc,ohd12ctc:cor.cary.tc_b1_lt_up", "ohx21ctc,ohd21ctc:cor.cary.tc_b1_lt_lw", 
                "ohx05ctc,ohd05ctc:cor.cary.tc_b1_rt_up", "ohx28ctc,ohd28ctc:cor.cary.tc_b1_rt_lw", "ohx13ctc,ohd13ctc:cor.cary.tc_b2_lt_up", 
                "ohx20ctc,ohd20ctc:cor.cary.tc_b2_lt_lw", "ohx04ctc,ohd04ctc:cor.cary.tc_b2_rt_up", "ohx29ctc,ohd29ctc:cor.cary.tc_b2_rt_lw", 
                "ohx14ctc,ohd14ctc:cor.cary.tc_m1_lt_up", "ohx19ctc,ohd19ctc:cor.cary.tc_m1_lt_lw", "ohx03ctc,ohd03ctc:cor.cary.tc_m1_rt_up", 
                "ohx30ctc,ohd30ctc:cor.cary.tc_m1_rt_lw", "ohx15ctc,ohd15ctc:cor.cary.tc_m2_lt_up", "ohx18ctc,ohd18ctc:cor.cary.tc_m2_lt_lw", 
                "ohx02ctc,ohd02ctc:cor.cary.tc_m2_rt_up", "ohx31ctc,ohd31ctc:cor.cary.tc_m2_rt_lw")
        }
        else {
            append(var) <- c("ohx09ctc,ohd09ctc:ohx09ctc", "ohx24ctc,ohd24ctc:ohx24ctc", "ohd08ctc,ohx08ctc:ohd08ctc", 
                "ohx25ctc,ohd25ctc:ohx25ctc", "ohx10ctc,ohd10ctc:ohx10ctc", "ohx23ctc,ohd23ctc:ohx23ctc", 
                "ohd07ctc,ohx07ctc:ohd07ctc", "ohx26ctc,ohd26ctc:ohx26ctc", "ohx11ctc,ohd11ctc:ohx11ctc", 
                "ohx22ctc,ohd22ctc:ohx22ctc", "ohx06ctc,ohd06ctc:ohx06ctc", "ohx27ctc,ohd27ctc:ohx27ctc", 
                "ohx12ctc,ohd12ctc:ohx12ctc", "ohx21ctc,ohd21ctc:ohx21ctc", "ohx05ctc,ohd05ctc:ohx05ctc", 
                "ohx28ctc,ohd28ctc:ohx28ctc", "ohx13ctc,ohd13ctc:ohx13ctc", "ohx20ctc,ohd20ctc:ohx20ctc", 
                "ohx04ctc,ohd04ctc:ohx04ctc", "ohx29ctc,ohd29ctc:ohx29ctc", "ohx14ctc,ohd14ctc:ohx14ctc", 
                "ohx19ctc,ohd19ctc:ohx19ctc", "ohx03ctc,ohd03ctc:ohx03ctc", "ohx30ctc,ohd30ctc:ohx30ctc", 
                "ohx15ctc,ohd15ctc:ohx15ctc", "ohx18ctc,ohd18ctc:ohx18ctc", "ohx02ctc,ohd02ctc:ohx02ctc", 
                "ohx31ctc,ohd31ctc:ohx31ctc")
        }
    }
    if (coronal_cary_surface) {
        if (label) {
            append(var) <- c("ohx09csc,ohd09csc:cor.cary.sc_ci_lt_up", "ohx24csc,ohd24csc:cor.cary.sc_ci_lt_lw", 
                "ohx08csc,ohd08csc:cor.cary.sc_ci_rt_up", "ohx25csc,ohd25csc:cor.cary.sc_ci_rt_lw", "ohx10csc,ohd10csc:cor.cary.sc_li_lt_up", 
                "ohx23csc,ohd23csc:cor.cary.sc_li_lt_lw", "ohx07csc,ohd07csc:cor.cary.sc_li_rt_up", "ohx26csc,ohd26csc:cor.cary.sc_li_rt_lw", 
                "ohx11csc,ohd11csc:cor.cary.sc_c_lt_up", "ohx22csc,ohd22csc:cor.cary.sc_c_lt_lw", "ohx06csc,ohd06csc:cor.cary.sc_c_rt_up", 
                "ohx27csc,ohd27csc:cor.cary.sc_c_rt_lw", "ohx12csc,ohd12csc:cor.cary.sc_b1_lt_up", "ohx21csc,ohd21csc:cor.cary.sc_b1_lt_lw", 
                "ohx05csc,ohd05csc:cor.cary.sc_b1_rt_up", "ohx28csc,ohd28csc:cor.cary.sc_b1_rt_lw", "ohx13csc,ohd13csc:cor.cary.sc_b2_lt_up", 
                "ohx20csc,ohd20csc:cor.cary.sc_b2_lt_lw", "ohx04csc,ohd04csc:cor.cary.sc_b2_rt_up", "ohx29csc,ohd29csc:cor.cary.sc_b2_rt_lw", 
                "ohx14csc,ohd14csc:cor.cary.sc_m1_lt_up", "ohx19csc,ohd19csc:cor.cary.sc_m1_lt_lw", "ohx03csc,ohd03csc:cor.cary.sc_m1_rt_up", 
                "ohx30csc,ohd30csc:cor.cary.sc_m1_rt_lw", "ohx15csc,ohd15csc:cor.cary.sc_m2_lt_up", "ohx18csc,ohd18csc:cor.cary.sc_m2_lt_lw", 
                "ohx02csc,ohd02csc:cor.cary.sc_m2_rt_up", "ohx31csc,ohd31csc:cor.cary.sc_m2_rt_lw")
        }
        else {
            append(var) <- c("ohx09csc,ohd09csc:ohx09csc", "ohx24csc,ohd24csc:ohx24csc", "ohx08csc,ohd08csc:ohx08csc", 
                "ohx25csc,ohd25csc:ohx25csc", "ohx10csc,ohd10csc:ohx10csc", "ohx23csc,ohd23csc:ohx23csc", 
                "ohx07csc,ohd07csc:ohx07csc", "ohx26csc,ohd26csc:ohx26csc", "ohx11csc,ohd11csc:ohx11csc", 
                "ohx22csc,ohd22csc:ohx22csc", "ohx06csc,ohd06csc:ohx06csc", "ohx27csc,ohd27csc:ohx27csc", 
                "ohx12csc,ohd12csc:ohx12csc", "ohx21csc,ohd21csc:ohx21csc", "ohx05csc,ohd05csc:ohx05csc", 
                "ohx28csc,ohd28csc:ohx28csc", "ohx13csc,ohd13csc:ohx13csc", "ohx20csc,ohd20csc:ohx20csc", 
                "ohx04csc,ohd04csc:ohx04csc", "ohx29csc,ohd29csc:ohx29csc", "ohx14csc,ohd14csc:ohx14csc", 
                "ohx19csc,ohd19csc:ohx19csc", "ohx03csc,ohd03csc:ohx03csc", "ohx30csc,ohd30csc:ohx30csc", 
                "ohx15csc,ohd15csc:ohx15csc", "ohx18csc,ohd18csc:ohx18csc", "ohx02csc,ohd02csc:ohx02csc", 
                "ohx31csc,ohd31csc:ohx31csc")
        }
    }
    if (coronal_caries_2nd_restoration_sc) {
        if (label) {
            append(var) <- c("ohx09rsc:re2nd_sc_ci_lt_up", "ohx24rsc:re2nd_sc_ci_lt_lw", "ohx08rsc:re2nd_sc_ci_rt_up", 
                "ohx25rsc:re2nd_sc_ci_rt_lw", "ohx10rsc:re2nd_sc_li_lt_up", "ohx23rsc:re2nd_sc_li_lt_lw", 
                "ohx07rsc:re2nd_sc_li_rt_up", "ohx26rsc:re2nd_sc_li_rt_lw", "ohx11rsc:re2nd_sc_c_lt_up", 
                "ohx22rsc:re2nd_sc_c_lt_lw", "ohx06rsc:re2nd_sc_c_rt_up", "ohx27rsc:re2nd_sc_c_rt_lw", 
                "ohx12rsc:re2nd_sc_b1_lt_up", "ohx21rsc:re2nd_sc_b1_lt_lw", "ohx05rsc:re2nd_sc_b1_rt_up", 
                "ohx28rsc:re2nd_sc_b1_rt_lw", "ohx13rsc:re2nd_sc_b2_lt_up", "ohx20rsc:re2nd_sc_b2_lt_lw", 
                "ohx04rsc:re2nd_sc_b2_rt_up", "ohx29rsc:re2nd_sc_b2_rt_lw", "ohx14rsc:re2nd_sc_m1_lt_up", 
                "ohx19rsc:re2nd_sc_m1_lt_lw", "ohx03rsc:re2nd_sc_m1_rt_up", "ohx30rsc:re2nd_sc_m1_rt_lw", 
                "ohx15rsc:re2nd_sc_m2_lt_up", "ohx18rsc:re2nd_sc_m2_lt_lw", "ohx02rsc:re2nd_sc_m2_rt_up", 
                "ohx31rsc:re2nd_sc_m2_rt_lw")
        }
        else {
            append(var) <- c("ohx09rsc", "ohx24rsc", "ohx08rsc", "ohx25rsc", "ohx10rsc", "ohx23rsc", 
                "ohx07rsc", "ohx26rsc", "ohx11rsc", "ohx22rsc", "ohx06rsc", "ohx27rsc", "ohx12rsc", "ohx21rsc", 
                "ohx05rsc", "ohx28rsc", "ohx13rsc", "ohx20rsc", "ohx04rsc", "ohx29rsc", "ohx14rsc", "ohx19rsc", 
                "ohx03rsc", "ohx30rsc", "ohx15rsc", "ohx18rsc", "ohx02rsc", "ohx31rsc")
        }
    }
    if (coronal_caries_2nd_restoration_tc) {
        if (label) {
            append(var) <- c("ohx09rtc:re2nd_tc_ci_lt_up", "ohx24rtc:re2nd_tc_ci_lt_lw", "ohx08rtc:re2nd_tc_ci_rt_up", 
                "ohx25rtc:re2nd_tc_ci_rt_lw", "ohx10rtc:re2nd_tc_li_lt_up", "ohx23rtc:re2nd_tc_li_lt_lw", 
                "ohx07rtc:re2nd_tc_li_rt_up", "ohx26rtc:re2nd_tc_li_rt_lw", "ohx11rtc:re2nd_tc_c_lt_up", 
                "ohx22rtc:re2nd_tc_c_lt_lw", "ohx06rtc:re2nd_tc_c_rt_up", "ohx27rtc:re2nd_tc_c_rt_lw", 
                "ohx12rtc:re2nd_tc_b1_lt_up", "ohx21rtc:re2nd_tc_b1_lt_lw", "ohx05rtc:re2nd_tc_b1_rt_up", 
                "ohx28rtc:re2nd_tc_b1_rt_lw", "ohx13rtc:re2nd_tc_b2_lt_up", "ohx20rtc:re2nd_tc_b2_lt_lw", 
                "ohx04rtc:re2nd_tc_b2_rt_up", "ohx29rtc:re2nd_tc_b2_rt_lw", "ohx14rtc:re2nd_tc_m1_lt_up", 
                "ohx19rtc:re2nd_tc_m1_lt_lw", "ohx03rtc:re2nd_tc_m1_rt_up", "ohx30rtc:re2nd_tc_m1_rt_lw", 
                "ohx15rtc:re2nd_tc_m2_lt_up", "ohx18rtc:re2nd_tc_m2_lt_lw", "ohx02rtc:re2nd_tc_m2_rt_up", 
                "ohx31rtc:re2nd_tc_m2_rt_lw")
        }
        else {
            append(var) <- c("ohx09rtc", "ohx24rtc", "ohx08rtc", "ohx25rtc", "ohx10rtc", "ohx23rtc", 
                "ohx07rtc", "ohx26rtc", "ohx11rtc", "ohx22rtc", "ohx06rtc", "ohx27rtc", "ohx12rtc", "ohx21rtc", 
                "ohx05rtc", "ohx28rtc", "ohx13rtc", "ohx20rtc", "ohx04rtc", "ohx29rtc", "ohx14rtc", "ohx19rtc", 
                "ohx03rtc", "ohx30rtc", "ohx15rtc", "ohx18rtc", "ohx02rtc", "ohx31rtc")
        }
    }
    if (sealants) {
        if (label) {
            append(var) <- c("ohx10se,ohx10se:sealants_li_lt_up", "ohx07se,ohx07se:sealants_li_rt_up", 
                "ohx12se,ohx12se:sealants_b1_lt_up", "ohx21se,ohx21se:sealants_b1_lt_lw", "ohx05se,ohx05se:sealants_b1_rt_up", 
                "ohx28se,ohx28se:sealants_b1_rt_lw", "ohx13se,ohx13se:sealants_b2_lt_up", "ohx20se,ohx20se:sealants_b2_lt_lw", 
                "ohx04se,ohx04se:sealants_b2_rt_up", "ohx29se,ohx29se:sealants_b2_rt_lw", "ohx14se,ohx14se:sealants_m1_lt_up", 
                "ohx19se,ohx19se:sealants_m1_lt_lw", "ohx03se,ohx03se:sealants_m1_rt_up", "ohx30se,ohx30se:sealants_m1_rt_lw", 
                "ohx15se,ohx15se:sealants_m2_lt_up", "ohx18se,ohx18se:sealants_m2_lt_lw", "ohx02se,ohx02se:sealants_m2_rt_up", 
                "ohx31se,ohx31se:sealants_m2_rt_lw")
        }
        else {
            append(var) <- c("ohx10se", "ohx07se", "ohx12se", "ohx21se", "ohx05se", "ohx28se", "ohx13se", 
                "ohx20se", "ohx04se", "ohx29se", "ohx14se", "ohx19se", "ohx03se", "ohx30se", "ohx15se", 
                "ohx18se", "ohx02se", "ohx31se")
        }
    }
    if (foc) {
        append(var) <- c("ohxfcant", "ohxfclz1", "ohxfclz2", "ohxfclz3", "ohxfclz4", "ohxfclz5", "ohxfclz6", 
            "ohxfclz7", "ohxfclz8", "ohxfcrz1", "ohxfcrz2", "ohxfcrz3", "ohxfcrz4", "ohxfcrz5", "ohxfcrz6", 
            "ohxfcrz7", "ohxfcrz8")
    }
    var2 <- var
    var <- var2
    years <- data_years(data, years)
    tsv <- nhs_tsv("ohx_|ohxden", years = years, cat = F)
    d <- nhs_read(tsv, var, lower_cd = TRUE, cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_paxraw` [internal]

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    allnms <- ls(envir = .GlobalEnv, all.names = T)
    NHANESpaxraw <<- NULL
    if (!"NHANESpaxraw" %in% allnms & "2003-2004" %in% years) {
        tsv <- nhs_tsv("paxraw", cat = F, years = 2003)
        NHANESpaxraw <- data.table::fread(tsv, showProgress = F, data.table = F)
        cd <- nhs_codebook(tsv)
        for (i in unique(cd$variable)) {
            (ck <- cd$variable %in% i)
            (code <- cd$code[ck])
            (label <- cd$label[ck])
            for (j in 1:length(code)) {
                NHANESpaxraw[NHANESpaxraw[, i] %in% code[j], i] <- label[j]
            }
        }
        NHANESpaxraw <- cbind(Year = 2003, NHANESpaxraw)
    }
    if (!"NHANESpaxraw2005" %in% allnms & "2005-2006" %in% years) {
        tsv <- nhs_tsv("paxraw", cat = F, years = 2005)
        NHANESpaxraw2005 <- data.table::fread(tsv, showProgress = F, data.table = F)
        cd <- nhs_codebook(tsv)
        for (i in unique(cd$variable)) {
            (ck <- cd$variable %in% i)
            (code <- cd$code[ck])
            (label <- cd$label[ck])
            for (j in 1:length(code)) {
                NHANESpaxraw2005[NHANESpaxraw2005[, i] %in% code[j], i] <- label[j]
            }
        }
        NHANESpaxraw <- plyr::rbind.fill(NHANESpaxraw, cbind(Year = 2005, NHANESpaxraw2005))
        NHANESpaxraw2005 <- NULL
    }
    gc()
    return_data(data, NHANESpaxraw, Year, key = "seqn", join = join)
}
```

## `db_pooltf` [internal]

```r
function (data, years, Year = FALSE) 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("pooltf", years = years, cat = FALSE)
    d <- data.table::fread(tsv, data.table = F)
    d <- d[d$sampleid %in% data$sampleid, ]
    data <- dplyr::left_join(data, d, "sampleid")
    data$Year <- NULL
    data
}
```

## `db_sandwiches` [exported]

```r
function (data, years, day = 1, fun = "mean", both2days = TRUE, unit = "gram", Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- db_driff(day = day, fun = fun, both2days = both2days, years = years, Year = TRUE, combination_food_type = TRUE, 
        grams = "sandwiches.gram", energy_kcal = "sandwiches.kcal")
    ck <- lookl(d$combination_food_type, "sandwich")
    d$sandwiches.gram[!ck & !is.na(d$sandwiches.gram)] <- 0
    d$sandwiches.kcal[!ck & !is.na(d$sandwiches.kcal)] <- 0
    d <- d[, c("seqn", "Year", "sandwiches.gram", "sandwiches.kcal")]
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    d <- aggregate2(d, c("sandwiches.gram", "sandwiches.kcal"), c("Year", "seqn"), ".sum.nona")
    var2 <- c("Year", "seqn")
    if ("gram" %in% unit) 
        append(var2) <- "sandwiches.gram"
    if ("kcal" %in% unit) 
        append(var2) <- "sandwiches.kcal"
    d <- d[, var2]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_slq` [exported]

```r
function (data, years, how_long_to_fall_asleep_minutes = FALSE, how_much_sleep_do_you_get_hours = FALSE, 
    ever_told_doctor_had_trouble_sleeping = FALSE, ever_told_by_doctor_have_sleep_disorder = FALSE, sleep_disorder_sleep_apnea = FALSE, 
    sleep_disorder_insomnia = FALSE, sleep_disorder_restless_legs = FALSE, sleep_disorder_other = FALSE, 
    how_often_do_you_snore = FALSE, how_often_do_you_snort_or_stop_breathing = FALSE, how_often_have_trouble_falling_asleep = FALSE, 
    how_often_wake_up_during_night = FALSE, how_often_wake_up_too_early_in_morning = FALSE, how_often_feel_unrested_during_the_day = FALSE, 
    how_often_feel_overly_sleepy_during_day = FALSE, how_often_did_you_not_get_enough_sleep = FALSE, 
    how_often_take_pills_to_help_you_sleep = FALSE, how_often_have_leg_jerks_while_sleeping = FALSE, 
    how_often_have_legs_cramp_while_sleeping = FALSE, difficulty_concentrating_when_tired = FALSE, difficulty_remembering_when_tired = FALSE, 
    difficulty_eating_when_tired = FALSE, difficulty_with_a_hobby_when_tired = FALSE, difficulty_getting_things_done = FALSE, 
    difficulty_with_finance_when_tired = FALSE, difficulty_at_work_because_tired = FALSE, difficulty_on_phone_when_tired = FALSE, 
    usual_sleep_time_on_weekdays_or_workdays = FALSE, usual_wake_time_on_weekdays_or_workdays = FALSE, 
    sleep_hours_weekdays_or_workdays = FALSE, usual_sleep_time_on_weekends = FALSE, usual_wake_time_on_weekends = FALSE, 
    sleep_hours_weekends = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    var2 <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        how_long_to_fall_asleep_minutes, "sld020m"), how_much_sleep_do_you_get_hours, "sld010h"), ever_told_doctor_had_trouble_sleeping, 
        "slq050"), ever_told_by_doctor_have_sleep_disorder, "slq060"), sleep_disorder_sleep_apnea, "slq070a"), 
        sleep_disorder_insomnia, "slq070b"), sleep_disorder_restless_legs, "slq070c"), sleep_disorder_other, 
        "slq070d"), how_often_do_you_snore, "slq030"), how_often_do_you_snort_or_stop_breathing, "slq040"), 
        how_often_have_trouble_falling_asleep, "slq080"), how_often_wake_up_during_night, "slq090"), 
        how_often_wake_up_too_early_in_morning, "slq100"), how_often_feel_unrested_during_the_day, "slq110"), 
        how_often_feel_overly_sleepy_during_day, "slq120"), how_often_did_you_not_get_enough_sleep, "slq130"), 
        how_often_take_pills_to_help_you_sleep, "slq140"), how_often_have_leg_jerks_while_sleeping, "slq150"), 
        how_often_have_legs_cramp_while_sleeping, "slq160"), difficulty_concentrating_when_tired, "slq170"), 
        difficulty_remembering_when_tired, "slq180"), difficulty_eating_when_tired, "slq190"), difficulty_with_a_hobby_when_tired, 
        "slq200"), difficulty_getting_things_done, "slq210"), difficulty_with_finance_when_tired, "slq220"), 
        difficulty_at_work_because_tired, "slq230"), difficulty_on_phone_when_tired, "slq240"), usual_sleep_time_on_weekdays_or_workdays, 
        "slq300"), usual_wake_time_on_weekdays_or_workdays, "slq310"), sleep_hours_weekdays_or_workdays, 
        "sld012"), usual_sleep_time_on_weekends, "slq320"), usual_wake_time_on_weekends, "slq330"), sleep_hours_weekends, 
        "sld013")
    if (isTRUE(usual_wake_time_on_weekdays_or_workdays)) 
        usual_wake_time_on_weekdays_or_workdays <- "usual_wake_time_on_weekdays_or_workdays"
    if (isTRUE(usual_wake_time_on_weekends)) 
        usual_wake_time_on_weekends <- "usual_wake_time_on_weekends"
    if (isTRUE(usual_sleep_time_on_weekdays_or_workdays)) 
        usual_sleep_time_on_weekdays_or_workdays <- "usual_sleep_time_on_weekdays_or_workdays"
    if (isTRUE(usual_sleep_time_on_weekends)) 
        usual_sleep_time_on_weekends <- "usual_sleep_time_on_weekends"
    tsv <- nhs_tsv("slq", years = years, cat = F)
    d <- nhs_read(tsv, var2, lower_cd = T, cat = F)
    if (is.character(d)) 
        return()
    if (is.character(usual_wake_time_on_weekdays_or_workdays) & usual_wake_time_on_weekdays_or_workdays %in% 
        colnames(d)) 
        d[, usual_wake_time_on_weekdays_or_workdays] <- lubridate::hm(d[, usual_wake_time_on_weekdays_or_workdays], 
            quiet = T)
    if (is.character(usual_wake_time_on_weekends) & usual_wake_time_on_weekends %in% colnames(d)) 
        d[, usual_wake_time_on_weekends] <- lubridate::hm(d[, usual_wake_time_on_weekends], quiet = T)
    if (is.character(usual_sleep_time_on_weekdays_or_workdays)) 
        d[, usual_sleep_time_on_weekdays_or_workdays] <- lubridate::hm(d[, usual_sleep_time_on_weekdays_or_workdays], 
            quiet = T)
    if (is.character(usual_sleep_time_on_weekends) & usual_sleep_time_on_weekends %in% colnames(d)) 
        d[, usual_sleep_time_on_weekends] <- lubridate::hm(d[, usual_sleep_time_on_weekends], quiet = T)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_sprint` [exported]

```r
function (data, years, Year = FALSE, join = "left") 
{
    version <- 1
    (file <- paste0(get_config_path(), "/attach/db_sprint~~version-", version, ".txt"))
    if (file.exists(file)) {
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    else {
        download.file("http://146.56.250.62:3838/data/nhanes-attach/db_sprint~~version-1.txt", file)
        d <- data.table::fread(file, data.table = F, showProgress = F, na.strings = c(NA_character_, 
            ""))
    }
    years <- data_years(data, years)
    d <- d[d$Year %in% years, ]
    return_data(data, d, Year, key = "seqn", join)
}
```

## `db_spx` [exported]

```r
function (data, years, test_status_first, test_comment_first, fvc_baseline_ml, extrapolated_volume_baseline_ml, 
    fev_0.5_baseline_ml, fev_0.75_baseline_ml, fev_1_baseline_ml, fev_3_baseline_ml, fev_6_baseline_ml, 
    pef_baseline_ml.s, fef_25.75_baseline_ml.s, forced_expiratory_time_baseline_s, fvc_quality_attribute_baseline, 
    fev1_quality_attribute_baseline, number_of_acceptable_curves_baseline, effort_quality_attribute_baseline, 
    selected_for_bronchodilator, spirometry_second_test_status, spirometry_second_test_comment, fvc_2nd_ml, 
    extrapolated_volume_2nd_ml, fev_0.5_2nd_ml, fev_0.75_2nd_ml, fev_1_2nd_ml, fev_3_2nd_ml, fev_6_2nd_ml, 
    pef_2nd_ml.s, fef_25.75_2nd_ml.s, forced_expiratory_time_2nd_s, fvc_quality_attribute_2nd, fev1_quality_attribute_2nd, 
    number_of_acceptable_curves_2nd, effort_quality_attribute_2nd, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("spx", "!~raw", years = years, cat = FALSE)
    if (length(tsv) == 0) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+6240><U+67E5><U+5E74><U+4EFD><U+4E2D><U+6CA1><U+6709>pbcd<U+6587><U+4EF6>"))
        if (!do::cnOS()) 
            stop("No pbcd data file in these years")
    }
    var <- variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(variable_formula(c(), 
        test_status_first, "spxnstat"), test_comment_first, "spxncmt"), fvc_baseline_ml, "spxnfvc"), 
        extrapolated_volume_baseline_ml, "spxnev"), fev_0.5_baseline_ml, "spxnfev5"), fev_0.75_baseline_ml, 
        "spxnfev7"), fev_1_baseline_ml, "spxnfev1"), fev_3_baseline_ml, "spxnfev3"), fev_6_baseline_ml, 
        "spxnfev6"), pef_baseline_ml.s, "spxnpef"), fef_25.75_baseline_ml.s, "spxnf257"), forced_expiratory_time_baseline_s, 
        "spxnfet"), fvc_quality_attribute_baseline, "spxnqfvc"), fev1_quality_attribute_baseline, "spxnqfv1"), 
        number_of_acceptable_curves_baseline, "spdnacc"), effort_quality_attribute_baseline, "spxnqeff"), 
        selected_for_bronchodilator, "spdbronc"), spirometry_second_test_status, "spxbstat"), spirometry_second_test_comment, 
        "spxbcmt"), fvc_2nd_ml, "spxbfvc"), extrapolated_volume_2nd_ml, "spxbev"), fev_0.5_2nd_ml, "spxbfev5"), 
        fev_0.75_2nd_ml, "spxbfev7"), fev_1_2nd_ml, "spxbfev1"), fev_3_2nd_ml, "spxbfev3"), fev_6_2nd_ml, 
        "spxbfev6"), pef_2nd_ml.s, "spxbpef"), fef_25.75_2nd_ml.s, "spxbf257"), forced_expiratory_time_2nd_s, 
        "spxbfet"), fvc_quality_attribute_2nd, "spxbqfvc"), fev1_quality_attribute_2nd, "spxbqfv1"), 
        number_of_acceptable_curves_2nd, "spdbacc"), effort_quality_attribute_2nd, "spxbqeff")
    if (is.null(var)) {
        if (do::cnOS()) 
            stop(tmcn::toUTF8("<U+6CA1><U+6709><U+6307><U+5B9A><U+8981><U+60F3><U+63D0><U+53D6><U+7684><U+6570><U+636E>"))
        if (!do::cnOS()) 
            stop("No data specified to extract")
    }
    d <- nhs_read(tsv, var, cat = FALSE)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_tea` [exported]

```r
function (data, years, day = 1, fun = c("mean", "alone", "sum"), unit = c("gram", "kcal", "cup"), sweeten = FALSE, 
    caffeinate = FALSE, green = FALSE, black = FALSE, oolong = FALSE, iced = FALSE, hot = FALSE, normT = FALSE, 
    leaf = FALSE, instant = FALSE, bottle = FALSE, both2days = TRUE, food.code = NULL, Year = FALSE, 
    join = "left") 
{
    unit <- match.arg(unit)
    fun <- match.arg(fun)
    years <- data_years(data, years)
    if (length(day) == 1) {
        d <- tea.1day(years = years, unit = unit, day = day, sweeten = sweeten, caffeinate = caffeinate, 
            green = green, black = black, oolong = oolong, iced = iced, hot = hot, normT = normT, leaf = leaf, 
            instant = instant, bottle = bottle)
        at <- attr(d, "food.code")
    }
    else {
        d1 <- tea.1day(years = years, unit = unit, day = 1, sweeten = sweeten, caffeinate = caffeinate, 
            green = green, black = black, oolong = oolong, iced = iced, hot = hot, normT = normT, leaf = leaf, 
            instant = instant, bottle = bottle, food.code = food.code)
        at1 <- attr(d1, "food.code")
        d2 <- tea.1day(years = years, unit = unit, day = 2, sweeten = sweeten, caffeinate = caffeinate, 
            green = green, black = black, oolong = oolong, iced = iced, hot = hot, normT = normT, leaf = leaf, 
            instant = instant, bottle = bottle, food.code = food.code)
        at2 <- attr(d2, "food.code")
        at <- unique(rbind(at1, at2))
        row.names(at) <- NULL
        head(d1)
        head(d2)
        d <- dplyr::left_join(d1, d2, c("seqn", "Year"), suffix = c(".d1", ".d2"))
        head(d)
        (commen <- unique(do::knife_right(set::grep_or(colnames(d), c("\\.d1", "\\.d2")), 3)))
        if (fun %in% c("sum", "mean")) {
            for (i in commen) {
                c12 <- paste0(i, c(".d1", ".d2"))
                cal <- eval(parse(text = sprintf("row.%ss(d[,c12],ifelse(both2days,F,T))", fun)))
                d$xx <- cal
                ck <- d$Year %in% c("1999-2000", "2001-2002")
                d$xx[ck] <- row.means(d[ck, c12])
                colnames(d)[ncol(d)] <- i
                d <- drop_col(d, c12)
            }
        }
    }
    d <- return_data(data, d, Year, key = "seqn", join = join)
    attr(d, "food.code") <- at
    d
}
```

## `db_urine.alb.cr` [exported]

```r
function (data, years, albumin_urine_mg.l = FALSE, albumin_urine_ug.ml = FALSE, creatinine_urine_mg.dl = FALSE, 
    creatinine_urine_umol.l = FALSE, uACR_mg.g = FALSE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    var2 <- variable_formula(variable_formula(c(), "albumin_urine_mg.l", "urxumasi,urxums"), "creatinine_urine_umol.l", 
        "urxucrsi,urxcrs")
    tsv <- nhs_tsv("lab16|l16|alb_cr", "!~l16_2", years = years, cat = F)
    d <- nhs_read(tsv, var2, cat = F)
    d$creatinine_urine_mg.dl <- d$creatinine_urine_umol.l/88.400000000000006
    d$albumin_urine_ug.ml <- d$albumin_urine_mg.l
    d$uACR_mg.g <- d$albumin_urine_mg.l/d$creatinine_urine_mg.dl * 100
    d <- d[, c("Year", "seqn", "albumin_urine_mg.l", "albumin_urine_ug.ml", "creatinine_urine_mg.dl", 
        "creatinine_urine_umol.l", "uACR_mg.g")]
    if (isFALSE(albumin_urine_mg.l)) 
        d <- drop_col(d, "albumin_urine_mg.l")
    if (isFALSE(albumin_urine_ug.ml)) 
        d <- drop_col(d, "albumin_urine_ug.ml")
    if (isFALSE(creatinine_urine_mg.dl)) 
        d <- drop_col(d, "creatinine_urine_mg.dl")
    if (isFALSE(creatinine_urine_umol.l)) 
        d <- drop_col(d, "creatinine_urine_umol.l")
    if (isFALSE(uACR_mg.g)) 
        d <- drop_col(d, "uACR_mg.g")
    var <- c("Year", "seqn")
    if (isTRUE(albumin_urine_mg.l)) 
        append(var) <- "albumin_urine_mg.l"
    if (isTRUE(albumin_urine_ug.ml)) 
        append(var) <- "albumin_urine_ug.ml"
    if (isTRUE(creatinine_urine_mg.dl)) 
        append(var) <- "creatinine_urine_mg.dl"
    if (isTRUE(creatinine_urine_umol.l)) 
        append(var) <- "creatinine_urine_umol.l"
    if (isTRUE(uACR_mg.g)) 
        append(var) <- "uACR_mg.g"
    if (is.character(albumin_urine_mg.l)) {
        col_rename(d) <- paste0("albumin_urine_mg.l:", albumin_urine_mg.l)
        append(var) <- albumin_urine_mg.l
    }
    if (is.character(albumin_urine_ug.ml)) {
        col_rename(d) <- paste0("albumin_urine_ug.ml:", albumin_urine_ug.ml)
        append(var) <- albumin_urine_ug.ml
    }
    if (is.character(creatinine_urine_mg.dl)) {
        col_rename(d) <- paste0("creatinine_urine_mg.dl:", creatinine_urine_mg.dl)
        append(var) <- creatinine_urine_mg.dl
    }
    if (is.character(creatinine_urine_umol.l)) {
        col_rename(d) <- paste0("creatinine_urine_umol.l:", creatinine_urine_umol.l)
        append(var) <- creatinine_urine_umol.l
    }
    if (is.character(uACR_mg.g)) {
        col_rename(d) <- paste0("uACR_mg.g:", uACR_mg.g)
        append(var) <- uACR_mg.g
    }
    d <- d[, var]
    return_data(data, d, Year, key = "seqn", join = join)
}
```


