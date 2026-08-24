# Integrated supporting reference: nhanesr-function-reference/references/expressions-nhs_.md

> Embedded source: `embedded-source/nhanesr-function-reference/references/expressions-nhs_.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Function Reference

Generated from installed package: `LOCAL_PATH`
Package version: `0.9.5.2`
Function objects extracted: `692`; exported names in NAMESPACE: `424`.

Use `function-index.csv` for machine-readable search. Use Markdown files for human-readable signatures and function bodies.

## Full Function Expressions: `nhs_`

## `nhs_Connect` [exported]

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

## `nhs_DOC` [exported]

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

## `nhs_Upload` [exported]

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

## `nhs_brief` [exported]

```r
function (...) 
UseMethod("nhs_brief")
```

## `nhs_brief.character` [internal]

```r
function (...) 
{
    x <- nhs_colnames(..., brief = TRUE)
    x$N <- ncol(x) - do::NA.row.sums(x)
    x[order(x$N, decreasing = TRUE), ]
}
```

## `nhs_brief.data.frame` [internal]

```r
function (...) 
{
    hold <- list(...)[[1]]
    hold <- hold[, !colnames(hold) %in% "seqn"]
    wh <- which(grepl("Year", colnames(hold)))
    if (length(wh) > 0) {
        for (i in 1:ncol(hold)) {
            if (i %in% wh) 
                (next)(i)
            hold[!is.na(hold[, i]), i] <- colnames(hold)[i]
        }
        hold <- unique(hold)
        if (length(wh) > 1) 
            hold <- hold[, -wh[1]]
        for (i in unique(hold[, wh[1]])) {
            (whr <- which(hold[, wh[1]] == i))
            if (length(whr) == 1) 
                (next)(i)
            for (j in colnames(hold)) {
                if (j %in% colnames(hold)[wh[1]]) 
                  (next)(j)
                if (all(is.na(hold[whr, j]))) {
                  "do nothing"
                }
                else {
                  hold[whr[1], j] <- j
                  hold[whr[-1], j] <- NA
                }
            }
        }
        hold <- unique(hold)
        for (i in unique(hold[, wh[1]])) {
            (whr <- which(hold[, wh[1]] == i))
            if (length(whr) == 1) 
                (next)(i)
            hold <- hold[-whr[-1], ]
        }
        hold[is.na(hold)] <- ""
        row.names(hold) <- NULL
    }
    else {
        hold <- colnames(hold)
    }
    hold
}
```

## `nhs_browse` [exported]

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

## `nhs_check` [exported]

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

## `nhs_codebook` [exported]

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

## `nhs_codebook.character` [internal]

```r
function (variable, files, tolower = FALSE) 
{
    if (missing(files)) 
        files <- nhs_tsv(cat = FALSE)
    ck <- tools::file_ext(files) != "codebook"
    if (any(ck)) {
        ext <- sprintf(unique(tools::file_ext(files[ck])), fmt = "\\.%s")
        files[ck] <- sprintf(do::Replace0(files[ck], ext), fmt = "%s.codebook")
    }
    if (length(files) > 200) 
        pb <- txtProgressBar(max = length(files), width = 25, style = 3)
    r <- do.call(lapply(files, function(i) {
        if (length(files) > 200) 
            setTxtProgressBar(pb, which(files == i))
        i <- do::Replace(do::formal_dir(i), "//", "/")
        (Year <- prepare_years(i))
        (Item <- prepare_items(i))
        (file <- do::Replace0(do::file.name(i), "\\.codebook"))
        (codei <- read.delim(i, comment.char = "#"))
        if (nrow(codei) == 0) 
            return()
        (codei <- codei[, c("variable", "code", "label")])
        if (tolower) 
            codei$label <- tolower(codei$label)
        cbind(Year = Year, Item = Item, file = file, codei)
    }), what = plyr::rbind.fill)
    if (length(files) > 200) 
        cat("\n")
    if (length(variable) == 0) 
        return(r)
    ck <- lookl(r$variable, variable, ignore.case = TRUE)
    r <- r[ck, ]
    dc <- reshape2::dcast(r, Year + Item + file + variable ~ label, toString, value.var = "code")
    dc5 <- dc[, 5:ncol(dc), drop = FALSE]
    od <- order(colMeans(sapply(dc5, as.numeric), na.rm = TRUE))
    dc[, 5:ncol(dc)] <- dc5[, od]
    dc
}
```

## `nhs_codebook.dataframe` [internal]

```r
function (variable, files, tolower = FALSE) 
{
    codei <- files[, c("Year", variable)]
    if (tolower) 
        codei$variable <- tolower(codei$variable)
    formu <- as.formula(sprintf("Year~%s", paste0(variable, collapse = "+")))
    reshape2::dcast(codei, formu, value.var = variable, fun.aggregate = length)
}
```

## `nhs_colnames` [exported]

```r
function (..., brief = FALSE) 
UseMethod("nhs_colnames")
```

## `nhs_colnames.character` [internal]

```r
function (..., brief = FALSE) 
{
    hold <- c(...)
    ck <- grepl(get_config_path(), hold, ignore.case = TRUE)
    (files <- hold[ck])
    (variable <- tolower(hold[!ck]))
    if (length(files) == 0) 
        files <- nhs_tsv(cat = FALSE)
    files <- unique(files)
    ck <- tools::file_ext(files) != "tsv"
    if (any(ck)) {
        ext <- sprintf(unique(tools::file_ext(files[ck])), fmt = "\\.%s")
        files[ck] <- sprintf(do::Replace0(files[ck], ext), fmt = "%s.tsv")
    }
    (years <- prepare_years(files))
    if (length(files) > 100) 
        pb <- txtProgressBar(max = length(files), width = 25, style = 3)
    df <- do.call(lapply(1:length(files), function(i) {
        if (length(files) > 100) 
            setTxtProgressBar(pb, i)
        namei <- colnames(data.table::fread(file = files[i], check.names = FALSE, showProgress = FALSE, 
            data.table = FALSE, nrows = 1))
        if (length(variable) > 0) {
            ck <- lookl(namei, variable, ignore.case = TRUE)
            namei <- namei[ck]
            namei
        }
        if (length(namei) > 0) {
            varLabel <- do::Replace(files[i], "\\.tsv", ".varLabel")
            varLabel <- read.delim(varLabel, comment.char = "#", row.names = 1)[namei, ]
            filei <- do::Replace0(do::file.name(files[i]), "\\.tsv")
            dfi <- as.data.frame(cbind(Year = prepare_years(files[i]), Items = prepare_items(files[i]), 
                file = filei, variable = namei))
            if (all(is.na(varLabel))) 
                return(dfi)
            if (nrow(varLabel) > 0) 
                dfi <- cbind(dfi, varLabel)
            dfi
        }
    }), what = plyr::rbind.fill)
    if (is.null(df)) {
        cat("result: 0")
        return()
    }
    df[is.na(df)] <- ""
    df <- df[, sapply(df, function(i) any(tryCatch(nchar(i) > 0, error = function(e) T))), drop = FALSE]
    class(df) <- c("nhs_colnames", "data.frame")
    if (brief) {
        brief <- reshape2::dcast(df[, c("Year", "Items", "file", "variable")], variable ~ Year, value.var = "variable")
        row.names(brief) <- brief$variable
        brief <- brief[, -which(colnames(brief) == "variable"), drop = FALSE]
        if (nrow(brief) > 0) {
            rnms <- row.names(brief)
            for (i in 1:length(rnms)) {
                if (i%%5 == 0 & length(rnms) > 5) {
                  rnms[i] <- sprintf("\"%s\",\n", rnms[i])
                }
                else {
                  rnms[i] <- sprintf("\"%s\",", rnms[i])
                }
                if (i == length(rnms)) 
                  clipr::write_clip(paste0(rnms, collapse = ""))
            }
        }
        return(brief)
    }
    df
}
```

## `nhs_colnames.list` [internal]

```r
function (..., order = FALSE, brief = FALSE) 
{
    hold <- list(...)
    files <- hold[[1]]
    rules <- unique(unlist(hold[-1]))
    years <- names(files)
    df <- data.frame(t(do.call(lapply(files, function(i) {
        namei <- colnames(i)
        as.data.frame(matrix(namei, nrow = 1, dimnames = list(NULL, namei)))
    }), what = plyr::rbind.fill)), check.names = FALSE, check.rows = FALSE)
    colnames(df) <- years
    if (order) 
        df <- df[order(row.names(df)), ]
    if (!is.null(rules)) 
        df <- df[lookl(row.names(df), rules), ]
    df
}
```

## `nhs_copy` [exported]

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

## `nhs_docFile_pc` [exported]

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

## `nhs_download` [exported]

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

## `nhs_file_table` [exported]

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

## `nhs_files_pc` [exported]

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

## `nhs_files_web` [exported]

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

## `nhs_html` [exported]

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

## `nhs_html_download` [exported]

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

## `nhs_items_pc` [exported]

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

## `nhs_items_web` [exported]

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

## `nhs_news` [exported]

```r
function (browse = FALSE) 
{
    browseURL("https://www.cdc.gov/nchs/nhanes/new_nhanes.htm")
}
```

## `nhs_pg` [exported]

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

## `nhs_read` [exported]

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

## `nhs_search` [exported]

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

## `nhs_search_file` [internal]

```r
function (..., data = NULL, cat = TRUE) 
{
    html <- paste0(get_config_path(), "/webpage.txt")
    data <- data.table::fread(html)
    ck <- lookl(..., x = data$txt, ignore.case = TRUE)
    x <- as.data.frame(data[ck, c("Year", "item", "file", "url")])
    if (cat) 
        cat("Results: ", nrow(x))
    class(x) <- c("nhs_search_file", "data.frame")
    x
}
```

## `nhs_target` [exported]

```r
function (...) 
{
    UseMethod("nhs_target")
}
```

## `nhs_target.character` [internal]

```r
function (..., data = NULL) 
{
    variable <- c(...)
    if (is.null(data)) {
        data <- data.table::fread(paste0(get_config_path(TRUE), "varLabel.txt"), showProgress = FALSE, 
            data.table = FALSE)
    }
    d1 <- data[, c("year", "item", "file", "variable", "target", "url")]
    d1[lookl(d1$variable, variable)]
}
```

## `nhs_target.data.frame` [internal]

```r
function (...) 
{
    tg <- attr(list(...)[[1]], "target")
    class(tg) <- c("target", "data.frame")
    tg
}
```

## `nhs_target.list` [internal]

```r
function (...) 
{
    tg <- attr(list(...)[[1]], "target")
    class(tg) <- c("target", "data.frame")
    tg
}
```

## `nhs_tsv` [exported]

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

## `nhs_update` [exported]

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

## `nhs_update0` [internal]

```r
function (path = NULL) 
{
    config_years(F)
    if (!dir.exists(path)) 
        stop("<U+8DEF><U+5F84><U+4E0D><U+5B58><U+5728>")
    message("<U+66F4><U+65B0>\n")
    copy_with_structure(path, get_config_path())
    message("\n<U+5EFA><U+5E93>")
    build_codebook()
    build_varLabel()
    build_html()
    message("<U+62F7><U+8D1D><U+6570><U+636E><U+7ED9><U+7528><U+6237>")
    file.copy(paste0(get_config_path(), "/varLabel.txt"), path)
    file.copy(paste0(get_config_path(), "/webpage.txt"), path)
    file.copy(paste0(get_config_path(), "/codebook.txt"), path)
}
```

## `nhs_varLabel` [exported]

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

## `nhs_view` [exported]

```r
function (x, ...) 
UseMethod("nhs_view")
```

## `nhs_view.Drug` [internal]

```r
function (x, ...) 
{
    key <- attr(x, "key")
    x <- highlight(x, key)
    x[is.na(x)] <- ""
    for (i in 1:ncol(x)) {
        if (grepl("rxddcn", colnames(x)[i])) {
            colnames(x)[i] <- highlight(colnames(x)[i], colors = "yellow")
        }
    }
    kableExtra::scroll_box(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, row.names = TRUE, 
        escape = FALSE, align = c("l", "c", "c", "c", "l")), full_width = FALSE), 0, align = "c"), height = "600px")
}
```

## `nhs_view.character` [internal]

```r
function (x, ..., n = 4) 
{
    h0 <- c(...)
    if (!is.null(h0)) 
        x <- highlight(x, h0)
    (mod <- length(x)%%n)
    append(x) <- rep("", n - mod)
    x <- data.frame(matrix(x, ncol = n))
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("c")), 
        full_width = FALSE), 0, align = "c"))
}
```

## `nhs_view.data.frame` [internal]

```r
function (x, ..., scroll_height = "600px") 
{
    h0 <- c(...)
    if ("Drug" %in% colnames(x)) 
        x <- x[order(x$Drug), ]
    x[is.na(x)] <- ""
    if (!is.null(h0)) {
        x <- x[lookl(x, h0), ]
        if (nrow(x) == 0) {
            print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl("no data", escape = FALSE, 
                align = c("c")), full_width = FALSE), 0, align = "c"))
            return("no results")
        }
        x1 <- unique(x)
        x <- highlight(x, h0)
        x <- unique(x)
    }
    else {
        x1 <- unique(x)
    }
    row.names(x) <- paste0(" ", nrow(x):1)
    for (i in 1:ncol(x)) {
        x[, i] <- do::Replace(x[, i], ";;;", paste0("<U+3002>", "<br/>"))
    }
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("c")), 
        full_width = FALSE), 0, align = "c"))
    row.names(x1) <- NULL
    invisible(x1)
}
```

## `nhs_view.incidence_byYear` [internal]

```r
function (x, ..., scroll_height = "1200px") 
{
    ck <- !is.na(x$`p-trend`)
    ck[1] <- F
    x[is.na(x)] <- ""
    x$characters[ck] <- paste0("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", x$characters[ck])
    x$characters[!ck] <- paste0("<font style=\"font-weight:bold\">", x$characters[!ck], "</font>")
    pp <- which(grepl("p-trend", colnames(x), T))
    colnames(x)[pp] <- sprintf("<span style=\"background-color:red\">%s</span>", colnames(x)[pp])
    for (i in 1:nrow(x)) {
        if (nchar(x[i, pp]) > 0) {
            ii <- tryCatch(as.numeric(x[i, pp]), warning = function(w) "w")
            if ((ii == "w" | ii <= 0.050000000000000003) & x[i, pp] != "ref") {
                x[i, pp] <- paste0("<font style=\"font-weight:bold\">", x[i, pp], "</font>")
            }
        }
    }
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("l", 
        "r", "r", "r", "r", "r", "r", "r", "r")), full_width = FALSE, fixed_thead = T), 0, align = "c"))
}
```

## `nhs_view.nhs_colnames` [internal]

```r
function (x, ..., label = TRUE, description = TRUE, target = TRUE, instructions = TRUE, hard.edits = TRUE, 
    datafame = FALSE, combine = NULL, scroll_height = "600px") 
{
    df <- x
    variable <- c(...)
    if (!is.null(variable)) {
        df <- df[lookl(df$variable, ..., ignore.case = TRUE), ]
    }
    if (!is.null(combine)) {
        for (i in combine) {
            ii <- unique(strsplit(i, " {0,}[,;] {0,}")[[1]])
            ii <- ii[ii %in% df$variable]
            df[df$variable %in% ii, "variable"] <- paste0(ii, collapse = ",")
        }
    }
    x <- reshape2::dcast(df, Items + variable ~ Year, toString, value.var = "file")
    colnames(x) <- do::Replace(colnames(x), "-", "<br>")
    id <- paste0_columns(df[, c("Items", "variable")], "---------")
    id_dup <- unique(id[duplicated(id)])
    for (i in id_dup) {
        (ck <- which(id == i))
        if ("label" %in% colnames(df) & label) {
            (lab <- df[ck, "label"])
            (cklab <- duplicated(tolower(lab)))
            (labi <- lab[!cklab])
            if (length(labi) > 1) {
                labi <- paste0(sapply(labi, function(j) {
                  (ckj <- tolower(lab) == tolower(j))
                  hf <- highlight(paste0(unique(df[ck, "file"][ckj]), collapse = ","), colors = "#37d8bf")
                  paste0(hf, "<br>", j)
                }), collapse = "<br>")
            }
            df[ck[1], "label"] <- labi
        }
        if ("description" %in% colnames(df) & description) {
            (lab <- df[ck, "description"])
            (cklab <- duplicated(tolower(lab)))
            (labi <- lab[!cklab])
            if (length(labi) > 1) {
                labi <- paste0(sapply(labi, function(j) {
                  (ckj <- tolower(lab) == tolower(j))
                  hf <- highlight(paste0(unique(df[ck, "file"][ckj]), collapse = ","), colors = "#37d8bf")
                  paste0(hf, "<br>", j)
                }), collapse = "<br>")
            }
            df[ck[1], "description"] <- labi
        }
        if ("target" %in% colnames(df) & target) {
            (lab <- df[ck, "target"])
            (cklab <- duplicated(tolower(lab)))
            (labi <- lab[!cklab])
            if (length(labi) > 1) {
                labi <- paste0(sapply(labi, function(j) {
                  (ckj <- tolower(lab) == tolower(j))
                  hf <- highlight(paste0(unique(df[ck, "file"][ckj]), collapse = ","), colors = "#37d8bf")
                  paste0(hf, "<br>", j)
                }), collapse = "<br>")
            }
            df[ck[1], "target"] <- labi
        }
        if (("instructions" %in% colnames(df)) & instructions) {
            (lab <- df[ck, "instructions"])
            (cklab <- duplicated(tolower(lab)))
            (labi <- lab[!cklab])
            if (length(labi) > 1) {
                labi <- paste0(sapply(labi, function(j) {
                  (ckj <- tolower(lab) == tolower(j))
                  hf <- highlight(paste0(unique(df[ck, "file"][ckj]), collapse = ","), colors = "#37d8bf")
                  paste0(hf, "<br>", j)
                }), collapse = "<br>")
            }
            df[ck[1], "instructions"] <- labi
        }
        if (("hard.edits" %in% colnames(df)) & hard.edits) {
            (lab <- df[ck, "hard.edits"])
            (cklab <- duplicated(tolower(lab)))
            (labi <- lab[!cklab])
            if (length(labi) > 1) {
                labi <- paste0(sapply(labi, function(j) {
                  (ckj <- tolower(lab) == tolower(j))
                  hf <- highlight(paste0(unique(df[ck, "file"][ckj]), collapse = ","), colors = "#37d8bf")
                  paste0(hf, "<br>", j)
                }), collapse = "<br>")
            }
            df[ck[1], "hard.edits"] <- labi
        }
    }
    df2 <- df[!duplicated(id), set::not(colnames(df), c("Year", "Years", "file"))]
    if ((("instructions" %in% colnames(df)) & !instructions)) 
        df2 <- df2[, set::not(colnames(df2), "instructions")]
    if ((("description" %in% colnames(df)) & !description)) 
        df2 <- df2[, set::not(colnames(df2), "description")]
    if ((("label" %in% colnames(df)) & !label)) 
        df2 <- df2[, set::not(colnames(df2), "label")]
    if ((("target" %in% colnames(df)) & !target)) 
        df2 <- df2[, set::not(colnames(df2), "target")]
    if ((("hard.edits" %in% colnames(df)) & !hard.edits)) 
        df2 <- df2[, set::not(colnames(df2), "hard.edits")]
    r <- dplyr::full_join(x, df2, by = c("Items", "variable"))
    if (datafame) {
        colnames(r) <- do::Replace(colnames(r), "<br>", "-")
        for (i in 1:ncol(r)) {
            r[, i] <- do::Replace0(r[, i], "<span style=\"background-color:#37d8bf\">", "</span>")
            r[, i] <- do::Replace(r[, i], "<br>", "/")
        }
        return(r)
    }
    df2 <- unique(df[, c("file", "url")])
    url <- df2$url
    names(url) <- df2$file
    url <- do::rm_nchar(url, 5)
    ck <- grepl("[0-9]{4}<br>[0-9]{4}", colnames(r))
    obj <- colnames(r)[ck]
    for (i in obj) {
        ri <- r[, i]
        if (length(ri) == 0) 
            (next)(i)
        for (j in 1:length(ri)) {
            if (nchar(ri[j]) < 1) 
                (next)(j)
            js <- strsplit(r[j, i], " {0,}, {0,}")[[1]]
            anchor <- do::Replace0(toupper(r[j, "variable"]), "<SPAN STYLE=\\\"BACKGROUND-COLOR:#.{,15}\\\">", 
                "</SPAN>")
            r[j, i] <- paste0(html_URL(js, url[js], anchor), collapse = ", ")
        }
    }
    r1 <- r[, set::not(colnames(r), "url")]
    if (nrow(r1) == 1) {
        r2 <- cbind(` ` = "1:End", r1)
    }
    else {
        r2 <- cbind(` ` = c(1:(nrow(r1) - 1), paste0(nrow(r1), ":End")), r1)
    }
    kableExtra::scroll_box(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(r2, escape = FALSE, 
        align = c("c", "l", "l", rep("c", sum(ck)), rep("l", 10))), full_width = TRUE), 0, align = "c"), 
        height = scroll_height)
}
```

## `nhs_view.nhs_file_web` [internal]

```r
function (x, ..., scroll_height = "600px") 
{
    h0 <- c(...)
    x <- cbind(seq = 1:nrow(x), x)
    if (!is.null(h0)) {
        ck <- !colnames(x) %in% c("DOC  url", "Data url")
        x[, ck] <- highlight(x[, ck], h0)
    }
    kableExtra::scroll_box(kableExtra::row_spec(kableExtra::column_spec(kableExtra::column_spec(kableExtra::kable_paper(kableExtra::kbl(x[, 
        1:7], escape = FALSE, align = c("c", "c", "l", "l", "l", "l", "l")), "striped"), 5, link = x$`DOC  url`), 
        6, link = x$`Data url`), 0, align = "c"), height = scroll_height)
}
```

## `nhs_view.nhs_search` [internal]

```r
function (x, ..., label = TRUE, description = TRUE, target = TRUE, instructions = TRUE, hard.edits = TRUE, 
    datafame = FALSE, scroll_height = "600px") 
{
    (h0 <- unique(c(...)))
    (h1 <- attr(x, "nhs_search"))
    hl <- unique(c(h1, h0))
    x[, -which(colnames(x) == "url")] <- highlight(x[, -which(colnames(x) == "url")], hl)
    colnames(x)[colnames(x) == "item"] <- "Items"
    colnames(x)[colnames(x) == "year"] <- "Year"
    class(x) <- c("nhs_colnames", "data.frame")
    nhs_view(x, label = label, description = description, target = target, instructions = instructions, 
        hard.edits = hard.edits, datafame = datafame, scroll_height = scroll_height)
}
```

## `nhs_view.nhs_search_file` [internal]

```r
function (x, ..., scroll_height = "600px") 
{
    x$file <- html_URL(x = x$file, href = x$url)
    x <- x[, c("Year", "item", "file")]
    r <- reshape2::dcast(x, item ~ Year, toString, value.var = c("file"))
    for (i in 1:nrow(r)) {
        for (j in 2:ncol(r)) {
            if (nchar(r[i, j]) > 0) {
                TTT <- html_URL("T", nhs_browse(colnames(r)[j], r$item[i], FALSE))
                r[i, j] <- paste0(r[i, j], "<br/>", TTT)
            }
        }
    }
    kableExtra::scroll_box(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(r, escape = FALSE, 
        align = c("c")), full_width = TRUE), 0, align = "c"), height = scroll_height)
}
```

## `nhs_view.regtable` [internal]

```r
function (x, ..., scroll_height = "1200px") 
{
    ck <- do::left(x$character, 4) == "    "
    x$character[ck] <- paste0("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", x$character[ck])
    x$character[!ck] <- paste0("<font style=\"font-weight:bold\">", x$character[!ck], "</font>")
    pp <- grepl("p", colnames(x), T)
    colnames(x)[pp] <- sprintf("<span style=\"background-color:red\">%s</span>", colnames(x)[pp])
    for (i in 1:nrow(x)) {
        if (nchar(x[i, pp]) > 0) {
            ii <- tryCatch(as.numeric(x[i, pp]), warning = function(w) "w")
            if ((ii == "w" | ii <= 0.050000000000000003) & x[i, pp] != "ref") {
                x[i, pp] <- paste0("<font style=\"font-weight:bold\">", x[i, pp], "</font>")
            }
        }
    }
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("l", 
        "r", "r", "r", "r", "r", "r", "r", "r")), full_width = FALSE, fixed_thead = T), 0, align = "c"))
}
```

## `nhs_view.stratum_model` [internal]

```r
function (x, ..., scroll_height = "1200px") 
{
    ck <- nchar(x[, 2]) == 0
    x$character[ck] <- paste0("<font style=\"font-weight:bold\">", x$character[ck], "</font>")
    x$character[!ck] <- paste0("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", x$character[!ck])
    pp <- which((colnames(x) == "p") | grepl("p for trend", colnames(x), T))
    colnames(x)[pp] <- sprintf("<span style=\"background-color:red\">%s</span>", colnames(x)[pp])
    if (length(pp) > 0) {
        for (j in pp) {
            for (i in 1:nrow(x)) {
                if (nchar(x[i, j]) > 0) {
                  ii <- tryCatch(as.numeric(x[i, j]), warning = function(w) "w")
                  if ((ii == "w" | ii <= 0.050000000000000003) & x[i, j] != "ref") {
                    x[i, j] <- paste0("<font style=\"font-weight:bold\">", x[i, j], "</font>")
                  }
                }
            }
        }
    }
    row.names(x) <- NULL
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("l", 
        "r", "r", "r", "r", "r", "r", "r", "r")), full_width = FALSE, fixed_thead = T), 0, align = "c"))
}
```

## `nhs_view.svy_tableone` [internal]

```r
function (x, ...) 
{
    row.names(x) <- NULL
    if ("strata" %in% class(x)) {
        if ("wtn" %in% class(x)) {
            if ("total" %in% class(x)) {
                ck <- grepl("\\[", x$variable)
                x[!ck, "variable"] <- paste0(do::rep_n("&nbsp;", 8), x[!ck, "variable"])
                colnames(x)[colnames(x) == "variable"] <- ""
                colnames(x)[colnames(x) == "unweighted"] <- "percent"
                colnames(x)[colnames(x) == "weighted"] <- "Percent"
                (group_loc <- which(grepl("_unwtd_n", colnames(x))))
                (group <- do::Replace0(colnames(x)[group_loc], "_unwtd_n"))
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_value")] <- "prevalence"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_value")] <- "prevalence"
                h1 <- c(1, 4, diff(c(group_loc, ncol(x))))
                names(h1) <- c(" ", "Study population", group, " ")[1:length(h1)]
                h2 <- c(1, 2, 2, rep(c(2, 2), length(group)), 1)
                names(h2) <- c(" ", "unweighted", "weighted", rep(c("unweighted", "weighted"), length(group)))
                bold_change(kableExtra::row_spec(kableExtra::add_header_above(kableExtra::add_header_above(kableExtra::kable_classic(kableExtra::kable(x, 
                  align = c("l", rep("c", ncol(x) - 1)), escape = FALSE), full_width = F), h2), h1), 
                  (1:nrow(x))[ck], TRUE))
            }
            else if (!"total" %in% class(x)) {
                ck <- grepl("\\[", x$variable)
                x[!ck, "variable"] <- paste0(do::rep_n("&nbsp;", 8), x[!ck, "variable"])
                colnames(x)[colnames(x) == "variable"] <- ""
                (group_loc <- which(grepl("_unwtd_n", colnames(x))))
                (group <- do::Replace0(colnames(x)[group_loc], "_unwtd_n"))
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_value")] <- "prevalence"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_value")] <- "prevalence"
                h1 <- c(1, diff(c(group_loc, ncol(x))), 1)
                names(h1) <- c(" ", group, " ")
                h2 <- c(1, rep(c(2, 2), length(group)))
                names(h2) <- c(" ", rep(c("unweighted", "weighted"), length(group)))
                bold_change(kableExtra::row_spec(kableExtra::add_header_above(kableExtra::add_header_above(kableExtra::kable_classic(kableExtra::kable(x, 
                  align = c("l", rep("c", ncol(x) - 1)), escape = FALSE), full_width = F), h2), h1), 
                  (1:nrow(x))[ck], TRUE))
            }
        }
        else if (!"wtn" %in% class(x)) {
            if ("total" %in% class(x)) {
                ck <- grepl("\\[", x$variable)
                x[!ck, "variable"] <- paste0(do::rep_n("&nbsp;", 8), x[!ck, "variable"])
                colnames(x)[colnames(x) == "variable"] <- ""
                (group_loc <- which(grepl("_unwtd_n", colnames(x))))
                (group <- do::Replace0(colnames(x)[group_loc], "_unwtd_n"))
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_value")] <- "unweighted"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_value")] <- "weighted"
                h1 <- c(1, 3, diff(c(group_loc, ncol(x))), 1)
                names(h1) <- c(" ", "Study population", group, " ")
                bold_change(kableExtra::row_spec(kableExtra::add_header_above(kableExtra::kable_classic(kableExtra::kable(x, 
                  align = c("l", rep("c", ncol(x) - 1)), escape = FALSE), full_width = F), h1), (1:nrow(x))[ck], 
                  TRUE))
            }
            else if (!"total" %in% class(x)) {
                ck <- grepl("\\[", x$variable)
                x[!ck, "variable"] <- paste0(do::rep_n("&nbsp;", 8), x[!ck, "variable"])
                colnames(x)[colnames(x) == "variable"] <- ""
                (group_loc <- which(grepl("_unwtd_n", colnames(x))))
                (group <- do::Replace0(colnames(x)[group_loc], "_unwtd_n"))
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_n")] <- "n"
                colnames(x)[colnames(x) %in% paste0(group, "_unwtd_value")] <- "unweighted"
                colnames(x)[colnames(x) %in% paste0(group, "_wtd_value")] <- "weighted"
                h1 <- c(1, diff(c(group_loc, ncol(x))), 1)
                names(h1) <- c(" ", group, " ")
                bold_change(kableExtra::row_spec(kableExtra::add_header_above(kableExtra::kable_classic(kableExtra::kable(x, 
                  align = c("l", rep("c", ncol(x) - 1)), escape = FALSE), full_width = F), h1), (1:nrow(x))[ck], 
                  TRUE))
            }
        }
    }
    else if (!"strata" %in% class(x)) {
        ck <- grepl("\\[", x$variable)
        x[!ck, "variable"] <- paste0(do::rep_n("&nbsp;", 8), x[!ck, "variable"])
        colnames(x)[colnames(x) == "variable"] <- ""
        colnames(x)[colnames(x) == "unweighted"] <- "percent"
        colnames(x)[colnames(x) == "weighted"] <- "Percent"
        bold_change(kableExtra::row_spec(kableExtra::add_header_above(kableExtra::kable_classic(kableExtra::kable(x, 
            align = c("l", "c", "c", "c", "c"), escape = FALSE), full_width = F), c(` ` = 1, unweighted = 2, 
            weighted = ifelse("wtn" %in% class(x), 2, 1))), (1:nrow(x))[ck], TRUE))
    }
}
```

## `nhs_view.svytableone` [internal]

```r
function (x, ..., scroll_height = "1200px") 
{
    ck <- do::left(x$variable, 4) == "~~~~"
    x$variable[ck] <- do::knife_left(x$variable[ck], 4)
    x$variable[ck] <- paste0("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", x$variable[ck])
    x$variable[!ck] <- paste0("<font style=\"font-weight:bold\">", x$variable[!ck], "</font>")
    pp <- grepl("pvalue", colnames(x), T)
    colnames(x)[pp] <- sprintf("<span style=\"background-color:red\">%s</span>", colnames(x)[pp])
    if (any(pp)) {
        for (i in 1:nrow(x)) {
            if (nchar(x[i, pp]) > 0) {
                ii <- tryCatch(as.numeric(x[i, pp]), warning = function(w) x[i, pp])
                if ((ii == "w" | ii <= 0.050000000000000003) & x[i, pp] != "ref") {
                  x[i, pp] <- paste0("<font style=\"font-weight:bold\">", x[i, pp], "</font>")
                }
            }
        }
    }
    print(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(x, escape = FALSE, align = c("l", 
        "r", "r", "r", "r", "r", "r", "r", "r")), full_width = FALSE, fixed_thead = T), 0, align = "c"))
}
```

## `nhs_view.target` [internal]

```r
function (x, ...) 
{
    anchor <- if ("anchor" %in% colnames(x)) 
        x$anchor
    else x$variable
    x$variable <- html_URL(x = x$variable, href = x$url, name = toupper(anchor))
    x <- x[, c("target", "year", "item", "file", "variable")]
    id <- paste0_columns(x[, c("year", "item", "file")])
    idu <- unique(id)
    for (i in 1:length(idu)) {
        if (i == 1) 
            r <- NULL
        ck <- id == idu[i]
        tck <- x[ck, ]
        tu <- unique(tck$target)
        for (j in tu) {
            (ckj <- which(tck$target == j))
            pck <- tck[ckj, "variable"]
            kmax <- 5
            if (length(pck) > kmax) {
                pck <- paste0(sapply(1:round(length(pck)/kmax), function(k) {
                  if (k < round(length(pck)/kmax)) {
                    paste0(pck[(k * kmax - (kmax - 1)):(k * kmax)], collapse = ",")
                  }
                  else {
                    paste0(pck[(k * kmax - (kmax - 1)):length(pck)], collapse = ",")
                  }
                }), collapse = "<br/>")
            }
            else {
                pck <- paste0(pck, collapse = ",")
            }
            tck[ckj[1], "variable"] <- pck
            if (length(ckj) > 1) 
                tck <- tck[-ckj[-1], ]
        }
        r <- rbind(r, tck)
    }
    r <- r[order(r$target, decreasing = TRUE), ]
    row.names(r) <- 1:nrow(r)
    kableExtra::scroll_box(kableExtra::row_spec(kableExtra::kable_styling(kableExtra::kbl(r, row.names = TRUE, 
        escape = FALSE, align = c("l", "c", "c", "c", "l")), full_width = TRUE), 0, align = "c"), height = "600px")
}
```

## `nhs_wt` [exported]

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

## `nhs_year_pc` [exported]

```r
function (range = TRUE) 
{
    do::unique_no.NA(do::increase(unique(stringr::str_extract(list.files(get_config_path()), "[0-9]{4}-[0-9]{4}"))))
}
```

## `nhs_years_web` [exported]

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


