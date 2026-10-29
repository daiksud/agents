---
type: Reference
title: software-development sources and maintenance notes
description: Human-facing source mappings, adoption rationale, and retained checking history for software-development.
sources:
- id: minodriven-designing-for-code-reading
  resource: https://speakerdeck.com/minodriven/designing-for-code-reading
- id: beck-andres-getting-started-xp
  resource: https://www.informit.com/articles/article.aspx?p=390816
- id: beck-andres-primary-practices
  resource: https://www.informit.com/articles/article.aspx?p=390816&seqNum=3
- id: ron-jeffries-xp
  resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
- id: fowler-beck-design-rules
  resource: https://martinfowler.com/bliki/BeckDesignRules.html
- id: fowler-yagni
  resource: https://martinfowler.com/bliki/Yagni.html
- id: newsletter-p-canon-tdd
  resource: https://newsletter.kentbeck.com/p/canon-tdd
- id: kent-beck-run-on-tests
  resource: https://newsletter.kentbeck.com/p/decompose-run-on-tests
- id: continuousdelivery-foundations-test-automation
  resource: https://continuousdelivery.com/foundations/test-automation/
- id: continuousdelivery-implementing-architecture
  resource: https://continuousdelivery.com/implementing/architecture/
- id: www-05-ddd-reference-2015-03-pdf
  resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
- id: github-instructions-oop-design-patterns-instructions-md
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md
- id: github-instructions-self-explanatory-code-commenting-instructions-md
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md
- id: github-instructions-qa-engineering-best-practices-instructions-md
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md
- id: context-engineering
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md
- id: taming-copilot
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
- id: issue-99
  resource: https://github.com/daiksud/agents/issues/99
- id: issue-140
  resource: https://github.com/daiksud/agents/issues/140
- id: github-copilot-cli-changelog
  resource: https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710
- id: issue-87
  resource: https://github.com/daiksud/agents/issues/87
- id: issue-100
  resource: https://github.com/daiksud/agents/issues/100
- id: issue-161
  resource: https://github.com/daiksud/agents/issues/161
  - id: change-record-agreement
    resource: https://github.com/daiksud/agents/issues/253
---

## Purpose and runtime documents

These are maintainer notes for [software-development](../../skills/software-development/SKILL.md). Runtime entry points and task references retain the instructions needed for execution; this document preserves attribution and background for maintenance. Any source-check dates below are retained history, not new verification performed during this separation.

### Source mapping

Source IDs are preserved from the original files, including aliases for the same URL. Local `practice-sources` bindings identified the former bundled catalog; its content is retained in this note.

