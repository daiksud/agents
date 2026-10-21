---
type: Reference
title: behavior-specification sources and maintenance notes
description: Human-facing source mappings, adoption rationale, and retained checking history for behavior-specification.
sources:
- id: cucumber-docs-bdd
  resource: https://cucumber.io/docs/bdd/
- id: cucumber-bdd-examples
  resource: https://cucumber.io/docs/bdd/examples/
- id: cucumber-bdd-better-gherkin
  resource: https://cucumber.io/docs/bdd/better-gherkin/
- id: cucumber-bdd-example-mapping
  resource: https://cucumber.io/docs/bdd/example-mapping/
- id: cucumber-gherkin-reference
  resource: https://cucumber.io/docs/gherkin/reference/
- id: newsletter-p-canon-tdd
  resource: https://newsletter.kentbeck.com/p/canon-tdd
- id: agilealliance-glossary-atdd
  resource: https://agilealliance.org/glossary/atdd/
- id: curiousduck-collections-2024-06-27-atdd
  resource: https://curiousduck.io/posts/collections/2024-06-27-atdd/
- id: lizkeogh-20-acceptance-criteria-vs-scenarios
  resource: https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/
- id: gherkin-markdown
  resource: https://github.com/cucumber/gherkin/blob/main/MARKDOWN_WITH_GHERKIN.md
- id: gherkin-ja
  resource: https://github.com/cucumber/gherkin/blob/5c869e7b75c7d1a40f70b8ab2bd1148600467fab/gherkin-languages.json#L1944-L1994
---

## Purpose and runtime documents

These are maintainer notes for [behavior-specification](../../skills/behavior-specification/SKILL.md). Runtime entry points and task references retain the instructions needed for execution; this document preserves attribution and background for maintenance. Any source-check dates below are retained history, not new verification performed during this separation.

### Source mapping

Source IDs are preserved from the original files, including aliases for the same URL. Local `practice-sources` bindings identified the former bundled catalog; its content is retained in this note.

| Runtime document or original catalog | Source mapping |
| --- | --- |
| Former bundled source catalog (`references/sources.md`) | [Sources for shared understanding and acceptance specifications](#sources-for-shared-understanding-and-acceptance-specifications) retains its source IDs and adoption notes |
| [references/behavior.md](../../skills/behavior-specification/references/behavior.md) | `practice-sources` (original resource: `sources.md`; catalog retained here), [^gherkin-markdown], [^gherkin-ja] |

## Sources for shared understanding and acceptance specifications

### Primary sources

The reference date is 2026-09-11. Undated material has no confirmed publication/update date. These are sources of definitions and proposals, not measurements of this skill's effectiveness.

| Author and material | Date and referenced section | Use in this skill |
| --- | --- | --- |
| Cucumber, Behaviour-Driven Development[^cucumber-docs-bdd] | Page update display 2026-09-10; not the concept's origin date | Shared understanding and Discovery / Formulation / Automation |
| Cucumber, Examples[^cucumber-bdd-examples], Writing better Gherkin[^cucumber-bdd-better-gherkin] | Undated | Business-meaningful specificity and declarative descriptions |
| Cucumber, Example Mapping[^cucumber-bdd-example-mapping], Gherkin Reference[^cucumber-gherkin-reference] | Undated | Distinguishing rules, examples, and questions; Rule and Scenario |
| Kent Beck, Canon TDD[^newsletter-p-canon-tdd] | 2023-12-11 | Test lists, one-at-a-time iteration, preserving expectations |
| Agile Alliance, Acceptance Test Driven Development[^agilealliance-glossary-atdd] | Undated | Acceptance tests before implementation and collaboration across perspectives |
| Elisabeth Hendrickson, ATDD Revisited[^curiousduck-collections-2024-06-27-atdd] | 2024-06-27 | Reassessment of 2008 practice, adapting participation and automation formats |
| Liz Keogh, Acceptance Criteria vs. Scenarios[^lizkeogh-20-acceptance-criteria-vs-scenarios] | 2011-06-20 | Differences between abstract conditions and concrete examples |

## Participation and automation rationale

Human-readable requirements must map to automated tests, but direct execution of the same file is not mandatory. Hendrickson's 2024 reassessment recommends few examples and necessary participants from experience of natural-language automation and synchronous collaboration involving everyone becoming burdensome. Cucumber, meanwhile, emphasizes dialogue across differing expertise. Preserve this difference and choose methods that obtain stakeholders' knowledge and confirm shared understanding.[^curiousduck-collections-2024-06-27-atdd] [^cucumber-docs-bdd]

## Retained source annotations

These annotations preserve the original per-file attribution and checking details.

### references/behavior.md

- `gherkin-markdown`: Moved the format rule and reference from the existing SKILL.md, preserving the original reference rather than adding a specification change or checking history.
- `gherkin-ja`: The fixed version of Japanese keywords specified in the existing SKILL.md.
- `practice-sources`: References and application decisions for BDD/ATDD and rules, examples, and questions.

[^gherkin-markdown]: [Markdown with Gherkin](https://github.com/cucumber/gherkin/blob/main/MARKDOWN_WITH_GHERKIN.md). Moved the format rule and reference from the existing SKILL.md, preserving the original reference rather than adding a specification change or checking history.
[^gherkin-ja]: [Japanese Gherkin keywords](https://github.com/cucumber/gherkin/blob/5c869e7b75c7d1a40f70b8ab2bd1148600467fab/gherkin-languages.json#L1944-L1994). The fixed version of Japanese keywords specified in the existing SKILL.md.
[^cucumber-docs-bdd]: [Behaviour-Driven Development](https://cucumber.io/docs/bdd/). Evidence for the reference scope and adoption decisions stated in the text.
[^cucumber-bdd-examples]: [Examples](https://cucumber.io/docs/bdd/examples/). Evidence for the reference scope and adoption decisions stated in the text.
[^cucumber-bdd-better-gherkin]: [Writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/). Evidence for the reference scope and adoption decisions stated in the text.
[^cucumber-bdd-example-mapping]: [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/). Evidence for the reference scope and adoption decisions stated in the text.
[^cucumber-gherkin-reference]: [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/). Evidence for the reference scope and adoption decisions stated in the text.
[^newsletter-p-canon-tdd]: [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd). Evidence for the reference scope and adoption decisions stated in the text.
[^agilealliance-glossary-atdd]: [Acceptance Test Driven Development](https://agilealliance.org/glossary/atdd/). Evidence for the reference scope and adoption decisions stated in the text.
[^curiousduck-collections-2024-06-27-atdd]: [ATDD Revisited](https://curiousduck.io/posts/collections/2024-06-27-atdd/). Evidence for the reference scope and adoption decisions stated in the text.
[^lizkeogh-20-acceptance-criteria-vs-scenarios]: [Acceptance Criteria vs. Scenarios](https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/). Evidence for the reference scope and adoption decisions stated in the text.
