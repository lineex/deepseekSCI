# Integrated supporting reference: nhanesr-function-reference/references/exported-function-expressions.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/exported-function-expressions.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Exported Full Function Expressions

## `%=%`

```r
function (a, b) 
{
    if (is.data.frame(a)) {
        for (i in 1:length(b)) {
            if (i == 1) {
                ck <- a == b
            }
            else {
                cki <- a == b
                ck <- ck | cki
            }
        }
    }
    else if (is.atomic(a)) {
        ck <- a %in% b
        ck[is.na(a)] <- NA
    }
    ck
}
```

## `DSD`

```r
function (data, years, prebiotic = FALSE, probiotic = FALSE, synbiotic = F, component = F, Year = F, 
    join = "left") 
{
    years <- data_years(data, years)
    dsd <- db_DSD()
    search <- do::paste0_columns(dsd[, c("supplement_name", "supplement_type", "ingredient_name", "ingredient_category", 
        "blend_component_name", "blend_component_name")])
    d0 <- db_dsids.30(years = years, Year = T)
    d <- unique(d0[, c("Year", "seqn")])
    comp <- data.frame()
    if (prebiotic) {
        comp1 <- c()
        vt <- c("glucan", "gum arabic", "inulin", "oligofruc", "oligosac", "prebiotic", "pre-biotic", 
            "resistant starch", "chicor", "psyllium", "resveratrol", "polydextrose", "wheat dextrin")
        for (i in vt) {
            seqn <- d0$seqn[d0$dsdsupid %in% dsd$dsdsupid[lookl(search, i)]]
            if (length(seqn) < 1) 
                (next)(i)
            comp1 <- c(comp1, i)
            d$i <- ifelse(d$seqn %in% seqn, 1, 0)
            colnames(d)[ncol(d)] <- i
        }
        d1 <- nhs_read(nhs_tsv("rxq_rx", cat = FALSE, years = years), "rxddrug,rxd240b:Drug", lower_cd = TRUE, 
            cat = FALSE)
        seqn <- d1$seqn[lookl(d1$Drug, "lactulose", NA2false = T)]
        if (length(seqn) > 0) {
            comp1 <- c(comp1, "lactulose")
            d$lactulose <- ifelse(d$seqn %in% seqn, 1, 0)
        }
        d$Prebiotic <- ifelse(row.sums(d[, comp1, drop = F]) > 0, "yes", "no")
        comp <- rbind(comp, data.frame(DSD = "Prebiotic", keywords = paste0(comp1, collapse = "; ")))
    }
    if (probiotic) {
        comp1 <- c()
        vt <- c("acidophilus", "animalis", "bacillus", "bacilli", "bifidobacteri", "bifidum", "boulardii", 
            "breve", "brevis", "bulgaricus", "casei", "cerevisiae", "coagulans", "delbrueckii", "enterococcus", 
            "faecalis", "faecium", "fermentum", "gasseri", "helveticus", "infantis", "lactis", "lactic acid bacteria", 
            "lactobacill", "lactococcus", "leuconostoc", "licheniformis", "longum", "mesenteric", "paracasei", 
            "pediococcus", "plantarum", "probiotic", "pro-biotic", "pro biotic", "propionibacteri", "reuteri", 
            "rhamnosus", "saccharomyc", "salivarius", "streptococcus", "subtilis", "thermophilus", "buchneri", 
            "butyricum", "caucasicus", "clausii", "clostridi", "coryniformis", "crispatus", "escherich", 
            "e. coli", "ecoli", "e coli", "florentinus", "johnsonii", "leichmannii", "mitis", "nissle", 
            "oligonitrophilus", "oralis", "rattus", "sanguis", "stearothermophilus")
        for (i in vt) {
            seqn <- d0$seqn[d0$dsdsupid %in% dsd$dsdsupid[lookl(search, i)]]
            if (length(seqn) < 1) 
                (next)(i)
            comp1 <- c(comp1, i)
            d$i <- ifelse(d$seqn %in% seqn, 1, 0)
            colnames(d)[ncol(d)] <- i
        }
        d$Probiotic <- ifelse(row.sums(d[, comp1, drop = F]) > 0, "yes", "no")
        comp <- rbind(comp, data.frame(DSD = "Probiotic", keywords = paste0(comp1, collapse = "; ")))
    }
    if (synbiotic) {
        comp1 <- c()
        vt <- c("synbiotic", "syn-biotic", "syn biotic")
        for (i in vt) {
            seqn <- d0$seqn[d0$dsdsupid %in% dsd$dsdsupid[lookl(search, i)]]
            if (length(seqn) < 1) 
                (next)(i)
            comp1 <- c(comp1, i)
            d$i <- ifelse(d$seqn %in% seqn, 1, 0)
            colnames(d)[ncol(d)] <- i
        }
        if (!is.null(comp1)) {
            d$Synbiotic <- ifelse(row.sums(d[, comp1, drop = F]) > 0, "yes", "no")
            comp <- rbind(comp, data.frame(DSD = "Synbiotic", keywords = paste0(comp1, collapse = "; ")))
        }
    }
    compt <- c()
    if (component) 
        compt <- unique(unlist(strsplit(comp$keywords, "; ")))
    d <- d[, c("Year", "seqn", c(comp$DSD, compt))]
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `DataDist`

```r
function (..., data, q.display, q.effect = c(0.25, 0.75), adjto.cat = c("mode", "first"), n.unique = 10) 
{
    old <- options()
    adjto.cat <- match.arg(adjto.cat)
    dd <- rms::datadist(..., data, q.display, q.effect, adjto.cat, n.unique = n.unique)
    old$datadist <- dd
    options(old)
}
```

## `Drug`

```r
function (..., data = NULL, years, take_drug = "take_drug", DrugNumber = FALSE, drugname = FALSE, fdaNDC = FALSE, 
    dcn = FALSE, icn = FALSE, icd10 = FALSE, yes.code = NULL, other.code = NULL, no.code = NULL, remove.other = T, 
    dup.take.drug = c("remove", "paste", "keep"), join = "left", Year = FALSE) 
{
    h0 <- c(...)
    if (do::left_equal(dup.take.drug, "paste")) 
        dup.take.drug <- "paste"
    if (do::left_equal(dup.take.drug, "remove")) 
        dup.take.drug <- "remove"
    if (do::left_equal(dup.take.drug, "keep")) 
        dup.take.drug <- "keep"
    dup.take.drug <- match.arg(dup.take.drug)
    years <- data_years(data, years)
    lss <- ls(envir = .GlobalEnv, all.names = T)
    if (!".drug_data" %in% lss) 
        build_drug_data(years)
    if (".drug_years" %in% lss) {
        (ck1 <- all(.drug_years %in% years))
        (ck2 <- all(years %in% .drug_years))
        if (ck1 & ck2) {
            "nothting"
        }
        else {
            build_drug_data(years)
        }
    }
    else {
        .drug_years <<- years
    }
    d <- .drug_data
    var <- c("Drug", "fdaNDC", "dcn", "icn", "icd10.code", "icd10.description")
    var <- set::and(var, colnames(d))
    if (!is.null(h0)) {
        ck <- lookl(d[, var], h0, ignore.case = T)
        d$take_drug[d$take_drug == "yes" & !ck] <- "other"
        if (!isFALSE(DrugNumber)) {
            dnumber <- data.frame(seqn = d$seqn, yes = d$take_drug, key = paste0(d$seqn, d$take_drug))
            dnumber.key <- data.frame(table(dnumber$key))
            colnames(dnumber.key) <- c("key", "DrugNumber")
            dnumber <- dplyr::left_join(dnumber, dnumber.key, "key")
            d$DrugNumber <- dnumber$DrugNumber
            d$DrugNumber[d$take_drug %in% "no"] <- 0
        }
        else {
            d$DrugNumber = 0
        }
        if (!remove.other) {
            d$seqn[ck] <- paste0(d$seqn[ck], "-yes")
        }
        else {
            (ck <- which((d$seqn %in% unique(d$seqn[ck])) & d$take_drug == "other"))
            length(ck)
            if (length(ck) > 0) 
                d <- d[-ck, ]
        }
    }
    else {
        if (!isFALSE(DrugNumber)) {
            dnumber.key <- data.frame(table(d$seqn))
            colnames(dnumber.key) <- c("seqn", "DrugNumber")
            dnumber.key$seqn <- as.numeric(as.character(dnumber.key$seqn))
            d <- dplyr::left_join(d, dnumber.key, "seqn")
            d$DrugNumber[d$take_drug %in% "no"] <- 0
        }
        else {
            d$DrugNumber = 0
        }
    }
    var <- c("seqn", "Year", "take_drug", "DrugNumber")
    if (isTRUE(drugname) | is.character(drugname)) 
        append(var) <- "Drug"
    if (isTRUE(fdaNDC)) 
        append(var) <- "fdaNDC"
    if (isTRUE(dcn)) 
        append(var) <- "dcn"
    if (isTRUE(icn)) 
        append(var) <- "icn"
    if (isTRUE(icd10) & "icd10.code" %in% colnames(d)) 
        append(var) <- c("icd10.code", "icd10.description")
    d <- d[, var]
    if (dup.take.drug == "paste" & any(anyDuplicated(d$seqn))) {
        seqn <- unique(d$seqn[duplicated(d$seqn)])
        for (i in seqn) {
            (n <- which(d$seqn %in% i))
            if (ncol(d) >= 5) {
                for (j in 5:ncol(d)) {
                  d[n, j] <- paste0(d[n, j], collapse = ";;;")
                }
            }
            d <- d[-n[-1], ]
        }
    }
    else if (dup.take.drug == "remove") {
        ck <- !duplicated(paste0(d$seqn, d$take_drug))
        d <- d[ck, ]
    }
    d$seqn <- as.numeric(do::Replace0(d$seqn, "-yes"))
    if (!is.null(yes.code) & !is.null(other.code) & !is.null(no.code)) {
        d$take_drug <- ifelse(d$take_drug == "yes", yes.code, ifelse(d$take_drug == "other", other.code, 
            no.code))
    }
    if (isFALSE(take_drug)) 
        d <- drop_col(d, "take_drug")
    if (is.character(take_drug)) 
        col_rename(d) <- paste0("take_drug:", take_drug)
    if (isFALSE(drugname)) 
        d <- drop_col(d, "Drug")
    if (is.character(drugname)) 
        col_rename(d) <- paste0("Drug:", drugname)
    if (isFALSE(DrugNumber)) 
        d <- drop_col(d, "DrugNumber")
    if (is.character(DrugNumber)) 
        col_rename(d) <- paste0("DrugNumber:", DrugNumber)
    if (isFALSE(fdaNDC)) 
        d <- drop_col(d, "fdaNDC")
    if (isFALSE(dcn)) 
        d <- drop_col(d, "dcn")
    if (isFALSE(icn)) 
        d <- drop_col(d, "icn")
    if (isFALSE(icd10)) 
        d <- drop_col(d, "icd10.code", "icd10.description")
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `Factor`

```r
function (x) 
{
    dropna <- function(x) x[!is.na(x)]
    v <- do::Replace0(paste0(deparse(substitute(x)), collapse = ""), " ")
    if (is.data.frame(x)) {
        cmd <- ""
        for (i in colnames(x)) {
            if (is.character(x[, i]) | is.factor(x[, i])) {
                string <- sprintf(paste0(dropna(unique(x[, i])), collapse = "', '"), fmt = "c('%s')")
                append(cmd) <- sprintf("%s$%s <- factor(%s$%s, %s)", v, i, v, i, string)
            }
        }
        cmd <- do::rm_nchar(cmd, 0)
        context <- rstudioapi::getActiveDocumentContext()
        start_line <- context$selection[[1]]$range$start[[1]]
        rstudioapi::insertText(text = cmd)
        rstudioapi::setCursorPosition(position = c(start_line - 1, 1), id = NULL)
        rstudioapi::insertText(text = "# ")
        invisible()
    }
    else {
        lv <- levels(x)
        if (is.null(lv)) 
            lv <- do::unique_no.NA(x)
        string1 <- sprintf("%s <- factor(%s, levels = c(%s))", v, v, paste0(sprintf("\"%s\"", lv), collapse = ","))
        string <- paste0(string1, "\n")
        context <- rstudioapi::getActiveDocumentContext()
        start_line <- context$selection[[1]]$range$start[[1]]
        start_char <- context$selection[[1]]$range$end[[2]]
        rstudioapi::insertText(text = string)
        rstudioapi::setCursorPosition(position = c(start_line - 1, 1), id = NULL)
        rstudioapi::insertText(text = "# ")
        invisible()
    }
}
```

## `Flavonoids_download`

```r
function () 
{
    html <- rvest::read_html("https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds-flavonoid-database/")
    url <- sprintf(do::attr_href(set::grep_not_and(set::grep_and(rvest::html_elements(html, xpath = "//a[@href]"), 
        "flav_dr"), "_0708_sas")), fmt = "https://www.ars.usda.gov%s")
    for (i in 1:length(url)) {
        fi <- do::Replace0(tolower(do::file.name(url[i])), ".exe", ".sas7bdat", ".zip")
        (destfile <- paste0(get_Flavonoids_path(), "/", fi, ".zip"))
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
    cat("\n")
}
```

## `Frailty49`

```r
function () 
{
    df <- data.table::fread("Item                                                \t variable                      \t code\n<strong>Cognition</strong>            \t -            \t -\n1. experience confusion/memory problems             \t pfq056,pfq057                 \t yes=1; no=0\n<strong>Dependence</strong>            \t -            \t -\n2. managing money difficulty                        \t pfq060a,pfq061a               \t no difficulty=0;<br/>some difficulty=0.33;<br/>much difficulty=0.66;<br/>unable to do=1\n3. walking for a quarter mile difficulty            \t pfq060b,pfq061b               \t the same to above\n4. walking up ten steps difficulty                  \t pfq060c,pfq061c               \t the same to above\n5. stooping, crouching, kneeling difficulty         \t pfq060d,pfq061d               \t the same to above\n6. lifting or carrying difficulty                   \t pfq060e,pfq061e               \t the same to above\n7. house chore difficulty                           \t pfq060f,pfq061f               \t the same to above\n8. preparing meals difficulty                       \t pfq060g,pfq061g               \t the same to above\n9. standingup from armless chair difficulty        \t pfq060i,pfq061i               \t the same to above\n10. getting in and out of bed difficulty            \t pfq060j,pfq061j               \t the same to above\n11. using fork, knife, drinking from cup difficulty \t pfq060k,pfq061k               \t the same to above\n12. dressing yourself difficulty                    \t pfq060l,pfq061l               \t the same to above\n13. standing for long periods difficulty            \t pfq060m,pfq061m               \t the same to above\n14. grasp/holding small objects difficulty          \t pfq060p,pfq061p               \t the same to above\n15. attending social event difficulty               \t pfq060r,pfq061r               \t the same to above\n16. leisure activity at home difficulty             \t pfq060s,pfq061s               \t the same to above\n17. push or pull large objects difficulty           \t pfq061t                       \t the same to above\n<strong>Depressive Symptoms</strong>            \t -            \t -\n18. have little interest in doing things            \t ciqd008,ciqd009,dpq010        \t <strong>~2003</strong><br />every day,nearly every day = 1<br/>most days = 0.75<br/>about half the days = 0.50<br/>less than half the days = 0.25<br/><strong>2005~</strong><br />nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n19. feeling down, depressed, or hopeless            \t dpq020,ciqd001,ciqd002        \t the same to above\n20. trouble sleeping or sleeping too much           \t dpq030,ciqd025,ciqd026        \t <strong>~2003</strong><br />every night = 1<br/>nearly every night = 0.66<br/>less often = 0.33<br/><strong>2005~</strong><br />nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n21. feeling tired or having little energy           \t dpq040                        \t nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n22. poor appetite or overeating                     \t ciqd019,ciqd022,dpq050        \t <strong>~2003</strong><br />yes = 1<br />no = 0<br /><strong>2005~</strong><br />the same to above\n23. feeling bad about yourself                      \t dpq060,ciqd029                \t the same to above\n24. trouble concentrating on things                 \t dpq070,ciqd043                \t the same to above\n<strong>Comorbidities</strong>            \t -            \t -\n25. doctor ever said you had arthritis              \t mcq160a                       \t yes = 1; no = 0\n26. ever told you had thyroid problem               \t mcq160i,mcd160m,mcq160m       \t the same to above\n27. ever told you had chronic bronchitis            \t mcq160k,mcq160p               \t the same to above\n28. ever told you had cancer or malignancy          \t mcq220                        \t the same to above\n29. ever told had congestive heart failure          \t mcq160b                       \t the same to above\n30. ever told you had coronary heart disease        \t mcq160c                       \t the same to above\n31. ever told you had angina/angina pectoris        \t mcq160d                       \t the same to above\n32. ever told you had heart attack                  \t mcq160e                       \t the same to above\n33. ever told you had a stroke                      \t mcq160f                       \t the same to above\n34. ever told you had high blood pressure           \t bpq020                        \t the same to above\n35. doctor told you have diabetes                   \t diq010                        \t yes = 1; no =0; borderline=0.5\n36. ever told you had weak/failing kidneys          \t kiq020,kiq022                 \t yes = 1; no =0\n37. urine leakage bother you?                       \t kiq040,kiq050                 \t <strong>1999<br /></strong>yes = 1 ; no = 0<br /><strong>2001~</strong><br />greatly = 1<br/>very much = 0.75<br/<br />somewhat = 0.5<br/>only a little = 0.25\n<strong>Hospital Utilization and Access to Care</strong>            \t -            \t -\n38. general health condition                        \t huq010                        \t excellent,very good,good = 0<br />fair, poor = 1\n39. health now compared with 1 year ago             \t huq020                        \t about the same, better = 0<br />worse = 1\n40. overnight hospital patient in last year         \t huq070,hud070,huq071          \t yes = 1, no = 0\n41. times receive healthcare over past year         \t huq050,huq051                 \t none = 0; 1-4 = 0.5; >=5 =1\n42. number of prescription medicines taken          \t rxd030,rxduse,rxd295,rxdcount \t no = 0; 1-4 = 0.5; >=5 =1\n<strong>Physical Performance and Anthropometry</strong>            \t -            \t -\n43. body mass index (kg/m^2)                        \t bmxbmi                        \t <18.5, <U+2265>30 = 1<br/>25<U+2013><30 = 0.5<br/>18.5<U+2013>25 = 0\n<strong>Laboratory Values</strong>            \t -            \t -\n44. glycohemoglobin(%)                              \t lbxgh                         \t 0%<U+2013>5.7% = 0, >5.7% = 1\n45. red blood cell count (million cells/ul)         \t lbxrbcsi                      \t M: 4.7<U+2013>6.1 = 0, Other = 1<br />F: 4.2<U+2013>5.4 = 0, Other = 1\n46. hemoglobin (g/dl)                               \t lbxhgb                        \t M: 13.5<U+2013>18 = 0, Other = 1<br />F: 12<U+2013>16 = 0, Other = 1\n47. red cell distribution width (%)                 \t lbxrdw                        \t 11.6<U+2013>14.6 = 0, Other = 1\n48. lymphocyte percent (%)                          \t lbxlypct                      \t 20<U+2013>40 = 0, Other = 1\n49. segmented neutrophils percent (%)               \t lbxnepct                      \t 40<U+2013>80 = 0, Other = 1\n")
    kableExtra::kable_styling(kableExtra::kbl(df, escape = FALSE), full_width = FALSE)
}
```

## `Full_Join`

```r
function (..., by = "seqn", cat = TRUE, inspect = NULL) 
{
    lt <- list(...)
    nms <- do::get_names(...)
    if (length(nms) == 2) {
        nrow1.before <- nrow(lt[[1]])
        ncol1.before <- ncol(lt[[1]])
        nrow2.before <- nrow(lt[[2]])
        ncol2.before <- ncol(lt[[2]])
        d <- dplyr::full_join(lt[[1]], lt[[2]], by)
        nrow.after <- nrow(d)
        ncol.after <- ncol(d)
        maxn <- max(nchar(nms[1]), nchar("Final"))
        nms[1] <- do::equal_length(nms[1], nchar = maxn)
        final <- do::equal_length("Final", nchar = maxn)
        diff1 <- nrow.after - nrow1.before
        diff2 <- nrow.after - nrow2.before
        cmd <- sprintf("# %s:%s(%s) ; %s:%s(%s) \n# %s:%s", nms[1], nrow1.before, ifelse(diff1 == 0, 
            diff1, paste0("+", diff1)), nms[2], nrow2.before, ifelse(diff2 == 0, diff2, paste0("+", diff2)), 
            final, nrow.after)
        if (cat) 
            cat(cmd)
        if (!is.null(inspect)) {
            if (cat) {
                cat("\n")
                for (i in inspect) {
                  cat("\n~~~~~~~~~~~~~~~~\n")
                  cat(crayon::bgWhite(i))
                  if (i %in% colnames(lt[[1]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[1]), ">\n")
                    if (nrow(lt[[1]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[1]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[1]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(lt[[2]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[2]), ">\n")
                    if (nrow(lt[[2]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[2]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[2]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(d)) {
                    cat(paste0("\n<Final>\n"))
                    iii <- d[[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                }
            }
        }
        return(d)
    }
    else if (length(nms) > 2) {
        d <- lt[[1]]
        for (i in 2:length(lt)) {
            d <- dplyr::full_join(d, lt[[i]], by)
        }
        d
    }
}
```

## `Inner_Join`

```r
function (..., by = "seqn", cat = TRUE, inspect = NULL) 
{
    lt <- list(...)
    nms <- do::get_names(...)
    if (length(nms) == 2) {
        nrow1.before <- nrow(lt[[1]])
        ncol1.before <- ncol(lt[[1]])
        nrow2.before <- nrow(lt[[2]])
        ncol2.before <- ncol(lt[[2]])
        d <- dplyr::inner_join(lt[[1]], lt[[2]], by)
        nrow.after <- nrow(d)
        ncol.after <- ncol(d)
        maxn <- max(nchar(nms[1]), nchar("Final"))
        nms[1] <- do::equal_length(nms[1], nchar = maxn)
        final <- do::equal_length("Final", nchar = maxn)
        diff1 <- nrow.after - nrow1.before
        diff2 <- nrow.after - nrow2.before
        cmd <- sprintf("# %s:%s(%s) ; %s:%s(%s) \n# %s:%s", nms[1], nrow1.before, diff1, nms[2], nrow2.before, 
            diff2, final, nrow.after)
        if (cat) 
            cat(cmd)
        if (!is.null(inspect)) {
            if (cat) {
                cat("\n")
                for (i in inspect) {
                  cat("\n~~~~~~~~~~~~~~~~\n")
                  cat(crayon::bgWhite(i))
                  if (i %in% colnames(lt[[1]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[1]), ">\n")
                    if (nrow(lt[[1]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[1]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[1]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(lt[[2]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[2]), ">\n")
                    if (nrow(lt[[2]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[2]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[2]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(d)) {
                    cat(paste0("\n<Final>\n"))
                    iii <- d[[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                }
            }
        }
        return(d)
    }
    else if (length(nms) > 2) {
        d <- lt[[1]]
        for (i in 2:length(lt)) {
            d <- dplyr::inner_join(d, lt[[i]], by)
        }
        d
    }
}
```

## `Left_Join`

```r
function (..., by = "seqn", cat = TRUE, inspect = NULL) 
{
    lt <- list(...)
    nms <- do::get_names(...)
    if (length(nms) == 2) {
        nrow1.before <- nrow(lt[[1]])
        ncol1.before <- ncol(lt[[1]])
        nrow2.before <- nrow(lt[[2]])
        ncol2.before <- ncol(lt[[2]])
        d <- dplyr::left_join(lt[[1]], lt[[2]], by)
        nrow.after <- nrow(d)
        ncol.after <- ncol(d)
        maxn <- max(nchar(nms[1]), nchar("Final"))
        nms[1] <- do::equal_length(nms[1], nchar = maxn)
        final <- do::equal_length("Final", nchar = maxn)
        diff <- nrow1.before - nrow2.before
        cmd <- sprintf("# %s:%s ; %s:%s(%s) \n# %s:%s", nms[1], nrow1.before, nms[2], nrow2.before, ifelse(diff > 
            0, paste0("+", diff), diff), final, nrow.after)
        if (cat) 
            cat(cmd)
        if (!is.null(inspect)) {
            if (cat) {
                cat("\n")
                for (i in inspect) {
                  cat("\n~~~~~~~~~~~~~~~~\n")
                  cat(crayon::bgWhite(i))
                  if (i %in% colnames(lt[[1]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[1]), ">\n")
                    if (nrow(lt[[1]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[1]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[1]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(lt[[2]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[2]), ">\n")
                    if (nrow(lt[[2]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[2]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[2]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(d)) {
                    cat(paste0("\n<Final>\n"))
                    iii <- d[[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                }
            }
        }
        return(d)
    }
    else if (length(nms) > 2) {
        d <- lt[[1]]
        for (i in 2:length(lt)) {
            d <- dplyr::left_join(d, lt[[i]], by)
        }
        d
    }
}
```

## `Qnplot`

```r
function (..., xlab = NULL, ylab = NULL, skip = 0, linewidth = 0.90000000000000002, axis.text.size = 10, 
    axis.label.size = 12, legend.text.size = 9.5, legend.position = "right", strip.text.size = 10, file = NULL, 
    width = par("din")[1], height = par("din")[2], unit = "in", dpi = 300) 
{
    suppressWarnings(dir.create(tempdir()))
    ls <- list(...)
    if (length(ls) == 1 & any(class(ls[[1]]) %in% c("glm", "cph", "ols"))) {
        fit = ls[[1]]
        d <- do::model.data(fit)
        x <- do::model.x(fit)
        d$xxx <- d[, x]
        res <- lapply(3:8, function(n) {
            d[, x] <- quant(d$xxx, n = n, Q = TRUE, cat = F)
            (fiti <- update(fit, data = d))
            (cf <- coef(fiti))
            (ck <- do::right(names(cf), 3) %in% paste0("=Q", 1:length(cf)))
            names(cf)[ck] <- do::right(names(cf)[ck], 2)
            (cf <- cf[ck])
            (c0 <- rep(0, length(cf) + 1))
            names(c0) <- paste0("Q", 1:length(c0))
            nms <- set::and(names(c0), names(cf))
            c0[nms] <- cf[nms]
            data.frame(n = n, Q = names(c0), Estimate = c0)
        }) %>% do.call(what = rbind)
        res$n <- paste0("Q", res$n)
        ggplot(res, aes(Q, Estimate, group = n)) + geom_line() + geom_point() + ggrepel::geom_text_repel(aes(label = round(Estimate, 
            2))) + xlab(NULL) + facet_wrap(~n) + theme(strip.text = element_text(size = 13))
    }
    else {
        df <- lapply(ls, function(i) i$reg_CI4plot) %>% do.call(what = rbind)
        ck <- df$character %in% paste0("Q", 1:nrow(df))
        df <- df[ck, ]
        p <- ggplot(df, aes(x = character, y = est, group = x, color = x)) + geom_line(show.legend = ifelse(length(unique(df$x)) == 
            1, F, T)) + geom_point(show.legend = ifelse(length(unique(df$x)) == 1, F, T)) + geom_errorbar(aes(ymin = low, 
            ymax = high), width = 0.20000000000000001, show.legend = ifelse(length(unique(df$x)) == 1, 
            F, T))
        if (length(unique(df$dyg)) > 1 & length(unique(df$model)) > 1) {
            p <- p + facet_grid(dyg ~ model)
        }
        else if (length(unique(df$dyg)) > 1) {
            p <- p + facet_grid(~dyg)
        }
        else if (length(unique(df$model)) > 1) {
            p <- p + facet_grid(~model)
        }
        if (is.null(xlab)) 
            xlab <- "Qn"
        if (is.null(ylab)) 
            ylab <- "Estimate"
        p <- p + ylab(ylab) + xlab(xlab) + theme(axis.text.x = element_text(size = axis.text.size, color = "#5D646F"), 
            axis.text.y = element_text(size = axis.text.size, color = "#5D646F"), axis.title = element_text(size = axis.label.size), 
            legend.position = legend.position, legend.text = element_text(size = legend.text.size), strip.text = element_text(color = "#5D646F", 
                size = strip.text.size, face = "bold"))
        print(p)
        if (!is.null(file)) {
            ggsave(filename = file, plot = p, width = width, height = height, dpi = dpi, units = unit)
        }
        invisible()
    }
}
```

## `RCS`

```r
function (..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.94999999999999996, ref.zero = TRUE, 
    log = TRUE) 
UseMethod("RCS")
```

## `Recode`

```r
function (x, ..., string = TRUE, cat = TRUE, to.numeric = FALSE, order = F) 
{
    replace <- c(...)
    if (is.data.frame(x)) {
        xh <- paste0(deparse(substitute(x)), collapse = "")
        for (i in 1:ncol(x)) {
            if (i == 1) 
                cmd <- c()
            if (tolower(colnames(x)[i]) %in% c("seqn", "year", "sdmvpsu", "sdmvstra")) 
                (next)(i)
            if (is.numeric(x[, i])) {
                (next)(i)
            }
            else {
                level <- levels(x[, i])
                if (is.null(level)) 
                  level <- do::unique_no.NA(as.character(x[, i]))
                if (anyNA(x[, i])) 
                  level <- c(level, "NA")
                replace <- sprintf(paste0(paste0(level, "::"), collapse = "\", \n\t\""), fmt = "\"%s\",\n\tto.numeric = FALSE)")
                cmdi <- paste0(xh, "$", colnames(x)[i], " <- Recode", "(", xh, "$", colnames(x)[i], ",\n\t", 
                  replace, "\n")
                if (is.null(cmd)) {
                  cmd <- cmdi
                }
                else {
                  cmd <- paste0(cmd, "\n", cmdi)
                }
            }
        }
        xx <- rstudioapi::getActiveDocumentContext()
        for (i in (xx$selection[[1]]$range$start[[1]]):1) {
            f6 <- do::Trim_left(xx$contents[i])
            if (f6 == "") {
                (next)(i)
            }
            else if (do::left(f6, 7) == "Recode(") {
                rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                rstudioapi::insertText("# ")
                rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                rstudioapi::insertText(text = cmd)
                (break)(i)
            }
            else if (do::left(f6, 7) == "nhanesR::Recode(") {
                rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                rstudioapi::insertText("# ")
                rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                rstudioapi::insertText(text = cmd)
                (break)(i)
            }
        }
        invisible(cmd)
    }
    else if (is.character(x) | is.factor(x)) {
        if (is.null(replace)) {
            xh <- paste0(deparse(substitute(x)), collapse = "")
            level <- levels(x)
            if (is.null(level)) 
                level <- do::unique_no.NA(as.character(x))
            if (order) 
                level <- do::increase(level)
            if (anyNA(x)) 
                level <- c(level, "NA")
            replace <- sprintf(paste0(paste0(level, "::"), collapse = "\", \n\t\""), fmt = "\"%s\",\n\tto.numeric = FALSE)")
            cmd <- paste0(xh, " <- Recode", "(", xh, ",\n\t", replace, "\n")
            xx <- rstudioapi::getActiveDocumentContext()
            for (i in (xx$selection[[1]]$range$start[[1]]):1) {
                f6 <- do::Trim_left(xx$contents[i])
                if (f6 == "") {
                  (next)(i)
                }
                else if (do::left(f6, 7) == "Recode(") {
                  rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                  rstudioapi::insertText("# ")
                  rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                  rstudioapi::insertText(text = cmd)
                  (break)(i)
                }
                else if (do::left(f6, 7) == "nhanesR::Recode(") {
                  rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                  rstudioapi::insertText("# ")
                  rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                  rstudioapi::insertText(text = cmd)
                  (break)(i)
                }
            }
            invisible(cmd)
        }
        else {
            (factorck <- is.factor(x))
            if (factorck) {
                (from <- do::Replace0(replace, " {0,}:: {0,}.*"))
                (ck <- lapply(from, function(i) {
                  x == i & !is.na(x)
                }))
                for (i in 1:length(ck)) {
                  (to <- do::Replace0(replace[i], ".*:: {0,}"))
                  if (to == "") 
                    (next)(i)
                  if (to == "NA") 
                    to <- NA
                  levels(x)[levels(x) == from[i]] <- to
                }
                if (any(from == "NA")) {
                  to <- do::Replace0(replace[from == "NA"], ".*:: {0,}")
                  if (to != "") {
                    levels(x) <- unique(c(levels(x), to))
                    x[is.na(x)] <- to
                  }
                }
            }
            else {
                x <- as.character(x)
                (from <- do::Replace0(replace, " {0,}:: {0,}.*"))
                (ck <- lapply(from, function(i) {
                  if (i == "NA") {
                    is.na(x)
                  }
                  else {
                    x == i & !is.na(x)
                  }
                }))
                for (i in 1:length(ck)) {
                  (to <- do::Replace0(replace[i], ".*:: {0,}"))
                  if (to == "") 
                    (next)(i)
                  if (to == "NA") 
                    to <- NA
                  x[ck[[i]]] <- to
                }
            }
            if (to.numeric) {
                to_numeric(x)
            }
            else {
                return(x)
            }
        }
    }
    else if (is.numeric(x)) {
        if (is.null(replace)) 
            replace <- median(x)
        if (all(is.numeric(replace))) {
            if (length(replace) == 1) {
                ck <- x < replace
                if (string) {
                  x[!is.na(ck) & ck] <- sprintf("[,%s)", replace)
                  x[!is.na(ck) & !ck] <- sprintf("[%s,]", replace)
                  level <- c(sprintf("[,%s)", replace), sprintf("[%s,]", replace))
                }
                else {
                  x[!is.na(ck) & ck] <- 1
                  x[!is.na(ck) & !ck] <- 2
                  cat(" < ", replace, "--->1\n")
                  cat(" >=", replace, "--->2\n\n")
                }
            }
            else {
                maxchr <- max(nchar(replace))
                replace <- replace[order(replace)]
                (replace <- replace[replace > min(x) & replace < max(x)])
                x0 <- x
                for (i in 1:length(replace)) {
                  if (i == 1) {
                    ck <- x0 < replace[1]
                    if (string) {
                      x[!is.na(ck) & ck] <- sprintf("[,%s)", replace[1])
                      level <- sprintf("[,%s)", replace[1])
                    }
                    else {
                      x[!is.na(ck) & ck] <- 1
                      if (cat) 
                        cat(paste0(paste0(do::rep_n(each = maxchr + 3, " "), " < "), paste0(replace[i], 
                          do::rep_n(" ", maxchr - nchar(replace[i]))), "--->", i, "\n"))
                    }
                  }
                  else {
                    ck <- x0 < replace[i] & x0 >= replace[i - 1]
                    if (string) {
                      x[!is.na(ck) & ck] <- sprintf("[%s,%s)", replace[i - 1], replace[i])
                      level <- c(level, sprintf("[%s,%s)", replace[i - 1], replace[i]))
                    }
                    else {
                      x[!is.na(ck) & ck] <- i
                      if (cat) 
                        cat(paste0(">=", paste0(replace[i - 1], do::rep_n(" ", maxchr - nchar(replace[i - 
                          1]))), "& < ", paste0(replace[i], do::rep_n(" ", maxchr - nchar(replace[i]))), 
                          "--->", i, "\n"))
                    }
                  }
                  if (i == length(replace)) {
                    ck <- x0 >= replace[i]
                    if (string) {
                      x[!is.na(ck) & ck] <- sprintf("[%s,]", replace[i])
                      level <- c(level, sprintf("[%s,]", replace[i]))
                    }
                    else {
                      x[!is.na(ck) & ck] <- i + 1
                      if (cat) 
                        cat(paste0(paste0(do::rep_n(each = maxchr + 3, " "), " >="), paste0(replace[i], 
                          do::rep_n(" ", maxchr - nchar(replace[i]))), "--->", i + 1, "\n\n"))
                    }
                  }
                }
                x <- factor(x, levels = level)
            }
        }
        else {
            x <- as.character(x)
            x <- Recode(x, replace, cat = cat)
        }
        return(x)
    }
}
```

## `Right_Join`

```r
function (..., by = "seqn", cat = TRUE, inspect = NULL) 
{
    lt <- list(...)
    nms <- do::get_names(...)
    if (length(nms) == 2) {
        nrow1.before <- nrow(lt[[1]])
        ncol1.before <- ncol(lt[[1]])
        nrow2.before <- nrow(lt[[2]])
        ncol2.before <- ncol(lt[[2]])
        d <- dplyr::right_join(lt[[1]], lt[[2]], by)
        nrow.after <- nrow(d)
        ncol.after <- ncol(d)
        maxn <- max(nchar(nms[1]), nchar("Final"))
        nms[1] <- do::equal_length(nms[1], nchar = maxn)
        final <- do::equal_length("Final", nchar = maxn)
        diff <- nrow2.before - nrow1.before
        cmd <- sprintf("# %s:%s(%s) ; %s:%s \n# %s:%s", nms[1], nrow1.before, ifelse(diff > 0, paste0("+", 
            diff), diff), nms[2], nrow2.before, final, nrow.after)
        if (cat) 
            cat(cmd)
        if (!is.null(inspect)) {
            if (cat) {
                cat("\n")
                for (i in inspect) {
                  cat("\n~~~~~~~~~~~~~~~~\n")
                  cat(crayon::bgWhite(i))
                  if (i %in% colnames(lt[[1]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[1]), ">\n")
                    if (nrow(lt[[1]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[1]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[1]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(lt[[2]])) {
                    nms1 <- paste0("\n<", do::Trim_right(nms[2]), ">\n")
                    if (nrow(lt[[2]]) > nrow(d)) {
                      cat(crayon::bgCyan(crayon::white(nms1)))
                    }
                    else if (nrow(lt[[2]]) < nrow(d)) {
                      cat(crayon::bgRed(crayon::white(nms1)))
                    }
                    else {
                      cat(nms1)
                    }
                    iii <- lt[[2]][[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                  if (i %in% colnames(d)) {
                    cat(paste0("\n<Final>\n"))
                    iii <- d[[i]]
                    if (is.numeric(iii)) {
                      cat(sprintf("Mean:%s; sd:%s; Median:%s; range:[%s]\n", round(mean(iii, na.rm = T), 
                        4), round(sd(iii, na.rm = T), 4), round(median(iii, na.rm = T), 4), paste0(round(range(iii, 
                        na.rm = T), 4), collapse = ",")))
                    }
                    else if (is.character(iii)) {
                      (tb <- do::give_names(data.frame(table(iii, useNA = "i")), c(i, "Freq")))
                      tb$Percent <- round(tb$Freq/sum(tb$Freq) * 100, 4)
                      colnames(tb)[3] <- "Percent(%)"
                      print(tb)
                    }
                  }
                }
            }
        }
        return(d)
    }
    else if (length(nms) > 2) {
        d <- lt[[1]]
        for (i in 2:length(lt)) {
            d <- dplyr::right_join(d, lt[[i]], by)
        }
        d
    }
}
```

## `add_col`

```r
function (data, colname = NULL, value = NULL, condition = NULL, position = NULL) 
UseMethod("add_col")
```

## `ageAdjust`

```r
function (design, agecat = NULL, population = NULL, disease = NULL, mean_var = NULL, by = NULL, subset = NULL) 
{
    if (is.null(agecat)) {
        d <- design$variables
        colnames(d)[tolower(colnames(d)) == "age"] <- "age"
        if (!"age" %in% colnames(d)) {
            if ("Year" %in% colnames(d)) {
                d <- db_demo(d, ageyr = "age", psu_strat = F)
            }
            else {
                d <- db_demo(d, years = prepare_years(), ageyr = "age", psu_strat = F)
            }
        }
        d <- add_col(d, "agecatiii", "0-1", d$age >= 0 & d$age <= 1)
        d <- add_col(d, "agecatiii", "1-1", d$age >= 1 & d$age <= 1)
        d <- add_col(d, "agecatiii", "2-4", d$age >= 2 & d$age <= 4)
        d <- add_col(d, "agecatiii", "5-5", d$age >= 5 & d$age <= 5)
        d <- add_col(d, "agecatiii", "6-8", d$age >= 6 & d$age <= 8)
        d <- add_col(d, "agecatiii", "9-9", d$age >= 9 & d$age <= 9)
        d <- add_col(d, "agecatiii", "10-11", d$age >= 10 & d$age <= 11)
        d <- add_col(d, "agecatiii", "12-14", d$age >= 12 & d$age <= 14)
        d <- add_col(d, "agecatiii", "15-17", d$age >= 15 & d$age <= 17)
        d <- add_col(d, "agecatiii", "18-19", d$age >= 18 & d$age <= 19)
        d <- add_col(d, "agecatiii", "20-24", d$age >= 20 & d$age <= 24)
        d <- add_col(d, "agecatiii", "25-29", d$age >= 25 & d$age <= 29)
        d <- add_col(d, "agecatiii", "30-34", d$age >= 30 & d$age <= 34)
        d <- add_col(d, "agecatiii", "35-39", d$age >= 35 & d$age <= 39)
        d <- add_col(d, "agecatiii", "40-44", d$age >= 40 & d$age <= 44)
        d <- add_col(d, "agecatiii", "45-49", d$age >= 45 & d$age <= 49)
        d <- add_col(d, "agecatiii", "50-54", d$age >= 50 & d$age <= 54)
        d <- add_col(d, "agecatiii", "55-59", d$age >= 55 & d$age <= 59)
        d <- add_col(d, "agecatiii", "60-64", d$age >= 60 & d$age <= 64)
        d <- add_col(d, "agecatiii", "65-69", d$age >= 65 & d$age <= 69)
        d <- add_col(d, "agecatiii", "70-74", d$age >= 70 & d$age <= 74)
        d <- add_col(d, "agecatiii", "75-79", d$age >= 75 & d$age <= 79)
        d <- add_col(d, "agecatiii", "80-84", d$age >= 80 & d$age <= 84)
        d <- add_col(d, "agecatiii", "85+", d$age >= 85)
        l0 <- census_2000.All.ages()$age
        d$agecatiii <- factor(d$agecatiii, levels = l0[l0 %in% d$agecatiii])
        population <- census_2000.All.ages()[l0 %in% d$agecatiii, "Population_in_thousands"]
        agecat <- "agecatiii"
        design <- update(design, agecatiii = d$agecatiii)
    }
    if (!is.null(by)) 
        by <- rev(by)
    if (!is.null(disease)) {
        disease.value <- design$variables[, disease]
        uv <- unique(disease.value)
        if (is.character(uv) | is.factor(uv)) {
            disease.value <- as.character(tolower(disease.value))
            if (all(do::unique_no.NA(disease.value) %in% c("yes", "no"))) {
                disease.value <- Recode(disease.value, "no::0", "yes::100", "NA::", to.numeric = T)
            }
            else if (all(disease.value %in% c("1", "0"))) {
                disease.value <- as.numeric(disease.value) * 100
            }
            else {
                stop("disease is not yes/no or 1/0")
            }
        }
        else if (is.numeric(uv)) {
            if (all(disease.value %in% c(1, 0))) {
                disease.value <- disease.value * 100
            }
            else {
                stop("disease is not yes/no or 1/0")
            }
        }
        else if (is.logical(uv)) {
            disease.value <- disease.value * 100
        }
        else {
            stop("disease is not yes/no or 1/0")
        }
        design$variables[, disease] <- disease.value
    }
    else {
        disease <- mean_var
    }
    if (is.null(by)) {
        design <- update(design, whenbyisnull = ifelse(is.na(disease), NA, "all"))
        svystd4ageAdjust <- survey::svystandardize(design = design, by = make.formula(agecat), over = make.formula("whenbyisnull"), 
            population = population, excluding.missing = make.formula(c(agecat, disease)))
        r <- survey::svyby(formula = make.formula(disease), by = make.formula("whenbyisnull"), survey::svymean, 
            design = svystd4ageAdjust, keep.names = F)
        colnames(r)[1] <- "all"
        return(r)
    }
    subset0 <- substitute(subset)
    if (is.null(subset0)) {
        svystd4ageAdjust <- survey::svystandardize(design = design, by = make.formula(agecat), population = population, 
            over = make.formula(by), excluding.missing = make.formula(c(by, agecat, disease)))
        r <- survey::svyby(formula = make.formula(disease), by = make.formula(by), survey::svymean, design = svystd4ageAdjust, 
            keep.names = F)
        r[, c(rev(by), disease, "se")]
    }
    else {
        .svystd4ageAdjust <<- survey::svystandardize(design = design, by = make.formula(agecat), population = population, 
            over = make.formula(by), excluding.missing = make.formula(c(by, agecat, disease)))
        pt0 <- parse(text = sprintf("subset(.svystd4ageAdjust, %s)", paste0(deparse(subset0), collapse = "")))
        r <- survey::svyby(formula = make.formula(disease), by = make.formula(by), survey::svymean, design = eval(pt0, 
            envir = .GlobalEnv), keep.names = F)
        r[, c(rev(by), disease, "se")]
    }
}
```

## `aggregate_max`

```r
function (data, x, by, na.rm = T) 
{
    .max.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        max(x, na.rm = TRUE)
    }
    if (na.rm) {
        aggregate2(data, x, by, ".max.nona")
    }
    else {
        aggregate2(data, x, by, "max")
    }
}
```

## `aggregate_mean`

```r
function (data, x, by, na.rm = T) 
{
    .mean.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        mean(x, na.rm = TRUE)
    }
    if (na.rm) {
        aggregate2(data, x, by, ".mean.nona")
    }
    else {
        aggregate2(data, x, by, "mean")
    }
}
```

## `aggregate_min`

```r
function (data, x, by, na.rm = T) 
{
    .min.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        min(x, na.rm = TRUE)
    }
    if (na.rm) {
        aggregate2(data, x, by, ".min.nona")
    }
    else {
        aggregate2(data, x, by, "min")
    }
}
```

## `aggregate_sum`

```r
function (data, x, by, na.rm = T) 
{
    .sum.nona <<- function(x) {
        if (all(is.na(x))) 
            return(NA)
        sum(x, na.rm = TRUE)
    }
    if (na.rm) {
        aggregate2(data, x, by, ".sum.nona")
    }
    else {
        aggregate2(data, x, by, "sum")
    }
}
```

## `append<-`

```r
function (x, value) 
{
    x <- c(x, value)
    x
}
```

## `bind_col`

```r
function (df) 
{
    df0 <- df
    df[is.na(df)] <- ""
    vc <- do::Trim(paste0_columns(df, collapse = ";"), ";")
    ck <- do::NA.row.sums(df0) == ncol(df0)
    vc[ck] <- NA
    do::Replace(vc, ";{2,}", ";")
}
```

## `browse_rxq_Drug`

```r
function () 
{
    nhs_html(nhs_tsv("rxq_drug", cat = FALSE)[1])
}
```

## `browse_rxq_Rx`

```r
function (years) 
{
    nhs_html(nhs_tsv("rxq_rx", years = years, cat = FALSE))
}
```

## `browser.fndds`

```r
function () 
{
    browseURL(system.file("data/fndds.html", package = "nhanesR"))
}
```

## `browser.fped`

```r
function () 
{
    browseURL(system.file("data/fped.html", package = "nhanesR"))
}
```

## `browser.survey`

```r
function () 
{
    url <- paste0("http://127.0.0.1:", tools::startDynamicHelp(NA), "/library/survey/html/00Index.html")
    cat(url)
    browseURL(url)
}
```

## `bu`

```r
function (x, rule) 
{
    if (missing(x)) 
        x <- get("bu_x", envir = .GlobalEnv)
    if (is.character(x)) {
        rule <- x
        x <- get("bu_x", envir = parent.frame())
    }
    rule <- do::Replace0(rule, " ")
    left <- ifelse(do::left(rule, 1) == "[", ">=", ">")
    right <- ifelse(do::right(rule, 1) == "]", "<=", "<")
    miss_left <- do::mid(rule, 2, 1) == ","
    miss_right <- do::left(do::right(rule, 2), 1) == ","
    value <- do::complete.data(as.numeric(do::list1(strsplit(do::knife_right(do::knife_left(rule, 1), 
        1), ","))))
    if (!miss_left & !miss_right) {
        string <- sprintf("x %s %s & x %s %s", left, value[1], right, value[2])
    }
    else if (!miss_left & miss_right) {
        string <- sprintf("x %s %s", left, value)
    }
    else if (miss_left & !miss_right) {
        string <- sprintf("x %s %s", right, value)
    }
    eval(parse(text = string))
}
```

## `bu_above.equal`

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

## `bu_lower.equal`

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

## `build_codebook`

```r
function (progress = T) 
{
    files <- nhs_tsv()
    ck <- tools::file_ext(files) != "codebook"
    if (any(ck)) {
        ext <- sprintf(unique(tools::file_ext(files[ck])), fmt = "\\.%s")
        files[ck] <- sprintf(do::Replace0(files[ck], ext), fmt = "%s.codebook")
    }
    if (progress) 
        pb <- txtProgressBar(max = length(files), width = 30, style = 3)
    fd <- do.call(lapply(files, function(i) {
        if (progress) 
            setTxtProgressBar(pb, which(files == i))
        i <- do::Replace(do::formal_dir(i), "//", "/")
        (Year <- prepare_years(i))
        (Item <- prepare_items(i))
        (file <- do::Replace0(do::file.name(i), "\\.codebook"))
        (codei <- read.delim(i, comment.char = "#"))
        if (nrow(codei) == 0) 
            return()
        (codei <- codei[, c("variable", "code", "label")])
        cbind(Year = Year, Item = Item, file = file, codei)
    }), what = plyr::rbind.fill)
    data.table::fwrite(fd, paste0(get_config_path(), "/codebook.txt"), sep = "\t", row.names = FALSE)
    if (progress) 
        cat("\n")
}
```

## `build_varLabel`

```r
function (progress = TRUE) 
{
    (varLabel <- nhs_files_pc(file_ext = "varLabel"))
    if (length(varLabel) == 0) 
        return()
    if (progress) 
        pb <- txtProgressBar(max = length(varLabel), width = 30, style = 3)
    fd <- do.call(lapply(varLabel, function(i) {
        if (progress) 
            setTxtProgressBar(pb, which(varLabel == i))
        df <- tryCatch(read.table(i, comment.char = "#", header = T), error = function(e) read.delim(i, 
            comment.char = "#"))
        if (nrow(df) == 0) 
            return()
        file <- do::Replace0(do::file.name(i), "\\.varLabel")
        cbind(year = prepare_years(i), item = prepare_items(i), file = file, df)
    }), what = plyr::rbind.fill)
    data.table::fwrite(fd, paste0(get_config_path(), "/varLabel.txt"), sep = "\t", row.names = FALSE)
    if (progress) 
        cat("\n")
}
```

## `census_2000.All.ages`

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

## `census_2010.All.ages`

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

## `census_range`

```r
function (..., sum = FALSE) 
{
    range <- c(...)
    if (length(range) == 1) {
        df <- do::col_split(do::Replace(census_2000.All.ages()$age, "\\+", "-100000"), "-")
        ck <- as.numeric(df$x1) >= range
        r <- census_2000.All.ages()[ck, ]
    }
    else if (length(range) == 2) {
        min <- min(range)
        max <- max(range)
        df <- do::col_split(do::Replace(census_2000.All.ages()$age, "\\+", "-100000"), "-")
        ck <- as.numeric(df$x1) >= min & max >= as.numeric(df$x2)
        r <- census_2000.All.ages()[ck, ]
    }
    if (sum) {
        return(sum(r[, 2]))
    }
    else {
        return(r)
    }
}
```

## `census_range.2010`

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

## `character2numeric`

```r
function (x) 
{
    if (is.numeric(x)) 
        return(x)
    (levels <- levels(x))
    if (is.null(levels)) 
        levels <- unique(x)
    (levels <- levels[!is.null(levels)])
    (levels <- levels[levels %in% unique(x)])
    (string <- paste0(levels, "::", 1:length(levels)))
    x <- as.character(x)
    Recode(x, string, to.numeric = T, cat = F)
}
```

## `check1`

```r
function (x) 
{
    if ("survey.design" %in% class(x)) 
        x = x$variables
    nmi <- unlist(lapply(colnames(x), function(i) {
        xu <- unique(x[, i])
        ck1 <- length(xu) == 1
        xu <- xu[!is.na(xu)]
        ck2 <- length(xu) == 1
        if (ck1 | ck2) 
            return(i)
    }))
    if (!is.null(nmi)) {
        r <- lapply(nmi, function(i) unique(x[, i]))
        names(r) <- nmi
        r
    }
}
```

## `col.counts`

```r
function (data) 
{
    colSums(!is.na(data))
}
```

## `col.max`

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

## `col.means`

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

## `col.sums`

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

## `col_rename`

```r
function (data, ...) 
{
    value <- c(...)
    if (is.null(value)) {
        cmd <- sprintf("col_rename(%s) <- c(%s)\n", deparse(substitute(data)), paste0(sprintf("%s'%s::'", 
            do::rep_n(" ", 16 + nchar(deparse(substitute(data)))), colnames(data)), collapse = ", \n"))
        cmd <- do::Replace(cmd, "\\) <- c\\( {1,}", ") <- c(")
        xx <- rstudioapi::getActiveDocumentContext()
        for (i in (xx$selection[[1]]$range$start[[1]]):1) {
            f6 <- do::Trim_left(xx$contents[i])
            if (f6 == "") {
                (next)(i)
            }
            else if (do::left(f6, 11) == "col_rename(" & !grepl("<-", f6)) {
                rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                rstudioapi::insertText("# ")
                rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                rstudioapi::insertText(text = cmd)
                (break)(i)
            }
        }
        invisible(cmd)
    }
    else {
        value <- do::Trim(c(...))
        (from <- strsplit(Replace0(ignore.case = T, value, " {0,}:.*"), " {0,}, {0,}"))
        (to <- Replace0(ignore.case = T, value, ".*: {0,}"))
        ck <- nchar(to) == 0
        from <- from[!ck]
        to <- to[!ck]
        for (i in 1:length(from)) {
            colnames(data)[colnames(data) %in% from[[i]]] <- to[i]
        }
        data
    }
}
```

## `col_rename<-`

```r
function (x, value) 
{
    col_rename(x, value)
}
```

## `config_items`

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

## `config_path`

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

## `config_temp`

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

## `config_years`

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

## `create_diag_MASLD.cap`

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

## `crude.Model.n`

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

## `cut_headtail`

```r
function (x, col, ..., cat = T) 
UseMethod("cut_headtail")
```

## `db_Alcohol.drinks`

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

## `db_DSD`

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

## `db_EVD68`

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

## `db_FoodCD`

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

## `db_HemalBiochemistry`

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

## `db_IgE`

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

## `db_MCD`

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

## `db_Menopause`

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

## `db_PbCd`

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

## `db_alpha.rb`

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

## `db_alpha.rsv`

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

## `db_aux`

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

## `db_auxar1`

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

## `db_auxar2`

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

## `db_auxtym1`

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

## `db_auxtym2`

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

## `db_auxwbr`

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

## `db_beta.rsv.braycurtis`

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

## `db_beta.rsv.unwunifrac`

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

## `db_beta.rsv.wunifrac`

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

## `db_blood.pressure`

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

## `db_bodyMeasure`

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

## `db_carotenoid`

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

## `db_cbc`

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

## `db_cfq`

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

## `db_coffee`

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

## `db_coffee.time`

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

## `db_demo`

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

## `db_dnmepi`

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

## `db_dr.ProcessedMeat`

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

## `db_dr.alcoh.beverages`

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

## `db_dr.apple`

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

## `db_dr.bananas`

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

## `db_dr.fdcd`

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

## `db_dr.iceCream`

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

## `db_dr.live.microbes`

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

## `db_dr.milk`

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

## `db_dr.nuts`

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

## `db_dr.ssb`

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

## `db_driff`

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

## `db_drtot`

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

## `db_ds.manganese`

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

## `db_ds.melatonin`

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

## `db_ds.silicon`

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

## `db_ds.zinc`

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

## `db_dsids`

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

## `db_dsids.30`

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

## `db_dstot`

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

## `db_dstot.30`

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

## `db_dxx`

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

## `db_dxxag`

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

## `db_dxxfem`

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

## `db_dxxspn`

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

## `db_eating.occasion`

```r
function (years, day = 1) 
{
    iff <- nhs_tsv(sprintf("xiff|%siff", day[1]), years = years, cat = FALSE)
    d <- nhs_read(iff, sprintf("drd030,drd030z,dr%s_030z:eating.occasion.name", day[1]), cat = FALSE)
    freq_count(d, "eating.occasion.name")
}
```

## `db_flavonoids`

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

## `db_flxcln`

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

## `db_fndds`

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

## `db_fped`

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

## `db_hormone`

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

## `db_mango`

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

## `db_mort`

```r
function (data, years, varLabel = TRUE, codebook = TRUE, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- do.call(lapply(years, function(i) mort_read(years = i, varLabel = varLabel, codebook = codebook)), 
        what = plyr::rbind.fill)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `db_muscle.strength`

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

## `db_nova`

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

## `db_ogtt`

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

## `db_ohxden`

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

## `db_sandwiches`

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

## `db_slq`

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

## `db_sprint`

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

## `db_spx`

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

## `db_tea`

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

## `db_urine.alb.cr`

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

## `design4matchit`

```r
function (design) 
{
    x <- cbind(design$variables, SW = (1/design$prob)/mean(1/design$prob))
    cbind(xrxoxwnxuxbxmxexr = 1:nrow(x), x)
}
```

## `dex_ABPI`

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

## `dex_ABSI`

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

## `dex_AHA.PREVENT`

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

## `dex_AIP`

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

## `dex_ASCVD.h10yr`

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

## `dex_BARD`

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

## `dex_BRI`

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

## `dex_BiologicalAge`

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

## `dex_CALLY`

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

## `dex_CCI`

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

## `dex_CDAI`

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

## `dex_CMDS`

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

## `dex_CMI`

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

## `dex_CONUT`

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

## `dex_DASH.Mellen`

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

## `dex_DII`

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

## `dex_DI_GM`

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

## `dex_FIB.4`

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

## `dex_FLI`

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

## `dex_FS`

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

## `dex_FSI`

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

## `dex_Frailty`

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

## `dex_GNRI`

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

## `dex_GPS`

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

## `dex_HEI`

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

## `dex_HOMA`

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

## `dex_HSI`

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

## `dex_HeartAge`

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

## `dex_LAP`

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

## `dex_LC9`

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

## `dex_LE8`

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

## `dex_LS7`

```r
function (data, years, count = FALSE, component_score = FALSE, component_raw = FALSE, hei_version = 2010, 
    Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    d <- LS7_Michelle(years, hei_version, count, component_score, component_raw)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `dex_MAO`

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

## `dex_METS.IR`

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

## `dex_METS.VF`

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

## `dex_MHO`

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

## `dex_MMII`

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

## `dex_MQI`

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

## `dex_MgDS`

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

## `dex_Muscle.strength`

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

## `dex_NAFLD.LFS`

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

## `dex_NFS`

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

## `dex_NLR`

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

## `dex_NPS`

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

## `dex_OBS`

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

## `dex_PAiaf`

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

## `dex_PLF`

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

## `dex_PLR`

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

## `dex_PRAL.NEAP`

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

## `dex_PhysicalActivity`

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

## `dex_RecreationalActivity`

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

## `dex_SARC.F`

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

## `dex_SDoH`

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

## `dex_SHR`

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

## `dex_SII`

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

## `dex_Tasks.HomeYard`

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

## `dex_TyG`

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

## `dex_VAI`

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

## `dex_VAT`

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

## `dex_WHR`

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

## `dex_WHtR`

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

## `dex_WorkActivity`

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

## `dex_YJP`

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

## `dex_ZJU`

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

## `dex_body.fat.percentage`

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

## `dex_eGDR`

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

## `dex_eGFR`

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

## `dex_ePWV`

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

## `dex_fasting.time`

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

## `dex_fat.mass`

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

## `dex_fii`

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

## `dex_lean.mass`

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

## `dex_phenoAge`

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

## `dex_ulb`

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

## `dex_usFLI`

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

## `dex_walk_bicycle`

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

## `diag_ACO`

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

## `diag_ASCVD`

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

## `diag_Anemia`

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

## `diag_Asthma`

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

## `diag_CKD`

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

## `diag_CKM`

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

## `diag_COPD`

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

## `diag_CVD`

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

## `diag_DM`

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

## `diag_Familial.Hypercholesterolemia`

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

## `diag_Fibrillation`

```r
function (data, years, Year = FALSE, join = "left") 
{
    diag_icd10("fibril", data = data, colname = "Fibrillation", Year = Year, years = years)
}
```

## `diag_Hyperlipidemia`

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

## `diag_Hypertension`

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

## `diag_MAFLD`

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

## `diag_MAFLD.FLI`

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

## `diag_MAFLD.usFLI`

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

## `diag_MASLD.FLI`

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

## `diag_MASLD.cap`

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

## `diag_MASLD.usFLI`

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

## `diag_MetS`

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

## `diag_NAFLD`

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

## `diag_OSAS.3`

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

## `diag_OSAS.3a`

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

## `diag_OSAS.3ha`

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

## `diag_OSAS.MAP`

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

## `diag_Overactive.bladder`

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

## `diag_PAD`

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

## `diag_PHQ9`

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

## `diag_Parkinson`

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

## `diag_Pregnant`

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

## `diag_RMetS`

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

## `diag_Resistant.hypertension`

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

## `diag_Retinal.Emboli`

```r
function (data, years, Year = FALSE, join = "left") 
{
    years <- data_years(data, years)
    tsv <- nhs_tsv("opxret", cat = T)
    d <- nhs_read(tsv, "opddholl:left.eye", "opdsholl:right.eye", "opduholl:worse.eye", cat = F)
    return_data(data, d, Year, key = "seqn", join = join)
}
```

## `diag_alcohol.associated.liver.disease`

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

## `diag_alcohol.user`

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

## `diag_angina`

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

## `diag_arthritis`

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

## `diag_atopic`

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

## `diag_binge`

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

## `diag_congestive.heart.failure`

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

## `diag_coronary.heart.disease`

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

## `diag_epilepsy`

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

## `diag_heart.attack`

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

## `diag_hypoparathyroidism`

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

## `diag_icd10`

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

## `diag_infertility`

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

## `diag_mFried.frailty`

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

## `diag_osteoporosis`

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

## `diag_periodontitis`

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

## `diag_periodontitis_CDC.AAP`

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

## `diag_preDM`

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

## `diag_sarcopenia`

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

## `diag_sarcopenia_low.muscle`

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

## `diag_smoke`

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

## `diag_stroke`

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

## `diag_viral.hepatitis`

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

## `diag_youth.hypertension`

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

## `diag_youth.obesity`

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

## `digit2character`

```r
function (x, round = 2) 
{
    digital.i <- function(x, round) {
        if (is.numeric(x)) {
            ck <- is.na(x)
            x = janitor::round_half_up(x, round)
            x <- format(x, nsmall = round)
            x[ck] <- NA
            x
        }
        else {
            x
        }
    }
    if (any(is.data.frame(x), is.matrix(x))) {
        for (i in 1:ncol(x)) {
            ty <- tryCatch(digital.i(x[, i], round), error = function(e) NA)
            if (all(is.na(ty))) 
                (next)(i)
            x[, i] = ty
        }
        x
    }
    else {
        digital.i(x, round)
    }
}
```

## `digit2character<-`

```r
function (x, value) 
{
    digit2character(x, value)
}
```

## `digit2numeric`

```r
function (x, round = 2) 
{
    if (any(is.data.frame(x), is.matrix(x))) {
        for (i in 1:ncol(x)) {
            ty <- tryCatch(janitor::round_half_up(x[, i], round), error = function(e) NA)
            if (all(is.na(ty))) 
                (next)(i)
            x[, i] = ty
        }
        x
    }
    else {
        janitor::round_half_up(x, round)
    }
}
```

## `digit2numeric<-`

```r
function (x, value) 
{
    digit2numeric(x, value)
}
```

## `dii`

```r
function (component, x) 
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
    if (missing(component)) {
        df <- as.data.frame(t(data.frame(diitable, check.names = FALSE)))
        colnames(df) <- c("Overall inflammatory effect score", "Global daily mean intake(units/d)", "SD", 
            "Raw inflammatory effect score")
        return(df[, c(4, 1, 2, 3)])
    }
    if (!component %in% names(diitable)) {
        component <- select.list(names(diitable), multiple = FALSE, title = ifelse(do::cnOS(), tmcn::toUTF8("<U+8BF7><U+9009><U+62E9><U+4E00><U+4E2A><U+5BF9><U+5E94><U+7684><U+5E8F><U+53F7>,<U+7136><U+540E><U+6309><U+56DE><U+8F66><U+952E>"), 
            "Select one choice number"))
    }
    d <- diitable[[component]]
    (pnorm((x - d[2])/d[3]) * 2 - 1) * d[1]
}
```

## `distinct`

```r
function (.data, ..., .keep_all = FALSE) 
{
    UseMethod("distinct")
}
```

## `drop_col`

```r
function (x, ...) 
{
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

## `drop_col<-`

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

## `drop_row`

```r
function (x, ...) 
UseMethod("drop_row")
```

## `drop_row<-`

```r
function (x, value) 
{
    x <- drop_row(x, value)
    x
}
```

## `drop_row_high_percent`

```r
function (d, ..., percent = 97.5) 
{
    cols <- do::get_names(...)
    for (i in 1:length(cols)) {
        cutoff <- quantile(d[, cols[i]], percent[1]/100, na.rm = T)
        ck <- d[, cols[i]] < cutoff & !is.na(d[, cols[i]])
        d <- d[ck, ]
    }
    d
}
```

## `drop_row_low_percent`

```r
function (d, ..., percent = 2.5) 
{
    cols <- do::get_names(...)
    for (i in 1:length(cols)) {
        cutoff <- quantile(d[, cols[i]], percent[1]/100, na.rm = T)
        ck <- d[, cols[i]] > cutoff & !is.na(d[, cols[i]])
        d <- d[ck, ]
    }
    d
}
```

## `drug_anti.Diabetic`

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

## `drug_anti.Hyperlipidemic`

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

## `drug_anti.Hypertensive`

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

## `drug_anti.infectives`

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

## `drug_anti.parkinson`

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

## `drug_fibrates`

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

## `drug_niacin`

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

## `drug_search`

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

## `each_id_first_row`

```r
function (data = NULL, ...) 
{
    ids <- c(...)
    ids <- paste0_columns(data[, ids, drop = F])
    ck <- duplicated(ids)
    data[!ck, ]
}
```

## `each_id_last_row`

```r
function (data = NULL, ...) 
{
    ids <- c(...)
    ids <- paste0_columns(data[, ids, drop = F])
    ck <- rev(duplicated(rev(ids)))
    data[!ck, ]
}
```

## `fndds_AddFoodDesc`

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

## `fndds_DerivDesc`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "DerivDesc", Year = Year, join = join)
}
```

## `fndds_FNDDSIngred`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FNDDSIngred", Year = Year, join = join)
}
```

## `fndds_FNDDSNutVal`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FNDDSNutVal", Year = Year, join = join)
}
```

## `fndds_FoodPortionDesc`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodPortionDesc", Year = Year, join = join)
}
```

## `fndds_FoodSubcodeLinks`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodSubcodeLinks", Year = Year, join = join)
}
```

