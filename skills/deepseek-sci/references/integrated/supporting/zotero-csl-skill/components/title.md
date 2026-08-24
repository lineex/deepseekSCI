# Integrated supporting reference: zotero-csl-skill/components/title.md

> Embedded source: `embedded-source/zotero-csl-skill/components/title.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 标题格式

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| article-journal | 格式 | `plain` / `quotes` / `italic` | 视风格而定 | 期刊文章标题的格式 |
| book | 格式 | `plain` / `italic` / `书名号` | 视风格而定 | 书籍标题的格式 |
| chapter | 格式 | `plain` / `quotes` | 视风格而定 | 章节标题的格式 |
| thesis | 格式 | `plain` / `quotes` / `italic` | 视风格而定 | 学位论文标题的格式 |
| webpage | 格式 | `plain` / `italic` | 视风格而定 | 网页标题的格式 |
| 是否双语 | 设计决策 | 是/否 | — | 中文用书名号 `《》` 和引号 `""`，英文用 italic 和 quotes |

## 模板

### 纯文本（所有类型无格式）

所有文献类型标题均为纯文本，无引号、无斜体、无书名号。

```xml
<macro name="title">
  <text variable="title"/>
</macro>
```

### 英文学术（book=italic, article=quotes）

典型输出：
- article-journal: "The Role of Institutions in Growth"
- book: *The Wealth of Nations*
- thesis: "Essays on Economic Growth", Ph.D. Dissertation
- webpage: *Policy Brief on Climate*

```xml
<macro name="title-en">
  <choose>
    <if type="article-journal article-magazine article-newspaper chapter paper-conference report" match="any">
      <text variable="title" text-case="title" quotes="true"/>
    </if>
    <else-if type="thesis">
      <group delimiter=", ">
        <text variable="title" text-case="title" quotes="true"/>
        <choose>
          <if variable="genre">
            <text variable="genre" text-case="title"/>
          </if>
          <else>
            <text value="Ph.D. Dissertation"/>
          </else>
        </choose>
      </group>
    </else-if>
    <else-if type="post post-weblog webpage" match="any">
      <text variable="title" text-case="title" font-style="italic"/>
    </else-if>
    <else>
      <!-- book, report 等独立出版物 -->
      <text variable="title" text-case="title" font-style="italic"/>
    </else>
  </choose>
</macro>
```

> **说明**：`quotes="true"` 使用 locale 中定义的引号字符（英文默认为 `""`，中文可配置为 `""`）。`text-case="title"` 将标题转为 Title Case。

### 中文学术（book=书名号《》, article=引号""）

典型输出：
- article-journal: "制度变迁与经济增长"
- book: 《国富论》
- webpage: "气候政策简报"

```xml
<macro name="title-zh">
  <choose>
    <if type="article-journal article-magazine article-newspaper" match="any">
      <text variable="title" quotes="true"/>
    </if>
    <else-if type="post post-weblog webpage" match="any">
      <text variable="title" quotes="true"/>
    </else-if>
    <else>
      <!-- book, chapter, thesis 等使用书名号 -->
      <text variable="title" prefix="《" suffix="》"/>
    </else>
  </choose>
</macro>
```

> **说明**：中文引号通过 locale 定义 `<term name="open-quote">"</term>` 和 `<term name="close-quote">"</term>` 实现，`quotes="true"` 会自动使用 locale 引号。书名号则通过 `prefix`/`suffix` 手动添加。

需要配合的 locale 定义：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="open-quote">"</term>
    <term name="close-quote">"</term>
    <term name="open-inner-quote">'</term>
    <term name="close-inner-quote">'</term>
  </terms>
</locale>
```

### 双语（title-en + title-zh）

完整双语方案，包含 volume 信息和 edition 处理：

```xml
<macro name="title-en">
  <choose>
    <if type="article-journal article-magazine article-newspaper chapter paper-conference report" match="any">
      <text variable="title" text-case="title" quotes="true"/>
    </if>
    <else-if type="thesis">
      <group delimiter=", ">
        <text variable="title" text-case="title" quotes="true"/>
        <choose>
          <if variable="genre">
            <text variable="genre" text-case="title"/>
          </if>
          <else>
            <text value="Ph.D. Dissertation"/>
          </else>
        </choose>
      </group>
    </else-if>
    <else-if type="collection manuscript personal_communication software" match="any">
      <text variable="title" text-case="title"/>
    </else-if>
    <else-if type="post post-weblog webpage" match="any">
      <text variable="title" text-case="title" font-style="italic"/>
    </else-if>
    <else>
      <group delimiter=", ">
        <text variable="title" text-case="title" font-style="italic"/>
        <text macro="volume-en"/>
      </group>
    </else>
  </choose>
</macro>

<macro name="title-zh">
  <choose>
    <if type="article-journal article-magazine article-newspaper" match="any">
      <text variable="title" quotes="true"/>
    </if>
    <else-if type="post post-weblog webpage" match="any">
      <text variable="title" quotes="true"/>
    </else-if>
    <else>
      <text variable="title" prefix="《" suffix="》"/>
      <choose>
        <if variable="container-title" match="none">
          <text macro="edition-zh" prefix="（" suffix="）"/>
          <text macro="volume-zh"/>
        </if>
      </choose>
    </else>
  </choose>
</macro>
```

## 注意事项

1. **`quotes="true"` vs 手动引号**：始终使用 `quotes="true"` 而非手动添加引号字符，这样可以通过 locale 统一控制引号样式，也能正确处理嵌套引号（inner-quote）。
2. **书名号只能手动添加**：CSL 没有内置的书名号支持，必须通过 `prefix="《"` `suffix="》"` 实现。
3. **`text-case="title"`**：仅对英文有效，会将标题转为 Title Case。中文宏中不应使用此属性。
4. **thesis 的 genre 字段**：用于区分硕士/博士论文。若用户未填写 genre，英文默认输出 "Ph.D. Dissertation"，中文可通过 locale term `<term name="thesis">博士论文</term>` 控制。
5. **book 类型的 volume**：英文中 volume 信息附加在标题后（如 *Title, Vol. 2*），中文中 volume 放在书名号之后（如《书名》第2卷）。
6. **classic 类型**：古籍类型在中文中有特殊处理（年代前缀、卷册分层），需要单独处理，参见参考 CSL 文件中的 `title-zh` 宏。

