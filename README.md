---
type: Guide
title: daiksud/agents
description: Installation and use of shared Skills through APM.
sources:
  - id: github-token-events
    resource: https://docs.github.com/en/actions/concepts/security/github_token
  - id: skill-independence
    resource: https://github.com/daiksud/agents/issues/285
  - id: apm-install
    resource: https://microsoft.github.io/apm/reference/cli/install/
  - id: apm-virtual-packages
    resource: https://microsoft.github.io/apm/consumer/install-packages/
---

This repository shares task-specific [Skills](skills/) through APM.

## Artifact language

All four installable Skills use Japanese. Follow the target repository's language conventions for produced artifacts.

## Maintainer references

[Maintainer references](docs/maintainer-references.md) collect sources and maintenance notes for the Skills. Current guidance lives in the Skills and their references. Ordinary tasks do not require loading maintainer notes.

## Prerequisites

The distribution targets are Codex and GitHub Copilot, as specified in [apm.yml](apm.yml). Use APM CLI to install the Skills globally. Keep each skill's bundled references and assets with its `SKILL.md`.

## Choose a skill

The four skills below are installable through APM. Each is independently usable without installing the others.[^skill-independence]

| Task | Skill |
| --- | --- |
| Preserve judgment reasons and PR/commit records | [decision-recording](skills/decision-recording/SKILL.md) |
| Configure continuous-delivery pipelines and artifact handling | [continuous-delivery](skills/continuous-delivery/SKILL.md) |
| Configure commit conventions, commitlint, and automatic version calculation | [versioning](skills/versioning/SKILL.md) |
| Configure GitHub repository settings and supporting `.github` files | [github-repo](skills/github-repo/SKILL.md) |

## Temporarily archived skills

The following bundles are preserved under `archived-skills/` for later refinement. APM's automatic discovery installs skills from the root `skills/` directory, not `archived-skills/`, so these eight bundles are excluded from this package's installation.

| Task | Archived skill |
| --- | --- |
| Assess development practices, architecture, and organization | [engineering-assessment](archived-skills/engineering-assessment/SKILL.md) |
| Clarify domain rules, examples, and acceptance conditions | [behavior-specification](archived-skills/behavior-specification/SKILL.md) |
| Estimate work in relative story points | [estimate-story-points](archived-skills/estimate-story-points/SKILL.md) |
| Record plans, Issues, and work-item decisions | [issue-management](archived-skills/issue-management/SKILL.md) |
| Implement behavior and contracts | [software-development](archived-skills/software-development/SKILL.md) |
| Author technical documents and structured specifications | [document-authoring](archived-skills/document-authoring/SKILL.md) |
| Deliver approved changes through PRs, review, CI, and main verification | [change-delivery](archived-skills/change-delivery/SKILL.md) |
| Review changes without modifying them | [code-review](archived-skills/code-review/SKILL.md) |

Continuous-delivery uses `pr.yml`, `push.yml`, and `release.yml` as the basic pipeline. Optional `merge-queue.yml` runs `screening` and `inspection` on `merge_group: checks_requested`; `push.yml` can skip both when it can reuse a matching artifact from a successful queue run.

Under the skill's terminology, the `deployment` phase deploys service artifacts and saves each main commit's CLI artifact to GitHub Actions Artifacts. The `release` phase handles releases: user-visible service behavior changes, or manual `release.yml` (`workflow_dispatch`) that assigns a formal CLI version and creates a GitHub Release from an inspected artifact.

Release versions are calculated automatically from commit history according to the adopted strategy. Continuous-delivery integrates the calculation result with build order, artifact reuse, and release.

The [decision-recording skill](skills/decision-recording/SKILL.md) covers the readers and purposes of documents, commit messages, comments, code, and tests. It includes a guide to preserving PR records through GitHub merge settings and two recording templates.

Versioning uses Semantic Versioning and Conventional Commits. It owns detailed convention guidance, commitlint setup, its standalone workflow, and version-calculation rules and tools. It also supports commit-convention setup without automatic releases. Continuous-delivery and decision-recording retain brief guidance recommending the conventions for their respective purposes.[^skill-independence]

