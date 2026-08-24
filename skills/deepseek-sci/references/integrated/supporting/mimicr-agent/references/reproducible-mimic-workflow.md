# Integrated supporting reference: mimicr-agent/references/reproducible-mimic-workflow.md

> Embedded source: `embedded-source/mimicr-agent/references/reproducible-mimic-workflow.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# MIMIC 可重复科研工作流

这套工作流默认解决四类高频问题：

1. 换台电脑就跑不了
   - 解决工具：Positron 项目根目录 + `here::here()`
2. 包更新之后结果悄悄变了
   - 解决工具：`renv`
3. 不知道上周的代码和这周有什么区别
   - 解决工具：Git
4. 分析做完还要手动搬运数字进报告
   - 解决工具：Quarto

## 目录结构

推荐项目结构：

```text
my_project/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── 00_setup.R
│   ├── 01_cohort.R
│   ├── 02_exposure.R
│   ├── 03_outcome.R
│   ├── 04_covariates.R
│   ├── 05_model.R
│   └── 06_visualize.R
├── reports/
│   └── analysis_report.qmd
├── outputs/
│   ├── figures/
│   └── tables/
├── refs/
│   └── codebook/
├── renv.lock
├── .gitignore
└── README.md
```

## 路径规则

不要在分析脚本里写：

```r
setwd("LOCAL_PATH")
```

项目代码里的文件路径统一改成：

```r
library(here)
readr::read_csv(here("data", "processed", "analytic_dat.csv"))
ggplot2::ggsave(here("outputs", "figures", "figure1.tiff"), dpi = 300)
```

数据库根目录单独管理，不和项目内文件路径混在一起：

```r
mimic_root <- normalizePath(
  Sys.getenv("MIMIC_DB_ROOT", unset = "LOCAL_PATH"),
  winslash = "/",
  mustWork = FALSE
)
mimicR430::config_path(mimic_root)
```

## 包版本规则

项目初始化后立即执行：

```r
renv::init()
```

新增或更新包后执行：

```r
renv::snapshot()
```

在新电脑或新环境恢复：

```r
renv::restore()
```

必须提交：

- `renv.lock`

不必提交：

- `renv/library/`

## Git 规则

最低要求掌握：

```bash
git status
git add scripts/05_model.R
git commit -m "update main model covariates and subgroup analysis"
git log --oneline
```

提交信息要写清楚改了什么，不能只写 `update`。

## Quarto 规则

Quarto 文件里把文字、代码、表格和图放在一起。内联结果要自动更新，不要手工把数字搬进 Word。

示例：

```markdown
---
title: "MIMIC Analysis Report"
format:
  html:
    toc: true
    code-fold: true
execute:
  echo: false
  warning: false
---

## Cohort Summary

```{r}
#| label: load-analytic-data
library(here)
analytic_dat <- readr::read_csv(here("data", "processed", "analytic_dat.csv"))
```

纳入样本量为 `r nrow(analytic_dat)` 例。
```

渲染命令：

```bash
quarto render reports/analysis_report.qmd
```

## 大数据与并发规则

默认按“大数据优先、稳定优先、分块优先”来写 R 代码：

```r
library(data.table)
library(future)
library(future.apply)

n_workers <- max(1L, future::availableCores() - 1L)
future::plan(future::multisession, workers = n_workers)
data.table::setDTthreads(threads = n_workers)
```

执行规则：

1. 优先只提取需要的列，不要把宽表整张读进内存。
2. 每完成一个昂贵提取步骤，立即把中间结果落盘到 `data/intermediate/`。
3. 并发只用于相互独立的任务，不要对一个超大对象盲目并发复制。
4. 优先使用 `data.table` 做大表过滤、连接和聚合。
5. 报告和出图脚本只读最终分析数据，不反复重跑原始大表提取。

## RDS 规则

把 `.rds` 当作模块级缓存和分析阶段交接格式：

1. `01_cohort.R` 结束时保存 `cohort_dt.rds`
2. `02_exposure.R` 结束时保存 `exposure_dt.rds`
3. `03_outcome.R` 结束时保存 `analytic_dt.rds`
4. 如果要覆盖已有 `.rds`，先备份旧文件，再写新文件
5. 最好把“覆盖前备份”写进保存函数本身，而不是只靠手工记忆

## 项目初始化

优先用本 skill 的初始化脚本：

```powershell
& 'LOCAL_PATH' 'LOCAL_PATH' --root 'LOCAL_PATH'
```

这个脚本会创建目录、初始化 `renv`、写 `.gitignore`、写 `README.md` 和 Quarto 报告骨架。

