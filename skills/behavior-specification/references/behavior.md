---
type: Reference
title: Shared understanding and feature documents
description: Define shared understanding in BDD/ATDD, declarative examples, and repository-language Markdown with Gherkin.
sources:
  - id: practice-sources
    resource: sources.md
  - id: gherkin-markdown
    resource: https://github.com/cucumber/gherkin/blob/main/MARKDOWN_WITH_GHERKIN.md
  - id: gherkin-ja
    resource: https://github.com/cucumber/gherkin/blob/5c869e7b75c7d1a40f70b8ab2bd1148600467fab/gherkin-languages.json#L1944-L1994
---

## Shared understanding and feature documents

Use this material for specification work and document creation without code, without starting TDD. When code changes are requested, hand agreed specifications to the dependency [software-development](../../software-development/SKILL.md).

### Shared understanding and acceptance conditions (BDD/ATDD)

- For systems and features, tell the story of “who can do what, in which situation, after completion” before design. Record it in existing Issue purposes or feature descriptions, making it observable through acceptance conditions and concrete examples. Do not require fixed syntax or separate story documents.
- Reuse agreed stories. If whose problem is resolved or the completed result is unsettled, retain questions; do not treat AI-assumed stories as agreed. Connect technical fixes and cleanup to existing purposes and expected results, without adding a stage of writing a new story every time.
- Before implementation, organize purposes, rules, representative examples, and unanswered questions from user, business, development, and validation perspectives. Iterate BDD Discovery, Formulation, and Automation in small cycles.
- Distinguish expectations established by agreed specifications from new proposals or assumptions. Retain examples with unsettled outcomes as questions, and confirm business decisions before implementation.
- Choose how to check with people having necessary knowledge. Do not require synchronous meetings or fixed participant counts every time, or record AI role-playing as stakeholder agreement.
- Define acceptance conditions and examples showing their meaning before corresponding implementation. Clarify observable acceptance results and connect them to automated tests checking expectations.
- For domain-rule additions or changes, create or update `docs/behavior/<feature-name>.feature.md` before implementation. Shared specifications of contracts with API users or operators may use the same format with explicit readers and observable results.
- Separate abstract rules from concrete scenarios. Include amounts, dates, and input/output examples meaningful for understanding rules or boundaries; omit unrelated data and internal implementation steps.
- Do not mix UI click sequences, internal classes, communication methods, or persistence methods into business specifications. However, do not exclude externally promised responses, saved results, or notifications as implementation detail.
- Keep human-readable specifications and automated tests traceable and consistent when specifications change. Direct execution of natural-language files or installing Cucumber is not mandatory.

### Feature document format

- Apply `document-authoring` and follow Markdown with Gherkin.[^gherkin-markdown]
- Follow [Repository artifact language](../../../.apm/instructions/language.instructions.md). For Japanese repositories, use Japanese keywords:[^gherkin-ja] headings `機能`, `背景`, `ルール`, and `シナリオ`; bulleted steps `前提`, `もし`, `ならば`, `かつ`, and `しかし`. For English repositories, use headings `Feature`, `Background`, `Rule`, and `Scenario`; bulleted steps `Given`, `When`, `Then`, `And`, and `But`.
- When parsing, select the matching dialect (`ja` for Japanese, `en` for English). Check heading and step structure after rumdl formatting.
- While editing is unavailable in Plan mode, show drafts within the plan; save before implementation code once editing is possible.

### Relationships and application decisions

BDD is collaborative practice developing shared understanding through examples; Cucumber describes it as iterating Discovery, Formulation, and Automation. ATDD considers acceptance tests before implementation, connecting requirements and validation. Their subjects overlap; this does not mean adding separate mandatory meetings or stages. TDD is programming iteration that progresses tests and implementation one at a time from a list of expected-behavior tests.

This skill starts with stories to organize purposes, rules, meaningful examples, acceptance conditions, and unanswered questions. Only when code changes are also requested does it hand agreed specifications and examples to `software-development`, connecting to that skill's test-first and assert-first implementation. Specification-only requests do not start implementation or TDD. Story-first work and conditional handoff are this environment's operating policy. Do not treat BDD, ATDD, and TDD as synonyms or claim one universal procedure for all organizations.

Human-readable requirements must map to automated tests, but direct execution of the same file is not mandatory. Hendrickson's 2024 reassessment recommends few examples and necessary participants from experience of natural-language automation and synchronous collaboration involving everyone becoming burdensome. Cucumber, meanwhile, emphasizes dialogue across differing expertise. Preserve this difference and choose methods that obtain stakeholders' knowledge and confirm shared understanding.

### Concrete, declarative example

The following Japanese-repository example assumes agreement on the story “buyers can understand applicable shipping costs when ordering” and the rule “shipping is free when the tax-inclusive product total is at least 5,000 yen.” Do not reuse this amount or total definition as settled facts in another business.

```markdown
## 機能: 注文の送料を決定する

購入者が注文するとき、税込商品合計に応じた送料を把握できる。

### ルール: 税込商品合計が5,000円以上なら送料無料

#### シナリオ: 無料になる境界の金額

- 前提: 注文の税込商品合計が5,000円である
- もし: 注文の送料を決定する
- ならば: 送料は0円になる
```

Examples at 4,999 yen or exceptional paths for the same rule can also check rule interpretation. Keep amounts concrete without exposing cart-screen click sequences or internal function names. Retain unsettled shipping charges or treatment of discounted amounts as questions rather than guessing expectations.

When saving the content above, add frontmatter following `document-authoring`. File paths and repository-language Markdown with Gherkin are this environment's operating conventions, not universal definitions of BDD.

Preserve sources and adoption decisions for shared understanding and examples in [Primary sources](sources.md).[^practice-sources]

[^gherkin-markdown]: Moved the format rule and reference from the existing SKILL.md, preserving the original reference rather than adding a specification change or checking history.
[^gherkin-ja]: The fixed version of Japanese keywords specified in the existing SKILL.md.
[^practice-sources]: References and application decisions for BDD/ATDD and rules, examples, and questions.
