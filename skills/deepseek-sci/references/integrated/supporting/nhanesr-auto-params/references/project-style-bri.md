# Integrated supporting reference: nhanesr-auto-params/references/project-style-bri.md

> Embedded source: `embedded-source/nhanesr-auto-params/references/project-style-bri.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# BRI 项目代码风格规则

以下规则来自现有可运行脚本 `LOCAL_PATH`，用于指导后续 NHANES / `nhanesR` 代码生成保持同一项目手感。

## 1. 代码组织方式

- 先按模块分别生成结局、暴露、人口学、饮食、行为、体测、代谢等数据表
- 各模块先保持独立，再统一用 `reduce(left_join, by = "seqn")` 合并
- 合并后再做纳入标准、缺失剔除、重编码和分组
- 变量名尽量短且统一，分析对象常用 `d1`、`fi`、`bri`、`nhs`、`fit0` 等命名模式

## 2. 常见函数用法

- 结局定义：优先用 `diag_*`
- 暴露构造：优先用 `dex_*`
- 协变量：优先用 `db_*`
- 生存结局：优先用 `db_mort()` 构造 `time/status`
- 加权设计：优先用 `svy_design()`
- 基线表：优先用 `svy_tableone()`
- 分层交互：优先用 `stratum_model()`
- RCS：优先用 `svyglm(... + rcs())` 后接 `RCS()`
- 生存曲线：优先用 `svykm()` + `svy_kmplot()`
- ROC/AUC：优先用 `roc()`、`wauc()`、`wroc()`、`wroc.plot()`

## 3. 人口学与分组重编码

- 婚姻：常合并成 `Married` / `Nonmarried`
- 教育：常合并成 3 类
- PIR：常合并成 `< 1` / `>= 1`
- 年龄：敏感性或分层时常二分类为 `< 65` / `>= 65`
- BMI：常二分类为 `<30` / `>=30`
- 糖尿病：常转为 `yes` / `no`
- 结局或暴露分组：常用 `quant(x, n = 3/4, Q = TRUE, round = 3)` + `Recode()`

## 4. 权重与周期处理

- 如果使用 1999-2017 多周期合并，先在 `db_demo()` 中取出 `wtmec4yr` 和 `wtmec2yr`
- 1999-2002 常按 4 年权重处理，后续 2 年周期按 2 年权重处理
- 权重合并时采用按总年数比例缩放的手工写法
- `Year` 字段常保留，用于区分不同周期权重来源

## 5. 样本筛选习惯

- 先按年龄等大标准筛样本，再按结局/暴露/关键协变量逐层筛
- 每一步都习惯性查看 `nrow()`
- 进入模型前常用 `complete.cases()` 或逐变量 `!is.na()`
- 在剔除缺失前会检查 `colSums(is.na())`

## 6. 模型表达习惯

- 主模型常按 `fit0`、`fit1`、`fit2`、`fit3` 递进组织
- 模型中常保留趋势检验 `p4trend()`
- 分层模型常显式设置 `adjust` 和 `interaction = TRUE`
- 结果输出常伴随基线表、分层表、RCS、KM、Cox、ROC 多模块联动

## 7. 项目级默认分析骨架

1. 定义结局
2. 定义生存时间与状态
3. 生成暴露
4. 生成人口学和协变量
5. 合并数据
6. 统一重编码
7. 逐步筛样本
8. 构建 survey design
9. 输出基线表
10. 跑 crude / adjusted models
11. 跑分层与交互
12. 跑 RCS
13. 跑 KM / Cox
14. 跑 ROC / AUC