## `fndds_FoodWeights`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "FoodWeights", Year = Year, join = join)
}
```

## `fndds_IngredNutVal`

```r
function (data, years, Year = FALSE, join = "left") 
{
    drop_col(db_fndds(data = data, years = years, files = "IngredNutVal", Year = Year, join = join), 
        "nutrient.value.source", "sr.28.derivation.code", "sr.28.addmod.year")
}
```

## `fndds_MainFoodDesc`

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

## `fndds_MoistAdjust`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "MoistAdjust", Year = Year, join = join)
}
```

## `fndds_NutDesc`

```r
function (data, years, Year = FALSE, join = "left") 
{
    drop_col(db_fndds(data = data, years = years, files = "NutDesc", Year = Year, join = join), "tagname", 
        "decimals")
}
```

## `fndds_SubcodeDesc`

```r
function (data, years, Year = FALSE, join = "left") 
{
    db_fndds(data = data, years = years, files = "SubcodeDesc", Year = Year, join = join)
}
```

## `fndds_comp.food.Desc`

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

## `fndds_comp.food.Portion.Weight`

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

## `fndds_comp.nutrients`

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

## `fndds_download`

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

## `fndds_file_colnames`

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

## `fndds_file_names`

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

## `fndds_food.code`

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

## `fndds_tsv`

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

