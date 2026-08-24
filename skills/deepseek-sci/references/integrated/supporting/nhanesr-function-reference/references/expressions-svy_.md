# Integrated supporting reference: nhanesr-function-reference/references/expressions-svy_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-svy_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `svy_`

## `svy_barplot` [exported]

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

## `svy_count` [exported]

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

## `svy_coxplot` [exported]

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

## `svy_design` [exported]

```r
function (data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") 
UseMethod("svy_design")
```

## `svy_design.data.frame` [internal]

```r
function (data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") 
{
    if (!weights %in% colnames(data)) 
        stop(tmcn::toUTF8("<U+5408><U+5E76><U+6743><U+91CD><U+4E0D><U+53EB>nhs_wt"))
    if (!psu %in% colnames(data)) 
        stop(tmcn::toUTF8("<U+6570><U+636E><U+4E2D><U+6CA1><U+6709>sdmvpsu"))
    if (!strata %in% colnames(data)) 
        stop(tmcn::toUTF8("<U+6570><U+636E><U+4E2D><U+6CA1><U+6709>sdmvstra"))
    if (anyNA(data[, weights])) {
        stop(tmcn::toUTF8("<U+6743><U+91CD><U+4E2D><U+6709><U+7F3A><U+5931><U+503C>,<U+8BF7><U+5148><U+5220><U+9664>"))
    }
    if (any(data[, weights] <= 0)) {
        stop(tmcn::toUTF8("<U+6743><U+91CD><U+4E2D><U+6709><U+6570><U+503C><U+7B49><U+4E8E>0,<U+8BF7><U+5148><U+5220><U+9664>0<U+6743><U+91CD>"))
    }
    if (any("Year" %in% do::left(colnames(data), 4))) {
        wh <- which("Year" %in% do::left(colnames(data), 4))[1]
        if (all(c("2017-2018", "2019-2020") %in% data[, wh])) {
            stop("<U+6570><U+636E><U+4E2D><U+4E0D><U+80FD><U+540C><U+65F6><U+5305><U+542B>2017-2018<U+548C>2019-2020, \n<U+56E0><U+4E3A>2019-2020<U+5176><U+5B9E><U+5C31><U+662F>2017-2020.03<U+FF0C>\n<U+FF0C><U+518D><U+63D0><U+53D6><U+4E00><U+4E2A>2017-2018<U+5C31><U+91CD><U+590D><U+4E86>")
        }
    }
    data <- deparse(substitute(data))
    if (data == "data") 
        stop("<U+6570><U+636E><U+7684><U+540D><U+5B57><U+4E0D><U+8981><U+53EB>data<U+FF0C><U+8BF7><U+6362><U+4E2A><U+540D><U+518D><U+52A0><U+6743>")
    weights <- do::Replace0(deparse(substitute(weights)), "\"")
    psu <- do::Replace0(deparse(substitute(psu)), "\"")
    strata <- do::Replace0(deparse(substitute(strata)), "\"")
    string <- "svydesign(data = %s,weights = ~%s,id = ~%s,strata = ~%s,nest = TRUE,survey.lonely.psu = \"adjust\")"
    txt <- parse(text = sprintf(string, data, weights, psu, strata))
    eval(txt)
}
```

## `svy_design.mids` [internal]

