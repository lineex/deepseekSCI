# Integrated supporting reference: zotero-csl-skill/components/container.md

> Embedded source: `embedded-source/zotero-csl-skill/components/container.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 容器格式

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| journal | 格式 | `plain` / `italic` / `书名号` | 视风格而定 | 期刊名的格式 |
| book-in | 连接词 | `"in"` / `"//"` | 视风格而定 | 章节与所属书籍之间的连接方式 |
| conference | 连接词 | `"in"` / `"//"` | 视风格而定 | 会议论文与论文集之间的连接方式 |
| 是否双语 | 设计决策 | 是/否 | — | 中文用书名号包裹期刊名，英文用斜体；中文用冒号连接编者与书名 |

## 模板

### 英文期刊（斜体）

典型输出：`*American Economic Review*, Vol.112, No.3`

```xml
<macro name="container-periodical-en">
  <choose>
    <if type="article-newspaper">
      <text variable="container-title" text-case="title"/>
    </if>
    <else>
      <group delimiter=", ">
        <text variable="container-title" text-case="title" font-style="italic"/>
        <group>
          <label variable="volume" form="short" text-case="capitalize-first"/>
          <number variable="volume"/>
        </group>
        <group>
          <label variable="issue" form="short" text-case="capitalize-first"/>
          <number variable="issue"/>
        </group>
      </group>
    </else>
  </choose>
</macro>
```

> **说明**：`<label variable="volume" form="short"/>` 输出 "Vol."，`<label variable="issue" form="short"/>` 输出 "No."。报纸的 container-title 不使用斜体。

### 英文会议/章节（in Editor, Book Title）

典型输出：`in John Smith and Jane Doe eds., *Handbook of Economics*`

```xml
<macro name="container-booklike-en">
  <choose>
    <if variable="container-title">
      <group delimiter=" ">
        <text term="in"/>
        <group delimiter=", ">
          <names variable="editor">
            <name and="text"/>
            <label form="short" prefix=", "/>
          </names>
          <text variable="container-title" text-case="title" font-style="italic"/>
        </group>
      </group>
    </if>
  </choose>
</macro>
```

> **说明**：`<text term="in"/>` 输出小写 "in"。编者姓名使用正常顺序（Given Surname），`<label form="short"/>` 输出 "eds." 或 "ed."。

### GB/T 7714 风格（// 连接）

典型输出：`// 张三, 李四. 经济学手册`

GB/T 7714 标准使用 `//` 作为析出文献与来源文献的分隔符。

```xml
<macro name="container-booklike-gbt">
  <choose>
    <if variable="container-title">
      <group prefix="// ">
        <group delimiter=". ">
          <names variable="editor">
            <name delimiter=", "/>
          </names>
          <text variable="container-title"/>
        </group>
      </group>
    </if>
  </choose>
</macro>
```

### 中文期刊（书名号《》）

典型输出：`《太平洋学报》（北京），2024年第3期`

```xml
<macro name="container-periodical-zh">
  <group delimiter="，">
    <group>
      <text variable="container-title" prefix="《" suffix="》"/>
      <text variable="section" prefix="（" suffix="）"/>
      <text variable="publisher-place" prefix="（" suffix="）"/>
    </group>
    <group>
      <text macro="date-zh"/>
      <choose>
        <if variable="issue">
          <text macro="issue-zh"/>
        </if>
        <else>
          <text macro="volume-zh"/>
        </else>
      </choose>
    </group>
  </group>
</macro>
```

> **说明**：中文期刊的卷期信息直接跟在日期后面（如"2024年第3期"）。`section` 用于报纸的版面信息，`publisher-place` 用于区分同名期刊的出版地。

需要依赖的辅助宏：

```xml
<macro name="issue-zh">
  <choose>
    <if is-numeric="issue">
      <text value="第"/>
      <number variable="issue"/>
      <label variable="issue" form="short"/>
    </if>
    <else>
      <text variable="issue"/>
    </else>
  </choose>
</macro>

<macro name="volume-zh">
  <choose>
    <if is-numeric="volume">
      <text value="第"/>
      <number variable="volume"/>
      <label variable="volume" form="short"/>
    </if>
    <else>
      <text variable="volume"/>
    </else>
  </choose>
</macro>
```

### 中文章节/会议（冒号连接编者与书名）

典型输出：`张三、李四主编：《经济学手册》`

