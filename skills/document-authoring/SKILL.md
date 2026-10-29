---
name: document-authoring
description: Use to create or update document artifacts such as READMEs, developer guides, Markdown, agent Instructions and Skills, specifications, features, ADRs, OpenAPI, and JSON Schema. Covers reader needs, content planning, drafting, editing, examples, maintenance, formats, sources, and Markdown quality. Use behavior-specification to discover acceptance conditions and examples without producing documents. Do not use solely to summarize existing documents or explain concepts.
---

# Author useful documents with OKF

Follow the dependency `issue-management` for Issue plans, publication permission, and Markdown quality when creating or updating documents, and `change-delivery` for approved repository changes and PR updates through public-main verification. `docs/` below refers to the working repository; `references/` refers to this skill's bundled resources.

## Application and reference material

- Follow [Repository artifact language](../../.apm/instructions/language.instructions.md) for repository documentation, including Markdown and feature documents. Determine the target repository's English or Japanese conventions before authoring.
- Author ordinary Markdown and feature documents in OKF v0.2. Preserve specific formats for GitHub Issue and PR bodies and comments, agent instruction files, Agent Skills `SKILL.md`, and contract documents such as OpenAPI and JSON Schema; do not add OKF frontmatter where the target format does not call for it.
- When creating or updating Instructions, Skills, or their task references, read [Separate execution guidance from maintainer notes](references/agent-documents.md). Keep execution rules at their entry points, load operational detail only when needed, and put provenance and maintenance-only supplements in human-facing `docs/` material.
- For reader-facing technical prose, including READMEs, guides, reference explanations, and contributor instructions, read [Developer documentation practices](references/technical-writing.md). Apply its reader, content-type, drafting, and editing guidance to the changed scope; spelling or metadata corrections do not require a new documentation plan or walkthrough.
- When creating or updating requirements, external contracts, acceptance conditions, design decisions, Engineering Policies, or ADRs, read [Clarifying specifications with existing documents](references/specification.md), first checking authoritative existing features, ADRs, and API specifications.
- When creating or revising current durable design policy in a repository adopting the change-record model, read [Engineering Policies](references/engineering-policies.md). Preserve existing ADR conventions elsewhere.
- When creating or updating OKF documents, read [Basic format and references](references/basic-format.md). Check exceptions for indexes/history and ordinary concepts, Bundle boundaries, and link resolution.
- For documents relying on external material, updates to sourced documents, or judgments about trust, freshness, or status, read [Provenance, trust, and lifecycle](references/provenance.md). Preserve existing sources, unknown metadata, and checking history even for minor corrections; when separating agent guidance, preserve its provenance in the maintainer note.
- When handling computation definitions or checking methods, read [Attested Computation](references/computation.md). Do not introduce computation contracts merely because a document contains numbers.

## Handoff according to the request

Read [Planning and execution scope](../issue-management/references/planning.md) for planning and approval, and [Issue records](../issue-management/references/issue-recording.md) for publication and save verification, before relevant operations. Before changing PR bodies or repository documents, separately check confirmed saving and execution approval; do not require recreating verified plans or obtaining the same approval again.

For unpublished information, confirm permission for only necessary parts and the posting destination and draft. Do not request the same publication permission again for published facts or saved and verified plans.

- For Issue planning alone, stop after `issue-management` saves, verifies, and presents it. Use that skill also for Issue-body or comment-only updates; `change-delivery` is unnecessary.
- For PR-body-only updates, use `issue-management` and `change-delivery` without expanding to repository editing or merging.
- For approved repository document changes, use [change-delivery](../change-delivery/SKILL.md) through public-main verification. Do not require code TDD for documents alone.

Without `issue-management`, do not begin Issue posting or document/PR changes; show drafts, unsaved plans, and missing dependencies. Without `change-delivery`, stop repository document and PR changes, but do not block Issue-body or comment-only updates. Preserve execution approval and saved plans even when dependencies are missing; do not substitute other Skills, and report incomplete scope and conditions for resumption.

## Creation and update process

1. Check readers, their existing knowledge, the task or decision the document supports, and observable success conditions. Use available evidence rather than inventing user research. Check authoritative sources, model boundaries, and existing terminology. Use `docs/` as the default Knowledge Bundle, and explicitly state the root when handling another distribution unit.
2. Determine whether the target is an ordinary concept, reserved file, or specific format. Read existing content and frontmatter before making diffs; do not drop unknown keys or sources through regeneration.
3. Use one concept per file for ordinary concepts, and include `type`. Also include the recommended `title` and `description` for concepts authored in this environment. Do not call this extra condition a mandatory OKF conformance requirement.
4. Choose the content type and outline around the reader's task, then draft and edit using [Developer documentation practices](references/technical-writing.md). Apply only relevant techniques to specialized formats and preserve their contracts. Reuse the existing plan and document structure where they fit.
5. Record `sources` and stable-ID claim footnotes in externally grounded human-facing documents. For agent execution guidance, preserve that mapping in maintainer notes under [Agent-document separation](references/agent-documents.md). Keep operational lookup links and required attribution where needed. Do not substitute navigation links for evidence or remove citations required in the resulting user artifact.
6. Determine whether changes are meaningful or only spelling/formatting, and update only actual confirmed generation/checking facts. Do not invent dates, human checks, or expiration dates, or claim old checks verify updated content.
7. Perform [Document quality checks](references/validation.md), separately reporting Markdown results, content checking, warnings for unverified or expired items, and checks that cannot run.

## Placement and content

- Add documents to existing categories appropriate to their purpose: current durable design policy in `docs/engineering-policies/` for repositories adopting that model (retain existing ADR conventions elsewhere), behavior in `docs/behavior/`, and others in `docs/<category>/<page-name>.md`. General guidance may be placed in `docs/<page-name>.md`.
- Create new categories only when existing ones do not fit. Do not uniformly add indexes or history files to every directory.
- Write `*.feature.md` with OKF frontmatter and Markdown with Gherkin from [Shared specification and format material](../behavior-specification/references/behavior.md) in the dependency `behavior-specification`.
- Link bundled material through file-relative links for viewing on GitHub and through APM. Record external sources as complete URLs, without assuming the original repository exists at the installation destination.
- Do not use external assets such as images that cannot be included in Markdown. This is this environment's authoring policy, not an OKF conformance condition.
- Use headings, lists, tables, and code blocks to show structure needed for decisions. Do not create empty sections or decorative tables.

## Document quality checks

Before publication, read [Markdown and content checks](references/validation.md), and format/check with rumdl. Validate specific formats such as OpenAPI and JSON Schema according to each format.

Do not turn successful format checks into evidence of source truth, human content review, or executed computations. Also compare categories, terminology, links, commands, final diffs, and content, and distinguish unverified, expired, and unexecutable items.
