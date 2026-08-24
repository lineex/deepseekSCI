# Integrated supporting reference: humanizer/knowledge/ai_markers.md

> Embedded source: `embedded-source/humanizer/knowledge/ai_markers.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# AI Fingerprint Markers - Comprehensive Catalog

## I. Lexical Markers (词汇层面)

### 1.1 High-Frequency Transitional Markers
AI-generated text over-relies on explicit logical connectors:

| Marker Type | Examples | Replacement Strategy |
|-------------|----------|---------------------|
| **Additive** | Moreover, Furthermore, Additionally, In addition | Omit or use implicit connection |
| **Causal** | Consequently, Therefore, Thus, Hence, As a result | Embed causality in verb choice |
| **Contrastive** | However, Nevertheless, Nonetheless, Conversely | Use "but/yet" or structural contrast |
| **Summary** | In summary, To conclude, In conclusion, Overall | Simply state the conclusion |
| **Sequence** | Firstly, Secondly, Thirdly, Finally | Use unmarked enumeration or bullets |

### 1.2 Overly Formal/Academic Vocabulary
| AI Preference | Human Alternative |
|---------------|-------------------|
| ameliorate | improve |
| utilize | use |
| elucidate | explain, clarify |
| facilitate | help, enable |
| demonstrate | show |
| encompass | include |
| commence | begin, start |
| terminate | end, stop |
| endeavor | try, attempt |
| ascertain | determine, find out |

### 1.3 Hedging Overuse
AI tends to over-hedge to appear balanced:
- "It is important to note that..."
- "It should be mentioned that..."
- "It is worth considering that..."
- "arguably", "potentially", "possibly" (excessive use)

---

## II. Syntactic Markers (句法层面)

### 2.1 Nominal Loading (名词化过度)
Converting verbs into noun phrases:

| Nominalized (AI) | Verbal (Human) |
|------------------|----------------|
| The implementation of the protocol | We implemented the protocol |
| The performance of analysis | We analyzed |
| The administration of treatment | We administered treatment |
| An examination of the data | We examined the data |
| The observation of changes | We observed changes |

### 2.2 Passive Voice Overuse
| Passive (AI) | Active (Human) |
|--------------|----------------|
| Blood samples were collected | We collected blood samples |
| Statistical analysis was performed | We performed statistical analysis |
| Significant differences were observed | Our analysis revealed significant differences |
| Patients were randomized to receive | We randomized patients to receive |

### 2.3 Sentence Structure Uniformity
AI-generated paragraphs exhibit:
- Similar sentence lengths (typically 15-25 words)
- Repetitive opening patterns ("The study...", "The data...", "The results...")
- Lack of rhetorical variation (no questions, exclamations, fragments)

### 2.4 Part-of-Speech Distribution
AI text characteristics:
- Higher noun-to-verb ratio
- Increased determiners and prepositions
- Reduced adjectives and adverbs
- Lower lexical diversity (Type-Token Ratio)

---

## III. Structural/Logical Markers (逻辑层面)

### 3.1 "Hollow Coherence"
AI produces superficially logical but depth-lacking text:
- Lists facts without synthesizing
- Avoids taking definitive positions
- Presents balanced views without genuine critical evaluation

### 3.2 Template-Like Organization
Recognizable AI paragraph structures:
```
[Topic sentence stating general principle]
[Supporting evidence 1]
[Supporting evidence 2]
[Transitional connector + minor qualification]
[Restated conclusion]
```

### 3.3 Evidence Treatment
| AI Pattern | Expert Pattern |
|------------|----------------|
| All citations treated equally | Evidence weighted by study quality |
| Linear enumeration of findings | Integration with mechanistic reasoning |
| Generic limitations statements | Specific methodological critiques |
| Avoidance of contradictions | Engagement with conflicting evidence |

---

## IV. Content Markers (内容层面)

### 4.1 Clinical Detail Absence
AI-generated medical text lacks:
- Specific physical examination findings
- Dynamic physiological observations
- Equipment/timing specifics
- Bedside clinical nuances

### 4.2 Ethical/Humanistic Depth
AI rarely incorporates:
- Patient dignity considerations
- End-of-life decision complexity
- Resource allocation ethics
- Family/caregiver perspectives

### 4.3 Negative Result Handling
| AI Explanation | Expert Explanation |
|----------------|-------------------|
| "May be due to small sample size" | "Effect dilution from population heterogeneity" |
| "Further research is needed" | "The intervention window may have been suboptimal given disease trajectory" |
| "Inconsistent with prior studies" | "Control group 'usual care' has evolved to incorporate intervention elements" |

---

## V. Detection Heuristics

### Quick Scan Checklist
1. **Connector Density:** >3 transitional markers per paragraph = suspicious
2. **Passive Ratio:** >60% passive constructions = suspicious
3. **Sentence Variance:** Standard deviation <5 words = suspicious
4. **Opening Diversity:** >3 consecutive same-structure sentence starts = suspicious
5. **Verb Vitality:** Noun-to-verb ratio >4:1 = suspicious

### Detailed Analysis Protocol
1. Run text through sentence length analyzer
2. Calculate Type-Token Ratio (TTR) for lexical diversity
3. Extract and count transitional markers
4. Identify passive voice percentage
5. Map paragraph structure templates
6. Score clinical specificity (0-10 scale)

---

## VI. Marker Severity Classification

| Severity | Marker Set | Risk to Publication |
|----------|------------|---------------------|
| **Critical** | Fabricated references, invented data | Rejection + misconduct investigation |
| **High** | Absent clinical depth, template structure | Likely desk rejection |
| **Medium** | Excessive connectors, passive overuse | Revision required |
| **Low** | Formal vocabulary preference | Minor editing |

---

## VII. Self-Assessment Rubric

Score your text on each dimension (1-5, where 5 = highly AI-like):

| Dimension | 1 (Human) | 5 (AI) |
|-----------|-----------|--------|
| Connector usage | Sparse, implicit | Dense, explicit |
| Voice | Active-dominant | Passive-dominant |
| Sentence rhythm | Varied | Uniform |
| Clinical detail | Granular | Generic |
| Evidence critique | Specific | Template |
| Vocabulary | Precise, contextual | Formal, generic |

**Total Score Interpretation:**
- 6-12: Minimal AI markers
- 13-20: Moderate revision needed
- 21-30: Substantial rewriting required

