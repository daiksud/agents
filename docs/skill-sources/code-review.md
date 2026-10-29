---
type: Reference
title: code-review sources and maintenance notes
description: Human-facing source mappings, adoption rationale, and retained checking history for code-review.
sources:
- id: github-instructions-code-review-generic-instructions-md
  resource: https://github.com/github/awesome-copilot/blob/main/instructions/code-review-generic.instructions.md
- id: fowler-beck-design-rules
  resource: https://martinfowler.com/bliki/BeckDesignRules.html
- id: fowler-yagni
  resource: https://martinfowler.com/bliki/Yagni.html
- id: change-record-agreement
  resource: https://github.com/daiksud/agents/issues/253
---

## Purpose and runtime documents

These are maintainer notes for [code-review](../../skills/code-review/SKILL.md). Runtime entry points and task references retain the instructions needed for execution; this document preserves attribution and background for maintenance. Any source-check dates below are retained history, not new verification performed during this separation.

### Source mapping

Source IDs are preserved from the original files, including aliases for the same URL.

| Runtime document or original catalog | Source IDs |
| --- | --- |
| [references/review-guidance.md](../../skills/code-review/references/review-guidance.md) | [^github-instructions-code-review-generic-instructions-md], [^fowler-beck-design-rules], [^fowler-yagni] |

## Sources and application policy

Referenced the quality perspectives, overall-to-detail investigation, and concrete constructive reporting in GitHub awesome-copilot's Generic Code Review Instructions.[^github-instructions-code-review-generic-instructions-md]

Using Martin Fowler's Beck Design Rules[^fowler-beck-design-rules] and Yagni[^fowler-yagni], established five perspectives for investigating complexity unnecessary for current requirements. These are this skill's application examples; the originals do not uniformly prohibit each structure.

This skill evaluates the simplest design meeting current requirements and safety for actual changes, assigning P0–P3 severity by impact. Do not directly apply the sources' area-specific severities, line-count guidance, or Copilot frontmatter. Report review results as judgments within checked scope; do not decide GitHub approval or merge.

## Retained source annotations

These annotations preserve the original per-file attribution and checking details.

### references/review-guidance.md

- `github-instructions-code-review-generic-instructions-md`: [GitHub awesome-copilot Generic Code Review Instructions](https://github.com/github/awesome-copilot/blob/main/instructions/code-review-generic.instructions.md). Evidence for the reference scope and adoption decisions stated in the text.
- `fowler-beck-design-rules`: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html). Apply to design meeting current requirements, clear intent, and judging unnecessary elements.
- `fowler-yagni`: [Yagni](https://martinfowler.com/bliki/Yagni.html). Distinguish anticipation of hypothetical future features from currently necessary health.

[^github-instructions-code-review-generic-instructions-md]: [GitHub awesome-copilot Generic Code Review Instructions](https://github.com/github/awesome-copilot/blob/main/instructions/code-review-generic.instructions.md). Evidence for the reference scope and adoption decisions stated in the text.
[^fowler-beck-design-rules]: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html). Apply to design meeting current requirements, clear intent, and judging unnecessary elements.
[^fowler-yagni]: [Yagni](https://martinfowler.com/bliki/Yagni.html). Distinguish anticipation of hypothetical future features from currently necessary health.

## Change-record policy adoption

[Review](../../skills/code-review/SKILL.md) and its PR-record guidance apply the agreement in [Issue #253](https://github.com/daiksud/agents/issues/253).[^change-record-agreement] The current rationale and boundaries live in [Change records policy](../engineering-policies/change-records.md): actual validation reporting is required while execution is discretionary unless independently required; PRs/commits retain historical judgment and topical policies retain current guidance. This adoption does not establish renewed checking of the external sources above.

[^change-record-agreement]: Owner-agreed change-record policy and implementation scope in Issue #253.
