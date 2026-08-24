# Integrated supporting reference: humanizer/knowledge/verification_checklist.md

> Embedded source: `embedded-source/humanizer/knowledge/verification_checklist.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Reference & Fact Verification Protocol

## I. The 6-Step Reference Verification Protocol

AI-generated references are the most detectable and damaging form of AI hallucination. This protocol ensures complete reference integrity.

### Step 1: DOI Validation
**Purpose:** Verify each Digital Object Identifier resolves correctly

**Method:**
1. Extract all DOIs from reference list
2. Test each at https://doi.org/[DOI]
3. Confirm landing page matches expected article

**Common AI Errors:**
- Completely fabricated DOIs
- DOIs with transposed digits
- DOIs from similar but different articles
- Valid DOI format but non-existent identifier

**Tool:** CrossRef Metadata Search (https://search.crossref.org/)

---

### Step 2: PubMed Alignment Check
**Purpose:** Verify journal abbreviations and indexing

**Method:**
1. Search PubMed for each cited article
2. Confirm journal abbreviation matches Index Medicus standard
3. Verify PMID if provided

**Common AI Errors:**
- Incorrect journal abbreviations (adding/removing periods)
- Mixing journal names with abbreviations
- Citing articles not indexed in PubMed
- Wrong journal for the article

**Reference:** NLM Catalog (https://www.ncbi.nlm.nih.gov/nlmcatalog/)

---

### Step 3: Author Identity Verification
**Purpose:** Confirm cited authors exist and work in claimed field

**Method:**
1. Search author names in PubMed/Google Scholar
2. Verify institutional affiliations
3. Check author has publications in claimed area

**Common AI Errors:**
- Plausible but non-existent author names ("J. Smithson from Oxford")
- Real author names attributed to wrong papers
- Invented co-author combinations
- Authors who don't work in the cited field

---

### Step 4: Content Tracing
**Purpose:** Verify cited claims match original source

**Method:**
1. Obtain original article abstract (minimum)
2. Compare cited claim to actual findings
3. Verify statistics if quoted

**Common AI Errors:**
- Study A's conclusion attributed to Study B
- Combining findings from multiple studies into single citation
- Inverted effect directions (positive claimed as negative)
- Methodological details from wrong study

---

### Step 5: Timeline Logic Check
**Purpose:** Ensure temporal coherence of citations

**Method:**
1. Verify cited publication dates
2. Confirm all cited work precedes or accompanies current study
3. Check for anachronistic references

**Common AI Errors:**
- Citing future publication dates
- Referencing studies that couldn't have informed the current work
- Incorrect publication years
- Confusing online ahead of print with final publication

---

### Step 6: Journal Existence Confirmation
**Purpose:** Ensure cited journals are real and indexed

**Method:**
1. Check journal in Web of Science/Scopus
2. Verify ISSN if provided
3. Confirm journal covers claimed subject area

**Common AI Errors:**
- Completely fabricated journal names
- Plausible-sounding but non-existent journals
- Predatory journals presented as legitimate
- Defunct journals cited for recent articles

---

## II. Verification Checklist Template

```
□ Reference #___: [Authors]. [Title]. [Journal]. [Year]
  
  □ DOI verified at doi.org: _______________
  □ PubMed/PMID confirmed: _______________
  □ Journal abbreviation correct: _______________
  □ First author identity verified: _______________
  □ Cited claim matches original: _______________
  □ Publication date logical: _______________
  □ Journal indexed and legitimate: _______________
  
  Status: □ Verified  □ Corrected  □ Removed
  Notes: _________________________________
```

---

## III. Data & Statistical Verification

### Numerical Consistency Checks

| Check | Method |
|-------|--------|
| **n-values sum** | Total N = sum of subgroups |
| **Percentages total** | Should sum to ~100% |
| **CI-P consistency** | P<0.05 should have CI excluding null |
| **Effect size direction** | Matches narrative interpretation |
| **Baseline balance** | Claimed randomization reflected in Table 1 |

### Statistical Recalculation
For key findings, manually verify:
- Odds Ratio from given counts
- Risk Ratio from incidence rates
- 95% CI from reported SE/SD
- P-value from test statistic

### Common AI Statistical Errors
- Mismatched numerators/denominators
- Impossible confidence intervals
- P-values inconsistent with effect sizes
- Mixing intention-to-treat with per-protocol numbers

---

## IV. Fact Verification Categories

### Medical Facts
| Category | Verification Source |
|----------|---------------------|
| Drug dosages | FDA label, UpToDate |
| Lab normal ranges | Institutional references |
| Pathophysiology | Harrison's, Cecil's |
| Epidemiology | CDC, WHO data |
| Guidelines | Society websites |

### Technical Facts
| Category | Verification Source |
|----------|---------------------|
| Equipment specs | Manufacturer documentation |
| Assay parameters | Kit inserts |
| Statistical methods | Original methodology papers |
| Software references | Official documentation |

---

## V. Red Flags Requiring Immediate Investigation

> [!CAUTION]
> Any of these findings should trigger complete reference/data review:

1. **Reference not found** in any database search
2. **Author name** returns no academic presence
3. **Journal abbreviation** doesn't match standard format
4. **Publication year** is in the future
5. **Statistical impossibility** (percentages >100%, negative counts)
6. **Effect size** seems implausible for the clinical context
7. **Sample size** doesn't match reported subgroups
8. **Quoted finding** contradicts original abstract

---

## VI. Documentation Template

For each manuscript, maintain a verification log:

```markdown
# Verification Log: [Manuscript Title]
Date: YYYY-MM-DD
Verified by: [Name]

## References Verified: ___/___

### Issues Found:
1. Ref #__: [Description of issue and resolution]
2. ...

## Statistics Verified: Yes/No

### Issues Found:
1. [Description and resolution]

## Facts Verified

### Issues Found:
1. [Description and resolution]

## Final Verification Status: 
□ All clear  □ Corrections made  □ Unresolved issues
```

---

## VII. Verification Tools Reference

| Tool | Purpose | URL |
|------|---------|-----|
| CrossRef | DOI verification | https://search.crossref.org/ |
| PubMed | Article/author search | https://pubmed.ncbi.nlm.nih.gov/ |
| NLM Catalog | Journal verification | https://www.ncbi.nlm.nih.gov/nlmcatalog/ |
| Retraction Watch | Check for retractions | https://retractionwatch.com/retraction-watch-database-user-guide/ |
| Beall's List | Predatory journal check | Various mirrors available |
| ICMJE | Journal membership | https://www.icmje.org/ |
| Scopus | Journal metrics | https://www.scopus.com/ |

