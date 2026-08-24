# Integrated supporting reference: nhanesr-function-reference/references/expressions-misc.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-misc.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `misc`

## `%=%` [exported]

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

## `DSD` [exported]

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

## `DataDist` [exported]

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

## `Drug` [exported]

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

## `Factor` [exported]

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

## `Flavonoids_download` [exported]

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

## `Frailty49` [exported]

```r
function () 
{
    df <- data.table::fread("Item                                                \t variable                      \t code\n<strong>Cognition</strong>            \t -            \t -\n1. experience confusion/memory problems             \t pfq056,pfq057                 \t yes=1; no=0\n<strong>Dependence</strong>            \t -            \t -\n2. managing money difficulty                        \t pfq060a,pfq061a               \t no difficulty=0;<br/>some difficulty=0.33;<br/>much difficulty=0.66;<br/>unable to do=1\n3. walking for a quarter mile difficulty            \t pfq060b,pfq061b               \t the same to above\n4. walking up ten steps difficulty                  \t pfq060c,pfq061c               \t the same to above\n5. stooping, crouching, kneeling difficulty         \t pfq060d,pfq061d               \t the same to above\n6. lifting or carrying difficulty                   \t pfq060e,pfq061e               \t the same to above\n7. house chore difficulty                           \t pfq060f,pfq061f               \t the same to above\n8. preparing meals difficulty                       \t pfq060g,pfq061g               \t the same to above\n9. standingup from armless chair difficulty        \t pfq060i,pfq061i               \t the same to above\n10. getting in and out of bed difficulty            \t pfq060j,pfq061j               \t the same to above\n11. using fork, knife, drinking from cup difficulty \t pfq060k,pfq061k               \t the same to above\n12. dressing yourself difficulty                    \t pfq060l,pfq061l               \t the same to above\n13. standing for long periods difficulty            \t pfq060m,pfq061m               \t the same to above\n14. grasp/holding small objects difficulty          \t pfq060p,pfq061p               \t the same to above\n15. attending social event difficulty               \t pfq060r,pfq061r               \t the same to above\n16. leisure activity at home difficulty             \t pfq060s,pfq061s               \t the same to above\n17. push or pull large objects difficulty           \t pfq061t                       \t the same to above\n<strong>Depressive Symptoms</strong>            \t -            \t -\n18. have little interest in doing things            \t ciqd008,ciqd009,dpq010        \t <strong>~2003</strong><br />every day,nearly every day = 1<br/>most days = 0.75<br/>about half the days = 0.50<br/>less than half the days = 0.25<br/><strong>2005~</strong><br />nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n19. feeling down, depressed, or hopeless            \t dpq020,ciqd001,ciqd002        \t the same to above\n20. trouble sleeping or sleeping too much           \t dpq030,ciqd025,ciqd026        \t <strong>~2003</strong><br />every night = 1<br/>nearly every night = 0.66<br/>less often = 0.33<br/><strong>2005~</strong><br />nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n21. feeling tired or having little energy           \t dpq040                        \t nearly every day = 1<br/>more than half the days = 0.66<br/>several days = 0.33\n22. poor appetite or overeating                     \t ciqd019,ciqd022,dpq050        \t <strong>~2003</strong><br />yes = 1<br />no = 0<br /><strong>2005~</strong><br />the same to above\n23. feeling bad about yourself                      \t dpq060,ciqd029                \t the same to above\n24. trouble concentrating on things                 \t dpq070,ciqd043                \t the same to above\n<strong>Comorbidities</strong>            \t -            \t -\n25. doctor ever said you had arthritis              \t mcq160a                       \t yes = 1; no = 0\n26. ever told you had thyroid problem               \t mcq160i,mcd160m,mcq160m       \t the same to above\n27. ever told you had chronic bronchitis            \t mcq160k,mcq160p               \t the same to above\n28. ever told you had cancer or malignancy          \t mcq220                        \t the same to above\n29. ever told had congestive heart failure          \t mcq160b                       \t the same to above\n30. ever told you had coronary heart disease        \t mcq160c                       \t the same to above\n31. ever told you had angina/angina pectoris        \t mcq160d                       \t the same to above\n32. ever told you had heart attack                  \t mcq160e                       \t the same to above\n33. ever told you had a stroke                      \t mcq160f                       \t the same to above\n34. ever told you had high blood pressure           \t bpq020                        \t the same to above\n35. doctor told you have diabetes                   \t diq010                        \t yes = 1; no =0; borderline=0.5\n36. ever told you had weak/failing kidneys          \t kiq020,kiq022                 \t yes = 1; no =0\n37. urine leakage bother you?                       \t kiq040,kiq050                 \t <strong>1999<br /></strong>yes = 1 ; no = 0<br /><strong>2001~</strong><br />greatly = 1<br/>very much = 0.75<br/<br />somewhat = 0.5<br/>only a little = 0.25\n<strong>Hospital Utilization and Access to Care</strong>            \t -            \t -\n38. general health condition                        \t huq010                        \t excellent,very good,good = 0<br />fair, poor = 1\n39. health now compared with 1 year ago             \t huq020                        \t about the same, better = 0<br />worse = 1\n40. overnight hospital patient in last year         \t huq070,hud070,huq071          \t yes = 1, no = 0\n41. times receive healthcare over past year         \t huq050,huq051                 \t none = 0; 1-4 = 0.5; >=5 =1\n42. number of prescription medicines taken          \t rxd030,rxduse,rxd295,rxdcount \t no = 0; 1-4 = 0.5; >=5 =1\n<strong>Physical Performance and Anthropometry</strong>            \t -            \t -\n43. body mass index (kg/m^2)                        \t bmxbmi                        \t <18.5, <U+2265>30 = 1<br/>25<U+2013><30 = 0.5<br/>18.5<U+2013>25 = 0\n<strong>Laboratory Values</strong>            \t -            \t -\n44. glycohemoglobin(%)                              \t lbxgh                         \t 0%<U+2013>5.7% = 0, >5.7% = 1\n45. red blood cell count (million cells/ul)         \t lbxrbcsi                      \t M: 4.7<U+2013>6.1 = 0, Other = 1<br />F: 4.2<U+2013>5.4 = 0, Other = 1\n46. hemoglobin (g/dl)                               \t lbxhgb                        \t M: 13.5<U+2013>18 = 0, Other = 1<br />F: 12<U+2013>16 = 0, Other = 1\n47. red cell distribution width (%)                 \t lbxrdw                        \t 11.6<U+2013>14.6 = 0, Other = 1\n48. lymphocyte percent (%)                          \t lbxlypct                      \t 20<U+2013>40 = 0, Other = 1\n49. segmented neutrophils percent (%)               \t lbxnepct                      \t 40<U+2013>80 = 0, Other = 1\n")
    kableExtra::kable_styling(kableExtra::kbl(df, escape = FALSE), full_width = FALSE)
}
```

## `Full_Join` [exported]

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

## `Inner_Join` [exported]

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

## `LS7_Michelle` [internal]

```r
function (years, hei_version = 2010, count, component_score, component_raw) 
{
    years <- prepare_years(years)
    cat("     1/7 Mean Bloog Pressure\n")
    d <- db_blood.pressure(years = years, bpx = FALSE, Year = TRUE)
    d <- drug_anti.Hypertensive(d, take_drug = "drug_hyper", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    cat("     2/7 Total cholesterol\n")
    cat("     3/7 HbA1c\n")
    d <- db_HemalBiochemistry(d, fast_total_cholesterol_mg.dl = "total_chol", HbA1c = TRUE)
    d <- drug_anti.Hyperlipidemic(d, take_drug = "drug_lipid", dup.take.drug = "remove", yes.code = 1, 
        no.code = 0, other.code = 0)
    d <- drug_anti.Diabetic(d, take_drug = "drug_DM", dup.take.drug = "remove", yes.code = 1, no.code = 0, 
        other.code = 0)
    cat("     4/7 Smoking\n")
    d <- diag_smoke(d)
    cat("     5/7 BMI\n")
    d <- db_bodyMeasure(d, BMI_kg.m2 = "BMI")
    cat("     6/7 Physical activity\n")
    d <- dex_PhysicalActivity(data = d, all.5 = TRUE, time = TRUE, direction = "no", total_time = TRUE)
    cat("     7/7 HEi\n")
    d <- dex_HEI(data = d, version = hei_version, method = "ssum", dietary = "tot", day = 1, energy = FALSE, 
        component = FALSE)
    ck_ideal <- (d$bpxsar < 120 & d$bpxdar < 80 & !d$drug_hyper %in% 1)
    ck_intermediate <- (d$bpxsar >= 120 & d$bpxsar < 140) | (d$bpxdar >= 80 & d$bpxdar < 90) | (d$bpxsar < 
        120 & d$bpxdar < 80 & d$drug_hyper %in% 1)
    ck_poor <- d$bpxsar >= 140 | d$bpxdar >= 90
    d$LS7score_bp[ck_ideal] <- 2
    d$LS7score_bp[ck_intermediate] <- 1
    d$LS7score_bp[ck_poor] <- 0
    ck_ideal <- d$total_chol < 200 & !d$drug_lipid %in% 1
    ck_intermediate <- (d$total_chol < 200 & d$drug_lipid %in% 1) | (d$total_chol >= 200 & d$total_chol < 
        240)
    ck_poor <- d$total_chol >= 240
    d$LS7score_total_chol[ck_ideal] <- 2
    d$LS7score_total_chol[ck_intermediate] <- 1
    d$LS7score_total_chol[ck_poor] <- 0
    ck_ideal <- d$HbA1c < 5.7000000000000002 & !d$drug_DM %in% 1
    ck_intermediate <- (d$HbA1c < 5.7000000000000002 & d$drug_DM %in% 1) | (d$HbA1c >= 5.7000000000000002 & 
        d$HbA1c < 6.4000000000000004)
    ck_poor <- d$HbA1c > 6.4000000000000004
    d$LS7score_HbA1c[ck_ideal] <- 2
    d$LS7score_HbA1c[ck_intermediate] <- 1
    d$LS7score_HbA1c[ck_poor] <- 0
    d$LS7score_smoke[d$smoke == "never"] <- 2
    d$LS7score_smoke[d$smoke == "former"] <- 1
    d$LS7score_smoke[d$smoke == "now"] <- 0
    d$LS7score_BMI[d$BMI < 25] <- 2
    d$LS7score_BMI[d$BMI >= 25 & d$BMI < 30] <- 1
    d$LS7score_BMI[d$BMI >= 30] <- 0
    d$LS7score_PA[d$PA_total_time >= 150] <- 2
    d$LS7score_PA[d$PA_total_time >= 1 & d$PA_total_time < 150] <- 1
    d$LS7score_PA[d$PA_total_time < 1] <- 0
    hei <- set::grep_and(colnames(d), c("hei", "total_score"))
    d$LS7score_HEI[d[, hei] > 80] <- 2
    d$LS7score_HEI[d[, hei] >= 50 & d[, hei] < 80] <- 1
    d$LS7score_HEI[d[, hei] < 50] <- 0
    score_matrix <- d[, set::grep_and(colnames(d), "LS7score_")]
    d$LS7_total_score <- row.sums(score_matrix)
    d$LS7_count <- row.counts(score_matrix)
    score_matrix[score_matrix != 2] <- 0
    score_matrix[score_matrix == 2] <- 1
    d$ideal_count <- row.sums(score_matrix)
    var <- c("Year", "seqn", "LS7_total_score", "ideal_count")
    if (count) 
        var <- c(var, "LS7_count")
    if (component_score) 
        var <- c(var, set::grep_and(colnames(d), "LS7score_"))
    if (component_raw) 
        var <- c(var, "bpxsar", "bpxdar", "drug_hyper", "total_chol", "HbA1c", "drug_lipid", "drug_DM", 
            "smoke", "BMI", "PA_total_time", hei)
    head(d)
    d <- d[, var]
    d
}
```

## `Left_Join` [exported]

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

## `NULLcodebook` [internal]

```r
function (firs_publish, last_revise, file) 
{
    df <- data.frame(variable = 1, code = 2, label = 3)
    df <- df[-c(1:nrow(df)), ]
    write.table(firs_publish, file, row.names = FALSE, col.names = FALSE, quote = FALSE)
    write.table(last_revise, file, row.names = FALSE, col.names = FALSE, append = TRUE, quote = FALSE)
    suppressWarnings(write.table(df, file, append = TRUE, sep = "\t", row.names = FALSE))
}
```

## `Qnplot` [exported]

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

## `Recode` [exported]

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

## `Replace0` [internal]

```r
function (data, ..., ignore.case = F) 
{
    from <- c(...)
    Replace1 <- function(data, from, to) {
        if (any(is.data.frame(data), is.matrix(data))) {
            for (i in 1:ncol(data)) {
                data[, i] = gsub(from, to, data[, i], ignore.case = ignore.case)
            }
        }
        else {
            data = gsub(from, to, data, ignore.case = ignore.case)
        }
        data
    }
    for (i in 1:length(from)) {
        data = Replace1(data, from[i], to = "")
    }
    data
}
```

## `Right_Join` [exported]

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

## `add_col` [exported]

```r
function (data, colname = NULL, value = NULL, condition = NULL, position = NULL) 
UseMethod("add_col")
```

## `add_color_to_text` [internal]

```r
function (text, key, color) 
{
    (first <- tmcn::toUTF8("<U+9B51>"))
    (mid <- tmcn::toUTF8("<U+9B45>"))
    (last <- tmcn::toUTF8("<U+9B49>"))
    names(color) <- tolower(key)
    from <- unique(unlist(lapply(key, function(i) stringr::str_extract_all(text, stringr::fixed(i, TRUE)))))
    if (length(from) == 0) 
        return(text)
    to <- sprintf("%s%s%s%s%s", first, color[tolower(from)], mid, from, last)
    names(to) <- from
    to
    text
    stringr::str_replace_all(text, to)
}
```

## `add_masc` [internal]

```r
function (d, ex_col = NULL) 
{
    for (i in colnames(d)) {
        if (i %in% ex_col) 
            (next)(i)
        ck <- is.na(d[, i])
        if (any(ck)) {
            if (!is.null(levels(d[, i]))) 
                (next)(i)
            d[ck, i] <- paste0(rnorm(sum(ck)), "zhangjing-zhishi-yikeshu", rnorm(sum(ck)))
        }
    }
    d
}
```

## `add_style` [internal]

