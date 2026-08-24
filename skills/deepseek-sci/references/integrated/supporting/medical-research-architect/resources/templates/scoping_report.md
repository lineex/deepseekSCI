# Integrated supporting reference: medical_research_architect/resources/templates/scoping_report.md

> Embedded source: `embedded-source/medical_research_architect/resources/templates/scoping_report.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Scoping & Gap Analysis Report

> **Purpose**: This report summarizes the literature landscape to confirm research novelty and identify potential innovation angles.

## Report Metadata
| Property | Value |
| :--- | :--- |
| **PICO Topic** | `[From PICO_definition.md]` |
| **Date** | `[DATE]` |
| **Version** | 1.0 |

---

## 1. Search Strategy

### Databases Searched
-   [x] **Zotero Local Library** (via `mcp_zotero-mcp_semantic_search`)
-   [x] **Zotero Global/Online** (via `mcp_zotero-mcp_search_library`)
-   [ ] PubMed (External - if applicable)
-   [ ] Cochrane Library (External - if applicable)

### Keywords Used
```
[Keyword 1], [Keyword 2], [Keyword 3], ...
```

### Filters Applied
-   **Date Range**: `[e.g., 2015 - Present]`
-   **Study Types**: `[e.g., RCT, Systematic Review, Meta-Analysis]`
-   **Language**: `[e.g., English]`

---

## 2. Key Findings from Literature

### Summary Table of Relevant Studies
| # | Title (Truncated) | Authors | Year | Study Type | Key Finding | Zotero Key |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
| 1 | `[Paper Title]` | `[First Author et al.]` | `[Year]` | `[RCT]` | `[Main conclusion]` | `[KEY]` |
| 2 | `[Paper Title]` | `[First Author et al.]` | `[Year]` | `[Review]` | `[Main conclusion]` | `[KEY]` |
| 3 | ... | ... | ... | ... | ... | ... |

### Key Themes Identified
1.  **Theme 1**: `[e.g., Most studies focus on short-term outcomes (< 6 months).]`
2.  **Theme 2**: `[e.g., Limited data on specific genetic sub-populations.]`
3.  **Theme 3**: `[e.g., Heterogeneity in outcome definitions.]`

---

## 3. Duplication & Overlap Assessment

### Exact Match Check
-   **Exact Duplicate Found?**: `[ ] Yes / [ ] No`
-   **Details**: `[If yes, cite the paper(s).]`

### Semantic Overlap Score
> Calculated using `mcp_zotero-mcp_semantic_search` or manual assessment.

| Comparator Paper | Semantic Similarity Score (0-1) | Assessment |
| :--- | :---: | :--- |
| `[Paper 1]` | `[0.XX]` | `[High/Med/Low Overlap]` |
| `[Paper 2]` | `[0.XX]` | `[High/Med/Low Overlap]` |

-   **Overall Overlap Verdict**: `[ ] Low (Proceed) / [ ] Medium (Caution) / [ ] High (Pivot Needed)`

---

## 4. Identified Research Gaps

Based on the literature review, the following gaps have been identified:

1.  **Gap 1 (Population)**: `[e.g., Lack of studies in pediatric populations.]`
2.  **Gap 2 (Outcome)**: `[e.g., No data on patient-reported quality of life outcomes.]`
3.  **Gap 3 (Methodology)**: `[e.g., Most studies are observational; RCTs are needed.]`
4.  **Gap 4 (Duration)**: `[e.g., Long-term (> 2 year) follow-up data is missing.]`

---

## 5. Innovation Pivot Recommendation

> If the research topic is saturated, select one of the following innovation branches. Use the `innovation_mindmap.mmd` template for visualization.

### Recommended Branches
-   [ ] **A. Sub-Population Focus**: `[e.g., Patients with a specific gene polymorphism (CYP2D6).]`
-   [ ] **B. Novel Outcome Metric**: `[e.g., Long-term cardiovascular event rate (MACE).]`
-   [ ] **C. Methodological Innovation**: `[e.g., Apply Mendelian Randomization for causal inference.]`
-   [ ] **D. Real-World Evidence**: `[e.g., Use electronic health records instead of trial data.]`

---

## 6. Agent Recommendation & Approval Gate

### Agent's Recommendation:
> `[ ] **PROCEED**: Novelty is confirmed. The proposed PICO addresses an identified gap.`
> `[ ] **PIVOT**: Topic is saturated. Recommend adopting Innovation Branch [A/B/C/D].`

### User/Expert Action Required:
-   `[ ]` **GAP_ACCEPT**: Confirm the recommendation and approve proceeding to SAP.
-   `[ ]` **GAP_REVISE**: Request revision of the scoping strategy or innovation angle.

