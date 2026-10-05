---
type: Reference
title: Choose XP taxonomy and focused lenses
description: Distinguish Values, Principles, and Primary / Corollary Practices in Extreme Programming, second edition, and select only focused lenses needed for the assessment.
sources:
  - id: xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
---

## Choose XP taxonomy and focused lenses

Read when assessing XP itself, its second edition, or classifications and relationships among Values / Principles / Practices and Primary / Corollary Practices.

The purpose is not to adopt or score every XP item. After checking taxonomy, read only categories relevant to the current problem through focused references.

### Do not flatten the taxonomy

XP's second edition distinguishes categories at different abstraction levels.[^xp-second-edition]

```text
Values
  ↓
Principles
  ↓
Practices
    ├─ Primary Practices
    └─ Corollary Practices
```

- **Values**: What matters in decisions.
- **Principles**: Bridges for applying Values to situations.
- **Practices**: Concrete actions executable in daily work.

Do not make these arrows maturity scores or mandatory adoption order. Do not score XP maturity by Practice counts or infer implementation from Value names alone.

### Values

Five Values:

- Communication
- Simplicity
- Feedback
- Courage
- Respect

When applying a Value to actual decisions, read only the [lightweight lookup of individual XP items](xp-auxiliary.md#values). Use the same reference for individual Values supporting other engineering lenses, without reading the full taxonomy.

### Principles

InformIT's Table of Contents lists these 14 named Principles. The introduction on the same publisher page inconsistently says “Eleven principles”; this repository bases taxonomy on the listed TOC and retains the discrepancy in provenance.[^xp-second-edition]

- Humanity
- Economics
- Mutual Benefit
- Self-Similarity
- Improvement
- Diversity
- Reflection
- Flow
- Opportunity
- Redundancy
- Failure
- Quality
- Baby Steps
- Accepted Responsibility

When applying a Principle to an actual problem, read only the [lightweight lookup of individual XP items](xp-auxiliary.md#principles). Do not read the full taxonomy when using individual Principles to support Architecture / Delivery / DORA or other lenses.

### Primary Practices

13 Primary Practices:

- Sit Together
- Whole Team
- Informative Workspace
- Energized Work
- Pair Programming
- Stories
- Weekly Cycle
- Quarterly Cycle
- Slack
- Ten-Minute Build
- Continuous Integration
- Test-First Programming
- Incremental Design

### Corollary Practices

11 Corollary Practices:

- Real Customer Involvement
- Incremental Deployment
- Team Continuity
- Shrinking Teams
- Root-Cause Analysis
- Shared Code
- Code and Tests
- Single Code Base
- Daily Deployment
- Negotiated Scope Contract
- Pay-Per-Use

Read only [Primary Practices](xp-auxiliary.md#primary-practices) when their meaning or evidence is needed, or [Corollary Practices](xp-auxiliary.md#corollary-practices) for those practices. Do not make adopted Practice counts maturity measures or required adoption counts.

### Select only necessary categories from the problem

| Problem | First XP lens |
| --- | --- |
| Requirements misunderstanding | Communication / Feedback in [Values](xp-auxiliary.md#values); if needed, Stories / Whole Team in [Practices](xp-auxiliary.md#primary-practices) |
| Premature or complex design | Simplicity in [Values](xp-auxiliary.md#values), Economics / Baby Steps in [Principles](xp-auxiliary.md#principles); if needed, Incremental Design in [Practices](xp-auxiliary.md#primary-practices) |
| Slow feedback or large changes | Feedback in [Values](xp-auxiliary.md#values), Flow / Baby Steps in [Principles](xp-auxiliary.md#principles); if needed, CI / Test-First / Incremental Design in [Practices](xp-auxiliary.md#primary-practices) |
| Unsustainable work | Respect in [Values](xp-auxiliary.md#values), Humanity in [Principles](xp-auxiliary.md#principles); if needed, Energized Work / Slack in [Practices](xp-auxiliary.md#primary-practices) |
| Recurring failures | Courage in [Values](xp-auxiliary.md#values), Reflection / Failure in [Principles](xp-auxiliary.md#principles); if needed, Root-Cause Analysis in [Corollary Practices](xp-auxiliary.md#corollary-practices) |
| Responsibility and authority mismatch | Respect in [Values](xp-auxiliary.md#values), Accepted Responsibility in [Principles](xp-auxiliary.md#principles); if needed, Whole Team in [Practices](xp-auxiliary.md#primary-practices) |

This table is not the only mapping. Select only categories and items relevant to the current problem; do not add unrelated XP items to unknowns lists.

### Runtime division of responsibilities

- Put Values and short continuously used decision principles in shared Instructions.
- `software-development` handles concrete execution of TDD, Pair Programming, Incremental Design, and similar practices.
- `engineering-assessment` handles taxonomy, selection, and evidence judgments during assessment.
- Read the [dedicated lens](architecture-and-organization.md) for Architecture / Organization details.
- Read the [DORA lens](dora.md) for Core / Capability / metrics.

For XP-primary assessment, enter through this taxonomy file and add the [lightweight lookup of individual XP items](xp-auxiliary.md) only when concrete item meanings are needed. If only classification is needed, do not read the lookup or expand every item into the unknowns list.

[^xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987). The 2004 edition's Table of Contents lists five Values, 14 named Principles, 13 Primary Practices, and 11 Corollary Practices. The same publisher page's introduction says “Eleven principles,” so use the TOC list for Principle counts and state the discrepancy. Checked 2026-09-27.