```r
function (data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") 
{
    data..imputation <- paste0(deparse(substitute(data)), "..imputation")
    data <- lapply(1:data$m, function(i) complete(data, action = i))
    d1 <- data[[1]]
    if (!weights %in% colnames(d1)) 
        stop(tmcn::toUTF8("<U+5408><U+5E76><U+6743><U+91CD><U+4E0D><U+53EB>nhs_wt"))
    if (!psu %in% colnames(d1)) 
        stop(tmcn::toUTF8("<U+6570><U+636E><U+4E2D><U+6CA1><U+6709>sdmvpsu"))
    if (!strata %in% colnames(d1)) 
        stop(tmcn::toUTF8("<U+6570><U+636E><U+4E2D><U+6CA1><U+6709>sdmvstra"))
    if (anyNA(d1[, weights])) {
        stop(tmcn::toUTF8("<U+6743><U+91CD><U+4E2D><U+6709><U+7F3A><U+5931><U+503C>,<U+8BF7><U+5148><U+5220><U+9664>"))
    }
    if (any(d1[, weights] <= 0)) {
        stop(tmcn::toUTF8("<U+6743><U+91CD><U+4E2D><U+6709><U+6570><U+503C><U+7B49><U+4E8E>0,<U+8BF7><U+5148><U+5220><U+9664>0<U+6743><U+91CD>"))
    }
    eval(parse(text = sprintf("%s <<- imputationList(data)", data..imputation)))
    weights <- do::Replace0(deparse(substitute(weights)), "\"")
    psu <- do::Replace0(deparse(substitute(psu)), "\"")
    strata <- do::Replace0(deparse(substitute(strata)), "\"")
    string <- "svydesign(data = %s,weights = ~%s,id = ~%s,strata = ~%s,nest = TRUE,survey.lonely.psu = \"adjust\")"
    txt <- parse(text = sprintf(string, data..imputation, weights, psu, strata))
    eval(txt)
}
```

## `svy_kmplot` [exported]

```r
function (x, ...) 
UseMethod("svy_kmplot")
```

## `svy_kmplot.svykm` [internal]

```r
function (x, ci = FALSE, xlab = "Time", ylab = "Survival Probability", pvalue = FALSE, round = 2, margin = c(30, 
    30, 90, 20), risktable = TRUE, freq = T, weighted.prop = T, rt.title.xy = NULL, rt.title = "Risk Table", 
    rt.title.color = "black", rt.title.size = 4, rt.text.y = -0.29999999999999999, color = "black", rt.text.size = 4, 
    ...) 
{
    if (!"varlog" %in% names(x) & ci) {
        sc <- attr(x, "call")
        sc$se <- TRUE
        x <- eval(sc, envir = .GlobalEnv)
    }
    df <- data.frame(time = x$time, surv = x$surv)
    if (ci) {
        df$low = exp(log(x$surv) - 1.96 * sqrt(x$varlog))
        df$high = exp(log(x$surv) + 1.96 * sqrt(x$varlog))
        df$high[df$high > 1] <- 1
    }
    p <- ggplot(df) + geom_line(aes(time, surv))
    if (ci) 
        p <- p + geom_line(aes(time, low), linetype = 2) + geom_line(aes(time, high), linetype = 2)
    p <- p + theme_classic() + xlab(xlab) + ylab(ylab)
    if (risktable) {
        xy <- ggplot_build(p)$data[[1]][, c("x", "y")]
        xbreak <- do::unique_no.NA(ggplot_build(p)$layout$panel_params[[1]]$x.sec$breaks)
        if (freq) {
            sc <- attr(x, "call")
            sc[[1]] <- quote(survival::survfit)
            scdata <- eval(sc$design)$variables
            sc$data <- quote(scdata)
            sc$design <- NULL
            rt.frq <- eval(sc)
            freq.n <- sapply(xbreak, function(i) {
                ii <- rt.frq$n.risk[rt.frq$time %in% i]
                if (length(ii) == 0) {
                  ii <- rt.frq$n.risk[which.min(abs(rt.frq$time - i))[1]]
                }
                ii
            })
        }
        if (weighted.prop) {
            y0 <- sapply(xbreak, function(i) {
                if (i %in% xy$x) {
                  xy$y[xy$x %in% i][1]
                }
                else {
                  xy$y[which.min(abs(xy$x - i))[1]]
                }
            })
            wt.prop <- round(y0 * 100, round)
        }
        if (freq & weighted.prop) {
            y <- sprintf("%s(%s)", freq.n, wt.prop)
        }
        else if (freq) {
            y <- freq.n
        }
        else if (weighted.prop) {
            y <- wt.prop
        }
        else {
            y <- "no"
        }
        p$theme$plot.margin <- unit(margin, "points")
        p
        if (is.null(rt.title.xy)) 
            rt.title.xy = c(mean(xbreak[1:2]), -0.20000000000000001)
        p <- p + annotate("text", x = rt.title.xy[1], y = rt.title.xy[2], label = rt.title, color = rt.title.color, 
            size = rt.title.size) + annotate("text", x = xbreak, label = y, y = rt.text.y, color = color, 
            size = rt.text.size) + coord_cartesian(ylim = c(0, 1), clip = "off")
    }
    p
}
```

