# Integrated supporting reference: nhanesr-function-reference/references/expressions-internal-dot.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-internal-dot.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `internal-dot`

## `.add_local_z` [internal]

```r
function (ip, wechat, end = NULL, win = F) 
{
    if (do::left(ip, 7) != "nhanesR") 
        stop("<U+4E0D><U+662F>nhanesR<U+8BA4><U+8BC1><U+7801>")
    if (wechat %in% .a$wechat) {
        cat("<U+5DF2><U+8D2D><U+4E70>")
        enddate <- .a[.a$wechat %in% wechat, "enddate"]
    }
    else {
        if (is.null(end)) 
            stop("<U+65B0><U+7528><U+6237><U+5FC5><U+987B><U+6307><U+5B9A><U+5E74>")
        enddate <- Sys.Date() + 365 * end + 2
    }
    (ai <- unique(data.frame(ip = ip, wechat = wechat, enddate = enddate)))
    if (ai$wechat %in% .a$wechat) {
        ai$enddate = do::last(.a$enddate[.a$wechat == ai$wechat])
    }
    .a <- rbind(.a, ai)
    .a <- unique(.a)
    if (grepl("WINDOWS", ip, T)) {
        pattern <- c("D14393E", "D17763E", "D18363E", "D19041E", "D19043E", "D19043E", "D19044E", "D19045E", 
            "D22000E", "D22621E", "D22623E", "D22631E", "D22635E", "D23590E", "D23601E", "D23606E", "D23619E", 
            "D23620E", "D26058E", "D26080E", "D26100E", "D26120E")
        if (grepl(paste0(pattern, collapse = "|"), ip)) {
            for (i in 1:length(pattern)) {
                ip2 <- do::Replace(ip, paste0(pattern, collapse = "|"), pattern[i])
                a2 <- data.frame(ip = ip2, wechat = wechat, enddate = ai$enddate)
                .a <- rbind(.a, a2)
                .a <- unique(.a)
            }
        }
    }
    row.names(.a) <- NULL
    print(.a$ip[.a$wechat == wechat])
    .a <- .a[nchar(.a$wechat) > 0, ]
    use_data_append(.a)
    devtools::load_all(".")
}
```

## `.add_year_1` [internal]

```r
function (id = NULL, year = 1) 
{
    if (is.null(id)) 
        stop("id<U+4E0D><U+80FD><U+4E3A><U+7A7A>")
    ck <- .a$ip %in% id | .a$wechat == id
    any(ck)
    (ai <- .a[ck, ])
    if (nrow(ai) == 0) 
        stop("<U+6CA1><U+6709><U+627E><U+5230><U+4EE5><U+524D><U+7684>id")
    print(ai)
    .a$enddate[ck] <- Sys.Date() + 370 * year
    use_data_append(.a)
    devtools::load_all(".")
}
```

## `.add_zhishi` [internal]

```r
function (data, file, write = TRUE) 
{
    data$id <- odd(1:(2 * nrow(data)))
    x <- data.frame(id = even(1:(2 * nrow(data))))
    data <- dplyr::full_join(x, data, "id")
    data[1:nrow(x), 2] <- paste0(tmcn::toUTF8("# <U+4E0A><U+6D77><U+679D><U+8BC6><U+533B><U+5B66><U+79D1><U+6280><U+6709><U+9650><U+516C><U+53F8><U+51FA><U+54C1>,<U+5FAE><U+4FE1>:Charleszhanggo"), 
        1:nrow(x))
    data <- data[order(data$id), -1]
    for (i in 1:ncol(data)) {
        nasum <- sum(is.na(data[, i]))
        if (nasum > 0) {
            data[is.na(data[, i]), i] <- paste0(tmcn::toUTF8("<U+4E0A><U+6D77><U+679D><U+8BC6><U+533B><U+5B66><U+79D1><U+6280><U+6709><U+9650><U+516C><U+53F8><U+51FA><U+54C1>,<U+5FAE><U+4FE1>:Charleszhanggo"), 
                rnorm(nasum))
        }
    }
    if (write) {
        data.table::fwrite(data, file, sep = "\t")
    }
    else {
        data
    }
}
```