## `food.code_used`

```r
function (d) 
{
    attr(d, "food.code")
}
```

## `forestplot`

```r
function (x, ...) 
UseMethod("forestplot")
```

## `fped_download`

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

## `fped_occasion`

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

## `fped_read`

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

## `freq_count`

```r
function (design, x, by = NULL, value = FALSE, per = FALSE, remove.name = FALSE, remove.suffix = FALSE, 
    round = 2, file = NULL) 
{
    if (length(x) > 1) 
        stop("x must be one")
    if (inherits(design, "survey.design")) 
        design <- design$variables
    if (is.null(by)) {
        r <- table(design[, x], useNA = "i")
        r <- as.data.frame(r)
        r$per <- digit2character(r[, 2]/sum(r[, 2], na.rm = TRUE), round)
        colnames(r) <- c(x, "n", "per")
    }
    else {
        direction <- "h"
        if (length(by) == 1) {
            design$newbyby <- design[, by]
        }
        else if (length(by) > 1) {
            design$newbyby <- do::paste0_columns(design[, by], "~~~~~")
        }
        r <- as.data.frame(table(x = design[, x], by = design[, "newbyby"]))
        r$x <- paste0(x, "-", r$x)
        if (!is.null(levels(design[, x]))) 
            r$x <- factor(r$x, levels = paste0(x, "-", levels(design[, x])))
        r <- cbind(do::col_split(r$by, "~~~~~", colnames = by), r[, -2])
        for (i in by) {
            if (!is.null(levels(design[, i]))) {
                r[, i] <- factor(r[, i], levels = levels(design[, i]))
            }
        }
        r <- eval(parse(text = sprintf("reshape2::dcast(r,%s~x,value.var = 'Freq')", paste0(by, collapse = " + "))))
        r2 <- r
        colnames(r2)[-c(1:length(by))] <- paste0(colnames(r2)[-c(1:length(by))], "_per")
        if (direction == "h") {
            for (i in 1:nrow(r2)) {
                r2[i, -c(1:length(by))] <- r2[i, -c(1:length(by))]/row.sums(r2[i, -c(1:length(by))])
            }
        }
        else if (direction == "v") {
            for (i in (length(by) + 1):ncol(r2)) {
                r2[, i] <- r2[, i]/col.sums(r2[, i, drop = FALSE])
            }
        }
        r <- cbind(r, r2[, -c(1:length(by))])
        digit2character(r) <- round
        if (!value) {
            ck <- !colnames(r) %in% unlist(lapply(x, function(i) paste0(i, "-", unique_no.NA(design[, 
                i]))))
            ck[1:length(by)] <- TRUE
            r <- r[, ck, drop = FALSE]
        }
        if (!per) {
            ck <- do::right(colnames(r), 4) != "_per"
            ck[1:length(by)] <- TRUE
            r <- r[, ck, drop = FALSE]
        }
        else {
            if (remove.suffix) 
                colnames(r) <- do::reverse(sub("rep_", "", do::reverse(colnames(r))))
        }
        if (remove.name) 
            colnames(r) <- sub(paste0(x, "-"), "", colnames(r))
    }
    if (!is.null(file)) {
        file <- ifelse(tolower(do::right(file, "5")) == ".xlsx", file, paste0(file, ".xlsx"))
        openxlsx::write.xlsx(r, file)
    }
    r
}
```

## `freq_mean`

```r
function (design, x, by = NULL, value = FALSE, sd = FALSE, low.high = FALSE, ci = FALSE, meanPMsd = FALSE, 
    meanSQsd = FALSE, round = 2, na.rm = TRUE) 
{
    if (inherits(design, "survey.design")) 
        design <- design$variables
    if (is.null(by)) {
        r <- ci.no.by(design, x, round)
        if (!value) 
            r <- drop_col(r, "mean")
        if (!sd) 
            r <- drop_col(r, "sd")
        if (!low.high) 
            r <- drop_col(r, c("low", "high"))
        if (!ci) 
            r <- drop_col(r, "ci")
        if (!meanPMsd) 
            r <- drop_col(r, "meanPMsd")
        if (!meanSQsd) 
            r <- drop_col(r, "meanSQsd")
        return(r)
    }
    else {
        r <- ci_by(design, x, by, round = round)
        if (!value) 
            r <- drop_col(r, x)
        if (!sd) 
            r <- drop_col(r, paste0(x, "_sd"))
        if (!low.high) 
            r <- drop_col(r, c(paste0(x, "_low"), paste0(x, "_high")))
        if (!ci) 
            r <- drop_col(r, paste0(x, "_ci"))
        if (!meanPMsd) 
            r <- drop_col(r, paste0(x, "_meanPMsd"))
        if (!meanSQsd) 
            r <- drop_col(r, paste0(x, "_meanSQsd"))
        return(r)
    }
}
```

## `getChangepoints`

```r
function (r, range = NULL) 
UseMethod("getChangepoints")
```

## `getKnot`

```r
function (fit) 
{
    rcstxt <- do::Replace0(fit$call$formula %>% deparse() %>% paste0(collapse = "") %>% do::Replace("r {0,}c {0,}s {0,}", 
        "rcs") %>% do::Replace0(" "), ".*[~+]rcs\\(", "\\).*", "\\+.*")
    if (grepl(",", rcstxt)) {
        as.numeric(do::Replace0(rcstxt, ".*,"))
    }
    else {
        not <- c(paste0(rcsx(fit), ""), paste0(rcsx(fit), "'"), paste0(rcsx(fit), do::rep_n("'", 2)), 
            paste0(rcsx(fit), do::rep_n("'", 3)), paste0(rcsx(fit), do::rep_n("'", 4)), paste0(rcsx(fit), 
                do::rep_n("'", 5)), paste0(rcsx(fit), do::rep_n("'", 6)), paste0(rcsx(fit), do::rep_n("'", 
                7)), paste0(rcsx(fit), do::rep_n("'", 8)), paste0(rcsx(fit), do::rep_n("'", 9)), paste0(rcsx(fit), 
                do::rep_n("'", 10)))
        not
        which.min(not %in% names(fit$coefficients))
    }
}
```

## `getReference`

```r
function (r) 
UseMethod("getReference")
```

## `get_config_items`

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

## `get_config_path`

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

## `get_config_years`

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

## `get_mort_path`

```r
function () 
{
    paste0(get_config_path(TRUE), "mort/")
}
```

## `group_mean`

