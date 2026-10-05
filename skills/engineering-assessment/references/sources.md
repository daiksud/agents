---
type: Reference
title: Primary materials and application decisions
description: Distinguish primary assessment sources, version differences, source summaries, and this skill’s application decisions.
sources:
  - id: github-instructions-devops-core-principles-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/devops-core-principles.instructions.md
  - id: www-explore-lean-what-is-lean
    resource: https://www.lean.org/explore-lean/what-is-lean/
  - id: tech-lean-practice
    resource: https://tech.lean.org/lean-practice
  - id: dora-guides-how-to-transform
    resource: https://dora.dev/guides/how-to-transform/
  - id: dora-capabilities-wip-limits
    resource: https://dora.dev/capabilities/wip-limits/
  - id: dora-capabilities-generative-organizational-culture
    resource: https://dora.dev/capabilities/generative-organizational-culture/
  - id: continuousdelivery
    resource: https://continuousdelivery.com/
  - id: continuousdelivery-principles
    resource: https://continuousdelivery.com/principles/
  - id: continuousdelivery-foundations-continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: martinfowler-articles-continuousintegration-html
    resource: https://martinfowler.com/articles/continuousIntegration.html
  - id: continuousdelivery-implementing-patterns
    resource: https://continuousdelivery.com/implementing/patterns/
  - id: continuousdelivery-foundations-configuration-management
    resource: https://continuousdelivery.com/foundations/configuration-management/
  - id: continuousdelivery-foundations-test-automation
    resource: https://continuousdelivery.com/foundations/test-automation/
  - id: continuousdelivery-implementing-architecture
    resource: https://continuousdelivery.com/implementing/architecture/
  - id: dora-guides-dora-metrics
    resource: https://dora.dev/guides/dora-metrics/
  - id: dora-insights-dora-metrics-history
    resource: https://dora.dev/insights/dora-metrics-history/
  - id: dora-assets-dora-core-v2-1-0-detail-pdf
    resource: https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf
  - id: dora-research
    resource: https://dora.dev/research/
  - id: dora-capabilities-catalog
    resource: https://dora.dev/capabilities/
  - id: dora-capabilities-working-in-small-batches
    resource: https://dora.dev/capabilities/working-in-small-batches/
  - id: dora-capabilities-loosely-coupled-teams
    resource: https://dora.dev/capabilities/loosely-coupled-teams/
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: informit-xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
  - id: oreilly-xp-principles
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml
  - id: oreilly-xp-primary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml
  - id: oreilly-xp-corollary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml
  - id: cucumber-docs-bdd
    resource: https://cucumber.io/docs/bdd/
  - id: cucumber-bdd-example-mapping
    resource: https://cucumber.io/docs/bdd/example-mapping/
  - id: cucumber-bdd-better-gherkin
    resource: https://cucumber.io/docs/bdd/better-gherkin/
  - id: agilealliance-glossary-atdd
    resource: https://agilealliance.org/glossary/atdd/
  - id: curiousduck-collections-2024-06-27-atdd
    resource: https://curiousduck.io/posts/collections/2024-06-27-atdd/
  - id: newsletter-p-canon-tdd
    resource: https://newsletter.kentbeck.com/p/canon-tdd
  - id: www-05-ddd-reference-2015-03-pdf
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
  - id: www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf
  - id: teamtopologies-key-concepts
    resource: https://teamtopologies.com/key-concepts
  - id: github-teamtopologies-team-api-template
    resource: https://github.com/TeamTopologies/Team-API-template
  - id: github-teamtopologies-team-dependencies-tracking
    resource: https://github.com/TeamTopologies/Team-Dependencies-Tracking
  - id: teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf
    resource: https://teamtopologies.com/s/Finding-software-boundaries-for-fast-flow-Team-Topologies-and-Domain-Driven-Design-mini-book-MB81-v1.pdf
---

## Primary materials and application decisions

Existing materials were checked on 2026-09-11, XP five-Values materials on 2026-09-26, and materials added for second-edition XP taxonomy, Architecture / Organization lenses, and DORA model organization on 2026-09-27. Rather than reproducing translations of the following, they were summarized and restructured in [principle relationships](principles.md), [assessment procedures](assessment.md), and conditional focused references. Do not label verification dates as publication dates for undated materials. In later assessments, record versions and verification dates actually referenced.

### DevOps, Lean, and improvement

