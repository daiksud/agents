---
type: Reference
title: Sources for design and testing
description: Retain implementation, design, and testing sources, existing verification history, and adoption decisions.
sources:
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
---

## Sources for design and testing

### Primary materials

The reference date is 2026-09-11. Undated means the publication or update date could not be established. These are sources of definitions and recommendations, not measurements of this skill's effectiveness.

| Author and material | Date and referenced location | Use in this skill |
| --- | --- | --- |
| Kent Beck, Canon TDD[^newsletter-p-canon-tdd] | 2023-12-11 | Test lists, one-at-a-time iterations, and retaining expectations |
| Jez Humble, Continuous Testing[^continuousdelivery-foundations-test-automation], Architecture[^continuousdelivery-implementing-architecture] | Undated | Fast feedback, exploration, testability, and incremental design improvement |
| Eric Evans, DDD Reference[^www-05-ddd-reference-2015-03-pdf] | March 2015, booklet pages 39–41 and others | Bounded Context, Ubiquitous Language, and Context Map |

### Adoption decisions for XP values

Ron Jeffries' What is Extreme Programming?[^ron-jeffries-xp] was checked on 2026-09-25. Apply Communication, Simplicity, Feedback, Courage, and Respect to sharing actual expectations, structure suited to current requirements, short validation, necessary design improvements, decision authority, and sustainable work. Do not make fixed meeting formats, team arrangements, or effectiveness figures from the originals shared requirements. Preserve agent authority, approval, publication, and review conditions as contracts of this environment.

### Adoption decisions for Simple Design and YAGNI

Martin Fowler's Beck Design Rules[^fowler-beck-design-rules] and Yagni[^fowler-yagni] were checked on 2026-09-25. Judge design from current tests and contracts, clarity of intent, duplication of the same rules, and necessary elements. Do not anticipate hypothetical future features; improve incrementally through actual feedback. Do not assign mechanical priority or scores between clarity and duplication, or omit necessary tests, Refactor, or CI. Assert-first and stage confirmation by the same Navigator are local policies, not requirements attributed to original XP sources.

### Adoption decisions for introducing XP alone

Kent Beck / Cynthia Andres' introductory article[^beck-andres-getting-started-xp] and Primary Practices summary[^beck-andres-primary-practices] were checked on 2026-10-04. The introduction allows trying practices one at a time and improving as an individual. The summary lists Test-first Programming, Incremental Design, Stories, Weekly Planning, Slack, Ten-minute Build, Continuous Integration, and Energized Work. Original CI integrates into shared code within hours; automated builds and tests support short feedback. The target of integrating into main on each active day is existing local operation, not the same frequency as the original.

Starting with TDD, incremental design, and automated validation; selecting outcomes at the start of the week and briefly reflecting at its end; reusing existing Issues and ToDos; adjusting scope while preserving quality; and handing off during rest are local solo proposals. They are not verbatim original provisions or claims that all XP practices are implemented. Preserve AI collaboration and review conditions even with one human. Do not add fixed meetings, weekly automation, or assumptions about fatigue.

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
| Context Engineering[^context-engineering] | Use meaningful names, paths, constants, discoverable placement, boundary types and public contracts, and explanations of complex flow. Prioritize existing placement and language conventions; do not require banning local type inference, uniform index files, internal exposure, or IDE operations |
| Taming Copilot[^taming-copilot] | Consider standard features and existing dependencies first and integrate necessary changes into existing structure. Do not omit required contracts, error cases, or TDD, or use shortest code or only user-listed files as the scope criterion |

[^newsletter-p-canon-tdd]: [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-foundations-test-automation]: [Continuous Testing](https://continuousdelivery.com/foundations/test-automation/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-implementing-architecture]: [Architecture](https://continuousdelivery.com/implementing/architecture/). Basis for the referenced scope and adoption decisions stated in the text.
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^ron-jeffries-xp]: [What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/). Applying the five values and practices to the situation.
[^fowler-beck-design-rules]: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html). Fowler’s formulation reviewed by Kent Beck himself.
[^fowler-yagni]: [Yagni](https://martinfowler.com/bliki/Yagni.html). Distinguishes unrequested features from health supporting current changes.
[^beck-andres-getting-started-xp]: [Getting Started with eXtreme Programming: Toe Dipping, Racing Dives, and Cannonballs](https://www.informit.com/articles/article.aspx?p=390816). Published 2005-06-10. Trying practices incrementally and starting improvements as an individual.
[^beck-andres-primary-practices]: [Appendix: Primary Practices](https://www.informit.com/articles/article.aspx?p=390816&seqNum=3). Summary of practices in the same article, distinct from specific solo procedures.
[^github-instructions-oop-design-patterns-instructions-md]: [OOP Design Patterns](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^github-instructions-self-explanatory-code-commenting-instructions-md]: [Self-explanatory Code Commenting](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^github-instructions-qa-engineering-best-practices-instructions-md]: [QA Engineering Best Practices](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^context-engineering]: [Context Engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md). Applied to naming, placement, types, public boundaries, and comment design.
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Applied to choosing standard features, existing dependencies, and minimal structure.
