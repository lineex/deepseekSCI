# Integrated supporting reference: nhanesr-function-reference/references/expressions-RCS.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-RCS.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `RCS`

## `RCS` [exported]

```r
function (..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.94999999999999996, ref.zero = TRUE, 
    log = TRUE) 
UseMethod("RCS")
```

## `RCS.default` [internal]

```r
function (..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.94999999999999996, ref.zero = TRUE, 
    log = TRUE) 
{
    if (is.character(reference)) {
        if (!all(reference %in% c("median"))) {
            stop("reference must be numeric or median(defult)")
        }
    }
    fit2 <- list(...)
    for (i in 1:length(fit2)) {
        if ("svytableone" %in% class(fit2[[i]])) {
            fit2[[i]] <- attr(fit2[[i]], "fit")
        }
    }
    modelname2 <- do::get_names(...)
    old <- options()
    if (is.null(by)) {
        x <- do.call(lapply(1:length(fit2), function(i) {
            svy <- svy2rms(fit2[[i]])
            fiti <- svy[[1]]
            di <- svy[[2]]
            rcsx <- rcsx(fiti)
            dd <- suppressWarnings(rms::datadist(di))
            options(datadist = dd)
            fiti <- suppressWarnings(update(fiti, data = di))
            optk <- getKnot(fiti)
            nkmethod <- "take in"
            if (!is.null(nknots)) {
                if (length(nknots) == 1) 
                  optk = nkonts
                if (length(nknots) > 1) 
                  optk <- nknots[i]
                if (is.na(optk)) {
                  if (do::cnOS()) 
                    stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                      length(fit2)))
                }
                fiti <- updateKnot(fiti, optk)
                nkmethod <- "you specify"
            }
            Nonlinear <- anova(fiti)[" Nonlinear", "P"]
            pOvarAll <- anova(fiti)[which(row.names(anova(fiti)) == " Nonlinear") - 1, "P"]
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            if (length(reference) == 1) 
                ref <- reference
            if (length(reference) > 1) 
                ref <- reference[i]
            if (is.na(ref)) {
                if (do::cnOS()) 
                  stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                if (do::cnOS()) 
                  stop("The number of references is inconsistent with the number of models")
            }
            if (ref == "median") {
                referenceString <- paste0(rcsx, " reference: median (", dd$limits["Adjust to", rcsx], 
                  ")")
                ref <- dd$limits["Adjust to", rcsx][1]
            }
            else if (is.numeric(ref)) {
                setReference(rcsx, ref)
                referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
            }
            cat("\n     nknots: ", optk, "(", nkmethod, ")", " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", 
                round(Nonlinear, 4), ")")
            cat("\n    ", referenceString)
            fiti <- suppressWarnings(update(fiti))
            method <- deparse(fiti$call[[1]])
            if (method == "ols") {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
                log = FALSE
            }
            else {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,fun=exp,ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
                if (log) {
                  x$yhat <- log(x$yhat)
                  x$lower <- log(x$lower)
                  x$upper <- log(x$upper)
                }
            }
            x$modelName <- modelname2[i]
            x$rcsName <- rcsx
            x$method <- method
            x$Ref <- ref
            class(x) <- "data.frame"
            x
        }), what = plyr::rbind.fill)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(paste0("m", mn), "data.frame")
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "predicted value"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
    else {
        (by2 <- paste0(by, collapse = " - "))
        ev <- new.env()
        ev$level <- NULL
        x <- do.call(lapply(1:length(fit2), function(i) {
            fiti <- fit2[[i]]
            rcsx <- rcsx(fiti)
            di <- model.data(fiti)[, c(all.vars(fiti$terms), by)]
            dd <- suppressWarnings(rms::datadist(di))
            options(datadist = dd)
            fiti <- update(fiti, data = di)
            if (length(by) == 1) 
                bycat = di[, by]
            else bycat = do::paste0_columns(di[, by], ";;;")
            byu <- unique(bycat)
            byu <- as.character(byu[!is.na(byu)])
            if (!is.null(levels(bycat))) 
                byu <- levels(bycat)[levels(bycat) %in% byu]
            if (is.null(ev$level)) {
                ev$level <- byu
            }
            else {
                ev$level <- unique(c(ev$level, byu))
            }
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            r <- do.call(lapply(1:length(byu), function(ki) {
                k <- byu[ki]
                dsub <- di[bycat == k, ]
                dd <- suppressWarnings(rms::datadist(dsub))
                options(datadist = dd)
                ei <- eval(parse(text = sprintf("update(fiti,formula. = .~. - %s, data=dsub)", by2)))
                optk <- getKnot(ei)
                if (!is.null(nknots)) {
                  if (length(nknots) == 1) 
                    optk <- nknots
                  if (length(nknots) > 1) 
                    optk <- nknots[length(byu) * (i - 1) + ki]
                  if (is.na(optk)) {
                    if (do::cnOS()) 
                      stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                        length(fit2)))
                  }
                  ei <- updateKnot(ei, optk, data = dsub)
                }
                Nonlinear <- anova(ei)[" Nonlinear", "P"]
                pOvarAll <- anova(ei)[which(row.names(anova(ei)) == " Nonlinear") - 1, "P"]
                if (length(reference) == 1) 
                  ref <- reference
                if (length(reference) > 1) 
                  ref <- reference[(i - 1) * ki + ki]
                if (is.na(ref)) {
                  if (do::cnOS()) 
                    stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                  if (do::cnOS()) 
                    stop("The number of references is inconsistent with the number of models")
                }
                if (ref == "median") {
                  ref <- dd$limits["Adjust to", rcsx]
                  referenceString <- paste0(rcsx, " reference: median (", ref, ")")
                }
                else if (is.numeric(ref)) {
                  setReference(rcsx, ref)
                  referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
                }
                cat(crayon::blue("\n", "group: ", by, "==", k))
                cat("\n     nknots: ", " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", round(Nonlinear, 
                  4), ")")
                cat("\n     ", referenceString)
                cat("\n     ", do::Replace(paste0(deparse(ei$call$formula), collapse = ""), " {2,}", 
                  " "))
                ei <- update(ei)
                method <- deparse(ei$call[[1]])
                if (method == "ols") {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                }
                else {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,fun=exp,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                }
                x$modelName <- modelname2[i]
                x$rcsName <- rcsx
                x$method <- method
                class(x) <- "data.frame"
                x <- cbind(x, do::col_split(k, ";;;", colnames = by))
                x$Ref <- ref
                x
            }), what = rbind)
        }), what = rbind)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        for (i in 1:length(by)) {
            x[, by[i]] <- factor(x[, by[i]], levels = unique(do::col_split(ev$level, ";;;")[, i]))
        }
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(sprintf("m%sby", mn), "data.frame")
        attr(x, "by") <- by
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "beta"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
}
```