```r
function (d, vars = NULL, bys = NULL) 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    vars[!grepl(":", vars)] <- paste0(vars[!grepl(":", vars)], ":", vars[!grepl(":", vars)])
    v <- sprintf("%s = mean(%s,na.rm=T)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `highlight`

```r
function (x, ..., colors = NULL) 
{
    if (is.null(colors)) 
        colors = c("#FFFF0080", "#00FF0033", "#DEA28280", "#FF000080", "#C1C3EE80", "#C08BED80", "#7CF14180", 
            "#E6EDDD80", "#8A5DB280", "#953BAE80", "#69EA9D80", "#888FAE80", "#4858E480", "#AAE0BE80", 
            "#ADAA9F80", "#E2DE7E80", "#E1969D80", "#D765A380", "#67CBE680", "#5E1C9580", "#AD3DDE80", 
            "#A565EE80", "#6FB32F80", "#BAD7E280", "#535B9980", "#E197DE80", "#E366E880", "#A89BE480", 
            "#CDEC3480", "#DECF4280", "#E7C6D780", "#CF55B380", "#70B2E380", "#D2C79180", "#8CE46E80", 
            "#DC562F80", "#F287EF80", "#E6EFB880", "#C8E97180", "#D8825180", "#8238EA80", "#E43B9180", 
            "#89C27980", "#E4B3E380", "#EA456E80", "#EBC5B680", "#50A27B80", "#707BE680", "#E7AD4F80", 
            "#5C94E680", "#E23AC580", "#56696380", "#E2706C80", "#59EBEC80")
    (first <- tmcn::toUTF8("<U+9B51>"))
    (mid <- tmcn::toUTF8("<U+9B45>"))
    (last <- tmcn::toUTF8("<U+9B49>"))
    hl <- unique(c(...))
    if (length(hl) == 0) {
        if (!is.atomic(x)) {
            if (do::cnOS()) 
                stop(tmcn::toUTF8("<U+6CA1><U+6709><U+6307><U+5B9A><U+9AD8><U+4EAE><U+5BF9><U+8C61>,<U+53EA><U+80FD><U+9AD8><U+4EAE><U+5411><U+91CF>"))
            if (!do::cnOS()) 
                stop("No highlighted object is specified, only vectors can be highlighted")
        }
        hl <- unique(x)
    }
    if (any(hl %in% c(first, mid, last))) 
        stop("can not highlight", paste0(hl[hl %in% c(first, mid, last)], collapse = ", "))
    rk <- order(nchar(hl), decreasing = TRUE)
    hl <- hl[rk]
    plt <- colors[seq_len(length(hl))]
    plt <- plt[rk]
    (ck <- is.atomic(x))
    if (ck) {
        x <- x[!is.na(x)]
        do::Replace(do::Replace(do::Replace(add_color_to_text(x, hl, plt), first, "<span style=\"background-color:"), 
            mid, "\">"), last, "</span>")
    }
    else {
        x1 <- paste0_columns(x, "---------")
        x2 <- do::col_split(do::Replace(do::Replace(do::Replace(add_color_to_text(x1, hl, plt), first, 
            "<span style=\"background-color:"), mid, "\">"), last, "</span>"), "---------", colnames = colnames(x))
        x2
    }
}
```

## `html_URL`

```r
function (x, href = NULL, name = NULL, target = "new") 
{
    if (do::left_equal(target, "new")) {
        target = "_blank"
        if (!is.null(href) & is.null(name)) {
            sprintf("<a href=\"%s\" target=\"%s\">%s</a>", href, target, x)
        }
        else if (is.null(href) & !is.null(name)) {
            sprintf("<a href=\"#%s\">%s</a>", name, x)
        }
        else if (!is.null(href) & !is.null(name)) {
            sprintf("<a href=\"%s#%s\" target=\"%s\">%s</a>", href, name, target, x)
        }
    }
    else {
        if (!is.null(href) & is.null(name)) {
            sprintf("<a href=\"%s\">%s</a>", href, x)
        }
        else if (is.null(href) & !is.null(name)) {
            sprintf("<a href=\"#%s\">%s</a>", name, x)
        }
        else if (!is.null(href) & !is.null(name)) {
            sprintf("<a href=\"%s#%s\">%s</a>", href, name, x)
        }
    }
}
```

## `ifel`

```r
function (...) 
{
    vn <- names(rlang::list2(...))[-1]
    gtn <- do::get_names(...)[-1]
    d1 <- list(...)[[1]]
    if (is.data.frame(d1) | is.matrix(d1)) {
        st <- sapply(1:length(gtn), function(i) {
            (gt <- capture.output(cat(gtn[i])))
            gt <- gt[!gt %in% c("{", "}")]
            sprintf("%s = case_when( %s)", vn[i], paste0(gt, collapse = ", \n"))
        }) %>% paste0(collapse = ", \n")
        eval(parse(text = sprintf("d1 |> mutate(%s)", st)))
    }
    else {
        d1 <- data.frame(d1) %>% do::give_names(gtn[n1])
        d1 <- eval(parse(text = sprintf("d1 |> mutate(xxx=case_when(%s))", paste0(gtn[n2], collapse = ","))))
        d1$xxx
    }
}
```

## `inset_both_frame`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'[ , ]')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `inset_both_square`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'( , )')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `inset_exact_match`

```r
function () 
{
    rstudioapi::insertText(text = " %=% ")
}
```

## `inset_left_frame`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'[ , )')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `inset_left_square`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'( , ]')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `inset_right_frame`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'( , ]')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `inset_right_square`

```r
function () 
{
    context <- rstudioapi::getActiveDocumentContext()
    start_line <- context$selection[[1]]$range$start[[1]]
    start_char <- context$selection[[1]]$range$start[[2]]
    rstudioapi::insertText(text = "bu( ,'[ , )')")
    rstudioapi::setCursorPosition(position = c(start_line, start_char + 3), id = NULL)
}
```

## `ip_analysis`

```r
function (fit, ip = NULL, round = 3, xlsx = NULL) 
{
    if (is.null(ip)) 
        stop("<U+5FC5><U+987B><U+6307><U+5B9A><U+5207><U+70B9>ip")
    (rcsx <- rcsx(fit))
    if (length(rcsx) == 0) 
        stop("<U+6A21><U+578B><U+4E2D><U+6CA1><U+6709><U+8FDB><U+884C>rcs")
    f0 <- delete_variable_rcs_keepx(fit)
    (rg <- reg_table(f0, round = round, x = rcsx, view = F))
    (p0 <- rg[, grepl("p", colnames(rg), T)])
    (ci0 <- rg[, grepl("95", colnames(rg))] %>% do::Replace0(" "))
    .ip_analysis.ip <<- ip
    (f1 <- suppressWarnings(eval(parse(text = sprintf("update(f0,subset=(%s < .ip_analysis.ip) & !is.na(%s))", 
        rcsx, rcsx)))))
    (rg <- reg_table(round = round, f1, x = rcsx, view = F))
    (p1 <- rg[, grepl("p", colnames(rg), T)] %>% do::Replace0(" "))
    (ci1 <- rg[, grepl("95", colnames(rg))] %>% do::Replace0(" "))
    (f2 <- suppressWarnings(eval(parse(text = sprintf("update(f0,subset=(%s >= .ip_analysis.ip) & !is.na(%s))", 
        rcsx, rcsx)))))
    (rg <- reg_table(round = round, f2, x = rcsx, view = F))
    (p2 <- rg[, grepl("p", colnames(rg), T)] %>% do::Replace0(" "))
    (ci2 <- rg[, grepl("95", colnames(rg))] %>% do::Replace0(" "))
    (nhsnm <- deparse(fit$call$design))
    nhs2 <- tryCatch(get(nhsnm, envir = .GlobalEnv), error = function(e) eval(parse(text = nhsnm)))
    nhs2$variables$inntteeraacctt <- ifelse(nhs2$variables[, rcsx] < ip, "p1", "p2")
    eval(parse(text = sprintf("%s <<- nhs2", nhsnm)))
    fit_act <- f0 %>% delete_variable(vars = rcsx) %>% add_variable(vars = paste0(rcsx, "*inntteeraacctt"))
    f01 <- f0 %>% add_variable(vars = "inntteeraacctt")
    anv <- suppressWarnings(tryCatch(anova(f01, fit_act), error = function(e) "e"))
    if (is.character(anv)) {
        if (all(anv == "e")) {
            anv <- anova(f01, fit_act, test = "Chisq")
        }
    }
    ipres <- data.frame(variable = c("standard regression", "two-piecewise regression", sprintf("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s < IP", 
        rcsx), sprintf("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s <U+2265> IP", rcsx), "p for Log-likelihood ratio"), 
        value = c(paste0(ci0, " ", p0), paste0("IP = ", round(ip, round)), paste0(ci1, " ", p1), paste0(ci2, 
            " ", p2), pvalue.format(anv$p, round)))
    print(html_table(ipres))
    if (!is.null(xlsx)) {
        x <- ipres
        x$variable <- do::Replace(x$variable, "&nbsp;", " ")
        openxlsx::write.xlsx(x, xlsx)
    }
    invisible(ipres)
}
```

## `live_microbes_table`

```r
function () 
{
    intake_of_live_microbes
}
```

## `look`

```r
function (x, ..., ignore.case = FALSE) 
{
    if (is.data.frame(x)) {
        ck <- lookl(x = x, ..., ignore.case = ignore.case)
        x[ck, ]
    }
    else {
        x[lookl(x = x, ..., ignore.case = ignore.case)]
    }
}
```

## `lookl`

```r
function (x, ..., ignore.case = TRUE, NA2false = FALSE) 
{
    if (is.data.frame(x)) 
        x <- paste0_columns(x, ";")
    looki(x = x, ..., ignore.case = ignore.case, NA2false = NA2false)
}
```

## `matchit4design`

```r
function (design, matchit) 
{
    if ("matchit" %in% class(matchit)) 
        matchit <- MatchIt::match.data(matchit)
    ck <- (1:nrow(nhs)) %in% matchit$xrxoxwnxuxbxmxexr
    subset(design, ck)
}
```

## `md.pattern`

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

## `md.value`

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

## `mdb_files`

```r
function (mdb) 
{
    if (do::is.windows()) {
        exe <- sprintf(list.files(system.file("data", package = "nhanesR"), "tables.exe", full.names = TRUE), 
            fmt = "\"%s\"")
        mdb <- sprintf("\"%s\"", mdb)
        do::list1(strsplit(do::Trim(system(paste(exe, mdb), intern = TRUE)), " "))
    }
    else {
        mdbr::mdb_tables(mdb)
    }
}
```

## `missForest2`

```r
function (d, ntree = 5, seed = 1) 
{
    code <- list()
    set.seed(seed)
    for (i in colnames(d)) {
        if (is.character(d[, i])) {
            (lvs <- do::increase(do::complete.data(unique(d[, i]))))
            d[, i] <- factor(d[, i], levels = lvs)
            code[[length(code) + 1]] <- list(class = "character_go_back", col = i)
        }
        else if (any(class(d[, i]) %in% "POSIXct")) {
            code[[length(code) + 1]] <- list(class = "column", col = i, lvs = d[, i])
            d[, i] <- NULL
        }
        else if (anyNA(d[, i]) & length(do::complete.data(unique(d[, i]))) <= 5 & all(do::complete.data(unique(d[, 
            i])) %in% (0:10000))) {
            d[, i] <- factor(d[, i], levels = do::complete.data(unique(d[, i])))
            code[[length(code) + 1]] <- list(class = "integer_go_back", col = i)
        }
    }
    d <- missForest::missForest(d, ntree = ntree)$ximp
    for (i in 1:length(code)) {
        di <- code[[i]]
        if (di$class == "character_go_back") {
            d[, di$col] <- as.character(d[, di$col])
        }
        else if (di$class == "column") {
            d[, di$col] <- di$lvs
        }
        else if (di$class == "integer_go_back") {
            d[, di$col] <- as.numeric(as.character(d[, di$col]))
        }
    }
    d
}
```

## `missValue`

```r
function (data, ...) 
{
    if ("survey.design" %in% class(data)) 
        data <- data$variables
    r <- do::give_names(data.frame(sapply(data, function(i) sum(is.na(i)))), "n")
    r$percent <- round(r$n/nrow(data) * 100, 2)
    r$total <- nrow(data)
    ft <- c(...)
    if (is.null(ft)) 
        return(r)
    r[lookl(row.names(r), ...), ]
}
```

## `mort_download`

```r
function () 
{
    html <- xml2::read_html("https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datalinkage/linked_mortality/")
    mortdf <- do::col_split(do::Replace(do::Replace(do::Replace0(do::Trim(set::grep_not_and(set::grep_and(do::list1(strsplit(as.character(rvest::html_elements(html, 
        xpath = "//pre")), "<br>|<pre>")), "NHANES"), "NHANES_III")), "</a>", "href=\\\""), " {0,}<a {0,}", 
        "<a"), " {0,}\\\"> {0,}", "\\\">"), c("<a", "\">"), colnames = c("update", "href", "filename"))
    mortdf$href <- paste0("https://ftp.cdc.gov", mortdf$href)
    mortdf <- mortdf[!grepl("_MORT_2015_PUBLIC.dat", mortdf$filename), ]
    mortdir <- paste0(get_config_path(), "/mort")
    mortdf$filename <- paste0(mortdir, "/", tolower(mortdf$filename))
    if (!dir.exists(mortdir)) 
        dir.create(mortdir, recursive = TRUE)
    for (i in 1:nrow(mortdf)) {
        if (i == 1) {
            cat(crayon::red("Download mortality data: ", nrow(mortdf)), "\n")
        }
        cat(do::file.name(mortdf$filename[i]), "\n")
        nullcon <- file(nullfile(), open = "wb")
        sink(nullcon, type = "message")
        wait <- TRUE
        while (wait) {
            download <- tryCatch(download.file(mortdf$href[i], destfile = mortdf$filename[i], quiet = FALSE, 
                mode = "wb"), error = function(e) "e", warning = function(w) "w")
            wait <- ifelse(download == "e" | download == "w", TRUE, FALSE)
        }
        sink(type = "message")
        close(nullcon)
        if (!wait) {
            dsn <- as.data.frame(readr::read_fwf(file = mortdf$filename[i], col_types = "ciiiiiiiddii", 
                readr::fwf_cols(publicid = c(1, 14), eligstat = c(15, 15), mortstat = c(16, 16), ucod_leading = c(17, 
                  19), diabetes = c(20, 20), hyperten = c(21, 21), dodqtr = c(22, 22), dodyear = c(23, 
                  26), wgt_new = c(27, 34), sa_wgt_new = c(35, 42), permth_int = c(43, 45), permth_exm = c(46, 
                  48)), na = c("", "."), progress = FALSE))
            colnames(dsn)[1] <- "seqn"
            df <- drop_col(dsn, c("dodqtr", "dodyear", "wgt_new", "sa_wgt_new"))
            file <- do::Replace(mortdf$filename[i], "\\.dat.*", ".tsv")
            write.table(df, file, sep = "\t", row.names = FALSE)
        }
    }
    cat("\n")
    mort_varLabel()
    mort_codebook()
    cat("create varLabel file\n")
    cat("create codebook file\n")
}
```

## `mort_read`

```r
function (years, varLabel = FALSE, codebook = TRUE) 
{
    (years <- do::Replace(prepare_years(years), "-", "_"))
    tsv <- set::grep_or(list.files(get_mort_path(), pattern = "tsv", full.names = TRUE), years)
    if (length(tsv) == 0) {
        cat("Invalid years:", paste0(years, collapse = ", "), "\n")
        return()
    }
    ck <- !sapply(years, function(i) any(grepl(i, tsv)))
    if (any(ck)) {
        cat("Invalid years:", paste0(years[ck], collapse = ", "), "\n")
    }
    df <- do.call(lapply(tsv, function(i) {
        data.table::fread(i, showProgress = FALSE, data.table = FALSE)
    }), what = plyr::rbind.fill)
    if (codebook) {
        cd <- read.delim(paste0(get_mort_path(), "mortality.codebook"))
        for (i in 1:ncol(df)) {
            if (colnames(df)[i] %in% cd$variable) {
                ck <- cd[, "variable"] == colnames(df)[i]
                head(cd)
                df[, i] <- Recode(df[, i], paste0(cd[ck, "code"], "::", cd[ck, "label"]))
            }
        }
    }
    if (varLabel) {
        vl <- read.delim(paste0(get_mort_path(), "mortality.varLabel"))
        df <- eval(parse(sprintf(paste0(sprintf("\"%s\" = \"%s\"", vl$variable, vl$label), collapse = ", "), 
            fmt = "expss::apply_labels(df,%s)"), file = "", n = NULL))
    }
    df
}
```

## `multibyteString`

```r
function (tsv) 
{
    tsv0 <- do::knife_right(tsv, "3")
    varlabel <- paste0(tsv0, "varLabel")
    codbook <- paste0(tsv0, "codebook")
    for (i in varlabel) {
        cat("\n", i)
        d <- read.delim(i, comment.char = "#", encoding = "UTF-8")
        for (j in d) {
            x <- tolower(j)
        }
    }
    for (i in codbook) {
        cat("\n", i)
        d <- data.table::fread(i, data.table = FALSE, encoding = "UTF-8")
        for (j in d) {
            x <- tolower(j)
        }
    }
    for (i in tsv) {
        cat("\n", i)
        d <- data.table::fread(i, data.table = FALSE, encoding = "UTF-8")
        for (j in d) {
            x <- tolower(j)
        }
    }
    invisible()
}
```

## `newVb`

```r
function (df, ...) 
{
    ll <- list(...)
    (Vbloc <- which(sapply(ll, class) == "character"))
    (Vbname <- as.character(ll[Vbloc]))
    (start <- Vbloc + 1)
    (end <- c(Vbloc[-1] - 1, length(ll)))
    st <- sapply(1:length(start), function(i) {
        (form <- ll[start[i]:end[i]])
        st <- sprintf("%s = case_when(%s)", Vbname[i], paste0(as.character(form), collapse = ", "))
    }) %>% paste0(collapse = ",")
    (st2 <- sprintf("mutate(df,%s)", st))
    eval(parse(text = st2))
}
```

## `nhanesR_startup_check`

```r
function () 
{
    cat("Not check: options(nhanesR_check=FALSE)")
}
```

## `nhs.pubmed`

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

## `nhs.pubmed_title`

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

## `nhs_Connect`

```r
function (user = "postgres", password = "pg", dbname = "nhanes", host = "localhost", port = 5432, ...) 
{
    conn <- DBI::dbConnect(RPostgreSQL::PostgreSQL(), user = user, password = password, host = host, 
        port = port)
    datname <- as.data.frame(dplyr::tbl(conn, dbplyr::sql("SELECT datname FROM pg_database")))[, 1]
    if (!"nhanes" %in% tolower(datname) & dbname == "nhanes") {
        message("\ncreate database nhanes")
        DBI::dbGetQuery(conn = conn, statement = "CREATE DATABASE nhanes;")
    }
    conn <- DBI::dbConnect(RPostgreSQL::PostgreSQL(), user = user, password = password, host = host, 
        port = port, dbname = dbname, ...)
    dbplyr::src_dbi(con = conn, auto_disconnect = TRUE)
}
```

## `nhs_DOC`

```r
function (tsv) 
{
    (years <- prepare_years(tsv))
    years[years == "2019-2020"] <- "2017-2018"
    (items <- prepare_items(tsv))
    (files <- do::Replace(do::file.name(tsv), c("\\.tsv", "\\.varLabel"), "\\.htm"))
    (url <- sprintf("https://wwwn.cdc.gov/Nchs/Nhanes/%s/%s", years, files))
    for (i in url) {
        browseURL(i)
    }
}
```

## `nhs_Upload`

```r
function (files, conn) 
{
    if (missing(conn)) 
        conn <- get("nhs_Connect", envir = .GlobalEnv)
    (years <- list.files(get_config_path()))
    for (i in years) {
        statement <- sprintf("CREATE SCHEMA IF NOT EXISTS \"%s\"", i)
        DBI::dbGetQuery(conn = conn$con, statement = statement)
    }
    if (missing(files)) 
        files <- nhs_tsv()
    if (length(files) == 0) {
        if (do::cnOS()) 
            stop(get_config_path(), tmcn::toUTF8(" <U+8DEF><U+5F84><U+4E0B><U+6CA1><U+6709>tsv<U+6587><U+4EF6>"))
        if (!do::cnOS()) 
            stop(get_config_path(), " has no tsv files")
    }
    pb <- txtProgressBar(max = length(files), width = 30, style = 3)
    for (i in 1:length(files)) {
        filei <- files[i]
        yeari <- prepare_years(filei)
        (tbl <- paste0(prepare_items(filei), "---", do::Replace0(do::file.name(filei), "\\.tsv")))
        x <- data.table::fread(filei, check.names = FALSE, showProgress = FALSE)
        DBI::dbWriteTable(conn = conn$con, name = c(yeari, tbl), value = x, overwrite = TRUE, row.names = FALSE)
        setTxtProgressBar(pb, i)
    }
    message("\nDONE !!! ")
}
```

## `nhs_brief`

```r
function (...) 
UseMethod("nhs_brief")
```

## `nhs_browse`

```r
function (years, items, open = TRUE) 
{
    if (do::cnOS()) {
        misys <- tmcn::toUTF8("<U+6307><U+5B9A>items<U+7684><U+65F6><U+5019>,<U+5FC5><U+987B><U+6307><U+5B9A>years")
        itemswrong <- tmcn::toUTF8("items<U+6307><U+5B9A><U+4E0D><U+5BF9>,<U+5FC5><U+987B><U+8981><U+662F><U+4E0B><U+5217><U+503C>: ")
    }
    else {
        misys <- "years must be given when items is specified."
        itemswrong <- "items is wrong, which should be as follows: "
    }
    years <- do::Replace0(prepare_years(years), "-.*")
    years[years == "2019"] <- "2017-2020"
    if (missing(years) & missing(items)) {
        if (open) 
            browseURL("https://wwwn.cdc.gov/nchs/nhanes/")
        if (!open) 
            "https://wwwn.cdc.gov/nchs/nhanes/"
    }
    else if (!missing(years) & missing(items)) {
        urls <- c()
        for (i in years) {
            urls <- c(urls, sprintf("https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?%s=%s", 
                ifelse(i == "2017-2020", "Cycle", "CycleBeginYear"), i))
        }
        if (open) 
            for (i in urls) browseURL(i)
        if (!open) 
            urls
    }
    else if (!missing(years) & !missing(items)) {
        items <- prepare_items(items)
        if (length(items) == 0) 
            stop(itemswrong, paste0(get_config_items(), collapse = ", "))
        urls <- c()
        for (i in years) {
            for (j in items) {
                urls <- c(urls, sprintf("https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=%s&%s=%s", 
                  j, ifelse(i == "2017-2020", "Cycle", "CycleBeginYear"), i))
            }
        }
        if (open) 
            for (i in urls) browseURL(i)
        if (!open) 
            urls
    }
    else if (missing(years) & !missing(items)) {
        items <- prepare_items(items)
        if (length(items) == 0) 
            stop(itemswrong, paste0(get_config_items(), collapse = ", "))
        urls <- c()
        for (i in years) {
            for (j in items) {
                urls <- c(urls, sprintf("https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=%s&%s=%s", 
                  j, ifelse(i == "2017-2020", "Cycle", "CycleBeginYear"), i))
            }
        }
        if (open) 
            for (i in urls) browseURL(i)
        if (!open) 
            urls
    }
}
```

## `nhs_check`

```r
function (years, items) 
{
    (years <- prepare_years(years))
    (items <- prepare_items(items))
    (dt <- rep(items, each = length(years)))
    (ys <- rep(years, length(items)))
    fmt <- paste0(get_config_path(), "/%s/%s")
    (nhs_dir <- do::increase(sprintf(fmt, ys, dt)))
    ext <- c("\\.codebook", "\\.varLabel", "\\.tsv", "\\.update", "\\.xpt", "\\.sas7bdat")
    for (i in 1:length(nhs_dir)) {
        error = 1
        (yeari <- prepare_years(nhs_dir[i]))
        (itemi <- prepare_items(nhs_dir[i]))
        if (i == 1) {
            cat("\n", yeari)
        }
        else {
            (yeari1 <- prepare_years(nhs_dir[i - 1]))
            if (yeari != yeari1) 
                cat("\n", yeari)
        }
        fn <- unique(do::Replace0(list.files(nhs_dir[i], paste0(ext, collapse = "|")), ext))
        fn
        j = which(fn == "dsbi")
        if (length(fn) == 0) 
            (next)(i)
        for (j in 1:length(fn)) {
            fnj <- fn[j]
            len <- sum(list.files(nhs_dir[i]) %in% do::Replace0(paste0(fnj, ext), "\\\\"))
            len
            if (len == 5) 
                (next)(j)
            if (i == 1) {
                cat("\n     ", itemi)
            }
            else {
                (itemi1 <- prepare_items(nhs_dir[i - 1]))
                if (itemi != itemi1) {
                  if (error == 1) {
                    error = 2
                    cat("\n     ", itemi)
                  }
                }
            }
            cat(crayon::green(paste0("\n          ", fnj, " ", len)))
        }
    }
}
```

## `nhs_codebook`

```r
function (..., tolower = FALSE) 
{
    x <- list(...)
    if (length(x) == 0) 
        return(nhs_codebook.character(character()))
    (ckdf <- sapply(x, class) == "data.frame")
    (cklist <- sapply(x, class) == "list")
    (ckpath <- sapply(x, function(i) any(grepl(get_config_path(), i, ignore.case = TRUE))))
    if (any(ckdf)) {
        files <- x[ckdf]
        other <- x[!(ckdf | cklist | ckpath)]
        variable <- unique(tolower(unlist(lapply(other, function(i) i[!grepl(get_config_path(), i, ignore.case = TRUE)]))))
        do.call(lapply(files, function(i) nhs_codebook.dataframe(variable, i, tolower)), what = rbind)
    }
    else if (any(ckpath)) {
        (files <- unique(unlist(x[ckpath])))
        (other <- x[!(ckdf | cklist | ckpath)])
        variable <- unique(tolower(unlist(lapply(other, function(i) i[!grepl(get_config_path(), i, ignore.case = TRUE)]))))
        nhs_codebook.character(variable, files, tolower)
    }
    else if (!any(ckpath)) {
        files <- nhs_files_pc(file_ext = "codebook")
        other <- x[!(ckdf | cklist | ckpath)]
        variable <- unique(tolower(unlist(lapply(other, function(i) i[!grepl(get_config_path(), i, ignore.case = TRUE)]))))
        nhs_codebook.character(variable, files, tolower)
    }
    else if (!any(cklist)) {
        files <- x[cklist]
        other <- x[!(ckdf | cklist | ckpath)]
        variable <- unique(tolower(unlist(lapply(other, function(i) i[!grepl(get_config_path(), i, ignore.case = TRUE)]))))
        lapply(files, function(i) do.call(lapply(files, function(j) do.call(nhs_codebook.dataframe(variable, 
            j, tolower), what = rbind)), what = rbind))
    }
}
```

## `nhs_colnames`

```r
function (..., brief = FALSE) 
UseMethod("nhs_colnames")
```

## `nhs_copy`

```r
function (dir) 
{
    (dir <- do::formal_dir(dir))
    from <- list.files(dir, recursive = TRUE, full.names = TRUE)
    for (i in 1:length(from)) {
        (to <- paste0(get_config_path(), do::knife_left(from[i], nchar(dir))))
        todir <- do::file.dir(to)
        if (!dir.exists(todir)) 
            dir.create(todir, showWarnings = F, recursive = T)
        cat(file.copy(from[i], to, overwrite = TRUE))
        cat(" ")
    }
}
```

## `nhs_docFile_pc`

```r
function (..., items, years, open = FALSE) 
{
    file_ext = "update"
    (years <- prepare_years(years))
    (items <- prepare_items(items))
    (d1 <- paste0(get_config_path(), "/", years, "/"))
    (d2 <- lapply(d1, function(i) paste0(i, items)))
    (d3 <- do.call(c, d2))
    f1 <- list.files(path = d3, full.names = TRUE)
    ck <- tools::file_ext(f1) %in% file_ext
    (f2 <- f1[ck])
    pattern <- c(...)
    if (is.null(pattern)) {
        if (length(f2) > 0) {
            url <- sapply(f2, function(i) read.delim(i, comment.char = "#", check.names = FALSE)[1, "DOC  url"])
            names(url) <- NULL
            if (open) {
                for (i in url) browseURL(i)
                return(url)
            }
            else {
                return(url)
            }
        }
        else {
            return()
        }
    }
    fn <- paste0(do::Replace0(do::file.name(f2), "\\.tsv"), ".")
    ck <- lookl(x = fn, ..., ignore.case = TRUE)
    docfile <- f2[ck]
    if (length(docfile) > 0) {
        url <- sapply(docfile, function(i) read.delim(i, comment.char = "#")[1, "DOC  url"])
        names(url) <- NULL
        if (open) {
            for (i in url) browseURL(i)
            return(url)
        }
        else {
            return(url)
        }
    }
    else {
        return()
    }
}
```

## `nhs_download`

```r
function (years, items, files, xpt = TRUE, tsv = TRUE, varLabel = TRUE, codebook = TRUE, update = TRUE, 
    filetable = NULL, cat = TRUE, redown = TRUE, updatekeyword = NULL) 
{
    if (do::cnOS()) {
        items0 <- tmcn::toUTF8("items<U+8D4B><U+503C><U+4E0D><U+5BF9>,<U+5E94><U+8BE5><U+662F><U+4E0B><U+5217><U+503C>: ")
        start <- tmcn::toUTF8("=====<U+5F00><U+59CB><U+4E0B><U+8F7D>=====")
    }
    else {
        items0 <- "items is not right, which should be: "
        start <- "=====starting====="
    }
    (years <- prepare_years(years))
    if (!is.null(filetable)) 
        years <- prepare_years(filetable$year)
    cat("\nyears: \n")
    do::cat_n(years, ind = 4)
    items <- prepare_items(items)
    if (!is.null(filetable)) 
        items <- prepare_items(filetable$items)
    cat("\n\nitems: \n")
    do::cat_n(items, n = 1, ind = 4)
    cat("\n\n", crayon::red(start), "\n")
    urls <- nhs_browse(years, items, FALSE)
    urls
    mode = "wb"
    testfile(urls = urls, mode = mode, files = files, redown = redown, xpt = xpt, tsv = tsv, varLabel = varLabel, 
        codebook = codebook, update = update, filetable = filetable, updatekeyword = updatekeyword)
    build_varLabel()
    build_codebook()
    build_html()
}
```

## `nhs_file_table`

```r
function (year, items, datafilename, docFilename, datafile, published, docURL, dataURL) 
{
    df <- data.frame(year, items, datafilename, docFilename, datafile, published, docURL, dataURL)
    colnames(df) <- c("year", "items", "Data File Name", "Doc File", "Data File", "Date Published", "DOC  url", 
        "Data url")
    df$year <- prepare_years(df$year)
    df$items <- prepare_items(df$items)
    df
}
```

## `nhs_files_pc`

```r
function (pattern = NULL, items, years, exclude = NULL, file_ext = NULL, cat = TRUE) 
{
    if (missing(years)) 
        years <- nhs_year_pc()
    years <- prepare_years(years)
    items <- prepare_items(items)
    d1 <- paste0(get_config_path(), "/", years, "/")
    d2 <- lapply(d1, function(i) paste0(i, items))
    d3 <- do.call(c, d2)
    if (is.null(file_ext)) 
        file_ext <- c("sas7bdat", "codebook", "varLabel", "tsv", "update", "xpt")
    if (!is.null(pattern)) 
        pattern <- paste0(pattern, collapse = "|")
    f1 <- list.files(path = d3, pattern = pattern, full.names = TRUE)
    ck <- tools::file_ext(f1) %in% file_ext
    f1[ck]
    f2 <- f1[ck]
    if (!is.null(exclude)) 
        f2 <- set::grep_not_or(f2, exclude)
    f2
}
```

## `nhs_files_web`

```r
function (years, items, cat = TRUE) 
{
    if (do::cnOS()) {
        retrieve <- tmcn::toUTF8("<U+63D0><U+53D6><U+6570><U+636E>(<U+5E74>):")
        items0 <- tmcn::toUTF8("items<U+8D4B><U+503C><U+4E0D><U+5BF9>,<U+5E94><U+8BE5><U+662F><U+4E0B><U+5217><U+503C>: ")
    }
    else {
        retrieve <- "retrieve items (year):"
        items0 <- "items is not right, which should be: "
    }
    (years <- prepare_years(years))
    (items <- prepare_items(items))
    (dt <- rep(items, each = length(years)))
    (ys <- rep(do::Replace0(years, "-.*"), length(items)))
    cycle2018 <- "CycleBeginYear"
    cycle2019 <- "Cycle"
    cycle <- sapply(ys, function(i) if (as.numeric(do::Replace0(i, "-.*")) == 2019) 
        cycle2019
    else if (as.numeric(i) < 2019) 
        cycle2018)
    ys[ys == "2019"] <- "2017-2020"
    urls <- sprintf("https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=%s&%s=%s", dt, cycle, 
        ys)
    (urls <- urls[order(ys)])
    (dt <- dt[order(ys)])
    (ys <- ys[order(ys)])
    for (i in 1:length(urls)) {
        if (i == 1) {
            res <- list()
            if (cat) 
                cat("\n", years[i])
        }
        else {
            if (ys[i] != ys[i - 1]) 
                if (cat) 
                  cat("\n", years[i])
        }
        if (cat) 
            cat("  ", dt[i])
        wait <- TRUE
        while (wait) {
            html <- tryCatch(xml2::read_html(urls[i]), error = function(e) "e")
            wait <- ifelse(is.character(html), TRUE, FALSE)
        }
        tbl <- rvest::html_table(html)
        if (length(tbl) == 0) {
            res <- c(res, list(data.frame(cbind(year = ys[i], items = dt[i]))))
        }
        else {
            df <- df.tolower(as.data.frame(listn(tbl, 1)))
            th <- rvest::html_text(rvest::html_elements(html, xpath = "//table/thead/tr//th"))
            urlp <- which(do::Replace0(tolower(th), " ") == "docfile")
            xpath <- sprintf("//table/tbody//tr/td[%s]", urlp)
            url1 <- sapply(rvest::html_elements(html, xpath = xpath), function(i) rvest::html_attr(rvest::html_elements(i, 
                xpath = "a"), "href"))
            url1[sapply(url1, length) == 0] <- NA
            url1 <- unlist(url1)
            ck <- do::left(url1, 2) == ".." & !is.na(url1)
            url1[ck] <- do::Replace(url1[ck], "\\.\\.", "/nchs/nhanes")
            xpath <- sprintf("//table/tbody//tr/td[%s]", urlp + 1)
            url2 <- sapply(rvest::html_elements(html, xpath = xpath), function(i) rvest::html_attr(rvest::html_elements(i, 
                xpath = "a"), "href"))
            url2[sapply(url2, length) == 0] <- NA
            url2 <- unlist(url2)
            ck <- do::left(url2, 2) == ".." & !is.na(url2)
            url2[ck] <- do::Replace(url2[ck], "\\.\\.", "/nchs/nhanes")
            colnames(df)[tolower(colnames(df)) == "years"] <- "year"
            dfi <- cbind(year = prepare_years(ys[i]), items = dt[i], df[, set::not(colnames(df), "year")], 
                `DOC  url` = paste0("https://wwwn.cdc.gov", url1), `Data url` = paste0("https://wwwn.cdc.gov", 
                  url2))
            ck <- tolower(do::file.name(url2)) == "dxa.aspx"
            ck[is.na(ck)] <- FALSE
            if (any(ck)) {
                dx <- dxa.aspx(url = dfi$`DOC  url`[ck], years = ys[i], items = dt[i])
                dfi[ck, ] <- dx
            }
            ck <- do::duplicated_last(paste0(df$`Doc File`, dfi$`Data url`))
            if (any(ck)) {
                dfi <- dfi[!ck, ]
            }
            row.names(dfi) <- NULL
            res <- c(res, list(dfi))
        }
    }
    x <- do.call(plyr::rbind.fill, res)
    class(x) <- c("nhs_file_web", "data.frame")
    rownames(x) <- NULL
    x
}
```

## `nhs_html`

```r
function (x, browse = TRUE) 
{
    html <- do::Replace(x, "\\.tsv", ".htm")
    if (!browse) 
        return(html)
    for (i in html) {
        if (file.exists(i)) {
            cli::cli_alert_success(i)
            browseURL(i)
        }
        else {
            update <- do::Replace(i, "\\.htm", ".update")
            url <- read.delim(update, check.names = FALSE)$"DOC  url"
            cli::cli_alert_success(i)
            browseURL(url)
        }
    }
}
```

## `nhs_html_download`

```r
function (tsv = NULL, download = FALSE, distribute = FALSE) 
{
    if (is.null(tsv)) 
        tsv <- nhs_tsv()
    if (download & length(tsv) > 0) {
        update <- do::Replace(tsv, "\\.tsv", "\\.update")
        url <- unique(sapply(update, function(i) read.delim(i, check.names = F)$"DOC  url"))
        for (i in 1:length(x)) {
            print(paste0(i, "/", length(x)))
            url <- x[i]
            html <- tryCatch(read_html(url), error = function(e) "e")
            if (all(html == "e")) 
                (next)(i)
            f <- tolower(do::file.name(url))
            xml2::write_html(html, f)
        }
    }
    htm <- list.files(pattern = "htm")
    if (distribute & length(htm) > 0 & length(tsv) > 0) {
        message("Distribute")
        htmfn <- do::Replace0(do::file.name(htm), ".htm")
        fn <- do::Replace0(do::file.name(tsv), ".tsv")
        for (i in htmfn) {
            from <- htm[htmfn == i]
            to <- do::file.dir(tsv[fn == i])
            for (j in to) {
                file.copy(from, j)
            }
        }
    }
}
```

## `nhs_items_pc`

```r
function (years) 
{
    if (missing(years)) 
        years <- nhs_year_pc()
    years <- prepare_years(years)
    urls <- paste0(get_config_path(), "/", years)
    res <- lapply(urls, function(i) list.files(i))
    names(res) <- years
    data.frame(do.call(rbind, res))
}
```

## `nhs_items_web`

```r
function (years, cat = TRUE) 
{
    if (do::cnOS()) {
        retrieve <- tmcn::toUTF8("<U+63D0><U+53D6><U+6570><U+636E>(<U+5E74>):")
    }
    else {
        retrieve <- "retrieve items (year):"
    }
    years <- prepare_years(years)
    urls <- paste0("https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=", do::Replace0(years, 
        "-.*"))
    for (i in 1:length(urls)) {
        if (cat) 
            cat("\n", retrieve, years[i])
        if (i == 1) 
            res <- list()
        wait = TRUE
        while (wait) {
            year_html <- tryCatch(xml2::read_html(urls[i]), error = function(e) "e")
            wait <- ifelse(is.character(year_html), TRUE, FALSE)
        }
        items_href = do::Replace0(do::Replace0(do::attr_href(set::grep_and(rvest::html_elements(year_html, 
            xpath = "//a[@class=\"list-title td-none td-ul-hover\"]"), "Component=")), ".*datapage\\.aspx\\?Component="), 
            "&CycleBeginYear.*")
        items_href = set::grep_not_and(items_href, "LimitedAccess")
        if (length(items_href) == 0) 
            items_href <- rep(NA, 5)
        res <- c(res, list(items_href))
        names(res)[i] <- years[i]
    }
    if (cat) 
        cat("\n\n")
    data.frame(do.call(rbind, res))
}
```

## `nhs_news`

```r
function (browse = FALSE) 
{
    browseURL("https://www.cdc.gov/nchs/nhanes/new_nhanes.htm")
}
```

## `nhs_pg`

```r
function (..., varLabel = TRUE, codebook = TRUE, nrows = Inf, lowercd = FALSE, force_rbind = FALSE, conn) 
{
    if (missing(conn)) 
        conn <- get("nhs_Connect", envir = .GlobalEnv)
    th <- c(...)
    ck <- grepl(get_config_path(), th, ignore.case = TRUE)
    (files <- th[ck])
    (variable <- tolower(th[!ck]))
    if (length(variable) > 0) {
        variable[!grepl("::", variable)] <- paste0(variable[!grepl("::", variable)], "::", variable[!grepl("::", 
            variable)])
        variable
    }
    if (do::cnOS()) {
        tsv <- tmcn::toUTF8("<U+5FC5><U+987B><U+662F>tsv<U+6587><U+4EF6>\n     ")
    }
    else {
        tsv <- "must be tsv file\n     "
    }
    if (any(tools::file_ext(files) != "tsv")) {
        files <- paste0(files[tools::file_ext(files) != "tsv"], collapse = "\n     ")
        tsv <- paste0(tsv, files)
        stop(tsv)
    }
    (years <- prepare_years(files))
    (yearu <- do::increase(unique(years)))
    maxnchar <- max(nchar(prepare_items(files)))
    data <- lapply(yearu, function(i) {
        (filesi <- files[years == i])
        cat(paste0("\n", crayon::red(do::Replace0(i, ".*/")), "(", length(filesi), ")"))
        for (j in 1:length(filesi)) {
            (filej <- do::file.name(filesi[j]))
            (itemsj <- prepare_items(filesi[j]))
            if (j == 1) {
                cat(paste0(itemsj, do::rep_n(" ", maxnchar - nchar(itemsj))))
            }
            else {
                if (itemsj != prepare_items(filesi[j - 1])) 
                  cat("\n           ", paste0(itemsj, do::rep_n(" ", maxnchar - nchar(itemsj))))
            }
            noext <- do::Replace0(filej, paste0("\\.", tools::file_ext(filej)))
            cat(paste0(" ", crayon::blue(noext)))
            (pgj <- sprintf("\"%s\".\"%s---%s\"", i, itemsj, do::Replace0(filej, "\\.tsv")))
            if (length(variable) == 0) {
                cmd <- sprintf("select * from %s", pgj)
                dfj <- DBI::dbGetQuery(conn = conn$con, statement = cmd)
                head(dfj)
                pair = colnames(dfj)
                names(pair) <- pair
            }
            else {
                cmd <- sprintf("select * from %s limit 1", pgj)
                namej <- colnames(DBI::dbGetQuery(conn = conn$con, statement = cmd))
                varlist <- strsplit(do::Replace0(variable, " {0,}::.*"), " {0,}; {0,}")
                names(varlist) <- do::Replace0(variable, ".*::")
                pair <- lapply(varlist, function(k) set::and(k, namej))
                (pair <- pair[sapply(pair, length) > 0])
                if (length(pair) == 0) {
                  dfj <- NULL
                }
                else {
                  pair <- unlist(pair)
                  varsql <- paste0(sprintf("\"%s\" as \"%s\"", pair, names(pair)), collapse = ", ")
                  cmd <- sprintf("select %s from %s", varsql, pgj)
                  if (!is.infinite(nrows)) 
                    cmd <- paste0(cmd, " limit ", nrows)
                  dfj <- DBI::dbGetQuery(conn = conn$con, statement = cmd)
                  dfj <- unique(dfj)
                  head(dfj)
                }
            }
            if (codebook & !is.null(dfj)) {
                (ckbkf <- do::Replace(filesi[j], "\\.tsv", ".codebook"))
                if (file.exists(ckbkf)) {
                  ckbk <- read.delim(ckbkf, comment.char = "#")
                  if (nrow(ckbk) > 0) {
                    ckbk$variable <- do::Trim(ckbk$variable)
                    ckbk$label <- do::Trim(ckbk$label)
                    ckbk$code <- do::Trim(ckbk$code)
                    if (lowercd) 
                      ckbk$label <- tolower(ckbk$label)
                    head(ckbk)
                    (ckbk <- ckbk[ckbk$variable %in% pair, ])
                    codepair <- set::and(pair, ckbk$variable)
                    if (nrow(ckbk) > 0) {
                      for (k in 1:length(codepair)) {
                        (code <- ckbk[ckbk$variable == codepair[k], ])
                        for (cd in 1:nrow(code)) {
                          cdjd <- dfj[, names(codepair[k])] == code[cd, "code"]
                          cdjd[is.na(cdjd)] <- FALSE
                          dfj[cdjd, names(codepair[k])] <- code[cd, "label"]
                        }
                      }
                    }
                  }
                }
            }
            if (varLabel & !is.null(dfj)) {
                (labefile <- do::Replace(filesi[j], "\\.tsv", ".varLabel"))
                if (file.exists(labefile)) {
                  labelj <- read.delim(labefile, comment.char = "#")
                  labelj <- labelj[labelj$variable %in% pair, ]
                  if (nrow(labelj) > 0) {
                    row.names(labelj) <- do::Trim(labelj$variable)
                    (labelj <- labelj[pair, "label"])
                    labelj <- labelj[!is.na(labelj)]
                    (labelj <- set::not(labelj, "seqn"))
                    if (length(labelj) > 0) {
                      dfj <- eval(parse(sprintf(paste0(sprintf("\"%s\" = \"%s\"", set::not(names(pair), 
                        "seqn"), labelj), collapse = ", "), fmt = "expss::apply_labels(dfj,%s)"), file = "", 
                        n = NULL))
                    }
                  }
                }
            }
            if (j == 1) {
                dfi <- dfj
            }
            else {
                dfi <- dplyr::full_join(dfi, dfj, by = "seqn")
            }
        }
        dfi
    })
    cons <- DBI::dbListConnections(RPostgreSQL::PostgreSQL())
    for (i in cons) DBI::dbDisconnect(i)
    names(data) <- yearu
    if (length(data) == 0) {
        if (cat) 
            cat("no data selected")
        if (cat) 
            cat("\nTime: ", time_diff(Sys.time(), t1), "\n")
        return()
    }
    else if (length(data) == 1) {
        if (force_rbind) {
            return(cbind(Year = names(data), data[[1]]))
        }
        else {
            return(data)
        }
    }
    else {
        (ck <- all(sapply(2:length(data), function(i) nrow(data[[1]]) == nrow(data[[i]]))))
        if (ck) {
            (ck <- all(sapply(2:length(data), function(i) any(do::increase(colnames(data[[1]])) == do::increase(colnames(data[[i]]))))))
        }
        if (ck) {
            for (i in 1:length(data)) {
                di <- cbind(Year = names(data)[i], data[[i]])
                data[[i]] <- di
            }
            names(data) = NULL
            df <- as.data.frame(do.call(rbind, data))
            row.names(df) = NULL
            return(df)
        }
        else {
            if (force_rbind) {
                for (i in 1:length(data)) {
                  data[[i]] <- cbind(Year = names(data)[i], data[[i]])
                }
                df <- do.call(plyr::rbind.fill, data)
                row.names(df) = NULL
                return(df)
            }
            else {
                return(data)
            }
        }
    }
}
```

## `nhs_read`

```r
function (..., varLabel = FALSE, codebook = TRUE, lower_cd = FALSE, Year = TRUE, nrows = Inf, cat = TRUE, 
    refuse_dontknow_toNA = TRUE, psu_strat = TRUE, join = c("full", "inner", "left", "right", "semi", 
        "anti", "nest")) 
{
    join <- match.arg(join)
    t1 <- Sys.time()
    hold <- list(...)
    hold <- lapply(hold, function(i) if (length(i) == 0) 
        character()
    else do::Trim(i))
    holdname <- do::get_names(...)
    holdname <- lapply(holdname, function(i) if (length(i) == 0) 
        character()
    else do::Trim(i))
    for (i in 1:length(hold)) {
        if (i < length(hold) & length(hold[[i]]) == 0) {
            if (!any(grepl(get_config_path(), hold[i + 1]))) 
                hold[[i + 1]] <- character()
        }
        else if (i == length(hold) & length(hold[[i]]) == 0) {
            hold[[i]] <- character()
        }
    }
    (ck <- sapply(hold, length) > 0)
    (hold <- hold[ck])
    tsv0(hold, msg.CN = tmcn::toUTF8("nhs_read()<U+6CA1><U+6709><U+63A5><U+6536><U+5230>tsv<U+6587><U+4EF6>"), 
        msg.EN = "no tsv files passed to nhs_read()")
    (holdname <- holdname[ck])
    (ck <- sapply(hold, function(i) any(grepl(get_config_path(), i))))
    if (sum(ck) > 1) {
        (hold_dup <- hold[ck])
        hold_ckname <- holdname[ck]
        for (i in 1:(length(hold_dup) - 1)) {
            for (j in (i + 1):length(hold_dup)) {
                if (any(hold_dup[[i]] %in% hold_dup[[j]])) {
                  duptsv <- set::and(hold_dup[[i]], hold_dup[[j]])
                  if (!do::cnOS()) 
                    msg <- paste0(hold_ckname[i], "and", hold_ckname[j], "have duplicated tsv file(", 
                      length(duptsv), ")\n", paste0(duptsv, collapse = "\n"))
                  if (do::cnOS()) 
                    msg <- paste0(hold_ckname[i], tmcn::toUTF8("<U+548C>"), hold_ckname[j], tmcn::toUTF8("<U+6709><U+91CD><U+590D><U+7684>tsv<U+6587><U+4EF6>("), 
                      length(duptsv), ")\n", paste0(set::and(hold_dup[[i]], hold_dup[[j]]), collapse = "\n"))
                  stop(msg)
                }
            }
        }
    }
    if (sum(ck) >= 1) 
        (holdname <- holdname[ck])
    for (i in 1:length(hold)) {
        if (any(grepl(get_config_path(), hold[i]))) {
            j <- i + 1
            p = 0
        }
        else {
            p = 1 + p
            if (p > 1) {
                hold[[j]] <- c(hold[[j]], hold[[i]])
                hold[[i]] <- NA
            }
        }
    }
    (hold <- hold[!sapply(hold, function(i) all(is.na(i)))])
    names(hold)[sapply(hold, function(i) any(grepl(get_config_path(), i)))] <- holdname
    for (i in 1:length(hold)) {
        if (i == 1) {
            tsv <- list()
            k <- 1
        }
        if (length(hold) == 1) {
            for (j in hold[[i]]) {
                tsv <- c(tsv, list(j))
                attr(tsv[[k]], "variable") <- "allvariableallvariable"
                attr(tsv[[k]], "holdname") <- names(hold)[i]
                k <- k + 1
            }
        }
        else if (any(grepl(get_config_path(), hold[[i]]))) {
            if (i + 1 <= length(hold)) {
                if (any(grepl(get_config_path(), hold[[i + 1]]))) {
                  for (j in hold[[i]]) {
                    tsv <- c(tsv, list(j))
                    attr(tsv[[k]], "variable") <- "allvariableallvariable"
                    attr(tsv[[k]], "holdname") <- names(hold)[i]
                    k <- k + 1
                  }
                }
                else {
                  for (j in 1:length(hold[[i]])) {
                    (tsv <- c(tsv, list(hold[[i]][j])))
                    if (j == 1) {
                      holdi1 <- hold[[i + 1]]
                      (ck <- do::right(holdi1, 2) == "-u")
                      if (any(ck)) 
                        holdi1[ck] <- do::knife_right(holdi1[ck], 2)
                      hold[[i + 1]] <- holdi1
                    }
                    attr(tsv[[k]], "uncodebook") <- holdi1[ck]
                    attr(tsv[[k]], "variable") <- holdi1
                    attr(tsv[[k]], "holdname") <- names(hold)[i]
                    k <- k + 1
                  }
                }
            }
            else if (i == length(hold)) {
                if (any(grepl(get_config_path(), hold[[i]]))) {
                  for (j in hold[[i]]) {
                    tsv <- c(tsv, list(j))
                    attr(tsv[[k]], "variable") <- "allvariableallvariable"
                    attr(tsv[[k]], "holdname") <- names(hold)[i]
                    k <- k + 1
                  }
                }
            }
        }
    }
    tsv
    (varlist <- lapply(tsv, function(i) attr(i, "variable")))
    (holdname <- sapply(tsv, function(i) attr(i, "holdname")))
    holdmaxn <- max(nchar(holdname)) + 1
    holdname <- sapply(holdname, function(i) paste0(i, do::rep_n(" ", holdmaxn - nchar(i))))
    (holdnameu <- unique(holdname))
    (uncodebook <- lapply(tsv, function(i) attr(i, "uncodebook")))
    (files <- unlist(tsv))
    filemaxn <- max(nchar(do::file.name(files))) - 4
    variablemaxn <- nchar(max(sapply(varlist, length)) + 1)
    if (do::cnOS()) {
        tsv <- tmcn::toUTF8("<U+5FC5><U+987B><U+662F>tsv<U+6587><U+4EF6>\n     ")
    }
    else {
        tsv <- "must be tsv file\n     "
    }
    if (any(tools::file_ext(files) != "tsv")) {
        files <- paste0(files[tools::file_ext(files) != "tsv"], collapse = "\n     ")
        tsv <- paste0(tsv, files)
        stop(tsv)
    }
    for (i in 1:length(holdnameu)) {
        if (i == 1) {
            years <- prepare_years(files)
            (yearu <- do::increase(unique(years)))
            data <- lapply(1:length(yearu), function(i) NULL)
            names(data) <- yearu
            items <- prepare_items(files)
            itemmaxn <- max(nchar(items))
            varLabeldata <- NULL
            variableorder <- c()
            all_joint <- c()
        }
        (filesi <- files[holdname %in% holdnameu[i]])
        (filesi <- filesi[order(paste0(prepare_items(filesi), prepare_years(filesi)))])
        if (cat) 
            cat(paste0(ifelse(i == 1, "\n", "\n\n"), crayon::red(do::Replace0(holdnameu[i], ".*/")), 
                "(", length(filesi), ifelse(length(filesi) < 10, ") ", ")")))
        for (j in 1:length(filesi)) {
            (filej <- do::file.name(filesi[j]))
            (itemsj <- prepare_items(filesi[j]))
            if (j == 1) {
                catviriablen <- 1
                if (cat) 
                  cat(paste0(itemsj, do::rep_n(" ", itemmaxn - nchar(itemsj))))
            }
            else {
                if (itemsj != prepare_items(filesi[j - 1])) 
                  if (cat) 
                    cat("\n           ", paste0(itemsj, do::rep_n(" ", itemmaxn - nchar(itemsj))))
            }
            (noext <- do::Replace0(filej, paste0("\\.", tools::file_ext(filej))))
            dfj <- data.table::fread(filesi[j], showProgress = FALSE, nrows = 1)
            (variable <- varlist[[which(files == filesi[j])]])
            excludename <- c("seqn", "drxiline", "dr1iline", "dr2iline", "drdifdcd", "dr1ifdcd", "dr2ifdcd", 
                "drxfdcd", "dr1mc", "dr2mc", "drxmc", "rxddrgid", "sampleid", "dsdpid", "dsdiid", "dsdsupid", 
                "_mult_")
            if (psu_strat) 
                excludename <- c(excludename, "sdmvpsu", "sdmvstra")
            if (all(variable == "allvariableallvariable")) {
                variable <- colnames(dfj)
                dfj <- tryCatch(data.table::fread(filesi[j], showProgress = FALSE, nrows = nrows), warning = function(w) "w")
                if (is.character(dfj)) 
                  dfj <- data.table::fread(filesi[j], showProgress = FALSE, nrows = nrows, fill = TRUE)
                if (cat) {
                  filemsg <- paste0(" ", crayon::blue(paste0(do::equal_length(noext, nchar = filemaxn), 
                    "(", do::equal_length(ncol(dfj), nchar = max(nchar(ncol(dfj)), variablemaxn)), ",", 
                    crayon::magenta(prepare_years(filesi[j], range = FALSE)), ")")))
                  cat(filemsg)
                }
                if (catviriablen%%3 == 0) 
                  if (cat) 
                    cat("\n", do::rep_n(" ", holdmaxn + itemmaxn + 4))
                catviriablen <- catviriablen + 1
                variableorder <- unique(c("Year", "seqn", variableorder, colnames(dfj)))
                variableorder[variableorder %in% c("drxiline", "dr1iline", "dr2iline")] <- "line"
                variableorder[variableorder %in% c("drdifdcd", "dr1ifdcd", "dr2ifdcd", "drxfdcd")] <- "food.code"
                all_joint <- unique(c("seqn", all_joint))
            }
            else {
                (variable <- do::Replace0(variable, " "))
                (variable[!grepl(":", variable)] <- paste0(variable[!grepl(":", variable)], ":", variable[!grepl(":", 
                  variable)]))
                variable <- paste0(tolower(do::Replace0(variable, ":.*")), ":", do::Replace0(variable, 
                  ".*:"))
                variableorder <- unique(c("Year", "seqn", variableorder, do::Replace0(variable, ".*:")))
                (ck <- sapply(tolower(variable), function(ii) any(unique(unlist(strsplit(do::Replace0(ii, 
                  ":.*"), ","))) %in% colnames(dfj))))
                if (!any(ck)) {
                  (holdnamej <- holdname[files == filesi[j]])
                  files[files == filesi[j]] <- "novariable"
                  if (cat) {
                    filemsg <- paste0(" ", crayon::red(paste0(do::equal_length(noext, nchar = filemaxn), 
                      "(", do::equal_length("0", nchar = max(nchar(ncol(dfj)), variablemaxn)), ",", crayon::magenta(prepare_years(filesi[j], 
                        range = FALSE)), ")")))
                    cat(filemsg)
                  }
                  if (catviriablen%%3 == 0) 
                    if (cat) 
                      cat("\n", do::rep_n(" ", holdmaxn + itemmaxn + 4))
                  catviriablen <- catviriablen + 1
                  (next)(j)
                }
                (names <- unique(variable[ck]))
                (allfrom <- tolower(do::Replace0(names, ":.*")))
                (keyvar <- paste0(excludename, ":", excludename))
                (keyvar <- keyvar[sapply(keyvar, function(keyi) do::Replace0(keyi, ":.*") %in% colnames(dfj))])
                if (length(keyvar) > 0) {
                  (names <- names[!sapply(allfrom, function(l) any(excludename %in% unique(strsplit(l, 
                    ",")[[1]])))])
                  (names <- c(keyvar, names))
                }
                dfj <- tryCatch(data.table::fread(filesi[j], showProgress = FALSE, nrows = nrows), warning = function(w) "w")
                if (is.character(dfj)) 
                  dfj <- data.table::fread(filesi[j], showProgress = FALSE, nrows = nrows, fill = TRUE)
                for (k in 1:length(names)) {
                  if (k == 1) 
                    keepnames <- rep(TRUE, length(names))
                  (fromk <- unique(unlist(strsplit(do::Replace0(tolower(names[k]), ":.*"), ","))))
                  (tok <- do::Replace0(names[k], ".*:"))
                  if (any(fromk %in% colnames(dfj))) {
                    (fromkj <- fromk[fromk %in% colnames(dfj)])
                    colnames(dfj)[colnames(dfj) %in% fromk] <- tok
                    varlabelk <- nhs_varLabel(filesi[j])
                    varlabelk = varlabelk[varlabelk$variable == fromkj, c("file", "label")]
                    labelkj <- varlabelk[1, 2]
                    names(labelkj) <- varlabelk[1, 1]
                    if (is.null(varLabeldata)) {
                      varLabeldata <- data.frame(rename = tok, `NHANES name` = I(list(fromkj)), label = I(list(labelkj)), 
                        check.names = FALSE)
                    }
                    else {
                      if (tok %in% varLabeldata[, 1]) {
                        varLabeldata[varLabeldata[, 1] == tok, "NHANES name"][[1]] <- list(unique(c(varLabeldata[varLabeldata[, 
                          1] == tok, "NHANES name"][[1]], fromkj)))
                        varLabeldata[varLabeldata[, 1] == tok, "label"][[1]] <- list(c(varLabeldata[varLabeldata[, 
                          1] == tok, "label"][[1]], labelkj))
                      }
                      else {
                        varlabelj <- data.frame(rename = tok, `NHANES name` = I(list(fromkj)), label = I(list(labelkj)), 
                          check.names = FALSE)
                        varLabeldata <- rbind(varLabeldata, varlabelj)
                      }
                    }
                  }
                  else {
                    keepnames[k] <- FALSE
                  }
                }
                (nm <- do::Replace0(names, ".*:")[keepnames])
                dfj <- unique(dfj[, nm, with = FALSE])
                if (!data.table::is.data.table(dfj)) {
                  dfj <- data.table::as.data.table(dfj)
                  colnames(dfj) <- nm
                }
                if (cat) {
                  filemsg <- paste0(" ", crayon::blue(paste0(do::equal_length(noext, nchar = filemaxn), 
                    "(", do::equal_length(ncol(dfj), nchar = max(nchar(ncol(dfj)), variablemaxn)), ",", 
                    crayon::magenta(prepare_years(filesi[j], range = FALSE)), ")")))
                  cat(filemsg)
                }
                if (catviriablen%%3 == 0) 
                  if (cat) 
                    cat("\n", do::rep_n(" ", holdmaxn + itemmaxn + 3))
                catviriablen <- catviriablen + 1
            }
            colnames(dfj)[colnames(dfj) %in% c("drxiline", "dr1iline", "dr2iline")] <- "line"
            colnames(dfj)[colnames(dfj) %in% c("drdifdcd", "dr1ifdcd", "dr2ifdcd", "drxfdcd")] <- "food.code"
            head(dfj)
            if (codebook) {
                (ckbkf <- do::Replace(filesi[j], "\\.tsv", ".codebook"))
                if (file.exists(ckbkf)) {
                  ckbk <- read.delim(ckbkf, comment.char = "#")
                  ckbk <- ckbk[!is.na(ckbk$variable), ]
                  if (length(ckbk) == 0) 
                    ckbk <- data.frame()
                  if (nrow(ckbk) > 0) {
                    dontcodebook.var.code <- c("sld010h:12", "sld012:2,14", "mcq180f:85", "mcd180f:85")
                    for (dontcdi in 1:length(dontcodebook.var.code)) {
                      dontcodebook.var <- strsplit(dontcodebook.var.code[dontcdi], ":")[[1]][1]
                      dontcodebook.code <- strsplit(strsplit(dontcodebook.var.code[dontcdi], ":")[[1]][-1], 
                        ",")[[1]]
                      if (dontcodebook.var %in% ckbk$variable) {
                        ckjdonti <- (ckbk$variable == dontcodebook.var) & (ckbk$code %in% dontcodebook.code)
                        if (length(ckbk) > 0) {
                          if (nrow(ckbk) > 0) {
                            ckbk <- ckbk[!ckjdonti, ]
                          }
                        }
                      }
                    }
                    dontcodebook <- c("ridageyr", "wtmec2yr", "indfmpir", "wtdrd1", "wtdr2d", "wtssnh2y")
                    ckbk <- ckbk[!ckbk$variable %in% dontcodebook, ]
                    if (length(ckbk) > 0) {
                      if (nrow(ckbk) > 1) {
                        ckbk$variable <- tolower(ckbk$variable)
                        if (lower_cd) 
                          ckbk$label <- tolower(ckbk$label)
                        ckbk$variable <- do::Trim(ckbk$variable)
                        ckbk$label <- do::Trim(ckbk$label)
                        ckbk$label <- do::Trim(ckbk$label, "`")
                        ckbk$label <- do::Trim(ckbk$label, ",")
                        ckbk$label[ckbk$label == "very much, or"] <- "very much"
                        ckbk$code <- do::Trim(ckbk$code)
                        head(ckbk)
                        if (length(variable) > 0) {
                          variable <- do::Replace0(variable, " ")
                          variable[!grepl(":", variable)] <- paste0(variable[!grepl(":", variable)], 
                            ":", variable[!grepl(":", variable)])
                          (select <- unique(unlist(strsplit(do::Replace0(variable, ":.*"), ","))))
                          exselect <- unique(unlist(lapply(do::Replace0(unlist(uncodebook[files == filesi[j]]), 
                            ":.*"), function(ui) strsplit(ui, ",|:"))))
                          select <- select[!select %in% exselect]
                          ckbk <- ckbk[ckbk$variable %in% select, ]
                          for (k in 1:length(variable)) {
                            fromk <- unique(unlist(strsplit(do::Replace0(variable[k], ":.*"), ",")))
                            tok <- do::Replace0(variable[k], ".*:")
                            ckbk[ckbk$variable %in% fromk, "variable"] <- tok
                          }
                        }
                        ckbk <- ckbk[ckbk$variable %in% colnames(dfj), ]
                        (ck <- nrow(ckbk) > 0)
                        if (ck) {
                          for (k in unique(ckbk$variable)) {
                            k <- do::Replace0(k, " ")
                            code <- ckbk[ckbk$variable == k, ]
                            code[, "label"] <- do::Replace(code[, "label"], " {2,}", " ")
                            code[, "label"] <- do::Replace(code[, "label"], " {0,}\n {0,}", " ")
                            dfjk <- dfj[[k]]
                            for (cd in 1:nrow(code)) {
                              dfjk[dfjk %in% code[cd, "code"]] <- code[cd, "label"]
                            }
                            dfj[[k]] <- dfjk
                            dfjk = "release it"
                          }
                        }
                      }
                    }
                  }
                }
            }
            head(dfj)
            if (varLabel) {
                (labefile <- do::Replace(filesi[j], "\\.tsv", ".varLabel"))
                if (file.exists(labefile)) {
                  labelj <- read.delim(labefile, comment.char = "#")
                  if (length(variable) > 0) {
                    variable <- do::Replace0(variable, " ")
                    variable[!grepl(":", variable)] <- paste0(variable[!grepl(":", variable)], ":", variable[!grepl(":", 
                      variable)])
                    (select <- unique(unlist(strsplit(do::Replace0(variable, ":.*"), ","))))
                    for (k in 1:length(variable)) {
                      fromk <- unique(unlist(strsplit(do::Replace0(variable[k], ":.*"), ",")))
                      tok <- do::Replace0(variable[k], ".*:")
                      labelj[labelj$variable %in% fromk, "variable"] <- tok
                    }
                  }
                  ck <- labelj$variable %in% colnames(dfj)
                  (labelj <- labelj[ck, c("variable", "label")])
                  if (nrow(labelj) > 0) {
                    dfj <- eval(parse(sprintf(paste0(sprintf("\"%s\" = \"%s\"", labelj$variable, labelj$label), 
                      collapse = ", "), fmt = "expss::apply_labels(dfj,%s)"), file = "", n = NULL))
                  }
                }
            }
            if (lower_cd) 
                for (il in 1:ncol(dfj)) if (is.character(dfj[[il]])) 
                  dfj[[il]] <- tolower(dfj[[il]])
            key <- excludename
            key[grepl("line", key)] <- "line"
            key[grepl("fdcd", key)] <- "food.code"
            key <- unique(key)
            if (filesi[j] %in% nhs_tsv("bfrpol|pcbpol|doxpol|pstpol", cat = FALSE) & nrow(dfj) > 0) {
                dfj$Year <- prepare_years(filesi[j])
                dfj <- db_pooltf(dfj)
            }
            if (is.null(data[[prepare_years(filesi[j])]])) {
                dfj$Year <- prepare_years(filesi[j])
                data[[prepare_years(filesi[j])]] <- dfj
                dfj <- "release it"
            }
            else {
                (j1 <- c("seqn", "food.code")[c("seqn", "food.code") %in% colnames(data[[prepare_years(filesi[j])]])])
                (all_joint <- j1[j1 %in% colnames(dfj)])
                joint <- sprintf(paste0(paste0(sprintf("'%s'", all_joint), "=", sprintf("'%s'", all_joint)), 
                  collapse = ","), fmt = "c(%s)")
                ps <- parse(text = sprintf("data[[prepare_years(filesi[j])]] <- suppressMessages(dplyr::%s_join(data[[prepare_years(filesi[j])]],dfj,by=%s))", 
                  join, joint))
                eval(ps)
                dfj <- "release it"
            }
        }
    }
    gc()
    varLabeldata[, 2] <- sapply(varLabeldata[, 2], function(i) {
        (namei <- do::unique_no.NA(i))
        if (length(namei) == 0) {
            ""
        }
        else {
            paste0(namei, collapse = ", ")
        }
    })
    varLabeldata[, 3] <- sapply(varLabeldata[, 3], function(i) {
        if (is.null(i)) 
            return("")
        (varlabeli <- do::unique_no.NA(i))
        if (length(varlabeli) == 0) {
            ""
        }
        else if (length(varlabeli) == 1) {
            varlabeli
        }
        else {
            paste0(sapply(varlabeli, function(j) sprintf("[%s] %s", paste0(names(i)[i == j], collapse = ","), 
                j)), collapse = "<br>")
        }
    })
    files <- files[files != "novariable"]
    names(data) <- yearu
    data <- data[!sapply(data, is.null)]
    target <- data.table::fread(paste0(get_config_path(TRUE), "varLabel.txt"), showProgress = FALSE, 
        data.table = FALSE)[, c("year", "item", "file", "variable", "target", "url")]
    tsv <- do::Replace0(files, get_config_path(T), "\\.tsv")
    ck <- paste0_columns(target[, c("year", "item", "file")], "/") %in% tsv
    target <- target[ck, ]
    row.names(target) <- NULL
    if (cat) 
        cat(crayon::red("\n\nOutput\n"))
    if (length(data) == 0) {
        if (cat) 
            cat("\nTime: ", time_diff(Sys.time(), t1), "\n")
        return("no data selected")
    }
    else {
        for (i in 1:length(data)) {
            data[[i]]$Year <- names(data)[i]
        }
        data <- as.data.frame(do.call(plyr::rbind.fill, data), check.names = FALSE)
        if (refuse_dontknow_toNA) 
            data <- to_NA(data)
        cnms <- set::not(do::character.nms(data), "Year", "dr2mc", "dr1mc", "drxfdcd", "drdifdcd", "dr1ifdcd", 
            "dr2ifdcd")
        for (i in cnms) {
            xi <- tryCatch(as.numeric(data[1, i]), warning = function(w) "wwwarning")
            if (is.na(xi)) {
                xi <- tryCatch(as.numeric(data[2, i]), warning = function(w) "wwwarning")
            }
            if (is.na(xi)) {
                xi <- tryCatch(as.numeric(funique.noNA(data[, i])), warning = function(w) function() "wwwarning")
            }
            if (is.function(xi)) 
                (next)(i)
            xi <- tryCatch(as.numeric(data[, i]), warning = function(w) function() "wwwarning")
            if (is.function(xi)) 
                (next)(i)
            data[, i] <- xi
        }
        vo <- seqn_by(x = colnames(data), unique(c("Year", unique(key), variableorder)))
        data <- data[, vo]
        colnames(data)[colnames(data) == "_mult_"] <- "\"_mult_\""
        eval(parse(text = sprintf("data <- data[order(%s),]", paste0(paste0("data$", set::and(c("Year", 
            excludename), colnames(data))), collapse = ","))))
        colnames(data)[colnames(data) == "\"_mult_\""] <- "_mult_"
        rownames(data) <- NULL
        nhs_years <- unique(data$Year)
        if (!Year) 
            data <- drop_col(data, "Year")
        if (cat) 
            cat("Data Type: data.frame", paste0("(", paste0(dim(data), collapse = ","), ")\n"))
        if (cat) 
            cat("Final Years Cycle:", length(nhs_years))
        if (cat) 
            cat("\nTime: ", time_diff(Sys.time(), t1), "\n")
        if ("drdifdcd" %in% colnames(data)) 
            data$drdifdcd <- format(data$drdifdcd, width = 8)
        if ("drdifdcd" %in% colnames(data)) 
            data$drdifdcd[data$drdifdcd %in% "      NA"] <- NA
        if ("dr1ifdcd" %in% colnames(data)) 
            data$dr1ifdcd <- format(data$dr1ifdcd, width = 8)
        if ("dr1ifdcd" %in% colnames(data)) 
            data$dr1ifdcd[data$dr1ifdcd %in% "      NA"] <- NA
        if ("dr2ifdcd" %in% colnames(data)) 
            data$dr2ifdcd <- format(data$dr2ifdcd, width = 8)
        if ("dr2ifdcd" %in% colnames(data)) 
            data$dr2ifdcd[data$dr2ifdcd %in% "      NA"] <- NA
        if ("drxfdcd" %in% colnames(data)) 
            data$drxfdcd <- format(data$drxfdcd, width = 8)
        if ("drxfdcd" %in% colnames(data)) 
            data$drxfdcd[data$drxfdcd %in% "      NA"] <- NA
        if ("dr1mc" %in% colnames(data)) 
            data$dr1mc <- format(data$dr1mc, width = 6)
        if ("dr1mc" %in% colnames(data)) 
            data$dr1mc[data$dr1mc %in% "    NA"] <- NA
        if ("dr2mc" %in% colnames(data)) 
            data$dr2mc <- format(data$dr2mc, width = 6)
        if ("dr2mc" %in% colnames(data)) 
            data$dr2mc[data$dr2mc %in% "    NA"] <- NA
        attr(data, "target") <- target
        attr(data, "varnameLabel") <- varLabeldata
        attr(data, "files") <- files
        attr(data, "nhs_years") <- nhs_years
        return(data)
    }
}
```

## `nhs_search`

```r
function (..., cat = TRUE, fileds = NULL) 
{
    key <- c(...)
    vartext <- paste0(get_config_path(), "/varLabel.txt")
    if (!file.exists(vartext)) 
        build_varLabel()
    varLabel <- data.table::fread(vartext, data.table = FALSE)
    if (is.null(key)) 
        return(varLabel)
    if (is.null(fileds)) {
        fileds <- set::not(colnames(varLabel), "url")
    }
    else {
        ck <- sapply(set::not(colnames(varLabel), "url"), function(i) any(sapply(fileds, function(j) do::left_equal(i, 
            j))))
        fileds <- colnames(varLabel)[ck]
    }
    index <- paste0_columns(varLabel[, fileds, drop = FALSE], "------")
    ck <- lookl(index, tolower(key), ignore.case = TRUE)
    df <- varLabel[ck, ]
    if (nrow(df) == 0) {
        cat("results: ", nrow(df))
        return()
    }
    nchar <- df
    for (i in 1:ncol(df)) {
        for (j in 1:nrow(df)) {
            nchar[j, i] <- tryCatch(nchar(df[j, i]), error = function(e) 1)
        }
        nchar[, i] <- as.numeric(nchar[, i])
    }
    if (is.data.frame(nchar) | is.matrix(nchar)) {
        df <- df[, colSums(nchar) > 0, drop = FALSE]
    }
    else {
        df <- df[, nchar > 0, drop = FALSE]
    }
    class(df) <- c("nhs_search", "data.frame")
    if (cat) 
        cat("results: ", nrow(df))
    keys <- unique(do::Trim_left(unique(unlist(strsplit(key, "\\|"))), c(" ", "~", "!", "=")))
    attr(df, "nhs_search") <- keys
    df
}
```

## `nhs_target`

```r
function (...) 
{
    UseMethod("nhs_target")
}
```

## `nhs_tsv`

```r
function (..., items, years, ex_years = NULL, cat = TRUE) 
{
    file_ext = "tsv"
    years <- prepare_years(years)
    if (!is.null(ex_years)) 
        years <- set::not(years, prepare_years(ex_years))
    items <- prepare_items(items)
    (d1 <- get_config_path() %+% "/" %+% years %+% "/")
    (d2 <- lapply(d1, function(i) i %+% items))
    (d3 <- do.call(c, d2))
    f1 <- list.files(path = d3, full.names = TRUE)
    ck <- tools::file_ext(f1) %in% file_ext
    f2 <- f1[ck]
    pattern <- c(...)
    if (is.null(pattern)) 
        return(f2)
    fn <- paste0(do::Replace0(do::file.name(f2), "\\.tsv"), ".")
    ck <- lookl(x = fn, pattern, ignore.case = TRUE)
    x <- f2[ck]
    if (cat) 
        print(x)
    invisible(x)
}
```

## `nhs_update`

```r
function (path = NULL) 
{
    config_years(F)
    if (!dir.exists(path)) 
        stop("<U+8DEF><U+5F84><U+4E0D><U+5B58><U+5728>")
    message("<U+66F4><U+65B0>\n")
    copy_with_structure(path, get_config_path())
    message("<U+5B8C><U+6210>\n")
}
```

## `nhs_varLabel`

```r
function (..., tolower = FALSE) 
{
    hold <- c(...)
    ck <- grepl(get_config_path(), hold, ignore.case = TRUE)
    files <- hold[ck]
    variable <- tolower(hold[!ck])
    if (length(files) == 0) 
        files <- nhs_files_pc(file_ext = "varLabel")
    ck <- tools::file_ext(files) != "varLabel"
    if (any(ck)) {
        ext <- sprintf(unique(tools::file_ext(files[ck])), fmt = "\\.%s")
        files[ck] <- sprintf(do::Replace0(files[ck], ext), fmt = "%s.varLabel")
    }
    do.call(lapply(files, function(i) {
        (Year <- prepare_years(i))
        (Item <- prepare_items(i))
        (file <- do::Replace0(do::file.name(i), "\\.varLabel"))
        lbii <- do::left(do::Replace0(readLines(i, 1), " "), 1)
        if (lbii == "#") {
            labeli <- read.delim(i, comment.char = "#")
        }
        else {
            labeli <- data.table::fread(i, data.table = F)
        }
        if (length(variable) > 0) {
            ck <- lookl(labeli$name, variable, ignore.case = TRUE)
            labeli <- labeli[ck, ]
            if (tolower) 
                labeli$label <- tolower(labeli$label)
        }
        if (nrow(labeli) == 0) 
            return()
        colnames(labeli)[1:2] <- c("variable", "label")
        cbind(Year = Year, Item = Item, file = file, labeli)
    }), what = plyr::rbind.fill)
}
```

## `nhs_view`

```r
function (x, ...) 
UseMethod("nhs_view")
```

## `nhs_wt`

```r
function (data, yr2, yr4, wtname = "cwt") 
{
    (cycle <- length(unique(data$Year)))
    if (missing(yr4)) {
        cwt <- data[, yr2] * 1/cycle
        eval(parse(text = sprintf("data$%s <- cwt", wtname)))
    }
    else {
        ck <- data$Year %in% prepare_years(1999:2001)
        cwt <- ifelse(ck, data[, yr4] * 2/cycle, data[, yr2] * 1/cycle)
        eval(parse(text = sprintf("data$%s <- cwt", wtname)))
    }
    return(data)
}
```

## `nhs_year_pc`

```r
function (range = TRUE) 
{
    do::unique_no.NA(do::increase(unique(stringr::str_extract(list.files(get_config_path()), "[0-9]{4}-[0-9]{4}"))))
}
```

## `nhs_years_web`

```r
function (range = TRUE) 
{
    home_url = "https://wwwn.cdc.gov/nchs/nhanes"
    html = xml2::read_html(home_url)
    years <- do::Replace0(rvest::html_text(rvest::html_nodes(html, xpath = "//div[@class=\"col-md-3 d-flex\"]/a")), 
        c("\t", "\n", "\r", "NHANES"))
    if (!range) 
        years <- do::Replace0(years, "-.*")
    years
}
```

## `optimal_nKnots`

```r
function (fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F) 
UseMethod("optimal_nKnots")
```

## `p4interaction`

```r
function (fit, adjust = NULL, df = Inf) 
{
    if ("svytableone" %in% class(fit)) 
        fit <- attr(fit, "fit")
    (allterms <- set::grep_and(attr(fit[["terms"]], "term.labels"), ":"))
    if (length(allterms) > 0) {
        if (any(class(fit) %in% "svycoxph")) {
            form <- sprintf(paste0(set::grep_and(attr(fit[["terms"]], "term.labels"), ":"), collapse = " + "), 
                fmt = "~%s")
            inter <- do::knife_left(form, 1)
            p <- regTermTest4svycoxph(fit, as.formula(form), method = "LRT", df = df)$p[[1]]
            adjust0 <- set::not(do::model.x(fit), unlist(strsplit(inter, ":")))
            if (length(adjust0) == 0) 
                adjust0 = ""
            adjust0 <- paste0(adjust0, collapse = ", ")
            p
        }
        else if (any(class(fit) %in% "svyglm")) {
            (form <- sprintf(paste0(set::grep_and(attr(fit[["terms"]], "term.labels"), ":"), collapse = " + "), 
                fmt = "~%s"))
            inter <- do::knife_left(form, 1)
            p <- regTermTest2(fit, test.terms = as.formula(form), method = "LRT", df = df)$p[[1]]
            adjust0 <- set::not(do::model.x(fit), unlist(strsplit(inter, ":")))
            if (length(adjust0) == 0) 
                adjust0 = ""
            adjust0 <- paste0(adjust0, collapse = ", ")
            p
        }
        else {
            inter <- paste0(set::grep_and(attr(fit[["terms"]], "term.labels"), ":"), collapse = " + ")
            int <- paste0(do::Replace(set::grep_and(attr(fit[["terms"]], "term.labels"), ":"), ":", "*"), 
                collapse = " - ")
            deint <- paste0(sapply(strsplit(set::grep_and(attr(fit[["terms"]], "term.labels"), ":"), 
                ":"), function(i) paste0(i, collapse = " + ")), collapse = " + ")
            form <- as.formula(sprintf(fmt = " . ~ . - %s + %s", int, deint))
            (fit0 <- update(fit, formula. = form))
            p <- 1 - pchisq(as.numeric(-2 * (logLik(fit0) - logLik(fit))), 1)
            adjust0 <- set::not(do::model.x(fit), unlist(strsplit(inter, ":")))
            if (length(adjust0) == 0) 
                adjust0 = ""
            adjust0 <- paste0(adjust0, collapse = ", ")
            p
        }
    }
    else {
        x <- do::model.x(fit)
        if (length(x) < 2) 
            stop("x must be 2 or more")
        x <- sapply(data.frame(combn(x, 2)), function(i) paste0(i, collapse = "*"))
        names(x) <- NULL
        do.call(lapply(x, function(i) {
            form <- i
            if (!is.null(adjust)) 
                form <- paste0(i, " + ", paste0(adjust, collapse = " + "))
            form <- as.formula(paste0(".~ ", form))
            fitin <- update(fit, formula. = form)
            p4interaction(fitin)
        }), what = rbind)
    }
}
```

## `p4trend`

```r
function (fit, x = NULL, character2integer = TRUE, quadratic = FALSE, round = 3) 
{
    if (is.null(x)) 
        stop(tmcn::toUTF8("<U+6CA1><U+6709><U+6307><U+5B9A>x"))
    if ("svytableone" %in% class(fit)) 
        fit <- attr(fit, "fit")
    rgt <- reg_table(fit, x = x, view = F)
    if ((nrow(rgt) - 1) <= 2) {
        x <- "noPvalue4trend"
        names(x) <- "p for trend"
        return(x)
    }
    if (character2integer) {
        (form <- as.formula(sprintf(". ~ . - %s + character2numeric(%s)", x, x)))
        (fitf <- update(fit, formula. = form))
        (resi <- tryCatch(reg_table(fit = fitf, round = round, view = F, x = sprintf("character2numeric(%s)", 
            x)), error = function(e) "e"))
        if (is.character(resi)) 
            resi <- reg_table(fit = fitf, round = round, view = F, x = x)
        (p.integer <- resi[, grepl("p", colnames(resi), T)])
        form <- as.formula(sprintf(". ~ . - %s + %s.median", x, x))
        fitf <- tryCatch(update(fit, formula. = form), error = function(e) "e")
        p.median <- NULL
        if (is.character(fitf)) {
            p.median <- NULL
        }
        else {
            (resi <- reg_table(fitf, round = round, view = F, x = sprintf("%s.median", x)))
            p.median <- resi[, grepl("p", colnames(resi), T)]
        }
        p1 <- c(p.integer, p.median)
        names(p1) <- c("p for trend(character2integer)", "p for trend(Median value)")[1:length(p1)]
    }
    if (quadratic) {
        form <- as.formula(sprintf(". ~ . - %s + poly(character2numeric(%s),2)", x, x))
        fitf <- update(fit, formula. = form)
        (resi <- reg_table(fit = fitf, round = round, view = F, x = paste0("poly(character2numeric(", 
            x, "), 2)", 1:2)))
        p.quadratic.1 <- resi[1, grepl("p", colnames(resi), T)]
        p.quadratic.2 <- resi[2, grepl("p", colnames(resi), T)]
        p2 <- c(p.quadratic.1, p.quadratic.2)
        names(p2) <- c("Linear P value", "Quadratic P value")
    }
    if (character2integer & quadratic) {
        sapply(c(p1, p2), function(i) {
            if (do::left(i, 1) == "<") {
                i
            }
            else {
                tryCatch(as.numeric(i), warning = function(w) w)
            }
        })
    }
    else if (character2integer) {
        sapply(p1, function(i) {
            if (do::left(i, 1) == "<") {
                i
            }
            else {
                tryCatch(as.numeric(i), warning = function(w) w)
            }
        })
    }
    else if (quadratic) {
        sapply(p2, function(i) {
            if (do::left(i, 1) == "<") {
                i
            }
            else {
                tryCatch(as.numeric(i), warning = function(w) w)
            }
        })
    }
}
```

## `paste_dataframe`

```r
function (...) 
{
    rr <- list(...)
    r1 <- rr[[1]]
    for (i in 2:length(rr)) {
        r1 <- paste1(r1, rr[[i]])
    }
    r1
}
```

## `person_years`

```r
function (data, outcome = NULL, year = NULL, by = NULL, per1000 = FALSE, round = 3) 
{
    if ("survey.design" %in% class(data)) 
        data <- data$variables
    if (is.null(time)) 
        stop(tmcn::toUTF8("<U+5FC5><U+987B><U+6307><U+5B9A>year"))
    if (anyNA(data[, outcome])) 
        stop(tmcn::toUTF8("outcome<U+4E2D><U+6709><U+7F3A><U+5931><U+503C>"))
    ck <- all(tolower(unique(data[, outcome])) %in% c("0", "1", "yes", "no"))
    if (!ck) 
        stop(tmcn::toUTF8("outcome<U+5FC5><U+987B><U+662F>0<U+548C>1,<U+6216><U+8005>yes<U+548C>no"))
    data[, outcome] <- Recode(tolower(data[, outcome]), "1::yes", "0::no")
    if (is.null(by)) {
        (outsum <- sum(data[, outcome] %in% 1))
        (yearsum <- sum(data[, year], na.rm = T))
        (res <- outsum/yearsum)
        if (per1000) 
            res <- res * 1000
        data.frame(variable = outcome, rate = round(res, round))
    }
    else {
        (outsum <- sum(data[, outcome] %in% 1))
        (yearsum <- sum(data[, year], na.rm = T))
        (res <- outsum/yearsum)
        if (per1000) 
            res <- res * 1000
        d1 <- data.frame(variable = "total", rate = round(res, round))
        rbind(d1, do.call(lapply(by, function(bi) {
            ck <- all(tolower(unique(data[, bi])) %in% c("0", "1", "yes", "no"))
            if (!ck) 
                stop(paste0(bi, tmcn::toUTF8("<U+5FC5><U+987B><U+662F>0<U+548C>1,<U+6216><U+8005>yes<U+548C>no")))
            data[, bi] <- Recode(tolower(data[, bi]), "1::yes", "0::no")
            (bu <- do::complete.data(unique(data[, bi])))
            rbind(data.frame(variable = bi, rate = ""), do.call(lapply(bu, function(k) {
                datai <- data[data[, bi] %in% k, ]
                (outsum <- sum(datai[, outcome] %in% "1"))
                (yearsum <- sum(datai[, year], na.rm = T))
                (res <- outsum/yearsum)
                if (per1000) 
                  res <- res * 1000
                data.frame(variable = paste0("", k), rate = round(res, round))
            }), what = rbind))
        }), what = rbind))
    }
}
```

## `prepare_items`

```r
function (items) 
{
    d5 <- get_config_items()
    if (missing(items)) {
        items <- d5
    }
    if (any(grepl(get_config_path(), items))) {
        x <- sapply(items, function(i) do::Replace0(i, do::formal_dir(get_config_path(), TRUE), do::formal_dir(prepare_years(i), 
            TRUE), "/.*"))
        names(x) <- NULL
        x
    }
    else {
        d5[tolower(do::left(d5, max(nchar(items)))) %in% tolower(do::left(items, max(nchar(items))))]
    }
}
```

## `prepare_years`

```r
function (years, range = TRUE) 
{
    ys <- get_config_years()
    if (!missing(years)) 
        years[years %in% "2017-2020"] <- "2019-2020"
    if (missing(years)) 
        years <- ys
    if (any(grepl(get_config_path(), years))) {
        x <- sapply(years, function(i) do::Replace0(i, do::formal_dir(get_config_path(), TRUE), "/.*"))
        names(x) <- NULL
        if (!range) 
            x <- do::Replace0(x, "-.*")
        x
    }
    else {
        if (!missing(years)) {
            years <- do::Replace0(years, "-.*")
            years <- ys[sapply(strsplit(ys, "-"), function(i) any(i %in% years))]
        }
        if (!range) 
            years <- do::Replace0(years, "-.*")
        years
    }
}
```

## `prevalence_byYear`

```r
function (object, y = NULL, stratum = NULL, adjust = NULL, round = 2, xlsx = NULL) 
{
    d <- object
    if ("survey.design" %in% class(object)) 
        d <- object$variables
    if (!"Year" %in% colnames(d)) 
        stop(tmcn::toUTF8("<U+6570><U+636E><U+4E2D><U+6CA1><U+6709>Year<U+5217>"))
    Year.tb <- table(d$Year)
    if (length(Year.tb) == 1) 
        stop(paste0(tmcn::toUTF8("Year<U+53EA><U+6709><U+4E00><U+4E2A><U+503C>,<U+4E5F><U+5C31><U+662F><U+53EA><U+6709><U+4E00><U+4E2A><U+5E74><U+4EFD>,<U+6CA1><U+6709><U+529E><U+6CD5><U+8FDB><U+884C><U+8BA1><U+7B97>: "), 
            names(Year.tb)))
    Year.tb <- sprintf("%s(n=%s)", names(Year.tb), Year.tb)
    Year.col <- paste0("Year", kit::funique(d$Year))
    ck <- tolower(unique(d[, y])) %in% c("no", "yes", 1, 0)
    if (!all(ck)) 
        stop(tmcn::toUTF8("y<U+53EA><U+80FD><U+662F>yes<U+548C>no,<U+6216><U+8005>1<U+548C>0"))
    d$Y100 <- Recode(tolower(d[, y]), "no::0", "yes::100", "1::100", to.numeric = T)
    d$Year.num <- Recode(d$Year, paste0(unique(d$Year), "::", 1:length(unique(d$Year))), to.numeric = T)
    if ("survey.design" %in% class(object)) 
        object$variables <- d
    if ("survey.design" %in% class(object)) {
        fit <- svyglm(Y100 ~ Year - 1, object)
        (est <- digit2character(fit$coefficients, round))
        est <- est[set::and(names(est), Year.col)]
        ci <- data.frame(suppressMessages(confint(fit)))
        ci <- ci[set::and(rownames(ci), Year.col), ]
        ci[ci < 0] <- 0
        ci[, 1] <- digit2character(ci[, 1], round)
        ci[, 2] <- digit2character(ci[, 2], round)
        ci
        l2 <- sprintf("%s(%s,%s)", est, ci[, 1], ci[, 2]) %>% matrix(1) %>% data.frame() %>% do::give_names(do::Replace0(names(est), 
            "Year"))
        total <- data.frame(characters = "total", l2, check.names = F)
        total$"p-trend" <- digit2character(summary(svyglm(factor(Y100) ~ Year.num, family = quasibinomial(), 
            object))$coef[2, 4], round)
        (final <- total)
        if (!is.null(stratum)) {
            res <- lapply(1:length(stratum), function(i) {
                (xi <- stratum[i])
                (xiu <- do::unique_no.NA(kit::funique(d[, xi])))
                ri <- lapply(1:length(xiu), function(j) {
                  if (is.null(adjust)) {
                    st <- sprintf("svyglm(Y100~Year-1,subset(object,%s %s '%s'))", xi, "%in%", xiu[j])
                  }
                  else {
                    adjust <- set::not(adjust, xi)
                    if (length(adjust) == 0) {
                      st <- sprintf("svyglm(Y100~Year-1,subset(object,%s %s '%s'))", xi, "%in%", xiu[j])
                    }
                    else {
                      st <- sprintf("svyglm(Y100~Year-1 + %s,subset(object,%s %s '%s'))", paste0(adjust, 
                        collapse = "+"), xi, "%in%", xiu[j])
                    }
                  }
                  (fit <- eval(parse(text = st)))
                  est <- digit2character(fit$coefficients, round)
                  est <- est[set::and(names(est), Year.col)]
                  ci <- data.frame(suppressMessages(confint(fit)))
                  ci <- ci[set::and(rownames(ci), Year.col), ]
                  ci[ci < 0] <- 0
                  ci[, 1] <- digit2character(ci[, 1], round)
                  ci[, 2] <- digit2character(ci[, 2], round)
                  ci
                  l2 <- sprintf("%s(%s,%s)", est, ci[, 1], ci[, 2]) %>% matrix(1) %>% data.frame() %>% 
                    do::give_names(do::Replace0(names(est), "Year"))
                  rj <- data.frame(characters = xiu[j], l2, check.names = F)
                  if (is.null(adjust)) {
                    st <- sprintf("svyglm(factor(Y100)~Year.num,family = quasibinomial(),\n                          subset(object,%s %s '%s'))", 
                      xi, "%in%", xiu[j])
                    rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                  }
                  else {
                    adjust <- set::not(adjust, xi)
                    if (length(adjust) == 0) {
                      st <- sprintf("svyglm(factor(Y100)~Year.num,family = quasibinomial(),\n                          subset(object,%s %s '%s'))", 
                        xi, "%in%", xiu[j])
                      rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                    }
                    else {
                      st <- sprintf("glm(factor(Y100)~Year.num+%s,family = quasibinomial(),\n                          subset(object,%s %s '%s'))", 
                        paste0(adjust, collapse = "+"), xi, "%in%", xiu[j])
                      rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                    }
                  }
                  rj
                }) %>% do.call(what = plyr::rbind.fill)
                plyr::rbind.fill(data.frame(characters = xi), ri)
            }) %>% do.call(what = plyr::rbind.fill) %>% do::Replace0(" ")
            final <- plyr::rbind.fill(final, res)
        }
    }
    else {
        fit <- glm(Y100 ~ Year - 1, data = d)
        est <- digit2character(fit$coefficients, round)
        est <- est[set::and(names(est), Year.col)]
        ci <- data.frame(suppressMessages(confint(fit)))
        ci <- ci[set::and(rownames(ci), Year.col), ]
        ci[ci < 0] <- 0
        ci[, 1] <- digit2character(ci[, 1], round)
        ci[, 2] <- digit2character(ci[, 2], round)
        l2 <- sprintf("%s(%s,%s)", est, ci[, 1], ci[, 2]) %>% matrix(1) %>% data.frame() %>% do::give_names(do::Replace0(names(est), 
            "Year"))
        total <- data.frame(characters = "total", l2, check.names = F)
        total$"p-trend" <- digit2character(summary(glm(factor(Y100) ~ Year.num, family = binomial(), 
            data = d))$coef[2, 4], round)
        final <- total
        if (!is.null(stratum)) {
            res <- lapply(1:length(stratum), function(i) {
                (xi <- stratum[i])
                xiu <- kit::funique(d[, xi])
                ri <- lapply(1:length(xiu), function(j) {
                  if (is.null(adjust)) {
                    st <- sprintf("glm(Y100~Year-1,data=subset(d,%s %s '%s'))", xi, "%in%", xiu[j])
                  }
                  else {
                    adjust <- set::not(adjust, xi)
                    if (length(adjust) == 0) {
                      st <- sprintf("glm(Y100~Year-1,data=subset(d,%s %s '%s'))", xi, "%in%", xiu[j])
                    }
                    else {
                      st <- sprintf("glm(Y100~Year-1 + %s,data=subset(d,%s %s '%s'))", paste0(adjust, 
                        collapse = "+"), xi, "%in%", xiu[j])
                    }
                  }
                  fit <- eval(parse(text = st))
                  est <- digit2character(fit$coefficients, round)
                  est <- est[set::and(names(est), Year.col)]
                  ci <- data.frame(suppressMessages(confint(fit)))
                  ci <- ci[set::and(rownames(ci), Year.col), ]
                  ci[ci < 0] <- 0
                  ci[, 1] <- digit2character(ci[, 1], round)
                  ci[, 2] <- digit2character(ci[, 2], round)
                  l2 <- sprintf("%s(%s,%s)", est, ci[, 1], ci[, 2]) %>% matrix(1) %>% data.frame() %>% 
                    do::give_names(do::Replace0(names(est), "Year"))
                  rj <- data.frame(characters = xiu[j], l2, check.names = F)
                  if (is.null(adjust)) {
                    st <- sprintf("glm(factor(Y100)~Year.num,family = binomial(),\n                          data=subset(d,%s %s '%s'))", 
                      xi, "%in%", xiu[j])
                    rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                  }
                  else {
                    adjust <- set::not(adjust, xi)
                    if (length(adjust) == 0) {
                      st <- sprintf("glm(factor(Y100)~Year.num,family = binomial(),\n                          data=subset(d,%s %s '%s'))", 
                        xi, "%in%", xiu[j])
                      rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                    }
                    else {
                      st <- sprintf("glm(factor(Y100)~Year.num+%s,family = binomial(),\n                          data=subset(d,%s %s '%s'))", 
                        paste0(adjust, collapse = "+"), xi, "%in%", xiu[j])
                      rj$"p-trend" <- digit2character(summary(eval(parse(text = st)))$coef[2, 4], round)
                    }
                  }
                  rj
                }) %>% do.call(what = plyr::rbind.fill)
                plyr::rbind.fill(data.frame(characters = xi), ri)
            }) %>% do.call(what = plyr::rbind.fill) %>% do::Replace0(" ")
            final <- plyr::rbind.fill(final, res)
        }
    }
    for (i in 1:length(Year.tb)) {
        colnames(final)[colnames(final) == do::Replace0(Year.tb[i], "\\(.*")] <- Year.tb[i]
    }
    if (!is.null(xlsx)) {
        f <- final
        ck <- !is.na(f$`p-trend`)
        ck[1] <- F
        f$characters[ck] <- paste0("    ", f$characters[ck])
        f[is.na(f)] <- ""
        openxlsx::write.xlsx(f, xlsx)
    }
    nhs_view.incidence_byYear(final)
    invisible(final)
}
```

## `quant`

```r
function (x, n, round = 3, cat = TRUE, Q = FALSE) 
{
    if (missing(n)) {
        xx <- rstudioapi::getActiveDocumentContext()
        for (i in (xx$selection[[1]]$range$start[[1]]):1) {
            f6 <- do::Trim_left(xx$contents[i])
            if (f6 == "") {
                (next)(i)
            }
            else if (do::left(f6, 6) == "quant(") {
                rstudioapi::setCursorPosition(list(c(i, 1)), xx$id)
                rstudioapi::insertText("# ")
                x = deparse(substitute(x))
                rstudioapi::setCursorPosition(list(c(i + 1, 1)), xx$id)
                rstudioapi::insertText(sprintf("%sQ <- quant(%s, n = ,Q = TRUE,round=3)\n", x, x))
                rstudioapi::setCursorPosition(list(c(i + 2, 1)), xx$id)
                rstudioapi::insertText(sprintf("%sQ.median <- quant.median(%s, n = ,round=3)\n", x, x))
                rstudioapi::setCursorPosition(list(c(i + 1, nchar(x) * 2 + 18)), xx$id)
            }
        }
    }
    else {
        if (n == 1) 
            return(x)
        s <- sprintf("quantile(x,c(%s),na.rm = TRUE)", paste0(paste0(rep(1:(n - 1), 1), "/", n), collapse = ","))
        cut <- round(eval(parse(text = s)), 3)
        cuts <- c(min(x, na.rm = TRUE), cut, max(x, na.rm = TRUE))
        x2 <- rep(NA, length(x))
        lev <- c()
        for (i in 1:(length(cuts) - 1)) {
            if (i == 1) {
                levi <- sprintf("[%s,%s]", cuts[i], cuts[i + 1])
                lev <- c(lev, levi)
                x2[x <= cuts[i + 1]] <- levi
            }
            else if (i < (length(cuts) - 1)) {
                levi <- sprintf("(%s,%s]", cuts[i], cuts[i + 1])
                x2[x > cuts[i] & x <= cuts[i + 1]] <- levi
                lev <- c(lev, levi)
            }
            else if (i == (length(cuts) - 1)) {
                levi <- sprintf("(%s,%s]", cuts[i], cuts[i + 1])
                lev <- c(lev, levi)
                x2[x > cuts[i]] <- levi
            }
        }
        x2 <- factor(x2, levels = lev)
        if (Q) {
            if (cat) {
                tb <- as.data.frame(table(x2))
                colnames(tb)[1] <- paste0(deparse(substitute(x)), collapse = "")
                tb$Per <- paste0(round(tb$Freq/sum(tb$Freq) * 100, 2), "%")
                tb$Q <- paste0("Q", 1:length(lev))
                print(tb[, c(1, 4, 2, 3)])
            }
            x2 <- Recode(x2, paste0(lev, "::Q", 1:length(lev)))
            x2
        }
        else {
            if (cat) {
                tb <- as.data.frame(table(x2, useNA = "i"))
                colnames(tb)[1] <- paste0(deparse(substitute(x)), collapse = "")
                tb$Per <- paste0(round(tb$Freq/sum(tb$Freq) * 100, 2), "%")
                print(tb)
            }
            x2
        }
    }
}
```

## `quant.median`

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

## `re_order`

```r
function (data, ...) 
{
    data0 <- deparse(substitute(data))
    (st <- do::Replace0(do::knife_right(do::knife_left(deparse(substitute(list(...))), 5), 1), "\"", 
        "'", paste0(data0, " {0,}$ {0,}")))
    ck <- eval(parse(text = sprintf(fmt = "with(%s, order(%s))", data0, st)))
    data[ck, ]
}
```

## `reg_check`

```r
function (...) 
{
    xx <- list(...)
    (vrs <- all.vars(xx[[which(sapply(xx, function(i) inherits(i, "formula")))]]))
    (cls <- colnames(xx[[which(sapply(xx, function(i) inherits(i, "survey.design") | inherits(i, "data.frame")))]]))
    v <- set::not(vrs, cls)
    if (length(v) == 0) 
        v <- "ok"
    print(v)
    invisible(v)
}
```

## `reg_table`

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
UseMethod("reg_table")
```

