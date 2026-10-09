---
type: Guide
title: daiksud/agents
description: Prerequisites for shared Instructions and Skills, and installation through APM.
sources:
  - id: codex-approval-assumption
    resource: https://github.com/daiksud/agents/issues/197
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

[The approval workflow](.github/workflows/approve-codex-review.yml) approves only open, non-Draft PRs when freshly fetched code and security reviews both completed normally for the full current HEAD, their results are clean and consistent, and the trusted Codex account currently has a PR thumbs-up without an eyes reaction. Abbreviated commits are resolved through the repository API. Under the approved operational assumption, this observable combination is the latest completed review; a unique provider execution identifier is not required.[^codex-approval-assumption]

Approval and invalidation stay in this workflow. It binds approvals to the current reviewed commit and tags them so dismissal preserves other reviewers and other automations. Each run fetches reviews first, then current PR, comments and reactions. Unknown, mixed, incomplete, or failed evidence never produces approval; an unrecoverable initial fetch fails the workflow, while a later evidence failure withdraws known automation approvals.

Event reconciliation uses a serialized per-PR concurrency group. GitHub may coalesce pending events; a later event or manual reconcile can re-evaluate current evidence.

CI changes Draft/Ready through native `gh` steps, while approval reconciliation responds independently to review events with the accepted processing lag. Failure-only Draft recovery is part of the check stage; the final ordinary job keeps the required check name `ci`. CI contains no review-wait loop. GitHub suppresses most workflow events caused by `GITHUB_TOKEN`, so CI performs its state changes directly rather than relying on a later Ready event.[^github-token-events]

Use the workflow's `workflow_dispatch` `reconcile` operation to explicitly fetch and re-evaluate current evidence. A manual reconcile is also the documented recovery for a thumbs-up that arrives after the summary event; this workflow intentionally does not add a polling framework. Local regression tests extract and execute the production shell run blocks with fixture-backed `gh` boundaries; they do not prove live event delivery or token permissions.

The accepted residual race remains: delayed provider publication may temporarily leave an older completed result and thumbs-up visible until the next event or manual reconcile. This design deliberately has no review-history, generation, barrier, or restart state framework. It checks current observable conditions; elapsed time is never completion evidence.[^codex-approval-assumption]

[^codex-approval-assumption]: Issue #197 records the accepted completed-state-plus-thumbs-up assumption and provider-publication/uncontrolled-start limitations.
[^github-token-events]: GitHub documents the workflow event suppression rules for repository `GITHUB_TOKEN` operations.