## `svy_kmplot.svykmlist` [internal]

```r
function (x, ci = FALSE, xlab = "Time", ylab = "Survival Probability", round = 3, pvalue = TRUE, pvalue.xy = NULL, 
    pvalue.size = 4, xlim = NULL, ylim = NULL, xbreaks = waiver(), ybreaks = waiver(), line.width = 0.69999999999999996, 
    axis.line.width = 0.59999999999999998, axis.ticks.length = 0.14999999999999999, axis.ticks.with = 0.59999999999999998, 
    axis.text.size = 10, axis.title = 12, margin = c(30, 30, 90, 20), legend.title = NULL, legend.position = "right", 
    legend.title.size = 13, legend.text.size = 10, risktable = TRUE, freq = T, weighted.prop = T, rt.title.xy = NULL, 
    rt.title = "Risk Table", rt.title.color = "black", rt.title.size = 4, rt.text.y = NULL, color = NULL, 
    rt.text.size = 4, ...) 
{
    round0 <- round
    if (!"varlog" %in% names(x[[1]]) & ci) {
        sc <- attr(x, "call")
        sc$se <- TRUE
        x <- eval(sc, envir = .GlobalEnv)
    }
    (var.x <- do::select(all.vars(attributes(x)$call$formula), -c(1, 2)))
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
    colnames(df)[1] <- var.x
    head(df)
    tail(df)
    p <- ggplot(data = unique(df[, c(var.x, "time", "surv")])) + geom_line(aes_string("time", "surv", 
        group = var.x, color = var.x), size = line.width)
    if (!is.null(color)) 
        p <- p + scale_colour_manual(values = color)
    if (is.null(ylim)) 
        ylim <- ggplot_build(p)$layout$panel_params[[1]]$y.sec$limits
    legend.color <- data.frame(colours = unique(ggplot_build(p)$data[[1]]["colour"]), label = ggplot_build(p)$plot$scales$scales[[1]]$get_labels())
    if (ci) 
        p <- p + geom_polygon(data = df, aes_string("time", "ci", group = var.x, fill = var.x), alpha = 0.20000000000000001)
    p <- p + theme_classic() + labs(color = ifelse(is.null(legend.title), var.x, legend.title)) + xlab(xlab) + 
        ylab(ylab) + scale_x_continuous(limits = xlim, breaks = xbreaks) + scale_y_continuous(limits = ylim, 
        breaks = ybreaks)
    p <- p + theme(axis.line = element_line(size = axis.line.width), axis.ticks.length = unit(axis.ticks.length, 
        "cm"), axis.ticks = element_line(size = axis.ticks.with), axis.text = element_text(size = axis.text.size), 
        axis.title = element_text(size = axis.title), legend.title = element_text(size = legend.title.size), 
        legend.text = element_text(size = legend.text.size), legend.position = legend.position, legend.background = element_blank())
    p
    if (!isFALSE(pvalue) & length(x) > 1) {
        if (isTRUE(pvalue)) {
            f <- attributes(x)$call
            f[[1]] <- quote(svylogrank)
            f$se <- NULL
            f$method = "small"
            pv <- suppressWarnings(tryCatch(eval(f, envir = .GlobalEnv)[[2]]["p"], error = function(e) "e"))
            if (pv == "e") {
                f$method = "large"
                pv <- suppressWarnings(tryCatch(eval(f, envir = .GlobalEnv)[[1]]["p"], error = function(e) "e"))
            }
            if (pv == "e") {
                f$method = "score"
                pv <- suppressWarnings(tryCatch(eval(f, envir = .GlobalEnv)["p"], error = function(e) "e"))
            }
            if (pv < 0.0001) {
                pv <- "<0.0001"
            }
            else if (pv < 0.001) {
                pv <- "<0.001"
            }
            else if (pv == "e") {
                pv <- "error"
            }
            else {
                (pv0 <- round(pv, round0))
                while (pv0 == 0) {
                  round0 = round0 + 1
                  pv0 <- round(pv, round0)
                }
                pv <- pv0
            }
            pv <- paste0("p:", pv)
        }
        else {
            pv = pvalue
        }
        xsec <- ggplot_build(p)$layout$panel_params[[1]]$x.sec$minor_breaks[2]
        ysec <- ggplot_build(p)$layout$panel_params[[1]]$y.sec$minor_breaks[2]
        if (is.null(pvalue.xy)) 
            pvalue.xy <- c(xsec, ysec)
        p <- p + annotate(geom = "text", x = pvalue.xy[1], y = pvalue.xy[2], label = pv, size = pvalue.size)
    }
    p
    if (risktable) {
        xy <- drop_col(dplyr::left_join(ggplot_build(p)$data[[1]][, c("x", "y", "colour")], legend.color, 
            "colour"), "colour")
        (xbreak <- do::unique_no.NA(ggplot_build(p)$layout$panel_params[[1]]$x.sec$breaks))
        (sc <- attr(x, "call"))
        sc[[1]] <- quote(survival::survfit)
        (scdata <- eval(sc$design)$variables)
        sc$data <- quote(scdata)
        sc$design <- NULL
        (rt.frq <- eval(sc))
        (group <- do::Replace0(names(rt.frq[["strata"]]), paste0(var.x, "=")))
        (frq.data <- data.frame(x = rt.frq$time, y = rt.frq$n.risk, event = rt.frq$n.event, label = rep(group, 
            rt.frq[["strata"]])))
        (freq.n <- do.call(lapply(xbreak, function(i) {
            do.call(lapply(unique(frq.data$label), function(j) {
                (dfj <- frq.data[frq.data$label %in% j, ])
                if (i %in% dfj$x) {
                  dfj <- unique(dfj[dfj$x %in% i, ])
                }
                else {
                  dfj <- unique(dfj[which.min(abs(dfj$x - i))[1], ])
                }
                dfj[, "x"] <- i
                dfj
            }), what = rbind)
        }), what = rbind))
        (y0 <- do.call(lapply(xbreak, function(i) {
            do.call(lapply(unique(xy$label), function(j) {
                dfj <- xy[xy$label %in% j, ]
                if (i %in% dfj$x) {
                  dfj <- unique(dfj[which(dfj$x %in% i)[1], ])
                }
                else {
                  dfj <- unique(dfj[which.min(abs(dfj$x - i))[1], ])
                }
                dfj[, "x"] <- i
                dfj
            }), what = rbind)
        }), what = rbind))
        y0$y <- digit2character(y0$y * 100, round)
        if (freq & weighted.prop) {
            y <- dplyr::full_join(freq.n, y0, c("x", "label"))
            y$y <- sprintf("%s(%s)", y$y.x, y$y.y)
            y <- y[, c("x", "label", "y")]
        }
        else if (freq) {
            y <- freq.n
        }
        else if (weighted.prop) {
            y <- y0
        }
        else {
            y <- "no"
        }
        y$y <- do::reverse(do::equal_length(do::reverse(y$y)))
        p$theme$plot.margin <- unit(margin, "points")
        p2 <- p
        ybreak <- do::unique_no.NA(ggplot_build(p)$layout$panel_params[[1]]$y.sec$breaks)
        if (is.null(rt.title.xy)) {
            y_contineous <- do::unique_no.NA(ggplot_build(p)$layout$panel_params[[1]]$y.sec$breaks)[1]
            y_dif <- diff(ggplot_build(p)$layout$panel_params[[1]]$y.sec$minor_breaks[1:2]) * 2.2999999999999998
            rt.title.xy <- c(mean(xbreak[1:2]), y_contineous - y_dif)
        }
        p <- suppressMessages(p + scale_y_continuous(limits = NULL))
        p <- p + annotate("text", x = rt.title.xy[1], y = rt.title.xy[2], label = rt.title, color = rt.title.color, 
            size = rt.title.size)
        if (is.null(rt.text.y)) 
            rt.text.y = sapply(1:length(legend.color$label), function(i) {
                if (i == 1) {
                  ybreak[1] - 1.5 * diff(ybreak[1:2])
                }
                else {
                  ybreak[1] - 1.5 * diff(ybreak[1:2]) - diff(ybreak[1:2])/2 * (i - 1)
                }
            })
        string <- sprintf(paste0(sapply(legend.color$label, function(i) {
            sprintf("annotate('text',\n                     x=xbreak,\n                     label=y$y[y$label == '%s'],\n                     y = %s,\n                     color='%s',\n                     size=rt.text.size)", 
                i, rt.text.y[legend.color$label == i], legend.color$colour[legend.color$label == i])
        }), collapse = "+\n "), fmt = "p + %s")
        p <- eval(parse(text = string)) + coord_cartesian(clip = "off", ylim = ylim)
    }
    p
}
```

