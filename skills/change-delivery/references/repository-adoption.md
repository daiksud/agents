---
type: Guide
title: Adopt repository change records
description: Propose and record equivalent local PR records and Engineering Policies within authorized repository work.
---

## Inspect the repository before proposing adoption

At the start of repository change work, read the applicable local `AGENTS.md` and contributor instructions, effective PR template or templates, and current policy documents. Look for prior adoption decisions in local instructions, policies, and linked Issues/PRs. Judge the retained information and behavior, not identical filenames or headings.

An equivalent setup already records the problem and actual result, relevant decisions, and actual validation status; removes HTML comments from actual PR descriptions; keeps current durable guidance discoverable; and retains historical judgments in PRs/commits. Accept it and fill only confirmed gaps. Preserve existing adopted, partial, declined, or deferred decisions. Do not repeatedly ask the same question or block unrelated development on adoption; revisit only when new relevant evidence or a changed scope warrants it.

## Propose concrete local changes

When a gap matters to the authorized work, show the exact proposed paths and additions/edits, their purpose, and the existing conventions they preserve. Reuse these assets rather than creating another policy system:

- [Canonical PR template](../assets/pull_request_template.md): adapt its retained information to the repository's effective template, commonly `.github/pull_request_template.md`. Preserve useful existing fields and headings, including multiple-template arrangements.
- [Local instruction example](../assets/agents-change-records.md): adapt the fragment to the target repository's `AGENTS.md` or equivalent contributor guidance. Replace the example paths with actual local targets and remove the adaptation note.
- [Engineering Policies authoring](../../document-authoring/references/engineering-policies.md): use the existing authoring procedure for currently effective cross-cutting or future-guiding policy. Retain existing equivalent placement and ADR arrangements where appropriate; do not perform a blanket migration. Ordinary local changes need no policy document.

The proposal must explicitly choose the PR/squash language. For repositories adopting verbatim PR-body squash messages, propose English PR bodies so English commit subjects, bodies, and footers remain consistent. Preserve other artifact-language conventions, including Issue bodies, documentation, and review discussion. Surface conflicts with explicit local instructions and obtain a resolution before publishing affected artifacts; do not silently overwrite them or translate away rationale at merge time. This default is limited to adopting repositories, not every package consumer. See [Repository artifact language](../../../.apm/instructions/language.instructions.md).

Apply concrete file changes through ordinary change delivery when they are within already authorized scope. If adoption is outside scope or a decision is pending, present the proposal and continue unaffected work. Record the actual adoption, partial adoption, or deferral and its scope in existing repository-local instructions/policies or a linked Issue/PR so later work can honor it. Do not add a mandatory adoption checklist to every development task.

## Keep local rules self-contained

Contributors and external reviewers must be able to understand the repository's rules without an installed agents package. Link local templates and policy documents from local instructions and retain these requirements in the repository:

- Every PR reports actual validation status. Execution, method, scope, rigor, and timing are discretionary unless independently required. `Not run` is valid without boilerplate justification or a post-merge plan; distinguish completed, partial, failed, planned, and unperformed checks. Preserve required CI and agreed acceptance conditions.
- Templates may contain HTML authoring comments. Remove every HTML comment from actual descriptions at creation/update, and check again during review and before merge while retaining substantive status and decisions.
- Current durable policy explains applicability, rationale, relevant alternatives, and trade-offs in revisable topical documents, with the introducing/revising PR reference. PRs and commits retain self-contained historical judgments after living policies change.
- Keep the final PR title and description aligned with the reviewed change and preserve them as squash subject/body. Follow [Commit messages](conventional-commits.md) and [Review and merge](review-and-merge.md#rebase-and-merge).

Copy only the relevant local instruction fragment. Do not copy the distribution repository's entire root `AGENTS.md` or its repository-specific APM/independent-validation exclusions. A consumer retains its own validation decisions.

## Separate file adoption, installation, and settings

Bundling these assets in the APM package makes them available; installation does not create/update a consumer's `.github/pull_request_template.md`, agent instructions, policies, or GitHub settings. Adoption requires target-repository file changes. Do not add bootstrap, synchronization, or simulation machinery.

When settings diagnosis/application is in the requested scope, use [github-repo](../../github-repo/SKILL.md) and its [PR/squash message alignment](../../github-repo/references/settings.md#pr-and-squash-message-alignment) path to check `squash_merge_commit_title = PR_TITLE` and `squash_merge_commit_message = PR_BODY`. File adoption does not authorize live settings changes. Preserve other merge, CI, and protection settings. If settings remain unchanged or unverified, record that scope accurately; explicit merge messages can preserve the record under the existing delivery procedure without claiming defaults were changed.

## Review the proposed result

Use proportionate ordinary review and selected static Markdown, local-link, and asset checks. Review whether an equivalent setup is accepted, a missing template produces concrete local edits, a prior decision is honored, and conflicting explicit language rules are surfaced before affected publication. Check the consumer's local links and independence from the installed package. Report actual validation status; static inspection does not establish executed adoption or successful agent judgments, and no independent simulation framework is required.
