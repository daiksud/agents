---
type: Policy
title: Review automation and merge protection
description: Bind Codex approval to the reviewed HEAD and leave merge eligibility to Rulesets.
---

## Current choice and applicability

This policy applies to this repository's [Codex approval workflow](../../.github/workflows/approve-codex-review.yml). It follows [gh-settings #554](https://github.com/daiksud/gh-settings/pull/554) and submits approval when these conditions hold:

1. Codex has reacted with 👍 on the PR.
2. The latest Codex Review Summary shows Code Review and Security Review as Completed.
3. Both full reviewed SHAs match the current PR HEAD.
4. This PR has no `github-actions[bot]` review in `APPROVED` or `DISMISSED` state for that full SHA.

GitHub's `user.login` identifies the Codex account. The latest Summary is selected by comment ID, and its Markdown status cells determine completion. After both signals are present, the workflow reads HEAD once and compares it with both full `commit_sha` fields in `codex-review-state:v1`. Missing, malformed or ambiguous commit metadata withholds approval. It submits the verified SHA as `commit_id` and requires the approval response to confirm that commit. Base, timestamps, receipts, finding flags, earlier requests and requested changes are not additional conditions.

Summary creation/edits and completed `ci-pr` runs trigger evaluation. CI success is a merge-protection concern. A Summary can update before its reaction appears, so the workflow waits with six retries at 30-second intervals. Each attempt reads Summary and reaction once, and reads HEAD only when both signals are present; it does not reread the signals before submission. A thumbs-up alone is not an `issue_comment` trigger; after polling ends, a later Summary or `ci-pr` completion event is needed. Per-PR concurrency serializes jobs. Before POST, the workflow reads all pages of this PR's review history once. Existing automatic approvals count without a body marker. A dismissed approval is never restored for the same HEAD, even after another Codex review. Another HEAD, PR or reviewer has separate history; nonapproval states do not suppress approval. History-read failures fail the run without approving.

## Ruleset responsibility

Rulesets own merge eligibility: required approvals, stale approval dismissal, required checks, base synchronization and review-thread resolution. Installing this package does not apply these settings to other repositories. The live [default Ruleset](https://github.com/daiksud/agents/rules/22615823), read on 2026-11-01, was active for `main`, with one required approval, resolved threads, `dismiss_stale_reviews_on_push: true` and strict required `pass` checks. Recheck current settings and applicable bypass permissions before claiming enforcement; this change does not alter them.

GitHub's [stale approval rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) concerns the approved diff and merge-base changes, not every SHA change in isolation. [Strict required checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging) require base synchronization before merging; they do not prove which diff Codex reviewed.

## Rationale and trade-offs

Full-SHA equality prevents a retained review for another commit from approving the current HEAD. Receipt validation, finding flags, base tracking and request-cycle bookkeeping remain outside this workflow. API failures are reported as failures; a successful run can withhold approval when evidence is absent or the reviewed SHAs differ.

Completed same-HEAD results and an existing thumbs-up remain reusable after a base change when this HEAD has no automatic approval history, including when other metadata or earlier comments describe findings. A newly issued approval therefore does not prove which diff was reviewed. Verification and POST are separate operations: a later push cannot retarget the submitted `commit_id`, but this is not an atomic current-HEAD guarantee. There is no extra reread if Summary or reaction changes after its read. Review-history checking and POST are also separate operations, not an atomic reservation against other writers. The workflow does not withdraw approvals or bypass merge protection. Actual approving reviews, required checks and resolved threads remain separate requirements. Ordinary [review and merge procedures](../../archived-skills/change-delivery/references/review-and-merge.md) still apply.