```xml
<macro name="container-booklike-zh">
  <group delimiter="：">
    <names variable="editor">
      <name delimiter="、"/>
      <label form="short"/>
    </names>
    <group>
      <choose>
        <if variable="container-title">
          <text variable="container-title" prefix="《" suffix="》"/>
          <choose>
            <if type="classic" match="none">
              <text macro="edition-zh" prefix="（" suffix="）"/>
              <text macro="volume-zh"/>
            </if>
          </choose>
        </if>
        <else-if type="paper-conference" variable="event-title" match="all">
          <text variable="event-title"/>
          <text value="论文"/>
        </else-if>
      </choose>
    </group>
  </group>
</macro>
```

> **说明**：中文用全角冒号 `：` 连接编者和书名。编者后附"主编"标签。会议论文若无 container-title 则使用 event-title 加"论文"。

### 双语完整方案（container-en + container-zh）

```xml
<!-- 英文期刊容器 -->
<macro name="container-periodical-en">
  <choose>
    <if type="article-newspaper">
      <text variable="container-title" text-case="title"/>
    </if>
    <else>
      <group delimiter=", ">
        <text variable="container-title" text-case="title" font-style="italic"/>
        <group>
          <label variable="volume" form="short" text-case="capitalize-first"/>
          <number variable="volume"/>
        </group>
        <group>
          <label variable="issue" form="short" text-case="capitalize-first"/>
          <number variable="issue"/>
        </group>
      </group>
    </else>
  </choose>
</macro>

<!-- 英文书籍类容器 -->
<macro name="container-booklike-en">
  <choose>
    <if variable="container-title">
      <group delimiter=" ">
        <text term="in"/>
        <group delimiter=", ">
          <names variable="editor">
            <name and="text"/>
            <label form="short" prefix=", "/>
          </names>
          <text variable="container-title" text-case="title" font-style="italic"/>
        </group>
      </group>
    </if>
  </choose>
</macro>

<!-- 中文期刊容器 -->
<macro name="container-periodical-zh">
  <group delimiter="，">
    <group>
      <text variable="container-title" prefix="《" suffix="》"/>
      <text variable="section" prefix="（" suffix="）"/>
      <text variable="publisher-place" prefix="（" suffix="）"/>
    </group>
    <group>
      <text macro="date-zh"/>
      <choose>
        <if variable="issue">
          <text macro="issue-zh"/>
        </if>
        <else>
          <text macro="volume-zh"/>
        </else>
      </choose>
    </group>
  </group>
</macro>

<!-- 中文书籍类容器 -->
<macro name="container-booklike-zh">
  <group delimiter="：">
    <names variable="editor">
      <name delimiter="、"/>
      <label form="short"/>
    </names>
    <group>
      <choose>
        <if variable="container-title">
          <text variable="container-title" prefix="《" suffix="》"/>
          <choose>
            <if type="classic" match="none">
              <text macro="edition-zh" prefix="（" suffix="）"/>
              <text macro="volume-zh"/>
            </if>
          </choose>
        </if>
        <else-if type="paper-conference" variable="event-title" match="all">
          <text variable="event-title"/>
          <text value="论文"/>
        </else-if>
      </choose>
    </group>
  </group>
</macro>
```

## 注意事项

1. **期刊 vs 书籍容器**：期刊文章（article-journal/article-magazine）使用期刊容器宏，章节（chapter）和会议论文（paper-conference）使用书籍类容器宏。在 entry-layout 宏中通过 `<choose>` 按类型调用不同的容器宏。
2. **`container-title` vs `collection-title`**：`container-title` 是直接包含当前文献的容器（如期刊名、论文集名），`collection-title` 是系列丛书名。中文丛书用书名号包裹。
3. **报纸容器**：中文报纸有特殊格式，包含出版地、版面号等信息，需要单独的宏处理（如 `container-newspaper-zh`）。
4. **`text-case="title"`**：仅对英文容器标题使用。中文不使用 text-case。
5. **卷期信息的位置**：英文中卷期跟在期刊名后（如 *Journal*, Vol.1, No.2），中文中卷期跟在日期后（如 2024年第3期）。
6. **`<text term="in"/>`**：在中文 locale 中可定义为"载"（`<term name="in">载</term>`），但实际中文学术引用中更常用冒号或 `//` 连接，而非"载"字。