## `rename`

```r
function (.data, ...) 
{
    UseMethod("rename")
}
```

## `row.counts`

```r
function (data) 
{
    rowSums(!is.na(data))
}
```

## `row.max`

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

## `row.means`

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

## `row.min`

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

## `row.sums`

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

## `row_names`

```r
function (data, names) 
{
    if (missing(names)) 
        return(row.names(data))
    row.names(data) <- names
    data
}
```

## `select`

```r
function (.data, ...) 
{
    UseMethod("select")
}
```

## `select_col`

```r
function (x, ...) 
{
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
        x[, rule, drop = FALSE]
    }
    else if (is.numeric(rule)) {
        x[, rule, drop = FALSE]
    }
    else if (is.character(rule)) {
        x[, set::and(rule, colnames(x)), drop = FALSE]
    }
}
```

## `select_col<-`

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

## `select_row`

```r
function (x, ...) 
UseMethod("select_row")
```

## `select_row<-`

```r
function (x, value) 
{
    x <- select_row(x, value)
    x
}
```

## `setReference`

```r
function (x, value) 
{
    old <- options()
    dd <- old$datadist
    if (is.null(dd)) {
        stop("no datadist can be updated in the options()")
    }
    else {
        if (class(dd)[1] == "datadist") {
            if (is.data.frame(x)) {
                rcsx <- attr(x, "rcsx")
                for (i in rcsx) {
                  value <- x[x$rcsName == i, i]
                  value <- ifelse(is.numeric(value), value, sprintf("'%s'", value))
                  dd$limits["Adjust to", i] <- value
                }
            }
            else {
                dd$limits["Adjust to", x] <- value
            }
            old$datadist <- dd
            options(old)
            return(dd)
        }
        else {
            stop("only used for datadist class")
        }
    }
}
```

