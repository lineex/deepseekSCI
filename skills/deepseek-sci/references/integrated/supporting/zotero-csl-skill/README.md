# Integrated supporting reference: zotero-csl-skill/README.md

> Embedded source: `embedded-source/zotero-csl-skill/README.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# CSL Style Generator — Claude Code Skill

[English](#english) | [中文](#中文)

<div align="center">

| 公众号 / WeChat Official Account | 微信群 / WeChat Group | Discord |
|:---:|:---:|:---:|
| <img src="MP.jpg" width="200"/> | <img src="0320.jpg" width="200"/> | [Join Discord](https://discord.gg/tGd5vTDASg) |
| 未来论文实验室 / Future Paper Lab | 扫码加入交流群 / Scan to join | English & 中文 |

</div>

---

<a id="中文"></a>

## 中文

### 简介

这是一个 [Claude Code](https://claude.com/claude-code) Skill，用于根据用户描述的引用格式，自动生成 [Zotero](https://www.zotero.org/) 可用的 CSL（Citation Style Language）样式文件。

支持从标准预设（GB/T 7714、APA、IEEE 等）一键生成，也支持根据用户提供的参考文献示例反推格式参数，生成完全自定义的 `.csl` 文件。

### 功能特性

- **7 种内置预设**：GB/T 7714 顺序编码 / 著者-出版年、APA 7、Chicago Notes、IEEE、MLA 9、中文社科脚注
- **模块化组件**：作者、标题、日期、容器、卷期页、出版信息、DOI/URL、正文引用、文献列表、中英文 locale，共 11 个可组合组件
- **中英文双语支持**：支持按 `language` 字段自动切换中英文格式（中文顿号、书名号、"等" vs 英文逗号、斜体、"et al."）
- **三阶段自动校验**：XML 语法检查 → CSL RelaxNG Schema 验证 → 逻辑规则审核（R1-R6）
- **实时预览**：基于 citeproc-py 渲染真实的 citation 和 bibliography 输出
- **内置测试数据**：包含 10 条覆盖期刊、书籍、会议、章节、网页、学位论文、报纸、报告以及中文条目的测试数据

### 项目结构

```
csl-skill/
├── SKILL.md                  # Skill 入口定义与工作流
├── presets/                   # 预设格式配方
│   ├── gbt7714-numeric.md     #   GB/T 7714 顺序编码
│   ├── gbt7714-author-date.md #   GB/T 7714 著者-出版年
│   ├── apa7.md                #   APA 第 7 版
│   ├── chicago-notes.md       #   Chicago 脚注
│   ├── ieee.md                #   IEEE
│   ├── mla9.md                #   MLA 第 9 版
│   └── chinese-note.md        #   中文社科脚注
├── components/                # 可组合的组件模板
│   ├── name.md                #   作者/姓名格式
│   ├── title.md               #   标题格式
│   ├── date.md                #   日期格式
│   ├── container.md           #   期刊/书籍容器
│   ├── locators.md            #   卷/期/页码
│   ├── publisher.md           #   出版信息
│   ├── access.md              #   DOI/URL
│   ├── citation.md            #   正文引用布局
│   ├── bibliography.md        #   参考文献列表布局
│   ├── locale-zh.md           #   中文本地化术语
│   └── locale-en.md           #   英文本地化术语
├── scripts/                   # 工具脚本
│   ├── validate_csl.py        #   CSL 校验（XML + Schema + 逻辑规则）
│   ├── preview_csl.py         #   CSL 预览（citeproc-py 渲染）
│   ├── test_data.json         #   10 条测试数据（中英文混合）
│   └── schema/v1.0.2/         #   CSL 1.0.2 RelaxNG Schema
├── validate/                  # 校验规则
│   ├── rules.md               #   R1-R7 逻辑一致性规则
│   └── schema-checklist.md    #   CSL 1.0.2 属性枚举速查表
├── output/                    # 生成的 CSL 文件
└── references/                # 参考 CSL 样式
```

### 使用方法

在 Claude Code 中使用 `/csl` 命令触发：

```
/csl GB/T 7714 顺序编码格式
```

```
/csl 帮我生成一个 APA 第 7 版的引用样式
```

```
/csl 我需要一个自定义格式，参考文献示例如下：
[1] 张伟, 李明. 基于深度学习的文本分析[J]. 计算机学报, 2024, 47(5): 1023-1035.
[2] Smith J. Introduction to Machine Learning. 3rd ed. New York: Academic Press, 2023.
```

#### 工作流程

1. **收集信息** — 确认引用方式（上标编号 / 行内编号 / 脚注）+ 参考文献示例
2. **解析需求** — 匹配预设或从示例反推参数
3. **读取配方** — 从 presets 或 components 获取格式参数
4. **生成 CSL** — 按骨架组装完整 XML 文件
5. **校验** — 三阶段自动校验，修复至通过
6. **预览** — 渲染真实输出，等待用户确认

### 依赖

校验和预览脚本需要以下 Python 依赖：

```bash
pip install lxml rnc2rng citeproc-py
```

| 包 | 用途 |
|---|---|
| `lxml` | XML 解析与 RelaxNG Schema 验证 |
| `rnc2rng` | 将 `.rnc` Schema 转换为 `.rng` 格式 |
| `citeproc-py` | CSL 渲染引擎，用于预览 |

### 手动使用脚本

```bash
# 校验 CSL 文件
python scripts/validate_csl.py output/my-style.csl

# 详细输出
python scripts/validate_csl.py --verbose output/my-style.csl