## `.cal` [internal]

```r
function () 
{
    x <- Sys.info()
    if (Sys.info()[1] != "Windows") {
        x <- x[!names(x) %in% c("machine")]
        if (x["user"] %in% c("NEW")) {
            x <- x[!names(x) %in% c("nodename")]
        }
    }
    x <- toupper(rev(do::Replace(do::Replace0(unique(x), " "), ".*-", "a")))
    z <- paste0(paste0(LETTERS[1:length(x)], x), collapse = "")
    if (do::is.windows()) {
        z0 <- tryCatch(paste0(z, "$z$", do::Replace0(set::grep_and(stringi::stri_trans_nfd(system("systeminfo", 
            intern = TRUE)), c("ID:", "-")), ".*ID:", " ")) %>% paste0(collapse = ""), error = function(e) "e")
        if (z0 != "e") 
            z <- z0
    }
    if (do::is.mac()) {
        Sys.setenv(PATH = paste(c(Sys.getenv("PATH"), "/usr/sbin"), collapse = ":"))
        z0 <- tryCatch(paste0(z, "$z$", do::Trim(system("system_profiler SPHardwareDataType | grep Serial | cut -f 2 -d:", 
            intern = T), c(" "))), error = function(e) "e")
        if (z0 != "e") 
            z <- z0
    }
    paste0("nhanesR", ".", z)
}
```

## `.delete_local_z` [internal]

```r
function (ip) 
{
    if (".a" %in% ls(envir = .GlobalEnv, all.names = T)) 
        rm(".a", envir = .GlobalEnv)
    .a <- .a[toupper(.a$ip) != toupper(ip), ]
    .a <- .a[toupper(.a$wechat) != toupper(ip), ]
    use_data_append(.a)
    devtools::load_all()
}
```

## `.onAttach` [internal]