## `stratum_model`

```r
function (object, time = NULL, y, x, stratum = NULL, adjust = NULL, p = TRUE, round = 3, view = TRUE, 
    xlsx = NULL, interaction = TRUE) 
{
    (ck <- length(suppressMessages(do::complete.data(unique(object$variables[[y]])))) == 2)
    if (!is.null(time)) {
        regtype <- "cox"
    }
    else if (ck) {
        regtype <- "logistic"
    }
    else {
        regtype <- "linear"
    }
    if (is.numeric(object$variables[, x]) | length(unique(object$variables[, x])) == 2) {
        cla <- c("data.frame", "stratum_model_1")
    }
    else {
        cla <- c("data.frame", "stratum_model_2")
    }
    rt <- do.call(lapply(y, function(i) {
        rt <- stratum_model_i(object, time, y = i, x, stratum, adjust, p, round, interaction)
        if (length(y) > 1) 
            rt[1, 1] <- i
        rt
    }), what = plyr::rbind.fill)
    colnames(rt) <- do::Replace0(colnames(rt), "_add_pvalue_.*")
    class(rt) <- c("stratum_model", "data.frame")
    rt[is.na(rt)] <- ""
    if (view) 
        nhs_view(rt)
    if (!is.null(xlsx)) {
        x <- rt
        ck <- nchar(x[, 2]) == 0
        x[!ck, 1] <- paste0("    ", x[!ck, 1])
        openxlsx::write.xlsx(x, xlsx)
    }
    rm(.stratum_model_object, .stratum_model_object2, envir = .GlobalEnv)
    for (i in 1:ncol(rt)) {
        (ck1 <- grepl(paste0(0:9, collapse = "|"), rt[, i]))
        (ck2 <- grepl("\\)", rt[, i]))
        (ck3 <- grepl("\\(", rt[, i]))
        (ck4 <- grepl(",", rt[, i]))
        (ck <- ck1 & ck2 & ck3 & ck4)
        if (any(ck)) {
            rt[ck, i] <- rt[ck, i] %>% do::Replace(", {1,}", ",") %>% do::Replace("\\( {1,}", "(") %>% 
                do::Trim(pattern = " ")
        }
    }
    attr(rt, "regtype") <- regtype
    class(rt) <- cla
    invisible(rt)
}
```