## `RCS.svycoxph` [internal]

```r
function (..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.94999999999999996, ref.zero = TRUE, 
    log = TRUE) 
{
    if (is.character(reference)) {
        if (!all(reference %in% c("median"))) {
            stop("reference must be numeric or median(defult)")
        }
    }
    fit2 <- list(...)
    modelname2 <- do::get_names(...)
    old <- options()
    if (is.null(by)) {
        x <- do.call(lapply(1:length(fit2), function(i) {
            svy <- svy2rms(fit2[[i]])
            fiti <- svy[[1]]
            di <- svy[[2]]
            rcsx <- rcsx(fiti)
            dd <- suppressWarnings(rms::datadist(di))
            options(datadist = dd)
            fiti <- suppressWarnings(update(fiti, data = di))
            optk <- getKnot(fiti)
            nkmethod <- "take in"
            if (!is.null(nknots)) {
                if (length(nknots) == 1) 
                  optk = nknots
                if (length(nknots) > 1) 
                  optk <- nknots[i]
                if (is.na(optk)) {
                  if (do::cnOS()) 
                    stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                      length(fit2)))
                }
                fiti <- updateKnot(fiti, optk, data = di)
                nkmethod <- "you specify"
            }
            Nonlinear <- anova(fiti)[" Nonlinear", "P"]
            pOvarAll <- anova(fiti)[which(row.names(anova(fiti)) == " Nonlinear") - 1, "P"]
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            if (length(reference) == 1) 
                ref <- reference
            if (length(reference) > 1) 
                ref <- reference[i]
            if (is.na(ref)) {
                if (do::cnOS()) 
                  stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                if (do::cnOS()) 
                  stop("The number of references is inconsistent with the number of models")
            }
            if (ref == "median") {
                referenceString <- paste0(rcsx, " reference: median (", dd$limits["Adjust to", rcsx], 
                  ")")
                ref <- dd$limits["Adjust to", rcsx][1]
            }
            else if (is.numeric(ref)) {
                setReference(rcsx, ref)
                referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
            }
            cat("\n     nknots: ", optk, "(", nkmethod, ")", " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", 
                round(Nonlinear, 4), ")")
            cat("\n    ", referenceString)
            fiti <- suppressWarnings(update(fiti))
            method <- deparse(fiti$call[[1]])
            if (method == "ols") {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
            }
            else {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,fun=exp,ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
                if (log) {
                  x$yhat <- log(x$yhat)
                  x$lower <- log(x$lower)
                  x$upper <- log(x$upper)
                }
            }
            x$modelName <- modelname2[i]
            x$rcsName <- rcsx
            x$method <- method
            x$Ref <- ref
            class(x) <- "data.frame"
            x
        }), what = plyr::rbind.fill)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(paste0("m", mn), "data.frame")
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "predicted value"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
    else {
        by2 <- paste0(by, collapse = " - ")
        ev <- new.env()
        ev$level <- NULL
        x <- do.call(lapply(1:length(fit2), function(i) {
            svy <- svy2rms(fit2[[i]], by = by)
            fiti <- svy[[1]]
            rcsx <- rcsx(fiti)
            di <- svy[[2]]
            options(datadist = suppressWarnings(rms::datadist(di)))
            fiti <- update(fiti, data = di)
            if (length(by) == 1) 
                bycat = di[, by]
            else bycat = do::paste0_columns(di[, by], ";;;")
            byu <- unique(bycat)
            byu <- as.character(byu[!is.na(byu)])
            if (!is.null(levels(bycat))) 
                byu <- levels(bycat)[levels(bycat) %in% byu]
            if (is.null(ev$level)) {
                ev$level <- byu
            }
            else {
                ev$level <- unique(c(ev$level, byu))
            }
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            r <- do.call(lapply(1:length(byu), function(ki) {
                k <- byu[ki]
                dsub <- di[bycat == k, ] %>% drop_col(by)
                dd <- suppressWarnings(rms::datadist(dsub))
                options(datadist = dd)
                ei <- eval(parse(text = sprintf("update(fiti,formula. = .~. - %s, data=dsub)", by2)))
                optk <- getKnot(ei)
                if (!is.null(nknots)) {
                  if (length(nknots) == 1) 
                    optk <- nknots
                  if (length(nknots) > 1) 
                    optk <- nknots[length(byu) * (i - 1) + ki]
                  if (is.na(optk)) {
                    if (do::cnOS()) 
                      stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                        length(fit2)))
                  }
                  ei <- updateKnot(ei, optk, data = dsub)
                }
                ea <- anova(ei)
                Nonlinear <- anova(ei)[" Nonlinear", "P"]
                pOvarAll <- anova(ei)[which(row.names(anova(ei)) == " Nonlinear") - 1, "P"]
                if (length(reference) == 1) 
                  ref <- reference
                if (length(reference) > 1) 
                  ref <- reference[(i - 1) * ki + ki]
                if (is.na(ref)) {
                  if (do::cnOS()) 
                    stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                  if (do::cnOS()) 
                    stop("The number of references is inconsistent with the number of models")
                }
                if (ref == "median") {
                  ref <- dd$limits["Adjust to", rcsx]
                  referenceString <- paste0(rcsx, " reference: median (", ref, ")")
                }
                else if (is.numeric(ref)) {
                  setReference(rcsx, ref)
                  referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
                }
                cat(crayon::blue("\n", "group: ", by, "==", k))
                cat("\n     nknots: ", " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", round(Nonlinear, 
                  4), ")")
                cat("\n    ", referenceString)
                cat("\n     ", do::Replace(paste0(deparse(ei$call$formula), collapse = ""), " {2,}", 
                  " "))
                ei <- update(ei)
                method <- deparse(ei$call[[1]])
                if (method == "ols") {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                }
                else {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,fun=exp,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                  if (log) {
                    x$yhat <- log(x$yhat)
                    x$lower <- log(x$lower)
                    x$upper <- log(x$upper)
                  }
                }
                x$modelName <- modelname2[i]
                x$rcsName <- rcsx
                x$method <- method
                class(x) <- "data.frame"
                x <- cbind(x, do::col_split(k, ";;;", colnames = by))
                x$Ref <- ref
                x
            }), what = rbind)
        }), what = rbind)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        for (i in 1:length(by)) {
            x[, by[i]] <- factor(x[, by[i]], levels = unique(do::col_split(ev$level, ";;;")[, i]))
        }
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(sprintf("m%sby", mn), "data.frame")
        attr(x, "by") <- by
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "beta"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
}
```

