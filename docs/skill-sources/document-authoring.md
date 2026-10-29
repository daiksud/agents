---
type: Reference
title: Sources and adoption notes for document authoring
description: Preserve source mappings and editorial decisions behind document-authoring guidance without requiring them during ordinary authoring.
sources:
- id: okf-spec
  resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
  title: Open Knowledge Format v0.2
- id: rumdl-md025
  resource: https://github.com/rvben/rumdl/blob/993b5b10feca512e07d017ba4550fe690cd08c51/docs/md025.md
- id: sample-attester
  resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/bundles/acme_retail/attesters/sql_equality.py
  title: Reference SQL attester
- id: github-create-specification-skill-md
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/create-specification/SKILL.md
- id: github-instructions-spec-driven-workflow-v1-instructions-md
  resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md
- id: docs-for-developers-contents
  resource: https://docsfordevelopers.com/table-of-contents/
  title: Docs for Developers detailed contents
- id: docs-for-developers-audience
  resource: https://link.springer.com/chapter/10.1007/978-1-4842-7217-6_1
  title: Understanding your audience, chapter overview
- id: docs-for-developers-planning
  resource: https://link.springer.com/chapter/10.1007/978-1-4842-7217-6_2
  title: Planning your documentation, chapter overview
- id: docs-for-developers-translator
  resource: https://speakerdeck.com/iwashi86/docs-for-developers
  title: Yoshimasa Iwase, Docs for Developers presentation
- id: docs-for-developers-publisher
  resource: https://link.springer.com/book/10.1007/978-1-4842-7217-6
  title: Docs for Developers, first edition publisher overview
- id: change-record-agreement
  resource: https://github.com/daiksud/agents/issues/253
---

## Purpose and scope

These are maintainer notes for [document-authoring](../../skills/document-authoring/SKILL.md). Runtime procedures remain in the skill and its conditional references. The dates and source observations below are retained research history; reorganizing them does not constitute a new source check.

The [OKF specification audit](../okf-specification-audit.md) preserves the detailed section mapping, upstream revisions, and reference-implementation observations.

## Source-to-guidance mapping

| Runtime document | Sources |
| --- | --- |
| [OKF basic format and references](../../skills/document-authoring/references/basic-format.md) | [^okf-spec] |
| [OKF provenance, trust, and lifecycle](../../skills/document-authoring/references/provenance.md) | [^okf-spec] |
| [Attested Computation contracts and verification](../../skills/document-authoring/references/computation.md) | [^okf-spec], [^rumdl-md025], [^sample-attester] |
| [Clarifying specifications with existing documents](../../skills/document-authoring/references/specification.md) | [^github-create-specification-skill-md], [^github-instructions-spec-driven-workflow-v1-instructions-md] |
| [Developer documentation practices](../../skills/document-authoring/references/technical-writing.md) | [^docs-for-developers-contents], [^docs-for-developers-audience], [^docs-for-developers-planning], [^docs-for-developers-translator], [^docs-for-developers-publisher] |

## Original annotation scope

### OKF basic format and references

- `okf-spec`: Fixed SPEC §§2–4, 6, 8–9, 11–12. This environment's additional conditions are distinguished in the text.

### OKF provenance, trust, and lifecycle

- `okf-spec`: Fixed SPEC §§4.1, 5, 7, 11, 13. This environment's update procedures and additional checks are application decisions.

### Attested Computation contracts and verification

- `okf-spec`: Pinned SPEC §§10–12. §10.5 is informative; operational verification items are local application decisions.
- `rumdl-md025`: rumdl 0.2.69, MD025 Front Matter Integration and Configuration examples.
- `sample-attester`: Findings from reading the fixed-SHA sample's docstring, `attest`, and `_canonicalize`, not measurements of effectiveness on an execution platform.

### Clarifying specifications with existing documents

- `github-create-specification-skill-md`: [GitHub awesome-copilot Create Specification](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/create-specification/SKILL.md). Evidence for reference scope and adoption decisions stated in the text.
- `github-instructions-spec-driven-workflow-v1-instructions-md`: [GitHub awesome-copilot Spec Driven Workflow v1](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md). Evidence for reference scope and adoption decisions stated in the text.

### Developer documentation practices

- `docs-for-developers-audience`: Publisher's chapter 1 overview. Supports research, support feedback, firsthand use, and friction logs for understanding readers.
- `docs-for-developers-planning`: Publisher's chapter 2 overview. Supports choosing needed content and content types before writing.
- `docs-for-developers-contents`: Authors' detailed first-edition contents, chapters 2–6 and 8–11. Establishes covered topics, not detailed rules from unaccessed chapters.
- `docs-for-developers-translator`: Yoshimasa Iwase's 2023-03-17 presentation, sections on chapters 1, 3, 8, and 9. Translator's public explanation, distinguished from the book text and the later Japanese-writing supplement.
- `docs-for-developers-publisher`: Apress first-edition overview. Supports documentation across the software lifecycle, feedback, measurement, organization, and maintenance alongside releases.

## Reference attester observations

