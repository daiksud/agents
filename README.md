---
type: Guide
title: daiksud/agents
description: Prerequisites for shared Instructions and Skills, and installation through APM.
sources:
  - id: github-token-events
    resource: https://docs.github.com/en/actions/concepts/security/github_token
---

This repository shares [development policy Instructions](.apm/instructions/) and [task-specific Skills](skills/) through APM.

## Artifact language

These shared guidance files use English. Artifacts created with them follow [Repository artifact language](.apm/instructions/language.instructions.md): commits, code comments, and Issue/PR titles always use English; bodies, discussions, reviews, and documentation use the target repository's English or Japanese conventions.

## Maintainer references

[Maintainer references](docs/maintainer-references.md) collect source mappings, adoption decisions, research history, and supplementary notes for the Instructions and Skills, including the [Sakura Miko conversation sources](docs/sakuramiko-style-reference.md). Execution rules remain in Instructions and skill entry points; operational details stay in conditional skill references. Ordinary tasks do not require loading the maintainer notes.

## Prerequisites

The distribution targets are Codex and GitHub Copilot, as specified in [apm.yml](apm.yml). Use an environment with APM CLI available, and install the complete set of Instructions and Skills globally. Because Skills depend on one another, copying only an individual `SKILL.md` is not a supported usage assumption.

Under the [collaboration instructions](.apm/instructions/collaboration.instructions.md), code changes require a Navigator with an independent execution context. Before the first code edit, confirm actual initial and follow-up responses from the same Navigator. If unavailable, do not begin code edits, including test code or refactoring; read-only investigation and planning within the approved scope may continue. Pair work is not required for consultation, explanation, planning alone, or documentation-only changes.

## Installation

The shared instructions require [yomiyasu](https://github.com/nanaism/yomiyasu/tree/main/skills/yomiyasu) for refining Japanese prose. Make the skill available separately; it is not included as an APM dependency of this package.

```bash
apm install --global --target codex,copilot daiksud/agents
apm compile --global
```

## Instructions and GitHub protection settings

The checking procedures defined by Instructions and Skills are separate from protection conditions mechanically enforced by GitHub. Each repository manages its own Rulesets and required status checks; installing this package alone does not apply the same protection settings.

[github-repo](skills/github-repo/SKILL.md) diagnoses immutable releases, squash-only merges, the main Ruleset, full-SHA requirements for external Actions, and free security features for the specified repository, and applies only the explicitly requested scope. “Diagnose the settings” ends with a report, “record the plan in an Issue” ends with a record, and “apply the settings” includes applying the differences and diagnosing again. It coordinates workflow content changes with [github-actions](skills/github-actions/SKILL.md), and does not create empty commits or PRs solely for GitHub-side settings changes.

This repository requires `pass` for pull requests. [PR validation](.github/workflows/ci-pr.yml) follows `draft → commit-stage → ready → acceptance-stage → pass`: every run first attempts to convert the PR to Draft, runs approval-policy tests and Markdown lint, marks it Ready, and then checks local file links including frontmatter paths. Creation, new commits, reopening, and PR edits trigger validation. Each stage requires its predecessor to succeed; the final `pass` check rejects failed, cancelled, or skipped validation. There is no special handling for fork or Dependabot PRs: a denied state change fails the run instead of allowing validation to continue. [Main-push validation](.github/workflows/ci.yml) runs the same approval-policy tests and Markdown lint.

CI does not wait for reviews or merge PRs. This repository does not wait for CodeQL scans or results before merging PRs. Check the [Ruleset](https://github.com/daiksud/agents/rules/22615823) for the latest enforced conditions, and [Review and merge](skills/change-delivery/references/review-and-merge.md) for procedures from ordinary review through post-integration verification.

## Codex approval automation

[The approval workflow](.github/workflows/approve-codex-review.yml) runs when `chatgpt-codex-connector[bot]` creates or edits a Codex Review Summary comment on a PR. It fetches that comment again and approves when both the Code Review and Security Review rows show `Completed` and the same Codex account has a thumbs-up reaction on the PR body. Other users' reactions do not count.

If both reviews are complete but Codex's thumbs-up is missing, it retries every 30 seconds, up to six retries after the initial check: at most 180 seconds of waiting. Each retry rereads the Summary before checking reactions, stopping without approval if either review is no longer complete. A timeout exits normally. A failed API or approval request fails the run without withdrawing existing approvals.

Approval uses `gh pr review --approve`. The workflow does not compare reviewed commits with HEAD, check the eyes reaction, inspect review history, suppress duplicate approvals, or withdraw approvals. PR lifecycle and review-submission triggers and manual reconciliation are removed. After the polling window ends, another Summary creation or edit is needed to start a new check.

The approval workflow has no `workflow_call` entry point. CI owns its Draft/Ready operations directly in `ci-pr.yml`. Each PR has workflow-level concurrency with `cancel-in-progress: true`, without HEAD/base checks, coordination with approval, or recovery to Draft after a failure. Cancellation is not an atomic latest-HEAD guarantee. Failed acceptance leaves the PR Ready but the required `pass` check unsuccessful. CI contains no review-wait loop and does not merge PRs. GitHub suppresses most workflow events caused by `GITHUB_TOKEN`, so CI changes Draft/Ready directly rather than relying on a later Ready event.[^github-token-events]

This intentionally trades freshness guarantees for a smaller approval rule: an older completed Summary and existing thumbs-up may approve newer code or a new review cycle before Codex publishes updated status. Existing approvals are not withdrawn when conditions change. Elapsed time is never evidence of completion. Regression tests execute the production shell with fixture-backed `gh` and `sleep` boundaries; they do not prove live event delivery or token permissions.

[^github-token-events]: GitHub documents the workflow event suppression rules for repository `GITHUB_TOKEN` operations.

## Change records and Engineering Policies

[Change records](.apm/instructions/change-records.instructions.md) distinguish historical decisions in PR descriptions/commits from current durable guidance in [Engineering Policies](docs/engineering-policies/change-records.md). PRs report actual validation status; `Not run` is valid unless checks are independently required. Existing required CI and the repository's validation exclusions remain applicable.

The [reusable PR template](skills/change-delivery/assets/pull_request_template.md) and [self-adoption copy](.github/pull_request_template.md) are updated together. Use [repository adoption](skills/change-delivery/references/repository-adoption.md) and the [local instruction example](skills/change-delivery/assets/agents-change-records.md) to fill consumer gaps while accepting equivalent arrangements and honoring prior decisions. Adoption explicitly proposes English PR bodies for verbatim squash records and routes authorized message-setting work to `github-repo`. Installation only bundles assets; it does not copy a consumer template, adopt local rules, migrate ADRs, or change GitHub settings.