## `svy_mean` [exported]

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

## `svy_missValue` [exported]

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

## `svy_population` [exported]

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

## `svy_quantile` [exported]

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

## `svy_reg_lm` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T) 
{
    fit0 <- fit
    ck1 <- any(is.infinite(confint(fit)))
    ck2 <- any(is.nan(confint(fit)))
    ck <- ck1 | ck2
    if (ck) {
        cfint <- confint(fit, ddf = survey::degf(fit$survey.design))
    }
    else {
        cfint <- confint(fit)
    }
    if (fit[["df.residual"]] <= 0) {
        fit <- summary(fit, df = survey::degf(fit$survey.design))
    }
    else {
        fit <- summary(fit)
    }
    coef <- as.data.frame(fit$coefficients, check.names = F)
    tb <- coef[!row.names(coef) %in% "(Intercept)", ]
    p <- grepl("pr\\(", colnames(tb), T)
    for (ii in 1:nrow(tb)) {
        if (!is.na(tb[ii, p])) {
            if (as.numeric(tb[ii, p]) < 0.0001) {
                pr <- "<0.0001"
            }
            else if (as.numeric(tb[ii, p]) < 0.001) {
                pr <- "<0.001"
            }
            else {
                prck <- TRUE
                round0 <- round
                while (prck) {
                  pr <- digit2character(as.numeric(tb[ii, p]), round0)
                  if (as.numeric(pr) == 0) {
                    round0 <- round0 + 1
                  }
                  else {
                    prck <- F
                  }
                }
            }
            tb[ii, p] <- pr
        }
    }
    tb$low <- cfint[!row.names(cfint) %in% "(Intercept)", 1]
    tb$high <- cfint[!row.names(cfint) %in% "(Intercept)", 2]
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(tb[, 1], "(", tb$low, ",", tb$high, ")")
    tb <- drop_col(tb, "low", "high")
    tb
    if (style == 0) 
        return(tb)
    if (is.null(x)) {
        x <- unique(c(do::model.x(fit0), row.names(tb)))
        if (length(fit0$xlevels) > 0) {
            ex <- unique(do.call(lapply(1:length(fit0$xlevels), function(ii) {
                paste0(names(fit0$xlevels)[ii], fit0$xlevels[[ii]])
            }), what = c))
            x <- set::not(x, ex)
        }
    }
    (parms <- names(fit0$xlevels))
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% parms) {
            (cat <- paste0(x[i], fit0$xlevels[[x[i]]]))
            if (all(cat %in% rownames(tb))) {
                resi <- tb[cat, ]
            }
            else if (any(cat %in% rownames(tb))) {
                resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                  NULL))), colnames(tb)), tb[cat[-1], ])
            }
            else {
                (next)(i)
            }
            if (style == 1) {
                res <- rbind(res, resi)
            }
            else if (style == 2) {
                res1 <- resi[1, ]
                res1[] <- ""
                row.names(res1) <- x[i]
                row.names(resi) <- paste0("    ", do::knife_left(row.names(resi), nchar(x[i])))
                resi <- rbind(res1, resi)
                resi <- cbind(character = row.names(resi), resi)
                row.names(resi) <- NULL
                res <- rbind(res, resi)
            }
        }
        else if (x[i] %in% row.names(tb)) {
            if (!is.na(tb[x[i], 1])) {
                resi <- tb[x[i], ]
                resi <- cbind(character = row.names(resi), resi)
                row.names(resi) <- NULL
                res <- rbind(res, resi)
            }
        }
    }
    res <- res[nchar(do::Replace0(res$character, " ")) > 0, ]
    if (view) 
        nhs_view.regtable(res)
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit0
    invisible(res)
}
```

## `svy_reg_logistic` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T) 
{
    fit0 <- fit
    ck1 <- any(is.infinite(confint(fit)))
    ck2 <- any(is.nan(confint(fit)))
    ck <- ck1 | ck2
    if (ck) {
        cfint <- exp(confint(fit, ddf = survey::degf(fit$survey.design)))
    }
    else {
        cfint <- exp(confint(fit))
    }
    if (fit[["df.residual"]] <= 0) {
        fit <- summary(fit, df = survey::degf(fit$survey.design))
    }
    else {
        fit <- summary(fit)
    }
    coef <- as.data.frame(fit$coefficients, check.names = F)
    res <- coef[!row.names(coef) %in% "(Intercept)", ]
    (p <- grepl("pr\\(", colnames(res), T))
    for (ii in 1:nrow(res)) {
        if (as.numeric(res[ii, p]) < 0.0001) {
            pr <- "<0.0001"
        }
        else if (as.numeric(res[ii, p]) < 0.001) {
            pr <- "<0.001"
        }
        else {
            prck <- TRUE
            round0 <- round
            while (prck) {
                pr <- digit2character(as.numeric(res[ii, p]), round0)
                if (as.numeric(pr) == 0) {
                  round0 <- round0 + 1
                }
                else {
                  prck <- F
                }
            }
        }
        res[ii, p] <- pr
    }
    res$OR <- exp(res[, 1])
    res$low <- cfint[!row.names(cfint) %in% "(Intercept)", 1]
    res$high <- cfint[!row.names(cfint) %in% "(Intercept)", 2]
    digit2numeric(res) <- round
    digit2character(res$low) <- round
    digit2character(res$high) <- round
    res$"95% CI" <- paste0(digit2character(res$OR, round), "(", res$low, ",", res$high, ")")
    tb <- drop_col(res, "low", "high")
    tb
    if (style == 0) 
        return(tb)
    if (is.null(x)) {
        x <- unique(c(do::model.x(fit0), row.names(tb)))
        if (length(fit0$xlevels) > 0) {
            ex <- unique(do.call(lapply(1:length(fit0$xlevels), function(ii) {
                paste0(names(fit0$xlevels)[ii], fit0$xlevels[[ii]])
            }), what = c))
            x <- set::not(x, ex)
        }
    }
    (parms <- names(fit0$xlevels))
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% parms) {
            (cat <- paste0(x[i], fit0$xlevels[[x[i]]]))
            if (all(cat %in% rownames(tb))) {
                resi <- tb[cat, ]
            }
            else if (any(cat %in% rownames(tb))) {
                resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                  NULL))), colnames(tb)), tb[cat[-1], ])
            }
            else {
                (next)(i)
            }
            if (style == 1) {
                res <- rbind(res, resi)
            }
            else if (style == 2) {
                res1 <- resi[1, ]
                res1[] <- ""
                row.names(res1) <- x[i]
                row.names(resi) <- paste0("    ", do::knife_left(row.names(resi), nchar(x[i])))
                resi <- rbind(res1, resi)
                resi <- cbind(character = row.names(resi), resi)
                row.names(resi) <- NULL
                res <- rbind(res, resi)
            }
        }
        else if (x[i] %in% row.names(tb)) {
            if (!is.na(tb[x[i], 1])) {
                resi <- tb[x[i], ]
                resi <- cbind(character = row.names(resi), resi)
                row.names(resi) <- NULL
                res <- rbind(res, resi)
            }
        }
    }
    res <- res[nchar(do::Replace0(res$character, " ")) > 0, ]
    if (view) 
        nhs_view.regtable(res)
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit0
    invisible(res)
}
```

## `svy_roc` [exported]

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

## `svy_roc_plot` [exported]

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

## `svy_tableone` [exported]

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

## `svy_uv.cox` [exported]

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

## `svy_uv.glm` [exported]

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

## `svy_uv.logit` [exported]

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