The bundled `sql_equality.py` sample uses no network. It checks normalized SQL equality and agreement between results in the receipt and displayed values. It trusts the executor for parameter-value checks and does not retrieve authoritative results again from the job ID. Normalizing comments, whitespace, and words is not complete SQL parsing; no guarantee of preserving meanings such as string literals can be inferred.[^sample-attester]

## Specification-authoring adoption

Checked GitHub awesome-copilot Create Specification[^github-create-specification-skill-md] on 2026-09-11, summarizing/restructuring explicit requirements, contracts, and acceptance conditions.

Prioritize existing OKF, features, and ADRs without adopting the source's `/spec/` placement, fixed filenames, all 11 sections, or custom frontmatter. Do not turn example test frameworks or coverage goals into common requirements. This is this environment's application decision, not a universal specification-format standard.

Checked GitHub awesome-copilot Spec Driven Workflow v1[^github-instructions-spec-driven-workflow-v1-instructions-md] on 2026-09-11, adopting preserved decision reasons and reconsideration conditions. Limit to important design decisions here, mapping assumptions to observations in existing ADRs. Under the later change-record policy, adopting repositories instead maintain current topical Engineering Policies and retain historical judgments in PRs/commits. Do not adopt fixed templates for all decisions, fixed three documents, complete operation logs, or uniform six stages.

## Developer-documentation adoption

Consulted the public materials below on 2026-10-21. The full book was not available in this work. Chapter topics and public explanations support the principles; the content-type completion criteria, example-verification rules, outline, friction-log fields, and integration with existing skills are this repository's adaptations. Do not attribute those details as verbatim book instructions or treat the contents page as evidence for unseen chapter text.

Use this guide for developer-documentation technique, [basic format](../../skills/document-authoring/references/basic-format.md) for OKF, [provenance](../../skills/document-authoring/references/provenance.md) for claims and sources, and `yomiyasu` for Japanese refinement. GitHub-post conventions and delivery remain with their existing skills. The translator labels additional Japanese-writing material separately from the book overview; that material is not imported here. No second-edition AI-specific technique is asserted from a publisher blurb.

### Public-material observations

The audience chapter describes using research, support issues, and firsthand product use to understand readers, including recording friction encountered while using the product.[^docs-for-developers-audience]

The translator's overview connects audience, goal, and document type to a goal-based title, an outline, and a structure that supports scanning.[^docs-for-developers-translator]

The publisher describes publishing and maintaining docs alongside code releases, using feedback and analysis to assess effectiveness, and organizing information so readers can find it.[^docs-for-developers-publisher]

The public contents identify comments, READMEs, introductory, conceptual, procedural, reference, code-sample, and visual-content topics.[^docs-for-developers-contents] The translator distinguishes task completion from expression and structural quality.[^docs-for-developers-translator]

[^okf-spec]: [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md). See the per-document mapping above for the original evidence scope.
[^rumdl-md025]: [rumdl-md025](https://github.com/rvben/rumdl/blob/993b5b10feca512e07d017ba4550fe690cd08c51/docs/md025.md). See the per-document mapping above for the original evidence scope.
[^sample-attester]: [Reference SQL attester](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/bundles/acme_retail/attesters/sql_equality.py). See the per-document mapping above for the original evidence scope.
[^github-create-specification-skill-md]: [github-create-specification-skill-md](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/create-specification/SKILL.md). See the per-document mapping above for the original evidence scope.
[^github-instructions-spec-driven-workflow-v1-instructions-md]: [github-instructions-spec-driven-workflow-v1-instructions-md](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md). See the per-document mapping above for the original evidence scope.
[^docs-for-developers-contents]: [Docs for Developers detailed contents](https://docsfordevelopers.com/table-of-contents/). See the per-document mapping above for the original evidence scope.
[^docs-for-developers-audience]: [Understanding your audience, chapter overview](https://link.springer.com/chapter/10.1007/978-1-4842-7217-6_1). See the per-document mapping above for the original evidence scope.
[^docs-for-developers-planning]: [Planning your documentation, chapter overview](https://link.springer.com/chapter/10.1007/978-1-4842-7217-6_2). See the per-document mapping above for the original evidence scope.
[^docs-for-developers-translator]: [Yoshimasa Iwase, Docs for Developers presentation](https://speakerdeck.com/iwashi86/docs-for-developers). See the per-document mapping above for the original evidence scope.
[^docs-for-developers-publisher]: [Docs for Developers, first edition publisher overview](https://link.springer.com/book/10.1007/978-1-4842-7217-6). See the per-document mapping above for the original evidence scope.

## Change-record policy adoption

[Policy authoring](../../skills/document-authoring/references/engineering-policies.md) and specification placement apply the agreement in [Issue #253](https://github.com/daiksud/agents/issues/253).[^change-record-agreement] The current rationale and boundaries live in [Change records policy](../engineering-policies/change-records.md): actual validation reporting is required while execution is discretionary unless independently required; PRs/commits retain historical judgment and topical policies retain current guidance. This adoption does not establish renewed checking of the external sources above.

[^change-record-agreement]: Owner-agreed change-record policy and implementation scope in Issue #253.