## `RCS.svyglm` [internal]

```r
function (..., nknots = NULL, reference = "median", by = NULL, conf.int = 0.94999999999999996, ref.zero = TRUE, 
    log = TRUE) 
{
    if (is.character(reference)) {
        if (!all(reference %in% c("median"))) {
            stop("reference must be numeric or median(defult)")
        }
    }
    fit2 <- list(...)
    modelname2 <- do::get_names(...)
    old <- options()
    if (is.null(by)) {
        x <- do.call(lapply(1:length(fit2), function(i) {
            svy <- svy2rms(fit = fit2[[i]])
            (fiti <- svy[[1]])
            (di <- svy[[2]])
            (rcsx <- rcsx(fiti))
            dd <- suppressWarnings(rms::datadist(di))
            options(datadist = dd)
            fiti <- suppressWarnings(update(fiti, data = di))
            (optk <- getKnot(fiti))
            nkmethod <- "take in"
            if (!is.null(nknots)) {
                if (length(nknots) == 1) 
                  optk = nknots
                if (length(nknots) > 1) 
                  optk <- nknots[i]
                if (is.na(optk)) {
                  if (do::cnOS()) 
                    stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                      length(fit2)))
                }
                fiti <- updateKnot(fiti, optk, data = di)
                nkmethod <- "you specify"
            }
            Nonlinear <- anova(fiti)[" Nonlinear", "P"]
            pOvarAll <- anova(fiti)[which(row.names(anova(fiti)) == " Nonlinear") - 1, "P"]
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            if (length(reference) == 1) 
                ref <- reference
            if (length(reference) > 1) 
                ref <- reference[i]
            if (is.na(ref)) {
                if (do::cnOS()) 
                  stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                if (do::cnOS()) 
                  stop("The number of references is inconsistent with the number of models")
            }
            if (ref == "median") {
                referenceString <- paste0(rcsx, " reference: median (", dd$limits["Adjust to", rcsx], 
                  ")")
                ref <- dd$limits["Adjust to", rcsx][1]
            }
            else if (is.numeric(ref)) {
                setReference(rcsx, ref)
                referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
            }
            cat("\n     nknots: ", optk, "(", nkmethod, ")", " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", 
                round(Nonlinear, 4), ")")
            cat("\n    ", referenceString)
            fiti <- suppressWarnings(update(fiti))
            method <- deparse(fiti$call[[1]])
            if (method == "ols") {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,\n                                             ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
                log = FALSE
            }
            else {
                x <- eval(parse(text = sprintf(fmt = "Predict(fiti,%s,fun=exp,\n                                             ref.zero=ref.zero,conf.int=conf.int)", 
                  rcsx)))
                if (log) {
                  x$yhat <- log(x$yhat)
                  x$lower <- log(x$lower)
                  x$upper <- log(x$upper)
                }
            }
            x$modelName <- modelname2[i]
            x$rcsName <- rcsx
            x$method <- method
            x$Ref <- ref
            class(x) <- "data.frame"
            x
        }), what = plyr::rbind.fill)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(paste0("m", mn), "data.frame")
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "predicted value"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
    else {
        by2 <- paste0(by, collapse = " - ")
        ev <- new.env()
        ev$level <- NULL
        x <- do.call(lapply(1:length(fit2), function(i) {
            svy <- svy2rms(fit2[[i]], by = by)
            fiti <- svy[[1]]
            rcsx <- rcsx(fiti)
            di <- svy[[2]]
            options(datadist = suppressWarnings(rms::datadist(di)))
            fiti <- update(fiti, data = di)
            if (length(by) == 1) 
                bycat = di[, by]
            else bycat = do::paste0_columns(di[, by], ";;;")
            byu <- unique(bycat)
            byu <- as.character(byu[!is.na(byu)])
            if (!is.null(levels(bycat))) 
                byu <- levels(bycat)[levels(bycat) %in% byu]
            if (is.null(ev$level)) {
                ev$level <- byu
            }
            else {
                ev$level <- unique(c(ev$level, byu))
            }
            cat("\n")
            cat(crayon::red("########## model: ", modelname2[i], " ##########"))
            r <- do.call(lapply(1:length(byu), function(ki) {
                k <- byu[ki]
                dsub <- di[bycat == k, ]
                dd <- suppressWarnings(rms::datadist(dsub))
                options(datadist = dd)
                ei <- eval(parse(text = sprintf("update(fiti,formula. = .~. - %s, data=dsub)", by2)))
                optk <- getKnot(ei)
                if (!is.null(nknots)) {
                  if (length(nknots) == 1) 
                    optk <- nknots
                  if (length(nknots) > 1) 
                    optk <- nknots[length(byu) * (i - 1) + ki]
                  if (is.na(optk)) {
                    if (do::cnOS()) 
                      stop(sprintf("nknots<U+4E2A><U+6570>(%s)", length(nknots)), sprintf("<U+548C><U+6A21><U+578B><U+4E2A><U+6570>(%s)<U+4E0D><U+4E00><U+81F4>", 
                        length(fit2)))
                  }
                  ei <- updateKnot(ei, optk, data = dsub)
                }
                Nonlinear <- anova(ei)[" Nonlinear", "P"]
                pOvarAll <- anova(ei)[which(row.names(anova(ei)) == " Nonlinear") - 1, "P"]
                if (length(reference) == 1) 
                  ref <- reference
                if (length(reference) > 1) 
                  ref <- reference[(i - 1) * ki + ki]
                if (is.na(ref)) {
                  if (do::cnOS()) 
                    stop("reference<U+4E2A><U+6570><U+548C><U+6A21><U+578B><U+4E2A><U+6570><U+4E0D><U+4E00><U+81F4>")
                  if (do::cnOS()) 
                    stop("The number of references is inconsistent with the number of models")
                }
                if (ref == "median") {
                  ref <- dd$limits["Adjust to", rcsx]
                  referenceString <- paste0(rcsx, " reference: median (", ref, ")")
                }
                else if (is.numeric(ref)) {
                  setReference(rcsx, ref)
                  referenceString <- paste0(rcsx, " reference: you specify (", ref, ")")
                }
                cat(crayon::blue("\n", "group: ", by, "==", k))
                cat("\n     nknots: ", optk, " (P ovarall:", round(pOvarAll, 4), "; NL-Pvalue:", round(Nonlinear, 
                  4), ")")
                cat("\n    ", referenceString)
                cat("\n     ", do::Replace(paste0(deparse(ei$call$formula), collapse = ""), " {2,}", 
                  " "))
                ei <- update(ei)
                method <- deparse(ei$call[[1]])
                if (method == "ols") {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                }
                else {
                  x <- eval(parse(text = sprintf(fmt = "Predict(ei,%s,fun=exp,ref.zero=ref.zero,conf.int=conf.int)", 
                    rcsx)))
                  if (log) {
                    x$yhat <- log(x$yhat)
                    x$lower <- log(x$lower)
                    x$upper <- log(x$upper)
                  }
                }
                x$modelName <- modelname2[i]
                x$rcsName <- rcsx
                x$method <- method
                class(x) <- "data.frame"
                x <- cbind(x, do::col_split(k, ";;;", colnames = by))
                x$Ref <- ref
                x
            }), what = rbind)
        }), what = rbind)
        if (is.null(old$datadist)) 
            options(datadist = NULL)
        options(old)
        for (i in 1:length(by)) {
            x[, by[i]] <- factor(x[, by[i]], levels = unique(do::col_split(ev$level, ";;;")[, i]))
        }
        mn <- ifelse(length(unique(x$modelName)) == 1, 1, 2)
        class(x) <- c(sprintf("m%sby", mn), "data.frame")
        attr(x, "by") <- by
        attr(x, "rcsx") <- unique(x$rcsName)
        if (unique(x$method) == "ols") 
            attr(x, "ylab") <- "beta"
        if (unique(x$method) == "lrm") 
            attr(x, "ylab") <- "odds"
        if (unique(x$method) == "lrm" & log) 
            attr(x, "ylab") <- "log odds"
        if (unique(x$method) == "cph") 
            attr(x, "ylab") <- "hazard"
        if (unique(x$method) == "cph" & log) 
            attr(x, "ylab") <- "log hazard"
        attr(x, "log") <- log
        invisible(x)
    }
}
```


