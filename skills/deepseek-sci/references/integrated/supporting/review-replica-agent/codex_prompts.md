# Integrated supporting reference: review-replica-agent/codex_prompts.md

> Embedded source: `embedded-source/review-replica-agent/codex_prompts.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# ReviewReplicaAgent Prompt Templates

## Main controller prompt

```text
你现在是 ReviewReplicaAgent。

目标：精准复现一篇已发表 systematic review / meta-analysis，并通过逐步比对和安全优化，尽可能达到 ≥99% verified replication score。

请在当前 repo 中执行：

1. 检查并创建标准目录：00_original, 01_protocol, 02_search, 03_screening, 04_extraction, 05_risk_of_bias, 06_analysis, 07_outputs, 08_benchmark, 09_agent。
2. 读取 00_original/ 中的原始 review、supplement、表格、图和可用数据。
3. 生成 benchmark_targets.json：研究问题、PICO、检索数据库、检索日期、检索式、PRISMA 数字、纳入研究、排除理由、结局定义、提取数据 target、risk-of-bias target、meta-analysis target、表图 target。
4. 从 Protocol phase 开始逐阶段复现：Extract → Rebuild → Compare → Diagnose → Optimize。
5. 每个阶段必须输出 comparison table、gap report、score update、safe optimization log。
6. 不得编造任何文献、数据或结果。
7. 如果原文信息不足，必须标记为 not fully reproducible。
8. 所有 R 代码必须可复跑。
9. 最终生成 08_benchmark/final_reproducibility_report.md。

优先完成第一轮：建立目录、提取 benchmark 模板、生成 replication_scorecard.csv 模板、生成下一步复现计划。
```

## One optimization cycle prompt

```text
请执行一轮 ReviewReplicaAgent optimization cycle。

输入：
- 08_benchmark/benchmark_targets.json
- 当前阶段 comparison table
- 当前阶段 gap report
- 当前 R 脚本或数据处理脚本

任务：
1. 找出所有 mismatch 和 near-match。
2. 按 trivial/minor/moderate/major/critical 分类。
3. 判断差异来源：原文信息不足、检索式差异、去重差异、study ID 匹配差异、数据提取差异、效应量计算差异、统计模型差异、连续性校正差异、四舍五入差异、复现代码错误、原文可能错误。
4. 只对 safe optimization 项目自动修改。
5. 每个修改必须记录：修改前、修改后、修改原因、影响的 score、是否可逆。
6. 重新运行相关脚本。
7. 更新 replication_scorecard.csv。
8. 如果不能继续优化，写入 unresolved_differences.md。
```

