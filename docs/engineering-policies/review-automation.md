---
type: Policy
title: Review automation and merge protection
description: Separate the two Codex approval conditions from Ruleset enforcement of merge eligibility.
---

## Current choice and applicability

This policy applies to this repository's [Codex approval workflow](../../.github/workflows/approve-codex-review.yml). It submits approval when both conditions hold:

1. Codex has reacted with 👍 on the PR.
2. The latest Codex Review Summary shows Code Review and Security Review as Completed.

GitHub's `user.login` identifies the Codex account. The latest Summary is selected by comment ID, and only its Markdown status cells determine completion. The workflow does not add HEAD, base, timestamps, receipts, finding flags, earlier requests or requested changes as approval conditions. It submits `APPROVE` without `commit_id`, leaving target-commit selection to GitHub. It does not require structured Summary metadata. Before submission it rereads only the same two conditions; changed comment bodies or reaction IDs are not extra gates.

Summary creation/edits and completed `ci-pr` runs trigger evaluation. CI success is a merge-protection concern, not another approval condition. A Summary can update before its reaction appears, so the workflow polls the same two conditions with six retries at 30-second intervals. A thumbs-up alone is not an `issue_comment` trigger; after polling ends, a later Summary or `ci-pr` completion event is needed. Per-PR concurrency serializes jobs. Repeated qualifying events can submit another approval; review-history checks do not suppress it.

## Ruleset responsibility

Rulesets own merge eligibility: required approvals, stale approval dismissal, required checks, base synchronization and review-thread resolution. Installing this package does not apply these settings to other repositories. The live [default Ruleset](https://github.com/daiksud/agents/rules/22615823), read on 2026-11-01, was active for `main`, with one required approval, resolved threads, `dismiss_stale_reviews_on_push: true` and strict required `pass` checks. Recheck current settings and applicable bypass permissions before claiming enforcement; this change does not alter them.

GitHub's [stale approval rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) concerns the approved diff and merge-base changes, not every SHA change in isolation. [Strict required checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging) require base synchronization before merging; they do not prove which diff Codex reviewed.

## Rationale and trade-offs

The user selected these two conditions to keep automatic approval small and leave merge policy with GitHub. HEAD/base correlation, receipt validation, finding flags and request-cycle bookkeeping are intentionally removed rather than becoming parallel approval policy. The workflow does not withdraw approvals or bypass merge protection. API failures are reported as failures; a successful run can withhold approval when either condition is absent.

A completed Summary and an existing thumbs-up can be reused after code or base changes, including when metadata or earlier comments describe findings. A newly issued approval therefore does not prove that the current commit or diff was reviewed, and stale dismissal of prior approvals cannot establish that proof. This is an accepted limit of the chosen policy, not a claim that Rulesets eliminate it. Actual approving reviews, required checks and resolved threads remain separate requirements. Ordinary [review and merge procedures](../../skills/change-delivery/references/review-and-merge.md) still apply.

Introducing/revising PR: [#265](https://github.com/daiksud/agents/pull/265).
