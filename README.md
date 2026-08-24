# DeepSeekSCI Medical Research Agent

DeepSeekSCI 是一个可移植的单一 `SKILL.md` 医学科研 Agent。原 Codex 医学科研库中的 86 个配套技能及其 145 个文本/Python 支持文件已经合并到同一个技能目录，不依赖宿主平台再安装其他技能。能力覆盖研究思路发掘、可行性验证、医学文献检索、研究设计、Python 分析、论文写作、内部审稿、选刊与投稿准备。

## Cherry Studio 导入

### 方法一：GitHub 直接安装

在 Cherry Studio 的“资源/技能市场/GitHub”中粘贴下面这个 **SKILL.md 文件链接**：

```text
https://github.com/lineex/deepseekSCI/blob/main/skills/deepseek-sci/SKILL.md
```

GitHub 输入框识别的是具体 `SKILL.md` 文件地址，不是仓库首页地址。安装时会同时取得同目录下的 `references/`、`scripts/` 和 `assets/`，其中 `references/integrated/` 是已合并的全部配套能力正文与支持文件。

### 方法二：ZIP 本地导入

下载 [deepseek-sci-cherry-studio.zip](https://raw.githubusercontent.com/lineex/deepseekSCI/main/releases/deepseek-sci-cherry-studio.zip)，然后在 Cherry Studio 的“资源/技能/导入技能”中选择该 ZIP。

### 方法三：目录导入

下载或克隆本仓库后，选择 `skills/deepseek-sci` 目录。这个目录内直接包含 `SKILL.md`。

## 其他 Agent 软件

标准技能目录是 [`skills/deepseek-sci`](skills/deepseek-sci)。支持 Agent Skills/Claude Skills 目录协议的软件可导入该目录；只支持单提示文件的软件可读取其中的 `SKILL.md`，完整运行需要连同 `references/integrated/`、`scripts/` 和 `assets/` 一起保留。

## 构建原则

- Python 3.11+。
- 确定性自动化、数据处理、统计分析、文档生成和打包均使用 Python。
- SQL 只通过 Python 的 SQLite、DuckDB 或数据库客户端执行。
- 原始检索结果不可变保存，记录查询式、日期、命中数、导出数与哈希。
- 所有数据库连接遵循会话检查、查询转换、检索、翻页、详情、导出、全文和审计契约。

重新生成兼容 ZIP：

```text
python tools/package_skill.py
```

## 许可

[MIT License](LICENSE)