| Runtime document or original catalog | Source mapping |
| --- | --- |
| Former bundled source catalog (`references/sources.md`) | [Sources for design and testing](#sources-for-design-and-testing) retains its source IDs and adoption notes |
| [references/agent-communication.md](../../skills/software-development/references/agent-communication.md) | [^issue-99], [^issue-140] |
| [references/copilot-cli-pairing.md](../../skills/software-development/references/copilot-cli-pairing.md) | [^github-copilot-cli-changelog], [^issue-87], [^issue-99], [^issue-100], [^issue-161] |
| [references/design.md](../../skills/software-development/references/design.md) | `practice-sources` (original resource: `sources.md`; catalog retained here) |
| [references/navigator-recovery.md](../../skills/software-development/references/navigator-recovery.md) | [^issue-140], [^issue-100], [^issue-161] |
| [references/testing.md](../../skills/software-development/references/testing.md) | `practice-sources` (original resource: `sources.md`; catalog retained here) |

## Sources for design and testing

### Primary materials

The reference date is 2026-09-11. Undated means the publication or update date could not be established. These are sources of definitions and recommendations, not measurements of this skill's effectiveness.

| Author and material | Date and referenced location | Use in this skill |
| --- | --- | --- |
| Kent Beck, Canon TDD[^newsletter-p-canon-tdd] | 2023-12-11 | Test lists, one-at-a-time iterations, and retaining expectations |
| Kent Beck, Decompose Run-On Tests[^kent-beck-run-on-tests] | March 2013; republished 2026-10-13 | Split exploratory test chains into diagnostic, contract-based tests |
| Jez Humble, Continuous Testing[^continuousdelivery-foundations-test-automation], Architecture[^continuousdelivery-implementing-architecture] | Undated | Fast feedback, exploration, testability, and incremental design improvement |
| Eric Evans, DDD Reference[^www-05-ddd-reference-2015-03-pdf] | March 2015, booklet pages 39–41 and others | Bounded Context, Ubiquitous Language, and Context Map |

### Adoption decisions for post-exploration test decomposition

Kent Beck's Decompose Run-On Tests[^kent-beck-run-on-tests] was checked on 2026-10-21. A sequence of operations and assertions may be useful when discovering a design, but later failures can obscure which action caused the problem. Decompose such exploratory tests into focused, descriptively named cases, omitting preceding assertions when covered elsewhere in the suite.

This environment additionally requires retaining only assertions that represent agreed, observable contracts; discard exploratory probes about incidental current behavior instead of turning them into requirements. Verify the suite preserves intended contract coverage before removing the original test. Do not mandate one assertion per test or split a multi-step scenario whose sequence is itself an agreed behavior.

### Adoption decisions for XP values

Ron Jeffries' What is Extreme Programming?[^ron-jeffries-xp] was checked on 2026-09-25. Apply Communication, Simplicity, Feedback, Courage, and Respect to sharing actual expectations, structure suited to current requirements, short validation, necessary design improvements, decision authority, and sustainable work. Do not make fixed meeting formats, team arrangements, or effectiveness figures from the originals shared requirements. Preserve agent authority, approval, publication, and review conditions as contracts of this environment.

### Adoption decisions for Simple Design and YAGNI

Martin Fowler's Beck Design Rules[^fowler-beck-design-rules] and Yagni[^fowler-yagni] were checked on 2026-09-25. Judge design from current tests and contracts, clarity of intent, duplication of the same rules, and necessary elements. Do not anticipate hypothetical future features; improve incrementally through actual feedback. Do not assign mechanical priority or scores between clarity and duplication, or omit necessary tests, Refactor, or CI. Assert-first and stage confirmation by the same Navigator are local policies, not requirements attributed to original XP sources.

### Adoption decisions for introducing XP alone

Kent Beck / Cynthia Andres' introductory article[^beck-andres-getting-started-xp] and Primary Practices summary[^beck-andres-primary-practices] were checked on 2026-10-04. The introduction allows trying practices one at a time and improving as an individual. The summary lists Test-first Programming, Incremental Design, Stories, Weekly Planning, Slack, Ten-minute Build, Continuous Integration, and Energized Work. Original CI integrates into shared code within hours; automated builds and tests support short feedback. The target of integrating into main on each active day is existing local operation, not the same frequency as the original.

Starting with TDD, incremental design, and automated validation; selecting outcomes at the start of the week and briefly reflecting at its end; reusing existing Issues and ToDos; adjusting scope while preserving quality; and handing off during rest are local solo proposals. They are not verbatim original provisions or claims that all XP practices are implemented. Preserve AI collaboration and review conditions even with one human. Do not add fixed meetings, weekly automation, or assumptions about fatigue.

### Adoption decisions for Design by Contract

MinoDriven's Designing for code reading[^minodriven-designing-for-code-reading], published 2026-09-30, was checked on 2026-10-06: slides 13–20 cover contract categories and black-box tests, 23–27 cover side effects and isolation, and 29–36 cover abstraction. Adopt these ideas to implement existing agreed domain behavior faithfully within this repository's incremental workflow.

Detailed guidance belongs in [design](../../skills/software-development/references/design.md#expressing-agreed-behavior-as-contracts) and [testing](../../skills/software-development/references/testing.md#mapping-contracts-to-observable-tests). Caller/callee ownership, current-scope enforcement, and the inventory example are local application choices, not universal business rules or verbatim deck requirements.

Reuse specification outcomes without mandatory discovery ceremonies. Identify only applicable conditions and implement one assert-first item at a time. Preserve happy-path MVP, resilient assertions, and ordinary review/CI; do not adopt repeated internal guards, speculative hardening, mandatory classes, a new framework, fixed templates, coverage quotas, or whole-repository retrofits. Contracts and tests are scoped evidence, not formal proof or the deck's near-total correctness claim.

### Sources of instruction examples and application decisions

The following GitHub awesome-copilot instruction examples checked on 2026-09-11 were summarized and restructured. Links are pinned to the checked commit. These are community examples, not universal mandatory OOP or testing rules.

| Material | Incorporated content and adjustments |
| --- | --- |
| OOP Design Patterns[^github-instructions-oop-design-patterns-instructions-md] | Use responsibilities, contracts, composition, and dependency direction. Do not require abstract types first, logging in every function, or fixed docstring formats |
| Self-explanatory Code Commenting[^github-instructions-self-explanatory-code-commenting-instructions-md] | Prioritize naming and structure; retain reasons and invisible contracts. Do not remove public contract explanations merely because they are not reasons |
| QA Engineering Best Practices[^github-instructions-qa-engineering-best-practices-instructions-md] | Use state isolation, UI condition waits, and representative-load validation. Do not mandate fixed ratios, coverage, retry counts, or particular tools |

The following examples checked on 2026-09-13 were also summarized and restructured from the same fixed commit.

| Material | Incorporated content and adjustments |
| --- | --- |
| Context Engineering[^context-engineering] | Use meaningful names, paths, constants, discoverable placement, boundary types and public contracts, and explanations of complex flow. Prioritize existing placement and the [shared artifact language policy](../../.apm/instructions/language.instructions.md); do not require banning local type inference, uniform index files, internal exposure, or IDE operations |
| Taming Copilot[^taming-copilot] | Consider standard features and existing dependencies first and integrate necessary changes into existing structure. Do not omit required contracts, error cases, or TDD, or use shortest code or only user-listed files as the scope criterion |

## Retained source annotations

These annotations preserve the original per-file attribution and checking details.

### references/agent-communication.md

- `issue-140`: [Issue #140](https://github.com/daiksud/agents/issues/140) on condition-specific required reading and Navigator sharing boundaries.
- `issue-99`: [Issue #99](https://github.com/daiksud/agents/issues/99) records low-entropy Controlled English internal communication and its boundary with external artifacts.

### references/copilot-cli-pairing.md

- `issue-99`: [Issue #99](https://github.com/daiksud/agents/issues/99) on separating runtime-independent internal communication protocols from runtime-specific transport.
- `github-copilot-cli-changelog`: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710) states `sync` tasks do not return reusable `agent_id` values; use `mode: "background"` for follow-up communication.
- `issue-87`: [Issue #87](https://github.com/daiksud/agents/issues/87) on continuing communication and actual response checks.
- `issue-100`: [Issue #100](https://github.com/daiksud/agents/issues/100) on evidence preservation, retirement, and rechecking boundaries.
- `issue-161`: [Issue #161](https://github.com/daiksud/agents/issues/161) on automatic re-pairing without user confirmation and context transfer.

### references/design.md

- `practice-sources`: References and application decisions for Simple Design, YAGNI, DDD, OOP Design Patterns, Self-explanatory Code Commenting, Context Engineering, and Taming Copilot; [Design by Contract adoption and limits](#adoption-decisions-for-design-by-contract).

### references/navigator-recovery.md

- `issue-140`: [Issue #140](https://github.com/daiksud/agents/issues/140) on recovery-only detail and retaining mandatory contracts at entry points.
- `issue-161`: [Issue #161](https://github.com/daiksud/agents/issues/161) on automatic re-pairing without user confirmation and transferring as much context as possible.
- `issue-100`: [Issue #100](https://github.com/daiksud/agents/issues/100) on evidence preservation, retiring the former Navigator, and revalidation from unconfirmed stages.

### references/testing.md

- `practice-sources`: References and application decisions for Canon TDD, Continuous Testing, Architecture, and QA Engineering Best Practices; [Design by Contract adoption and limits](#adoption-decisions-for-design-by-contract).

[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) records low-entropy Controlled English internal communication and its boundary with external artifacts.
[^issue-140]: [Issue #140](https://github.com/daiksud/agents/issues/140) on condition-specific required reading and Navigator sharing boundaries.
[^github-copilot-cli-changelog]: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710) states `sync` tasks do not return reusable `agent_id` values; use `mode: "background"` for follow-up communication.
[^issue-87]: [Issue #87](https://github.com/daiksud/agents/issues/87) on continuing communication and actual response checks.
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) on evidence preservation, retirement, and rechecking boundaries.
[^issue-161]: [Issue #161](https://github.com/daiksud/agents/issues/161) on automatic re-pairing without user confirmation and context transfer.
[^newsletter-p-canon-tdd]: [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd). Basis for the referenced scope and adoption decisions stated in the text.
[^kent-beck-run-on-tests]: [Decompose Run-On Tests](https://newsletter.kentbeck.com/p/decompose-run-on-tests). Originally published March 2013 and republished 2026-10-13; source of the run-on-test decomposition technique. The contract triage and multi-step exceptions above are this environment's application policy.
[^continuousdelivery-foundations-test-automation]: [Continuous Testing](https://continuousdelivery.com/foundations/test-automation/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-implementing-architecture]: [Architecture](https://continuousdelivery.com/implementing/architecture/). Basis for the referenced scope and adoption decisions stated in the text.
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^ron-jeffries-xp]: [What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/). Applying the five values and practices to the situation.
[^fowler-beck-design-rules]: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html). Fowler’s formulation reviewed by Kent Beck himself.
[^fowler-yagni]: [Yagni](https://martinfowler.com/bliki/Yagni.html). Distinguishes unrequested features from health supporting current changes.
[^beck-andres-getting-started-xp]: [Getting Started with eXtreme Programming: Toe Dipping, Racing Dives, and Cannonballs](https://www.informit.com/articles/article.aspx?p=390816). Published 2005-06-10. Trying practices incrementally and starting improvements as an individual.
[^beck-andres-primary-practices]: [Appendix: Primary Practices](https://www.informit.com/articles/article.aspx?p=390816&seqNum=3). Summary of practices in the same article, distinct from specific solo procedures.
[^minodriven-designing-for-code-reading]: [Designing for code reading](https://speakerdeck.com/minodriven/designing-for-code-reading), MinoDriven, 2026-09-30. Contract/test, side-effect-isolation, and abstraction ideas, with local adoption limits above.
[^github-instructions-oop-design-patterns-instructions-md]: [OOP Design Patterns](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^github-instructions-self-explanatory-code-commenting-instructions-md]: [Self-explanatory Code Commenting](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^github-instructions-qa-engineering-best-practices-instructions-md]: [QA Engineering Best Practices](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^context-engineering]: [Context Engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md). Applied to naming, placement, types, public boundaries, and comment design.
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Applied to choosing standard features, existing dependencies, and minimal structure.

## Change-record policy adoption

[Development](../../skills/software-development/SKILL.md) and its design/testing references apply the agreement in [Issue #253](https://github.com/daiksud/agents/issues/253).[^change-record-agreement] The current rationale and boundaries live in [Change records policy](../engineering-policies/change-records.md): actual validation reporting is required while execution is discretionary unless independently required; PRs/commits retain historical judgment and topical policies retain current guidance. This adoption does not establish renewed checking of the external sources above.

[^change-record-agreement]: Owner-agreed change-record policy and implementation scope in Issue #253.
