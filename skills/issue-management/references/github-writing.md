---
type: Instruction
title: Writing Issues and PRs
description: Define information retained in GitHub Issue and Pull Request titles and bodies, and their distinct roles.
sources:
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: github-issue-quickstart
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart
  - id: github-review-changes
    resource: https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes
  - id: github-link-pr-issue
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
  - id: google-cl-descriptions
    resource: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
---

## Writing Issues and PRs

Issues record desired states and completion conditions; Pull Requests record actual changes and validation. Do not duplicate the same template for both; future readers should trace “what changes/changed” and “why needed” from titles/bodies. GitHub recommends immediately understandable titles and purpose/resolution information for Issues, and context explaining problems, approaches, and results for PRs. Google's change-description guide also emphasizes preserving changes/reasons in future history.[^github-issue-quickstart] [^github-review-changes] [^google-cl-descriptions]

### Titles

Follow [Repository artifact language](../../../.apm/instructions/language.instructions.md): Issue/PR titles always use English and this Conventional Commits format; bodies and comments follow the target repository's English or Japanese conventions.

```text
<type>[(scope)][!]: <description>
```

Conventional Commits 1.0.0 specifies commit messages. Applying it to Issue/PR titles is a local convention in this environment for shared vocabulary across work items, changes, and squash commits; the standard itself does not require Issue/PR titles.[^conventional-commits]

- Use types such as `feat`, `fix`, `docs`, `refactor`, `test`, or `chore` appropriate to target commit conventions and change intent. Prioritize repository-specific permitted types.
- Add scope only when a short noun can express a stable domain, component, or responsibility. Do not add meaningless scope as filler.
- Write specific concise descriptions in English imperative form, identifying targets/changes without final periods. Do not use only unclear expressions such as “fix bug,” “update docs,” or “phase 1.”[^google-cl-descriptions]
- Use `!` only for types whose repository conventions permit breaking changes, and only when incompatibility is confirmed. This environment's default permits only `feat` or `fix`. Do not assume unverified breaking changes at the Issue stage.

### Common body principles

- Bodies alone should convey purpose, reasons, and important context. Links to Issues, design documents, or external material provide evidence/details; do not make reasons understandable only after following links.[^google-cl-descriptions]
- Prioritize target Issue Forms, Issue templates, or PR templates. If unspecified, choose appropriate structure without common requirements for fixed headings, empty sections, or “none” filler.
- Distinguish confirmed facts, plans, executed results, and uncertainties. Do not describe plans as executed changes/validation or infer unknown causes/effects.
- Short Issues/PRs may be short. Judge retained context for current decisions and future retrieval/understanding rather than volume.

### Issue bodies

Center Issues on “what state to achieve,” rather than “how it was implemented.” GitHub likewise asks for purpose and helpful resolution information, including reproduction, expected results, and actual results for bugs.[^github-issue-quickstart]

- Show purpose, problems, and differences from the current state.
- Show success conditions judging completion and constraints to preserve.
- When implementation plans are settled, record scope, order, and validation. Do not infer unsettled methods, files, or designs and fix them as success conditions.
- For bugs, record reproduction conditions, expected results, and actual results as needed.
- State pending approval, unexecuted validation, dependencies, and other statuses affecting completion judgments.

### PR bodies

PRs record actual changes being reviewed. GitHub recommends clear titles/descriptions explaining problems, approaches, results, and points needing review attention.[^github-review-changes]

- Write what changed and why it was necessary.
- Show executed validation/results, separating unverified scope.
- Include important constraints, known limits, intentional exclusions, or particular review focus only when needed for decisions.
- Do not copy Issue bodies verbatim; let Issues explain goals and PRs explain actual diffs.
- If review changes content, reasons, validation results, or important constraints, update descriptions to current HEAD.

When a PR completely resolves an Issue, closing keywords such as `Closes #123`, `Fixes #123`, or `Resolves #123` may be used in PR bodies targeting the default branch. For partial resolution or remaining follow-up work, use ordinary references without automatic closure. On GitHub, merging linked PRs with closing keywords into the default branch automatically closes related Issues.[^github-link-pr-issue]

### Sources and application decisions

Use Conventional Commits syntax, types, scopes, and breaking-change notation as the title-format basis; applying them to Issues/PRs is this environment's convention. Adopt purpose-expressive titles, resolution/review context, problem/approach/result explanations, and Issue linking from GitHub guides. Adopt preserving changes/reasons in future history and retaining needed body context beyond short summaries from Google Engineering Practices. Do not introduce fixed templates, mandatory body lengths, or identical headings for every Issue/PR.

[^github-issue-quickstart]: GitHub Docs, “Quickstart for GitHub Issues.” Descriptive Issue titles, purpose, and bug reproduction/expected/actual result examples.
[^github-review-changes]: GitHub Docs, “Helping others review your changes.” Guidance on small clear PRs and context about problems, approaches, results, and review needs.
[^google-cl-descriptions]: Google Engineering Practices, “Writing good CL descriptions.” Guidance on preserving changes/reasons in future history, with short summaries and needed context.
[^conventional-commits]: Conventional Commits 1.0.0. Commit syntax, types, scopes, and breaking-change specifications.
[^github-link-pr-issue]: GitHub Docs, “Linking a pull request to an issue.” Issue links through closing keywords and automatic closure on default-branch merge.
