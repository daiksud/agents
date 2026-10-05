---
name: behavior-specification
description: Use to discover and specify user-facing behavior, domain rules, external contracts, and acceptance conditions, including specification work without code. Do not use for internal technical fixes that preserve agreed contracts or design limited to implementation methods.
---

# Discover and specify behavior

Organize results promised to users or external systems before deciding how to implement them. `docs/` below refers to the working repository.

## From purpose to acceptance conditions

1. Check existing stories, glossaries, features, API specifications, and agreed rules, and reuse authoritative sources. For new features, describe who can do what, in which situation, after completion. Connect technical fixes and cleanup to existing purposes and expected results.
2. Read [Shared understanding and feature documents](references/behavior.md), and separate rules, meaningful concrete examples, and unanswered questions using BDD, ATDD, and Example Mapping perspectives. Do not settle unagreed business decisions through agreement between AIs or technical prototypes.
3. Define acceptance conditions before the corresponding implementation, and show which normal, boundary, or failure results should be observed. Do not mix internal implementation procedures into business specifications; preserve externally promised responses, saved results, and notifications as contracts.
4. For domain-rule additions or changes, save `docs/behavior/<feature-name>.feature.md` before implementation, even for agreed rules. Do not unnecessarily rewrite correct existing specifications. For external technical contracts, prioritize existing authoritative API specifications or similar sources; when a shared specification is needed, features may be used with explicit readers and observable results.

When saving documents, also use the dependency `document-authoring`; features follow the Japanese Markdown with Gherkin in [Shared specification format](references/behavior.md#feature-document-format). Read [Primary sources](references/sources.md) when checking definitions, sources, or adoption reasons. Do not uniformly require meetings, participant counts, or automation tools.

## Handoff and completion

- For specification-only requests without code changes, present stories, concrete examples, acceptance conditions, and unanswered questions, then stop. Do not implicitly start Issue creation, publication, or TDD.
- When asked to create or update an Issue plan, use `issue-management` for publication permission, execution scope, and post-save checks. For planning-only requests, do not require installation of `change-delivery` or `document-authoring`; stop after saving and retrieving the Issue plan, checking its body and display, and presenting its URL, without saving documents or implementing.
- For approved feature documents in the repository, use `document-authoring` and `change-delivery`, without recreating saved Issue plans or approval, and proceed through post-integration main verification. In Plan Mode or read-only environments, present drafts without claiming saving or implementation occurred.
- If `issue-management` is unavailable, do not post to Issues or substitute another Skill; show the unsaved draft and restrictions. If `change-delivery` is unavailable, do not save documents or substitute another Skill; show incomplete scope. If `document-authoring` is unavailable, do not save documents; show required formats and dependencies.
- When code changes are requested, hand agreed specifications, concrete examples, unanswered questions, and their mapping to tests to the dependency [software-development](../software-development/SKILL.md). Saving specifications alone does not approve implementation. Retain existing implementation approval without asking for the same approval again.