## `subsetdesign2df`

```r
function (design, ...) 
{
    design <- subset(design, ...)
    design$variables$weights <- (1/design$prob)/mean(1/design$prob)
    design$variables
}
```

## `svy_barplot`

```r
function (x, beside = TRUE, ...) 
{
    (value <- attr(x, "value"))
    if (class(value)[1] == "svystat") {
        bar <- as.data.frame(value)
        bar <- cbind(variable = row.names(bar), bar)
        ggplot(bar, aes_string(x = "variable", y = "mean")) + geom_bar(stat = "identity") + theme(axis.title.x = element_blank())
    }
    else if (class(value)[1] == "svyby") {
        value$bybybyby <- paste0_columns(value[, attr(x, "by")])
        value <- value[, c("bybybyby", attr(x, "x"))]
        id.var <- paste0(attr(x, "by"), collapse = ",")
        colnames(value)[1] <- id.var
        df <- reshape2::melt(value, id.vars = id.var)
        ggplot(data = df, aes_string(x = sprintf("`%s`", id.var), y = "value", fill = "variable")) + 
            geom_bar(stat = "identity", color = "black", position = position_dodge()) + scale_fill_brewer(palette = "Blues")
    }
}
```

## `svy_count`

```r
function (design, x, by = NULL, value = FALSE, per = FALSE, se = FALSE, low.high = FALSE, ci = FALSE, 
    perSQse = FALSE, valueSQper = FALSE, direction = c("h", "v"), na.rm = TRUE, remove.name = FALSE, 
    remove.suffix = FALSE, round = 2) 
{
    if (sum(value, per, se, low.high, ci, perSQse, valueSQper) == 0) 
        ci = TRUE
    x1 <- paste0(x, collapse = " + ")
    for (i in x) {
        if (is.null(levels(design$variable[, i]))) {
            design <- eval(parse(text = sprintf("update(design,%s=factor(%s))", i, i)))
        }
    }
    if (is.null(by)) {
        population <- svy_population(design)
        p <- parse(text = sprintf("survey::svytotal(~%s,design,na.rm=%s)", x1, na.rm))
        r.wt <- data.frame(eval(p))
        if (nrow(r.wt) == 1) 
            colnames(r.wt)[2] <- "SE"
        r.wt$PER <- r.wt$total/population * 100
        r.wt$Low <- (r.wt$total - 1.96 * r.wt$SE)/population * 100
        r.wt$High <- (r.wt$total + 1.96 * r.wt$SE)/population * 100
        r.wt$SE <- r.wt$SE/population
        digit2character(r.wt) <- round
        r.wt$CI <- sprintf("%s(%s,%s)", r.wt$PER, r.wt$Low, r.wt$High)
        r.wt$perSQse <- sprintf("%s(%s)", r.wt$PER, r.wt$SE)
        r.wt$valueSQper <- sprintf("%s(%s)", r.wt$total, r.wt$PER)
        r.wt <- r.wt[, c("total", "PER", "SE", "Low", "High", "CI", "perSQse", "valueSQper")]
        if (!value) 
            r.wt <- drop_col(r.wt, "total")
        if (!per) 
            r.wt <- drop_col(r.wt, "PER")
        if (!se) 
            r.wt <- drop_col(r.wt, "SE")
        if (!low.high) 
            r.wt <- drop_col(r.wt, "Low", "High")
        if (!ci) 
            r.wt <- drop_col(r.wt, "CI")
        if (!perSQse) 
            r.wt <- drop_col(r.wt, "perSQse")
        if (!valueSQper) 
            r.wt <- drop_col(r.wt, "valueSQper")
    }
    else {
        direction <- match.arg(direction)
        for (i in by) {
            if (is.null(levels(design$variable[, i]))) {
                design <- eval(parse(text = sprintf("update(design,%s=factor(%s))", i, i)))
            }
        }
        if (length(by) == 1) {
            design <- update(design, newby = design$variables[, by])
        }
        else if (length(by) > 1) {
            design <- update(design, newby = do::paste0_columns(design$variables[, by], "~~~~~"))
        }
        if (direction == "h") {
            string <- "survey::svyby(~%s, ~newby, design, survey::svytotal,na.rm=%s,keep.names = FALSE,drop.empty.groups = FALSE,na.rm.by = TRUE,na.rm.all=TRUE)"
            (parse <- parse(text = sprintf(string, x1, na.rm)))
            (r.count <- as.data.frame(eval(parse)))
            (r.count <- r.count[, 1:((ncol(r.count) + 1)/2)])
            string <- "survey::svyby(~%s, ~newby, design, survey::svymean,na.rm=%s,keep.names = FALSE,\n        drop.empty.groups = TRUE,na.rm.by = TRUE,na.rm.all=TRUE)"
            (r.per.se <- as.data.frame(eval(parse(text = sprintf(string, x1, na.rm)))))
        }
        else if (direction == "v") {
            string <- "survey::svyby(~%s, ~newby, design, survey::svytotal,na.rm=%s,keep.names = FALSE,drop.empty.groups = FALSE,na.rm.by = TRUE,na.rm.all=TRUE)"
            (parse <- parse(text = sprintf(string, x1, na.rm)))
            (r.count <- as.data.frame(eval(parse)))
            (r.count <- r.count[, 1:((ncol(r.count) + 1)/2)])
            r.per.se <- do.call(lapply(x, function(x1) {
                x1 <- x1
                string <- "survey::svyby(~newby,~%s,  design, survey::svymean,na.rm=%s,keep.names = FALSE,drop.empty.groups = TRUE,na.rm.by = TRUE,na.rm.all=TRUE)"
                (r.per.se.v <- as.data.frame(eval(parse(text = sprintf(string, x1, na.rm)))))
                pv <- c(x1, paste0("newby", unique(design$variables[, "newby"])))
                r.v <- do::Replace0(reshape2::dcast(col_rename(reshape2::melt(r.per.se.v[, colnames(r.per.se.v) %in% 
                  pv], id.var = x1), paste0(x1, ":x")), variable ~ x, value.var = "value"), "newby")
                colnames(r.v)[-1] <- paste0(x1, colnames(r.v)[-1])
                pvse <- c(x1, paste0("se.newby", unique(design$variables[, "newby"])))
                rse.v <- drop_col(do::Replace0(reshape2::dcast(col_rename(reshape2::melt(r.per.se.v[, 
                  colnames(r.per.se.v) %in% pvse], id.var = x1), paste0(x1, ":x")), variable ~ x, value.var = "value"), 
                  "se.newby"), 1)
                colnames(rse.v) <- paste0("se.", x1, colnames(rse.v))
                r.per.se <- cbind(r.v, rse.v)
                colnames(r.per.se)[1] <- "newby"
                to_numeric(r.per.se) <- colnames(r.per.se)
                r.per.se
            }), what = cbind)
            if (length(x) > 1) 
                r.per.se <- r.per.se[, -which(colnames(r.per.se) == "newby")[-1]]
        }
        for (i in colnames(r.per.se)) {
            (se.i <- paste0("se.", i))
            if (se.i %in% colnames(r.per.se)) {
                r.per.se$iiiiiiiiii <- r.per.se[, i] - 1.96 * r.per.se[, se.i]
                colnames(r.per.se)[ncol(r.per.se)] <- paste0("Low.", i)
                r.per.se$iiiiiiiiii <- r.per.se[, i] + 1.96 * r.per.se[, se.i]
                colnames(r.per.se)[ncol(r.per.se)] <- paste0("High.", i)
            }
        }
        dupvar <- which(do::left(colnames(r.count), nchar(x1)) == x1)
        var.value <- do.call(lapply(x, function(i) {
            paste0(i, do::unique_no.NA(as.character(design$variables[, i])))
        }), what = c)
        ck <- colnames(r.per.se) %in% var.value
        colnames(r.per.se)[ck] <- paste0("PER.", colnames(r.per.se)[ck])
        r.per.se[, -1] <- r.per.se[, -1] * 100
        r.count$newby <- as.character(r.count$newby)
        r.per.se$newby <- as.character(r.per.se$newby)
        r.wt <- dplyr::full_join(r.count, r.per.se, "newby")
        r.wt <- cbind(do::col_split(r.wt$newby, "~~~~~", colnames = by), r.wt[, -1])
        for (i in by) {
            if (!is.null(levels(design$variables[, i]))) 
                r.wt[, i] <- factor(r.wt[, i], levels = levels(design$variables[, i]))
        }
        digit2character(r.wt) <- round
        for (i in 1:ncol(r.wt)) {
            (namei <- colnames(r.wt)[i])
            for (x1 in x) {
                if (do::left(namei, nchar(x1)) == x1) {
                  colnames(r.wt)[i] <- sub(x1, paste0(x1, "-"), namei)
                }
                if (do::left(namei, nchar(x1) + 3) == paste0("se.", x1)) {
                  colnames(r.wt)[i] <- paste0(sub(paste0("se.", x1), paste0(x1, "-"), namei), "_SE")
                }
                if (do::left(namei, nchar(x1) + 4) == paste0("PER.", x1)) {
                  colnames(r.wt)[i] <- paste0(sub(paste0("PER.", x1), paste0(x1, "-"), namei), "_PER")
                }
                if (do::left(namei, nchar(x1) + 4) == paste0("Low.", x1)) {
                  colnames(r.wt)[i] <- paste0(sub(paste0("Low.", x1), paste0(x1, "-"), namei), "_Low")
                }
                if (do::left(namei, nchar(x1) + 5) == paste0("High.", x1)) {
                  colnames(r.wt)[i] <- paste0(sub(paste0("High.", x1), paste0(x1, "-"), namei), "_High")
                }
            }
        }
        for (i in colnames(r.wt)) {
            peri <- paste0(i, "_PER")
            Lowi <- paste0(i, "_Low")
            (Highi <- paste0(i, "_High"))
            (SEi <- paste0(i, "_SE"))
            if (peri %in% colnames(r.wt)) {
                r.wt$iiiiii <- sprintf("%s(%s,%s)", r.wt[, peri], r.wt[, Lowi], r.wt[, Highi])
                colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_CI")
                r.wt$iiiiii <- sprintf("%s(%s)", r.wt[, peri], r.wt[, SEi])
                colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_perSQse")
                r.wt$iiiiii <- sprintf("%s(%s)", r.wt[, i], r.wt[, peri])
                colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_valueSQper")
            }
        }
        var.value <- do.call(lapply(x, function(i) {
            paste0(i, "-", do::unique_no.NA(as.character(design$variables[, i])))
        }), what = c)
        ck <- !colnames(r.wt) %in% var.value
        ck[1:length(by)] <- TRUE
        if (!value) 
            r.wt <- r.wt[, ck]
        ck <- do::right(colnames(r.wt), 4) != "_PER"
        ck[1:length(by)] <- TRUE
        if (!per) 
            r.wt <- r.wt[, ck]
        ck <- do::right(colnames(r.wt), 3) != "_SE"
        ck[1:length(by)] <- TRUE
        if (!se) 
            r.wt <- r.wt[, ck]
        ck <- do::right(colnames(r.wt), 3) != "_CI"
        ck[1:length(by)] <- TRUE
        if (!ci) 
            r.wt <- r.wt[, ck]
        ck <- do::right(colnames(r.wt), 8) != "_perSQse"
        ck[1:length(by)] <- TRUE
        if (!perSQse) 
            r.wt <- r.wt[, ck]
        ck <- do::right(colnames(r.wt), 11) != "_valueSQper"
        ck[1:length(by)] <- TRUE
        if (!valueSQper) 
            r.wt <- r.wt[, ck]
        ck <- !(do::right(colnames(r.wt), 4) %in% c("_Low") | do::right(colnames(r.wt), 5) %in% c("_High"))
        ck[1:length(by)] <- TRUE
        if (!low.high) 
            r.wt <- r.wt[, ck]
        if (remove.suffix) {
            rev <- do::reverse(colnames(r.wt))
            colnames(r.wt) <- do::reverse(sub("IC_|ES_|REP_|wol_|hgih_|repQSeulav_|esQSrep_", "", rev))
        }
        if (remove.name) 
            colnames(r.wt) <- sub(paste0(x1, "-"), "", colnames(r.wt))
    }
    r.wt
}
```

## `svy_coxplot`

```r
function (model, ..., ci = FALSE, legend.title = NULL, legend.name = NULL) 
{
    d <- list(...)
    m <- max(sapply(d, length))
    for (i in 1:length(d)) {
        di <- d[[i]]
        mvi <- model$survey.design$variables[, names(d)[i]]
        if (is.character(mvi)) {
            leftdi <- set::not(di, mvi)
            if (length(leftdi) > 0) {
                if (do::cnOS()) 
                  stop(tmcn::toUTF8("<U+53D8><U+91CF> "), names(d)[i], tmcn::toUTF8(" <U+4E2D><U+7684>"), 
                    paste0(leftdi, collapse = ", "), tmcn::toUTF8("<U+5206><U+7C7B><U+4E0D><U+5728><U+539F><U+6570><U+636E><U+5206><U+7C7B><U+4E2D>("), 
                    paste0(do::unique_no.NA(as.character(mvi)), collapse = ", "), ")")
                if (!do::cnOS()) 
                  stop("value of variable ", names(d)[i], ": ", paste0(leftdi, collapse = ", "), "not exist in raw data(", 
                    paste0(do::unique_no.NA(as.character(mvi)), collapse = ", "), ")")
            }
        }
        else if (is.numeric(mvi)) {
            min.di <- min(di, na.rm = TRUE)
            min.mvi <- min(mvi, na.rm = TRUE)
            if (min.di < min.mvi) {
                if (do::cnOS()) 
                  stop(tmcn::toUTF8("<U+53D8><U+91CF> "), names(d)[i], tmcn::toUTF8("<U+7684><U+6700><U+5C0F><U+503C>("), 
                    min.di, tmcn::toUTF8(")<U+5C0F><U+4E8E><U+539F><U+59CB><U+6570><U+636E><U+6700><U+5C0F><U+503C>("), 
                    min.mvi, ")")
                if (!do::cnOS()) 
                  stop("the min value of variable ", names(d)[i], " (", max.di, ") is lower than raw data(", 
                    max.mvi, ")")
            }
            max.di <- max(di, na.rm = TRUE)
            max.mvi <- max(mvi, na.rm = TRUE)
            if (max.di > max.mvi) {
                if (do::cnOS()) 
                  stop(tmcn::toUTF8("<U+53D8><U+91CF> "), names(d)[i], tmcn::toUTF8(" <U+7684><U+6700><U+5927><U+503C>("), 
                    max.di, tmcn::toUTF8(")<U+5927><U+4E8E><U+539F><U+59CB><U+6570><U+636E><U+6700><U+5927><U+503C>("), 
                    max.mvi, ")")
                if (!do::cnOS()) 
                  stop("the max value of variable ", names(d)[i], " (", max.di, ") is over than raw data(", 
                    max.mvi, ")")
            }
        }
        if (length(di < m)) {
            d[[i]] <- c(di, rep(di[length(di)], m - length(di)))
        }
    }
    newdata <- as.data.frame(d)
    left <- set::not(do::model.x(model), colnames(newdata))
    if (length(left) > 0) {
        if (do::cnOS()) 
            stop(paste0(tmcn::toUTF8("<U+6CA1><U+6709><U+8D4B><U+503C><U+7684><U+53D8><U+91CF>:"), paste0(left, 
                collapse = ", ")))
        if (do::cnOS()) 
            stop(paste0("Variable without assignment:", paste0(left, collapse = ", ")))
    }
    x <- predict(object = model, se = ifelse(ci, TRUE, FALSE), type = "curve", newdata = newdata)
    names(x) <- 1:length(x)
    if (!is.null(legend.name)) 
        names(x) <- legend.name
    df <- do.call(lapply(1:length(x), function(i) {
        xi <- x[[i]]
        dflow <- data.frame(x = names(x)[i], time = xi$time, surv = xi$surv)
        if (ci) {
            dflow$ci = exp(log(xi$surv) - 1.96 * sqrt(xi$varlog))
            dflow[1, c("surv", "ci")] <- 1
        }
        else {
            dflow[1, "surv"] <- 1
        }
        dflow <- rbind(dflow[1, ], dflow)
        dfhigh <- data.frame(x = names(x)[i], time = xi$time, surv = xi$surv)
        if (ci) {
            dfhigh$ci = exp(log(xi$surv) + 1.96 * sqrt(xi$varlog))
            dfhigh[1, c("surv", "ci")] <- 1
        }
        else {
            dfhigh[1, "surv"] <- 1
        }
        dfhigh <- rbind(dfhigh[1, ], dfhigh)
        dfhigh <- dfhigh[rev(row.names(dfhigh)), ]
        dfi <- rbind(dflow, dfhigh)
        if (ci) 
            dfi$ci[dfi$ci > 1] <- 1
        dfi
    }), what = rbind)
    df$x <- factor(df$x, levels = names(x))
    var.x <- "x"
    if (!is.null(legend.title)) {
        colnames(df)[1] <- legend.title
        var.x <- legend.title
    }
    head(df)
    p <- ggplot() + geom_line(data = unique(df[, c(var.x, "time", "surv")]), aes_string("time", "surv", 
        group = var.x, color = var.x))
    if (ci) 
        p <- p + geom_polygon(data = df, aes_string("time", "ci", group = var.x, fill = var.x), alpha = 0.20000000000000001)
    p <- p + theme_classic() + xlab("time") + ylab("Survival Probability")
    if (is.null(legend.title)) 
        p <- p + theme(legend.title = element_blank())
    p
}
```

