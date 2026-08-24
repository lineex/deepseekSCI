# Integrated supporting reference: zotero-csl-skill/components/publisher.md

> Embedded source: `embedded-source/zotero-csl-skill/components/publisher.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 出版信息

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| format | 格式 | `"Place: Publisher"` / `"Publisher, Place"` / 仅 Publisher | 视风格而定 | 出版地与出版社的排列和连接方式 |
| 是否双语 | 设计决策 | 是/否 | — | 中文和英文出版社格式基本一致，主要差异在学位论文处理 |

## 模板

### 标准：New York: Academic Press

典型输出：`New York: Academic Press`

```xml
<macro name="publisher">
  <group delimiter=": ">
    <text variable="publisher-place"/>
    <text variable="publisher"/>
  </group>
</macro>
```

也可以反转顺序（Publisher, Place）：

```xml
<macro name="publisher">
  <group delimiter=", ">
    <text variable="publisher"/>
    <text variable="publisher-place"/>
  </group>
</macro>
```

### 仅出版社

典型输出：`Academic Press`

参考文件中英文出版社宏的实际做法——只输出出版社名称，不含出版地：

```xml
<macro name="publisher-en">
  <text variable="publisher"/>
</macro>
```

> **说明**：部分人文社科风格（如太平洋学报）英文引用中只需要出版社名称，不要求出版地。

### 中文出版社

典型输出：`商务印书馆` / `北京：商务印书馆`

```xml
<!-- 仅出版社 -->
<macro name="publisher-zh">
  <text variable="publisher"/>
</macro>

<!-- 含出版地 -->
<macro name="publisher-zh">
  <group delimiter="：">
    <text variable="publisher-place"/>
    <text variable="publisher"/>
  </group>
</macro>
```

> **说明**：中文使用全角冒号 `：` 连接出版地与出版社。部分风格（如 GB/T 7714）要求包含出版地，部分风格（如太平洋学报）省略出版地。

### 学位论文（仅学校名）

典型输出（英文）：`Harvard University`
典型输出（中文）：`北京大学，博士论文`

学位论文的 `publisher` 字段通常存储学校名。

```xml
<!-- 英文学位论文 -->
<macro name="publisher-en">
  <text variable="publisher"/>
</macro>

<!-- 中文学位论文（含论文类型） -->
<macro name="publisher-zh">
  <choose>
    <if type="thesis">
      <text variable="publisher"/>
      <group delimiter="，">
        <choose>
          <if variable="genre">
            <text variable="genre"/>
          </if>
          <else>
            <text term="thesis"/>
          </else>
        </choose>
      </group>
    </if>
    <else>
      <text variable="publisher"/>
    </else>
  </choose>
</macro>
```

> **说明**：英文学位论文的类型信息（Ph.D. Dissertation）通常在标题宏中处理（参见 title.md），出版社宏只输出学校名。中文学位论文的类型标签（博士论文/硕士论文）放在出版社宏中，通过 `genre` 变量获取用户填写的类型，无 genre 时回退到 locale term `<term name="thesis">博士论文</term>`。

需要配合的 locale 定义：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="thesis">博士论文</term>
  </terms>
</locale>
```

### 双语完整方案（publisher-en + publisher-zh）

```xml
<macro name="publisher-en">
  <text variable="publisher"/>
</macro>

<macro name="publisher-zh">
  <choose>
    <if type="thesis">
      <text variable="publisher"/>
      <group delimiter="，">
        <choose>
          <if variable="genre">
            <text variable="genre"/>
          </if>
          <else>
            <text term="thesis"/>
          </else>
        </choose>
      </group>
    </if>
    <else>
      <text variable="publisher"/>
    </else>
  </choose>
</macro>
```

### 会议/事件出版信息

会议论文若无 container-title，则出版信息来自 event 相关字段：

```xml
<!-- 英文会议 -->
<macro name="event-en">
  <choose>
    <if variable="container-title" match="none">
      <group delimiter=", ">
        <group delimiter=" ">
          <text value="Paper Prepared for"/>
          <text variable="event-title"/>
        </group>
        <names variable="organizer">
          <name delimiter="、"/>
          <substitute>
            <text variable="publisher"/>
            <text variable="publisher-place"/>
          </substitute>
        </names>
        <choose>
          <if variable="event-date">
            <date variable="event-date" form="text"/>
          </if>
          <else>
            <date variable="issued" form="text"/>
          </else>
        </choose>
      </group>
    </if>
  </choose>
</macro>

<!-- 中文会议 -->
<macro name="event-zh">
  <choose>
    <if variable="container-title" match="none">
      <group delimiter="，">
        <group>
          <text variable="event-title"/>
          <text value="论文"/>
        </group>
        <names variable="organizer">
          <name delimiter="、"/>
          <substitute>
            <text variable="publisher"/>
            <text variable="publisher-place"/>
          </substitute>
        </names>
        <choose>
          <if variable="event-date">
            <date variable="event-date" form="text"/>
          </if>
          <else>
            <date variable="issued" form="text"/>
          </else>
        </choose>
      </group>
    </if>
  </choose>
</macro>
```

## 注意事项

1. **出版地的取舍**：不同引用风格对出版地的要求不同。APA 第 7 版已取消出版地要求，GB/T 7714 仍要求出版地。根据目标风格决定是否包含 `publisher-place`。
2. **中英文标点差异**：英文用半角冒号+空格 `": "`，中文用全角冒号 `"："`。
3. **学位论文的特殊性**：`publisher` 在学位论文中存储的是学校名而非出版社名。英文论文类型放在 title 宏中，中文论文类型放在 publisher 宏中——这是两种语言风格的习惯差异。
4. **`publisher-place` 的多用途**：该变量在不同文献类型中含义不同——书籍中是出版地，报纸中是发行地，档案中是馆藏地。容器宏和出版社宏需要注意不要重复输出。
5. **缺失值处理**：当 `publisher` 或 `publisher-place` 为空时，`<group>` 会自动抑制分隔符。不需要额外的条件判断。
6. **与容器宏的配合**：在 entry-layout 宏中，出版社信息通常跟在容器信息之后。对于期刊文章，不需要出版社信息（期刊名已足够）；对于书籍和章节，出版社信息必不可少。