# 预览渲染效果
python scripts/preview_csl.py output/my-style.csl

# 使用自定义测试数据预览
python scripts/preview_csl.py output/my-style.csl --data my_data.json
```

---

<a id="english"></a>

## English

### Overview

A [Claude Code](https://claude.com/claude-code) Skill that generates [Zotero](https://www.zotero.org/)-compatible CSL (Citation Style Language) style files from natural language descriptions.

Supports one-click generation from built-in presets (GB/T 7714, APA, IEEE, etc.) as well as fully custom `.csl` files reverse-engineered from user-provided reference examples.

### Features

- **7 built-in presets**: GB/T 7714 Numeric / Author-Date, APA 7, Chicago Notes, IEEE, MLA 9, Chinese Social Science Notes
- **Modular components**: 11 composable building blocks — author, title, date, container, locators, publisher, access, citation, bibliography, zh-locale, en-locale
- **Bilingual support**: Automatic Chinese/English format switching based on the `language` field (Chinese: dunhao, guillemets, "等"; English: commas, italics, "et al.")
- **3-stage validation**: XML syntax check → CSL RelaxNG Schema validation → Logic rules audit (R1-R6)
- **Live preview**: Real citation and bibliography rendering via citeproc-py
- **Built-in test data**: 10 entries covering journal articles, books, conferences, chapters, webpages, theses, newspapers, reports, and Chinese-language items

### Project Structure

```
csl-skill/
├── SKILL.md                  # Skill entry point & workflow definition
├── presets/                   # Format presets
│   ├── gbt7714-numeric.md     #   GB/T 7714 Numeric
│   ├── gbt7714-author-date.md #   GB/T 7714 Author-Date
│   ├── apa7.md                #   APA 7th Edition
│   ├── chicago-notes.md       #   Chicago Notes
│   ├── ieee.md                #   IEEE
│   ├── mla9.md                #   MLA 9th Edition
│   └── chinese-note.md        #   Chinese Social Science Notes
├── components/                # Composable component templates
│   ├── name.md                #   Author/name formatting
│   ├── title.md               #   Title formatting
│   ├── date.md                #   Date formatting
│   ├── container.md           #   Journal/book container
│   ├── locators.md            #   Volume/issue/page
│   ├── publisher.md           #   Publisher info
│   ├── access.md              #   DOI/URL
│   ├── citation.md            #   In-text citation layout
│   ├── bibliography.md        #   Bibliography layout
│   ├── locale-zh.md           #   Chinese locale terms
│   └── locale-en.md           #   English locale terms
├── scripts/                   # Utility scripts
│   ├── validate_csl.py        #   CSL validator (XML + Schema + logic)
│   ├── preview_csl.py         #   CSL preview (citeproc-py rendering)
│   ├── test_data.json         #   10 test entries (mixed zh/en)
│   └── schema/v1.0.2/         #   CSL 1.0.2 RelaxNG Schema files
├── validate/                  # Validation rules
│   ├── rules.md               #   R1-R7 logic consistency rules
│   └── schema-checklist.md    #   CSL 1.0.2 attribute reference
├── output/                    # Generated CSL files
└── references/                # Reference CSL styles
```

### Usage

Invoke with the `/csl` command in Claude Code:

```
/csl GB/T 7714 numeric style
```

```
/csl Generate an APA 7th edition citation style
```

```
/csl I need a custom format. Here are sample references:
[1] Zhang W, Li M. Deep learning text analysis[J]. Journal of Computers, 2024, 47(5): 1023-1035.
[2] Smith J. Introduction to Machine Learning. 3rd ed. New York: Academic Press, 2023.
```

#### Workflow

1. **Gather info** — Confirm citation style (superscript / inline / footnote) + reference examples
2. **Parse requirements** — Match a preset or reverse-engineer parameters from examples
3. **Load recipe** — Retrieve format parameters from presets or components
4. **Generate CSL** — Assemble complete XML from the skeleton structure
5. **Validate** — 3-stage automatic validation, fix until pass
6. **Preview** — Render real output, await user confirmation

### Dependencies

The validation and preview scripts require the following Python packages:

```bash
pip install lxml rnc2rng citeproc-py
```

| Package | Purpose |
|---|---|
| `lxml` | XML parsing and RelaxNG Schema validation |
| `rnc2rng` | Convert `.rnc` schema to `.rng` format |
| `citeproc-py` | CSL rendering engine for preview |

### Running Scripts Manually

```bash
# Validate a CSL file
python scripts/validate_csl.py output/my-style.csl

# Verbose output
python scripts/validate_csl.py --verbose output/my-style.csl

# Preview rendered output
python scripts/preview_csl.py output/my-style.csl

# Preview with custom test data
python scripts/preview_csl.py output/my-style.csl --data my_data.json
```

### Validation Rules

The validator checks 7 rule categories:

| Rule | Category | Description |
|------|----------|-------------|
| R1 | Structural completeness | Required elements: `<style>`, `<info>`, `<citation>`, `<layout>` |
| R2 | Macro integrity | All referenced macros must be defined; unused macros are warned |
| R3 | Class consistency | `class` attribute must match `citation-format` category |
| R4 | Parameter validity | `et-al-min` > `et-al-use-first`, valid enum values |
| R5 | Bilingual ordering | Locale-specific `<layout>` elements must precede the fallback |
| R6 | No residuals | No placeholder text `[TODO]`, no empty macros |
| R7 | Best practices | `<substitute>` in `<names>`, `<sort>` in `<bibliography>`, etc. |