| Material and author | Reference points and cautions |
| --- | --- |
| DevOps Core Principles — GitHub awesome-copilot[^github-instructions-devops-core-principles-instructions-md] (checked 2026-09-11) | Make CALMS, end-to-end responsibility, operational observation, and procedure sharing concrete for assessment. Do not mandate full automation or particular products; update fixed Four Keys, MTTR, and Elite values to current DORA definitions. Reference as community instruction examples |
| What is Lean? — Lean Enterprise Institute[^www-explore-lean-what-is-lean] | Consider value, work, people, and continuous experiments from customer problems |
| Lean practice — LEI[^tech-lean-practice] | Value, value streams, flow, pull, and improvement |
| How to transform — Jez Humble / DORA[^dora-guides-how-to-transform] (updated 2025-10-06) | Improve through current states, target states, constraints, and small experiments |
| WIP limits — DORA[^dora-capabilities-wip-limits] | Address work in progress and bottlenecks, including invisible work |
| Generative organizational culture — DORA[^dora-capabilities-generative-organizational-culture] | Do not judge cooperation, information sharing, and learning from policy files alone |

### CI, CD, and measurement

| Material and author | Reference points and cautions |
| --- | --- |
| Continuous Delivery — Jez Humble[^continuousdelivery], principles[^continuousdelivery-principles] | Deliverable state, built-in quality, small batches, shared responsibility |
| CI foundations[^continuousdelivery-foundations-continuous-integration], Continuous Integration — Martin Fowler[^martinfowler-articles-continuousintegration-html] (2024-01-18 version) | Frequent integration into shared main, fast automated checks, broken-build repair, and distinction from CI tools |
| Delivery patterns[^continuousdelivery-implementing-patterns], configuration management[^continuousdelivery-foundations-configuration-management] | Build artifacts once and promote between environments; track configuration, dependencies, and recovery |
| Test automation[^continuousdelivery-foundations-test-automation], architecture[^continuousdelivery-implementing-architecture] | Improve testability and deployability from small footholds, including exploration |
| Software delivery performance metrics — Nathen Harvey / DORA[^dora-guides-dora-metrics] (updated 2026-01-05) | Current five-metric definitions, application-level measurement, avoiding competition, single metrics, and excessive measurement investment |
| Metrics history — DORA[^dora-insights-dora-metrics-history] (updated 2026-01-02) | Changes in recovery metric targets, added rework, distinction between reliability and delivery metrics |
| DORA Core v2.1.0[^dora-assets-dora-core-v2-1-0-detail-pdf], research model explanation[^dora-research] | Core is a stable research model with a different update cycle from the latest guide. Do not confuse its four-metric diagram with the current five metrics |
| DORA Capability Catalog[^dora-capabilities-catalog] (checked 2026-09-27) | Includes items labeled `core` / `AI` and items outside Core. Do not equate the whole Catalog with Core or required adoption; choose only problem-relevant capabilities |
| Working in small batches — DORA[^dora-capabilities-working-in-small-batches] (checked 2026-09-27) | Check Lean product management, short feedback loops, and overlap of `core` / `AI` labels. Do not treat XP / Lean Practice and DORA Capability classifications as contradictory |

DORA text and figures are Google LLC's CC BY 4.0, except where individual pages state exceptions. This skill summarizes materials and provides application guidance; it is not DORA certification or a guarantee of universal causality.

### XP values and small feedback

| Material and author | Reference points and cautions |
| --- | --- |
| What is Extreme Programming? — Ron Jeffries[^ron-jeffries-xp] (checked 2026-09-26) | Apply Communication, Simplicity, Feedback, Courage, and Respect to current requirements, small feedback, and continuous design improvement. Do not make fixed meeting/role/period formats or original effectiveness figures shared requirements |
| Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres[^informit-xp-second-edition] (2004, checked 2026-09-27) | Distinguish Values / Principles / Practices; reflect names and classifications of the TOC's 14 Principles, 13 Primary Practices, and 11 Corollary Practices in runtime taxonomy. The same publisher introduction says “Eleven principles”; adopt the TOC count and retain the discrepancy. Do not make Practice counts maturity measures or mandatory checklists |
| XP 2nd ed. Principles / Primary / Corollary chapters — O'Reilly licensed preview[^oreilly-xp-principles][^oreilly-xp-primary-practices][^oreilly-xp-corollary-practices] (checked 2026-09-27) | Beyond named taxonomy, check Principles bridging Values and behavior, selecting Primary Practices from the greatest local improvement opportunities, and Corollary Practices' potential difficulty/danger without Primary foundations. `xp.md` retains taxonomy and routing; diagnostic meanings in `xp-auxiliary.md` are short application paraphrases for this skill, not reproduced originals |

