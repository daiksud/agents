---
type: Instruction
title: Writing Issues and PRs
description: Define information retained in GitHub Issue and Pull Request titles and bodies, and their distinct roles.
---

## Writing Issues and PRs

Issues record desired states and completion conditions; Pull Requests record actual changes and validation. Do not duplicate the same template for both; future readers should trace “what changes/changed” and “why needed” from titles/bodies.

### Titles

Follow [Repository artifact language](../../../.apm/instructions/language.instructions.md): Issue/PR titles always use English and this Conventional Commits format; bodies and comments follow the target repository's English or Japanese conventions, with the explicit English PR-body adoption choice for verbatim squash records described in that language instruction.

```text
<type>[(scope)][!]: <description>
```

Conventional Commits 1.0.0 specifies commit messages. Applying it to Issue/PR titles is a local convention in this environment for shared vocabulary across work items, changes, and squash commits; the standard itself does not require Issue/PR titles.

- Use types such as `feat`, `fix`, `docs`, `refactor`, `test`, or `chore` appropriate to target commit conventions and change intent. Prioritize repository-specific permitted types.
- Add scope only when a short noun can express a stable domain, component, or responsibility. Do not add meaningless scope as filler.
- Write specific concise descriptions in English imperative form, identifying targets/changes without final periods. Do not use only unclear expressions such as “fix bug,” “update docs,” or “phase 1.”
- Use `!` only for types whose repository conventions permit breaking changes, and only when incompatibility is confirmed. This environment's default permits only `feat` or `fix`. Do not assume unverified breaking changes at the Issue stage.

### Common body principles

- Bodies alone should convey purpose, reasons, and important context. Links to Issues, design documents, or external material provide evidence/details; do not make reasons understandable only after following links.
- Prioritize target Issue Forms, Issue templates, or PR templates. If unspecified, choose appropriate structure without common requirements for fixed headings, empty sections, or “none” filler.
- Distinguish confirmed facts, plans, executed results, and uncertainties. Do not describe plans as executed changes/validation or infer unknown causes/effects.
- Short Issues/PRs may be short. Judge retained context for current decisions and future retrieval/understanding rather than volume.

### Issue bodies

Center Issues on “what state to achieve,” rather than “how it was implemented.”

- Show purpose, problems, and differences from the current state.
- Show success conditions judging completion and constraints to preserve.
- When implementation plans are settled, record scope, order, and validation. Do not infer unsettled methods, files, or designs and fix them as success conditions.
- For bugs, record reproduction conditions, expected results, and actual results as needed.
- State pending approval, unexecuted validation, dependencies, and other statuses affecting completion judgments.

### PR bodies

PRs record actual changes being reviewed.

- Record the problem or need, actual change and resulting behavior, and decisions needed to understand this change. Retain confirmed bug causes, constraints, relevant alternatives, and trade-offs when useful; do not invent analysis to fill sections.
- Follow [Change records](../../../.apm/instructions/change-records.instructions.md). Every actual description states validation status: checked scope and observed results, including failures/material limitations, or `Not run`. Execution is discretionary unless independently required. No justification, particular command, or post-merge plan is mandatory boilerplate. Clearly distinguish plans, including optional post-merge checks, from completed checks.
- Use the [reusable template](../../change-delivery/assets/pull_request_template.md) when no target template exists: Summary, Decisions, Validation. Equivalent existing headings are acceptable. Remove Decisions if unnecessary or if Summary already retains the reasoning; keep substantive validation status.
- Remove all HTML comments when creating or updating actual descriptions, including template instructions. Comments may remain in template files. An empty Validation section or one containing only instructions does not report status.
- Keep the judgment made at the time self-contained even when linking a living Engineering Policy. Current cross-cutting policy belongs in topical policy documents for repositories adopting that model; ordinary local decisions remain in the PR.
- Do not copy Issue bodies verbatim; let Issues explain goals and PRs explain actual diffs.
- If review changes content, reasons, validation results, or important constraints, update descriptions to current HEAD. Before merge, check the final description for accurate decisions/status and no HTML comments; preserve it with the title as the squash message using `PR_TITLE` / `PR_BODY` in `change-delivery`.

When a PR completely resolves an Issue, closing keywords such as `Closes #123`, `Fixes #123`, or `Resolves #123` may be used in PR bodies targeting the default branch. For partial resolution or remaining follow-up work, use ordinary references without automatic closure. On GitHub, merging linked PRs with closing keywords into the default branch automatically closes related Issues.