```r
function (x, selector = NULL, n = NULL, pseudo = NULL, pseudo.link = FALSE, pseudo.visited = FALSE, pseudo.hover = FALSE, 
    pseudo.active = FALSE, pseudo.checked = FALSE, pseudo.disabled = FALSE, pseudo.empty = FALSE, pseudo.enabled = FALSE, 
    pseudo.first_child = FALSE, pseudo.first_of_type = FALSE, pseudo.focus = FALSE, pseudo.in_range = FALSE, 
    pseudo.invalid = FALSE, pseudo.lang = FALSE, pseudo.last_child = FALSE, pseudo.last_of_type = FALSE, 
    pseudo.not = FALSE, pseudo.nth_child = FALSE, pseudo.nth_last_child = FALSE, pseudo.nth_last_of_type = FALSE, 
    pseudo.nth_of_type = FALSE, pseudo.only_of_type = FALSE, pseudo.only_child = FALSE, pseudo.optional = FALSE, 
    pseudo.out_of_range = FALSE, pseudo.read_only = FALSE, pseudo.read_write = FALSE, pseudo.required = FALSE, 
    pseudo.root = FALSE, pseudo.target = FALSE, pseudo.valid = FALSE, pseudo.after = FALSE, pseudo.before = FALSE, 
    pseudo.first_letter = FALSE, pseudo.first_line = FALSE, pseudo.selection = FALSE, pseuded.selector = NULL, 
    opacity = NULL, background = NULL, background_color = NULL, background_image = NULL, background_size = NULL, 
    background_size.cover = FALSE, background_size.contain = FALSE, background_repeat = NULL, background_repeat.no_repeat = FALSE, 
    background_repeat.repeat_x = FALSE, background_repeat.repeat_y = FALSE, background_position = NULL, 
    background_attachment.fixed = FALSE, background_attachment.scroll = FALSE, background_clip.border = FALSE, 
    background_clip.padding = FALSE, background_clip.content = FALSE, background_origin = NULL, background_origin.border_box = FALSE, 
    background_origin.padding_box = FALSE, background_origin.content_box = FALSE, border = NULL, border_style.dashed = FALSE, 
    border_style.dotted = FALSE, border_style.double = FALSE, border_style.groove = FALSE, border_style.hidden = FALSE, 
    border_style.inset = FALSE, border_style.none = FALSE, border_style.outset = FALSE, border_style.ridge = FALSE, 
    border_style.solid = FALSE, border_left_style.dashed = FALSE, border_left_style.dotted = FALSE, border_left_style.double = FALSE, 
    border_left_style.groove = FALSE, border_left_style.hidden = FALSE, border_left_style.inset = FALSE, 
    border_left_style.none = FALSE, border_left_style.outset = FALSE, border_left_style.ridge = FALSE, 
    border_left_style.solid = FALSE, border_right_style.dashed = FALSE, border_right_style.dotted = FALSE, 
    border_right_style.double = FALSE, border_right_style.groove = FALSE, border_right_style.hidden = FALSE, 
    border_right_style.inset = FALSE, border_right_style.none = FALSE, border_right_style.outset = FALSE, 
    border_right_style.ridge = FALSE, border_right_style.solid = FALSE, border_top_style.dashed = FALSE, 
    border_top_style.dotted = FALSE, border_top_style.double = FALSE, border_top_style.groove = FALSE, 
    border_top_style.hidden = FALSE, border_top_style.inset = FALSE, border_top_style.none = FALSE, border_top_style.outset = FALSE, 
    border_top_style.ridge = FALSE, border_top_style.solid = FALSE, border_bottom_style.dashed = FALSE, 
    border_bottom_style.dotted = FALSE, border_bottom_style.double = FALSE, border_bottom_style.groove = FALSE, 
    border_bottom_style.hidden = FALSE, border_bottom_style.inset = FALSE, border_bottom_style.none = FALSE, 
    border_bottom_style.outset = FALSE, border_bottom_style.ridge = FALSE, border_bottom_style.solid = FALSE, 
    border_width = NULL, border_color = NULL, border_radius = NULL, border_left_width = NULL, border_left_color = NULL, 
    border_left_radius = NULL, border_right_width = NULL, border_right_color = NULL, border_right_radius = NULL, 
    border_top_width = NULL, border_top_color = NULL, border_top_radius = NULL, border_bottom_width = NULL, 
    border_bottom_color = NULL, border_bottom_radius = NULL, border_collapse.separate = FALSE, border_collapse.collapse = FALSE, 
    border_collapse.inherit = FALSE, margin = NULL, margin_top = NULL, margin_right = NULL, margin_bottom = NULL, 
    margin_left = NULL, padding = NULL, padding_top = NULL, padding_right = NULL, padding_bottom = NULL, 
    padding_left = NULL, height = NULL, width = NULL, max_width = NULL, min_width = NULL, max_height = NULL, 
    min_height = NULL, outline_style.dotted = FALSE, outline_style.dashed = FALSE, outline_style.solid = FALSE, 
    outline_style.double = FALSE, outline_style.groove = FALSE, outline_style.ridge = FALSE, outline_style.inset = FALSE, 
    outline_style.outset = FALSE, outline_style.none = FALSE, outline_style.hidden = FALSE, outline_color = NULL, 
    outline_width = NULL, outline_offset = NULL, outline = NULL, color = NULL, text_align.center = FALSE, 
    text_align.left = FALSE, text_align.right = FALSE, text_align.justify = FALSE, text_direction.rtl = FALSE, 
    vertical_align.top = FALSE, vertical_align.middle = FALSE, vertical_align.bottom = FALSE, text_decoration.none = FALSE, 
    text_decoration.overline = FALSE, text_decoration.line_through = FALSE, text_decoration.underline = FALSE, 
    text_transform.uppercase = FALSE, text_transform.lowercase = FALSE, text_transform.capitalize = FALSE, 
    text_indent = NULL, letter_spacing = NULL, word_spacing = NULL, line_height = NULL, white_space.pre = FALSE, 
    white_space.nowrap = FALSE, white_space.pre_warp = FALSE, white_space.pre_line = FALSE, white_space.inherit = FALSE, 
    text_shadow = NULL, overflow = NULL, overflow.hidden = FALSE, overflow.scroll = FALSE, overflow.auto = FALSE, 
    overflow.inherit = FALSE, overflow_x = NULL, overflow_x.hidden = FALSE, overflow_x.scroll = FALSE, 
    overflow_x.auto = FALSE, overflow_x.inherit = FALSE, overflow_y = NULL, overflow_y.hidden = FALSE, 
    overflow_y.scroll = FALSE, overflow_y.auto = FALSE, overflow_y.inherit = FALSE, text_overflow.clip = FALSE, 
    text_overflow.ellipsis = FALSE, text_overflow.string = FALSE, font_size = NULL, font_family = NULL, 
    font_family.Serif = FALSE, font_family.Times_New_Roman = FALSE, font_family.Georgia = FALSE, font_family.Garamond = FALSE, 
    font_family.Sans_serif = FALSE, font_family.Arial = FALSE, font_family.Verdana = FALSE, font_family.Helvetica = FALSE, 
    font_family.Monospace = FALSE, font_family.Courier_New = FALSE, font_family.Lucida_Console = FALSE, 
    font_family.Monaco = FALSE, font_family.Cursive = FALSE, font_family.Brush_Script_MT = FALSE, font_family.Lucida_Handwriting = FALSE, 
    font_family.Fantasy = FALSE, font_family.Copperplate = FALSE, font_family.Papyrus = FALSE, font_style.normal = FALSE, 
    font_style.italic = FALSE, font_style.oblique = FALSE, font_weight.bold = FALSE, font_weight.normal = FALSE, 
    font_variant.normal = FALSE, font_variant.small_caps = FALSE, list_style_type.none = FALSE, list_style_type.circle = FALSE, 
    list_style_type.square = FALSE, list_style_type.upper_roman = FALSE, list_style_type.lower_alpha = FALSE, 
    list_style_image = NULL, list_style_position.outside = FALSE, list_style_position.inside = FALSE, 
    display = NULL, display.none = FALSE, display.block = FALSE, display.inline = FALSE, display.inline_block = FALSE, 
    display.table_cell = FALSE, display.flex = FALSE, visibility = NULL, visibility.visible = FALSE, 
    visibility.hidden = FALSE, visibility.collapse = FALSE, visibility.inherit = FALSE, position = NULL, 
    position.static = FALSE, position.relative = FALSE, position.fixed = FALSE, position.absolute = FALSE, 
    position.sticky = FALSE, top = NULL, bottom = NULL, left = NULL, right = NULL, go_top = NULL, go_bottom = NULL, 
    go_left = NULL, go_right = NULL, z_index = NULL, float = NULL, float.left = FALSE, float.right = FALSE, 
    float.none = FALSE, float.inherit = FALSE, clear = NULL, clear.both = FALSE, box_sizing = NULL, box_sizing.border_box = FALSE, 
    box_sizing.content_box = FALSE, box_sizing.inherit = FALSE, content = NULL, transform = NULL, transform.translate = FALSE, 
    transform.rotate = FALSE, transform.scaleX = FALSE, transform.scaleY = FALSE, transform.scale = FALSE, 
    transform.skewX = FALSE, transform.skewY = FALSE, transform.skew = FALSE, transform.matrix = FALSE, 
    transition = NULL, transition_delay = NULL, transition_duration = NULL, transition_property = NULL, 
    transition_timing_function = NULL, transition_timing_function.ease = FALSE, transition_timing_function.linear = FALSE, 
    transition_timing_function.ease_in = FALSE, transition_timing_function.ease_out = FALSE, transition_timing_function.ease_in_out = FALSE, 
    animation = NULL, animation_fadenum = NULL, animation_name = NULL, animation_duration = NULL, animation_delay = NULL, 
    animation_iteration_count = NULL, animation_direction = NULL, animation_timing_function = NULL, animation_fill_mode = NULL, 
    resize = NULL, resize.none = FALSE, resize.both = FALSE, resize.horizontal = FALSE, resize.vertical = FALSE, 
    flex_flow = NULL, flex_direction = NULL, flex_direction.column = FALSE, flex_direction.row = FALSE, 
    flex_direction.row_reverse = FALSE, flex_direction.column_reverse = FALSE, flex_wrap = NULL, flex_wrap.nowrap = FALSE, 
    flex_wrap.wrap = FALSE, flex_wrap.wrap_reverse = FALSE, justify_content = NULL, justify_content.center = FALSE, 
    justify_content.flex_start = FALSE, justify_content.flex_end = FALSE, justify_content.space_evenly = FALSE, 
    justify_content.space_around = FALSE, justify_content.space_between = FALSE, align_items = NULL, 
    align_items.center = FALSE, align_items.flex_start = FALSE, align_items.flex_end = FALSE, align_items.stretch = FALSE, 
    align_items.baseline = FALSE, align_content = NULL, align_content.space_between = FALSE, align_content.space_around = FALSE, 
    align_content.stretch = FALSE, align_content.center = FALSE, align_content.flex_start = FALSE, align_content.flex_end = FALSE, 
    align_self = NULL, align_self.space_between = FALSE, align_self.space_around = FALSE, align_self.stretch = FALSE, 
    align_self.center = FALSE, align_self.flex_start = FALSE, align_self.flex_end = FALSE, order = NULL, 
    flex = NULL, flex_grow = NULL, flex_shrink = NULL, flex_basis = NULL, grid_template_columns = NULL, 
    grid_template_rows = NULL, grid_gap = NULL, grid_area = NULL, grid_column_gap = NULL, grid_row_gap = NULL, 
    grid_column = NULL, grid_column_start = NULL, grid_column_end = NULL, grid_row = NULL, grid_row_start = NULL, 
    grid_row_end = NULL, cursor = NULL) 
{
    border_style <- NULL
    if (border_style.dashed) 
        border_style <- c(border_style, "dashed")
    if (border_style.dotted) 
        border_style <- c(border_style, "dotted")
    if (border_style.double) 
        border_style <- c(border_style, "double")
    if (border_style.groove) 
        border_style <- c(border_style, "groove")
    if (border_style.hidden) 
        border_style <- c(border_style, "hidden")
    if (border_style.inset) 
        border_style <- c(border_style, "inset")
    if (border_style.none) 
        border_style <- c(border_style, "none")
    if (border_style.outset) 
        border_style <- c(border_style, "outset")
    if (border_style.ridge) 
        border_style <- c(border_style, "ridge")
    if (border_style.solid) 
        border_style <- c(border_style, "solid")
    if (!is.null(border_style)) {
        border_style <- border_style[1:min(length(border_style), 4)]
        border_style <- paste0(border_style, collapse = " ")
    }
    if (background_repeat.no_repeat) 
        background_repeat <- c(background_repeat, "no-repeat")
    if (background_repeat.repeat_x) 
        background_repeat <- c(background_repeat, "repeat-x")
    if (background_repeat.repeat_y) 
        background_repeat <- c(background_repeat, "repeat-y")
    if (!is.null(background_repeat)) 
        background_repeat <- paste0(background_repeat, collapse = ",")
    background_attachment <- NULL
    if (background_attachment.fixed) 
        background_attachment <- "fixed"
    if (background_attachment.scroll) 
        background_attachment <- "scroll"
    if (!is.null(background_attachment)) 
        background_attachment <- background_attachment[1]
    background_clip <- NULL
    if (background_clip.border) 
        background_clip <- "border-box"
    if (background_clip.padding) 
        background_clip <- "padding-box"
    if (background_clip.content) 
        background_clip <- "content-box"
    if (!is.null(background_clip)) 
        background_clip <- background_clip[1]
    border_left_style <- NULL
    if (border_left_style.dashed) 
        border_left_style = "dashed"
    if (border_left_style.dotted) 
        border_left_style = "dotted"
    if (border_left_style.double) 
        border_left_style = "double"
    if (border_left_style.groove) 
        border_left_style = "groove"
    if (border_left_style.hidden) 
        border_left_style = "hidden"
    if (border_left_style.inset) 
        border_left_style = "inset"
    if (border_left_style.none) 
        border_left_style = "none"
    if (border_left_style.outset) 
        border_left_style = "outset"
    if (border_left_style.ridge) 
        border_left_style = "ridge"
    if (border_left_style.solid) 
        border_left_style = "solid"
    border_right_style <- NULL
    if (border_right_style.dashed) 
        border_right_style = "dashed"
    if (border_right_style.dotted) 
        border_right_style = "dotted"
    if (border_right_style.double) 
        border_right_style = "double"
    if (border_right_style.groove) 
        border_right_style = "groove"
    if (border_right_style.hidden) 
        border_right_style = "hidden"
    if (border_right_style.inset) 
        border_right_style = "inset"
    if (border_right_style.none) 
        border_right_style = "none"
    if (border_right_style.outset) 
        border_right_style = "outset"
    if (border_right_style.ridge) 
        border_right_style = "ridge"
    if (border_right_style.solid) 
        border_right_style = "solid"
    border_top_style <- NULL
    if (border_top_style.dashed) 
        border_top_style = "dashed"
    if (border_top_style.dotted) 
        border_top_style = "dotted"
    if (border_top_style.double) 
        border_top_style = "double"
    if (border_top_style.groove) 
        border_top_style = "groove"
    if (border_top_style.hidden) 
        border_top_style = "hidden"
    if (border_top_style.inset) 
        border_top_style = "inset"
    if (border_top_style.none) 
        border_top_style = "none"
    if (border_top_style.outset) 
        border_top_style = "outset"
    if (border_top_style.ridge) 
        border_top_style = "ridge"
    if (border_top_style.solid) 
        border_top_style = "solid"
    border_bottom_style <- NULL
    if (border_bottom_style.dashed) 
        border_bottom_style = "dashed"
    if (border_bottom_style.dotted) 
        border_bottom_style = "dotted"
    if (border_bottom_style.double) 
        border_bottom_style = "double"
    if (border_bottom_style.groove) 
        border_bottom_style = "groove"
    if (border_bottom_style.hidden) 
        border_bottom_style = "hidden"
    if (border_bottom_style.inset) 
        border_bottom_style = "inset"
    if (border_bottom_style.none) 
        border_bottom_style = "none"
    if (border_bottom_style.outset) 
        border_bottom_style = "outset"
    if (border_bottom_style.ridge) 
        border_bottom_style = "ridge"
    if (border_bottom_style.solid) 
        border_bottom_style = "solid"
    if (background_origin.border_box) 
        background_origin <- "border_box"
    if (background_origin.padding_box) 
        background_origin <- "padding_box"
    if (background_origin.content_box) 
        background_origin <- "content_box"
    border_collapse <- NULL
    if (border_collapse.separate) 
        border_collapse <- "separate"
    if (border_collapse.collapse) 
        border_collapse <- "collapse"
    if (border_collapse.inherit) 
        border_collapse <- "inherit"
    outline_style <- NULL
    if (outline_style.dotted) 
        outline_style <- "dotted"
    if (outline_style.dashed) 
        outline_style <- "dashed"
    if (outline_style.solid) 
        outline_style <- "solid"
    if (outline_style.double) 
        outline_style <- "double"
    if (outline_style.groove) 
        outline_style <- "groove"
    if (outline_style.ridge) 
        outline_style <- "ridge"
    if (outline_style.inset) 
        outline_style <- "inset"
    if (outline_style.outset) 
        outline_style <- "outset"
    if (outline_style.none) 
        outline_style <- "none"
    if (outline_style.hidden) 
        outline_style <- "hidden"
    text_align <- NULL
    if (text_align.center) 
        text_align <- "center"
    if (text_align.left) 
        text_align <- "left"
    if (text_align.right) 
        text_align <- "right"
    if (text_align.justify) 
        text_align <- "justify"
    text_direction <- NULL
    if (text_direction.rtl) 
        text_direction <- "rtl"
    vertical_align <- NULL
    if (vertical_align.top) 
        vertical_align <- "top"
    if (vertical_align.middle) 
        vertical_align <- "middle"
    if (vertical_align.bottom) 
        vertical_align <- "bottom"
    text_decoration <- NULL
    if (text_decoration.none) 
        text_decoration <- "none"
    if (text_decoration.overline) 
        text_decoration <- "overline"
    if (text_decoration.line_through) 
        text_decoration <- "line-through"
    if (text_decoration.underline) 
        text_decoration <- "underline"
    text_transform <- NULL
    if (text_transform.uppercase) 
        text_transform <- "uppercase"
    if (text_transform.lowercase) 
        text_transform <- "lowercase"
    if (text_transform.capitalize) 
        text_transform <- "capitalize"
    white_space <- NULL
    if (white_space.pre) 
        white_space <- "pre"
    if (white_space.nowrap) 
        white_space <- "nowrap"
    if (white_space.pre_warp) 
        white_space <- "pre-warp "
    if (white_space.pre_line) 
        white_space <- "pre-line"
    if (white_space.inherit) 
        white_space <- "inherit"
    text_overflow <- NULL
    if (text_overflow.clip) 
        text_overflow <- "clip"
    if (text_overflow.ellipsis) 
        text_overflow <- "ellipsis"
    if (text_overflow.string) 
        text_overflow <- "string"
    if (overflow.hidden) 
        overflow <- "hidden"
    if (overflow.scroll) 
        overflow <- "scroll"
    if (overflow.auto) 
        overflow <- "auto"
    if (overflow.inherit) 
        overflow <- "inherit"
    if (overflow_x.hidden) 
        overflow_x <- "hidden"
    if (overflow_x.scroll) 
        overflow_x <- "scroll"
    if (overflow_x.auto) 
        overflow_x <- "auto"
    if (overflow_x.inherit) 
        overflow_x <- "inherit"
    if (overflow_y.hidden) 
        overflow_y <- "hidden"
    if (overflow_y.scroll) 
        overflow_y <- "scroll"
    if (overflow_y.auto) 
        overflow_y <- "auto"
    if (overflow_y.inherit) 
        overflow_y <- "inherit"
    if (font_family.Serif) 
        font_family <- "Serif"
    if (font_family.Times_New_Roman) 
        font_family <- "'Times New Roman'"
    if (font_family.Georgia) 
        font_family <- "Georgia"
    if (font_family.Garamond) 
        font_family <- "Garamond"
    if (font_family.Sans_serif) 
        font_family <- "\"Sans serif\""
    if (font_family.Arial) 
        font_family <- "Arial"
    if (font_family.Verdana) 
        font_family <- "Verdana"
    if (font_family.Helvetica) 
        font_family <- "Helvetica"
    if (font_family.Monospace) 
        font_family <- "Monospace"
    if (font_family.Courier_New) 
        font_family <- "\"Courier New\""
    if (font_family.Lucida_Console) 
        font_family <- "\"Lucida Console\""
    if (font_family.Monaco) 
        font_family <- "Monaco"
    if (font_family.Cursive) 
        font_family <- "Cursive"
    if (font_family.Brush_Script_MT) 
        font_family <- "\"Brush Script MT\""
    if (font_family.Lucida_Handwriting) 
        font_family <- "\"Lucida Handwriting\""
    if (font_family.Fantasy) 
        font_family <- "Fantasy"
    if (font_family.Copperplate) 
        font_family <- "Copperplate"
    if (font_family.Papyrus) 
        font_family <- "Papyrus"
    font_style <- NULL
    if (font_style.normal) 
        font_style <- "normal"
    if (font_style.italic) 
        font_style <- "italic"
    if (font_style.oblique) 
        font_style <- "oblique"
    font_weight <- NULL
    if (font_weight.bold) 
        font_weight <- "bold"
    if (font_weight.normal) 
        font_weight <- "normal"
    font_variant <- NULL
    if (font_variant.normal) 
        font_variant <- "normal"
    if (font_variant.small_caps) 
        font_variant <- "small-caps"
    list_style_type <- NULL
    if (list_style_type.none) 
        list_style_type <- "none"
    if (list_style_type.circle) 
        list_style_type <- "circle"
    if (list_style_type.square) 
        list_style_type <- "square"
    if (list_style_type.upper_roman) 
        list_style_type <- "upper-roman"
    if (list_style_type.lower_alpha) 
        list_style_type <- "lower-alpha"
    if (!is.null(list_style_image)) 
        list_style_image <- sprintf("url(%s)", list_style_image)
    list_style_position <- NULL
    if (list_style_position.outside) 
        list_style_position <- "outside"
    if (list_style_position.inside) 
        list_style_position <- "inside"
    if (display.none) 
        display <- "none"
    if (display.block) 
        display <- "block"
    if (display.inline) 
        display <- "inline"
    if (display.inline_block) 
        display <- "inline-block"
    if (display.table_cell) 
        display <- "table-cell"
    if (display.flex) 
        display <- "flex"
    if (visibility.visible) 
        visibility <- "visible"
    if (visibility.hidden) 
        visibility <- "hidden"
    if (visibility.collapse) 
        visibility <- "collapse"
    if (visibility.inherit) 
        visibility <- "inherit"
    if (position.static) 
        position <- "static"
    if (position.relative) 
        position <- "relative"
    if (position.fixed) 
        position <- "fixed"
    if (position.absolute) 
        position <- "absolute"
    if (position.sticky) 
        position <- "sticky"
    if (!is.null(go_top)) 
        bottom <- go_top
    if (!is.null(go_bottom)) 
        top <- go_bottom
    if (!is.null(go_left)) 
        right <- go_left
    if (!is.null(go_right)) 
        left <- go_right
    if (float.left) 
        float <- "left"
    if (float.right) 
        float <- "right"
    if (float.none) 
        float <- "none"
    if (float.inherit) 
        float <- "inherit"
    if (box_sizing.border_box) 
        box_sizing <- "border-box"
    if (box_sizing.content_box) 
        box_sizing <- "content-box"
    if (box_sizing.inherit) 
        box_sizing <- "inherit"
    if (clear.both) 
        clear = "both"
    if (!is.null(content)) 
        content <- content
    if (!is.null(background_image)) 
        background_image <- sprintf(paste0(unlist(strsplit(background_image, " {0,}, {0,}")), collapse = "),url("), 
            fmt = "url(%s)")
    if (background_size.cover) 
        background_size <- "cover"
    if (background_size.contain) 
        background_size <- "contain"
    if (is.character(transform.translate)) 
        transform <- sprintf("translate(%s)", transform.translate)
    if (is.character(transform.rotate)) 
        transform <- sprintf("rotate(%sdeg)", transform.rotate)
    if (is.character(transform.scaleX)) 
        transform <- sprintf("scaleX(%s)", transform.scaleX)
    if (is.character(transform.scaleY)) 
        transform <- sprintf("scaleY(%s)", transform.scaleY)
    if (is.character(transform.scale)) 
        transform <- sprintf("scale(%s)", transform.scale)
    if (is.character(transform.skewX)) 
        transform <- sprintf("skewX(%s)", transform.skewX)
    if (is.character(transform.skewY)) 
        transform <- sprintf("skewY(%s)", transform.skewY)
    if (is.character(transform.skew)) 
        transform <- sprintf("skew(%s)", transform.skew)
    if (is.character(transform.matrix)) 
        transform <- sprintf("matrix(%s)", transform.matrix)
    if (!is.null(animation_fadenum)) 
        animation <- paste0("fadenum ", animation_fadenum)
    if (transition_timing_function.ease) 
        transition_timing_function <- "ease"
    if (transition_timing_function.linear) 
        transition_timing_function <- "linear"
    if (transition_timing_function.ease_in) 
        transition_timing_function <- "ease-in"
    if (transition_timing_function.ease_out) 
        transition_timing_function <- "ease-out"
    if (transition_timing_function.ease_in_out) 
        transition_timing_function <- "ease-in-out"
    if (resize.none) 
        resize <- "none"
    if (resize.both) 
        resize <- "both"
    if (resize.horizontal) 
        resize <- "horizontal"
    if (resize.vertical) 
        resize <- "vertical"
    if (flex_direction.column) 
        flex_direction <- "column"
    if (flex_direction.row) 
        flex_direction <- "row"
    if (flex_direction.row_reverse) 
        flex_direction <- "row-reverse"
    if (flex_direction.column_reverse) 
        flex_direction <- "column-reverse"
    if (flex_wrap.nowrap) 
        flex_wrap <- "nowrap"
    if (flex_wrap.wrap) 
        flex_wrap <- "wrap"
    if (flex_wrap.wrap_reverse) 
        flex_wrap <- "wrap-reverse"
    if (justify_content.center) 
        justify_content <- "center"
    if (justify_content.flex_start) 
        justify_content <- "flex-start"
    if (justify_content.flex_end) 
        justify_content <- "flex-end"
    if (justify_content.space_evenly) 
        justify_content <- "space-evenly"
    if (justify_content.space_around) 
        justify_content <- "space-around"
    if (justify_content.space_between) 
        justify_content <- "space-between"
    if (align_items.center) 
        align_items <- "center"
    if (align_items.flex_start) 
        align_items <- "flex-start"
    if (align_items.flex_end) 
        align_items <- "flex-end"
    if (align_items.stretch) 
        align_items <- "stretch"
    if (align_items.baseline) 
        align_items <- "baseline"
    if (align_content.space_between) 
        align_content <- "space-between"
    if (align_content.space_around) 
        align_content <- "space-around"
    if (align_content.stretch) 
        align_content <- "stretch"
    if (align_content.center) 
        align_content <- "center"
    if (align_content.flex_start) 
        align_content <- "flex-start"
    if (align_content.flex_end) 
        align_content <- "flex-end"
    if (align_self.space_between) 
        align_self <- "space-between"
    if (align_self.space_around) 
        align_self <- "space-around"
    if (align_self.stretch) 
        align_self <- "stretch"
    if (align_self.center) 
        align_self <- "center"
    if (align_self.flex_start) 
        align_self <- "flex-start"
    if (align_self.flex_end) 
        align_self <- "flex-end"
    newAttribs <- list(opacity = opacity, background = background, background_color = background_color, 
        background_image = background_image, background_repeat = background_repeat, background_position = background_position, 
        background_attachment = background_attachment, background_size = background_size, background_origin = background_origin, 
        background_clip = background_clip, border = border, border_style = border_style, border_left_style = border_left_style, 
        border_top_style = border_top_style, border_right_style = border_right_style, border_bottom_style = border_bottom_style, 
        border_width = border_width, border_color = border_color, border_left_width = border_left_width, 
        border_left_color = border_left_color, border_left_radius = border_left_radius, border_right_width = border_right_width, 
        border_right_color = border_right_color, border_right_radius = border_right_radius, border_top_width = border_top_width, 
        border_top_color = border_top_color, border_top_radius = border_top_radius, border_bottom_width = border_bottom_width, 
        border_bottom_color = border_bottom_color, border_bottom_radius = border_bottom_radius, border_radius = border_radius, 
        border_collapse = border_collapse, margin = margin, margin_top = margin_top, margin_right = margin_right, 
        margin_bottom = margin_bottom, margin_left = margin_left, padding = padding, padding_top = padding_top, 
        padding_right = padding_right, padding_bottom = padding_bottom, padding_left = padding_left, 
        height = height, max_height = max_height, min_height = min_height, width = width, min_width = min_width, 
        max_width = max_width, outline_style = outline_style, outline_color = outline_color, outline_width = outline_width, 
        outline_offset = outline_offset, outline = outline, color = color, text_align = text_align, direction = text_direction, 
        vertical_align = vertical_align, text_decoration = text_decoration, text_transform = text_transform, 
        text_indent = text_indent, letter_spacing = letter_spacing, word_spacing = word_spacing, line_height = line_height, 
        white_space = white_space, text_shadow = text_shadow, text_overflow = text_overflow, overflow = overflow, 
        overflow_x = overflow_x, overflow_y = overflow_y, font_size = font_size, font_family = font_family, 
        font_style = font_style, font_weight = font_weight, font_variant = font_variant, list_style_type = list_style_type, 
        list_style_image = list_style_image, list_style_position = list_style_position, display = display, 
        visibility = visibility, position = position, top = top, bottom = bottom, left = left, right = right, 
        z_index = z_index, float = float, box_sizing = box_sizing, clear = clear, content = content, 
        transform = transform, animation = animation, transition = transition, transition_delay = transition_delay, 
        transition_duration = transition_duration, transition_property = transition_property, transition_timing_function = transition_timing_function, 
        resize = resize, flex_flow = flex_flow, flex_direction = flex_direction, flex_wrap = flex_wrap, 
        justify_content = justify_content, align_items = align_items, align_content = align_content, 
        order = order, flex = flex, flex_grow = flex_grow, flex_shrink = flex_shrink, flex_basis = flex_basis, 
        align_self = align_self, grid_gap = grid_gap, grid_column_gap = grid_column_gap, grid_row_gap = grid_row_gap, 
        grid_template_columns = grid_template_columns, grid_template_rows = grid_template_rows, grid_row = grid_row, 
        grid_area = grid_area, grid_column = grid_column, grid_column_start = grid_column_start, grid_column_end = grid_column_end, 
        grid_row_start = grid_row_start, grid_row_end = grid_row_end, cursor = cursor)
    names(newAttribs) <- gsub("_", "-", names(newAttribs))
    newAttribs <- newAttribs[!sapply(newAttribs, is.null)]
    newAttribs <- newAttribs
    if (length(newAttribs) == 0) {
        style <- NULL
    }
    else {
        style <- sapply(1:length(newAttribs), function(i) paste0(names(newAttribs)[i], ":", newAttribs[[i]]))
    }
    if (missing(x)) {
        if (is.null(selector)) 
            stop("selector must be given")
        if (pseudo.link) 
            pseudo <- "link"
        if (pseudo.visited) 
            pseudo <- "visited"
        if (pseudo.hover) 
            pseudo <- "hover"
        if (pseudo.active) 
            pseudo <- "active"
        if (pseudo.checked) 
            pseudo <- "checked"
        if (pseudo.disabled) 
            pseudo <- "disabled"
        if (pseudo.empty) 
            pseudo <- "empty"
        if (pseudo.enabled) 
            pseudo <- "enabled"
        if (pseudo.first_child) 
            pseudo <- "first-child"
        if (pseudo.first_of_type) 
            pseudo <- "first-of-type"
        if (pseudo.focus) 
            pseudo <- "focus"
        if (pseudo.in_range) 
            pseudo <- "in-range"
        if (pseudo.invalid) 
            pseudo <- "invalid"
        if (isTRUE(pseudo.lang)) 
            stop("pseudo.lang must be character or FLASE")
        if (is.character(pseudo.lang)) 
            pseudo <- sprintf("lang(%s)", pseudo.lang)
        if (pseudo.last_child) 
            pseudo <- "last-child"
        if (pseudo.last_of_type) 
            pseudo <- "last-of-type"
        if (isTRUE(pseudo.not)) 
            stop("pseudo.not must be character or FLASE")
        if (is.character(pseudo.not)) 
            pseudo <- sprintf("not(%s)", pseudo.not)
        if (isTRUE(pseudo.nth_child)) 
            stop("pseudo.nth_child must be character or FLASE")
        if (is.character(pseudo.nth_child)) 
            pseudo <- sprintf("nth-child(%s)", pseudo.nth_child)
        if (isTRUE(pseudo.nth_last_child)) 
            stop("pseudo.nth_last_child must be character or FLASE")
        if (is.character(pseudo.nth_last_child)) 
            pseudo <- sprintf("nth-last-child(%s)", pseudo.nth_last_child)
        if (isTRUE(pseudo.nth_last_of_type)) 
            stop("pseudo.nth_last_of_type must be character or FLASE")
        if (is.character(pseudo.nth_last_of_type)) 
            pseudo <- sprintf("nth-last-of-type(%s)", pseudo.nth_last_of_type)
        if (isTRUE(pseudo.nth_of_type)) 
            stop("pseudo.nth_of_type must be character or FLASE")
        if (is.character(pseudo.nth_of_type)) 
            pseudo <- sprintf("nth-of-type(%s)", pseudo.nth_of_type)
        if (isTRUE(pseudo.only_of_type)) 
            stop("pseudo.only_of_type must be character or FLASE")
        if (is.character(pseudo.only_of_type)) 
            pseudo <- sprintf("only-of-type(%s)", pseudo.only_of_type)
        if (pseudo.only_child) 
            pseudo <- "only-child"
        if (pseudo.optional) 
            pseudo <- "optional"
        if (pseudo.out_of_range) 
            pseudo <- "out-of-range"
        if (pseudo.read_only) 
            pseudo <- "read-only"
        if (pseudo.read_write) 
            pseudo <- "read-write"
        if (pseudo.required) 
            pseudo <- "required"
        if (pseudo.root) 
            pseudo <- "root"
        if (pseudo.target) 
            pseudo <- "target"
        if (pseudo.valid) 
            pseudo <- "valid"
        if (pseudo.after) 
            pseudo <- ":after"
        if (pseudo.before) 
            pseudo <- ":before"
        if (pseudo.first_letter) 
            pseudo <- ":first-letter"
        if (pseudo.first_line) 
            pseudo <- ":first-line"
        if (pseudo.selection) 
            pseudo <- ":selection"
        if (!is.null(pseudo)) 
            pseudo <- paste0(":", pseudo)
        if (!is.null(pseuded.selector)) 
            pseudo <- paste0(pseudo, " ", pseuded.selector)
        children <- paste0("\n    ", selector, pseudo, "{\n        ", paste0(style, collapse = ";\n        "), 
            "\n    }\n")
        st <- list(name = "style", attribs = list(), children = list(children))
        st <- structure(st, class = "shiny.tag")
        st
    }
    else {
        if (class(x)[1] == "list") 
            class(x) <- c("shiny.tag.list", "list")
        if (is.null(selector)) {
            if (length(x) == 0) 
                return(x)
            if (!is.null(style)) {
                if (inherits(x, "shiny.tag")) {
                  if (is.null(x$attribs$style)) {
                    style3 <- style
                  }
                  else {
                    style2 <- c(strsplit(x$attribs$style, ";")[[1]], style)
                    ck <- rev(duplicated(rev(do::Replace0(style2, " {0,}: {0,}.*"))))
                    style3 <- style2[!ck]
                  }
                  x$attribs$style <- paste0(style3, collapse = ";")
                }
                else if (inherits(x, "shiny.tag.list")) {
                  if (is.null(n)) {
                    kk <- 1:length(x)
                  }
                  else {
                    if (any(n %in% "last")) {
                      n[n %in% "last"] <- length(x)
                      n <- as.numeric(n)
                    }
                    kk <- unique(n)
                  }
                  for (i in kk) {
                    if (x[[i]]$name == "style") 
                      (next)(i)
                    if (is.null(x[[i]]$attribs$style)) {
                      style3 <- style
                    }
                    else {
                      style2 <- c(strsplit(x[[i]]$attribs$style, ";")[[1]], style)
                      ck <- rev(duplicated(rev(do::Replace0(style2, " {0,}: {0,}.*"))))
                      style3 <- style2[!ck]
                    }
                    x[[i]]$attribs$style <- paste0(style3, collapse = ";")
                  }
                }
            }
            return(x)
        }
        else {
            if (length(x) == 0) 
                return(x)
            x <- find_tags(x, selector = selector, n = n)
            if (is.null(style) & is.null(n)) 
                return(x$selectedTags())
            if (is.null(style) & !is.null(n)) 
                return(x$selectedTags())
            for (k in 1:x$length()) {
                if (is.null(x$selectedTags()[[k]]$attribs$style)) {
                  style2 <- style
                }
                else {
                  style2 <- c(strsplit(x$selectedTags()[[k]]$attribs$style, ";")[[1]], style)
                  ck <- rev(duplicated(rev(do::Replace0(style2, " {0,}: {0,}.*"))))
                  style2 <- style2[!ck]
                }
                style2 <- list(paste0(style2, collapse = ";"))
                names(style2) <- "style"
                x$filter(function(x, i) i == k)$removeAttrs("style")
                do.call(x$filter(function(x, i) i == k)$addAttrs, style2)
            }
            xii <- x$allTags()$children
            if (length(xii) == 1) {
                xii[[1]]
            }
            else {
                structure(xii, class = "shiny.tag.list")
            }
        }
    }
}
```

## `add_variable` [internal]

```r
function (fit, ..., vars = NULL, data = NULL) 
{
    nms <- do::get_names(...)
    if (length(nms) > 0) 
        nms <- do::Trim_left(nms, "d.d_")
    nms <- unique(c(nms, vars))
    if (!is.null(data)) {
        datanm <- deparse(substitute(data))
        callenv <- new.env()
        if ("dataxxyyyyxx" %in% do::model.x(fit)) {
            data$dataxxyyyyxx <- rnorm(nrow(data))
            eval(parse(text = sprintf("callenv$%s = data", datanm)))
            form <- sprintf("update(fit,.~. + %s - dataxxyyyyxx)", paste0(nms, collapse = "+"))
            callenv$fit <- fit
            eval(parse(text = form), callenv)
        }
        else {
            eval(parse(text = sprintf("callenv$%s = data", deparse(substitute(data)))))
            form <- sprintf("update(fit,.~. + %s)", paste0(nms, collapse = "+"))
            callenv$fit <- fit
            eval(parse(text = form), callenv)
        }
    }
    else {
        eval(parse(text = sprintf("update(fit,.~. + %s - dataxxyyyyxx)", paste0(nms, collapse = "+"))))
    }
}
```

## `ageAdjust` [exported]

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

## `aggregate2` [internal]

```r
function (data, x, by, fun) 
{
    by2 <- paste0(sapply(by, function(i) sprintf("%s = data[,\"%s\"]", i, i)), collapse = ", ")
    for (i in 1:length(x)) {
        di <- eval(parse(text = sprintf("aggregate(data[,\"%s\"],list(%s),\"%s\")", x[i], by2, fun)))
        colnames(di)[ncol(di)] <- x[i]
        if (i == 1) {
            df <- di
        }
        else {
            df <- dplyr::full_join(df, di, by)
        }
    }
    df
}
```

## `aggregate_max` [exported]

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

## `aggregate_mean` [exported]

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

## `aggregate_min` [exported]

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

## `aggregate_sum` [exported]

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

## `attach_file` [internal]

```r
function (attach) 
{
    paste0(get_config_path(), "/attach/", attach, ".txt")
}
```

## `attach_read` [internal]

```r
function (file) 
{
    if (file.exists(file)) {
        d <- data.table::fread(file)
        d <- d[!lookl(d$seqn, tmcn::toUTF8("# <U+4E0A><U+6D77><U+679D><U+8BC6><U+533B><U+5B66><U+79D1><U+6280><U+6709><U+9650><U+516C><U+53F8><U+51FA><U+54C1>,<U+5FAE><U+4FE1>:Charleszhanggo")), 
            ]
        ck <- sapply(d, function(i) lookl(i, tmcn::toUTF8("<U+4E0A><U+6D77><U+679D><U+8BC6><U+533B><U+5B66><U+79D1><U+6280><U+6709><U+9650><U+516C><U+53F8><U+51FA><U+54C1>,<U+5FAE><U+4FE1>:Charleszhanggo")))
        d[ck] <- NA
        d
    }
}
```

## `bind_col` [exported]

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

## `bold_change` [internal]

```r
function (r) 
{
    rs <- do::list1(strsplit(as.character(r), "<tr>"))
    rs[grepl("font-weight: bold;", rs)] <- sapply(rs[grepl("font-weight: bold;", rs)], function(i) {
        j <- 1
        while (grepl("font-weight: bold;", i)) {
            if (j == 1) {
                i <- sub("font-weight: bold;", "font-weight: bbbb;", i)
            }
            else {
                i <- sub("font-weight: bold;", "", i)
            }
            j <- j + 1
        }
        sub("font-weight: bbbb;", "font-weight: bold;", i)
    })
    r <- paste0(rs, collapse = "<tr>")
    class(r) <- c("kableExtra", "knitr_kable")
    r
}
```

## `browse_rxq_Drug` [exported]

```r
function () 
{
    nhs_html(nhs_tsv("rxq_drug", cat = FALSE)[1])
}
```

## `browse_rxq_Rx` [exported]

```r
function (years) 
{
    nhs_html(nhs_tsv("rxq_rx", years = years, cat = FALSE))
}
```

## `bu` [exported]

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

## `build_codebook` [exported]

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

## `build_drug_data` [internal]

```r
function (years) 
{
    .drug_years <<- years
    d1 <- nhs_read(nhs_tsv("rxq_rx", years = years, cat = FALSE), "rxduse,rxd030:take_drug", "rxddrug,rxd240b:Drug", 
        "fdacode1", "fdacode2", "fdacode3", "fdacode4", "fdacode5", "fdacode6", "rxdrsc1", "rxdrsc2", 
        "rxdrsc3", "rxdrsd1", "rxdrsd2", "rxdrsd3", lower_cd = TRUE, cat = FALSE)
    if (is.character(d1)) 
        return()
    d1 <- d1[!is.na(d1$take_drug), ]
    d2 <- nhs_read(nhs_tsv("rxq_drug", years = years[1], cat = FALSE), cat = FALSE, lower_cd = TRUE, 
        Year = FALSE)
    d <- dplyr::left_join(d1, d2, "rxddrgid")
    d$fdaNDC <- paste_dcn.icn(d, "fdacode")
    d$dcn <- paste_dcn.icn(d, "rxddcn")
    d$icn <- paste_dcn.icn(d, "rxdicn")
    var <- c("Drug", "fdaNDC", "dcn", "icn")
    if ("rxdrsc1" %in% colnames(d)) {
        append(var) <- c("icd10.code", "icd10.description")
        d$icd10.code <- paste_dcn.icn(d, "rxdrsc")
        d$icd10.description <- paste_dcn.icn(d, "rxdrsd")
    }
    d <- d[, c("seqn", "Year", "take_drug", var)]
    .drug_data <<- d
}
```

## `build_drug_search_data` [internal]

```r
function (years) 
{
    .drug_search_years <<- years
    d1 <- nhs_read(nhs_tsv("rxq_rx", years = years, cat = FALSE), "rxduse,rxd030:take_drug", "rxddrug,rxd240b:Drug", 
        "fdacode1", "fdacode2", "fdacode3", "fdacode4", "fdacode5", "fdacode6", "rxdrsc1", "rxdrsc2", 
        "rxdrsc3", "rxdrsd1", "rxdrsd2", "rxdrsd3", lower_cd = F, cat = FALSE)
    d1 <- d1[!is.na(d1$take_drug), ]
    d2 <- nhs_read(nhs_tsv("rxq_drug", years = 1999, cat = FALSE), cat = FALSE, lower_cd = TRUE, Year = FALSE)
    d <- dplyr::left_join(d1, d2, "rxddrgid")
    d$fdaNDC <- paste_dcn.icn(d, "fdacode")
    d$dcn <- paste_dcn.icn(d, "rxddcn")
    d$icn <- paste_dcn.icn(d, "rxdicn")
    var <- c("Drug", "fdaNDC", "dcn", "icn")
    if ("rxdrsc1" %in% colnames(d)) {
        append(var) <- c("icd10.code", "icd10.description")
        d$icd10.code <- paste_dcn.icn(d, "rxdrsc")
        d$icd10.description <- paste_dcn.icn(d, "rxdrsd")
    }
    d <- d[, var]
    d[is.na(d)] <- ""
    .drug_search_data <<- d
}
```

## `build_html` [internal]

```r
function () 
{
    (tsv <- c(nhs_tsv(), nhs_files_pc(file_ext = "pdf")))
    pb <- txtProgressBar(max = length(tsv), style = 3, width = 30)
    for (j in 1:length(tsv)) {
        if (j == 1) 
            res <- data.frame()
        setTxtProgressBar(pb, j)
        (i <- tsv[j])
        (html <- nhs_html(i, FALSE))
        (Year <- prepare_years(i))
        (item <- prepare_items(i))
        (file <- do::Replace0(do::file.name(i), "\\.tsv", "\\.pdf"))
        (update <- do::Replace(i, c("\\.pdf", "\\.tsv"), ".update"))
        (url <- read.delim(update, check.names = FALSE)$"DOC  url")
        if (tools::file_ext(i) == "tsv") {
            if (file.exists(html)) {
                txt <- as.character(xml2::read_html(html))
            }
            else {
                varlabel <- paste0(as.list(nhs_varLabel(i)), collapse = "")
                codebook <- paste0(as.list(nhs_codebook(i)), collapse = "")
                txt <- paste0(varlabel, codebook)
            }
        }
        else {
            txt <- paste0(pdftools::pdf_text(i), collapse = "")
        }
        df <- data.frame(Year, item, file, url, txt)
        res <- rbind(res, df)
    }
    html <- paste0(get_config_path(), "/webpage.txt")
    data.table::fwrite(res, html)
}
```

## `build_varLabel` [exported]

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

## `census_range` [exported]

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

## `character2numeric` [exported]

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

## `check1` [exported]

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

## `ci_by` [internal]

```r
function (data, x, by, round = 2) 
{
    if (length(x) == 1) {
        mean <- mean_by(data, x, by)
        sd <- sd_by(data, x, by)
        mean <- dplyr::full_join(mean, sd, by)
        mean$highiiiiii <- mean[, x] - 1.96 * sd[, ncol(sd)]
        colnames(mean)[ncol(mean)] <- paste0(x, "_low")
        mean$highiiiiii <- mean[, x] + 1.96 * sd[, ncol(sd)]
        colnames(mean)[ncol(mean)] <- paste0(x, "_high")
        digit2character(mean) <- round
        mean$highiiiiii <- sprintf("%s(%s,%s)", mean[, x], mean[, paste0(x, "_low")], mean[, paste0(x, 
            "_high")])
        colnames(mean)[ncol(mean)] <- paste0(x, "_ci")
        mean$highiiiiii <- paste0(mean[, x], "<U+00B1>", mean[, paste0(x, "_sd")])
        colnames(mean)[ncol(mean)] <- paste0(x, "_meanPMsd")
        mean$highiiiiii <- paste0(mean[, x], "(", mean[, paste0(x, "_sd")], ")")
        colnames(mean)[ncol(mean)] <- paste0(x, "_meanSQsd")
        return(mean)
    }
    else {
        for (i in 1:length(x)) {
            if (i == 1) {
                r1 <- ci_by(data, x[i], by)
            }
            else {
                r2 <- ci_by(data, x = x[i], by)
                r1 <- dplyr::full_join(r1, r2, by)
            }
        }
        r1 <- r1[, c(by, x, paste0(x, "_sd"), paste0(x, "_low"), paste0(x, "_high"), paste0(x, "_ci"), 
            paste0(x, "_meanPMsd"), paste0(x, "_meanSQsd"))]
        for (i in by) {
            if (!is.null(levels(data[, i]))) 
                r1[, i] <- factor(r1[, i], levels = levels(data[, i]))
        }
        return(r1)
    }
}
```

## `codebook_url` [internal]

```r
function (url, file, html) 
{
    if (file.exists(file)) {
        cd00 <- read.delim(file, comment.char = "#")
        if (nrow(cd00) > 0) {
            cd00 <- cd00[, c("variable", "code", "label")]
        }
        else {
            cd00 <- NULL
        }
    }
    else {
        cd00 <- NULL
    }
    if (!missing(url)) {
        if (tools::file_ext(url) == "pdf") {
            pdf <- paste0(do::Replace0(file, tools::file_ext(file)), "pdf")
            if (file.exists(pdf)) 
                file.remove(pdf)
            if (file.exists(pdf)) 
                unlink(pdf, force = TRUE)
            cat(crayon::bgWhite(" pdf"))
            nullcon <- file(nullfile(), open = "wb")
            sink(nullcon, type = "message")
            download.file(url, pdf)
            sink(type = "message")
            close(nullcon)
            if (!file.exists(file)) {
                NULLcodebook("#firs_publish", "#last_revise", file)
            }
            return(invisible("pdf"))
        }
    }
    codebook <- set::grep_and(rvest::html_elements(html, xpath = "//div[@id=\"Codebook\"]//div[@class=\"pagebreak\"]"), 
        c("dl", "table"))
    if (length(codebook) == 0) {
        NULLcodebook(firs_publish, last_revise, file)
        return("no codebook")
    }
    df <- do::select(do.call(lapply(codebook, label_table), what = plyr::rbind.fill), j = 1:3)
    colnames(df) <- tolower(colnames(df))
    df
    df <- df[tolower(df$"value description") != "missing", ]
    df <- df[tolower(df$"value description") != "range of values", ]
    colnames(df) <- c("variable", "code", "label")
    df
    if (nrow(df) == 0 | all(table(df[, "variable"]) == 1)) {
        NULLcodebook(firs_publish, last_revise, file)
        invisible("ok")
    }
    else {
        if (!is.null(cd00)) 
            df <- unique(rbind(df, cd00))
        suppressWarnings(write.table(df, file, sep = "\t", row.names = FALSE))
        invisible("ok")
    }
}
```