Treating five values as diagnostic questions and avoiding judging XP success by Practice counts or particular organizational forms are this skill's application decisions.

### BDD, ATDD, TDD, DDD, and Team Topologies

| Material and author | Reference points and cautions |
| --- | --- |
| BDD — Cucumber[^cucumber-docs-bdd], Example Mapping[^cucumber-bdd-example-mapping], Better Gherkin[^cucumber-bdd-better-gherkin] | Discovery, formulation, automation, rules/examples/questions, and declarative concrete examples. Do not equate BDD with file formats alone |
| ATDD — Agile Alliance[^agilealliance-glossary-atdd] | Create acceptance tests before implementation from customer, development, and testing perspectives |
| ATDD revisited — Elisabeth Hendrickson[^curiousduck-collections-2024-06-27-atdd] (2024-06-27) | Practical reflection against making heavyweight all-hands meetings or natural-language automation ends in themselves. Does not replace the BDD definition |
| Canon TDD — Kent Beck[^newsletter-p-canon-tdd] (2023-12-11) | Iterate failure, minimal implementation, and necessary cleanup one at a time from a test list |
| DDD Reference — Eric Evans[^www-05-ddd-reference-2015-03-pdf] (2015-03) | Terminology, models, boundaries, Context Maps, and focus on business complexity |
| Getting started with DDD in legacy systems — Eric Evans[^www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf] (2013) | Start at small boundaries surrounded by existing systems |
| Key Concepts — Team Topologies[^teamtopologies-key-concepts] | Four team types, three interactions, value flow, cognitive load |
| Team API[^github-teamtopologies-team-api-template], Dependencies Tracking[^github-teamtopologies-team-dependencies-tracking] | Responsibilities and engagement; distinguish blocking dependencies from service use |
| Finding software boundaries — Team Topologies / DDD mini-book[^teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf] (2023-05-19) | Overlay team and context maps; includes one team owning multiple boundaries |
| Loosely coupled teams — DORA[^dora-capabilities-loosely-coupled-teams] (checked 2026-09-27) | Assess independent change/test/deploy and low cross-team coordination as capabilities, rather than architecture styles or service counts. Do not default to Microservices; distinguish monoliths that can meet outcomes |

This skill's proportionality to solo development; organization into observed, gap, unverified, and not-applicable states; and selection of answers, Issue records, documents, or implementation handoffs according to the requested terminal deliverable are design decisions applying these materials to the working environment. Assessment topics alone do not require Issue saving. Issues may be saved through the applicable path when Issue recording is the terminal deliverable, or when existing workflows require supporting records for implementation plans, shared-standard candidates, or weakly related follow-up requests. Do not reinterpret supporting Issues as the current terminal deliverable. Do not present these decisions as official maturity scales or organizational standards.

