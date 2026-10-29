---
type: Reference
title: Change delivery sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the change-delivery skill.
sources:
  - id: continuousdelivery-foundations-continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: github-src-index-ts
    resource: https://github.com/conventional-changelog/commitlint/blob/f4b108182e6d20eca52433135c7ba1675746318e/%40commitlint/config-conventional/src/index.ts#L24-L36
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: commit-message-storyteller
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/commit-message-storyteller/SKILL.md
  - id: conventional-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/conventional-commit/SKILL.md
  - id: git-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/git-commit/SKILL.md
  - id: gh-pr-edit
    resource: https://cli.github.com/manual/gh_pr_edit
  - id: github-rest-review-requests
    resource: https://docs.github.com/en/rest/pulls/review-requests#request-reviewers-for-a-pull-request
  - id: docs-request-a-code-review-use-code-review
    resource: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review
  - id: github-graphql-pulls
    resource: https://docs.github.com/en/graphql/reference/pulls
  - id: github-installed-apps
    resource: https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps
  - id: github-app-installation-api
    resource: https://docs.github.com/en/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app
  - id: github-app-user-installations
    resource: https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token
  - id: codex-github-review
    resource: https://developers.openai.com/codex/integrations/github
  - id: codex-github-review-current
    resource: https://learn.chatgpt.com/docs/third-party/github
  - id: github-app-user-access
    resource: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
  - id: ruleset-rules
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: code-owners
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  - id: approval-code-owner-exception
    resource: https://github.com/daiksud/agents/issues/165
  - id: copilot-work-started-observation
    resource: https://github.com/daiksud/agents/pull/166
---

## Scope

Maintainer reference for [change-delivery](../../skills/change-delivery/SKILL.md). These records explain source provenance and adoption history. Execution procedures and decision-relevant details remain in the skill and its task-specific references; ordinary execution does not require this document.

The checking records below are retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Source mapping

The following mapping preserves the original source IDs and annotation scope for each runtime document.

### Branches and integration units

Runtime material: [branches.md](../../skills/change-delivery/references/branches.md).