## `svy_design`

```r
function (data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") 
UseMethod("svy_design")
```

## `svy_kmplot`

```r
function (x, ...) 
UseMethod("svy_kmplot")
```

## `svy_mean`

```r
function (design, x, by = NULL, value = FALSE, se = FALSE, low.high = FALSE, ci = FALSE, meanPMse = FALSE, 
    meanSQse = FALSE, geometric = FALSE, round = 2, remove.suffix = FALSE, na.rm = TRUE) 
{
    if (all(isFALSE(value), isFALSE(se), isFALSE(low.high), isFALSE(ci), isFALSE(meanPMse), isFALSE(meanSQse))) 
        meanSQse = T
    x1 <- paste0(x, collapse = " + ")
    if (geometric) 
        design$variables[, x] <- log(design$variables[, x])
    if (is.null(by)) {
        (cmd <- sprintf("survey::svymean(~%s,design,na.rm=%s)", x1, na.rm))
        (passvalue <- eval(parse(text = cmd)))
        (r.wt <- as.data.frame(passvalue))
        colnames(r.wt)[2] <- "SE"
        if (geometric) {
            r.wt$Low <- exp(r.wt$mean - 1.96 * r.wt$SE)
            r.wt$High <- exp(r.wt$mean + 1.96 * r.wt$SE)
            r.wt$mean <- exp(r.wt$mean)
            r.wt$SE <- exp(r.wt$SE)
        }
        else {
            r.wt$Low <- r.wt[, 1] - 1.96 * r.wt[, 2]
            r.wt$High <- r.wt[, 1] + 1.96 * r.wt[, 2]
        }
        digit2character(r.wt) <- round
        r.wt$CI <- sprintf("%s(%s,%s)", r.wt[, 1], r.wt$Low, r.wt$High)
        r.wt$meanPMse <- paste0(r.wt$mean, "<U+00B1>", r.wt$SE)
        r.wt$meanSQse <- paste0(r.wt$mean, "(", r.wt$SE, ")")
        (r.wt <- cbind(xiiiii = row.names(r.wt), r.wt))
        colnames(r.wt)[1] <- "variable"
        row.names(r.wt) <- NULL
        if (!value) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "mean"), drop = FALSE]
        if (!se) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "SE"), drop = FALSE]
        if (!low.high) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "Low", "High"), drop = FALSE]
        if (!ci) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "CI"), drop = FALSE]
        if (!meanPMse) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "meanPMse"), drop = FALSE]
        if (!meanSQse) 
            r.wt <- r.wt[, set::not(colnames(r.wt), "meanSQse"), drop = FALSE]
        attr(r.wt, "value") <- passvalue
        class(r.wt) <- c("svy_mean", "data.frame")
        attr(r.wt, "x") <- x
        return(r.wt)
    }
    else {
        (by1 <- paste0(by, collapse = " + "))
        string <- "survey::svyby(~%s, ~%s, design, survey::svymean,keep.names = FALSE,na.rm=%s,drop.empty.groups = TRUE,na.rm.by = TRUE,na.rm.all=TRUE)"
        cmd <- sprintf(string, x1, by1, na.rm)
        (passvalue <- eval(parse(text = cmd)))
        r.wt <- as.data.frame(passvalue)
        if (length(x) == 1) 
            colnames(r.wt)[ncol(r.wt)] <- paste0("se.", x)
        for (i in 1:length(x)) {
            if (geometric) {
                r.wt$lolll <- exp(r.wt[, x[i]] - 1.96 * r.wt[, paste0("se.", x[i])])
                colnames(r.wt)[ncol(r.wt)] <- paste0(x[i], "_Low")
                r.wt$lolll <- exp(r.wt[, x[i]] + 1.96 * r.wt[, paste0("se.", x[i])])
                colnames(r.wt)[ncol(r.wt)] <- paste0(x[i], "_High")
                r.wt[, x[i]] <- exp(r.wt[, x[i]])
                r.wt[, paste0("se.", x[i])] <- exp(r.wt[, paste0("se.", x[i])])
                colnames(r.wt)[colnames(r.wt) == paste0("se.", x[i])] <- paste0(x[i], "_SE")
            }
            else {
                r.wt$lolll <- r.wt[, x[i]] - 1.96 * r.wt[, paste0("se.", x[i])]
                colnames(r.wt)[ncol(r.wt)] <- paste0(x[i], "_Low")
                r.wt$lolll <- r.wt[, x[i]] + 1.96 * r.wt[, paste0("se.", x[i])]
                colnames(r.wt)[ncol(r.wt)] <- paste0(x[i], "_High")
                colnames(r.wt)[colnames(r.wt) == paste0("se.", x[i])] <- paste0(x[i], "_SE")
            }
        }
        digit2character(r.wt) <- round
        for (i in x) {
            r.wt$CIIIIiiiiii <- sprintf("%s(%s,%s)", r.wt[, i], r.wt[, paste0(i, "_Low")], r.wt[, paste0(i, 
                "_High")])
            colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_CI")
            r.wt$CIIIIiiiiii <- paste0(r.wt[, i], "<U+00B1>", r.wt[, paste0(i, "_SE")])
            colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_meanPMse")
            r.wt$CIIIIiiiiii <- paste0(r.wt[, i], "(", r.wt[, paste0(i, "_SE")], ")")
            colnames(r.wt)[ncol(r.wt)] <- paste0(i, "_meanSQse")
        }
        if (!value) {
            ck <- !colnames(r.wt) %in% x
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (!se) {
            ck <- !colnames(r.wt) %in% paste0(x, "_SE")
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (!low.high) {
            ck <- !colnames(r.wt) %in% c(paste0(x, "_Low"), paste0(x, "_High"))
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (!ci) {
            ck <- !colnames(r.wt) %in% c(paste0(x, "_Low"), paste0(x, "_CI"))
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (!meanPMse) {
            ck <- !colnames(r.wt) %in% paste0(x, "_meanPMse")
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (!meanSQse) {
            ck <- !colnames(r.wt) %in% paste0(x, "_meanSQse")
            ck[1:length(by)] <- TRUE
            r.wt <- r.wt[, ck, drop = FALSE]
        }
        if (remove.suffix) {
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_SE")] <- x
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_Low")] <- x
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_High")] <- x
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_CI")] <- x
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_meanPMse")] <- x
            colnames(r.wt)[colnames(r.wt) %in% paste0(x, "_meanSQse")] <- x
        }
        attr(r.wt, "value") <- passvalue
        attr(r.wt, "by") <- by
        attr(r.wt, "x") <- x
        class(r.wt) <- c("svy_mean", "data.frame")
        return(r.wt)
    }
}
```

## `svy_missValue`

```r
function (design, plot = TRUE) 
{
    ck <- sapply(design$variables, function(i) sum(is.na(i)))
    ck <- ck[ck > 0]
    percent <- paste0(ck, "(", round(ck/nrow(design$variables), 4) * 100, "%)")
    d <- data.frame(variable = names(ck), value = ck/nrow(design$variables), percent = percent)
    if (plot) {
        ggplot(d, aes(y = variable)) + geom_bar(aes(weight = value)) + theme(axis.line = element_blank(), 
            axis.ticks = element_blank(), axis.title = element_blank(), axis.text.x = element_blank()) + 
            scale_x_continuous(limits = c(0, 1.2), expand = c(0, 0)) + geom_text(aes(label = percent), 
            stat = "count", colour = "royalblue")
    }
    else {
        row.names(d) <- NULL
        d
    }
}
```

## `svy_population`

```r
function (design, by = NULL) 
{
    if (is.null(by)) {
        design <- update(design, onlyfortotal = 1)
        return(survey::svytable(~onlyfortotal, design)[[1]])
    }
    else {
        if (length(by) == 1) {
            design <- update(design, xxxxxxyyyyyy = design$variables[, by])
        }
        else {
            design <- update(design, xxxxxxyyyyyy = do::paste0_columns(design$variables[, by], ";;"))
        }
        uv <- unique(design$variables$xxxxxxyyyyyy)
        r <- lapply(uv, function(i) {
            p <- svy_population(subset(design, xxxxxxyyyyyy %in% i))
            data.frame(x = i, population = p)
        }) %>% do.call(what = rbind)
        colnames(r)[1] = by
        r
    }
}
```

## `svy_quantile`

```r
function (design, x, by = NULL, quantile = FALSE, q0.25 = FALSE, q0.5 = FALSE, q0.75 = FALSE, round = 2, 
    remove.prefix = FALSE, remove.suffix = FALSE, na.rm = TRUE) 
{
    if (sum(quantile, q0.25, q0.5, q0.75) == 0) 
        quantile = TRUE
    x1 <- paste0(x, collapse = " + ")
    if (is.null(by)) {
        cmd <- sprintf("survey::svyquantile(~%s,design,c(0.25,0.50,0.75),na.rm=%s)", x1, na.rm)
        passvalue <- eval(parse(text = cmd))
        r.wt <- do.call(lapply(1:length(passvalue), function(i) {
            pi <- digit2character(passvalue[[i]], round)
            (quantilen <- sprintf("%s(%s,%s)", pi[, 1][2], pi[, 1][1], pi[, 1][3]))
            (q0.25 <- sprintf("%s(%s,%s)", pi[1, ][1], pi[1, ][2], pi[1, ][3]))
            (q0.5 <- sprintf("%s(%s,%s)", pi[2, ][1], pi[2, ][2], pi[2, ][3]))
            (q0.75 <- sprintf("%s(%s,%s)", pi[3, ][1], pi[3, ][2], pi[3, ][3]))
            data.frame(variable = names(passvalue)[i], q0.25, q0.5, q0.75, quantile = quantilen)
        }), what = rbind)
        r.wt
        if (!quantile) 
            r.wt <- drop_col(r.wt, "quantile")
        if (!q0.25) 
            r.wt <- drop_col(r.wt, "q0.25")
        if (!q0.5) 
            r.wt <- drop_col(r.wt, "q0.5")
        if (!q0.75) 
            r.wt <- drop_col(r.wt, "q0.75")
        if (remove.prefix) 
            colnames(r.wt) <- do::Replace0(colnames(r.wt), paste0(x, "\\."))
        if (remove.suffix) 
            colnames(r.wt) <- do::Replace0(colnames(r.wt), c("\\.quantile", "\\.0\\.25", "\\.0\\.5", 
                "\\.0\\.75"))
        return(r.wt)
    }
    else {
        by1 <- paste0(by, collapse = " + ")
        svq <- function(x, design, ...) survey::svyquantile(x = x, design = design, quantiles = c(0.25, 
            0.5, 0.75), ...)
        string <- "survey::svyby(~%s, ~%s, design, svq,keep.names = FALSE,na.rm=%s,drop.empty.groups = TRUE,na.rm.by = TRUE,na.rm.all=TRUE)"
        cmd <- sprintf(string, x1, by1, na.rm)
        pi <- eval(parse(text = cmd))
        for (i in x) {
            quantilen <- paste0(i, ".quantile")
            q0.25n <- paste0(i, ".0.25")
            q0.5n <- paste0(i, ".0.5")
            q0.75n <- paste0(i, ".0.75")
            qse0.5 <- paste0("se.", i, ".0.5")
            qse0.25 <- paste0("se.", i, ".0.25")
            qse0.75 <- paste0("se.", i, ".0.75")
            (quantiled <- sprintf("%s(%s,%s)", digit2character(pi[, q0.5n], round), digit2character(pi[, 
                q0.25n], round), digit2character(pi[, q0.75n], round)))
            (q0.25d <- sprintf("%s(%s,%s)", digit2character(pi[, q0.25n], round), digit2character(pi[, 
                q0.25n] - 1.96 * pi[, qse0.25], round), digit2character(pi[, q0.25n] + 1.96 * pi[, qse0.25], 
                round)))
            (q0.5d <- sprintf("%s(%s,%s)", digit2character(pi[, q0.5n], round), digit2character(pi[, 
                q0.5n] - 1.96 * pi[, qse0.5], round), digit2character(pi[, q0.5n] + 1.96 * pi[, qse0.5], 
                round)))
            (q0.75d <- sprintf("%s(%s,%s)", digit2character(pi[, q0.75n], round), digit2character(pi[, 
                q0.75n] - 1.96 * pi[, qse0.75], round), digit2character(pi[, q0.75n] + 1.96 * pi[, qse0.75], 
                round)))
            pi$qaaaaa1 <- q0.25d
            pi$qaaaaa2 <- q0.5d
            pi$qaaaaa3 <- q0.75d
            pi$qaaaaa4 <- quantiled
            pi <- drop_col(pi, c(q0.25n, q0.5n, q0.75n, qse0.5, qse0.25, qse0.75))
            colnames(pi)[(ncol(pi) - 3):ncol(pi)] <- c(q0.25n, q0.5n, q0.75n, quantilen)
        }
        pi
        if (!quantile) 
            pi <- drop_col(pi, paste0(x, ".quantile"))
        if (!q0.25) 
            pi <- drop_col(pi, paste0(x, ".0.25"))
        if (!q0.5) 
            pi <- drop_col(pi, paste0(x, ".0.5"))
        if (!q0.75) 
            pi <- drop_col(pi, paste0(x, ".0.75"))
        if (remove.prefix) 
            colnames(pi) <- do::Replace0(colnames(pi), paste0(x, "\\."))
        if (remove.suffix) 
            colnames(pi) <- do::Replace0(colnames(pi), c("\\.quantile", "\\.0\\.25", "\\.0\\.5", "\\.0\\.75"))
        return(pi)
    }
}
```

## `svy_roc`

```r
function (design, score, class, rescale = TRUE) 
{
    if (rescale) {
        wt <- (1/design$prob)/mean(1/design$prob)
    }
    else {
        wt <- (1/design$prob)
    }
    roc <- WeightedROC::WeightedROC(guess = design$variables[, score], label = design$variables[, class], 
        weight = wt)
    auc <- WeightedROC::WeightedAUC(roc)
    attributes(auc)$roc <- roc
    class(auc) <- c("svy_roc", "character")
    print(auc)
    invisible(auc)
}
```

## `svy_roc_plot`

```r
function (..., color = NULL, lwd = 1.05, legend.title = NULL, legend.names = NULL) 
{
    data <- list(...)
    ck <- length(data) == 1
    if (ck) {
        data <- attr(data[[1]], "roc")
    }
    else {
        if (is.null(legend.names)) 
            legend.names <- 1:length(data)
        for (i in 1:length(data)) {
            di <- attr(data[[i]], "roc")
            di$group <- legend.names[i]
            data[[i]] <- di
        }
        data <- do.call(rbind, data)
        data$group <- factor(data$group, levels = legend.names)
        if (is.null(legend.title)) 
            legend.title <- "group"
        colnames(data)[ncol(data)] <- legend.title
    }
    if (ck) {
        p <- ggplot(data)
        p <- p + geom_line(aes_string(x = "FPR", y = "TPR"), size = lwd)
    }
    else {
        p <- ggplot(data)
        p <- p + geom_line(aes_string(x = "FPR", y = "TPR", color = legend.title), size = lwd)
    }
    if (!is.null(color)) {
        p <- p + scale_color_manual(values = color)
    }
    p + xlab("1 - Specificity") + ylab("Sensitivity") + scale_x_continuous(limits = c(0, 1), expand = c(0, 
        0)) + scale_y_continuous(limits = c(0, 1), expand = c(0, 0)) + coord_fixed() + theme_bw() + geom_abline(intercept = 0, 
        slope = 1, color = "gray", linetype = "dashed", size = 0.75) + theme(legend.position = "right", 
        panel.spacing = unit(2, "lines"))
}
```

## `svy_tableone`

```r
function (design, cv = NULL, cv.nn = NULL, gv = NULL, by = NULL, c_meanSQse = FALSE, c_meanPMse = FALSE, 
    c_ci = FALSE, c_geometric = FALSE, g_N = FALSE, g_percent = FALSE, g_perSQse = FALSE, g_NSQper = FALSE, 
    g_nSQper = FALSE, g_ci = FALSE, g_direction = "v", total = FALSE, round = 2, view = T, xlsx = NULL, 
    pvalue = TRUE) 
{
    (ck.by <- list(cv = cv, gv = gv, cv.nn = cv.nn, by = by))
    if (any(!unlist(ck.by) %in% colnames(design))) {
        str <- paste0(unlist(ck.by)[!unlist(ck.by) %in% colnames(design)], collapse = ", ")
        stop(paste0("nhs<U+4E2D><U+6CA1><U+6709><U+4EE5><U+4E0B><U+53D8><U+91CF>: ", str))
    }
    (ck.by <- ck.by[!sapply(ck.by, is.null)])
    if (length(ck.by) > 1) {
        for (i in 1:(length(ck.by) - 1)) {
            for (j in (i + 1):length(ck.by)) {
                if (names(ck.by)[i] == "cv" & names(ck.by)[j] == "cv.nn") 
                  (next)(j)
                ck.common <- set::and(ck.by[[i]], ck.by[[j]])
                if (length(ck.common) > 0) 
                  stop(names(ck.by)[i], " and ", names(ck.by)[j], " have the same variable: ", paste0(ck.common, 
                    collapse = ", "))
            }
        }
    }
    (v <- c(cv, cv.nn, gv))
    (lv <- set::not(v, colnames(design$variables)))
    if (length(lv) > 0) {
        if (do::cnOS()) 
            stop("<U+53D8><U+91CF> ", paste0(lv, collapse = ", "), " <U+8F93><U+5165><U+9519><U+8BEF>")
        if (!do::cnOS()) 
            stop("variable ", paste0(lv, collapse = ", "), " not exist")
    }
    if (!is.null(by)) {
        if (length(by) == 1) {
            bykeys <- design$variables[, by]
        }
        else {
            bykeys <- paste0_columns(design$variables[, by], collapse = ";")
        }
        design <- update(design, bybybybybyby = bykeys)
        by <- "bybybybybyby"
    }
    r1 <- NULL
    if (!is.null(cv)) {
        r1 <- tb1.contineous.normal(design, cv, by, meanSQse = c_meanSQse, meanPMse = c_meanPMse, ci = c_ci, 
            total, round, pvalue = pvalue, c_geometric = c_geometric)
    }
    r2 <- NULL
    if (!is.null(cv.nn)) {
        r2 <- tb1.contineous.not.normal(design, x = cv.nn, by, total, round, pvalue = pvalue)
    }
    r3 <- NULL
    if (!is.null(gv)) {
        r3 <- tb1.categorial(design, x = gv, by, value = g_N, per = g_percent, perSQse = g_perSQse, NSQper = g_NSQper, 
            nSQper = g_nSQper, ci = g_ci, direction = g_direction, total = total, round, pvalue = pvalue)
    }
    r <- plyr::rbind.fill(r1, r2)
    r <- plyr::rbind.fill(r, r3)
    row.names(r) <- NULL
    if (view) 
        nhs_view.svytableone(r)
    r$variable <- do::Replace(r$variable, "~~~~", "    ")
    if (!is.null(xlsx)) 
        openxlsx::write.xlsx(r, xlsx)
    if (all(r$Pvalue %in% "NULL")) 
        r <- r[, -ncol(r)]
    invisible(r)
}
```

## `svy_uv.cox`

```r
function (design, time, status, x, adjust = NULL, round = 2, view = T, xlsx = NULL) 
{
    r <- do.call(lapply(x, function(i) {
        if (is.null(adjust)) {
            txt <- sprintf("survey::svycoxph(survival::Surv(%s,%s)~%s,design=design)", time, status, 
                i)
        }
        else {
            txt <- sprintf("survey::svycoxph(survival::Surv(%s,%s)~%s+%s,design=design)", time, status, 
                i, paste0(adjust, collapse = "+"))
        }
        di <- reg_table(eval(parse(text = txt)), round = round, view = F, x = x)
    }), what = rbind)
    if (view) 
        nhs_view.regtable(r)
    if (!is.null(xlsx)) 
        openxlsx::write.xlsx(r, xlsx)
    invisible(r)
}
```

## `svy_uv.glm`

```r
function (design, y, x, adjust = NULL, round = 2, view = T, xlsx = NULL) 
{
    r <- do.call(lapply(x, function(i) {
        if (is.null(adjust)) {
            txt <- sprintf("survey::svyglm(%s ~ %s,design = design)", y, i)
        }
        else {
            txt <- sprintf("survey::svyglm(%s ~ %s+%s,design = design)", y, i, paste0(adjust, collapse = "+"))
        }
        reg_table(eval(parse(text = txt)), round = round, view = F, x = x)
    }), what = rbind)
    if (view) 
        nhs_view.regtable(r)
    if (!is.null(xlsx)) 
        openxlsx::write.xlsx(r, xlsx)
    invisible(r)
}
```

## `svy_uv.logit`

```r
function (design, y, x, adjust = NULL, round = 2, family = quasibinomial, view = T, xlsx = NULL) 
{
    r <- do.call(lapply(x, function(i) {
        if (is.null(adjust)) {
            txt <- sprintf("survey::svyglm(%s ~ %s,design = design,family=%s)", y, i, deparse(substitute(family)))
        }
        else {
            txt <- sprintf("survey::svyglm(%s ~ %s + %s,design = design,family=%s)", y, i, paste0(adjust, 
                collapse = "+"), deparse(substitute(family)))
        }
        reg_table(eval(parse(text = txt)), round = round, view = F, x = x)
    }), what = rbind)
    if (view) 
        nhs_view.regtable(r)
    if (!is.null(xlsx)) 
        openxlsx::write.xlsx(r, xlsx)
    invisible(r)
}
```

## `to_NA`

```r
function (x, dont_know = TRUE, refused = TRUE) 
{
    if (is.data.frame(x)) {
        cnms <- do::character.nms(x)
        if (length(cnms) > 0) {
            for (i in cnms) {
                if (any(lookl(funique.noNA(x[, i]), "don\\'{0,}t {0,}know")) | any(lookl(funique.noNA(x[, 
                  i]), "refused"))) {
                  x[, i][tolower(x[, i]) %in% c("don't know", "don't  know", "dont know", "dont  know", 
                    "refused")] <- NA
                }
            }
        }
    }
    else if (is.list(x)) {
        for (j in 1:length(x)) {
            xj <- x[[j]]
            for (i in 1:ncol(xj)) {
                xj[, i][xj[, i] %in% c("don't know", "don't  know", "dont know", "dont  know", "refused")] <- NA
            }
            x[[j]] <- xj
        }
    }
    else if (is.character(x)) {
        x[x %in% c("don't know", "don't  know", "dont know", "dont  know", "refused")] <- NA
    }
    return(x)
}
```

## `to_numeric`

```r
function (x) 
{
    if (is.data.frame(x)) {
        for (i in 1:ncol(x)) {
            xi <- tryCatch(as.numeric(x[, i]), error = function(e) "error", warning = function(w) "error")
            if (all(xi %in% "error")) 
                (next)(i)
            x[, i] <- xi
        }
    }
    else if (is.character(x) | is.factor(x)) {
        x <- as.numeric(as.character(x))
    }
    return(x)
}
```

## `to_numeric<-`

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

## `transfer_fndds`

```r
function () 
{
    fndds <- paste0(get_config_path(), "/fndds")
    mdb <- set::grep_or(list.files(fndds, "mdb", full.names = TRUE, recursive = TRUE), c(prepare_years(), 
        "vitaminae"))
    mdb
    exe <- sprintf(list.files(system.file("data", package = "nhanesR"), "export.exe", full.names = TRUE), 
        fmt = "\"%s\"")
    for (i in 1:length(mdb)) {
        message(i, "/", length(mdb), " ", do::file.name(mdb[i]))
        files <- mdb_files(mdb[i])
        for (j in 1:length(files)) {
            cat(paste0("    ", j, "/", length(files), " ", files[j]), "\n")
            d <- system(paste(exe, mdb[i], files[j]), intern = TRUE)
            di <- data.table::fread(text = d, check.names = TRUE, data.table = FALSE)
            colnames(di) <- tolower(colnames(di))
            yeari <- do::Replace0(mdb[i], fndds, "_ACCESS.*", ".*FNDDS_")
            if (tolower(do::file.name(mdb[i])) == "vitaminae.mdb") 
                yeari = "1999-2000"
            di$Year <- yeari
            tsv <- paste0(do::file.dir(mdb[i]), files[j], ".tsv")
            data.table::fwrite(di, tsv, sep = "\t")
        }
    }
}
```

## `updateKnot`

```r
function (fit, k, data = NULL) 
{
    (rcsx <- rcsx(fit))
    (f0 <- paste0(deparse(fit$call$formula), collapse = ""))
    (f1 <- as.formula(sub(paste0("rcs\\(", rcsx, "[a-zA-Z0-9, \\._]{0,}\\)"), paste0("rcs\\(", rcsx, 
        ",", k, ")"), f0)))
    old <- options()
    if (is.null(data)) 
        data = model.data(fit)
    options(datadist = rms::datadist(data))
    if (!grepl("subset", deparse(fit$call$data))) 
        eval(parse(text = sprintf("%s = data", deparse(fit$call$data))))
    f <- suppressWarnings(update(fit, formula. = f1))
    if (is.null(old$datadist)) 
        options(datadist = NULL)
    options(old)
    f
}
```

## `value.numbar`

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

## `varExtracted`

```r
function (x) 
{
    varnamelabel <- attr(x, "varnameLabel")
    kableExtra::kable_classic(kableExtra::kable_paper(kableExtra::kbl(varnamelabel, escape = FALSE), 
        "striped"), full_width = FALSE)
}
```

## `var_labels`

```r
function (df, order = FALSE) 
{
    x <- sapply(df, expss::var_lab)
    x[sapply(x, is.null)] <- ""
    if (is.list(x)) 
        label <- unlist(x)
    else label <- x
    df <- data.frame(colname = names(x), label = label)
    if (order) 
        df <- df[order(df[, 1]), ]
    row.names(df) = NULL
    df
}
```

## `write.yier`

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

## `youth.obesity`

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


