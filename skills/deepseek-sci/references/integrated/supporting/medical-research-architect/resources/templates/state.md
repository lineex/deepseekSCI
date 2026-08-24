# Integrated supporting reference: medical_research_architect/resources/templates/state.md

> Embedded source: `embedded-source/medical_research_architect/resources/templates/state.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Research State Board

> This file is the **single source of truth** for this research project's workflow. The AI agent MUST read this before any action and update it after every phase.

## Project Metadata

| Property | Value |
| :--- | :--- |
| **Project Title** | `[TBD]` |
| **Lead Architect** | Antigravity AI |
| **Created** | `[DATE]` |
| **Last Updated** | `[DATE]` |

---

## Current Status

| Property | Value |
| :--- | :--- |
| **Current Phase** | `INIT` |
| **Phase Status** | `PENDING` |

### Status Codes
-   `INIT`: Initial state, awaiting topic input.
-   `IN_PROGRESS`: Agent is actively working on this phase.
-   `AUDIT_PENDING`: Agent has completed work and awaits user/expert review.
-   `REVISE_NEEDED`: User has requested changes. Agent must iterate.
-   `APPROVED`: User has approved the phase. Agent may proceed.

### Phase Codes
-   `PICO`: Phase 1 - PICO Definition
-   `GAP`: Phase 2 - Innovation & Gap Analysis
-   `SAP`: Phase 3 - Statistical Analysis Plan
-   `DRAFT`: Phase 4 - Manuscript Drafting
-   `COMPLETE`: All phases finished.

---

## Phase Checklists & Audit Logs

### Phase 1: PICO Definition
| Task | Status | Notes |
| :--- | :---: | :--- |
| Population (P) defined | `[ ]` | |
| Intervention (I) defined | `[ ]` | |
| Comparison (C) defined & validated | `[ ]` | *Auditor: Is this a valid comparator?* |
| Outcome (O) defined | `[ ]` | |
| **Phase Approval** | **`PENDING`** | |

### Phase 2: Innovation & Gap Analysis
| Task | Status | Notes |
| :--- | :---: | :--- |
| Global literature scan (Zotero/PubMed) | `[ ]` | |
| Semantic search on local library | `[ ]` | |
| Scoping Report generated | `[ ]` | |
| Novelty confirmed OR Innovation Pivot selected | `[ ]` | |
| **Phase Approval** | **`PENDING`** | |

### Phase 3: Statistical Analysis Plan (SAP)
| Task | Status | Notes |
| :--- | :---: | :--- |
| SAP Protocol drafted | `[ ]` | |
| Causal DAG defined (if observational) | `[ ]` | |
| Analysis script generated | `[ ]` | |
| Script executed & results captured | `[ ]` | |
| Assumption checks passed | `[ ]` | |
| Visualizations created | `[ ]` | |
| **Phase Approval** | **`PENDING`** | |

### Phase 4: Manuscript Drafting
| Task | Status | Notes |
| :--- | :---: | :--- |
| Methods section drafted | `[ ]` | |
| Results section drafted | `[ ]` | |
| Discussion section drafted | `[ ]` | |
| Peer Review Simulation completed | `[ ]` | |
| Reproducibility log updated | `[ ]` | |
| **Phase Approval** | **`PENDING`** | |

---

## Revision History
| Date | Phase | Action | Summary |
| :--- | :--- | :--- | :--- |
| `[DATE]` | `INIT` | Created | Project initialized. |