## `col_rename` [exported]

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

## `copy_with_structure` [internal]

```r
function (src_dir, dest_dir) 
{
    files <- list.files(src_dir, recursive = TRUE, full.names = TRUE)
    for (file in files) {
        (relative_path <- do::Trim_left(do::knife_left(file, nchar(src_dir)), "/"))
        target_file <- file.path(dest_dir, relative_path)
        target_dir <- dirname(target_file)
        if (!dir.exists(target_dir)) {
            dir.create(target_dir, recursive = TRUE)
        }
        file.copy(file, target_file, overwrite = T)
    }
}
```

## `create_db_sprint` [internal]

```r
function (version = 1) 
{
    d <- db_blood.pressure(dar = T, bpx = F, Year = T) %>% diag_Hypertension(drug = "drug") %>% drug_anti.Hypertensive(drugname = "AHM")
    d$Hypertension[d$take_drug %in% "yes"] <- "yes"
    d$drug[d$take_drug %in% "yes"] <- "yes"
    d2 <- d[d$Hypertension %in% "yes" & d$drug %in% "yes", ]
    n <- gregexpr(";", d2$AHM) %>% sapply(function(i) {
        ii <- as.numeric(i)
        if (all(is.na(ii))) 
            return(NA)
        if (length(ii) == 1) {
            if (ii == -1) {
                1
            }
            else {
                2
            }
        }
        else {
            length(ii) + 1
        }
    })
    n[nchar(d2$AHM) == 0 | is.na(d2$AHM)] <- NA
    d2$AHM.number <- n
    d2 <- d2[!is.na(d2$bpxsar), ]
    d2$bpxsar <- round(d2$bpxsar)
    d2$bpxdar <- round(d2$bpxdar)
    d2 <- d2[!is.na(d2$AHM.number), ]
    d3 <- d2[, c("seqn", "Year", "AHM", "AHM.number", "bpxsar", "bpxdar")]
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/db_sprint~~version-", version, ".txt"))
    data.table::fwrite(d3, file, sep = "\t")
}
```

## `create_dex_CMI` [internal]

