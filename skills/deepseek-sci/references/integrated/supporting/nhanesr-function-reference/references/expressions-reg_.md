# Integrated supporting reference: nhanesr-function-reference/references/expressions-reg_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-reg_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `reg_`

## `reg_check` [exported]

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

## `reg_logistic` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T) 
{
    fit0 <- fit
    cfint <- suppressMessages(exp(confint(fit)))
    if (inherits(fit, "glm")) 
        fit <- summary(fit)
    (coef <- as.data.frame(fit$coefficients, check.names = F))
    (tb <- coef[!row.names(coef) %in% "(Intercept)", ])
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
    tb$OR <- exp(tb[, 1])
    tb$low <- cfint[!row.names(cfint) %in% "(Intercept)", 1]
    tb$high <- cfint[!row.names(cfint) %in% "(Intercept)", 2]
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(digit2character(tb$OR, round), "(", tb$low, ",", tb$high, ")")
    tb <- drop_col(tb, "low", "high")
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
    parms <- names(fit0$xlevels)
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% parms) {
            cat <- paste0(x[i], fit0$xlevels[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", 6), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
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

## `reg_table` [exported]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
UseMethod("reg_table")
```

## `reg_table.coxph` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    fit0 <- fit
    if (inherits(fit, "coxph")) 
        fit <- quiet(summary(fit))
    (coef <- as.data.frame(fit$coefficients, check.names = F))
    (tb <- coef[, c("coef", "se(coef)", "z", "Pr(>|z|)", "exp(coef)")])
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
    colnames(tb)[5] <- "HR"
    (int <- fit$conf.int)
    tb$low <- int[, "lower .95", drop = FALSE]
    tb$high <- int[, "upper .95", drop = FALSE]
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(digit2character(tb$HR, round), "(", tb$low, ",", tb$high, ")")
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
            cat <- paste0(x[i], fit0$xlevels[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
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
    r <- res
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit0
    invisible(res)
}
```

## `reg_table.cph` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    tb <- capture.output(fit)
    tb <- do::rm_nchar(do::Trim(tb[which(grepl("Pr\\(>\\|Z\\|\\)", tb)):length(tb)]), 1)
    tb <- do::col_split(tb[-1], " {1,}", colnames = c("variable", "Coef", "S.E.", "Wald Z", "Pr(>|Z|)"))
    tb
    row.names(tb) <- tb[, 1]
    tb <- tb[, -1]
    p <- grepl("pr\\(", colnames(tb), T)
    for (ii in 1:nrow(tb)) {
        if (!is.na(tb[ii, p])) {
            p0 <- tryCatch(as.numeric(tb[ii, p]), warning = function(w) tb[ii, p])
            if (p0 == "w") 
                (next)(ii)
            if (p0 < 0.0001) {
                pr <- "<0.0001"
            }
            else if (p0 < 0.001) {
                pr <- "<0.001"
            }
            else {
                prck <- TRUE
                round0 <- round
                while (prck) {
                  pr <- digit2character(p0, round0)
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
    tb$HR <- exp(fit$coefficients)
    tb$low <- exp(fit$coefficients + qnorm(0.025000000000000001) * sqrt(diag(fit$var)))
    tb$high <- exp(fit$coefficients + qnorm(1 - 0.025000000000000001) * sqrt(diag(fit$var)))
    tb$Coef <- as.numeric(tb$Coef)
    tb$S.E. <- as.numeric(tb$S.E.)
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(tb[, "HR"], "(", tb$low, ",", tb$high, ")")
    tb <- drop_col(tb, "low", "high")
    tb
    if (style == 0) 
        return(tb)
    if (is.null(x)) {
        x <- unique(c(fit$Design$name, row.names(tb)))
        if (any(fit$Design$assume == "category")) {
            (category <- fit$Design$name[fit$Design$assume == "category"])
            ex <- unique(do.call(lapply(category, function(ii) {
                paste0(ii, "=", fit$Design$parms[[ii]])
            }), what = c))
            x <- set::not(x, ex)
        }
    }
    (xas <- fit$Design$assume)
    (parms <- fit$Design$parms)
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% names(parms)) {
            cat <- paste0(x[i], "=", parms[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
            if (style == 1) {
                res <- rbind(res, resi)
            }
            else if (style == 2) {
                res1 <- resi[1, ]
                res1[] <- ""
                row.names(res1) <- x[i]
                row.names(resi) <- paste0("    ", do::knife_left(row.names(resi), nchar(x[i]) + 1))
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
    r <- res
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit
    invisible(res)
}
```

## `reg_table.glm` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    if (tolower(fit$family[[1]]) == "gaussian") {
        r <- reg_table.lm(fit, round, style = style, x = x, view = view)
    }
    else {
        r <- reg_logistic(fit, round, style = style, x = x, view = view)
    }
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(r) <- c("svytableone", "data.frame")
    attr(r, "fit") <- fit
    invisible(r)
}
```

## `reg_table.lm` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T) 
{
    fit0 <- fit
    cfint <- confint(fit)
    fit <- summary(fit)
    (coef <- as.data.frame(fit$coefficients, check.names = F))
    tb <- coef[!row.names(coef) %in% "(Intercept)", ]
    (p <- grepl("pr\\(", colnames(tb), T))
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
            cat <- paste0(x[i], fit0$xlevels[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
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

## `reg_table.lrm` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    tb <- capture.output(fit)
    tb <- do::rm_nchar(do::Trim(tb[which(grepl("Pr\\(>\\|Z\\|\\)", tb)):length(tb)]), 1)
    tb <- do::col_split(tb[-1], " {1,}", colnames = c("variable", "Coef", "S.E.", "Wald Z", "Pr(>|Z|)"))
    tb
    row.names(tb) <- tb[, 1]
    tb <- tb[, -1]
    tb <- tb[!row.names(tb) %in% "Intercept", ]
    p <- grepl("pr\\(", colnames(tb), T)
    for (ii in 1:nrow(tb)) {
        if (!is.na(tb[ii, p])) {
            p0 <- tryCatch(as.numeric(tb[ii, p]), warning = function(w) tb[ii, p])
            if (p0 == "w") 
                (next)(ii)
            if (p0 < 0.0001) {
                pr <- "<0.0001"
            }
            else if (p0 < 0.001) {
                pr <- "<0.001"
            }
            else {
                prck <- TRUE
                round0 <- round
                while (prck) {
                  pr <- digit2character(p0, round0)
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
    tb$OR <- exp(fit$coefficients[!names(fit$coefficients) %in% "Intercept"])
    tb$low <- exp(fit$coefficients[!names(fit$coefficients) %in% "Intercept"] + qnorm(0.025000000000000001) * 
        sqrt(diag(fit$var)[!row.names(fit$var) %in% "Intercept"]))
    tb$high <- exp(fit$coefficients[!names(fit$coefficients) %in% "Intercept"] + qnorm(1 - 0.025000000000000001) * 
        sqrt(diag(fit$var)[!row.names(fit$var) %in% "Intercept"]))
    tb$Coef <- as.numeric(tb$Coef)
    tb$S.E. <- as.numeric(tb$S.E.)
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(tb[, "OR"], "(", tb$low, ",", tb$high, ")")
    tb <- drop_col(tb, "low", "high")
    if (style == 0) 
        return(tb)
    if (is.null(x)) {
        (x <- unique(c(fit$Design$name, row.names(tb))))
        if (any(fit$Design$assume == "category")) {
            (category <- fit$Design$name[fit$Design$assume == "category"])
            ex <- unique(do.call(lapply(category, function(ii) {
                paste0(ii, "=", fit$Design$parms[[ii]])
            }), what = c))
            x <- set::not(x, ex)
        }
    }
    (xas <- fit$Design$assume)
    (parms <- fit$Design$parms)
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% names(parms)) {
            cat <- paste0(x[i], "=", parms[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
            if (style == 1) {
                res <- rbind(res, resi)
            }
            else if (style == 2) {
                res1 <- resi[1, ]
                res1[] <- ""
                row.names(res1) <- x[i]
                row.names(resi) <- paste0("    ", do::knife_left(row.names(resi), nchar(x[i]) + 1))
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
    r <- res
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit
    invisible(res)
}
```

## `reg_table.ols` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    (tb <- data.frame(summary.lm(fit)$coefficients, check.names = F))
    (tb <- as.data.frame(tb[!row.names(tb) %in% "Intercept", ], check.names = FALSE))
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
    (ci <- data.frame(confint(fit), check.names = F))
    (ci <- ci[!row.names(ci) %in% "Intercept", ])
    tb$low <- ci[, 1]
    tb$high <- ci[, 2]
    digit2numeric(tb) <- round
    digit2character(tb$low) <- round
    digit2character(tb$high) <- round
    tb$"95% CI" <- paste0(tb[, 1], "(", tb$low, ",", tb$high, ")")
    tb <- drop_col(tb, "low", "high")
    tb
    if (style == 0) 
        return(tb)
    if (is.null(x)) {
        x <- unique(c(fit$Design$name, row.names(tb)))
        if (any(fit$Design$assume == "category")) {
            (category <- fit$Design$name[fit$Design$assume == "category"])
            ex <- unique(do.call(lapply(category, function(ii) {
                paste0(ii, "=", fit$Design$parms[[ii]])
            }), what = c))
            x <- set::not(x, ex)
        }
    }
    (xas <- fit$Design$assume)
    (parms <- fit$Design$parms)
    res <- NULL
    for (i in 1:length(x)) {
        if (x[i] %in% names(parms)) {
            cat <- paste0(x[i], "=", parms[[x[i]]])
            resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                NULL))), colnames(tb)), tb[cat[-1], ])
            if (style == 1) {
                res <- rbind(res, resi)
            }
            else if (style == 2) {
                res1 <- resi[1, ]
                res1[] <- ""
                row.names(res1) <- x[i]
                row.names(resi) <- paste0("    ", do::knife_left(row.names(resi), nchar(x[i]) + 1))
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
    r <- res
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit
    invisible(res)
}
```

## `reg_table.svycoxph` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    fit0 <- fit
    if (fit[["degf.resid"]] <= 0) {
        fit <- quiet(summary(fit, df = survey::degf(fit$survey.design)))
    }
    else {
        fit <- quiet(summary(fit))
    }
    coef <- as.data.frame(fit$coefficients, check.names = F)
    res <- coef[, c("coef", "se(coef)", "robust se", "z", "Pr(>|z|)", "exp(coef)")]
    p <- grepl("pr\\(", colnames(res), T)
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
    colnames(res)[6] <- "HR"
    int <- fit$conf.int
    res$low <- int[, "lower .95", drop = FALSE]
    res$high <- int[, "upper .95", drop = FALSE]
    digit2numeric(res) <- round
    digit2character(res$low) <- round
    digit2character(res$high) <- round
    res$"95% CI" <- paste0(digit2character(res$HR, round), "(", res$low, ",", res$high, ")")
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
            else {
                resi <- rbind(do::give_names(data.frame(matrix(rep("ref", ncol(tb)), nrow = 1, dimnames = list(cat[1], 
                  NULL))), colnames(tb)), tb[cat[-1], ])
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
    r <- res
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(res) <- c("svytableone", "data.frame")
    attr(res, "fit") <- fit0
    invisible(res)
}
```

## `reg_table.svyglm` [internal]

```r
function (fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL) 
{
    if (tolower(fit$family[[1]]) == "gaussian") {
        r <- svy_reg_lm(fit, round, style = style, x = x, view = view)
    }
    else {
        r <- svy_reg_logistic(fit, round, style = style, x = x, view = view)
    }
    if (!is.null(xlsx)) {
        header_bold <- openxlsx::createStyle(textDecoration = "Bold")
        wb <- openxlsx::createWorkbook()
        openxlsx::addWorksheet(wb, "Sheet1")
        for (i in 1:ncol(r)) {
            openxlsx::writeData(wb, sheet = 1, x = colnames(r)[i], startCol = i, startRow = 1, headerStyle = header_bold)
            if (i == 1) {
                for (j in 1:nrow(r)) {
                  if (do::left(r[j, i], 4) == "    ") {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                }
            }
            else if (grepl("p", colnames(r)[i], T)) {
                for (j in 1:nrow(r)) {
                  ck <- F
                  if (is.numeric(r[j, i])) {
                    if (r[j, i] < 0.050000000000000003) 
                      ck <- TRUE
                  }
                  if (ck) {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1, headerStyle = header_bold)
                  }
                  else {
                    openxlsx::writeData(wb, sheet = 1, x = r[j, i], startCol = i, startRow = j + 1)
                  }
                }
            }
            else {
                openxlsx::writeData(wb, sheet = 1, x = r[, i], startCol = i, startRow = 2)
            }
        }
        openxlsx::saveWorkbook(wb, xlsx, overwrite = TRUE)
    }
    class(r) <- c("svytableone", "data.frame")
    attr(r, "fit") <- fit
    invisible(r)
}
```


