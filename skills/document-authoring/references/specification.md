---
type: Guide
title: Clarifying specifications with existing documents
description: Show procedures for recording requirements, constraints, external contracts, and acceptance conditions in existing authoritative documents, clarifying uncertainties and validation mappings.
---

## Clarifying specifications with existing documents

Write specifications so people and agents understand the same expectations and verify achievement. Begin by checking actors, purpose, success conditions, readers, model boundaries, and existing agreed specifications, rather than creating an overall specification document.

Distinguish actors using systems from readers making decisions from specifications. State whether information serves API users, implementers, validators, or others; retain questions if readership is unconfirmed.

### Choose authoritative sources and placement

1. Find target glossaries, features, Engineering Policies or ADRs, API documents, schemas, and related tests; identify authoritative sources for current requirements/contracts. Retain conflicts with unknown precedence as questions to authorized people.
2. Record effective behavior in features, current design guidance in topical documents, and API/data contracts in existing API documents/schemas. Historical reasons and comparisons belong in self-contained PR/commit messages. Do not duplicate specifications in separate documents.
3. Add documents to appropriate existing categories only where authoritative sources are missing. Shared behavior uses `docs/behavior/`; current policy uses existing placement under [Current policy authoring](engineering-policies.md). Do not require a policy directory, `/spec/`, or separate overall specifications for every change.
4. Give ordinary Markdown concepts OKF-required type and this environment's additional title/description. Use reserved formats for indexes/logs. Preserve OpenAPI, JSON Schema, and other contract formats without OKF headers. Align terminology with target `docs/glossary.md`, updating changed meanings and applicable model boundaries.

When human-readable specifications and machine-readable contracts such as OpenAPI coexist, show authoritative sources and mappings for each item. Retain purpose, assumptions, and references sufficient for standalone understanding, without duplicating entire glossaries/schemas to eliminate external context. Check linked existence/versions; inaccessible information remains unverified.

### Make necessary content concrete

Describe needed items below for target decisions, implementation, and validation. Do not require fixed chapter numbers or every section, or create empty sections.

| Content | Clarify |
| --- | --- |
| Purpose and readers | Who wants which state, scope, existing assumptions, and expectations changed now |
| Requirements, constraints, recommendations | Distinguish required behavior, selection restrictions, and optional improvements. Do not turn recommendations into agreed requirements |
| External contracts | Decision-relevant inputs/outputs, meanings/units, failures, side effects, defaults, and compatibility; refer to existing authoritative sources |
| Acceptance conditions | Observable results establishing each requirement, mapped to examples including necessary boundaries/exceptional paths |
| Dependencies and constraints | Needed external capabilities/contracts and effective constraints. Put the reasons for selecting or changing them in the PR/commit |
| Validation mappings | Trace corresponding tests/procedures and observed results. Use existing identifiers/stable headings when tracking from multiple locations is needed |
| Unsettled matters | Separate expectations from assumptions/proposals/questions, identifying whose decisions are needed. Do not invent unagreed thresholds or business failure handling |

Keep business-meaningful amounts, dates, and inputs in acceptance examples. Do not mix UI click sequences or internal-class construction into business rules; promised API-user/operator responses, saved results, and notifications are contracts.

Document creation alone does not require TDD execution. When code changes are requested, carry agreed specifications, unanswered questions, and validation mappings into the approved implementation; use test-first techniques when selected or independently required.

For example, with existing shipping features and quotation API OpenAPI, update features as authoritative for free-shipping conditions and OpenAPI for request/response formats, connecting corresponding tests. If whether subtotal is before or after discounts is unagreed, retain a question without creating an independent definition in a new overall specification.

### Feature documents

Save domain-rule additions or changes in `docs/behavior/<feature-name>.feature.md` before implementation. Reuse correct existing specifications. Apply [OKF frontmatter](basic-format.md) and [Markdown with Gherkin](https://github.com/cucumber/gherkin/blob/main/MARKDOWN_WITH_GHERKIN.md), keeping rules separate from concrete scenarios and observable acceptance results.

- In Japanese repositories, use headings `機能`, `背景`, `ルール`, and `シナリオ`, and bulleted steps `前提`, `もし`, `ならば`, `かつ`, and `しかし`.
- In English repositories, use headings `Feature`, `Background`, `Rule`, and `Scenario`, and bulleted steps `Given`, `When`, `Then`, `And`, and `But`.
- Select the matching parser dialect, `ja` or `en`, when parsing. Check headings and steps after formatting; direct execution of feature files or installing Cucumber is not required.
- Keep assumptions and unagreed business decisions as questions. Agreement between AIs or a technical prototype does not establish stakeholder agreement.

### Assumptions and reassessment of important design decisions

When structural, external-contract, or operational choices significantly affect purpose/success conditions, document the effective constraints and operating conditions needed to implement them. Record selection reasons, comparisons, and the evidence behind a change in its PR/commit. Distinguish confirmed constraints from unresolved assumptions; do not invent unsupported numbers/deadlines.

For example, document which operations may be retried and the API's current idempotency window. Explain why retransmission was selected and which alternatives were rejected in the corresponding commit. If that contract changes, update the affected specification and record the new judgment in the change PR/commit. Assumption changes alone do not settle replacement approaches; confirm changes to purpose, outcomes, acceptance conditions, external impact, or authority before dependent implementation, preserving existing approval within the same scope.

Use policy links as supplementary navigation. A PR/commit must explain its judgment without requiring the reader to open those links. Without current specifications, follow “Choose authoritative sources and placement.” Do not require new/updated policy files or empty formal fields for spelling fixes preserving design choices.

### Checks

- Check requirements, constraints, recommendations, and unsettled matters are distinguishable, and necessary assumptions, terms, contracts, and examples reach readers. Do not turn example test frameworks or coverage goals into common requirements.
- Check acceptance conditions map to every requirement and document/test expectations agree. Unexecuted tests are not successful.
- Check duplicate/conflicting authoritative sources, links/reference versions, and preservation of existing OKF formats. Even ADR-only updates include these, final diff inspection, and [Markdown quality checks](validation.md) in validation plans. Distinguish executed results from unexecuted plans.