[^skill-independence]: [Independent skill guidance and versioning responsibilities](https://github.com/daiksud/agents/issues/285).

## Installation

Use [yomiyasu](https://github.com/nanaism/yomiyasu/tree/main/skills/yomiyasu) for refining Japanese prose. It is not included as an APM dependency of this package.

```bash
apm install --global --target codex,copilot daiksud/agents
```

To install only [github-repo](skills/github-repo/SKILL.md), specify its skill directory. Its bundled references and assets provide the guidance for repository settings and supporting configuration.[^apm-install][^apm-virtual-packages]

```bash
apm install --global --target codex,copilot daiksud/agents/skills/github-repo
```

[^apm-install]: [APM command reference](https://microsoft.github.io/apm/reference/cli/install/) documents global installation and explicit targets.
[^apm-virtual-packages]: [APM package installation](https://microsoft.github.io/apm/consumer/install-packages/) documents skill subdirectory references. See the [source mapping](docs/skill-sources/github-repo.md#standalone-installation) for the documentation-check scope.

## Skills and GitHub protection settings

The checking procedures defined by Skills are separate from protection conditions mechanically enforced by GitHub. Each repository manages its own Rulesets and required status checks; installing this package alone does not apply the same protection settings.

[github-repo](skills/github-repo/SKILL.md) diagnoses and applies the requested repository settings and maintains supporting `.github` files using its own references and assets. Its bundle covers Dependabot, CODEOWNERS, issue and PR templates, `SECURITY.md`, optional `CONTRIBUTING.md` and `SUPPORT.md`, and GitHub Actions dependency lockfiles, so it can handle this work when installed on its own. “Diagnose the settings” ends with a report, “record the plan in an Issue” ends with a record, and “apply the settings” includes applying the differences and diagnosing again. GitHub-side settings changes do not require empty commits or PRs; repository file changes follow the target repository's delivery rules.

Choose github-repo for repository settings and supporting configuration. [Continuous-delivery](skills/continuous-delivery/SKILL.md) covers pipeline design, build and test stages, artifact reuse, deployment, and releases. [Decision-recording](skills/decision-recording/SKILL.md) covers the content and purpose of change records, and [versioning](skills/versioning/SKILL.md) covers commit conventions and version calculation. These responsibilities guide skill selection; github-repo's execution uses its own bundle.

This repository requires `pass` for pull requests. [PR validation](.github/workflows/ci-pr.yml) follows `draft → commit-stage → ready → acceptance-stage → pass`: every run first attempts to convert the PR to Draft, rejects HTML comment openers in the PR body, runs approval-policy tests and Markdown lint, marks it Ready, and then checks local file links including frontmatter paths. Creation, new commits, reopening, and PR edits trigger validation. Each stage requires its predecessor to succeed; the final `pass` check rejects failed, cancelled, or skipped validation. There is no special handling for fork or Dependabot PRs: a denied state change fails the run instead of allowing validation to continue. [Main-push validation](.github/workflows/ci.yml) runs the same approval-policy tests and Markdown lint.

CI does not wait for reviews or merge PRs. This repository does not wait for CodeQL scans or results before merging PRs. Check the [Ruleset](https://github.com/daiksud/agents/rules/22615823) for the latest enforced conditions and [AGENTS.md](AGENTS.md) for repository-specific validation and change-record requirements.

## Codex approval automation

[The approval workflow](.github/workflows/approve-codex-review.yml) approves when Codex has reacted with 👍, the latest Codex Review Summary shows both Code Review and Security Review as Completed, and both full reviewed SHAs match the current PR HEAD. It reads the visible status cells and the Summary's full `commit_sha` fields, and identifies Codex by its GitHub login. Finding flags, receipts, timestamps, base and prior requests are not extra conditions. Before POST, it checks all pages of this PR's review history; an existing `github-actions[bot]` review in `APPROVED` or `DISMISSED` state for the same full SHA suppresses another approval, without requiring a body marker.

Summary creation/edits and completed `ci-pr` runs trigger evaluation, regardless of the CI run's conclusion. If the reaction has not arrived, it retries every 30 seconds, at most six times. Once both signals are present, it reads HEAD once and submits that verified SHA as `commit_id`; it does not reread Summary or reaction before submission. Per-PR concurrency serializes runs. Same-HEAD rereviews do not restore a dismissed automatic approval; another HEAD or PR has its own history. The history check and POST are not an atomic reservation against other writers. [Review automation responsibilities](docs/engineering-policies/review-automation.md) records the policy and its limits.

The approval workflow has no `workflow_call` entry point. CI owns its Draft/Ready operations directly in `ci-pr.yml`. Each PR has workflow-level concurrency with `cancel-in-progress: true`, without HEAD/base checks, coordination with approval, or recovery to Draft after a failure. Cancellation is not an atomic latest-HEAD guarantee. Failed acceptance leaves the PR Ready but the required `pass` check unsuccessful. CI contains no review-wait loop and does not merge PRs. GitHub suppresses most workflow events caused by `GITHUB_TOKEN`, so CI changes Draft/Ready directly rather than relying on a later Ready event.[^github-token-events]

[^github-token-events]: GitHub documents the workflow event suppression rules for repository `GITHUB_TOKEN` operations.

## Decision records and current guidance

[decision-recording](skills/decision-recording/SKILL.md) explains what each reader needs: current working information in documents, self-contained historical judgments in PRs/commits, Why-not constraints beside code, behavior and structure in code, and observable contracts in tests. It prescribes no document directory or policy name. [Local policy](docs/engineering-policies/change-records.md) retains actual validation reporting; `Not run` applies to discretionary checks, with required CI and repository validation exclusions preserved.

Use the [PR template](skills/decision-recording/assets/pull_request_template.md) and [local instruction example](skills/decision-recording/assets/agents-decision-records.md) to adopt the recording practice. Start with the decision and overview without a heading, then use flat Background, Considerations, Impact, Validation, and References sections. Keep the opening and validation status; remove unnecessary sections and every HTML authoring comment. The [GitHub settings guide](skills/decision-recording/references/github-settings.md) covers squash and merge-commit merging with final PR title/body messages and prohibits rebase merging.

For convention and tool setup, [versioning](skills/versioning/SKILL.md) provides the [Conventional Commits guide](skills/versioning/references/conventional-commits.md), [commitlint guide](skills/versioning/references/commitlint.md), and [workflow](skills/versioning/assets/commitlint.yml). The workflow pins Bun and commitlint while honoring existing commitlint configuration. A separate step rejects HTML comment openers in the PR body without changing commitlint rules. Consumer files and live settings require adoption in the target repository; package installation alone does not apply them. This repository's active CI remains described above.
