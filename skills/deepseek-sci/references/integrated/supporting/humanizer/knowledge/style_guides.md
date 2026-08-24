# Integrated supporting reference: humanizer/knowledge/style_guides.md

> Embedded source: `embedded-source/humanizer/knowledge/style_guides.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Journal-Specific Style Guides

## NEJM Style Guide

### General Characteristics
- **Tone:** Gravitas, authoritative, measured
- **Focus:** Physiological mechanisms over statistical associations
- **Word Economy:** Extreme concision required (~2700 words for Original Articles)

### Structure Requirements
| Section | Typical Length | Key Features |
|---------|---------------|--------------|
| Abstract | 250 words | Structured: Background, Methods, Results, Conclusions |
| Introduction | 2-3 paragraphs | Concise problem statement, gap identification |
| Methods | Variable | Sufficient for replication, ethics statement |
| Results | ~1000 words | Data presentation without interpretation |
| Discussion | ~1000 words | Mechanistic interpretation, limitations |

### Citation Style
- Vancouver system (numbered references)
- Superscript numbers placed OUTSIDE punctuation
- Example: "...as previously described.¹²"

### Language Preferences
| NEJM Prefers | Avoid |
|--------------|-------|
| "We found" | "It was found" |
| "The data suggest" | "The data is suggestive of" |
| Mechanism-focused interpretation | Pure statistical description |
| Measured confidence | Overstatement |

### Discussion Section Expectations
- Start with key finding summary (1 sentence)
- Place result in context of prior knowledge
- Explain physiological plausibility
- Address limitations specifically
- Suggest clinical implications conservatively

---

## JAMA Style Guide

### General Characteristics
- **Tone:** Modern, direct, accessible
- **Focus:** Clinical practice implications
- **Evidence Framework:** GRADE methodology emphasized

### Title Conventions
- Declarative preferred over interrogative
- Often includes study design: "...A Randomized Clinical Trial"
- No geographic location unless directly relevant
- Concise but informative

**Examples:**
- ✅ "Effect of X on Y in Patients with Z: A Randomized Clinical Trial"
- ❌ "Is X Better Than Y? A Study from Johns Hopkins"

### Voice Guidelines
JAMA actively encourages:
- First person plural ("We enrolled...")
- Active voice for clarity
- Direct statements over hedged constructions

### Abstract Structure
- Importance (why this matters)
- Objective (study question)
- Design, Setting, Participants
- Interventions/Exposures
- Main Outcomes and Measures
- Results (with confidence intervals)
- Conclusions and Relevance

### Statistical Reporting
- Report exact P values unless <.001
- Always include 95% CI for effect sizes
- Use CONSORT for RCTs
- Absolute differences preferred over relative

---

## Critical Care Medicine (CCM) Style Guide

### General Characteristics
- **Tone:** Technical expertise, clinical realism
- **Focus:** ICU-specific physiological complexity
- **Emphasis:** Practical bedside applicability

### Unique Considerations
- Recognition of treatment heterogeneity
- Emphasis on physiological targets over rigid protocols
- Awareness of competing risks in critically ill patients
- Integration of monitoring data interpretation

### Pathophysiology Expectations
CCM expects authors to demonstrate:
- Understanding of organ cross-talk
- Dynamic disease trajectory awareness
- Recognition of individual patient variability
- Equipment and monitoring specifics

### Discussion Section Tone
- Acknowledge uncertainty explicitly
- Discuss generalizability to different ICU settings
- Consider resource implications
- Address timing of interventions

### Example CCM-Appropriate Language
```
"Although MAP was maintained above the protocolized threshold, 
the persistence of elevated lactate suggests ongoing tissue hypoperfusion 
that macrocirculatory endpoints may fail to detect—a finding consistent 
with emerging evidence of endothelial dysfunction in distributive shock."
```

---

## Comparative Style Matrix

| Feature | NEJM | JAMA | CCM |
|---------|------|------|-----|
| **Word Limit** | ~2700 | ~3000 | ~3500 |
| **Title Style** | Concise | Declarative + Design | Descriptive |
| **Voice** | Mixed | Active preferred | Technical |
| **Discussion Focus** | Mechanism | Clinical translation | Bedside application |
| **Evidence Language** | Conservative | GRADE-aligned | Uncertainty-aware |
| **Statistical Presentation** | Precise | Comprehensive | Context-heavy |

---

## Common Style Errors to Avoid

### Cross-Journal
- Inconsistent abbreviation usage
- Mixing British and American spelling
- Overly long sentences (>35 words)
- Redundant phrases ("past history", "future plans")
- Dangling modifiers

### NEJM-Specific
- Excessive word count
- Purely statistical interpretation without mechanism
- Overstatement of clinical implications

### JAMA-Specific
- Passive voice overuse
- Interrogative titles
- Missing study design in title
- Inadequate patient-centered outcomes

### CCM-Specific
- Ignoring physiological complexity
- Oversimplified treatment paradigms
- Lacking ICU-specific context
- Ignoring monitoring data interpretation

---

## Adaptation Workflow

When adapting text for a specific journal:

1. **Identify target journal** and load appropriate style requirements
2. **Adjust word count** to target specification
3. **Modify title format** to match journal convention
4. **Calibrate voice** (active/passive ratio)
5. **Reframe discussion** according to journal's interpretive emphasis
6. **Verify citation format** (superscript position, et al. rules)
7. **Cross-check** against recent publications in target journal

