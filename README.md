---
type: Guide
title: daiksud/agents
description: Installation and use of shared Skills through APM.
sources:
  - id: github-token-events
    resource: https://docs.github.com/en/actions/concepts/security/github_token
---

This repository shares task-specific [Skills](skills/) through APM.

## Artifact language

Most Skills use English. The [github-actions](skills/github-actions/SKILL.md) and [decision-recording](skills/decision-recording/SKILL.md) skills use Japanese. Follow the target repository's language conventions for produced artifacts.

## Maintainer references

[Maintainer references](docs/maintainer-references.md) collect source mappings, adoption decisions, and supplementary notes for Skills and retired Instructions, including the [Sakura Miko conversation sources](docs/sakuramiko-style-reference.md). Current guidance lives in the Skills and their references. Ordinary tasks do not require loading maintainer notes.

## Prerequisites

The distribution targets are Codex and GitHub Copilot, as specified in [apm.yml](apm.yml). Use APM CLI to install the Skills globally. Some Skills depend on others, so copying only a `SKILL.md` may omit required references.

The [github-actions skill](skills/github-actions/SKILL.md) can be used independently with its complete directory, containing `SKILL.md` and four bundled references.

The [decision-recording skill](skills/decision-recording/SKILL.md) can also be used independently with its complete directory. It covers the readers and purposes of documents, commit messages, comments, code, and tests, with GitHub settings and Conventional Commits guides, two recording templates, and a standalone commitlint workflow.

## Installation

Use [yomiyasu](https://github.com/nanaism/yomiyasu/tree/main/skills/yomiyasu) for refining Japanese prose. It is not included as an APM dependency of this package.

```bash
apm install --global --target codex,copilot daiksud/agents
```

## Skills and GitHub protection settings

The checking procedures defined by Skills are separate from protection conditions mechanically enforced by GitHub. Each repository manages its own Rulesets and required status checks; installing this package alone does not apply the same protection settings.

[github-repo](skills/github-repo/SKILL.md) diagnoses immutable releases, squash and merge-commit methods, PR-based commit messages, the main Ruleset, full-SHA requirements for external Actions, and free security features for the specified repository, and applies only the explicitly requested scope. “Diagnose the settings” ends with a report, “record the plan in an Issue” ends with a record, and “apply the settings” includes applying the differences and diagnosing again. It coordinates workflow content changes with [github-actions](skills/github-actions/SKILL.md), and does not create empty commits or PRs solely for GitHub-side settings changes.

This repository requires `pass` for pull requests. [PR validation](.github/workflows/ci-pr.yml) follows `draft → commit-stage → ready → acceptance-stage → pass`: every run first attempts to convert the PR to Draft, runs approval-policy tests and Markdown lint, marks it Ready, and then checks local file links including frontmatter paths. Creation, new commits, reopening, and PR edits trigger validation. Each stage requires its predecessor to succeed; the final `pass` check rejects failed, cancelled, or skipped validation. There is no special handling for fork or Dependabot PRs: a denied state change fails the run instead of allowing validation to continue. [Main-push validation](.github/workflows/ci.yml) runs the same approval-policy tests and Markdown lint.

CI does not wait for reviews or merge PRs. This repository does not wait for CodeQL scans or results before merging PRs. Check the [Ruleset](https://github.com/daiksud/agents/rules/22615823) for the latest enforced conditions, and [Review and merge](skills/change-delivery/references/review-and-merge.md) for procedures from ordinary review through post-integration verification.

## Codex approval automation

[The approval workflow](.github/workflows/approve-codex-review.yml) approves when Codex has reacted with 👍, the latest Codex Review Summary shows both Code Review and Security Review as Completed, and both full reviewed SHAs match the current PR HEAD. It reads the visible status cells and the Summary's full `commit_sha` fields, and identifies Codex by its GitHub login. Finding flags, receipts, timestamps, base and prior requests are not extra conditions. Before POST, it checks all pages of this PR's review history; an existing `github-actions[bot]` review in `APPROVED` or `DISMISSED` state for the same full SHA suppresses another approval, without requiring a body marker.

Summary creation/edits and completed `ci-pr` runs trigger evaluation, regardless of the CI run's conclusion. If the reaction has not arrived, it retries every 30 seconds, at most six times. Once both signals are present, it reads HEAD once and submits that verified SHA as `commit_id`; it does not reread Summary or reaction before submission. Per-PR concurrency serializes runs. Same-HEAD rereviews do not restore a dismissed automatic approval; another HEAD or PR has its own history. The history check and POST are not an atomic reservation against other writers. [Review automation responsibilities](docs/engineering-policies/review-automation.md) records the policy and its limits.

The approval workflow has no `workflow_call` entry point. CI owns its Draft/Ready operations directly in `ci-pr.yml`. Each PR has workflow-level concurrency with `cancel-in-progress: true`, without HEAD/base checks, coordination with approval, or recovery to Draft after a failure. Cancellation is not an atomic latest-HEAD guarantee. Failed acceptance leaves the PR Ready but the required `pass` check unsuccessful. CI contains no review-wait loop and does not merge PRs. GitHub suppresses most workflow events caused by `GITHUB_TOKEN`, so CI changes Draft/Ready directly rather than relying on a later Ready event.[^github-token-events]

[^github-token-events]: GitHub documents the workflow event suppression rules for repository `GITHUB_TOKEN` operations.

## Decision records and current guidance

[decision-recording](skills/decision-recording/SKILL.md) explains what each reader needs: current working information in documents, self-contained historical judgments in PRs/commits, Why-not constraints beside code, behavior and structure in code, and observable contracts in tests. It prescribes no document directory or policy name. [Local policy](docs/engineering-policies/change-records.md) retains actual validation reporting; `Not run` applies to discretionary checks, with required CI and repository validation exclusions preserved.

Use the [PR template](skills/decision-recording/assets/pull_request_template.md), [local instruction example](skills/decision-recording/assets/agents-decision-records.md), and [commitlint workflow](skills/decision-recording/assets/commitlint.yml) to adopt the practice. The [GitHub settings guide](skills/decision-recording/references/github-settings.md) covers squash and merge-commit merging with final PR title/body messages, prohibits rebase merging, and explains the required `commitlint` check. The [Conventional Commits guide](skills/decision-recording/references/conventional-commits.md) describes latest Bun/commitlint defaults and user configuration. Installation bundles these assets; consumer files and live settings require adoption in the target repository. This repository's active CI remains described above.
