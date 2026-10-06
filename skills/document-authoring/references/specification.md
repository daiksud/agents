---
type: Guide
title: Clarifying specifications with existing documents
description: Show procedures for recording requirements, constraints, external contracts, and acceptance conditions in existing authoritative documents, clarifying uncertainties and validation mappings.
sources:
  - id: github-create-specification-skill-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/create-specification/SKILL.md
  - id: github-instructions-spec-driven-workflow-v1-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md
---

## Clarifying specifications with existing documents

Write specifications so people and agents understand the same expectations and verify achievement. Begin by checking actors, purpose, success conditions, readers, model boundaries, and existing agreed specifications, rather than creating an overall specification document.

Distinguish actors using systems from readers making decisions from specifications. State whether information serves API users, implementers, validators, or others; retain questions if readership is unconfirmed.

### Choose authoritative sources and placement

1. Find target glossaries, features, ADRs, API documents, schemas, and related tests; identify authoritative sources for current requirements/contracts. Retain conflicts with unknown precedence as questions to authorized people.
2. Record existing behavior in features, design choices/reasons in ADRs, and API/data contracts in existing API documents/schemas. Do not copy specifications into separate documents; provide authoritative links and necessary summaries.
3. Add documents to appropriate existing categories only where authoritative sources are missing. Shared behavior uses `docs/behavior/`, design decisions `docs/adr/`, and others follow document-authoring placement rules. Do not require `/spec/` or separate overall specifications for every change.
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
| Dependencies and reasons | Needed external capabilities/contracts, constraint evidence, and choice reasons. State technical choices when agreed constraints |
| Validation mappings | Trace corresponding tests/procedures and observed results. Use existing identifiers/stable headings when tracking from multiple locations is needed |
| Unsettled matters | Separate expectations from assumptions/proposals/questions, identifying whose decisions are needed. Do not invent unagreed thresholds or business failure handling |

Keep business-meaningful amounts, dates, and inputs in acceptance examples. Do not mix UI click sequences or internal-class construction into business rules; promised API-user/operator responses, saved results, and notifications are contracts.

Features follow Japanese Markdown with Gherkin in [Shared specification and format material](../../behavior-specification/references/behavior.md) in the dependency behavior-specification. Document creation alone does not require TDD execution. When code changes are requested, hand agreed specifications and unanswered questions to software-development's test-first implementation.

For example, with existing shipping features and quotation API OpenAPI, update features as authoritative for free-shipping conditions and OpenAPI for request/response formats, connecting corresponding tests. If whether subtotal is before or after discounts is unagreed, retain a question without creating an independent definition in a new overall specification.

### Assumptions and reassessment of important design decisions

When structural, external-contract, or operational choices significantly affect purpose/success conditions, record dependent assumptions and reconsideration conditions alongside reasons in existing ADRs. Attach confirmed evidence/specification references to assumptions, distinguishing unverified hypotheses. Connect reconsideration conditions to observations/changes showing assumptions failed; do not invent unsupported numbers/deadlines. Retain questions for unagreed necessary conditions.

For example, if retransmission is chosen because an external API guarantees idempotency for a period, reference guarantee evidence and make shortened guarantee periods or changed target operations reconsideration conditions. When met, compare original judgments and new evidence, preserving reasons to retain/change decisions under existing ADR history/succession conventions. Assumption changes alone do not settle replacement approaches; follow `issue-management` planning/approval for implementation scope or policy changes, handing only approved changes to `change-delivery`.

Put authoritative ADR links and decision-relevant summaries in Issues rather than duplicate decision records. Without authoritative documents, follow “Choose authoritative sources and placement.” Do not require new/updated ADRs or empty formal fields for spelling fixes preserving design choices.

### Checks

- Check requirements, constraints, recommendations, and unsettled matters are distinguishable, and necessary assumptions, terms, contracts, and examples reach readers.
- Check acceptance conditions map to every requirement and document/test expectations agree. Unexecuted tests are not successful.
- Check duplicate/conflicting authoritative sources, links/reference versions, and preservation of existing OKF formats. Even ADR-only updates include these, final diff inspection, and rumdl formatting/checking under document-authoring Markdown-quality procedures in validation plans. Distinguish executed results from unexecuted plans.

### Sources and application decisions

Checked GitHub awesome-copilot Create Specification[^github-create-specification-skill-md] on 2026-09-11, summarizing/restructuring explicit requirements, contracts, and acceptance conditions.

Prioritize existing OKF, features, and ADRs without adopting the source's `/spec/` placement, fixed filenames, all 11 sections, or custom frontmatter. Do not turn example test frameworks or coverage goals into common requirements. This is this environment's application decision, not a universal specification-format standard.

Checked GitHub awesome-copilot Spec Driven Workflow v1[^github-instructions-spec-driven-workflow-v1-instructions-md] on 2026-09-11, adopting preserved decision reasons and reconsideration conditions. Limit to important design decisions here, mapping assumptions to observations in existing ADRs. Do not adopt fixed templates for all decisions, fixed three documents, complete operation logs, or uniform six stages.

[^github-create-specification-skill-md]: [GitHub awesome-copilot Create Specification](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/create-specification/SKILL.md). Evidence for reference scope and adoption decisions stated in the text.
[^github-instructions-spec-driven-workflow-v1-instructions-md]: [GitHub awesome-copilot Spec Driven Workflow v1](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md). Evidence for reference scope and adoption decisions stated in the text.