[^github-instructions-devops-core-principles-instructions-md]: [DevOps Core Principles — GitHub awesome-copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/devops-core-principles.instructions.md). Basis for the referenced scope and adoption decisions stated in the text.
[^www-explore-lean-what-is-lean]: [What is Lean? — Lean Enterprise Institute](https://www.lean.org/explore-lean/what-is-lean/). Basis for the referenced scope and adoption decisions stated in the text.
[^tech-lean-practice]: [Lean practice — LEI](https://tech.lean.org/lean-practice). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-guides-how-to-transform]: [How to transform — Jez Humble / DORA](https://dora.dev/guides/how-to-transform/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-capabilities-wip-limits]: [WIP limits — DORA](https://dora.dev/capabilities/wip-limits/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-capabilities-generative-organizational-culture]: [Generative organizational culture — DORA](https://dora.dev/capabilities/generative-organizational-culture/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery]: [Continuous Delivery — Jez Humble](https://continuousdelivery.com/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-principles]: [Principles](https://continuousdelivery.com/principles/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-foundations-continuous-integration]: [CI foundations](https://continuousdelivery.com/foundations/continuous-integration/). Basis for the referenced scope and adoption decisions stated in the text.
[^martinfowler-articles-continuousintegration-html]: [Continuous Integration — Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-implementing-patterns]: [Delivery patterns](https://continuousdelivery.com/implementing/patterns/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-foundations-configuration-management]: [Configuration management](https://continuousdelivery.com/foundations/configuration-management/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-foundations-test-automation]: [Test automation](https://continuousdelivery.com/foundations/test-automation/). Basis for the referenced scope and adoption decisions stated in the text.
[^continuousdelivery-implementing-architecture]: [Architecture](https://continuousdelivery.com/implementing/architecture/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-guides-dora-metrics]: [Software delivery performance metrics — Nathen Harvey / DORA](https://dora.dev/guides/dora-metrics/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-insights-dora-metrics-history]: [Metrics history — DORA](https://dora.dev/insights/dora-metrics-history/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-assets-dora-core-v2-1-0-detail-pdf]: [DORA Core v2.1.0](https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-research]: [Research model explanation](https://dora.dev/research/). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-capabilities-catalog]: [DORA Capability Catalog](https://dora.dev/capabilities/). Check Core / AI labels and differences between the full Catalog and Core Model. Checked 2026-09-27.
[^dora-capabilities-working-in-small-batches]: [Working in small batches — DORA](https://dora.dev/capabilities/working-in-small-batches/). Check Core / AI labels, short feedback loops, and Lean product management relationships. Checked 2026-09-27.
[^ron-jeffries-xp]: [What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/). References and application decisions for the five values, current requirements, small feedback, and design improvement.
[^informit-xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — InformIT](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987). Base taxonomy on the 2004 edition’s Table of Contents. The TOC lists 14 named Principles while the same page’s introduction says “Eleven principles”; retain that discrepancy. Checked 2026-09-27.
[^oreilly-xp-principles]: [Chapter 5. Principles — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml). Chapter structure treating Principles as bridges between Values and concrete behavior. Checked 2026-09-27.
[^oreilly-xp-primary-practices]: [Chapter 7. Primary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml). Selecting Primary Practices according to environment and greatest improvement opportunities. Checked 2026-09-27.
[^oreilly-xp-corollary-practices]: [Chapter 9. Corollary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml). Cautions on using Corollary Practices with Primary foundations and application conditions. Checked 2026-09-27.
[^cucumber-docs-bdd]: [BDD — Cucumber](https://cucumber.io/docs/bdd/). Basis for the referenced scope and adoption decisions stated in the text.
[^cucumber-bdd-example-mapping]: [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/). Basis for the referenced scope and adoption decisions stated in the text.
[^cucumber-bdd-better-gherkin]: [Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/). Basis for the referenced scope and adoption decisions stated in the text.
[^agilealliance-glossary-atdd]: [ATDD — Agile Alliance](https://agilealliance.org/glossary/atdd/). Basis for the referenced scope and adoption decisions stated in the text.
[^curiousduck-collections-2024-06-27-atdd]: [ATDD revisited — Elisabeth Hendrickson](https://curiousduck.io/posts/collections/2024-06-27-atdd/). Basis for the referenced scope and adoption decisions stated in the text.
[^newsletter-p-canon-tdd]: [Canon TDD — Kent Beck](https://newsletter.kentbeck.com/p/canon-tdd). Basis for the referenced scope and adoption decisions stated in the text.
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf]: [Getting started with DDD in legacy systems — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^teamtopologies-key-concepts]: [Key Concepts — Team Topologies](https://teamtopologies.com/key-concepts). Basis for the referenced scope and adoption decisions stated in the text.
[^github-teamtopologies-team-api-template]: [Team API](https://github.com/TeamTopologies/Team-API-template). Basis for the referenced scope and adoption decisions stated in the text.
[^github-teamtopologies-team-dependencies-tracking]: [Dependencies Tracking](https://github.com/TeamTopologies/Team-Dependencies-Tracking). Basis for the referenced scope and adoption decisions stated in the text.
[^teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf]: [Finding software boundaries — Team Topologies / DDD mini-book](https://teamtopologies.com/s/Finding-software-boundaries-for-fast-flow-Team-Topologies-and-Domain-Driven-Design-mini-book-MB81-v1.pdf). Basis for the referenced scope and adoption decisions stated in the text.
[^dora-capabilities-loosely-coupled-teams]: [Loosely coupled teams — DORA](https://dora.dev/capabilities/loosely-coupled-teams/). Basis for assessing independent change/test/deploy, team coupling, Inverse Conway, and Microservices trade-offs. Checked 2026-09-27.