```r
function (version = 2) 
{
    d <- db_bodyMeasure(waist_circumference_cm = "waist", height_cm = "height", Year = T, years = 2011) %>% 
        db_HemalBiochemistry(fast_triglyceride_mmol.L = "tg_mmol.L", hdl_cholesterol_mmol.L = "hdl_mmol.L")
    d$WHtR <- d$waist/d$height
    d$CMI <- d$tg_mmol.L/d$hdl_mmol.L * d$WHtR
    d <- d %>% dplyr::select(Year, seqn, CMI, tg_mmol.L, hdl_mmol.L, WHtR)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/dex_CMI~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `create_dex_LE8` [internal]

```r
function (version = 1) 
{
    library(dplyr)
    d <- dex_PhysicalActivity(all.5 = T, time = T, total_time = T, direction = "no", Year = T) %>% db_demo(ageyr = "age", 
        psu_strat = F, join = "inner")
    d$PA_total_time[is.na(d$PA_total_time)] <- 0
    d <- d %>% mutate(score_pa = case_when(age >= 20 & PA_total_time >= 150 ~ 100, age >= 20 & PA_total_time >= 
        120 ~ 90, age >= 20 & PA_total_time >= 90 ~ 80, age >= 20 & PA_total_time >= 60 ~ 60, age >= 
        20 & PA_total_time >= 30 ~ 40, age >= 20 & PA_total_time >= 1 ~ 20, age >= 20 & PA_total_time < 
        1 ~ 0))
    d <- diag_smoke(d, quit_years = T, anyone.smoke.in.home = "inhome", days.used.nicotine.stop.smoking.aid_past5days = "nicotine", 
        join = "inner")
    d <- d %>% mutate(score_smoke = case_when(age >= 20 & smoke == "never" ~ 100, age >= 20 & smoke == 
        "former" & quit_years >= 5 ~ 75, age >= 20 & smoke == "former" & quit_years >= 1 ~ 50, age >= 
        20 & smoke == "former" ~ 25, age >= 20 & nicotine > 0 ~ 25, age >= 20 & smoke == "now" ~ 0))
    d$score_smoke <- ifelse(d$inhome %in% "yes", d$score_smoke - 20, d$score_smoke)
    d$score_smoke[d$score_smoke < 0] <- 0
    d0 <- nhs_read(nhs_tsv("slq"), "sld010h,sld012:sleep_hours")
    d <- inner_join(d, d0, "seqn")
    d <- d %>% mutate(score_sleep = case_when(age >= 20 & sleep_hours >= 7 & sleep_hours < 9 ~ 100, age >= 
        20 & sleep_hours >= 9 & sleep_hours < 10 ~ 90, age >= 20 & sleep_hours >= 6 & sleep_hours < 7 ~ 
        70, age >= 20 & ((sleep_hours >= 5 & sleep_hours < 6) | sleep_hours >= 10) ~ 40, age >= 20 & 
        sleep_hours >= 4 & sleep_hours < 5 ~ 20, age >= 20 & sleep_hours < 4 ~ 0))
    d <- db_bodyMeasure(d, BMI_kg.m2 = "bmi", join = "inner")
    d <- d %>% mutate(score_bmi = case_when(age >= 20 & bmi >= 40 ~ 0, age >= 20 & bmi >= 35 ~ 15, age >= 
        20 & bmi >= 30 ~ 30, age >= 20 & bmi >= 25 ~ 70, age >= 20 & bmi < 25 ~ 100))
    d <- db_HemalBiochemistry(d, join = "inner", fast_total_cholesterol_mg.dl = "chol", hdl_cholesterol_mg.dl = "hdl") %>% 
        drug_anti.Hyperlipidemic()
    d <- d %>% mutate(score_non.hdl = case_when(age >= 20 & (chol - hdl >= 220) ~ 0, age >= 20 & (chol - 
        hdl >= 190) ~ 20, age >= 20 & (chol - hdl >= 160) ~ 40, age >= 20 & (chol - hdl >= 130) ~ 60, 
        age >= 20 & (chol - hdl < 130) ~ 100))
    ck <- d$take_drug %in% "yes"
    d$take_drug <- NULL
    d$score_non.hdl[ck] <- d$score_non.hdl[ck] - 20
    d$score_non.hdl[d$score_non.hdl < 0] <- 0
    d <- db_HemalBiochemistry(d, join = "inner", fast_glucose_mg.dl = "glu", HbA1c = "a1c") %>% diag_DM(HbA1c = F, 
        fast_glu = F, OGTT2 = F, rand_glu = F, drug = F)
    d <- d %>% mutate(score_glucose = case_when(age >= 20 & DM %in% "no" & (glu < 100 | a1c < 5.7000000000000002) ~ 
        100, age >= 20 & DM %in% "no" & ((glu >= 100 & glu < 125) | (a1c >= 5.7000000000000002 & a1c < 
        6.4000000000000004)) ~ 60, age >= 20 & DM %in% "DM" & a1c < 7 ~ 40, age >= 20 & DM %in% "DM" & 
        a1c >= 7 & a1c < 8 ~ 30, age >= 20 & DM %in% "DM" & a1c >= 8 & a1c < 9 ~ 20, age >= 20 & DM %in% 
        "DM" & a1c >= 9 & a1c < 10 ~ 10, age >= 20 & DM %in% "DM" & a1c >= 10 ~ 0))
    d <- db_blood.pressure(d, join = "inner", bpx = F) %>% drug_anti.Hypertensive()
    d <- d %>% mutate(score_bp = case_when(age >= 20 & bpxsar < 120 & bpxdar < 80 ~ 100, age >= 20 & 
        bpxsar >= 120 & bpxsar < 130 & bpxdar < 80 ~ 75, age >= 20 & ((bpxsar >= 130 & bpxsar < 140) | 
        (bpxdar >= 80 & bpxdar < 90)) ~ 50, age >= 20 & ((bpxsar >= 140 & bpxsar < 160) | (bpxdar >= 
        90 & bpxdar < 100)) ~ 25, age >= 20 & (bpxsar >= 160 | bpxdar >= 100) ~ 0))
    d$score_bp[d$take_drug %in% "yes"] <- d$score_bp[d$take_drug %in% "yes"] - 20
    d$take_drug <- NULL
    d$score_bp[d$score_bp < 0] <- 0
    d <- d %>% dplyr::select(seqn, Year, age, score_pa, score_smoke, score_sleep, score_bmi, score_non.hdl, 
        score_glucose, score_bp, PA_total_time, smoke, quit_years, inhome, nicotine, sleep_hours, bmi, 
        chol, hdl, glu, a1c, DM, bpxsar, bpxdar)
    unique(d$score_pa)
    unique(d$score_smoke)
    unique(d$score_sleep)
    unique(d$score_bmi)
    unique(d$score_non.hdl)
    unique(d$score_glucose)
    unique(d$score_bp)
    hei1 <- dex_HEI(version = "2015", day = 1, component = F, energy = F)
    colnames(hei1)[2] <- "hei.day1"
    hei12 <- dex_HEI(version = "2015", day = c(1, 2), component = F, energy = F)
    colnames(hei12)[2] <- "hei.day12"
    d <- Inner_Join(d, hei1, hei12)
    d <- d[d$age >= 20, ]
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/dex_LE8~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `create_dex_SDoH` [internal]

```r
function (version = 1) 
{
    tsv_emp <- nhs_tsv("ocq", ex_years = c(1999:2001, 2019))
    d1 <- nhs_read(tsv_emp, "ocq150,ocd150:employment", "ocq380,ocd383,ocq383:reason")
    d1$employment <- Recode(d1$employment, "Working at a job or business::employed", "With a job or business but not at work::no", 
        "Not working at a job or business?::no", "Looking for work, or::no", to.numeric = FALSE)
    d1$reason <- Recode(d1$reason, "Going to school::student", "Retired::retired", "Disabled::no", "Taking care of house or family::no", 
        "Other::no", "Unable to work for health reasons::no", "On layoff::no", "Unable to work for health reasons/Disabled::no", 
        "Can't find work/On layoff::no", "Seasonal/Contract work::no", "NA::", to.numeric = FALSE)
    d1$Employment <- paste0(d1$employment, "--", d1$reason)
    d1$Employment <- Recode(d1$Employment, "employed--NA::Employed, student, retired", "no--student::Employed, student, retired", 
        "no--retired::Employed, student, retired", "no--NA::Not employed", "no--no::Not employed", "NA--NA::NA", 
        to.numeric = FALSE)
    d1$score_Employment <- Recode(d1$Employment, "Not employed::1", "Employed, student, retired::0", 
        to.numeric = T)
    d1 <- d1[, c("seqn", "Employment", "score_Employment")]
    d2 <- db_demo(poverty = "PIR", psu_strat = F, Year = T)
    d2 <- d2[!d2$Year %in% prepare_years(c(1999:2001, 2019)), ]
    d2$PIR <- ifelse(d2$PIR >= 3, ">=3", "<3")
    d2$score_PIR <- Recode(d2$PIR, "<3::1", ">=3::0", "NA::", to.numeric = T)
    d2 <- d2[, c("seqn", "PIR", "score_PIR")]
    tsv_food <- nhs_tsv("fsq", ex_years = c(1999:2001, 2019))
    d3 <- nhs_read(tsv_food, "fsd032a:f1", "fsd032b:f2", "fsd032c:f3", "fsd041:f4", "fsd052:f5_often", 
        "fsd061:f6", "fsd071:f7", "fsd081:f8", "fsd092:f9", "fsd102:f10_often")
    for (i in set::not(colnames(d3), c("seqn", "Year"))) {
        d3[, i] <- tolower(d3[, i])
        d3[, i] <- Recode(d3[, i], "screened out::safe", "never true::safe", "no::safe", "often true::dange", 
            "sometimes true::dange", "yes::dange", "only 1 or 2 months?::dange", "some months but not every month, or::dange", 
            "almost every month::dange", to.numeric = FALSE)
        d3[, paste0("score_", i)] <- ifelse(d3[, i] %in% "dange", 1, 0)
    }
    nms <- c("f1", "f2", "f3", "f4", "f5_often", "f6", "f7", "f8", "f9", "f10_often")
    d3$score_Food.security <- ifelse(row.sums(d3[, paste0("score_", nms)]) > 0, 1, 0)
    d3$Food.security <- ifelse(row.sums(d3[, paste0("score_", nms)]) > 0, "Marginal, low, or very low", 
        "Full food security")
    d3 <- d3[, c("seqn", "Food.security", "score_Food.security")]
    d4 <- db_demo(edu = T, Year = T)
    d4 <- d4[!d4$Year %in% prepare_years(c(1999:2001, 2019)), ]
    d4$edu <- tolower(d4$edu)
    d4$Education <- Recode(d4$edu, "high school graduate/ged or equivalent::High school or more", "high school grad/ged or equivalent::High school or more", 
        "high school graduate::High school or more", "ged or equivalent::High school or more", "some college or aa degree::High school or more", 
        "college graduate or above::High school or more", "more than high school::High school or more", 
        "12th grade, no diploma::Less than high school", "11th grade::Less than high school", "10th grade::Less than high school", 
        "9-11th grade (includes 12th grade with no diploma)::Less than high school", "9th grade::Less than high school", 
        "less than 9th grade::Less than high school", "8th grade::Less than high school", "7th grade::Less than high school", 
        "6th grade::Less than high school", "5th grade::Less than high school", "less than 5th grade::Less than high school", 
        "4th grade::Less than high school", "3rd grade::Less than high school", "2nd grade::Less than high school", 
        "1st grade::Less than high school", "never attended / kindergarten only::Less than high school", 
        to.numeric = FALSE)
    d4$score_Education <- ifelse(d4$Education == "Less than high school", 1, 0)
    d4 <- d4[, c("seqn", "Education", "score_Education")]
    tsv_huq <- nhs_tsv("huq", ex_years = c(1999:2001, 2019))
    d5 <- nhs_read(tsv_huq, "huq030", "huq040,huq041,huq042:type", Year = F)
    d5$huq030 <- tolower(d5$huq030)
    d5$type <- tolower(d5$type)
    d5$xt <- paste0(d5$huq030, "-", d5$type)
    d5$Access.to.healthcare <- Recode(d5$xt, "yes-a doctor's office or health center::Routine place to go for healthcare", 
        "yes-a va medical center or va outpatient clinic::Routine place to go for healthcare", "yes-clinic or health center::Routine place to go for healthcare", 
        "yes-doctor's office or hmo::Routine place to go for healthcare", "yes-doesn't go to one place most often::Routine place to go for healthcare", 
        "yes-hospital outpatient department::Routine place to go for healthcare", "yes-NA::Routine place to go for healthcare", 
        "yes-some other place::Routine place to go for healthcare", "there is more than one place-a doctor's office or health center::Routine place to go for healthcare", 
        "there is more than one place-a va medical center or va outpatient clinic::Routine place to go for healthcare", 
        "there is more than one place-clinic or health center::Routine place to go for healthcare", "there is more than one place-doctor's office or hmo::Routine place to go for healthcare", 
        "there is more than one place-doesn't go to one place most often::Routine place to go for healthcare", 
        "there is more than one place-hospital outpatient department::Routine place to go for healthcare", 
        "there is more than one place-NA::Routine place to go for healthcare", "there is more than one place-some other place::Routine place to go for healthcare", 
        "yes-urgent care center or clinic in a drug store or grocery store::No routine place, or ER/hospital/other", 
        "yes-hospital emergency room::No routine place, or ER/hospital/other", "yes-emergency room::No routine place, or ER/hospital/other", 
        "there is more than one place-emergency room::No routine place, or ER/hospital/other", "there is more than one place-hospital emergency room::No routine place, or ER/hospital/other", 
        "there is more than one place-urgent care center or clinic in a drug store or grocery store::No routine place, or ER/hospital/other", 
        "there is no place-NA::No routine place, or ER/hospital/other", "NA-NA::NA", to.numeric = FALSE)
    d5$score_Access.to.healthcare <- Recode(d5$Access.to.healthcare, "Routine place to go for healthcare::0", 
        "No routine place, or ER/hospital/other::1", "NA::", to.numeric = T)
    d5 <- d5[, c("seqn", "Access.to.healthcare", "score_Access.to.healthcare")]
    tsv_hiq <- nhs_tsv("hiq", ex_years = c(1999:2001, 2019))
    d6 <- nhs_read(tsv_hiq, "hid010,hiq011:cover", "hid030a,hiq031a,hiq032a:private")
    ck1 <- tolower(d6$cover) %in% "yes"
    ck2 <- tolower(d6$private) %in% c("yes", "covered by private insurance")
    d6$Health.insurance <- ifelse(ck1 & ck2, "Private insurance", "Government or no insurance")
    d6$Health.insurance[is.na(d6$cover)] <- NA
    d6$score_Health.insurance <- Recode(d6$Health.insurance, "Private insurance::0", "Government or no insurance::1", 
        "NA::", to.numeric = T)
    d6 <- d6[, c("seqn", "Health.insurance", "score_Health.insurance")]
    tsv_hoq <- nhs_tsv("hoq", ex_years = c(1999:2001, 2019))
    d7 <- nhs_read(tsv_hoq, "hoq065")
    d7$Housing.instability <- Recode(d7$hoq065, "Owned or being bought::Own home", "Rented::Rent or other arrangement", 
        "Other arrangement::Rent or other arrangement", "NA::", to.numeric = FALSE)
    d7$score_Housing.instability <- Recode(d7$Housing.instability, "Rent or other arrangement::1", "Own home::0", 
        "NA::", to.numeric = T)
    d7 <- d7[, c("seqn", "Housing.instability", "score_Housing.instability")]
    d8 <- db_demo(marital = T, psu_strat = F, Year = T)
    d8 <- d8[!d8$Year %in% prepare_years(c(1999:2001, 2019)), ]
    d8$Marital.status <- Recode(d8$marital, "Married::Married or living with a partner", "Living with partner::Married or living with a partner", 
        "Married/Living with partner::Married or living with a partner", "Never married::Not married nor living with a partner", 
        "Widowed::Not married nor living with a partner", "Divorced::Not married nor living with a partner", 
        "Separated::Not married nor living with a partner", "Widowed/Divorced/Separated::Not married nor living with a partner")
    d8$score_Marital.status <- Recode(d8$Marital.status, "Not married nor living with a partner::1", 
        "Married or living with a partner::0", to.numeric = T)
    d8 <- d8[, c("seqn", "Marital.status", "score_Marital.status")]
    d <- Full_Join(d1, d2, d3, d4, d5, d6, d7, d8)
    compo <- c("Employment", "PIR", "Food.security", "Education", "Access.to.healthcare", "Health.insurance", 
        "Housing.instability", "Marital.status")
    score.var <- c("score_Employment", "score_PIR", "score_Food.security", "score_Education", "score_Access.to.healthcare", 
        "score_Health.insurance", "score_Housing.instability", "score_Marital.status")
    d$SDoH <- row.sums(d[, score.var])
    d$SDoH_count <- 8 - do::NA.row.sums(d[, score.var])
    ddemo <- db_demo(ageyr = "age", Year = T)
    d <- Inner_Join(d, ddemo)
    d <- d[, c("seqn", "Year", "SDoH", "SDoH_count", score.var, compo)]
    d <- add_masc(d, c("seqn", "Year"))
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/dex_SDoH~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `create_diag_smoke` [internal]

```r
function (version = 2) 
{
    smq <- nhs_tsv("smq\\.|smq_")
    smq_fam <- nhs_tsv("smqfam")
    smq_mec <- nhs_tsv("smqmec")
    d <- db_demo(nhs_read(smq, "smq020:smoke", "smq040:smoke_now", "smd030:start_age-u", "smq050q:quit_time-u", 
        "smq050u:quit_unite", "smd057:cigarettes_per_day_when_quit", "smd090,smd650:avg_cigarettes_per_day_past_30_days", 
        smq_fam, "smd410,smd470:anyone.smoke.in.home", smq_mec, "smd830,smq830:days.used.nicotine.stop.smoking.aid_past5days", 
        lower_cd = TRUE, cat = FALSE), ageyr = "age")
    d$quit_time[is.na(d$quit_unite)] <- NA
    d$start_age[d$start_age %=% c(777, 999)] <- NA
    d$smoke[d$smoke == "no"] <- "never"
    d$smoke[d$smoke == "yes"] <- "now"
    d$smoke[grepl("not {0,}at {0,}all", d$smoke_now)] <- "former"
    ck <- d$quit_unite %in% "months"
    d$quit_time2[ck] <- janitor::round_half_up(d$quit_time[ck]/12, 1)
    ck <- d$quit_unite %in% "weeks"
    d$quit_time2[ck] <- janitor::round_half_up(d$quit_time[ck] * 7/365, 1)
    ck <- d$quit_unite %in% "days"
    d$quit_time2[ck] <- janitor::round_half_up(d$quit_time[ck]/365, 1)
    ck <- d$quit_unite %in% "years"
    d$quit_time2[ck] <- d$quit_time[ck]
    d$quit_years <- d$quit_time2
    d$smoking_years <- d$age - d$start_age - d$quit_time2
    d$smoking_years2 <- d$age - d$start_age
    d$smoking_years[is.na(d$smoking_years)] <- d$smoking_years2[is.na(d$smoking_years)]
    d$smoking_years2 <- NULL
    d$cigarettes_per_day_when_quit <- Recode(d$cigarettes_per_day_when_quit, "1 cigarette or less::1", 
        "95 cigarettes or more::95", to.numeric = T)
    d$avg_cigarettes_per_day_past_30_days <- Recode(d$avg_cigarettes_per_day_past_30_days, "95 cigarettes or more::95", 
        "1 cigarette or less::1", to.numeric = T)
    d$pack_years <- d$cigarettes_per_day_when_quit/20 * d$smoking_years
    d$pack_years2 <- d$avg_cigarettes_per_day_past_30_days/20 * d$smoking_years
    d$pack_years[is.na(d$pack_years)] <- d$pack_years2[is.na(d$pack_years)]
    d$pack_years2 <- NULL
    ck <- do::left(d$anyone.smoke.in.home, 2) == "no"
    d$anyone.smoke.in.home[ck] <- "no"
    d$anyone.smoke.in.home[!ck] <- "yes"
    d <- d %>% dplyr::select(Year, seqn, smoke, start_age, quit_years, smoking_years, pack_years, cigarettes_per_day_when_quit, 
        avg_cigarettes_per_day_past_30_days, anyone.smoke.in.home, days.used.nicotine.stop.smoking.aid_past5days)
    if (!dir.exists(paste0(get_config_path(), "/attach/"))) 
        dir.create(paste0(get_config_path(), "/attach/"))
    (file <- paste0(get_config_path(), "/attach/diag_smoke~~version-", version, ".txt"))
    data.table::fwrite(d, file, sep = "\t")
}
```

## `cut_headtail` [exported]

```r
function (x, col, ..., cat = T) 
UseMethod("cut_headtail")
```

## `d2db` [internal]

```r
function (d) 
{
    nms <- colnames(d)
    nms[nms %in% "Year"] <- "'Year'"
    nms[nms %in% "seqn"] <- "'seqn'"
    txt <- c("#' thisfunction", "#' ", "#' @description\n#' ", "#' @param data <U+8981><U+8FFD><U+52A0><U+7684><U+6570><U+636E>", 
        "#' @param all logical", "#' @param years <U+6307><U+5B9A><U+5E74><U+4EFD>", "#' @param Year <U+662F><U+5426><U+4FDD><U+7559>Year<U+5217>", 
        sprintf("#' @param %s character or logical", set::not(colnames(d), "Year", "seqn")), "#' @param join <U+6570><U+636E><U+5408><U+5E76><U+7684><U+65B9><U+5411><U+FF0C>full<U+FF0C>inner<U+FF0C>left<U+FF0C>right", 
        "#' @return thisfunction", "#' @export", "thisfunction <- function(data=NULL,\n             all=FALSE,", 
        "years,", paste0(paste0(set::not(colnames(d), "Year", "seqn"), collapse = ",\n"), ",\nYear=F", 
            ",\njoin='left'){"), "\n             ck <- all(", paste0(sprintf("miss(%s)", set::not(colnames(d), 
            "Year", "seqn")), collapse = ",\n"), ")", "if (all){", "if (ck){", paste0(set::not(colnames(d), 
            "Year", "seqn"), " <- TRUE"), "}else{", sprintf("if (miss(%s))  %s <- TRUE", set::not(colnames(d), 
            "Year", "seqn"), set::not(colnames(d), "Year", "seqn")), "}", "}else{", "if (ck){", "return()", 
        "}else{", sprintf("if (miss(%s))  %s <- FALSE", set::not(colnames(d), "Year", "seqn"), set::not(colnames(d), 
            "Year", "seqn")), "}", "}", sprintf("if (isTRUE(%s)) %s = '%s'", set::not(colnames(d), "Year", 
            "seqn"), set::not(colnames(d), "Year", "seqn"), set::not(colnames(d), "Year", "seqn")), "", 
        "var2 <- c() |>", paste0(sprintf("variable_formula(%s,'%s')", nms, colnames(d)), collapse = "|>\n"), 
        "years <- data_years(data,years)", "############## bulid data begin", "", "", "############## build data end", 
        "", "\nd <- d[,do::Replace0(var2,':.*'),drop=F]\n    d <- col_rename(d,var2)\n    return_data(data,d,Year,key = 'seqn',join)", 
        "}")
    clipr::write_clip(txt)
}
```

## `data_years` [internal]

```r
function (data, years) 
{
    if (!missing(data)) {
        if (!is.null(data)) {
            if (nrow(data) > 0) {
                ck_psu <- set::grep_and(colnames(data), "Year\\.[\\.xy]{1,}")
                if (length(ck_psu) >= 2) {
                  col_rename(data) <- paste0(ck_psu[1], ":Year")
                  data <- drop_col(data, ck_psu[-1])
                }
                if (!"Year" %in% colnames(data)) {
                  nhs_years <- attr(data, "nhs_years")
                  if (length(nhs_years)) {
                    years <- nhs_years
                  }
                  else {
                    if (missing(years)) {
                      if (do::cnOS()) 
                        stop(tmcn::toUTF8("data<U+4E2D><U+6CA1><U+6709>Year<U+5217>"))
                      if (!do::cnOS()) 
                        stop("no Year column in data")
                    }
                  }
                }
                else {
                  years = unique(data$Year)
                }
            }
        }
    }
    years = prepare_years(years)
    years
}
```

## `delet_masc` [internal]

```r
function (d, ex_col = NULL) 
{
    for (i in colnames(d)) {
        ck <- lookl(d[, i], "zhangjing-zhishi-yikeshu")
        ck[is.na(ck)] <- F
        if (any(ck)) {
            d[ck, i] <- NA
        }
    }
    to_numeric(d)
}
```

## `delete_variable` [internal]

```r
function (fit, ..., vars = NULL, data = NULL) 
{
    nms <- do::get_names(...)
    nms <- unique(c(nms, vars))
    if (!is.null(data)) {
        callenv <- new.env()
        eval(parse(text = sprintf("callenv$%s = data", deparse(substitute(data)))))
        form <- sprintf("update(fit,.~. - %s)", paste0(nms, collapse = "-"))
        callenv$fit <- fit
        eval(parse(text = form), callenv)
    }
    else {
        eval(parse(text = sprintf("update(fit,.~. - %s)", paste0(nms, collapse = "-"))))
    }
}
```

## `delete_variable_rcs_keepx` [internal]

```r
function (fit, data = NULL, dataxxyyyyxx = F) 
{
    (rcsx <- rcsx(fit))
    (nms <- c(sprintf("rcs(%s)", rcsx), paste0("rcs(", rcsx, ",", 1:100, ")")))
    if (!is.null(data)) {
        datanm <- deparse(substitute(data))
        callenv <- new.env()
        if (length(do::model.x(fit)) == 1) {
            if (dataxxyyyyxx) {
                data$dataxxyyyyxx <- rep(rnorm(nrow(data)))
                eval(parse(text = sprintf("callenv$%s = data", datanm)))
                form <- sprintf("update(fit,.~. + dataxxyyyyxx - %s + %s)", paste0(nms, collapse = "-"), 
                  rcsx)
                callenv$fit <- fit
                eval(parse(text = form), callenv)
            }
            else {
                eval(parse(text = sprintf("callenv$%s = data", datanm)))
                form <- sprintf("update(fit,.~. - %s + %s)", paste0(nms, collapse = "-"), rcsx)
                callenv$fit <- fit
                eval(parse(text = form), callenv)
            }
        }
        else {
            eval(parse(text = sprintf("callenv$%s = data", datanm)))
            form <- sprintf("update(fit,.~. - %s)", paste0(nms, collapse = "-"))
            callenv$fit <- fit
            eval(parse(text = form), callenv)
        }
    }
    else {
        eval(parse(text = sprintf("update(fit,.~. - %s + %s)", paste0(nms, collapse = "-"), rcsx)))
    }
}
```

## `design4matchit` [exported]

```r
function (design) 
{
    x <- cbind(design$variables, SW = (1/design$prob)/mean(1/design$prob))
    cbind(xrxoxwnxuxbxmxexr = 1:nrow(x), x)
}
```

## `deviance_svycoxph` [internal]

```r
function (object) 
{
    2 * (object$ll[1] - object$ll[2])
}
```

## `digit` [internal]

```r
function (x, round) 
{
    digital.i <- function(x, round) {
        if (is.numeric(x)) {
            x = round(x, round)
            isna <- is.na(x)
            x <- format(x, nsmall = round)
            x[isna] <- NA
            x
        }
        else {
            format(x, digits = round, nsmall = round)
        }
    }
    if (any(is.data.frame(x), is.matrix(x))) {
        for (i in 1:ncol(x)) {
            x[, i] = digital.i(x[, i], round)
        }
        x
    }
    else {
        digital.i(x, round)
    }
}
```

## `digit2character` [exported]

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

## `digit2numeric` [exported]

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

## `dii` [exported]

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

## `distinct` [exported]

```r
function (.data, ..., .keep_all = FALSE) 
{
    UseMethod("distinct")
}
```

## `dl` [internal]

```r
function (li) 
{
    title <- do::Replace(tolower(do::Trim(rvest::html_text(rvest::html_elements(li, "dt"), TRUE), ":")), 
        " {1,}", " ")
    title[title == "variable name"] <- "variable"
    title[title == "sas label"] <- "label"
    title[title == "english text"] <- "description"
    title[title == "english instructions"] <- "instructions"
    title
    cont <- do::Replace0(do::Replace(tolower(do::Trim(rvest::html_text(rvest::html_elements(li, "dd"), 
        TRUE), ":")), " {1,}", " "), "\r", "\n", "\t")
    if (anyDuplicated(title)) {
        duptitle <- names(table(title))[table(title) > 1]
        for (i in duptitle) {
            ck <- which(title == i)
            dupcont <- paste0(cont[ck], collapse = ";\n")
            title <- title[-ck[-1]]
            cont <- cont[-ck[-1]]
            cont[ck[1]] <- dupcont
        }
    }
    data.frame(matrix(cont, nrow = 1, dimnames = list(NULL, title)), check.names = FALSE)
}
```

## `drop_col` [exported]

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

## `drop_row` [exported]

```r
function (x, ...) 
UseMethod("drop_row")
```

## `drop_row_high_percent` [exported]

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

## `drop_row_low_percent` [exported]

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

## `eGFR_CKD_EPI_Scr_2021` [internal]

```r
function (data, scr_mg.dl) 
{
    data <- add_col(data, "p1", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p2", -0.24099999999999999, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p3", 1.012, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p4", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p1", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] > 0.69999999999999996)
    data <- add_col(data, "p2", -0.24099999999999999, data$sex == "female" & data[, scr_mg.dl] > 0.69999999999999996)
    data <- add_col(data, "p3", 1.012, data$sex == "female" & data[, scr_mg.dl] > 0.69999999999999996)
    data <- add_col(data, "p4", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] > 0.69999999999999996)
    data <- add_col(data, "p1", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p2", -0.24099999999999999, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p3", 1.012, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p4", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p1", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p2", -0.24099999999999999, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p3", 1.012, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
    data <- add_col(data, "p4", 0.69999999999999996, data$sex == "female" & data[, scr_mg.dl] <= 0.69999999999999996)
}
```

## `eGFR_FAS_age` [internal]

```r
function (data, scr_mg.dl) 
{
    data <- add_col(data, "Q", 0.26000000000000001, data$age == 1)
    data <- add_col(data, "Q", 0.28999999999999998, data$age == 2)
    data <- add_col(data, "Q", 0.31, data$age == 3)
    data <- add_col(data, "Q", 0.34000000000000002, data$age == 4)
    data <- add_col(data, "Q", 0.38, data$age == 5)
    data <- add_col(data, "Q", 0.40999999999999998, data$age == 6)
    data <- add_col(data, "Q", 0.44, data$age == 7)
    data <- add_col(data, "Q", 0.46000000000000002, data$age == 8)
    data <- add_col(data, "Q", 0.48999999999999999, data$age == 9)
    data <- add_col(data, "Q", 0.51000000000000001, data$age == 10)
    data <- add_col(data, "Q", 0.53000000000000003, data$age == 11)
    data <- add_col(data, "Q", 0.56999999999999995, data$age == 12)
    data <- add_col(data, "Q", 0.58999999999999997, data$age == 13)
    data <- add_col(data, "Q", 0.60999999999999999, data$age == 14)
    data <- add_col(data, "Q", 0.71999999999999997, data$sex == "male" & data$age == 15)
    data <- add_col(data, "Q", 0.78000000000000003, data$sex == "male" & data$age == 16)
    data <- add_col(data, "Q", 0.81999999999999995, data$sex == "male" & data$age == 17)
    data <- add_col(data, "Q", 0.84999999999999998, data$sex == "male" & data$age == 18)
    data <- add_col(data, "Q", 0.88, data$sex == "male" & data$age == 19)
    data <- add_col(data, "Q", 0.90000000000000002, data$sex == "male" & data$age >= 20)
    data <- add_col(data, "Q", 0.64000000000000001, data$sex == "female" & data$age == 15)
    data <- add_col(data, "Q", 0.67000000000000004, data$sex == "female" & data$age == 16)
    data <- add_col(data, "Q", 0.68999999999999995, data$sex == "female" & data$age == 17)
    data <- add_col(data, "Q", 0.68999999999999995, data$sex == "female" & data$age == 18)
    data <- add_col(data, "Q", 0.69999999999999996, data$sex == "female" & data$age == 19)
    data <- add_col(data, "Q", 0.69999999999999996, data$sex == "female" & data$age >= 20)
    data <- add_col(data, "Qb", 1, data$age <= 40)
    data <- add_col(data, "Qb", 0.98799999999999999^(data$age - 40), data$age > 40)
    107.3/(data[, scr_mg.dl]/data$Q) * data$Qb
}
```

## `eGFR_FAS_height` [internal]

```r
function (data, scr_mg.dl) 
{
    data <- add_col(data, "Q", 0.26000000000000001, data$height <= 75)
    data <- add_col(data, "Q", 0.28999999999999998, data$height <= 87 & data$height > 75)
    data <- add_col(data, "Q", 0.31, data$height <= 95.5 & data$height > 87)
    data <- add_col(data, "Q", 0.34000000000000002, data$height <= 102.5 & data$height > 95.5)
    data <- add_col(data, "Q", 0.38, data$height <= 110 & data$height > 102.5)
    data <- add_col(data, "Q", 0.40999999999999998, data$height <= 116.7 & data$height > 110)
    data <- add_col(data, "Q", 0.44, data$height <= 123.5 & data$height > 116.7)
    data <- add_col(data, "Q", 0.46000000000000002, data$height <= 129.5 & data$height > 123.5)
    data <- add_col(data, "Q", 0.48999999999999999, data$height <= 135 & data$height > 129.5)
    data <- add_col(data, "Q", 0.51000000000000001, data$height <= 140 & data$height > 135)
    data <- add_col(data, "Q", 0.53000000000000003, data$height <= 146 & data$height > 140)
    data <- add_col(data, "Q", 0.56999999999999995, data$height <= 152.5 & data$height > 146)
    data <- add_col(data, "Q", 0.58999999999999997, data$height <= 159 & data$height > 152.5)
    data <- add_col(data, "Q", 0.60999999999999999, data$height <= 165 & data$height > 159)
    data <- add_col(data, "Q", 0.71999999999999997, data$sex == "male" & data$height <= 172 & data$height > 
        165)
    data <- add_col(data, "Q", 0.78000000000000003, data$sex == "male" & data$height <= 176 & data$height > 
        172)
    data <- add_col(data, "Q", 0.81999999999999995, data$sex == "male" & data$height <= 178 & data$height > 
        176)
    data <- add_col(data, "Q", 0.84999999999999998, data$sex == "male" & data$height <= 179 & data$height > 
        178)
    data <- add_col(data, "Q", 0.88, data$sex == "male" & data$height <= 180 & data$height > 179)
    data <- add_col(data, "Q", 0.90000000000000002, data$sex == "male" & data$height > 180)
    data <- add_col(data, "Q", 0.64000000000000001, data$sex == "female" & data$height <= 164.5 & data$height > 
        159)
    data <- add_col(data, "Q", 0.67000000000000004, data$sex == "female" & data$height <= 166 & data$height > 
        164.5)
    data <- add_col(data, "Q", 0.68999999999999995, data$sex == "female" & data$height <= 166.5 & data$height > 
        166)
    data <- add_col(data, "Q", 0.68999999999999995, data$sex == "female" & data$height <= 167 & data$height > 
        166.5)
    data <- add_col(data, "Q", 0.69999999999999996, data$sex == "female" & data$height <= 167.5 & data$height > 
        167)
    data <- add_col(data, "Q", 0.69999999999999996, data$sex == "female" & data$height > 167.5)
    data <- add_col(data, "Qb", 1, data$age <= 40)
    data <- add_col(data, "Qb", 0.98799999999999999^(data$age - 40), data$age > 40)
    107.3/(data[, scr_mg.dl]/data$Q) * data$Qb
}
```

## `each_id_first_row` [exported]

```r
function (data = NULL, ...) 
{
    ids <- c(...)
    ids <- paste0_columns(data[, ids, drop = F])
    ck <- duplicated(ids)
    data[!ck, ]
}
```

## `each_id_last_row` [exported]

```r
function (data = NULL, ...) 
{
    ids <- c(...)
    ids <- paste0_columns(data[, ids, drop = F])
    ck <- rev(duplicated(rev(ids)))
    data[!ck, ]
}
```

## `equal` [internal]

```r
function (a, b) 
a == b
```

## `even` [internal]

```r
function (x) 
{
    x[seq(2, length(x), 2)]
}
```

## `evenl` [internal]

```r
function (x) 
{
    x <- rep(FALSE, length(x))
    x[seq(2, length(x), 2)] <- TRUE
    x
}
```

## `explicit1` [internal]

```r
function (formula) 
{
    if (length(formula) == 1) 
        return(formula == 1)
    if (!(formula[[1]] == "+" || formula[[1]] == "*" || formula[[1]] == "/" || formula[[1]] == "^" || 
        formula[[1]] == "~")) 
        return(FALSE)
    if (length(formula) == 3) {
        (formula[[2]] == 1) || explicit1(formula[[2]]) || explicit1(formula[[3]])
    }
    else {
        (formula[[2]] == 1) || explicit1(formula[[2]])
    }
}
```

## `filepage` [internal]

```r
function (yeari, itemsi, mode, files, filetable = NULL, cat = TRUE, redown = TRUE, update = FALSE, xpt = TRUE, 
    tsv = TRUE, varLabel = TRUE, codebook = TRUE, updatefile = TRUE, updatekeyword = NULL) 
{
    if (is.null(filetable)) {
        filetablei <- nhs_files_web(yeari, itemsi, FALSE)
        ck <- ncol(filetablei) < 8
        if (ck) 
            return()
        filetable <- filetablei
    }
    ckf <- tolower(do::file.name(filetable$`Data url`))
    ckf <- do::Replace0(ckf, paste0("\\.", tools::file_ext(ckf)))
    if (!is.null(updatekeyword) & nrow(filetable) > 0) {
        cku <- lookl(filetable$`Date Published`, updatekeyword)
        filetable <- filetable[cku, ]
        if (nrow(filetable) == 0) {
            if (cat) 
                cat(paste0(" (", nrow(filetable), ")"))
            return(invisible())
        }
    }
    if (!missing(files) & nrow(filetable) > 0) {
        ckf <- tolower(do::file.name(filetable$`Data url`))
        ckf <- do::Replace0(ckf, paste0("\\.", tools::file_ext(ckf)))
        ckfj <- grepl(paste0(files, collapse = "|"), ckf, TRUE)
        ckf <- ckf[ckfj]
        filetable <- filetable[ckfj, ]
    }
    if (cat) 
        cat(paste0(" (", nrow(filetable), ")"))
    if (nrow(filetable) == 0) 
        return(invisible())
    (ck.vid <- lookl(ckf, "vid"))
    ck.vid.nona <- !is.na(ck.vid)
    ck.vid <- ck.vid[ck.vid.nona]
    filetable <- filetable[ck.vid.nona, ]
    if (any(ck.vid)) {
        filetable$`DOC  url`[ck.vid] <- sprintf("https://wwwn.cdc.gov/nchs/nhanes/%s/%s.htm", filetable$year[ck.vid], 
            ckf[ck.vid])
    }
    (fd <- paste0(get_config_path(), "/", prepare_years(yeari), "/", prepare_items(itemsi)))
    if (!dir.exists(fd)) 
        dir.create(path = fd, showWarnings = FALSE, recursive = TRUE)
    if (cat) 
        cat("-->", fd)
    for (j in 1:nrow(filetable)) {
        (tablej <- filetable[j, ])
        (xptj <- tablej$`Data url`)
        (docj <- tablej$`DOC  url`)
        (sizej <- do::Replace0(tablej$`Data File`, c(".*- {0,}", "\\].*")))
        (fj <- tolower(do::file.name(xptj)))
        if (tolower(filetable$`Date Published`[j]) == "withdrawn") 
            (fj <- do::Replace0(tablej$`Doc File`, " .*"))
        (fn <- sprintf("%s/%s", fd, fj))
        if (cat) 
            cat("\n")
        if (cat) 
            cat(crayon::blue(paste0("           ", j, ": ", fj, " (size:", sizej)))
        if (tolower(filetable$`Date Published`[j]) == "withdrawn") {
            if (cat) 
                cat(" withdrawn")
            (next)(j)
        }
        if (file.exists(fn)) {
            (pattern <- paste0(do::Replace0(fj, "\\.xpt|\\.zip"), c(".sas7bdat", ".codebook", ".varLabel", 
                ".tsv", ".update", ".xpt")))
            (f5 <- list.files(fd) %in% pattern)
            (ck <- sum(f5) == 5)
            if (update) 
                ck <- FALSE
            if (!ck) {
                if (redown & xpt) {
                  nullcon <- file(nullfile(), open = "wb")
                  sink(nullcon, type = "message")
                  wait <- TRUE
                  while (wait) {
                    download <- tryCatch(download.file(xptj, destfile = fn, quiet = FALSE, mode = mode), 
                      error = function(e) "e", warning = function(w) "w")
                    wait <- ifelse(download == "e" | download == "w", TRUE, FALSE)
                  }
                  sink(type = "message")
                  close(nullcon)
                  if (tools::file_ext(fn) == "zip") {
                    oldwd <- getwd()
                    zip = fn
                    setwd(do::Replace0(fn, fj))
                    if (do::is.windows()) {
                      unzip(zipfile = fn, overwrite = TRUE)
                      (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(unzip(zipfile = fn, overwrite = TRUE, 
                        list = TRUE)[, "Name"])))
                    }
                    else {
                      suppressWarnings(untar(tarfile = fn))
                      (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(untar(tarfile = fn, list = TRUE)[, 
                        "Name"])))
                    }
                    setwd(oldwd)
                  }
                  cat(crayon::red(paste0(" download: ", filesize(fn), ")")))
                }
                else {
                  if (xpt) {
                    if (tools::file_ext(fn) == "zip") {
                      (zip = fn)
                      if (do::is.windows()) {
                        (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(unzip(zipfile = zip, overwrite = TRUE, 
                          list = TRUE)[, "Name"])))
                      }
                      else {
                        (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(untar(tarfile = zip, list = TRUE)[, 
                          "Name"])))
                      }
                      if (!file.exists(fn)) {
                        oldwd <- getwd()
                        setwd(do::Replace0(zip, fj))
                        if (do::is.windows()) {
                          unzip(zipfile = zip, overwrite = TRUE)
                        }
                        else {
                          untar(tarfile = zip)
                        }
                        setwd(oldwd)
                      }
                      else {
                        if (cat) 
                          cat(crayon::blue(paste0(" Exist: ", filesize(zip), ")")))
                      }
                    }
                    else {
                      if (cat) 
                        cat(crayon::blue(paste0(" Exist: ", filesize(fn), ")")))
                    }
                  }
                }
            }
            else {
                if (cat) 
                  cat(crayon::blue(paste0(" Exist: ", filesize(fn), ")")))
            }
        }
        else {
            if (xpt) {
                nullcon <- file(nullfile(), open = "wb")
                sink(nullcon, type = "message")
                wait <- TRUE
                while (wait) {
                  download <- tryCatch(download.file(xptj, destfile = fn, quiet = FALSE, mode = mode), 
                    error = function(e) "e", warning = function(w) "w")
                  wait <- ifelse(download == "e" | download == "w", TRUE, FALSE)
                }
                sink(type = "message")
                close(nullcon)
                if (tools::file_ext(fn) == "zip") {
                  oldwd <- getwd()
                  zip = fn
                  setwd(do::Replace0(fn, fj))
                  if (do::is.windows()) {
                    unzip(zipfile = fn, overwrite = TRUE)
                    (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(unzip(zipfile = fn, overwrite = TRUE, 
                      list = TRUE)[, "Name"])))
                  }
                  else {
                    suppressWarnings(untar(tarfile = fn))
                    (fn <- paste0(do::knife_right(fn, 3), tools::file_ext(untar(tarfile = fn, list = TRUE)[, 
                      "Name"])))
                  }
                  setwd(oldwd)
                }
                cat(crayon::red(paste0(" download: ", filesize(fn), ")")))
            }
        }
        if (tsv) 
            xpt2tsv(xpt = fn)
        if (varLabel | codebook) {
            wait <- 0
            while (wait < 10) {
                html <- tryCatch(xml2::read_html(url), error = function(e) "e")
                wait <- ifelse(is.character(html), wait + 1, 40)
            }
            if (wait != 40) 
                (next)(j)
        }
        if (varLabel) {
            (file <- do::Replace(fn, paste0("\\.", tools::file_ext(fn)), ".varLabel"))
            varLabel_url(url = docj, file = file, html = html)
        }
        if (codebook) {
            (file <- do::Replace(fn, paste0("\\.", tools::file_ext(fn)), ".codebook"))
            codebook_url(url = docj, file = file, html = html)
        }
        if (updatefile) {
            (file <- do::Replace(fn, paste0("\\.", tools::file_ext(fn)), ".update"))
            suppressWarnings(write.table(tablej, file, row.names = FALSE, sep = "\t"))
        }
    }
}
```

## `filesize` [internal]

```r
function (file) 
{
    size <- file.size(file)
    if (size < 1024) {
        paste(round(size, 2), "b")
    }
    else if (size < 1024 * 1024) {
        paste(round(size/1024, 2), "kb")
    }
    else if (size < 1024 * 1024 * 1024) {
        paste(round(size/1024/1024, 2), "mb")
    }
    else if (size < 1024 * 1024 * 1024 * 1024) {
        paste(round(size/1024/1024/1024, 2), "Gb")
    }
    else if (size < 1024 * 1024 * 1024 * 1024 * 1024) {
        paste(round(size/1024/1024/1024/1024, 2), "TB")
    }
}
```

## `forestplot` [exported]

```r
function (x, ...) 
UseMethod("forestplot")
```

## `formula2arguments` [internal]

```r
function () 
{
    x <- readClipboard()
    x
    writeClipboard(paste0(do::Replace0(x, ".*variable_formula\\(", ",.*"), " = FALSE, "))
}
```

## `fped0304` [internal]

```r
function (day = 1, dietary = "iff", grams = FALSE) 
{
    fpeddir <- paste0(get_config_path(), "/fped")
    f <- list.files(fpeddir, "equiv0304.sas7bdat", recursive = TRUE, full.names = TRUE)
    mped <- as.data.frame(haven::read_sas(f))
    colnames(mped) <- tolower(colnames(mped))
    mped <- drop_col(mped, "equivflag")
    colnames(mped)[1] <- "food.code"
    colnames(mped)[2] <- "mc"
    ckna <- is.na(mped$food.code)
    mped$food.code <- format(mped$food.code, width = 8)
    mped$food.code[ckna] <- NA
    mped$m_soy[mped$food.code == 11310000] <- 0
    mped$d_total[mped$food.code == 11310000] <- round(100 * (1/244), 3)
    mped$m_soy[mped$food.code == 11320000] <- 0
    mped$d_total[mped$food.code == 11320000] <- round(100 * (1/245), 3)
    mped$m_soy[mped$food.code == 11321000] <- 0
    mped$d_total[mped$food.code == 11321000] <- round(100 * (1/240), 3)
    mped$m_soy[mped$food.code == 11330000] <- 0
    mped$d_total[mped$food.code == 11330000] <- round(100 * (1/245), 3)
    ck <- mped$food.code == 58106210
    mped$g_total[ck] <- 1.8799999999999999
    mped$g_whl[ck] <- 0
    mped$g_nwhl[ck] <- 1.8799999999999999
    mped$v_total[ck] <- 0.12
    mped$v_tomato[ck] <- 0.12
    mped$d_total[ck] <- 0.69999999999999996
    mped$d_cheese[ck] <- 0.69999999999999996
    mped$discfat_oil[ck] <- 0.44
    mped$discfat_sol[ck] <- 8
    mped$add_sug[ck] <- 0.19
    ck <- mped$food.code == 58106220
    mped$g_total[ck] <- 1.75
    mped$g_whl[ck] <- 0
    mped$g_nwhl[ck] <- 1.75
    mped$v_total[ck] <- 0.12
    mped$v_tomato[ck] <- 0.12
    mped$d_total[ck] <- 0.66000000000000003
    mped$d_cheese[ck] <- 0.66000000000000003
    mped$discfat_oil[ck] <- 0.44
    mped$discfat_sol[ck] <- 10.619999999999999
    mped$add_sug[ck] <- 0.19
    ck <- mped$food.code == 58106230
    mped$g_total[ck] <- 1.8799999999999999
    mped$g_whl[ck] <- 0
    mped$g_nwhl[ck] <- 1.8799999999999999
    mped$v_total[ck] <- 0.12
    mped$v_tomato[ck] <- 0.12
    mped$d_total[ck] <- 0.66000000000000003
    mped$d_cheese[ck] <- 0.66000000000000003
    mped$discfat_oil[ck] <- 0.44
    mped$discfat_sol[ck] <- 8.8200000000000003
    mped$add_sug[ck] <- 0.19
    f <- list.files(fpeddir, "cnppmyp_v1nhanes0304_wjfrt.sas7bdat", recursive = TRUE, full.names = TRUE)
    jfrt <- as.data.frame(haven::read_sas(f))
    colnames(jfrt) <- tolower(colnames(jfrt))
    colnames(jfrt)[colnames(jfrt) %in% "foodcode"] <- "food.code"
    jfrt <- jfrt[, c("food.code", "modcode", "frtjuice", "wholefrt")]
    colnames(jfrt)[1] <- "food.code"
    colnames(jfrt)[2] <- "mc"
    ckna <- is.na(jfrt$food.code)
    jfrt$food.code <- format(jfrt$food.code, width = 8)
    jfrt$food.code[ckna] <- NA
    newmped <- dplyr::inner_join(mped, jfrt, c("food.code", "mc"))
    food <- nhs_read(nhs_tsv(sprintf("%siff_c", day), cat = FALSE), "dr1igrms,dr2igrms:grams", "dr1drstz,dr2drstz:rstz", 
        cat = FALSE, codebook = FALSE, Year = FALSE)
    demo <- nhs_read(nhs_tsv("demo_c", cat = FALSE), "ridageyr", cat = FALSE, codebook = FALSE, Year = FALSE)
    food <- dplyr::inner_join(food, demo, "seqn")
    colnames(food)[colnames(food) %in% c("dr1ifdcd", "dr2ifdcd")] <- "food.code"
    colnames(food)[colnames(food) %in% c("dr1mc", "dr2mc")] <- "mc"
    colnames(food)[colnames(food) %in% c("dr1iline", "dr2iline")] <- "line"
    isna <- is.na(newmped$mc)
    newmped$mc <- format(newmped$mc, width = 6)
    newmped$mc[isna] <- NA
    newmped$food.code <- as.numeric(newmped$food.code)
    fdpyr <- dplyr::inner_join(food, newmped, c("food.code", "mc"))
    pyrvar <- colnames(newmped)[-c(1, 2)]
    for (i in pyrvar) {
        fdpyr[, i] <- fdpyr[, i] * fdpyr$grams/100
    }
    if (grams) 
        pyrvar <- c(pyrvar, "grams")
    fdpyr <- fdpyr[, c("seqn", "line", "ridageyr", "rstz", "food.code", pyrvar)]
    fdpyr[, pyrvar][fdpyr[, pyrvar] < 0] <- 0
    if (dietary == "tot") {
        fped <- NULL
        for (i in pyrvar) {
            di <- aggregate(fdpyr[, i], list(seqn = fdpyr$seqn), FUN = sum)
            colnames(di)[2] <- i
            if (is.null(fped)) {
                fped <- di
            }
            else {
                fped <- dplyr::inner_join(fped, di, "seqn")
            }
        }
        fped[, pyrvar][fped[, pyrvar] < 0] <- 0
        fped <- dplyr::inner_join(fped, unique(fdpyr[, c("seqn", "ridageyr", "rstz")]), "seqn")
    }
    else {
        fped <- fdpyr
    }
    colnames(fped)[colnames(fped) == "wholefrt"] <- "f_whole"
    colnames(fped)[colnames(fped) == "frtjuice"] <- "f_juice"
    colnames(fped)[colnames(fped) == "v_orange"] <- "v_dpyel"
    fped <- drop_col(fped, "line")
    return(fped)
}
```

## `freq_count` [exported]

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

## `freq_mean` [exported]

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

## `full_join_character` [internal]

```r
function (model.i) 
{
    if (length(model.i) == 1) 
        return(model.i[[1]])
    for (i in 1:length(model.i)) {
        dii <- model.i[[i]]
        for (j in 1:nrow(dii)) {
            if (do::left(dii$character[j], 8) == "data&&y:") {
                pre <- dii$character[j]
            }
            else {
                dii$character[j] <- paste0(pre, "------>>>", dii$character[j])
            }
        }
        model.i[[i]] <- dii
    }
    di <- model.i[[1]]
    for (i in 2:length(model.i)) {
        di <- dplyr::full_join(di, model.i[[i]], "character")
    }
    di$character <- do::Replace0(di$character, ".*------>>>")
    di
}
```

## `getChangepoints` [exported]

```r
function (r, range = NULL) 
UseMethod("getChangepoints")
```

## `getKnot` [exported]

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

## `getReference` [exported]

```r
function (r) 
UseMethod("getReference")
```

## `get_Flavonoids_path` [internal]

```r
function () 
{
    (dir <- paste0(get_config_path(), "/Flavonoids"))
    if (!dir.exists(dir)) 
        dir.create(dir)
    dir
}
```

## `get_mort_path` [exported]

```r
function () 
{
    paste0(get_config_path(TRUE), "mort/")
}
```

## `group_cal` [internal]

```r
function (d, mean_vars = NULL, median_vars = NULL, sd_vars = NULL, max_vars = NULL, min_vars = NULL, 
    sum_vars = NULL, uniq_vars = NULL, paste_vars = NULL, uniq_past_vars = NULL, collapse = ",", bys = NULL) 
{
    d <- data.table::data.table(d)
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    v <- c()
    if (!is.null(mean_vars)) 
        v <- c(v, sprintf("%s = mean(%s,na.rm=T)", do::Replace0(mean_vars, ".*:"), do::Replace0(mean_vars, 
            ":.*")))
    if (!is.null(sd_vars)) 
        v <- c(v, sprintf("%s = sd(%s,na.rm=T)", do::Replace0(sd_vars, ".*:"), do::Replace0(sd_vars, 
            ":.*")))
    if (!is.null(median_vars)) 
        v <- c(v, sprintf("%s = median(%s,na.rm=T)", do::Replace0(median_vars, ".*:"), do::Replace0(median_vars, 
            ":.*")))
    if (!is.null(max_vars)) 
        v <- c(v, sprintf("%s = max(%s,na.rm=T)", do::Replace0(max_vars, ".*:"), do::Replace0(max_vars, 
            ":.*")))
    if (!is.null(min_vars)) 
        v <- c(v, sprintf("%s = min(%s,na.rm=T)", do::Replace0(min_vars, ".*:"), do::Replace0(min_vars, 
            ":.*")))
    if (!is.null(sum_vars)) 
        v <- c(v, sprintf("%s = sum(%s,na.rm=T)", do::Replace0(sum_vars, ".*:"), do::Replace0(sum_vars, 
            ":.*")))
    if (!is.null(uniq_vars)) 
        v <- c(v, sprintf("%s = unique(%s)", do::Replace0(uniq_vars, ".*:"), do::Replace0(uniq_vars, 
            ":.*")))
    if (!is.null(paste_vars)) {
        (v1 <- do::Replace0(paste_vars, ".*:"))
        if (any(do::right(v1, 2) == "-u")) 
            v1[do::right(v1, 2) == "-u"] <- do::knife_right(v1[do::right(v1, 2) == "-u"], 2)
        (v2 <- do::Replace0(paste_vars, ":.*"))
        (uiq <- do::right(v2, 2) == "-u")
        if (any(uiq)) {
            v2[uiq] <- do::knife_right(v2[uiq], 2)
            v2[uiq] <- paste0("kit::funique(", v2[uiq], ")")
        }
        vi <- sprintf("%s = group_use_paste(%s,collapse=collapse)", v1, v2)
        v <- c(v, vi)
    }
    if (!is.null(uniq_past_vars)) {
        (v1 <- do::Replace0(uniq_past_vars, ".*:"))
        if (any(do::right(v1, 2) == "-u")) 
            v1[do::right(v1, 2) == "-u"] <- do::knife_right(v1[do::right(v1, 2) == "-u"], 2)
        (v2 <- do::Replace0(uniq_past_vars, ":.*"))
        (uiq <- do::right(v2, 2) == "-u")
        if (any(uiq)) {
            v2[uiq] <- do::knife_right(v2[uiq], 2)
            v2[uiq] <- paste0("unique_no_NA(", v2[uiq], ")")
        }
        vi <- sprintf("%s = unique_no_NA(%s,collapse)", v1, v2)
        v <- c(v, vi)
    }
    (v <- paste0(v, collapse = ",\n"))
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    if (!is.null(uniq_past_vars)) {
        for (i in do::Replace0(uniq_past_vars, ".*:")) {
            d[d[, i] == "thisisNANAisTHIS", i] <- NA
        }
    }
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_max` [internal]

```r
function (d, vars = NULL, bys = NULL) 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    vars[!grepl(":", vars)] <- paste0(vars[!grepl(":", vars)], ":", vars[!grepl(":", vars)])
    v <- sprintf("%s = max(%s,na.rm=T)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_mean` [exported]

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

## `group_min` [internal]

```r
function (d, vars = NULL, bys = NULL) 
{
    (by <- do::Replace0(bys, ":.*"))
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    vars[!grepl(":", vars)] <- paste0(vars[!grepl(":", vars)], ":", vars[!grepl(":", vars)])
    v <- sprintf("%s = min(%s,na.rm=T)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_paste` [internal]

```r
function (d, vars = NULL, bys = NULL, collapse = ",") 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    (v1 <- do::Replace0(vars, ".*:"))
    if (any(do::right(v1, 2) == "-u")) 
        v1[do::right(v1, 2) == "-u"] <- do::knife_right(v1[do::right(v1, 2) == "-u"], 2)
    (v2 <- do::Replace0(vars, ":.*"))
    (uiq <- do::right(v2, 2) == "-u")
    if (any(uiq)) {
        v2[uiq] <- do::knife_right(v2[uiq], 2)
        v2[uiq] <- paste0("kit::funique(", v2[uiq], ")")
    }
    v <- sprintf("%s = group_use_paste(%s,collapse=collapse)", v1, v2) %>% paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_sd` [internal]

```r
function (d, vars = NULL, bys = NULL) 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    vars[!grepl(":", vars)] <- paste0(vars[!grepl(":", vars)], ":", vars[!grepl(":", vars)])
    v <- sprintf("%s = sd(%s,na.rm=T)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_sum` [internal]

```r
function (d, vars = NULL, bys = NULL) 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    vars[!grepl(":", vars)] <- paste0(vars[!grepl(":", vars)], ":", vars[!grepl(":", vars)])
    v <- sprintf("%s = sum(%s,na.rm=T)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_unique` [internal]

```r
function (d, vars = NULL, bys = NULL) 
{
    by <- do::Replace0(bys, ":.*")
    bys[!grepl(":", bys)] <- paste0(bys[!grepl(":", bys)], ":", bys[!grepl(":", bys)])
    d <- data.table::data.table(d)
    v <- sprintf("%s = kit::funique(%s)", do::Replace0(vars, ".*:"), do::Replace0(vars, ":.*", vars)) %>% 
        paste0(collapse = ",\n")
    st <- "d[,.(\n        %s\n    ),by=.(%s)] |> suppressWarnings()"
    d <- eval(parse(text = sprintf(st, v, paste0(by, collapse = ", "))))
    d <- as.data.frame(eval(parse(text = sprintf("d[order(%s),]", paste0(by, collapse = ",")))))
    col_rename(d) <- bys
    inf2NA(d)
}
```

## `group_use_paste` [internal]

```r
function (x, collapse = ",") 
{
    if (all(is.na(x))) 
        return(".._..NA.._..")
    paste0(x[!is.na(x)], collapse = collapse)
}
```

## `head4span` [internal]

```r
function (x, p1 = NULL, p2 = NULL, rm0 = F) 
{
    (x1 <- x[-length(x)])
    (x2 <- x[-1])
    (end <- c(which(x2 != x1), length(x)))
    (start <- c(1, end[-length(end)] + 1))
    hs <- lapply(1:length(start), function(i) {
        c(p1, p2, start[i], end[i])
    })
    if (rm0) {
        ck <- sapply(hs, function(i) (i[4] - i[3]) == 0)
        hs <- hs[!ck]
    }
    hs
}
```

## `hei_2010` [internal]

```r
function (indat, kcal = "dr1tkcal", lv_total = "legume_added_dr1t_v_total", lbeangrn = "legume_added_beangrn", 
    f_total = "dr1t_f_total", wholefrt = "wholefrt", g_whl = "dr1t_g_whole", d_total = "dr1t_d_total", 
    lallmeat = "legume_added_allmeat", lseaplant = "legume_added_seaplant", monopoly = "monopoly", sfat = "dr1tsfat", 
    sodi = "dr1tsodi", g_nwhl = "dr1t_g_refined", emptycal10 = "emptycal10", varLabel = FALSE, energy = TRUE, 
    component = TRUE, density = FALSE, join = "seqn") 
{
    k0 <- indat[, kcal] > 0
    indat$vegden[k0] <- indat[k0, lv_total]/(indat[k0, kcal]/1000)
    indat$heix1_totalveg = 5 * (indat$vegden/1.1000000000000001)
    indat$heix1_totalveg[indat$heix1_totalveg > 5] <- 5
    indat$heix1_totalveg[indat$vegden == 0] <- 0
    indat$grbnden[k0] = indat[k0, lbeangrn]/(indat[k0, kcal]/1000)
    indat$heix2_green_and_bean = 5 * (indat$grbnden/0.20000000000000001)
    indat$heix2_green_and_bean[indat$heix2_green_and_bean > 5] <- 5
    indat$heix2_green_and_bean[indat$grbnden == 0] <- 0
    indat$frtden[k0] = indat[k0, f_total]/(indat[k0, kcal]/1000)
    indat$heix3_totalfruit = 5 * (indat$frtden/0.80000000000000004)
    indat$heix3_totalfruit[indat$heix3_totalfruit > 5] <- 5
    indat$heix3_totalfruit[indat$frtden == 0] <- 0
    indat$whfrden[k0] = indat[k0, wholefrt]/(indat[k0, kcal]/1000)
    indat$heix4_wholefruit = 5 * (indat$whfrden/0.40000000000000002)
    indat$heix4_wholefruit[indat$heix4_wholefruit > 5] <- 5
    indat$heix4_wholefruit[indat$whfrden == 0] <- 0
    indat$wgrnden[k0] = indat[k0, g_whl]/(indat[k0, kcal]/1000)
    indat$heix5_wholegrain = 10 * (indat[, "wgrnden"]/1.5)
    indat$heix5_wholegrain[indat$heix5_wholegrain > 10] <- 10
    indat$heix5_wholegrain[indat$wgrnden == 0] <- 0
    indat$dairyden[k0] = indat[k0, d_total]/(indat[k0, kcal]/1000)
    indat$heix6_totaldairy = 10 * (indat$dairyden/1.3)
    indat$heix6_totaldairy[indat$heix6_totaldairy > 10] <- 10
    indat$heix6_totaldairy[indat$dairyden == 0] <- 0
    indat$meatden[k0] = indat[k0, lallmeat]/(indat[k0, kcal]/1000)
    indat$heix7_totprot = 5 * (indat$meatden/2.5)
    indat$heix7_totprot[indat$heix7_totprot > 5] <- 5
    indat$heix7_totprot[indat$meatden == 0] <- 0
    indat$seaplden[k0] <- indat[k0, lseaplant]/(indat[k0, kcal]/1000)
    indat$heix8_seaplant_prot = 5 * (indat$seaplden/0.80000000000000004)
    indat$heix8_seaplant_prot[indat$heix8_seaplant_prot > 5] <- 5
    indat$heix8_seaplant_prot[indat$seaplden == 0] <- 0
    indat$faratio[indat[, sfat] > 0] <- indat[indat[, sfat] > 0, "monopoly"]/indat[indat[, sfat] > 0, 
        sfat]
    farmin = 1.2
    farmax = 2.5
    indat$heix9_fattyacid <- ifelse(indat[, sfat] == 0 & indat[, monopoly] == 0, 0, ifelse(indat[, sfat] == 
        0 & indat[, monopoly] > 0, 10, ifelse(indat[, "faratio"] >= farmax, 10, ifelse(indat[, "faratio"] <= 
        farmin, 0, 10 * (indat[, "faratio"] - farmin)/(farmax - farmin)))))
    indat$sodden[k0] <- indat[k0, sodi]/indat[k0, kcal]
    sodmin = 1.1000000000000001
    sodmax = 2
    indat$heix10_sodium <- ifelse(indat[, "sodden"] <= sodmin, 10, ifelse(indat[, "sodden"] >= sodmax, 
        0, 10 - (10 * (indat[, "sodden"] - sodmin)/(sodmax - sodmin))))
    indat$rgden[k0] <- indat[k0, g_nwhl]/(indat[k0, kcal]/1000)
    rgmin = 1.8
    rgmax = 4.2999999999999998
    indat$heix11_refinedgrain <- ifelse(indat[, "rgden"] <= rgmin, 10, ifelse(indat[, "rgden"] >= rgmax, 
        0, 10 - (10 * (indat[, "rgden"] - rgmin)/(rgmax - rgmin))))
    indat$sofa_perc[k0] <- 100 * indat[k0, "emptycal10"]/indat[k0, kcal]
    sofamin = 19
    sofamax = 50
    indat$heix12_sofaas <- ifelse(indat$sofa_perc <= sofamin, 20, ifelse(indat$sofa_perc >= sofamax, 
        0, 20 - (20 * (indat$sofa_perc - sofamin)/(sofamax - sofamin))))
    indat$heix1_totalveg[indat[, kcal] == 0] <- 0
    indat$heix2_green_and_bean[indat[, kcal] == 0] <- 0
    indat$heix3_totalfruit[indat[, kcal] == 0] <- 0
    indat$heix4_wholefruit[indat[, kcal] == 0] <- 0
    indat$heix5_wholegrain[indat[, kcal] == 0] <- 0
    indat$heix6_totaldairy[indat[, kcal] == 0] <- 0
    indat$heix7_totprot[indat[, kcal] == 0] <- 0
    indat$heix8_seaplant_prot[indat[, kcal] == 0] <- 0
    indat$heix9_fattyacid[indat[, kcal] == 0] <- 0
    indat$heix10_sodium[indat[, kcal] == 0] <- 0
    indat$heix11_refinedgrain[indat[, kcal] == 0] <- 0
    indat$heix12_sofaas[indat[, kcal] == 0] <- 0
    indat$hei2010_total_score = with(indat, heix1_totalveg + heix2_green_and_bean + heix3_totalfruit + 
        heix4_wholefruit + heix5_wholegrain + heix6_totaldairy + heix7_totprot + heix8_seaplant_prot + 
        heix9_fattyacid + heix10_sodium + heix11_refinedgrain + heix12_sofaas)
    if (varLabel) {
        indat <- expss::apply_labels(indat, hei2010_total_score = "total hei-2010 score", heix1_totalveg = "hei-2010 component 1 total vegetables", 
            heix2_green_and_bean = "hei-2010 component 2 greens and beans", heix3_totalfruit = "hei-2010 component 3 total fruit", 
            heix4_wholefruit = "hei-2010 component 4 whole fruit", heix5_wholegrain = "hei-2010 component 5 whole grains", 
            heix6_totaldairy = "hei-2010 component 6 dairy", heix7_totprot = "hei-2010 component 7 total protein foods", 
            heix8_seaplant_prot = "hei-2010 component 8 seafood and plant protein", heix9_fattyacid = "hei-2010 component 9 fatty acid ratio", 
            heix10_sodium = "hei-2010 component 10 sodium", heix11_refinedgrain = "hei-2010 component 11 refined grains", 
            heix12_sofaas = "hei-2010 component 12 sofaas calories", vegden = "density of mped/fped total vegetables per 1000 kcal", 
            grbnden = "density of mped/fped of dark green veg and beans per 1000 kcal", frtden = "density of mped/fped total fruit per 1000 kcal", 
            whfrden = "density of mped/fped whole fruit per 1000 kcal", wgrnden = "density of mped/fped of whole grain per 1000 kcal", 
            dairyden = "density of mped/fped of dairy per 1000 kcal", meatden = "density of mped/fped total meat/protein per 1000 kcal", 
            seaplden = "denstiy of mped/fped of seafood and plant protein per 1000 kcal", faratio = "fatty acid ratio", 
            sodden = "density of sodium per 1000 kcal", rgden = "density of mped/fped of refined grains per 1000 kcal", 
            sofa_perc = "percent of calories from added sugar, solid fat, and alcohol")
    }
    colnms <- c(join, "hei2010_total_score")
    if (energy) 
        colnms <- c(join, kcal, "hei2010_total_score")
    if (component) 
        colnms <- c(colnms, c("heix1_totalveg", "heix2_green_and_bean", "heix3_totalfruit", "heix4_wholefruit", 
            "heix5_wholegrain", "heix6_totaldairy", "heix7_totprot", "heix8_seaplant_prot", "heix9_fattyacid", 
            "heix10_sodium", "heix11_refinedgrain", "heix12_sofaas"))
    if (density) 
        colnms <- c(colnms, "vegden", "grbnden", "frtden", "whfrden", "wgrnden", "dairyden", "meatden", 
            "seaplden", "faratio", "sodden", "rgden", "sofa_perc")
    indat[, colnms]
}
```

## `hei_2010_PerDay_pratio` [internal]

```r
function (seqn = NULL, years = 1999, day = "1", dietary = "tot", seed = NULL, varLabel = FALSE) 
{
    if (dietary == "iff") 
        join <- c("seqn", "line")
    else join <- "seqn"
    fped <- fped_read(years = years, day = day, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(ifelse(day == "1", sprintf("drx%s|dr1%s", dietary, dietary), sprintf("drx%s|dr2%s", 
        dietary, dietary)), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "wtdr4yr", "wtdrd1", "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", 
        "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= maxalcgr, 0, 7 * (dt$alco - maxalcgr))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    demo <- nhs_read(nhs_tsv("demo", years = years, cat = FALSE), "sdmvstra", "sdmvpsu", cat = FALSE, 
        Year = FALSE)
    indat <- dplyr::inner_join(indat, demo, "seqn")
    indat <- wt_dr_day1(data = indat, wtname = "wtdr", cat = FALSE)
    if (!is.null(seqn)) 
        indat <- indat[indat$seqn %in% seqn, ]
    choice <- c("kcal", "v_total", "v_drkgr", "v_legumes", "f_total", "f_whole", "g_whole", "d_total", 
        "pf_total", "seaplant", "monopoly", "sfat", "sodi", "g_refined", "emptycal10")
    for (i in choice) attributes(indat[, i]) <- NULL
    indat1 <- reshape2::melt(indat[, c(join, choice)], id.vars = join)
    one <- dplyr::inner_join(indat[, c(join, choice, "sdmvstra", "sdmvpsu", "wtdr")], indat1, join)
    head(one)
    for (i in choice) one[, i] <- ifelse(one$variable == i, 1, 0)
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = one)
    glm <- survey::svyglm(value ~ -1 + kcal + v_total + v_drkgr + v_legumes + f_total + f_whole + g_whole + 
        d_total + pf_total + seaplant + monopoly + sfat + sodi + g_refined + emptycal10, design = dg)
    sigma <- glm$cov.unscaled
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = indat)
    mean <- survey::svymean(~kcal + v_total + v_drkgr + v_legumes + f_total + f_whole + g_whole + d_total + 
        pf_total + seaplant + monopoly + sfat + sodi + g_refined + emptycal10, dg)
    mu <- as.data.frame(mean)[, 1]
    if (!is.null(seed)) 
        set.seed(seed)
    indat <- as.data.frame(mvtnorm::rmvnorm(n = 10000, mean = mu, sigma = sigma))
    colnames(indat) <- colnames(sigma)
    afterleg <- leg2010a(indat = indat, kcal = "kcal", allmeat = "pf_total", seaplant = "seaplant", v_total = "v_total", 
        v_drkgr = "v_drkgr", legumes = "v_legumes")
    aftermac <- hei_2010(indat = afterleg, kcal = "kcal", lv_total = "legume_added_v_total", lbeangrn = "legume_added_beangrn", 
        f_total = "f_total", wholefrt = "f_whole", g_whl = "g_whole", d_total = "d_total", lallmeat = "legume_added_allmeat", 
        lseaplant = "legume_added_seaplant", monopoly = "monopoly", sfat = "sfat", sodi = "sodi", g_nwhl = "g_refined", 
        emptycal10 = "emptycal10", varLabel = varLabel, energy = FALSE, component = TRUE, density = FALSE, 
        join = NULL)
    head(aftermac)
    data.frame(min = sapply(aftermac, min), max = sapply(aftermac, max), mean = sapply(aftermac, mean), 
        sd = sapply(aftermac, sd), lowci = sapply(aftermac, function(i) quantile(i, 0.025000000000000001)), 
        upci = sapply(aftermac, function(i) quantile(i, 0.97499999999999998)))
}
```

## `hei_2010_PerDay_ssum` [internal]

```r
function (years, day = "2", dietary = "tot", varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, 
    version = 2010) 
{
    if (dietary == "iff") 
        join <- c("seqn", "food.code")
    else join <- "seqn"
    fped <- fped_read(years = years, day = day, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(ifelse(day == "1", sprintf("drx%s|dr1%s", dietary, dietary), sprintf("drx%s|dr2%s", 
        dietary, dietary)), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", 
        "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", 
        "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", 
        codebook = FALSE, varLabel = FALSE, cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    dt$maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= dt$maxalcgr, 0, 7 * (dt$alco - dt$maxalcgr))
    dt$line <- NULL
    dt$dr1mc <- NULL
    dt <- group_sum(dt, c("kcal", "sfat", "alco", "sodi", "mfat", "pfat", "monopoly", "maxalcgr", "exalccal"), 
        c("Year", join))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    afterleg <- leg2010a(indat = indat, kcal = "kcal", allmeat = "pf_total", seaplant = "seaplant", v_total = "v_total", 
        v_drkgr = "v_drkgr", legumes = "v_legumes")
    hei_2010(indat = afterleg, kcal = "kcal", lv_total = "legume_added_v_total", lbeangrn = "legume_added_beangrn", 
        f_total = "f_total", wholefrt = "f_whole", g_whl = "g_whole", d_total = "d_total", lallmeat = "legume_added_allmeat", 
        lseaplant = "legume_added_seaplant", monopoly = "monopoly", sfat = "sfat", sodi = "sodi", g_nwhl = "g_refined", 
        emptycal10 = "emptycal10", varLabel = varLabel, energy = energy, component = component, density = density, 
        join = join)
}
```

## `hei_2010_PerPerson_pratio` [internal]

```r
function (seqn = NULL, years = years, dietary = "tot", seed = NULL) 
{
    if (dietary == "iff") 
        join <- c("seqn", "line")
    else join <- "seqn"
    fped <- fped_read(years = years, day = 1, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(sprintf("drx%s|dr1%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "wtdr4yr", "wtdrd1", "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", 
        "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= maxalcgr, 0, 7 * (dt$alco - maxalcgr))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    indat1 <- indat
    fped <- fped_read(years = years, day = 2, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(sprintf("drx%s|dr2%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", 
        "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", 
        "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", 
        codebook = FALSE, varLabel = FALSE, cat = FALSE, Year = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= maxalcgr, 0, 7 * (dt$alco - maxalcgr))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    indat2 <- indat
    indat <- dplyr::inner_join(indat1, indat2, join)
    indat <- wt_dr_day1(indat, wtname = "wtdr", cat = FALSE)
    if (!is.null(seqn)) 
        indat <- indat[indat$seqn %in% seqn, ]
    choice <- choice <- do::knife_right(colnames(indat)[do::right(colnames(indat), 2) == ".x"], 2)
    for (i in choice) {
        which <- which(colnames(indat) %in% paste0(i, c(".x", ".y")))
        indat$last <- row.sums(indat[, which])
        indat <- indat[, -which]
        colnames(indat)[ncol(indat)] <- i
    }
    do::increase(colnames(indat))
    ck <- indat$Year %in% c("1999-2000", "2001-2002")
    indat[ck, choice] <- indat[ck, choice]/2
    demo <- nhs_read(nhs_tsv("demo", years = years, cat = FALSE), "sdmvstra", "sdmvpsu", cat = FALSE, 
        Year = FALSE)
    indat <- dplyr::inner_join(indat, demo, "seqn")
    choice <- c("kcal", "v_total", "v_drkgr", "v_legumes", "f_total", "f_whole", "g_whole", "d_total", 
        "pf_total", "seaplant", "monopoly", "sfat", "sodi", "g_refined", "emptycal10")
    for (i in choice) attributes(indat[, i]) <- NULL
    indat1 <- reshape2::melt(indat[, c(join, choice)], id.vars = join)
    one <- dplyr::inner_join(indat[, c(join, choice, "sdmvstra", "sdmvpsu", "wtdr")], indat1, join)
    head(one)
    for (i in choice) one[, i] <- ifelse(one$variable == i, 1, 0)
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = one)
    glm <- survey::svyglm(value ~ -1 + kcal + v_total + v_drkgr + v_legumes + f_total + f_whole + g_whole + 
        d_total + pf_total + seaplant + monopoly + sfat + sodi + g_refined + emptycal10, design = dg)
    sigma <- glm$cov.unscaled
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = indat)
    mean <- survey::svymean(~kcal + v_total + v_drkgr + v_legumes + f_total + f_whole + g_whole + d_total + 
        pf_total + seaplant + monopoly + sfat + sodi + g_refined + emptycal10, dg)
    mu <- as.data.frame(mean)[, 1]
    if (!is.null(seed)) 
        set.seed(seed)
    indat <- as.data.frame(mvtnorm::rmvnorm(n = 10000, mean = mu, sigma = sigma))
    colnames(indat) <- colnames(sigma)
    afterleg <- leg2010a(indat = indat, kcal = "kcal", allmeat = "pf_total", seaplant = "seaplant", v_total = "v_total", 
        v_drkgr = "v_drkgr", legumes = "v_legumes")
    aftermac <- hei_2010(indat = afterleg, kcal = "kcal", lv_total = "legume_added_v_total", lbeangrn = "legume_added_beangrn", 
        f_total = "f_total", wholefrt = "f_whole", g_whl = "g_whole", d_total = "d_total", lallmeat = "legume_added_allmeat", 
        lseaplant = "legume_added_seaplant", monopoly = "monopoly", sfat = "sfat", sodi = "sodi", g_nwhl = "g_refined", 
        emptycal10 = "emptycal10", varLabel = FALSE, energy = FALSE, component = TRUE, density = FALSE, 
        join = NULL)
    head(aftermac)
    data.frame(min = sapply(aftermac, min), max = sapply(aftermac, max), mean = sapply(aftermac, mean), 
        sd = sapply(aftermac, sd), lowci = sapply(aftermac, function(i) quantile(i, 0.025000000000000001)), 
        upci = sapply(aftermac, function(i) quantile(i, 0.97499999999999998)))
}
```

## `hei_2010_PerPerson_ssum` [internal]

```r
function (years, dietary = "tot", varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, 
    both2days = F) 
{
    if (dietary == "iff") 
        join <- c("seqn", "line")
    else join <- "seqn"
    fped <- fped_read(years = years, day = 1, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(sprintf("drx%s|dr1%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "wtdr4yr", "wtdrd1", "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", 
        "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= maxalcgr, 0, 7 * (dt$alco - maxalcgr))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    indat1 <- indat
    fped <- fped_read(years = years, day = 2, dietary = dietary, version = 2010)
    tsv <- nhs_tsv(sprintf("drx%s|dr2%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr2tkcal,dr1ikcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr2tsfat,dr1isfat,dr2isfat:sfat", 
        "drxtalco,drxialco,dr1talco,dr2talco,dr1ialco,dr2ialco:alco", "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", 
        "drxtmfat,drximfat,dr1tmfat,dr2tmfat,dr1imfat,dr2imfat:mfat", "drxtpfat,drxipfat,dr1tpfat,dr2tpfat,dr1ipfat,dr2ipfat:pfat", 
        codebook = FALSE, varLabel = FALSE, cat = FALSE, Year = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    maxalcgr <- 13 * (dt$kcal/1000)
    dt$exalccal <- ifelse(dt$alco <= maxalcgr, 0, 7 * (dt$alco - maxalcgr))
    indat <- dplyr::inner_join(dt, fped, join)
    indat$emptycal10 <- indat$addsugc + indat$solfatc + indat$exalccal
    indat2 <- indat
    indat <- dplyr::full_join(indat1, indat2, join)
    choice <- choice <- do::knife_right(colnames(indat)[do::right(colnames(indat), 2) == ".x"], 2)
    for (i in choice) {
        (which <- which(colnames(indat) %in% paste0(i, c(".x", ".y"))))
        if (length(which) == 0) 
            (next)(i)
        indat$last <- row.means(indat[, which], na.rm = !both2days)
        indat <- indat[, -which]
        colnames(indat)[ncol(indat)] <- i
    }
    do::increase(colnames(indat))
    ck <- indat$Year %in% c("1999-2000", "2001-2002")
    indat[ck, choice] <- indat[ck, choice]/2
    afterleg <- leg2010a(indat = indat, kcal = "kcal", allmeat = "pf_total", seaplant = "seaplant", v_total = "v_total", 
        v_drkgr = "v_drkgr", legumes = "v_legumes")
    hei_2010(indat = afterleg, kcal = "kcal", lv_total = "legume_added_v_total", lbeangrn = "legume_added_beangrn", 
        f_total = "f_total", wholefrt = "f_whole", g_whl = "g_whole", d_total = "d_total", lallmeat = "legume_added_allmeat", 
        lseaplant = "legume_added_seaplant", monopoly = "monopoly", sfat = "sfat", sodi = "sodi", g_nwhl = "g_refined", 
        emptycal10 = "emptycal10", varLabel = varLabel, energy = energy, component = component, density = density, 
        join = join)
}
```

## `hei_2015` [internal]

```r
function (indat = indat, kcal = "dr1tkcal", vtotalleg = "vtotalleg", vdrkgrleg = "vdrkgrleg", f_total = "dr1t_f_total", 
    fwholefrt = "fwholefrt", g_whole = "dr1t_g_whole", d_total = "dr1t_d_total", pfallprotleg = "pfallprotleg", 
    pfseaplantleg = "pfseaplantleg", monopoly = "monopoly", satfat = "dr1tsfat", sodium = "dr1tsodi", 
    g_refined = "dr1t_g_refined", add_sugars = "dr1t_add_sugars", varLabel = FALSE, energy = TRUE, component = TRUE, 
    density = FALSE, join = "seqn") 
{
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$frtden[ck] <- indat[ck, f_total]/(indat[ck, kcal]/1000)
    indat$hei2015c3_totalfruit = 5 * (indat$frtden/0.80000000000000004)
    indat$hei2015c3_totalfruit[indat$hei2015c3_totalfruit > 5] <- 5
    indat$hei2015c3_totalfruit[indat$frtden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$whfrden[ck] <- indat[ck, fwholefrt]/(indat[ck, kcal]/1000)
    indat$hei2015c4_wholefruit = 5 * (indat$whfrden/0.40000000000000002)
    indat$hei2015c4_wholefruit[indat$hei2015c4_wholefruit > 5] <- 5
    indat$hei2015c4_wholefruit[indat$whfrden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$vegden[ck] <- indat[ck, vtotalleg]/(indat[ck, kcal]/1000)
    indat$hei2015c1_totalveg = 5 * (indat$vegden/1.1000000000000001)
    indat$hei2015c1_totalveg[indat$hei2015c1_totalveg > 5] <- 5
    indat$hei2015c1_totalveg[indat$vegden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$grbnden[ck] <- indat[ck, vdrkgrleg]/(indat[ck, kcal]/1000)
    indat$hei2015c2_green_and_bean = 5 * (indat$grbnden/0.20000000000000001)
    indat$hei2015c2_green_and_bean[indat$hei2015c2_green_and_bean > 5] <- 5
    indat$hei2015c2_green_and_bean[indat$grbnden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$wgrnden[ck] <- indat[ck, g_whole]/(indat[ck, kcal]/1000)
    indat$hei2015c5_wholegrain = 10 * (indat$wgrnden/1.5)
    indat$hei2015c5_wholegrain[indat$hei2015c5_wholegrain > 10] <- 10
    indat$hei2015c5_wholegrain[indat$wgrnden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$dairyden[ck] <- indat[ck, d_total]/(indat[ck, kcal]/1000)
    indat$hei2015c6_totaldairy = 10 * (indat$dairyden/1.3)
    indat$hei2015c6_totaldairy[indat$hei2015c6_totaldairy > 10] <- 10
    indat$hei2015c6_totaldairy[indat$dairyden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$protden[ck] <- indat[ck, pfallprotleg]/(indat[ck, kcal]/1000)
    indat$hei2015c7_totprot = 5 * (indat$protden/2.5)
    indat$hei2015c7_totprot[indat$hei2015c7_totprot > 5] <- 5
    indat$hei2015c7_totprot[indat$protden == 0] <- 0
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$seaplden[ck] <- indat[ck, pfseaplantleg]/(indat[ck, kcal]/1000)
    indat$hei2015c8_seaplant_prot = 5 * (indat$seaplden/0.80000000000000004)
    indat$hei2015c8_seaplant_prot[indat$hei2015c8_seaplant_prot > 5] <- 5
    indat$hei2015c8_seaplant_prot[indat$seaplden == 0] <- 0
    ck <- indat[, satfat] > 0 & !is.na(indat[, satfat])
    indat$faratio[ck] <- indat[ck, monopoly]/indat[ck, satfat]
    indat$hei2015c9_fattyacid <- ifelse(indat[, satfat] == 0 & indat[, monopoly] == 0, 0, ifelse(indat[, 
        satfat] == 0 & indat[, monopoly] > 0, 10, ifelse(indat$faratio >= 2.5, 10, ifelse(indat$faratio <= 
        1.2, 0, 10 * ((indat$faratio - 1.2)/(2.5 - 1.2))))))
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$rgden[ck] <- indat[ck, g_refined]/(indat[ck, kcal]/1000)
    indat$hei2015c11_refinedgrain <- ifelse(indat$rgden <= 1.8, 10, ifelse(indat$rgden >= 4.2999999999999998, 
        0, 10 - (10 * (indat$rgden - 1.8)/(4.2999999999999998 - 1.8))))
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$sodden[ck] <- indat[ck, sodium]/indat[ck, kcal]
    sodmin = sodmax = indat$hei2015c10_sodium <- ifelse(indat$sodden <= 1.1000000000000001, 10, ifelse(indat$sodden >= 
        2, 0, 10 - (10 * (indat$sodden - 1.1000000000000001)/(2 - 1.1000000000000001))))
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$addsug_perc[ck] <- 100 * (indat[ck, add_sugars] * 16/indat[ck, kcal])
    indat$hei2015c13_addsug <- ifelse(indat$addsug_perc >= 26, 0, ifelse(indat$addsug_perc <= 6.5, 10, 
        10 - (10 * (indat$addsug_perc - 6.5)/(26 - 6.5))))
    ck <- indat[, kcal] > 0 & !is.na(indat[, kcal])
    indat$sfat_perc[ck] <- 100 * (indat[ck, satfat] * 9/indat[ck, kcal])
    indat$hei2015c12_sfat <- ifelse(indat$sfat_perc >= 16, 0, ifelse(indat$sfat_perc <= 8, 10, 10 - (10 * 
        (indat$sfat_perc - 8)/(16 - 8))))
    ck <- indat[, kcal] %in% 0
    indat$hei2015c1_totalveg[ck] = 0
    indat$hei2015c2_green_and_bean[ck] = 0
    indat$hei2015c3_totalfruit[ck] = 0
    indat$hei2015c4_wholefruit[ck] = 0
    indat$hei2015c5_wholegrain[ck] = 0
    indat$hei2015c6_totaldairy[ck] = 0
    indat$hei2015c7_totprot[ck] = 0
    indat$hei2015c8_seaplant_prot[ck] = 0
    indat$hei2015c9_fattyacid[ck] = 0
    indat$hei2015c10_sodium[ck] = 0
    indat$hei2015c11_refinedgrain[ck] = 0
    indat$hei2015c12_sfat[ck] = 0
    indat$hei2015c13_addsug[ck] = 0
    indat$hei2015_total_score <- with(indat, hei2015c1_totalveg + hei2015c2_green_and_bean + hei2015c3_totalfruit + 
        hei2015c4_wholefruit + hei2015c5_wholegrain + hei2015c6_totaldairy + hei2015c7_totprot + hei2015c8_seaplant_prot + 
        hei2015c9_fattyacid + hei2015c10_sodium + hei2015c11_refinedgrain + hei2015c12_sfat + hei2015c13_addsug)
    if (varLabel) {
        indat <- expss::apply_labels(indat, hei2015_total_score = "total hei-2015 score", hei2015c1_totalveg = "hei-2015 component 1 total vegetables", 
            hei2015c2_green_and_bean = "hei-2015 component 2 greens and beans", hei2015c3_totalfruit = "hei-2015 component 3 total fruit", 
            hei2015c4_wholefruit = "hei-2015 component 4 whole fruit", hei2015c5_wholegrain = "hei-2015 component 5 whole grains", 
            hei2015c6_totaldairy = "hei-2015 component 6 dairy", hei2015c7_totprot = "hei-2015 component 7 total protein foods", 
            hei2015c8_seaplant_prot = "hei-2015 component 8 seafood and plant protein", hei2015c9_fattyacid = "hei-2015 component 9 fatty acid ratio", 
            hei2015c10_sodium = "hei-2015 component 10 sodium", hei2015c11_refinedgrain = "hei-2015 component 11 refined grains", 
            hei2015c12_sfat = "hei-2015 component 12 sat fat", hei2015c13_addsug = "hei-2015 component 13 added sugar", 
            vegden = "density of total vegetables per 1000 kcal", grbnden = "density of dark green veg and beans per 1000 kcal", 
            frtden = "density of total fruit per 1000 kcal", whfrden = "density of whole fruit per 1000 kcal", 
            wgrnden = "density of whole grain per 1000 kcal", dairyden = "density of dairy per 1000 kcal", 
            protden = "density of total protein per 1000 kcal", seaplden = "density of seafood and plant protein per 1000 kcal", 
            faratio = "fatty acid ratio", sodden = "density of sodium per 1000 kcal", rgden = "density of refined grains per 1000 kcal", 
            sfat_perc = "percent of calories from sat fat", addsug_perc = "percent of calories from added sugar")
    }
    colnms <- c(join, "hei2015_total_score")
    if (energy) 
        colnms <- c(join, kcal, "hei2015_total_score")
    if (component) 
        colnms <- c(colnms, "hei2015c1_totalveg", "hei2015c2_green_and_bean", "hei2015c3_totalfruit", 
            "hei2015c4_wholefruit", "hei2015c5_wholegrain", "hei2015c6_totaldairy", "hei2015c7_totprot", 
            "hei2015c8_seaplant_prot", "hei2015c9_fattyacid", "hei2015c10_sodium", "hei2015c11_refinedgrain", 
            "hei2015c12_sfat", "hei2015c13_addsug")
    if (density) 
        colnms <- c(colnms, "vegden", "grbnden", "frtden", "whfrden", "wgrnden", "dairyden", "protden", 
            "seaplden", "faratio", "sodden", "rgden", "sfat_perc", "addsug_perc")
    indat[, colnms]
}
```

## `hei_2015_PerDay_pratio` [internal]

```r
function (seqn = NULL, years = 2009, day = "1", dietary = "tot", seed = NULL, varLabel = FALSE) 
{
    if (dietary == "iff") 
        join <- c("seqn", "line")
    else join <- "seqn"
    fped <- fped_read(years = years, day = day, dietary = dietary, cat = FALSE, version = 2015)
    tsv <- nhs_tsv(ifelse(day == "1", sprintf("drx%s|dr1%s", dietary, dietary), sprintf("drx%s|dr2%s", 
        dietary, dietary)), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "wtdr4yr", "wtdrd1", "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", 
        "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", 
        "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", 
        codebook = FALSE, varLabel = FALSE, cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    indat <- dplyr::inner_join(dt, fped, join)
    if (!is.null(seqn)) 
        indat <- indat[indat$seqn %in% seqn, ]
    indat <- wt_dr_day1(indat, wtname = "wtdr", cat = FALSE)
    demo <- nhs_read(nhs_tsv("demo", years = years, cat = FALSE), "sdmvstra", "sdmvpsu", cat = FALSE, 
        Year = FALSE)
    indat <- dplyr::inner_join(indat, demo, "seqn")
    choice <- c("kcal", "vtotalleg", "vdrkgrleg", "f_total", "f_whole", "g_whole", "d_total", "pfallprotleg", 
        "pfseaplantleg", "monopoly", "sfat", "sodi", "g_refined", "add_sugars")
    for (i in choice) attributes(indat[, i]) <- NULL
    indat1 <- reshape2::melt(indat[, c(join, choice)], id.vars = join)
    one <- dplyr::inner_join(indat[, c(join, choice, "sdmvstra", "sdmvpsu", "wtdr")], indat1, join)
    head(one)
    for (i in choice) one[, i] <- ifelse(one$variable == i, 1, 0)
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = one)
    glm <- survey::svyglm(value ~ -1 + kcal + vtotalleg + vdrkgrleg + f_total + f_whole + g_whole + d_total + 
        pfallprotleg + pfseaplantleg + monopoly + sfat + sodi + g_refined + add_sugars, design = dg)
    sigma <- glm$cov.unscaled
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = indat)
    mean <- survey::svymean(~kcal + vtotalleg + vdrkgrleg + f_total + f_whole + g_whole + d_total + pfallprotleg + 
        pfseaplantleg + monopoly + sfat + sodi + g_refined + add_sugars, dg)
    mu <- as.data.frame(mean)[, 1]
    if (!is.null(seed)) 
        set.seed(seed)
    sim_data <- as.data.frame(mvtnorm::rmvnorm(n = 10000, mean = mu, sigma = sigma))
    colnames(sim_data) <- colnames(sigma)
    aftermac <- hei_2015(indat = sim_data, kcal = "kcal", vtotalleg = "vtotalleg", vdrkgrleg = "vdrkgrleg", 
        f_total = "f_total", fwholefrt = "f_whole", g_whole = "g_whole", d_total = "d_total", pfallprotleg = "pfallprotleg", 
        pfseaplantleg = "pfseaplantleg", monopoly = "monopoly", satfat = "sfat", sodium = "sodi", g_refined = "g_refined", 
        add_sugars = "add_sugars", varLabel = FALSE, energy = FALSE, component = TRUE, density = FALSE, 
        join = NULL)
    head(aftermac)
    data.frame(min = sapply(aftermac, min), max = sapply(aftermac, max), mean = sapply(aftermac, mean), 
        sd = sapply(aftermac, sd), lowci = sapply(aftermac, function(i) quantile(i, 0.025000000000000001)), 
        upci = sapply(aftermac, function(i) quantile(i, 0.97499999999999998)))
}
```

## `hei_2015_PerDay_ssum` [internal]

```r
function (years, day, dietary, varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, version = 2015) 
{
    if (dietary == "iff") 
        join <- c("seqn", "food.code")
    else join <- "seqn"
    fped <- fped_read(years = years, day = day, dietary = dietary, version = 2015)
    tsv <- nhs_tsv(ifelse(day == "1", sprintf("drx%s|dr1%s", dietary, dietary), sprintf("drx%s|dr2%s", 
        dietary, dietary)), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodium", "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$line <- NULL
    dt$dr1mc <- NULL
    dt$monopoly <- dt$mfat + dt$pfat
    dt <- group_sum(dt, c("kcal", "sfat", "sodium", "mfat", "pfat", "monopoly"), set::and(c("Year", "seqn", 
        "food.code"), colnames(dt)))
    indat <- dplyr::inner_join(dt, fped, join)
    hei_2015(indat = indat, kcal = "kcal", vtotalleg = "vtotalleg", vdrkgrleg = "vdrkgrleg", f_total = "f_total", 
        fwholefrt = "f_whole", g_whole = "g_whole", d_total = "d_total", pfallprotleg = "pfallprotleg", 
        pfseaplantleg = "pfseaplantleg", monopoly = "monopoly", satfat = "sfat", sodium = "sodium", g_refined = "g_refined", 
        add_sugars = "add_sugars", varLabel = varLabel, energy = energy, component = component, density = density, 
        join = join)
}
```

## `hei_2015_PerPerson_pratio` [internal]

```r
function (seqn = seqn, years = years, dietary = dietary, seed = NULL) 
{
    if (dietary == "iff") 
        join <- c("seqn", "line")
    else join <- "seqn"
    fped <- fped_read(years = years, day = "1", dietary = dietary, version = 2015)
    tsv <- nhs_tsv(sprintf("drx%s|dr1%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "wtdr4yr", "wtdrd1", "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", 
        "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", 
        "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", 
        codebook = FALSE, varLabel = FALSE, cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    indat1 <- dplyr::inner_join(dt, fped, join)
    fped <- fped_read(years = years, day = "2", dietary = dietary, version = 2015)
    tsv <- nhs_tsv(sprintf("drx%s|dr2%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE, Year = FALSE)
    dt$monopoly <- dt$mfat + dt$pfat
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    indat2 <- dplyr::inner_join(dt, fped, join)
    indat <- dplyr::inner_join(indat1, indat2, join)
    indat <- wt_dr_day1(indat, wtname = "wtdr", cat = FALSE)
    choice <- choice <- do::knife_right(colnames(indat)[do::right(colnames(indat), 2) == ".x"], 2)
    for (i in 1:length(choice)) {
        which <- which(colnames(indat) %in% paste0(choice[i], c(".x", ".y")))
        indat$last <- row.sums(indat[, which])
        indat <- indat[, -which]
        colnames(indat)[ncol(indat)] <- choice[i]
    }
    demo <- nhs_read(nhs_tsv("demo", years = years, cat = FALSE), "sdmvstra", "sdmvpsu", cat = FALSE, 
        Year = FALSE)
    indat <- dplyr::inner_join(indat, demo, "seqn")
    choice <- c("kcal", "vtotalleg", "vdrkgrleg", "f_total", "f_whole", "g_whole", "d_total", "pfallprotleg", 
        "pfseaplantleg", "monopoly", "sfat", "sodi", "g_refined", "add_sugars")
    for (i in choice) attributes(indat[, i]) <- NULL
    indat1 <- reshape2::melt(indat[, c(join, choice)], id.vars = join)
    one <- dplyr::inner_join(indat[, c(join, choice, "sdmvstra", "sdmvpsu", "wtdr")], indat1, join)
    head(one)
    for (i in choice) one[, i] <- ifelse(one$variable == i, 1, 0)
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = one)
    glm <- survey::svyglm(value ~ -1 + kcal + vtotalleg + vdrkgrleg + f_total + f_whole + g_whole + d_total + 
        pfallprotleg + pfseaplantleg + monopoly + sfat + sodi + g_refined + add_sugars, design = dg)
    sigma <- glm$cov.unscaled
    dg <- survey::svydesign(id = ~sdmvpsu, weights = ~wtdr, strata = ~sdmvstra, nest = TRUE, data = indat)
    mean <- survey::svymean(~kcal + vtotalleg + vdrkgrleg + f_total + f_whole + g_whole + d_total + pfallprotleg + 
        pfseaplantleg + monopoly + sfat + sodi + g_refined + add_sugars, dg)
    mu <- as.data.frame(mean)[, 1]
    if (!is.null(seed)) 
        set.seed(seed)
    sim_data <- as.data.frame(mvtnorm::rmvnorm(n = 10000, mean = mu, sigma = sigma))
    colnames(sim_data) <- colnames(sigma)
    aftermac <- hei_2015(indat = sim_data, kcal = "kcal", vtotalleg = "vtotalleg", vdrkgrleg = "vdrkgrleg", 
        f_total = "f_total", fwholefrt = "f_whole", g_whole = "g_whole", d_total = "d_total", pfallprotleg = "pfallprotleg", 
        pfseaplantleg = "pfseaplantleg", monopoly = "monopoly", satfat = "sfat", sodium = "sodi", g_refined = "g_refined", 
        add_sugars = "add_sugars", varLabel = FALSE, energy = FALSE, component = TRUE, density = FALSE, 
        join = NULL)
    head(aftermac)
    data.frame(min = sapply(aftermac, min), max = sapply(aftermac, max), mean = sapply(aftermac, mean), 
        sd = sapply(aftermac, sd), lowci = sapply(aftermac, function(i) quantile(i, 0.025000000000000001)), 
        upci = sapply(aftermac, function(i) quantile(i, 0.97499999999999998)))
}
```

## `hei_2015_PerPerson_ssum` [internal]

```r
function (years, dietary = "tot", varLabel = FALSE, energy = TRUE, component = TRUE, density = FALSE, 
    both2days = F) 
{
    if (dietary == "iff") 
        join <- c("seqn", "food.code")
    else join <- "seqn"
    fped <- fped_read(years = years, day = "1", dietary = dietary, version = 2015)
    tsv <- nhs_tsv(sprintf("drx%s|dr1%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE)
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    dt$monopoly <- dt$mfat + dt$pfat
    indat1 <- dplyr::inner_join(dt, fped, join)
    fped <- fped_read(years = years, day = "2", dietary = dietary, version = 2015)
    tsv <- nhs_tsv(sprintf("drx%s|dr2%s", dietary, dietary), years = years, cat = FALSE)
    dt <- nhs_read(tsv, "drxtkcal,drxikcal,dr1tkcal,dr1ikcal,dr2tkcal,dr2ikcal:kcal", "drxtsfat,drxisfat,dr1tsfat,dr1isfat,dr2tsfat,dr2isfat:sfat", 
        "drdtsodi,drdisodi,dr1tsodi,dr1isodi,dr2tsodi,dr2isodi:sodi", "drxtmfat,drximfat,dr1tmfat,dr1imfat,dr2tmfat,dr2imfat:mfat", 
        "drxtpfat,drxipfat,dr1tpfat,dr1ipfat,dr2tpfat,dr2ipfat:pfat", codebook = FALSE, varLabel = FALSE, 
        cat = FALSE, Year = FALSE)
    dt$monopoly <- dt$mfat + dt$pfat
    colnames(dt) <- rename_line(colnames(dt))
    colnames(dt) <- rename_fdcd(colnames(dt))
    dt <- drop_col(dt, "fdcd")
    indat2 <- dplyr::inner_join(dt, fped, join)
    indat <- dplyr::full_join(indat1, indat2, join)
    choice <- do::knife_right(colnames(indat)[do::right(colnames(indat), 2) == ".x"], 2)
    for (i in 1:length(choice)) {
        which <- which(colnames(indat) %in% paste0(choice[i], c(".x", ".y")))
        indat$last <- row.means(indat[, which], na.rm = !both2days)
        indat <- indat[, -which]
        colnames(indat)[ncol(indat)] <- choice[i]
    }
    hei_2015(indat = indat, kcal = "kcal", vtotalleg = "vtotalleg", vdrkgrleg = "vdrkgrleg", f_total = "f_total", 
        fwholefrt = "f_whole", g_whole = "g_whole", d_total = "d_total", pfallprotleg = "pfallprotleg", 
        pfseaplantleg = "pfseaplantleg", monopoly = "monopoly", satfat = "sfat", sodium = "sodi", g_refined = "g_refined", 
        add_sugars = "add_sugars", varLabel = varLabel, energy = energy, component = component, density = density, 
        join = join)
}
```

## `highlight` [exported]

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

## `histgram_range` [internal]

```r
function (x, bins) 
{
    x <- x[!is.na(x)]
    x_range <- range(x)
    width <- (x_range[2] - x_range[1])/(bins - 1)
    boundary <- width/2
    shift <- floor((x_range[1] - boundary)/width)
    origin <- boundary + shift * width
    max_x <- x_range[2] + (1 - 1e-08) * width
    breaks <- seq(origin, max_x, width)
    range(table(cut(x = x, breaks = breaks, right = TRUE, include.lowest = TRUE)))
}
```

## `html_URL` [exported]

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

## `html_space` [internal]

```r
function (n = 1) 
{
    paste0(rep("&nbsp;", n), collapse = "")
}
```

## `html_table` [internal]

```r
function (df, ..., caption = NULL, header = 1, headtop = 0, bodytop = 0, headspan.list = NULL, foot = "") 
{
    at <- rlang::list2(...)
    at <- at[!sapply(at, is.null)]
    title <- ""
    if (!is.null(caption)) 
        title <- sprintf("<caption  style=\"position:sticky;top:0px;background-color: #cdf3e5;\">%s</caption>", 
            caption)
    (head <- matrix(colnames(df), nrow = 1, dimnames = list(NULL, colnames(df))))
    if (header[1] > 1) {
        head <- rbind(head, df[1:(header[1] - 1), ])
        df <- df[-(1:(header - 1)), ]
    }
    for (i in 1:nrow(head)) {
        head[i, ] <- sprintf("<th style=\"outline: 1.5px solid #a8a3a3;outline-offset:-1px\">%s</th>", 
            head[i, ])
    }
    if ("headspan" %in% names(at) | !is.null(headspan.list)) {
        hl <- list()
        if ("headspan" %in% names(at)) {
            (wh <- which(names(at) %in% "headspan"))
            hl <- at[wh]
        }
        if (!is.null(headspan.list)) 
            hl <- c(hl, headspan.list)
        for (i in 1:length(hl)) {
            (ati <- hl[[i]])
            if (ati[1] == 1) {
                ati <- ati[-1]
                if (ati[3] > ati[2]) {
                  head[ati[1], ati[2]] <- sub("<th ", sprintf("<th align=\"center\" colspan=\"%s\" style=\"outline: 1.5px solid #a8a3a3;outline-offset:-1px\"", 
                    ati[3] - ati[2] + 1), head[ati[1], ati[2]])
                  head[ati[1], (ati[2] + 1):ati[3]] <- ""
                }
            }
            else if (ati[1] == 2) {
                ati <- ati[-1]
                if (ati[3] > ati[2]) {
                  head[ati[2], ati[1]] <- sub("<th ", sprintf("<th align=\"center\" rowspan=\"%s\"", 
                    ati[3] - ati[2] + 1), head[ati[2], ati[1]])
                  head[(ati[2] + 1):ati[3], ati[1]] <- ""
                }
            }
            else {
                stop("span<U+7B2C><U+4E00><U+4E2A><U+4F4D><U+7F6E><U+5FC5><U+987B><U+662F>1<U+6216><U+8005>2")
            }
        }
    }
    if (nrow(df) <= ncol(df)) {
        for (i in 1:nrow(df)) {
            df[i, ] <- sprintf("<td style=\"border:1px solid #addaea\">%s</td>", df[i, ])
        }
    }
    else {
        for (i in 1:ncol(df)) {
            df[, i] <- sprintf("<td style=\"border:1px solid #addaea\">%s</td>", df[, i])
        }
    }
    if ("span" %in% names(at)) {
        wh <- which(names(at) %in% "span")
        for (i in wh) {
            ati <- at[[i]]
            if (is.list(ati)) {
                atl <- ati
                for (j in 1:length(atl)) {
                  ati <- atl[[j]]
                  if (ati[1] == 1) {
                    ati <- ati[-1]
                    if (ati[3] > ati[2]) {
                      df[ati[1], ati[2]] <- sub("<td ", sprintf("<td align=\"center\" colspan=\"%s\"", 
                        ati[3] - ati[2] + 1), df[ati[1], ati[2]])
                      df[ati[1], (ati[2] + 1):ati[3]] <- ""
                    }
                  }
                  else if (ati[1] == 2) {
                    ati <- ati[-1]
                    if (ati[3] > ati[2]) {
                      df[ati[2], ati[1]] <- sub("<td ", sprintf("<td align=\"center\" rowspan=\"%s\"", 
                        ati[3] - ati[2] + 1), df[ati[2], ati[1]])
                      df[(ati[2] + 1):ati[3], ati[1]] <- ""
                    }
                  }
                  else {
                    stop("span<U+7B2C><U+4E00><U+4E2A><U+4F4D><U+7F6E><U+5FC5><U+987B><U+662F>1<U+6216><U+8005>2")
                  }
                }
            }
            else {
                if (ati[1] == 1) {
                  ati <- ati[-1]
                  if (ati[3] > ati[2]) {
                    df[ati[1], ati[2]] <- sub("<td ", sprintf("<td align=\"center\" colspan=\"%s\"", 
                      ati[3] - ati[2] + 1), df[ati[1], ati[2]])
                    df[ati[1], (ati[2] + 1):ati[3]] <- ""
                  }
                }
                else if (ati[1] == 2) {
                  ati <- ati[-1]
                  if (ati[3] > ati[2]) {
                    df[ati[2], ati[1]] <- sub("<td ", sprintf("<td align=\"center\" rowspan=\"%s\"", 
                      ati[3] - ati[2] + 1), df[ati[2], ati[1]])
                    df[(ati[2] + 1):ati[3], ati[1]] <- ""
                  }
                }
                else {
                  stop("span<U+7B2C><U+4E00><U+4E2A><U+4F4D><U+7F6E><U+5FC5><U+987B><U+662F>1<U+6216><U+8005>2")
                }
            }
        }
    }
    head <- apply(cbind("<tr style=\"\">", head, "</tr>"), 1, paste, collapse = "") %>% paste0(collapse = "\n")
    body <- apply(cbind("<tr>", df, "</tr>"), 1, paste, collapse = "") %>% paste0(collapse = "\n")
    sprintf("<table style=\"border-collapse:collapse;background-color: #edf0f4\">\n            %s\n            <thead style=\"position:sticky;top:%spx;background-color: #f9e1e1;border:none;z-index:2;\">\n                %s\n            </thead>\n            <tbody style=\"position: relative;top: %spx;z-index:1;\">\n                %s\n            </tbody>\n            <div style=\"display: none;\">powered by zhangjing, wechat:Charlszhanggo</div>\n        </table>\n            <div>%s</div>", 
        title, ifelse(nchar(title) == 0, 0 + headtop, 20 + headtop), head, bodytop, body, foot) %>% HTML() %>% 
        browsable()
}
```

## `icd10_search` [internal]

```r
function (..., years) 
{
    h0 <- c(...)
    rxq_rx_tsv <- nhs_tsv("rxq_rx", cat = FALSE)
    d <- nhs_read(rxq_rx_tsv, "rxdrsc1", "rxdrsc2", "rxdrsc3", "rxdrsd1", "rxdrsd2", "rxdrsd3", cat = FALSE)
    c1 <- d[nchar(d$rxdrsd1) > 0, c("rxdrsc1", "rxdrsd1")]
    col_rename(c1) <- c("rxdrsc1:code", "rxdrsd1:description")
    c2 <- d[nchar(d$rxdrsd2) > 0, c("rxdrsc2", "rxdrsd2")]
    col_rename(c2) <- c("rxdrsc2:code", "rxdrsd2:description")
    c3 <- d[nchar(d$rxdrsd3) > 0, c("rxdrsc3", "rxdrsd3")]
    col_rename(c3) <- c("rxdrsc3:code", "rxdrsd3:description")
    cd10 <- unique(rbind(c1, c2, c3))
    nhs_view(cd10, h0)
}
```

## `ifel` [exported]

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

## `inf2NA` [internal]

```r
function (x) 
{
    if (is.data.frame(x)) {
        for (i in 1:ncol(x)) {
            ck <- is.infinite(x[, i]) | is.na(x[, i]) | x[, i] %in% ".._..NA.._.."
            x[ck, i] <- NA
        }
    }
    else {
        ck <- is.infinite(x)
        x[ck] <- NA
    }
    x
}
```

## `inset_both_frame` [exported]

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

## `inset_both_square` [exported]

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

## `inset_exact_match` [exported]

```r
function () 
{
    rstudioapi::insertText(text = " %=% ")
}
```

## `inset_left_frame` [exported]

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

## `inset_left_square` [exported]

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

## `inset_right_frame` [exported]

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

## `inset_right_square` [exported]

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

## `interi` [internal]

```r
function (fit) 
{
    (allterms <- set::grep_and(attr(fit[["terms"]], "term.labels"), ":"))
    (v1 <- strsplit(allterms, ":")[[1]][[1]])
    (v2 <- strsplit(allterms, ":")[[1]][[2]])
    (factor.list <- c(fit$xlevels, fit$Design$parms))
    (factor.var <- names(factor.list))
    expit <- ifelse(regType(fit) == "lm", F, T)
    if (v1 %in% factor.var) {
        (v1c <- c(paste0(v1, "=", factor.list[[v1]]), paste0(v1, factor.list[[v1]])))
        if (expit) 
            (OR10 <- exp(sum(fit$coefficients[v1c], na.rm = T)))
        if (!expit) 
            (OR10 <- sum(fit$coefficients[v1c], na.rm = T))
    }
    else {
        v1c <- v1
        if (expit) 
            (OR10 <- exp(fit$coefficients[v1]))
        if (!expit) 
            (OR10 <- fit$coefficients[v1])
    }
    if (v2 %in% factor.var) {
        (v2c <- c(paste0(v2, "=", factor.list[[v2]]), paste0(v2, factor.list[[v2]])))
        if (expit) 
            (OR01 <- exp(sum(fit$coefficients[v2c], na.rm = T)))
        if (!expit) 
            (OR01 <- sum(fit$coefficients[v2c], na.rm = T))
    }
    else {
        v2c <- v2
        if (expit) 
            (OR01 <- exp(fit$coefficients[v2]))
        if (!expit) 
            (OR01 <- fit$coefficients[v2])
    }
    (vc <- unlist(lapply(v1c, function(i) c(paste0(i, ":", v2c), paste(i, "*", v2c)))))
    if (expit) 
        (OR11 <- exp(sum(fit$coefficients[vc], na.rm = T)))
    if (!expit) 
        (OR11 <- sum(fit$coefficients[vc], na.rm = T))
    (RERI <- OR11 - OR10 - OR01 + 1)
    (AP <- RERI/OR11)
    (S <- (OR11 - 1)/(OR10 + OR01 - 2))
    data.frame(RERI, AP, S, row.names = NULL)
}
```

## `intersection` [internal]

```r
function (fit, round, boot = 2000, seed = NULL) 
{
    data <- model.data(fit)
    set.seed(seed)
    bootn <- lapply(1:boot, function(i) sample(1:nrow(data), nrow(data), T))
    pb <- txtProgressBar(max = boot, style = 3, width = 25)
    res <- do.call(lapply(1:length(bootn), function(i) {
        setTxtProgressBar(pb, i)
        if (grepl("svy", fit$call[[1]])) {
            ck <- (1:nrow(fit$survey.design$variables)) %in% bootn[[i]]
            interi(update(fit, design = subset(fit$survey.design, ck)))
        }
        else {
            interi(update(fit, data = data[bootn[[i]], ]))
        }
    }), what = rbind)
    cat("\n")
    mean <- sapply(res, mean)
    lower.95CI <- sapply(res, function(i) quantile(i, probs = 0.025000000000000001))
    upper.95CI <- sapply(res, function(i) quantile(i, probs = 1 - 0.025000000000000001))
    data.frame(mean, lower.95CI, upper.95CI)
}
```

## `ip_analysis` [exported]

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

## `label2varLabel` [internal]

```r
function () 
{
    label <- nhs_files_pc(file_ext = "label")
    if (length(label) > 0) {
        varLabel <- do::Replace(label, "\\.label", ".varLabel")
        ck <- file.rename(label, varLabel)
    }
}
```

## `label_table` [internal]

```r
function (div) 
{
    variable <- tolower(rvest::html_text(rvest::html_elements(div, xpath = "dl/dd[1]")))
    label <- as.data.frame(listn(rvest::html_table(rvest::html_elements(div, xpath = "table"))))
    cbind(variable, label)
}
```

## `leg2010a` [internal]

```r
function (indat, kcal, allmeat, seaplant, v_total, v_drkgr, legumes) 
{
    indat$mbmax = 2.5 * (indat[, kcal]/1000)
    ck1 <- indat[, allmeat] < indat[, "mbmax"]
    indat[ck1, "meatleg"] <- indat[ck1, legumes] * 4
    indat[ck1, "needmeat"] <- indat[ck1, "mbmax"] - indat[ck1, allmeat]
    ck2 <- indat[, "meatleg"] <= indat[, "needmeat"]
    ck12 <- ck1 & ck2
    indat$legtype[ck12] <- "allmeat"
    indat$legume_added_allmeat[ck12] <- indat[ck12, allmeat] + indat[ck12, "meatleg"]
    indat$legume_added_seaplant[ck12] <- indat[ck12, seaplant] + indat[ck12, "meatleg"]
    indat$legume_added_v_total[ck12] <- indat[ck12, v_total]
    indat$legume_added_beangrn[ck12] <- indat[ck12, v_drkgr]
    ck1n2 <- ck1 & !ck2
    indat$legtype[ck1n2] <- "meat/veg"
    indat$extrmeat[ck1n2] <- indat[ck1n2, "meatleg"] - indat[ck1n2, "needmeat"]
    indat$extrleg[ck1n2] <- indat[ck1n2, "extrmeat"]/4
    indat$legume_added_allmeat[ck1n2] <- indat[ck1n2, allmeat] + indat[ck1n2, "needmeat"]
    indat$legume_added_seaplant[ck1n2] <- indat[ck1n2, "seaplant"] + indat[ck1n2, "needmeat"]
    indat$legume_added_v_total[ck1n2] <- indat[ck1n2, v_total] + indat[ck1n2, "extrleg"]
    indat$legume_added_beangrn[ck1n2] <- indat[ck1n2, v_drkgr] + indat[ck1n2, "extrleg"]
    ckn1 <- !ck1
    indat$legtype[ckn1] <- "allveg"
    indat$legume_added_allmeat[ckn1] <- indat[ckn1, allmeat]
    indat$legume_added_seaplant[ckn1] <- indat[ckn1, "seaplant"]
    indat$legume_added_v_total[ckn1] <- indat[ckn1, v_total] + indat[ckn1, legumes]
    indat$legume_added_beangrn[ckn1] <- indat[ckn1, v_drkgr] + indat[ckn1, legumes]
    indat
}
```

## `listn` [internal]

```r
function (x, n = 1) 
{
    x[[n]]
}
```

## `live_microbes_table` [exported]

```r
function () 
{
    intake_of_live_microbes
}
```

## `look` [exported]

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

## `looki` [internal]

```r
function (x, ..., ignore.case = FALSE, NA2false = FALSE) 
{
    lookup <- c(...)
    lookup <- do::Trim_left(lookup)
    kk <- do::left(lookup, 1)
    (k1 <- (kk == "~") | (!kk %in% c("!", "=")))
    (k3 <- kk %in% c("="))
    kk <- do::left(lookup, 2)
    (k2 <- kk == "!~")
    (k4 <- kk == "!=")
    if (!any(k1) & !any(k2) & !any(k3) & !any(k4)) 
        stop("no select rules")
    if (any(k1) & any(k3)) {
        (k1 <- do::Replace0(lookup[k1], "~"))
        k1 <- gsub(" {0,}\\| {0,}", "|", k1)
        k1g <- equal(row.sums(data.frame(lapply(k1, function(i) stringi::stri_detect_regex(x, i, case_insensitive = ignore.case)))), 
            length(k1))
        (k3 <- do::Replace0(lookup[k3], "="))
        k3 <- gsub(" {0,}\\| {0,}", "|", k3)
        if (ignore.case) {
            k3g <- equal(row.sums(data.frame(lapply(k3, function(i) tolower(x) %in% unique(unlist(strsplit(tolower(i), 
                "\\|")))))), length(k3))
        }
        else {
            k3g <- equal(row.sums(data.frame(lapply(k3, function(i) x %in% unique(unlist(strsplit(i, 
                "\\|")))))), length(k3))
        }
        k13 <- k1g | k3g
    }
    else if (any(k1) & !any(k3)) {
        (k1 <- do::Replace0(lookup[k1], "~"))
        k1 <- gsub(" {0,}\\| {0,}", "|", k1)
        k1g <- equal(row.sums(data.frame(lapply(k1, function(i) stringi::stri_detect_regex(x, i, case_insensitive = ignore.case)))), 
            length(k1))
        k13 <- k1g
    }
    else if (!any(k1) & any(k3)) {
        (k3 <- do::Replace0(lookup[k3], "="))
        k3 <- gsub(" {0,}\\| {0,}", "|", k3)
        if (ignore.case) {
            k3g <- equal(row.sums(data.frame(lapply(k3, function(i) tolower(x) %in% unique(unlist(strsplit(tolower(i), 
                "\\|")))))), length(k3))
        }
        else {
            k3g <- equal(row.sums(data.frame(lapply(k3, function(i) x %in% unique(unlist(strsplit(i, 
                "\\|")))))), length(k3))
        }
        k13 <- k3g
    }
    else {
        k13 <- rep(TRUE, length(x))
    }
    if (any(k2) & any(k4)) {
        (k2 <- do::Replace0(lookup[k2], "!~"))
        k2 <- gsub(" {0,}\\| {0,}", "|", k2)
        k2g <- equal(row.sums(data.frame(lapply(k2, function(i) stringi::stri_detect_regex(x, i, case_insensitive = ignore.case)))), 
            length(k2))
        (k4 <- do::Replace0(lookup[k4], "!="))
        k4 <- unique(unlist(strsplit(k4, "\\|")))
        if (ignore.case) {
            k4g <- equal(row.sums(data.frame(lapply(k4, function(i) tolower(x) %in% unique(unlist(strsplit(tolower(i), 
                "\\|")))))), length(k4))
        }
        else {
            k4g <- equal(row.sums(data.frame(lapply(k4, function(i) x %in% unique(unlist(strsplit(i, 
                "\\|")))))), length(k4))
        }
        k24 <- k2g | k4g
    }
    else if (any(k2) & !any(k4)) {
        (k2 <- do::Replace0(lookup[k2], "!~"))
        k2 <- gsub(" {0,}\\| {0,}", "|", k2)
        k2g <- equal(row.sums(data.frame(lapply(k2, function(i) stringi::stri_detect_regex(x, i, case_insensitive = ignore.case)))), 
            length(k2))
        k24 <- k2g
    }
    else if (!any(k2) & any(k4)) {
        (k4 <- do::Replace0(lookup[k4], "!="))
        k4 <- unique(unlist(strsplit(k4, "\\|")))
        if (ignore.case) {
            k4g <- equal(row.sums(data.frame(lapply(k4, function(i) tolower(x) %in% unique(unlist(strsplit(tolower(i), 
                "\\|")))))), length(k4))
        }
        else {
            k4g <- equal(row.sums(data.frame(lapply(k4, function(i) x %in% unique(unlist(strsplit(i, 
                "\\|")))))), length(k4))
        }
        k24 <- k4g
    }
    else {
        k24 <- rep(FALSE, length(x))
    }
    kg <- k13 & (!k24)
    if (NA2false) 
        kg[is.na(kg)] <- FALSE
    kg
}
```

## `lookl` [exported]

```r
function (x, ..., ignore.case = TRUE, NA2false = FALSE) 
{
    if (is.data.frame(x)) 
        x <- paste0_columns(x, ";")
    looki(x = x, ..., ignore.case = ignore.case, NA2false = NA2false)
}
```

## `matchit4design` [exported]

```r
function (design, matchit) 
{
    if ("matchit" %in% class(matchit)) 
        matchit <- MatchIt::match.data(matchit)
    ck <- (1:nrow(nhs)) %in% matchit$xrxoxwnxuxbxmxexr
    subset(design, ck)
}
```

## `mdb_files` [exported]

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

## `mean_by` [internal]

```r
function (data, x, by) 
{
    if (length(x) == 1) {
        string <- sprintf("aggregate(data[,x],by=list(%s),mean,na.rm=TRUE)", paste0(sprintf("data[,'%s']", 
            by), collapse = ","))
        r <- eval(parse(text = string))
        colnames(r)[1:length(by)] <- by
        colnames(r)[ncol(r)] <- x
        return(r)
    }
    else {
        for (i in 1:length(x)) {
            if (i == 1) {
                r1 <- mean_by(data, x[i], by)
            }
            else {
                r2 <- mean_by(data, x = x[i], by)
                r1 <- dplyr::full_join(r1, r2, by)
            }
        }
        return(r1)
    }
}
```

## `miss` [internal]

```r
function (x = 1) 
{
    ck <- tryCatch(list(x), error = function(e) "e", warning = function(w) "w")
    ck %in% "e"
}
```

## `missForest2` [exported]

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

## `missValue` [exported]

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

## `mort_codebook` [internal]

```r
function () 
{
    variable <- c("eligstat", "eligstat", "eligstat", "mortstat", "mortstat", "ucod_leading", "ucod_leading", 
        "ucod_leading", "ucod_leading", "ucod_leading", "ucod_leading", "ucod_leading", "ucod_leading", 
        "ucod_leading", "ucod_leading", "diabetes", "diabetes", "hyperten", "hyperten")
    id <- c(1L, 1L, 1L, 2L, 2L, 3L, 3L, 3L, 3L, 3L, 3L, 3L, 3L, 3L, 3L, 4L, 4L, 5L, 5L)
    code <- c("1", "2", "3", "0", "1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0", "1", "0", 
        "1")
    label <- c("Eligible", "Under age 18, not available for public release", "Ineligible", "Assumed alive", 
        "Assumed deceased", "Diseases of heart (I00-I09, I11, I13, I20-I51)", "Malignant neoplasms (C00-C97)", 
        "Chronic lower respiratory diseases (J40-J47)", "Accidents (unintentional injuries) (V01-X59, Y85-Y86)", 
        "Cerebrovascular diseases (I60-I69)", "Alzheimer's disease (G30)", "Diabetes mellitus (E10-E14)", 
        "Influenza and pneumonia (J09-J18)", "Nephritis, nephrotic syndrome and nephrosis (N00-N07, N17-N19, N25-N27)", 
        "All other causes (residual)", "No - Condition not listed as a multiple cause of death", "Yes - Condition listed as a multiple cause of death", 
        "No - Condition not listed as a multiple cause of death", "Yes - Condition listed as a multiple cause of death")
    df <- data.frame(id, variable, code, label)
    file = paste0(get_mort_path(), "mortality.codebook")
    write.table(df, file, sep = "\t", row.names = FALSE)
}
```

## `mort_download` [exported]

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

## `mort_read` [exported]

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

## `mort_varLabel` [internal]

```r
function () 
{
    variable <- c("eligstat", "mortstat", "ucod_leading", "diabetes", "hyperten", "permth_int", "permth_exm")
    label <- c("Eligibility Status for Mortality Follow-up", "Final Mortality Status", "Underlying Cause of Death: Recode", 
        "Diabetes Flag from Multiple Cause of Death (MCOD)", "Hypertension Flag from Multiple Cause of Death (MCOD)", 
        "Number of Person Months of Follow-up from NHANES interview date", "Number of Person Months of Follow-up from NHANES Mobile Examination Center (MEC) date")
    df <- data.frame(variable, label)
    file = paste0(get_mort_path(), "mortality.varLabel")
    write.table(df, file, sep = "\t", row.names = FALSE)
}
```

## `multibyteString` [exported]

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

## `nchar_max` [internal]

```r
function (x) 
{
    x[which.max(nchar(x))]
}
```

## `newVb` [exported]

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

## `nhanesR_startup_check` [exported]

```r
function () 
{
    cat("Not check: options(nhanesR_check=FALSE)")
}
```

## `odd` [internal]

```r
function (x) 
{
    x[seq(1, length(x), 2)]
}
```

## `oddl` [internal]

```r
function (x) 
{
    x <- rep(FALSE, length(x))
    x[seq(1, length(x), 2)] <- TRUE
    x
}
```

## `optimal_nKnots` [exported]

```r
function (fit, n = 3:8, by = NULL, plot = TRUE, title = NULL, data = NULL, cat = F) 
UseMethod("optimal_nKnots")
```

## `order_fit` [internal]

```r
function (fs) 
{
    for (i in 1:length(fs)) {
        if (class(fs[[i]])[1] == "svytableone") {
            fs[[i]] <- attr(fs[[i]], "fit")
        }
    }
    fs.x <- lapply(fs, do::model.x)
    (fs.x.length <- sapply(fs.x, length))
    (x1 <- which(sapply(fs.x, function(i) length(i) == 1)))
    ck <- all(sapply(1:length(x1), function(i) {
        if (length(x1) == 1) {
            all(diff(fs.x.length[1:length(fs.x)]) > 0)
        } else {
            if (i < length(x1)) {
                ck1 <- all(diff(fs.x.length[x1[i]:(x1[i + 1] - 1)]) > 0)
                x1i <- fs.x[x1[i]][1][[1]]
                ck2 <- all(sapply(fs.x[x1[i]:(x1[i + 1] - 1)], function(i) x1i %in% i))
                ck1 & ck2
            } else {
                ck1 <- all(diff(fs.x.length[x1[i]:length(fs.x)]) > 0)
                x1i <- fs.x[x1[i]][1][[1]]
                ck2 <- all(sapply(fs.x[x1[i]:length(fs.x)], function(i) x1i %in% i))
                ck1 & ck2
            }
        }
    }))
    fs.y <- sapply(fs, function(i) paste0(do::model.y(i), collapse = ",  "))
    fs.data <- sapply(fs, function(i) {
        if (grepl("svy", class(i)[1])) {
            do::Replace0(do::Replace0(do::Replace(paste0(deparse(i$call$design), collapse = ""), " {2,}", 
                " "), "\""), "'")
        }
        else {
            do::Replace0(do::Replace0(do::Replace(paste0(deparse(i$call$data), collapse = ""), " {2,}", 
                " "), "\""), "'")
        }
    })
    x1 <- sapply(fs.x, function(i) if (length(i) == 1) 
        i
    else NA)
    x1 <- unique(x1[!is.na(x1)])
    r <- lapply(1:length(x1), function(i) {
        (xi <- x1[i])
        (ck.x <- sapply(fs.x, function(i) any(i %in% xi)))
        if (ck) {
            (order.0 <- paste0(fs.data[ck.x], "~~", fs.y[ck.x], "~~~", sapply(fs.x[ck.x], length)))
            fi <- fs[ck.x]
            up <- unique(do::Replace0(order.0, "~~~.*"))
            r <- lapply(up, function(j) {
                fi[do::Replace0(order.0, "~~~.*") == j]
            })
        }
        else {
            (order.0 <- paste0(fs.data[ck.x], "~~", fs.y[ck.x], "~~~", sapply(fs.x[ck.x], length)))
            fi <- fs[ck.x]
            up <- unique(do::Replace0(order.0, "~~~.*"))
            r <- lapply(up, function(j) {
                fi[do::Replace0(order.0, "~~~.*") == j]
            })
        }
        names(r) <- up
        r
    })
    names(r) <- x1
    r
}
```

## `p4interaction` [exported]

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

## `p4trend` [exported]

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

## `paste0_columns` [internal]

```r
function (df, collapse = ",") 
{
    if (ncol(df) == 1) {
        df[, 1]
    }
    else {
        apply(df, 1, paste0, collapse = collapse)
    }
}
```

## `paste1` [internal]

```r
function (x1, x2) 
{
    if (all(is.data.frame(x1), is.data.frame(x2))) {
        for (i in 1:ncol(x1)) {
            x1[, i] <- paste0(x1[, i], x2[, i])
        }
    }
    else if (all(is.atomic(x1), is.atomic(x2))) {
        x1 <- paste0(x1, x2)
    }
    else {
        if (!is.data.frame(x1)) {
            xa <- x2
            x2 <- x1
            x1 <- xa
        }
        for (i in 1:ncol(x1)) {
            x1[, i] <- paste0(x1[, i], x2)
        }
    }
    x1
}
```

## `paste_dataframe` [exported]

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

## `person_years` [exported]

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

## `prepare_items` [exported]

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

## `prepare_years` [exported]

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

## `prevalence_byYear` [exported]

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

## `qoute_n` [internal]

```r
function (x, pos = "left") 
{
    if (length(x) == 0) 
        return(0)
    if (pos == "left") {
        sum(strsplit(x, "")[[1]] == "(")
    }
    else {
        sum(strsplit(x, "")[[1]] == ")")
    }
}
```

## `quant` [exported]

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

## `quiet` [internal]

```r
function (x) 
{
    sink(tempfile())
    on.exit(sink())
    invisible(force(x))
}
```

## `rcsx` [internal]

```r
function (fit) 
{
    rcsx1 <- unique(do::Replace0(do::knife_left(names(fit$coefficients)[do::left(names(fit$coefficients), 
        4) == "rcs("], 4), "\\).*", ",.*"))
    rcsx2 <- tryCatch(unique(do::Replace0(names(fit$assign)[startsWith(names(fit$assign), "rcs")], " {0,}\\,.*", 
        " {0,}\\).*", "rcs\\(")), error = function(e) character())
    unique(c(rcsx1, rcsx2))
}
```

## `re_order` [exported]

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

## `regTermTest2` [internal]

```r
function (model, test.terms, null = NULL, df, method = c("Wald", "WorkingWald", "LRT"), lrt.approximation = "saddlepoint") 
{
    if (missing(df)) 
        df <- NULL
    method <- match.arg(method)
    canonicalOrder <- function(term) {
        tt <- strsplit(term, ":")
        tt <- lapply(tt, sort)
        sapply(tt, paste, collapse = ":")
    }
    if (inherits(test.terms, "formula")) {
        test_intercept <- explicit1(test.terms)
        test.terms <- attr(terms(test.terms), "term.labels")
    }
    else test_intercept <- FALSE
    okbeta <- !is.na(coef(model, na.rm = FALSE))
    tt <- attr(terms(model), "term.labels")
    aa <- attr(model.matrix(model), "assign")[okbeta]
    if ((inherits(model, "svyloglin") || inherits(model, "svyolr")) && attr(terms(model), "intercept")) {
        aa <- aa[-1]
    }
    index <- which(aa %in% match(canonicalOrder(test.terms), canonicalOrder(tt)))
    if (any(is.na(index))) {
        stop("Terms didn't match:", canonicalOrder(test.terms), canonicalOrder(tt))
    }
    if (test_intercept) {
        if (attr(terms(model), "intercept")) 
            index <- unique(c(1, index))
        else stop("model does not have an intercept")
    }
    beta <- coef(model)[index]
    if (!is.null(null)) 
        beta <- beta - null
    V <- vcov(model)[index, index]
    if (is.null(df)) {
        if (inherits(model, "svyglm")) 
            df <- ifelse(model$df.residual <= 0, degf(model$survey.design), model$df.residual)
        else if (inherits(model, "svycoxph")) 
            df <- ifelse(model$degf.resid <= 0, degf(model$survey.design), model$degf.resid)
        else if (inherits(model, "lm")) 
            df <- model$df.residual
        else if (inherits(model, "coxph")) 
            df <- model$n - length(coef(model))
        else if (inherits(model, "MIresult")) 
            df <- min(model$df[index])
        else if (inherits(model, "svyloglin")) 
            df <- model$df + 1 - length(index)
        else if (inherits(model, "svyolr")) 
            df <- model$df.residual
        else df <- length(resid(model)) - length(coef(model))
    }
    if (method %in% c("LRT", "WorkingWald")) {
        if (inherits(model, "svyglm")) 
            V0 <- model$naive.cov
        else if (inherits(model, "svycoxph")) 
            V0 <- model$inv.info
        else if (inherits(model, "lm")) 
            V0 <- vcov(model)
        else if (inherits(model, "coxph")) {
            if (is.null(model$naive.var)) 
                V0 <- model$var
            else V0 <- model$naive.var
        }
        else if (inherits(model, "svyolr")) {
            V0 <- solve(model$Hess)
        }
        else stop("method='LRT' not supported for this model")
        V0 <- V0[index, index]
        if (test_intercept) {
            test.formula <- make.formula(c(1, test.terms))[[2]]
        }
        else {
            test.formula <- make.formula(test.terms)[[2]]
        }
        if (!("formula" %in% names(model$call))) 
            names(model$call)[[2]] <- "formula"
        if (method == "LRT") {
            model0 <- eval(bquote(update(.(model), . ~ . - (.(test.formula)))), environment(formula(model)))
            chisq <- deviance(model0) - deviance(model)
        }
        else {
            chisq <- beta %*% solve(V0) %*% beta
        }
        misspec <- eigen(solve(V0) %*% V, only.values = TRUE)$values
        if (df == Inf) {
            p <- pchisqsum(chisq, rep(1, length(misspec)), misspec, method = lrt.approximation, lower.tail = FALSE)
        }
        else {
            p <- pFsum(chisq, rep(1, length(misspec)), misspec, ddf = 0, method = lrt.approximation, 
                lower.tail = FALSE)
        }
        rval <- list(call = sys.call(), mcall = model$call, chisq = chisq, df = length(index), test.terms = test.terms, 
            p = p, lambda = misspec, ddf = df)
        if (method == "LRT") 
            class(rval) <- "regTermTestLRT"
        else class(rval) <- "regTermTestWW"
        return(rval)
    }
    chisq <- beta %*% solve(V) %*% beta
    if (df < Inf) {
        Ftest <- chisq/length(index)
        rval <- list(call = sys.call(), mcall = model$call, Ftest = Ftest, df = length(index), ddf = df, 
            test.terms = test.terms, p = pf(Ftest, length(index), df, lower.tail = FALSE))
    }
    else {
        rval <- list(call = sys.call(), mcall = model$call, chisq = chisq, df = length(index), test.terms = test.terms, 
            p = pchisq(chisq, length(index), lower.tail = FALSE))
    }
    class(rval) <- "regTermTest"
    rval
}
```

## `regTermTest4svycoxph` [internal]

```r
function (model, test.terms, null = NULL, df, method = c("Wald", "WorkingWald", "LRT"), lrt.approximation = "saddlepoint") 
{
    if (missing(df)) 
        df <- NULL
    method <- match.arg(method)
    canonicalOrder <- function(term) {
        tt <- strsplit(term, ":")
        tt <- lapply(tt, sort)
        sapply(tt, paste, collapse = ":")
    }
    if (inherits(test.terms, "formula")) {
        test_intercept <- explicit1(test.terms)
        test.terms <- attr(terms(test.terms), "term.labels")
    }
    else test_intercept <- FALSE
    okbeta <- !is.na(coef(model, na.rm = FALSE))
    tt <- attr(terms(model), "term.labels")
    aa <- attr(model.matrix(model), "assign")[okbeta]
    if ((inherits(model, "svyloglin") || inherits(model, "svyolr")) && attr(terms(model), "intercept")) {
        aa <- aa[-1]
    }
    index <- which(aa %in% match(canonicalOrder(test.terms), canonicalOrder(tt)))
    if (any(is.na(index))) 
        stop("Terms didn't match:", canonicalOrder(test.terms), canonicalOrder(tt))
    if (test_intercept) {
        if (attr(terms(model), "intercept")) 
            index <- unique(c(1, index))
        else stop("model does not have an intercept")
    }
    beta <- coef(model)[index]
    if (!is.null(null)) 
        beta <- beta - null
    V <- vcov(model)[index, index]
    if (is.null(df)) {
        if (inherits(model, "svyglm")) 
            df <- ifelse(model$df.residual <= 0, degf(model$survey.design), model$df.residual)
        else if (inherits(model, "svycoxph")) 
            df <- ifelse(model$degf.resid <= 0, degf(model$survey.design), model$degf.resid)
        else if (inherits(model, "lm")) 
            df <- model$df.residual
        else if (inherits(model, "coxph")) 
            df <- model$n - length(coef(model))
        else if (inherits(model, "MIresult")) 
            df <- min(model$df[index])
        else if (inherits(model, "svyloglin")) 
            df <- model$df + 1 - length(index)
        else if (inherits(model, "svyolr")) 
            df <- model$df.residual
        else df <- length(resid(model)) - length(coef(model))
    }
    if (method %in% c("LRT", "WorkingWald")) {
        if (inherits(model, "svyglm")) 
            V0 <- model$naive.cov
        else if (inherits(model, "svycoxph")) 
            V0 <- model$inv.info
        else if (inherits(model, "lm")) 
            V0 <- vcov(model)
        else if (inherits(model, "coxph")) {
            if (is.null(model$naive.var)) 
                V0 <- model$var
            else V0 <- model$naive.var
        }
        else if (inherits(model, "svyolr")) {
            V0 <- solve(model$Hess)
        }
        else stop("method='LRT' not supported for this model")
        V0 <- V0[index, index]
        if (test_intercept) {
            test.formula <- make.formula(c(1, test.terms))[[2]]
        }
        else {
            test.formula <- make.formula(test.terms)[[2]]
        }
        if (!("formula" %in% names(model$call))) 
            names(model$call)[[2]] <- "formula"
        if (method == "LRT") {
            model0 <- eval(bquote(update(.(model), . ~ . - (.(test.formula)))), environment(formula(model)))
            chisq <- deviance_svycoxph(model0) - deviance_svycoxph(model)
        }
        else {
            chisq <- beta %*% solve(V0) %*% beta
        }
        misspec <- eigen(solve(V0) %*% V, only.values = TRUE)$values
        if (df == Inf) 
            p <- pchisqsum(chisq, rep(1, length(misspec)), misspec, method = lrt.approximation, lower.tail = FALSE)
        else p <- pFsum(chisq, rep(1, length(misspec)), misspec, ddf = df, method = lrt.approximation, 
            lower.tail = FALSE)
        rval <- list(call = sys.call(), mcall = model$call, chisq = chisq, df = length(index), test.terms = test.terms, 
            p = p, lambda = misspec, ddf = df)
        if (method == "LRT") 
            class(rval) <- "regTermTestLRT"
        else class(rval) <- "regTermTestWW"
        return(rval)
    }
    chisq <- beta %*% solve(V) %*% beta
    if (df < Inf) {
        Ftest <- chisq/length(index)
        rval <- list(call = sys.call(), mcall = model$call, Ftest = Ftest, df = length(index), ddf = df, 
            test.terms = test.terms, p = pf(Ftest, length(index), df, lower.tail = FALSE))
    }
    else {
        rval <- list(call = sys.call(), mcall = model$call, chisq = chisq, df = length(index), test.terms = test.terms, 
            p = pchisq(chisq, length(index), lower.tail = FALSE))
    }
    class(rval) <- "regTermTest"
    rval
}
```

## `regType` [internal]

```r
function (fit) 
{
    if (fit$call[[1]] == "svycoxph") {
        "coxph"
    }
    else if (fit$call[[1]] == "coxph") {
        "coxph"
    }
    else if (fit$call[[1]] == "cph") {
        "coxph"
    }
    else if (fit$call[[1]] == "ols") {
        "lm"
    }
    else if (fit$call[[1]] == "lrm") {
        "logit"
    }
    else if (fit$call[[1]] == "lm") {
        "lm"
    }
    else if (fit$call[[1]] == "svyglm") {
        if (fit$family[[1]] == "gaussian") {
            "lm"
        }
        else {
            "logit"
        }
    }
    else if (fit$call[[1]] == "glm") {
        if (fit$family[[1]] == "gaussian") {
            "lm"
        }
        else {
            "logit"
        }
    }
}
```

## `rename` [exported]

```r
function (.data, ...) 
{
    UseMethod("rename")
}
```

## `rename_fdcd` [internal]

```r
function (x, fdcd = "food.code") 
{
    if (is.data.frame(x)) {
        colnames(x) <- rename_fdcd(colnames(x), fdcd = fdcd)
    }
    else {
        x[x %in% c("drdifdcd", "dr1ifdcd", "dr2ifdcd", "drxfdcd")] <- fdcd
    }
    x
}
```

## `rename_line` [internal]

```r
function (x) 
{
    if (is.data.frame(x)) {
        colnames(x) <- rename_line(colnames(x))
    }
    else {
        x[x %in% c("drxiline", "dr1iline", "dr2iline")] <- "line"
    }
    x
}
```

## `rename_rstz` [internal]

```r
function (x) 
{
    if (is.data.frame(x)) {
        colnames(x) <- rename_rstz(colnames(x))
    }
    else {
        x[x %in% c("dr1drstz", "dr2drstz", "drddrsts", "drddrstz")] <- "rstz"
    }
    x
}
```

## `return_data` [internal]

```r
function (data, d, Year, key = "seqn", join = "left") 
{
    if (!missing(data)) {
        if (!is.null(data)) {
            append_year <- unique(data$Year)
            if (is.null(append_year)) 
                append_year <- attr(data, "nhs_years")
            ck_psu <- set::grep_and(colnames(data), "sdmvpsu")
            if (length(ck_psu) >= 2) {
                col_rename(data) <- paste0(ck_psu[1], ":sdmvpsu")
                data <- drop_col(data, ck_psu[-1])
            }
            ck_stra <- set::grep_and(colnames(data), "sdmvstra")
            if (length(ck_stra) >= 2) {
                col_rename(data) <- paste0(ck_stra[1], ":sdmvstra")
                data <- drop_col(data, ck_stra[-1])
            }
            ck_psu <- set::grep_and(colnames(data), "Year\\.[\\.xy]{1,}")
            if (length(ck_psu) >= 2) {
                col_rename(data) <- paste0(ck_psu[1], ":Year")
                data <- drop_col(data, ck_psu[-1])
            }
        }
    }
    if (!missing(d)) {
        ck_psu <- set::grep_and(colnames(d), "sdmvpsu")
        if (length(ck_psu) >= 2) {
            col_rename(d) <- paste0(ck_psu[1], ":sdmvpsu")
            d <- drop_col(d, ck_psu[-1])
        }
        ck_stra <- set::grep_and(colnames(d), "sdmvstra")
        if (length(ck_stra) >= 2) {
            col_rename(d) <- paste0(ck_stra[1], ":sdmvstra")
            d <- drop_col(d, ck_stra[-1])
        }
        ck_psu <- set::grep_and(colnames(d), "Year\\.[\\.xy]{1,}")
        if (length(ck_psu) >= 2) {
            col_rename(d) <- paste0(ck_psu[1], ":Year")
            d <- drop_col(d, ck_psu[-1])
        }
        append_year <- unique(d$Year)
    }
    if (!Year) 
        d <- drop_col(d, "Year")
    if (missing(data)) {
        attr(d, "nhs_years") <- append_year
        return(d)
    }
    if (is.null(data)) {
        attr(d, "nhs_years") <- append_year
        return(d)
    }
    if (!is.null(data)) {
        if (nrow(data) == 0) {
            attr(d, "nhs_years") <- append_year
            return(d)
        }
    }
    if ("Year" %in% data) 
        d <- drop_col(d, "Year")
    data <- eval(parse(text = sprintf("dplyr::%s_join(data,d,key)", join)))
    ck_psu <- set::grep_and(colnames(data), "Year\\.[\\.xy]{1,}")
    if (length(ck_psu) >= 2) {
        col_rename(data) <- paste0(ck_psu[1], ":Year")
        data <- drop_col(data, ck_psu[-1])
    }
    attr(data, "nhs_years") <- append_year
    data
}
```

## `row_names` [exported]

```r
function (data, names) 
{
    if (missing(names)) 
        return(row.names(data))
    row.names(data) <- names
    data
}
```

## `sd_by` [internal]

```r
function (data, x, by) 
{
    if (length(x) == 1) {
        string <- sprintf("aggregate(data[,x],by=list(%s),sd,na.rm=TRUE)", paste0(sprintf("data[,'%s']", 
            by), collapse = ","))
        r <- eval(parse(text = string))
        colnames(r)[1:length(by)] <- by
        colnames(r)[ncol(r)] <- paste0(x, "_sd")
        return(r)
    }
    else {
        for (i in 1:length(x)) {
            if (i == 1) {
                r1 <- sd_by(data, x[i], by)
            }
            else {
                r2 <- sd_by(data, x = x[i], by)
                r1 <- dplyr::full_join(r1, r2, by)
            }
        }
        return(r1)
    }
}
```

## `search_fn` [internal]

```r
function (...) 
{
    pkg <- "nhanesR"
    allfns <- do::increase(getNamespaceExports(pkg))
    h0 <- c(...)
    dn <- paste0(".", pkg, "search4fntxt")
    if (dn %in% ls(envir = .GlobalEnv)) {
        vt <- get(dn)
        ck <- lookl(vt, h0)
        fni <- allfns[ck]
    }
    else {
        txt <- sapply(allfns, function(i) {
            hs <- eval(parse(text = sprintf("help(i,'%s')", pkg)))
            if (class(hs)[1] == "help_files_with_topic") {
                xx <- utils:::.getHelpFile(as.character(hs))
                paste0(do::rm_nchar(as.character(xx), 1), collapse = ";;;;;")
            }
            else if (class(hs)[1] == "dev_topic") {
                (xx <- capture.output(tools::Rd2txt(hs$path)) %>% do::Replace0("_\b", " ") %>% do::rm_nchar(1))
                paste0(xx, collapse = ";;;;")
            }
        })
        eval(parse(text = sprintf("%s <<- txt", dn)))
        ck <- lookl(txt, h0)
        fni <- allfns[ck]
    }
    if (length(fni) > 0) {
        help.start()
        for (i in fni) {
            hs <- eval(parse(text = sprintf("help(i,'%s')", pkg)))
            if (class(hs)[1] == "dev_topic") {
                rstudioapi::callFun("previewRd", hs$path)
            }
            else if (class(hs)[1] == "help_files_with_topic") {
                print(hs)
            }
        }
        cat(paste0(rev(fni), collapse = "\n"))
    }
    else {
        message("<U+6CA1><U+6709><U+641C><U+5230><U+76F8><U+5173><U+51FD><U+6570>")
        invisible()
    }
}
```

## `search_words_inR` [internal]

```r
function (..., edit = F) 
{
    (r <- list.files("./r", full.names = T) %>% set::grep_not_and("sysdata.rda"))
    h0 <- c(...)
    for (j in 1:length(h0)) {
        if (j == 1) 
            ck <- T
        ckj <- sapply(r, function(i) {
            txt <- suppressWarnings(readLines(i))
            any(grepl(h0[j], txt, ignore.case = T))
        })
        ck <- ck & ckj
    }
    r <- r[ck]
    if (edit) {
        clipr::write_clip(h0)
        file.edit(r)
    }
    r
}
```

## `search_words_inR_inline` [internal]

```r
function (..., edit = F, ignore.case = T) 
{
    (r <- list.files("./r", full.names = T) %>% set::grep_not_and("sysdata.rda"))
    h0 <- c(...)
    ck <- sapply(r, function(i) {
        txt <- suppressWarnings(readLines(i))
        any(set::grepl_and(txt, h0))
    })
    r <- r[ck]
    if (edit) {
        clipr::write_clip(h0)
        file.edit(r)
    }
    r
}
```

## `select` [exported]

```r
function (.data, ...) 
{
    UseMethod("select")
}
```

## `select_col` [exported]

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

## `select_df` [internal]

```r
function (x, ...) 
{
    x[, c(...)]
}
```

## `select_row` [exported]

```r
function (x, ...) 
UseMethod("select_row")
```

## `seqn_by` [internal]

```r
function (x, by) 
{
    bylist <- lapply(by, nchar)
    names(bylist) <- by
    de <- do::decrease(unique(nchar(by)))
    for (i in 1:length(de)) {
        ck <- sapply(by, function(j) nchar(j) == de[i])
        xi <- by[ck]
        for (j in 1:length(xi)) {
            ckj <- do::left(x, nchar(xi[j])) == xi[j]
            bylist[[xi[j]]] <- x[ckj]
            x <- x[!ckj]
        }
    }
    xn <- unlist(bylist)
    names(xn) <- NULL
    xn
}
```

## `setReference` [exported]

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

## `showSpecialMessage` [internal]

```r
function (..., envir = parent.frame()) 
{
    temp <- tempfile()
    nullcon <- file(temp, open = "wb")
    sink(nullcon, type = "message")
    expr <- substitute(...)
    suppressWarnings(tryCatch(eval(expr, envir = envir), error = function(e) list(error = conditionMessage(e))))
    sink(type = "message")
    close(nullcon)
    msg <- readLines(temp, encoding = "UTF-8")
    unlink(temp)
    msg
}
```

## `size_bt2unit` [internal]

```r
function (bt) 
{
    if (bt < 1024) {
        paste(round(bt, 2), "B")
    }
    else if (bt < 1024 * 1024) {
        paste(round(bt/1024, 2), "KB")
    }
    else if (bt < 1024 * 1024 * 1024) {
        paste(round(bt/1024/1024, 2), "MB")
    }
    else if (bt < 1024 * 1024 * 1024 * 1024) {
        paste(round(bt/1024/1024/1024, 2), "GB")
    }
    else if (bt < 1024 * 1024 * 1024 * 1024 * 1024) {
        paste(round(bt/1024/1024/1024/1024, 2), "TB")
    }
}
```

## `start_with` [internal]

```r
function (x, start) 
{
    ck <- rowSums(data.frame(lapply(start, function(i) startsWith(x, i))))
    x[ck > 0]
}
```

## `stork_paper` [internal]

```r
function (english, file = "stork2.xlsx") 
{
    df <- stork_paper1(english)
    wb <- openxlsx::createWorkbook()
    openxlsx::addWorksheet(wb, "Sheet1")
    openxlsx::writeData(wb, sheet = 1, x = "<U+53D1><U+8868><U+65E5><U+671F>", startCol = 1, startRow = 1)
    openxlsx::writeData(wb, sheet = 1, x = "<U+79D1><U+5BA4>", startCol = 2, startRow = 1)
    openxlsx::writeData(wb, sheet = 1, x = "<U+4E34><U+5E8A><U+5173><U+952E><U+8BCD>", startCol = 3, 
        startRow = 1)
    openxlsx::writeData(wb, sheet = 1, x = "<U+7EDF><U+8BA1><U+5173><U+952E><U+8BCD>", startCol = 4, 
        startRow = 1)
    for (i in 1:ncol(df)) {
        openxlsx::writeData(wb, sheet = 1, x = colnames(df)[i], startCol = i + 4, startRow = 1)
        if (colnames(df)[i] == "pmid") {
            x <- sprintf("https://pubmed.ncbi.nlm.nih.gov/%s/", df$pmid)
            names(x) <- df$pmid
            class(x) <- "hyperlink"
            openxlsx::writeData(wb, sheet = 1, x = x, startCol = i + 4, startRow = 2)
        }
        else {
            openxlsx::writeData(wb, sheet = 1, x = df[, i], startCol = i + 4, startRow = 2)
        }
    }
    openxlsx::saveWorkbook(wb, file, overwrite = TRUE)
}
```

## `stork_paper1` [internal]

```r
function (html) 
{
    hi <- set::grep_and(rvest::html_elements(rvest::html_element(rvest::read_html(html), xpath = "//div[@class=\"card-body bg-light\"]"), 
        xpath = "//div[@id != \"exportspinner\"]"), "id=\"stork-paper-")
    hi
    r <- do.call(lapply(1:length(hi), function(i) {
        year <- as.numeric(do::Replace0(date(), ".* "))
        year <- c(year - 1, year, year + 1)
        (yeartxt <- paste0(sprintf(".*\\(%s\\) {0,}", year), collapse = "|"))
        (title <- rvest::html_text(set::grep_and(rvest::html_children(hi[[i]]), "<a target=\"_blank\" href=")))
        (title.cn <- do::Trim(do::Replace0(rvest::html_text(hi[[i]]), " {0,}PMID: .*", title, ".*\n"), 
            c("]", "[")))
        (journal <- do::Replace0(do::Replace0(do::Replace0(do::Replace0(do::Replace0(rvest::html_text(hi[[i]]), 
            " {0,}PMID: .*"), " {0,}[0-9\\.]{0,} {0,}<U+533A>.*"), " {0,}\\(impact factor:.*"), yeartxt), 
            "\n.*"))
        (factor <- ifelse(grepl("impact factor:", rvest::html_text(hi[[i]]), TRUE), as.numeric(do::Replace0(rvest::html_text(hi[[i]]), 
            ".*\\(impact factor: {0,}", " {0,}\\).*")), numeric()))
        (level <- rvest::html_text(set::grep_and(rvest::html_children(hi[[i]]), "<U+533A>")))
        if (length(level) == 0) 
            level <- NA
        (pmid <- do::Replace0(rvest::html_text(set::grep_and(rvest::html_children(hi[[i]]), "PMID: ")), 
            " {0,}doi:.*", " {0,}PMID: {0,}"))
        (yeartxt2 <- paste0(sprintf(" {0,}\\(%s\\).*", year), collapse = "|"))
        (author <- do::Replace0(rvest::html_text(hi[[i]]), yeartxt2, ".* by "))
        data.frame(title.cn, title, factor, level, pmid, journal, author)
    }), what = rbind)
    df <- do::Replace0(r, " {0,}Free full text {0,}")
    cbind(id = 1:nrow(df), df)
}
```

## `stratum_model` [exported]

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

## `stratum_model_i` [internal]

```r
function (object, time = NULL, y, x, stratum = NULL, adjust = NULL, p = TRUE, round = 3, interaction = TRUE) 
{
    .stratum_model_object <<- object
    if (length(x) != 1) 
        stop(tmcn::toUTF8("x<U+53EA><U+80FD><U+662F>1<U+4E2A><U+53D8><U+91CF>"))
    (allvars <- c(time, y, x, stratum, adjust))
    ck <- allvars %in% colnames(object)
    if (!all(ck)) {
        stop(paste0(tmcn::toUTF8("<U+62FC><U+5199><U+9519><U+8BEF><U+7684><U+53D8><U+91CF>: "), paste0(allvars[!ck], 
            collapse = ", ")))
    }
    (x.vars <- c(x, adjust))
    if ("survey.design" %in% class(object)) {
        ck <- length(do::complete.data(unique(object$variables[, y]))) == 2
        if (!is.null(time)) {
            regtype <- "cox"
            formu0 <- sprintf("survey::svycoxph(survival::Surv(%s,%s) ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss,design=.stratum_model_object2)", 
                time, y)
        }
        else if (ck) {
            regtype <- "logistic"
            formu0 <- sprintf("survey::svyglm(%s ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss,family=quasibinomial(),design=.stratum_model_object2)", 
                y)
        }
        else {
            regtype <- "linear"
            formu0 <- sprintf("survey::svyglm(%s ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss, design=.stratum_model_object2)", 
                y)
        }
    }
    else {
        (ck <- length(suppressMessages(do::complete.data(unique(object[[y]])))) == 2)
        if (!is.null(time)) {
            regtype <- "cox"
            formu0 <- sprintf("rms::cph(Surv(%s,%s) ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss,data=.stratum_model_object2,iter.max=400)", 
                time, y)
        }
        else if (ck) {
            regtype <- "logistic"
            formu0 <- sprintf("rms::lrm(%s ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss,data=.stratum_model_object2)", 
                y)
        }
        else {
            regtype <- "linear"
            formu0 <- sprintf("rms::ols(%s ~ ddlalaeaeatatasasatatapapaoaoaaaaarruummsss, data=.stratum_model_object2)", 
                y)
        }
    }
    if ("survey.design" %in% class(object)) {
        data0 <- as.data.frame(object$variables)
    }
    else {
        data0 <- as.data.frame(object)
    }
    rt <- do.call(lapply(1:length(stratum), function(i) {
        (su <- do::complete.data(unique(data0[[stratum[i]]])))
        (level <- set::and(levels(su), unique(su)))
        y
        if (regtype %in% c("cox", "logistic")) {
            ys0 <- eval(parse(text = sprintf("table(%s=data0[,y],%s=data0[,stratum[i]])", y, stratum[i])))
            if (any(ys0 == 0)) {
                print(ys0)
                stop(tmcn::toUTF8("<U+7ED3><U+5C40><U+5728><U+67D0><U+4E9B><U+5C42><U+4E2D><U+53EA><U+6709><U+4E00><U+4E2A><U+6570><U+503C>,<U+4E0D><U+80FD><U+8FDB><U+884C><U+5206><U+5C42>"))
            }
        }
        if (is.null(level)) 
            level <- su
        passformu <- new.env()
        rt <- do.call(lapply(level, function(j) {
            ck <- data0[[stratum[i]]] %in% j
            (n <- sum(ck))
            .stratum_model_object2 <<- eval(parse(text = sprintf("subset(object,%s %s '%s')", stratum[i], 
                "%in%", j)))
            stratum_model_object2.data0 <- data0[ck, ]
            for (vi in x.vars) {
                viu <- do::complete.data(unique(stratum_model_object2.data0[, vi]))
                if (length(viu) <= 1) {
                  if (stratum[i] != vi) {
                    tbe <- print(eval(parse(text = sprintf("table(%s=data0[,stratum[i]],%s=data0[,vi])", 
                      stratum[i], vi))))
                    if (min(tbe) <= 0) 
                      stop(tmcn::toUTF8(paste0("<U+53D8><U+91CF> ", vi, " <U+5728><U+5C42><U+53D8><U+91CF> ", 
                        stratum[i], " <U+4E2D><U+7684> ", j, " <U+5C42><U+4E2D><U+4EC5><U+6709><U+4E00><U+4E2A><U+552F><U+4E00><U+503C>: ", 
                        viu)))
                  }
                }
            }
            formu <<- do::Replace(formu0, "ddlalaeaeatatasasatatapapaoaoaaaaarruummsss", paste0(set::not(x.vars, 
                stratum[i]), collapse = "+"))
            passformu$formu <- formu
            fit <- eval(parse(text = formu))
            (rt <- reg_table(fit, x = x, view = F, round = round))
            pos2 <- c(1, which(grepl("ci", colnames(rt), T)), which(grepl("p", colnames(rt), T)))
            (rt2 <- rt[, pos2])
            colnames(rt2)[ncol(rt2)] <- "p"
            if (nrow(rt2) == 1) {
                rt2[1, 1] <- j
                rt2
            }
            else {
                rt2[, 1] <- do::Trim_left(rt2[, 1])
                (rt2 <- rt2[nchar(rt2[, 2]) > 0, ])
                rt3 <- do.call(lapply(1:nrow(rt2), function(m) {
                  if (m == 1) {
                    do::give_names(rt2[m, -1], c(c(rt2[m, 1], paste0("p_add_pvalue_", rt2[m, 1]))))[, 
                      -2, drop = F]
                  }
                  else {
                    do::give_names(rt2[m, -1], c(c(rt2[m, 1], paste0("p_add_pvalue_", rt2[m, 1]))))
                  }
                }), what = cbind)
                (rt3 <- cbind(character = j, rt3))
                (cbind(rt3, as.data.frame(t(p4trend(fit, x, round = round)))))
            }
        }), what = plyr::rbind.fill)
        (rt <- rbind(rt[1, ], rt))
        rt[1, 1] <- stratum[i]
        rt[1, -1] <- ""
        if (interaction) {
            rt$"p for interaction" <- ""
            formu2 <- do::Replace(do::Replace(do::Replace(passformu$formu, paste0("~ ", x, "\\+{0,1}"), 
                paste0("~ ", x, "*", stratum[i], " + ")), "\\+ ,", ","), ".stratum_model_object2", ".stratum_model_object")
            rt[1, ncol(rt)] <- suppressWarnings(tryCatch(pvalue.digit(p4interaction(eval(parse(text = formu2))), 
                round), error = function(e) "error"))
        }
        rt
    }), what = plyr::rbind.fill)
    rt
    if (!p) 
        rt <- rt[, !grepl("p_add_pvalue_", colnames(rt))]
    rt
}
```

## `subsetdesign2df` [exported]

```r
function (design, ...) 
{
    design <- subset(design, ...)
    design$variables$weights <- (1/design$prob)/mean(1/design$prob)
    design$variables
}
```

## `svy2rms` [internal]

```r
function (fit, by = NULL) 
{
    (cal <- fit$call)
    deparse(fit$call[[1]])
    if (deparse(fit$call[[1]]) %in% c("ols", "lrm", "cph")) {
        nms <- c(all.vars(fit$terms), by)
        dcal <- eval(cal$data)
        res <- list(fit, dcal[, nms])
        return(res)
    }
    if (deparse(cal[[1]]) == "svycoxph") {
        cal[[1]] <- as.name("cph")
    }
    else if (fit$family[[1]] == "gaussian") {
        cal[[1]] <- as.name("ols")
    }
    else {
        cal[[1]] <- as.name("lrm")
    }
    cal$family <- NULL
    .svy2rms.data <- fit$survey.design$variables
    if (!is.null(by)) {
        (chn <- set::and(colnames(.svy2rms.data)[sapply(.svy2rms.data, function(i) is.character(i) | 
            is.factor(i))], all.vars(fit$terms)))
        chn <- set::not(chn, by)
        if (length(chn) >= 1) {
            for (i in chn) {
                tb <- eval(parse(text = sprintf("table(%s=.svy2rms.data[,i],%s=.svy2rms.data[,by])", 
                  i, by)))
                if (any(tb == 0)) {
                  cat("\n")
                  print(tb)
                  cat("\n")
                  stop(tmcn::toUTF8("<U+5206><U+7EC4><U+53D8><U+91CF>  "), by, tmcn::toUTF8("  <U+4E0E><U+5206><U+7C7B><U+53D8><U+91CF>  "), 
                    i, tmcn::toUTF8("  <U+6709>0<U+4EA4><U+53C9><U+4E9A><U+7EC4>"))
                }
            }
        }
    }
    .svy2rms.data$weights <- (1/fit$survey.design$prob)/mean(1/fit$survey.design$prob)
    .svy2rms.data <<- .svy2rms.data
    (p <- fit$survey.design$call$data)
    if (is.null(p)) {
        names(cal)[names(cal) == "design"] <- "data"
        x <- tryCatch(cal[[3]][[1]], error = function(e) "e")
        if (is.character(x)) {
            cal[[3]] <- as.name(".svy2rms.data")
        }
        else {
            if (all(deparse(x) == "subset")) {
                cal[[3]][[2]] <- as.name(".svy2rms.data")
            }
            else {
                cal[[3]][[1]] <- as.name(".svy2rms.data")
            }
        }
        cal$weights <- as.name("weights")
        cal$normwt <- TRUE
        cal$maxit <- 200
        cal$tol <- 1.0000000000000001e-09
        old <- options()
        options(datadist = suppressWarnings(rms::datadist(.svy2rms.data)))
        res <- list(fit = suppressWarnings(eval(cal)), data = .svy2rms.data)
        names(res)[2] <- deparse(p)
    }
    else {
        eval(parse(text = sprintf("%s = .svy2rms.data", deparse(p))))
        names(cal)[names(cal) == "design"] <- "data"
        cal[[3]] <- as.name(deparse(p))
        cal$weights <- as.name("weights")
        cal$normwt <- TRUE
        cal$maxit <- 200
        cal$tol <- 1.0000000000000001e-09
        old <- options()
        options(datadist = suppressWarnings(rms::datadist(.svy2rms.data)))
        res <- list(fit = suppressWarnings(eval(cal)), data = .svy2rms.data)
        names(res)[2] <- deparse(p)
    }
    if (is.null(old$datadist)) 
        options(datadist = NULL)
    options(old)
    res
}
```

## `tableB` [internal]

```r
function (..., id = NULL, class = NULL, title = NULL, name = NULL) 
{
    attribs <- list(id = id, class = class, title = title, name = name)
    children <- list(...)
    st <- list(name = "table", attribs = attribs, children = children)
    st <- structure(st, class = "shiny.tag")
    st
}
```

## `tbodyB` [internal]

```r
function (..., class = NULL, title = NULL, name = NULL) 
{
    attribs <- list(class = class, title = title, name = name)
    children <- list(...)
    st <- list(name = "tbody", attribs = attribs, children = children)
    st <- structure(st, class = "shiny.tag")
    st
}
```

## `tdB` [internal]

```r
function (..., colspan = NULL, headers = NULL, rowspan = NULL, class = NULL, title = NULL, name = NULL) 
{
    attribs <- list(colspan = colspan, headers = headers, rowspan = rowspan, class = class, title = title, 
        name = name)
    children <- list(...)
    st <- list(name = "td", attribs = attribs, children = children)
    st <- structure(st, class = "shiny.tag")
    st
}
```

## `test_mode` [internal]

```r
function (years = 1999, items = "die") 
{
    fl <- nhs_files_web(years, items, FALSE)
    ck <- set::grepl_and(fl$`Data File`, "kb")
    fl <- fl[ck, ]
    url <- fl$`Data url`[1]
    xpt <- tempfile(fileext = ".xpt")
    mode <- c("wb", "w", "ab")
    for (i in mode) {
        x <- tryCatch(download.file(url = url, destfile = xpt, mode = i, quiet = TRUE), error = function(e) "e", 
            warning = function(w) "w")
        if (x == 0) {
            x <- tryCatch(haven::read_xpt(xpt), error = function(e) "e")
            if (is.data.frame(x)) 
                return(i)
        }
    }
}
```

## `testfile` [internal]

```r
function (urls, files, mode, redown = TRUE, xpt = TRUE, tsv = TRUE, varLabel = TRUE, codebook = TRUE, 
    update = TRUE, filetable = NULL, updatekeyword = NULL) 
{
    for (i in 1:length(urls)) {
        (yeari <- do::Replace0(urls[i], ".*="))
        (itemsi <- urlComponet(urls[i]))
        if (i == 1) {
            cat("\n", prepare_years(yeari), "\n")
            cat("      ", itemsi)
        }
        else {
            if (urlyear(urls[i]) != urlyear(urls[i - 1])) {
                cat("\n", prepare_years(yeari))
            }
            if (itemsi != urlComponet(urls[i - 1])) {
                cat("\n      ", itemsi)
            }
        }
        filepage(yeari = yeari, itemsi = itemsi, mode = mode, files = files, redown = redown, xpt = xpt, 
            tsv = tsv, varLabel = varLabel, codebook = codebook, updatefile = update, filetable = filetable, 
            updatekeyword = updatekeyword)
        if (i == length(urls)) 
            cat("\n")
    }
}
```

## `thB` [internal]

```r
function (..., abbr = NULL, colspan = NULL, headers = NULL, rowspan = NULL, scope.col = FALSE, scope.colgroup = FALSE, 
    scope.row = FALSE, scope.rowgroup = FALSE, class = NULL, title = NULL, name = NULL) 
{
    scope <- NULL
    if (scope.col) 
        scope <- "col"
    if (scope.colgroup) 
        scope <- "colgroup"
    if (scope.row) 
        scope <- "row"
    if (scope.rowgroup) 
        scope <- "rowgroup"
    attribs <- list(abbr = abbr, colspan = colspan, headers = headers, rowspan = rowspan, scope = scope, 
        class = class, title = title, name = name)
    children <- list(...)
    st <- list(name = "th", attribs = attribs, children = children)
    st <- structure(st, class = "shiny.tag")
    st
}
```

## `time_diff` [internal]

```r
function (t1, t2) 
{
    diff <- as.numeric(t1) - as.numeric(t2)
    if (diff < 60) {
        dif <- round(diff/1, 2)
        p <- paste(dif, ifelse(dif == 1, "second", "seconds"))
    }
    else if (diff >= 60 & diff < 60 * 60) {
        dif <- round(diff/60, 2)
        p <- paste(dif, ifelse(diff == 1, "minute", "minutes"))
    }
    else if (diff >= 60 * 60 & diff < 60 * 60 * 24) {
        dif <- round(diff/60/60, 2)
        p <- paste(dif, ifelse(diff == 1, "hour", "hours"))
    }
    else if (diff >= 60 * 60 * 24 & diff < 60 * 60 * 24 * 365) {
        dif <- round(diff/60/60/24, 2)
        p <- paste(dif, ifelse(diff == 1, "day", "days"))
    }
    else if (diff >= 60 * 60 * 24 * 365 & diff < 60 * 60 * 24 * 365 * 100) {
        dif <- round(diff/60/60/24/365, 2)
        p <- paste(dif, ifelse(diff == 1, "year", "years"))
    }
    else {
        dif <- round(diff/60/60/24/365/100, 2)
        p <- paste(dif, ifelse(diff == 1, "century", "centurys"))
    }
    p
}
```

## `to_NA` [exported]

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

## `to_numeric` [exported]

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

## `to_sql` [internal]

```r
function (x, name, before = "", after = "") 
{
    (name <- sprintf("LOWER(%s)", name))
    x <- tolower(do::Trim(do::Replace(do::Replace(do::Replace(do::Replace(x, " {0,}\\| {0,}", "\\|"), 
        " {0,}\\& {0,}", "\\&"), " {0,}\\( {0,}", "\\("), " {0,}\\) {0,}", "\\)")))
    x
    lq = 0
    while (do::left(x, 1) == "(") {
        lq <- lq + 1
        x <- do::knife_left(x, 1)
    }
    rq = 0
    while (do::right(x, 1) == "(") {
        rq <- rq + 1
        x <- do::knife_right(x, 1)
    }
    lq_in <- qoute_n(nchar_max(stringr::str_extract_all(x, "[\\|\\&]\\({0,}")[[1]]), "left")
    rq_in <- qoute_n(nchar_max(stringr::str_extract_all(x, "\\){0,}[\\|\\&]")[[1]]), "right")
    for (i in lq_in:0) {
        for (j in rq_in:0) {
            from <- paste0(paste0(rep(")", j), collapse = ""), "\\|", paste0(rep("(", i), collapse = ""))
            to <- paste0(paste0(after, "%'"), paste0(rep(")", j), collapse = ""), " OR ", paste0(rep(")", 
                i), collapse = ""), paste0(" ", name, " like '%", before))
            x <- gsub(from, to, x)
            from <- paste0(paste0(rep(")", j), collapse = ""), "\\&", paste0(rep("(", i), collapse = ""))
            to <- paste0(paste0(after, "%'"), paste0(rep(")", j), collapse = ""), " AND ", paste0(rep(")", 
                i), collapse = ""), paste0(" ", name, " like '%", before))
            x <- gsub(from, to, x)
        }
    }
    paste0(paste0(paste0(rep("(", lq), collapse = ""), name, " like '%", before), x, paste0(paste0(rep(")", 
        rq), collapse = ""), after, "%'"))
}
```

## `trB` [internal]

```r
function (..., class = NULL, title = NULL, name = NULL) 
{
    attribs <- list(class = class, title = title, name = name)
    children <- list(...)
    st <- list(name = "tr", attribs = attribs, children = children)
    st <- structure(st, class = "shiny.tag")
    st
}
```

## `transfer_fndds` [exported]

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

## `tsv0` [internal]

```r
function (tsv, return.NULL = FALSE, data, msg.CN = NULL, msg.EN = NULL) 
{
    if (is.null(msg.CN)) {
        if (is.null(return.NULL)) {
            msg.CN <- "error"
        }
        else {
            msg.CN <- tmcn::toUTF8("<U+8BE5><U+5E74><U+4EFD><U+6CA1><U+6709><U+6570><U+636E>")
        }
    }
    if (is.null(msg.EN)) {
        if (is.null(return.NULL)) {
            msg.EN <- "error"
        }
        else {
            msg.EN <- "no data in these years"
        }
    }
    if (is.null(tsv)) {
        if (!missing(data)) 
            return(data)
        if (!do::cnOS() & return.NULL) 
            return(msg.CN)
        if (!do::cnOS() & !return.NULL) 
            stop(msg.EN)
        if (do::cnOS() & !return.NULL) 
            stop(msg.CN)
        if (do::cnOS() & return.NULL) 
            return(msg.CN)
    }
    if (is.character(tsv)) {
        if (length(tsv) == 0) {
            if (!missing(data)) 
                return(data)
            if (!do::cnOS() & !return.NULL) 
                stop(msg.EN)
            if (!do::cnOS() & return.NULL) 
                return(msg.CN)
            if (do::cnOS() & !return.NULL) 
                stop(msg.CN)
            if (do::cnOS() & return.NULL) 
                return(msg.CN)
        }
        else if (all(tsv == "no data selected")) {
            if (!missing(data)) 
                return(data)
            if (!do::cnOS() & !return.NULL) 
                stop(msg.EN)
            if (!do::cnOS() & return.NULL) 
                return(msg.CN)
            if (do::cnOS() & !return.NULL) 
                stop(msg.CN)
            if (do::cnOS() & return.NULL) 
                return(msg.CN)
        }
    }
    else if (is.data.frame(tsv)) {
        if (nrow(tsv) == 0) {
            if (!missing(data)) 
                return(data)
            if (!do::cnOS() & !return.NULL) 
                stop(msg.EN)
            if (!do::cnOS() & return.NULL) 
                return(msg.CN)
            if (do::cnOS() & !return.NULL) 
                stop(msg.CN)
            if (do::cnOS() & return.NULL) 
                return(msg.CN)
        }
    }
    else if (is.list(tsv)) {
        if (length(tsv) == 0) {
            if (!missing(data)) 
                return(data)
            if (!do::cnOS() & !return.NULL) 
                stop(msg.EN)
            if (!do::cnOS() & return.NULL) 
                return(msg.CN)
            if (do::cnOS() & !return.NULL) 
                stop(msg.CN)
            if (do::cnOS() & return.NULL) 
                return(msg.CN)
        }
    }
}
```

## `unique_no_NA` [internal]

```r
function (x, collapse = ",") 
{
    x <- kit::funique(x)
    if (length(x) == 1) {
        if (is.na(x)) 
            return("thisisNANAisTHIS")
        x
    }
    else {
        x <- x[!is.na(x)]
        if (length(x) == 1) 
            return(x)
        paste0(x, collapse = collapse)
    }
}
```

## `updateKnot` [exported]

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

## `urlComponet` [internal]

```r
function (url) 
{
    do::Replace0(url, c(".*\\?Component=", "\\&CycleBeginYear.*"))
}
```

## `urlyear` [internal]

```r
function (url) 
{
    do::Replace0(url, c(".*=", ".*Nhanes/", "/.*"))
}
```

## `use_data_append` [internal]

```r
function (...) 
{
    nms <- do::get_names(...)
    lt <- list(...)
    env <- new.env(hash = FALSE)
    load("R/sysdata.rda", envir = env)
    for (i in 1:length(nms)) {
        env[[nms[i]]] <- lt[[i]]
    }
    save(list = names(env), file = "R/sysdata.rda", envir = env)
}
```

## `use_data_list` [internal]

```r
function () 
{
    env <- new.env(hash = FALSE)
    load("R/sysdata.rda", envir = env)
    nms <- names(env)
    env <- NULL
    nms
}
```

## `use_data_remove` [internal]

```r
function (...) 
{
    nms <- c(...)
    env <- new.env(hash = FALSE)
    load("R/sysdata.rda", envir = env)
    env[nms] <- NULL
    save(list = names(env), file = "R/sysdata.rda", envir = env)
}
```

## `varExtracted` [exported]

```r
function (x) 
{
    varnamelabel <- attr(x, "varnameLabel")
    kableExtra::kable_classic(kableExtra::kable_paper(kableExtra::kbl(varnamelabel, escape = FALSE), 
        "striped"), full_width = FALSE)
}
```

## `varLab_NULL` [internal]

```r
function (firs_publish, last_revise, file) 
{
    df <- data.frame(variable = 1, label = 2)
    df <- df[-c(1:nrow(df)), ]
    suppressWarnings(write.table(firs_publish, file, row.names = FALSE, col.names = FALSE, quote = FALSE))
    suppressWarnings(write.table(last_revise, file, row.names = FALSE, col.names = FALSE, append = TRUE, 
        quote = FALSE))
    suppressWarnings(write.table(x = df, file = file, sep = "\t", eol = "\n", row.names = FALSE, append = TRUE))
}
```

## `varLabel_url` [internal]

```r
function (url, file, html) 
{
    if (do::file.name(file) == "rxq_drug.varLabel") {
        htmlto <- do::Replace(file, "\\.varLabel", ".htm")
        xml2::write_html(html, htmlto)
        df <- as.data.frame(do::list1(rvest::html_table(rvest::html_elements(html, xpath = "//div[@id=\"Sections\"]"))))
        colnames(df) <- tolower(colnames(df))
        for (i in 1:ncol(df)) {
            df[, i] <- tolower(df[, i])
        }
        df <- df[, c("variable name", "label")]
        df <- df[nchar(df[[1]]) > 0, ]
        colnames(df)[1] <- "variable"
        df <- cbind(df, url)
        suppressWarnings(data.table::fwrite(df, file, sep = "\t"))
        invisible("ok")
    }
    else {
        if (tools::file_ext(url) == "pdf") {
            pdf <- paste0(do::Replace0(file, tools::file_ext(file)), "pdf")
            if (file.exists(pdf)) 
                file.remove(pdf)
            if (file.exists(pdf)) 
                unlink(pdf, force = TRUE)
            cat(crayon::bgWhite(" pdf"))
            nullcon <- file(nullfile(), open = "wb")
            sink(nullcon, type = "message")
            download.file(url, pdf)
            sink(type = "message")
            close(nullcon)
            if (!file.exists(file)) 
                varLab_NULL("#firs_publish:pdf", "#last_revise:pdf", file)
            return(invisible("pdf"))
        }
        if (missing(html)) {
            wait <- TRUE
            while (wait) {
                html <- tryCatch(xml2::read_html(url), error = function(e) "e")
                wait <- ifelse(is.character(html), TRUE, FALSE)
            }
        }
        htmlto <- do::Replace(file, paste0("\\.", tools::file_ext(file)), ".htm")
        xml2::write_html(html, htmlto)
        codebook <- set::grep_and(rvest::html_elements(html, xpath = "//div[@id=\"Codebook\"]//div[@class=\"pagebreak\"]"), 
            c("dl", "table"))
        codebook
        if (do::file.name(file) %in% c("p_imq.varLabel", "imq_j.varLabel", "alb_cr_g.varLabel")) {
            codebook <- rvest::html_elements(html, xpath = "//div[@id=\"Codebook\"]//div[@class=\"pagebreak\"]")
        }
        if (length(codebook) == 0) {
            varLab_NULL(firs_publish, last_revise, file)
            return(invisible("no codebook"))
        }
        df <- do.call(lapply(rvest::html_elements(codebook, xpath = "dl"), dl), what = plyr::rbind.fill)
        df
        if (nrow(df) == 0) {
            varLab_NULL(firs_publish, last_revise, file)
            return(invisible("no varLabel"))
        }
        else {
            df <- cbind(df, url)
            suppressWarnings(data.table::fwrite(df, file, sep = "\t"))
            invisible("ok")
        }
    }
}
```

## `var_labels` [exported]

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

## `var_labels_2_var_formula` [internal]

```r
function (tsv) 
{
    d <- nhs_read(tsv, nrows = 1, varLabel = TRUE)
    df <- var_labels(d)
    df <- df[!df$colname %=% c("seqn", "Year"), ]
    df[, 2] <- do::Replace(do::Replace(df[, 2], " ", "_"), "#_of", "number_of")
    df <- sprintf("variable_formula(%s,'%s')", df[, 2], df[, 1])
    if (length(df) > 1) 
        df[1:(length(df) - 1)] <- paste0(df[1:(length(df) - 1)], " |> ")
    writeClipboard(df)
}
```

## `variable_formula` [internal]

```r
function (var, arg, variable) 
{
    if (missing(var)) 
        var <- c()
    xc <- deparse(substitute(arg))
    if (missing(arg)) 
        return(var)
    if (isFALSE(arg)) 
        return(var)
    if (isTRUE(arg)) {
        c(var, sprintf("%s:%s", variable, xc))
    }
    else if (tolower(arg) == "-u") {
        c(var, sprintf("%s:%s-u", variable, xc))
    }
    else if (is.character(arg)) {
        c(var, sprintf("%s:%s", variable, arg))
    }
}
```

## `vitaminAE19999` [internal]

```r
function (data, VitA = FALSE, VitE = FALSE, dietary = "iff") 
{
    if (isFALSE(VitA) & isFALSE(VitE)) 
        stop("one of VitA or VitE must be specified")
    d <- drop_col(data.table::fread(list.files(list.files(list.files(get_config_path(), "fndds", full.names = TRUE), 
        "vitAMINAE", ignore.case = T, full.names = TRUE), "FNDDSNutVal.tsv", full.names = TRUE), data.table = F), 
        "start.date", "end.date")
    colnames(d)[1] <- "food.code"
    d$nutrient.code <- Recode(d$nutrient.code, "320::vitamin_a_rae_mcg", "323::vitamin_e_as_alpha_tocopherol_mg")
    d <- drop_col(col_rename(dplyr::left_join(drop_col(col_rename(dplyr::left_join(nhs_read(nhs_tsv("drxiff", 
        years = 1999, cat = F), "drdifdcd", "drxigrms", cat = F, Year = F), d[d$nutrient.code %in% "vitamin_a_rae_mcg", 
        ], "food.code"), "nutrient.value:vitamin_a_rae_mcg"), "nutrient.code", "Year"), d[d$nutrient.code %in% 
        "vitamin_e_as_alpha_tocopherol_mg", ], "food.code"), "nutrient.value:vitamin_e_as_alpha_tocopherol_mg"), 
        "nutrient.code", "Year")
    d$vitamin_a_rae_mcg <- d$drxigrms/100 * d$vitamin_a_rae_mcg
    d$vitamin_e_as_alpha_tocopherol_mg <- d$drxigrms/100 * d$vitamin_e_as_alpha_tocopherol_mg
    d <- drop_col(d, "drxigrms")
    var2 <- c("seqn", "line")
    if (VitA) 
        append(var2) <- "vitamin_a_rae_mcg"
    if (VitE) 
        append(var2) <- "vitamin_e_as_alpha_tocopherol_mg"
    d <- d[, var2]
    if (dietary == "iff") {
        return_data(data, d, Year = FALSE, key = c("seqn", "line"), join = "left")
    }
    else if (dietary == "tot") {
        .sum.nona <<- function(x) {
            if (all(is.na(x))) 
                return(NA)
            sum(x, na.rm = TRUE)
        }
        d <- aggregate_sum(data = d, x = colnames(d)[-c(1, 2)], by = "seqn")
        return_data(data, d, Year = FALSE, key = "seqn", join = "left")
    }
}
```

## `wt_dr_day1` [internal]

```r
function (data, wtname = NULL, cat = TRUE) 
{
    dl <- data
    dl2 <- dl[, colnames(dl) %in% c("Year", "wtdrd1", "wtdr4yr")]
    if (ncol(dl2) == 3) 
        dl2$wtdrd1[is.na(dl2$wtdrd1)] <- dl2$wtdr4yr[is.na(dl2$wtdrd1)]
    years1 <- unique(dl[, "Year"])
    years2 <- unique(dl2$Year[!is.na(dl2$wtdrd1)])
    if (length(years1) != length(years2)) {
        if (cat) 
            cat("\nInvalid years cycle:", paste0(set::not(years1, years2), collapse = ", "), "\n\n")
    }
    years <- prepare_years(years2)
    n <- length(years)
    drname <- sprintf("drd1_%syr", n * 2)
    if (!is.null(wtname)) 
        drname <- wtname
    do::exec(paste0("dl$", drname, "<- NA"))
    ck <- c("1999-2000", "2001-2002") %in% years
    if (any(ck)) {
        yeari <- c("1999-2000", "2001-2002")[ck]
        if (sum(ck) == 1) 
            wtdr <- "wtdrd1"
        if (sum(ck) == 2) 
            wtdr <- "wtdr4yr"
        for (i in yeari) {
            dl[dl$Year == i, drname] <- dl[dl$Year == i, wtdr] * sum(ck)/n
        }
        if (cat) 
            cat(crayon::blue(paste0(yeari, collapse = ", ")), paste0(drname, " = ", wtdr, " * ", sum(ck), 
                "/", n))
        if (cat) 
            cat("\n")
    }
    yeari <- set::not(years, c("1999-2000", "2001-2002"))
    if (length(yeari) == 0) 
        return(dl)
    wtdr <- "wtdrd1"
    head = NULL
    if (sum(ck) == 2) 
        head = "           "
    for (i in yeari) {
        dl[dl$Year == i, drname] <- dl[dl$Year == i, wtdr] * 1/n
        if (cat) 
            cat(crayon::blue(paste0(head, i)), paste0(drname, " = ", wtdr, " * ", 1, "/", n), "\n")
    }
    dl
}
```

## `xpt2tsv` [internal]

```r
function (xpt) 
{
    ext <- tools::file_ext(xpt)
    if (ext == "xpt") {
        sas <- haven::read_xpt(xpt)
    }
    else {
        sas <- haven::read_sas(xpt)
    }
    colnames(sas) <- tolower(colnames(sas))
    (tsv <- do::Replace(xpt, paste0("\\.", ext), ".tsv"))
    data.table::fwrite(sas, tsv, sep = "\t")
}
```

## `yes1` [internal]

```r
function (d1) 
{
    ck <- d1 == 1
    d1[ck] <- "yes"
    d1[!ck] <- "no"
    d1
}
```


