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

## Prerequisites

The distribution targets are Codex and GitHub Copilot, as specified in [apm.yml](apm.yml). Use an environment with APM CLI available, and install the complete set of Instructions and Skills globally. Because Skills depend on one another, copying only an individual `SKILL.md` is not a supported usage assumption.

Under the [collaboration instructions](.apm/instructions/collaboration.instructions.md), code changes require a Navigator with an independent execution context. Before the first code edit, confirm actual initial and follow-up responses from the same Navigator. If unavailable, do not begin code edits, including test code or refactoring; read-only investigation and planning within the approved scope may continue. Pair work is not required for consultation, explanation, planning alone, or documentation-only changes.

## Installation

```bash
apm install --global --target codex,copilot daiksud/agents
apm compile --global
```

## Instructions and GitHub protection settings

The checking procedures defined by Instructions and Skills are separate from protection conditions mechanically enforced by GitHub. Each repository manages its own Rulesets and required status checks; installing this package alone does not apply the same protection settings.

[github-repo](skills/github-repo/SKILL.md) diagnoses immutable releases, squash-only merges, the main Ruleset, full-SHA requirements for external Actions, and free security features for the specified repository, and applies only the explicitly requested scope. “Diagnose the settings” ends with a report, “record the plan in an Issue” ends with a record, and “apply the settings” includes applying the differences and diagnosing again. It coordinates workflow content changes with [github-actions](skills/github-actions/SKILL.md), and does not create empty commits or PRs solely for GitHub-side settings changes.

This repository requires `ci`. [PR validation](.github/workflows/ci-pr.yml) follows `draft → commit-stage → ready → acceptance-stage → check`: eligible same-repository PRs return to Draft for approval-policy tests and Markdown lint, become Ready after that succeeds on the current HEAD and base branch, and then undergo local file-link validation including frontmatter paths. Creation, new commits, reopening, and PR edits trigger validation, including base-branch changes. Fork and Dependabot PRs receive validation without state changes. [Main-push validation](.github/workflows/ci.yml) runs the same approval-policy tests and Markdown lint.

CI does not wait for reviews or merge PRs. This repository does not wait for CodeQL scans or results before merging PRs. Check the [Ruleset](https://github.com/daiksud/agents/rules/22615823) for the latest enforced conditions, and [Review and merge](skills/change-delivery/references/review-and-merge.md) for procedures from ordinary review through post-integration verification.

## Codex approval automation

[The approval workflow](.github/workflows/approve-codex-review.yml) runs when `chatgpt-codex-connector[bot]` creates or edits a Codex Review Summary comment on a PR. It fetches that comment again and approves when both the Code Review and Security Review rows show `Completed` and the same Codex account has a thumbs-up reaction on the PR body. Other users' reactions do not count.

If both reviews are complete but Codex's thumbs-up is missing, it retries every 30 seconds, up to six retries after the initial check: at most 180 seconds of waiting. Each retry rereads the Summary before checking reactions, stopping without approval if either review is no longer complete. A timeout exits normally. A failed API or approval request fails the run without withdrawing existing approvals.

Approval uses `gh pr review --approve`. The workflow does not compare reviewed commits with HEAD, check the eyes reaction, inspect review history, suppress duplicate approvals, or withdraw approvals. PR lifecycle and review-submission triggers and manual reconciliation are removed. After the polling window ends, another Summary creation or edit is needed to start a new check.

The reusable `workflow_call` and `controlled-ci` job remain for CI's Draft/Ready operations, including their existing HEAD/base and mutation-eligibility checks. Those checks do not participate in approval decisions. CI contains no review-wait loop and does not merge PRs. GitHub suppresses most workflow events caused by `GITHUB_TOKEN`, so CI changes Draft/Ready directly rather than relying on a later Ready event.[^github-token-events]

This intentionally trades freshness guarantees for a smaller approval rule: an older completed Summary and existing thumbs-up may approve newer code or a new review cycle before Codex publishes updated status. Existing approvals are not withdrawn when conditions change. Elapsed time is never evidence of completion. Regression tests execute the production shell with fixture-backed `gh` and `sleep` boundaries; they do not prove live event delivery or token permissions.

[^github-token-events]: GitHub documents the workflow event suppression rules for repository `GITHUB_TOKEN` operations.
