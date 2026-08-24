# Integrated supporting reference: nhanesr-auto-params/references/nhanesr-core-functions.md

> Embedded source: `embedded-source/nhanesr-auto-params/references/nhanesr-core-functions.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# nhanesR Core Function Parameters

## config_path
Title: Config path of 'NHANES' database
Usage: `config_path(path)`
- `path`: required. path of 'NHANES' database

## config_years
Title: Config years of 'NHANES' database
Usage: `config_years(cat = T)`
- `cat`: optional; default `T`. 

## config_items
Title: Config items of 'NHANES' database
Usage: `config_items(items)`
- `items`: required. items of 'NHANES' database. If items is missing, Demographics, Dietary, Examination, Laboratory and Questionnaire will be used.

## get_config_path
Title: Get config information of "NHANES" database
Usage: `get_config_path(slash = FALSE) get_config_items() get_config_years(range = TRUE)`
- `slash`: optional; default `FALSE`. logical for end with slash

## get_config_years
Title: Get config information of "NHANES" database
Usage: `get_config_path(slash = FALSE) get_config_items() get_config_years(range = TRUE)`
- `range`: optional; default `TRUE`. 

## get_config_items
Title: Get config information of "NHANES" database
Usage: `get_config_path(slash = FALSE) get_config_items() get_config_years(range = TRUE)`

## prepare_years
Title: prepare years from config
Usage: `prepare_years(years, range = TRUE)`
- `years`: required. one or more years
- `range`: optional; default `TRUE`. logical.

## prepare_items
Title: prepare items from config ignore capital and little letters and left match
Usage: `prepare_items(items)`
- `items`: required. one or more items

## nhs_download
Title: Download data from 'NHANES' database
Usage: `nhs_download(   years,   items,   files,   xpt = TRUE,   tsv = TRUE,   varLabel = TRUE,   codebook = TRUE,   update = TRUE,   filetable = NULL,   cat = TRUE,   redown = TRUE,   updatekeyword = NULL )`
- `years`: required. one or more years
- `items`: required. one or more items
- `files`: required. which files to be download
- `xpt`: optional; default `TRUE`. logical. whether to download original data
- `tsv`: optional; default `TRUE`. logical. whether to restore tsv file
- `varLabel`: optional; default `TRUE`. logical. whether to restore varLabel file
- `codebook`: optional; default `TRUE`. logical. whether to restore codebook file.
- `update`: optional; default `TRUE`. logical. whether to restore upate file.
- `filetable`: optional; default `NULL`. ignore. only used in update.
- `cat`: optional; default `TRUE`. logical. whether to print download process.
- `redown`: optional; default `TRUE`. logical. whether to download the existed file.
- `updatekeyword`: optional; default `NULL`. update key word

## nhs_read
Title: Read data from 'NHANES' database in local PC
Usage: `nhs_read(   ...,   varLabel = FALSE,   codebook = TRUE,   lower_cd = FALSE,   Year = TRUE,   nrows = Inf,   cat = TRUE,   refuse_dontknow_toNA = TRUE,   psu_strat = TRUE,   join = c("full", "inner", "left", "right", "semi", "anti", "nest") )`
- `...`: optional. one or more data file path, or variable names
- `varLabel`: optional; default `FALSE`. logical, whether to add varLabel for variable
- `codebook`: optional; default `TRUE`. logical, whether to decode variable
- `lower_cd`: optional; default `FALSE`. logical. whether to ignore case in codebook
- `Year`: optional; default `TRUE`. logical. whether to keep Year column
- `nrows`: optional; default `Inf`. The maximum number of rows to read.
- `cat`: optional; default `TRUE`. logical. whether to show progress information
- `refuse_dontknow_toNA`: optional; default `TRUE`. logical. whether transform refuse and dont know to NA
- `psu_strat`: optional; default `TRUE`. logical
- `join`: optional; default `c("full", "inner", "left", "right", "semi", "anti", "nest")`. join method. One of full, inner, left, right, semi, anti, nest

## nhs_search
Title: search in "NHANES" database
Usage: `nhs_search(..., cat = TRUE, fileds = NULL)`
- `...`: optional. one or more keywords, use look() function to search.
- `cat`: optional; default `TRUE`. logical. whether to show results number
- `fileds`: optional; default `NULL`. 

## nhs_colnames
Title: exact colnames name
Usage: `nhs_colnames(..., brief = FALSE) nhs_colnamescharacter(..., brief = FALSE) nhs_colnameslist(..., order = FALSE, brief = FALSE)`
- `...`: optional. path of tsv files or dataframe or list of nhs_read()
- `brief`: optional; default `FALSE`. logical. whether to return brief results

## nhs_varLabel
Title: label for variable file path or variable names shoul be given together, no matter which is first. They will be divided into files and variables according to whether they contain a path or not.
Usage: `nhs_varLabel(..., tolower = FALSE)`
- `...`: optional. file path of nhs_files_pc() or variable names
- `tolower`: optional; default `FALSE`. logical. Whether to transform lebel to be lower.

## nhs_codebook
Title: Codebook for variable
Usage: `nhs_codebook(..., tolower = FALSE)`
- `...`: optional. one(suggest) or more variable names
- `tolower`: optional; default `FALSE`. logical

## nhs_wt
Title: calculate cominbe weight
Usage: `nhs_wt(data, yr2, yr4, wtname = "cwt")`
- `data`: required. data
- `yr2`: required. weight for 2 years
- `yr4`: required. weight for 4 years: 1999-2000 and 2001-2002
- `wtname`: optional; default `"cwt"`. name for combine weight column

## svy_design
Title: svy_design
Usage: `svy_design(data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") svy_designdata.frame(data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra") svy_designmids(data, weights = "nhs_wt", psu = "sdmvpsu", strata = "sdmvstra")`
- `data`: required. data
- `weights`: optional; default `"nhs_wt"`. weights
- `psu`: optional; default `"sdmvpsu"`. sdmvpsu
- `strata`: optional; default `"sdmvstra"`. sdmvstra

## svy_tableone
Title: table one for survey data
Usage: `svy_tableone(   design,   cv = NULL,   cv.nn = NULL,   gv = NULL,   by = NULL,   c_meanSQse = FALSE,   c_meanPMse = FALSE,   c_ci = FALSE,   c_geometric = FALSE,   g_N = FALSE,   g_percent = FALSE,   g_perSQse = FALSE,   g_NSQper = FALSE,   g_nSQper = FALSE,   g_ci = FALSE,   g_direction = "v",   total = FALSE,   round = 2,   view = T,   xlsx = NULL,   pvalue = TRUE )`
- `design`: required. design
- `cv`: optional; default `NULL`. continuous variable
- `cv.nn`: optional; default `NULL`. continuous variable with non-normal distribution
- `gv`: optional; default `NULL`. categorical variable
- `by`: optional; default `NULL`. by
- `c_meanSQse`: optional; default `FALSE`. logical
- `c_meanPMse`: optional; default `FALSE`. logical
- `c_ci`: optional; default `FALSE`. logical
- `c_geometric`: optional; default `FALSE`. logical, wether to calculate geometric mean for contineous variable
- `g_N`: optional; default `FALSE`. logical
- `g_percent`: optional; default `FALSE`. logical
- `g_perSQse`: optional; default `FALSE`. logical
- `g_NSQper`: optional; default `FALSE`. logical
- `g_nSQper`: optional; default `FALSE`. 
- `g_ci`: optional; default `FALSE`. logical
- `g_direction`: optional; default `"v"`. logical
- `total`: optional; default `FALSE`. logical
- `round`: optional; default `2`. 2
- `view`: optional; default `T`. 
- `xlsx`: optional; default `NULL`. 
- `pvalue`: optional; default `TRUE`. 

## reg_table
Title: for svyglm
Usage: `reg_table(fit, round = 2, style = 2, x = NULL, view = T, xlsx = NULL)`
- `fit`: required. fit
- `round`: optional; default `2`. 2
- `style`: optional; default `2`. integer
- `x`: optional; default `NULL`. x varaibles
- `view`: optional; default `T`. logical
- `xlsx`: optional; default `NULL`. 

## RCS
Title: RCS
Usage: `RCS(   ...,   nknots = NULL,   reference = "median",   by = NULL,   conf.int = 0.95,   ref.zero = TRUE,   log = TRUE )`
- `...`: optional. one or more regression
- `nknots`: optional; default `NULL`. number of knots
- `reference`: optional; default `"median"`. reference, default is median
- `by`: optional; default `NULL`. one or more variable
- `conf.int`: optional; default `0.95`. 
- `ref.zero`: optional; default `TRUE`. 
- `log`: optional; default `TRUE`. 

## stratum_model
Title: 建立分层模型
Usage: `stratum_model(   object,   time = NULL,   y,   x,   stratum = NULL,   adjust = NULL,   p = TRUE,   round = 3,   view = TRUE,   xlsx = NULL,   interaction = TRUE )`
- `object`: required. 数据分析的对象，object=d，或者object=nhs
- `time`: optional; default `NULL`. 时间变量，仅仅在cox回归的时候使用，线性回归和logistic回归不使用
- `y`: required. y变量，例如y='goal'
- `x`: required. x变量，例如x='x'
- `stratum`: optional; default `NULL`. 要分层的变量，注意分层变量必须是分类变量，连续变量是无法进行分层的，例如stratum=c('s1','s2','s3')
- `adjust`: optional; default `NULL`. 要调整的变量，例如adjust = c('a1','a2','a3')
- `p`: optional; default `TRUE`. 逻辑值，是否显示p值
- `round`: optional; default `3`. 设置小数点，默认是3位小数
- `view`: optional; default `TRUE`. 逻辑值，是否在Viewer窗口中显示结果
- `xlsx`: optional; default `NULL`. 赋值可以把结果写到excel里面，例如xlsx = "我的结果.xlsx"
- `interaction`: optional; default `TRUE`. 逻辑值，是否进行交互检验

## diag_DM
Title: attach Diabetes Mellitus
Usage: `diag_DM(   data,   years,   told = TRUE,   HbA1c = TRUE,   fast_glu = TRUE,   OGTT2 = TRUE,   rand_glu = TRUE,   drug = TRUE,   DM1 = FALSE,   cat = TRUE,   Year = FALSE,   join = "left",   exclude_Pregnant = TRUE )`
- `data`: required. data
- `years`: required. years
- `told`: optional; default `TRUE`. logical or character
- `HbA1c`: optional; default `TRUE`. logical or character
- `fast_glu`: optional; default `TRUE`. logical or character
- `OGTT2`: optional; default `TRUE`. logical or character
- `rand_glu`: optional; default `TRUE`. logical or character
- `drug`: optional; default `TRUE`. logical or character
- `DM1`: optional; default `FALSE`. logical
- `cat`: optional; default `TRUE`. logical
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join
- `exclude_Pregnant`: optional; default `TRUE`. logical whether to exclude pregant

## diag_Hypertension
Title: attach Hypertension
Usage: `diag_Hypertension(   data,   years,   told = TRUE,   drug = TRUE,   bpx = TRUE,   method = c("mean", "times"),   systolic = 140,   diastolic = 90,   n = 3,   component = FALSE,   yes1 = FALSE,   cat = TRUE,   Year = FALSE,   join = "left" )`
- `data`: required. data
- `years`: required. years
- `told`: optional; default `TRUE`. logical or character
- `drug`: optional; default `TRUE`. logical or character
- `bpx`: optional; default `TRUE`. logical or character
- `method`: optional; default `c("mean", "times")`. mean or times
- `systolic`: optional; default `140`. 140
- `diastolic`: optional; default `90`. 90
- `n`: optional; default `3`. number of test for diagnose hypertension
- `component`: optional; default `FALSE`. logical
- `yes1`: optional; default `FALSE`. logical
- `cat`: optional; default `TRUE`. logical
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join

## diag_CKD
Title: chronic kidney disease
Usage: `diag_CKD(   data,   years,   ckd = c("A2", "G3a"),   show_CKD = TRUE,   show_prognosis = TRUE,   show_ACR = FALSE,   show_eGFR = FALSE,   eGFR_method = "CKD_EPI_Scr_2009",   yes1 = FALSE,   Year = FALSE,   join = "left" )`
- `data`: required. data
- `years`: required. years
- `ckd`: optional; default `c("A2", "G3a")`. the lowest diagnosis standard
- `show_CKD`: optional; default `TRUE`. logical
- `show_prognosis`: optional; default `TRUE`. logical
- `show_ACR`: optional; default `FALSE`. logical
- `show_eGFR`: optional; default `FALSE`. logical
- `eGFR_method`: optional; default `"CKD_EPI_Scr_2009"`. one of CKD_EPI_Scr_2021(default), CKD_EPI_Scr_2009, MDRD_2007, MDRD_2000, MDRD_1999, CKD_EPI_SCysC CKD_EPI_Scr_SCysC, Schwartz, BIS1_Scr, BIS2_Scr_SCysC, Cockcroft_Gault,
- `yes1`: optional; default `FALSE`. logical
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join

## diag_CVD
Title: Cardiovascular Disease
Usage: `diag_CVD(data, years, Year = FALSE, join = "left")`
- `data`: required. data
- `years`: required. years
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join

## diag_MetS
Title: Attach Metabolic Syndrome
Usage: `diag_MetS(   data,   years,   methods = c("ATP", "IDF2006", "IDF2009", "Harm"),   component = FALSE,   yes1 = FALSE,   join = "left",   Year = FALSE,   cat = TRUE )`
- `data`: required. data
- `years`: required. years
- `methods`: optional; default `c("ATP", "IDF2006", "IDF2009", "Harm")`. ATP or IDF or Harm
- `component`: optional; default `FALSE`. logical
- `yes1`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join
- `Year`: optional; default `FALSE`. logical
- `cat`: optional; default `TRUE`. logical

## dex_HEI
Title: Calculate Healthy Eating Index
Usage: `dex_HEI(   data,   years,   version = c("2015", "2010"),   method = c("ssum", "pratio"),   dietary = c("tot", "iff"),   day = 1,   both2days = F,   varLabel = FALSE,   energy = TRUE,   component = TRUE,   density = FALSE,   seed = NULL )`
- `data`: required. data to be attached
- `years`: required. years
- `version`: optional; default `c("2015", "2010")`. 2015 or 2010
- `method`: optional; default `c("ssum", "pratio")`. ssum or pratio. ssum: simple sum, pratio: population ratio
- `dietary`: optional; default `c("tot", "iff")`. tot or iff
- `day`: optional; default `1`. 1 or 2 for per day, 1 and 2 for per person
- `both2days`: optional; default `F`. 
- `varLabel`: optional; default `FALSE`. (for ssum) logical. whether to add variable label to HEI data
- `energy`: optional; default `TRUE`. (for ssum) logical. whether to keep energy column
- `component`: optional; default `TRUE`. (for ssum) logical. whether to keep component columns
- `density`: optional; default `FALSE`. (for ssum) logical. whether to keep density columns
- `seed`: optional; default `NULL`. (for pratio) seed

## dex_DII
Title: calculate dietary inflammatory index
Usage: `dex_DII(   data,   years,   day = 1,   rawComponet = FALSE,   both2days = F,   cat = TRUE,   Year = FALSE,   join = "left" )`
- `data`: required. dataframe or list to be attarched
- `years`: required. years
- `day`: optional; default `1`. 1
- `rawComponet`: optional; default `FALSE`. logical, whether to keep raw componet data
- `both2days`: optional; default `F`. 
- `cat`: optional; default `TRUE`. logical
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join

## dex_LE8
Title: Life Essential 8 age over and equal 20 years population
Usage: `dex_LE8(data, years, day = 1, componet = FALSE, Year = FALSE, join = "left")`
- `data`: required. data
- `years`: required. years
- `day`: optional; default `1`. 1 or c(1,2) for hei
- `componet`: optional; default `FALSE`. logical
- `Year`: optional; default `FALSE`. logical
- `join`: optional; default `"left"`. join

## dex_Frailty
Title: Frailty Index
Usage: `dex_Frailty(data, years, component = FALSE)`
- `data`: required. data
- `years`: required. years
- `component`: optional; default `FALSE`. logical. whether to keep 49 components