```r
function (...) 
{
    options(error = NULL)
    suppressWarnings(rm(.drug_search_years, envir = .GlobalEnv))
    suppressWarnings(rm(.drug_search_data, envir = .GlobalEnv))
    suppressPackageStartupMessages(require(htmltools, warn.conflicts = F, quietly = T))
    suppressPackageStartupMessages(require(Hmisc, warn.conflicts = F, quietly = T))
    suppressPackageStartupMessages(require(dplyr, warn.conflicts = F, quietly = T))
    suppressPackageStartupMessages(require(openxlsx, warn.conflicts = F, quietly = T))
    suppressPackageStartupMessages(require(rms, warn.conflicts = F, quietly = T))
    suppressPackageStartupMessages(require(ggplot2, warn.conflicts = F, quietly = T))
    suppressWarnings(dir.create(tempdir()))
    options(warn = -1)
    options(scipen = 99)
    suppressWarnings(library(rms, quietly = T, warn.conflicts = F))
    suppressWarnings(library(survey, quietly = T, warn.conflicts = F))
    (zz <- .zz())
    pkg <- "nhanesR"
    if (zz$c2 == "out") {
        packageStartupMessage(tmcn::toUTF8("<U+5DF2><U+8FC7><U+671F>,<U+8BF7><U+91CD><U+65B0><U+8D2D><U+4E70>"))
        (path <- .libPaths()[sapply(.libPaths(), function(i) pkg %in% list.files(i))])
        unlink(paste0(path, "/", pkg), force = TRUE, recursive = TRUE)
        e <- tryCatch(detach(paste0("package:", pkg), unload = TRUE), error = function(e) "e")
    }
    else {
        if (zz$ck) {
            (temp <- config_temp())
            (ck_years <- suppressMessages(get_config_years()))
            (ck_items <- suppressMessages(get_config_items()))
            (ck_path <- suppressMessages(get_config_path()))
            (ck <- any(is.null(ck_years), is.null(ck_items), is.null(ck_path)))
            if (ck) {
                packageStartupMessage(tmcn::toUTF8("<U+5728><U+4F7F><U+7528>nhanesR<U+5305><U+4E4B><U+524D>,<U+8BF7><U+5148><U+5B8C><U+6210><U+4EE5><U+4E0B>3<U+9879><U+914D><U+7F6E>\n     1.<U+4F7F><U+7528>config_path()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+8DEF><U+5F84>\n     2.<U+4F7F><U+7528>config_years()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+5E74><U+4EFD>\n     3.<U+4F7F><U+7528>config_items()<U+547D><U+4EE4><U+914D><U+7F6E><U+6570><U+636E><U+5E93><U+6587><U+4EF6><U+7C7B><U+578B>"))
            }
            else {
                packageStartupMessage(paste0(tmcn::toUTF8("\n<U+6570><U+636E><U+5E93><U+8DEF><U+5F84><U+662F>: "), 
                  get_config_path()))
                updatetxt <- paste0(get_config_path(), "/update.txt")
                if (file.exists(updatetxt)) {
                  last <- readLines(updatetxt)
                  diff <- as.numeric(Sys.Date() - as.Date(last))
                  packageStartupMessage(tmcn::toUTF8("\n<U+6570><U+636E><U+5E93><U+672B><U+6B21><U+66F4><U+65B0><U+65E5><U+671F><U+662F>: "), 
                    last)
                  if (diff > -1) {
                    packageStartupMessage(tmcn::toUTF8("<U+6570><U+636E><U+5E93><U+672A><U+66F4><U+65B0><U+5929><U+6570>: "), 
                      diff)
                  }
                }
                eval(parse(text = "options(survey.lonely.psu=\"adjust\")"), envir = .GlobalEnv)
            }
        }
        else {
            packageStartupMessage(tmcn::toUTF8("<U+4F60><U+7684><U+9A8C><U+8BC1><U+7801>:"), zz$ip)
            packageStartupMessage(tmcn::toUTF8("<U+8BF7><U+5C06><U+9A8C><U+8BC1><U+7801><U+53D1><U+7ED9><U+6211>"))
            packageStartupMessage(tmcn::toUTF8("<U+5FAE><U+4FE1><U+53F7>:"), "Charleszhanggo")
            (path <- .libPaths()[sapply(.libPaths(), function(i) pkg %in% list.files(i))])
            unlink(paste0(path, "/", pkg), force = TRUE, recursive = TRUE)
            e <- tryCatch(detach(paste0("package:", pkg), unload = TRUE), error = function(e) "e")
        }
    }
    options(warn = 0)
}
```

## `.show_local_z` [internal]

```r
function (wechat) 
{
    if (".a" %in% ls(envir = .GlobalEnv, all.names = T)) 
        rm(".a", envir = .GlobalEnv)
    .a[grepl(wechat, .a$wechat) | .a$ip %in% wechat, ]
}
```

## `.zz` [internal]

```r
function () 
{
    (ip <- .cal())
    if (".a" %in% ls(envir = .GlobalEnv, all.names = T)) 
        rm(".a", envir = .GlobalEnv)
    if (do::is.windows()) {
        (c1 <- (.a$ip %in% ip) | (do::Replace0(.a$ip, "nhanesR.", "\\$z\\$.*") %in% do::Replace0(ip, 
            "nhanesR.", "\\$z\\$.*")) | (do::Replace0(.a$ip, "\\$z\\$.*") %in% do::Replace0(ip, "\\$z\\$.*")))
        sum(c1)
        if (any(c1)) {
            if (do::last(.a$enddate[c1]) < Sys.Date()) {
                c2 = "out"
            }
            else {
                c2 = "use"
            }
        }
        else {
            c2 = "use"
        }
        list(ck = any(c1), c2 = c2, ip = ip)
    }
    else {
        (c1 <- grepl(do::Replace0(ip, ".*\\$z\\$"), do::Replace0(.a$ip, ".*\\$z\\$"), T))
        sum(c1)
        if (any(c1)) {
            if (do::last(.a$enddate[c1]) < Sys.Date()) {
                c2 = "out"
            }
            else {
                c2 = "use"
            }
        }
        else {
            c2 = "use"
        }
        list(ck = any(c1), c2 = c2, ip = ip)
    }
}
```