| Source | Original annotation scope |
| --- | --- |
| [^continuousdelivery-foundations-continuous-integration] | [CI principles](https://continuousdelivery.com/foundations/continuous-integration/). Evidence for the reference scope and adoption decisions stated in the text. |
| [^github-src-index-ts] | [@commitlint/config-conventional type definitions](https://github.com/conventional-changelog/commitlint/blob/f4b108182e6d20eca52433135c7ba1675746318e/%40commitlint/config-conventional/src/index.ts#L24-L36). Evidence for the reference scope and adoption decisions stated in the text. |

### Commit messages

Runtime material: [conventional-commits.md](../../skills/change-delivery/references/conventional-commits.md).

| Source | Original annotation scope |
| --- | --- |
| [^git-commit] | Git Commit. Adopt actual-diff/purpose-based units and hook-failure handling, applying staging examples under existing change protection. |
| [^commit-message-storyteller] | Commit Message Storyteller. Adopt purpose/background/impact and subject writing, without guessing unverified background or fixed output formats. |
| [^conventional-commits] | Conventional Commits 1.0.0. Standard syntax, types, scopes, bodies, footers, and breaking changes. |
| [^conventional-commit] | Conventional Commit. Adopt diff/message agreement and structure, without XML or automatic execution from drafts. |

### Review and merge

Runtime material: [review-and-merge.md](../../skills/change-delivery/references/review-and-merge.md).

| Source | Original annotation scope |
| --- | --- |
| [^docs-request-a-code-review-use-code-review] | [Copilot Code Review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review). Evidence for reference scope and adoption decisions stated in the text. |
| [^codex-github-review] | [Codex GitHub review](https://developers.openai.com/codex/integrations/github). Evidence for review configuration, requests, result checks, and installation alone not establishing completion. |
| [^github-graphql-pulls] | [GitHub GraphQL Pull requests](https://docs.github.com/en/graphql/reference/pulls). Evidence for PR reviewer-candidate fields/arguments. |
| [^github-installed-apps] | [Checking installed GitHub Apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps). Checking installed Apps and repository access. |
| [^github-app-user-access] | [GitHub App user access token scope](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app). Evidence for access limited by both App/user and same-task successful operations used in candidate assessment. |
| [^github-app-installation-api] | [Repository installation API](https://docs.github.com/en/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app). Authentication requires the checked App's own JWT. |
| [^github-app-user-installations] | [Installations accessible to user access tokens](https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token). Installation scope limited to the authenticated GitHub App. |
| [^ruleset-rules] | [Available Ruleset rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets). Required approval counts and Code Owner requirements. |
| [^code-owners] | [About Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). CODEOWNERS application and approval with multiple owners. |
| [^approval-code-owner-exception] | Effective approval conditions adopted in Issue #165 when the sole Code Owner is the PR author. |
| [^gh-pr-edit] | [GitHub CLI: gh pr edit](https://cli.github.com/manual/gh_pr_edit). Evidence for ordinary requests with `--add-reviewer "@copilot"`. |
| [^github-rest-review-requests] | [REST API: Request reviewers](https://docs.github.com/en/rest/pulls/review-requests#request-reviewers-for-a-pull-request). Formal API path used when needed. |

## Conventional commits adoption notes

Checked fixed versions of three GitHub awesome-copilot resources, summarizing/restructuring commit-message-storyteller's purpose/reason writing guidance,[^commit-message-storyteller] conventional-commit's diff checks/structure,[^conventional-commit] and git-commit's purpose-based units and failure handling.[^git-commit]

Integrate with existing approval/change protection in this environment. Do not adopt fixed XML, unconditional commits after drafting, repeated “Story told” explanations, or removal of all footers without Issues. 72 characters guides readability; no uniform body-length limit is established.

## Copilot execution observation

The original [review procedure](../../skills/change-delivery/references/review-and-merge.md#checking-execution-after-copilot-requests) recorded that PR #166 emitted `copilot_work_started` while `requested_reviewers=[]` and reviews were absent, followed by normal completion.[^copilot-work-started-observation] This historical observation is not a permanent public API contract or evidence of a current review's state. The execution procedure retains the need to correlate the event with a request for the current, unchanged HEAD.

## Codex Ready-state policy

The requester selected Ready-only Codex review requests, including retries, for this workflow. The current official GitHub integration documentation describes the `@codex review` comment trigger but does not state a Draft/Ready prerequisite.[^codex-github-review-current] The [Alternative review procedure](../../skills/change-delivery/references/review-and-merge.md#alternative-review) therefore records Ready as an operating policy, without asserting that Codex universally rejects draft PRs. This service-specific prerequisite leaves the shared 10-minute retry policy product-independent and preserves the separate CI, review, approval, and merge conditions.

[^continuousdelivery-foundations-continuous-integration]: [continuousdelivery-foundations-continuous-integration](https://continuousdelivery.com/foundations/continuous-integration/).
[^github-src-index-ts]: [github-src-index-ts](https://github.com/conventional-changelog/commitlint/blob/f4b108182e6d20eca52433135c7ba1675746318e/%40commitlint/config-conventional/src/index.ts#L24-L36).
[^git-commit]: [git-commit](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/git-commit/SKILL.md).
[^commit-message-storyteller]: [commit-message-storyteller](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/commit-message-storyteller/SKILL.md).
[^conventional-commits]: [conventional-commits](https://www.conventionalcommits.org/en/v1.0.0/).
[^conventional-commit]: [conventional-commit](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/conventional-commit/SKILL.md).
[^docs-request-a-code-review-use-code-review]: [docs-request-a-code-review-use-code-review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review).
[^codex-github-review]: [codex-github-review](https://developers.openai.com/codex/integrations/github).
[^github-graphql-pulls]: [github-graphql-pulls](https://docs.github.com/en/graphql/reference/pulls).
[^github-installed-apps]: [github-installed-apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).
[^github-app-user-access]: [github-app-user-access](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app).
[^github-app-installation-api]: [github-app-installation-api](https://docs.github.com/en/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app).
[^github-app-user-installations]: [github-app-user-installations](https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token).
[^ruleset-rules]: [ruleset-rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
[^code-owners]: [code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
[^approval-code-owner-exception]: [approval-code-owner-exception](https://github.com/daiksud/agents/issues/165).
[^gh-pr-edit]: [gh-pr-edit](https://cli.github.com/manual/gh_pr_edit).
[^github-rest-review-requests]: [github-rest-review-requests](https://docs.github.com/en/rest/pulls/review-requests#request-reviewers-for-a-pull-request).
[^copilot-work-started-observation]: [copilot-work-started-observation](https://github.com/daiksud/agents/pull/166).
[^codex-github-review-current]: [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github). Current request instructions checked for the Ready-state policy; no Draft/Ready prerequisite was stated.
