---
type: Policy
title: Review automation and merge protection
description: Separate Codex review interpretation from Ruleset enforcement of merge eligibility.
---

## Current choice and applicability

This policy applies to this repository's [Codex approval workflow](../../.github/workflows/approve-codex-review.yml). It interprets trusted completed review results for the current HEAD and submits approval for that commit. Rulesets own merge eligibility, including required approvals, stale approval dismissal, required checks and base synchronization. Installing this package does not apply this repository's protection settings to another repository.

The live [default Ruleset](https://github.com/daiksud/agents/rules/22615823), read on 2026-11-01, was active for `main`, with `dismiss_stale_reviews_on_push: true` and `strict_required_status_checks_policy: true` for `pass`. Recheck live rules and applicable bypass permissions before claiming enforcement. This change does not apply settings or use bypass permissions.

GitHub's [stale approval rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-pull-request-reviews-before-merging) tracks changes to the approved diff, including changes introduced through the merge base. A new HEAD SHA or an update to `main` is not by itself a complete statement of dismissal conditions. [Strict required checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets#require-status-checks-to-pass-before-merging) require an up-to-date base before merge; this does not prove which base Codex reviewed.

## Rationale and trade-offs

The workflow verifies Codex Bot/App provenance, completed code and security results for the exact HEAD, findings and the trusted thumbs-up. Nullable security results additionally need the latest trusted clean receipt of each kind for that HEAD and full-SHA resolution. It rechecks trusted evidence, reaction, open state and HEAD before submitting approval with the verified `commit_id`.

Completed same-HEAD results and an existing thumbs-up remain usable after another request. No timestamp, edit-time or request-cycle comparison forces the same code to be reviewed again. Base history, stale approval dismissal and merge checks stay with GitHub rather than being duplicated in the workflow. Keeping separate responsibilities avoids a permanent approval hold after a base retarget.

This intentionally does not prove review-cycle identity or detect edited/replayed evidence through timestamps. A HEAD-only result does not identify the reviewed base or prove that the current diff was reviewed after a base update. A workflow may withhold approval and still exit successfully; approval is separate from passing CI and merge eligibility. Required checks remain enforced by the live rules, not by the act of approving.

## Alternatives and reconsideration

Requiring a new request/receipt cycle after every request, or tracking base history inside the workflow, adds coordination that does not demonstrate a code change at the same HEAD. The chosen boundary uses current commit/result identity and leaves merge policy to Rulesets. If merge protection needs to change, inspect and explicitly authorize that settings change rather than silently compensating in approval automation. Ordinary [review and merge procedures](../../skills/change-delivery/references/review-and-merge.md) still apply.
