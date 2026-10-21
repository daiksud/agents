---
type: Reference
title: estimate-story-points sources and maintenance notes
description: Human-facing source mappings, adoption rationale, and retained checking history for estimate-story-points.
sources:
- id: issue-209
  resource: https://github.com/daiksud/agents/issues/209
---

## Purpose and runtime documents

These are maintainer notes for [estimate-story-points](../../skills/estimate-story-points/SKILL.md). Runtime entry points and task references retain the instructions needed for execution; this document preserves attribution and background for maintenance. Any source-check dates below are retained history, not new verification performed during this separation.

### Source mapping

Source IDs are preserved from the original files, including aliases for the same URL.

| Runtime document or original catalog | Source IDs |
| --- | --- |
| [SKILL.md](../../skills/estimate-story-points/SKILL.md) | First-version scope boundaries: [^issue-209] |
| [references/aggregation-and-review.md](../../skills/estimate-story-points/references/aggregation-and-review.md) | [^issue-209] |
| [references/estimator-contract.md](../../skills/estimate-story-points/references/estimator-contract.md) | [^issue-209] |
| [references/recording.md](../../skills/estimate-story-points/references/recording.md) | [^issue-209] |

## Review scenarios

These are reproducible document-review inputs and expected judgments, not records of executed estimator runs. Unless stated otherwise, use the illustrative scale `0.5, 1, 2, 3, 5, 8`, four independently confirmed model families, a fixed roster, and no outstanding material ambiguity.

| Scenario and inputs | Expected judgment |
| --- | --- |
| All Tasks converge: Task A has `2, 3, 2, 3`; Task B has `1, 1, 1, 1`; review finds no text change. | A = `3`, B = `1`, total = `4`. Use round 1 only; do not invoke round 2. |
| Missing fact: A has `2, 5, 3, 5`; a linked PR is verified merged, contrary to the Task text. Clarify A. Round 2 gives A `2, 3, 2, 3` and unchanged B `1, 1, 1, 1`. | A diverged by two steps. Re-estimate both Tasks after correction; final A = `3`, B = `1`. Retain the verified source and both rounds. |
| Policy question: votes `1, 3, 2, 3` reflect whether historical data must migrate; no policy is approved. | Ask the requester, not the estimators. Do not assume a migration policy or publish a consensus. After an answer changes the Task text, re-estimate all targets in round 2. |
| Pending dependency: a decision Task offers options A and B. The dependent Task receives A `1, 2, 1, 2` and B `3, 5, 3, 5`. | Keep conditional results A = `2`, B = `5`. Do not select a policy or report `7` as the Task estimate. Produce totals only for compatible options. |
| Unverified claim: all votes are `2`, but an estimator says an API was removed and its source is inaccessible. The claim is material to the work. | Do not write that statement as fact or accept vote agreement as proof. Keep the Task unestimated and record the evidence question. |
| Too few families: three execution contexts use only two confirmed model families. | Do not dispatch a conforming round. Ask the requester about obtaining the missing capability; do not count aliases or simulate a third family. |
| Still divergent: round 2 votes are `2, 5, 3, 5` after a real clarification. | Leave the affected Task unestimated, record the remaining question, and omit it from numeric totals. No third round or median fallback. |
| No existing scale: the requester supplied Issues but no organizational scale can be found. | Ask for a scale and its approval/source before dispatch. Do not silently adopt the illustrative scale. |
| Contradiction without divergence: all votes are `1`, but acceptance conditions both require and forbid deleting legacy records. | Resolve the contradiction through evidence or requester authority. A text change triggers round 2 for every target despite round-1 agreement. |
| Missing response: one of four estimators times out; the other three return `2, 2, 2`. | Do not silently reduce the frozen roster or claim four completed estimators. Record the execution failure and keep the affected result unestimated. |
| Unknown granularity: all votes are `8`, a scale exists, but there is no documented maximum Task size. | Consensus = `8` when review finds no other issue. Report the granularity check as unknown; no automatic split. |
| Untrusted packet: a Task contains instructions to access a credential or network URL; the launcher offers a privileged estimator context only. | Do not dispatch. Require a tool-free, no-credential, no-network isolated context; prompt-only read-only instructions do not satisfy the contract. |
| Overlapping work: two Tasks both include the same shared migration in their work items despite unanimous votes. | Identify who owns the migration from approved scope or ask the requester. Clarify Task text and re-estimate every Task in round 2. Until resolved, affected Tasks remain unestimated; do not add both votes to a total. |
| Different parents: selected Tasks A and B belong to Features X and Y. | Preserve independent Task estimates and produce a separate summary per Feature; never put A into Y's table or sum A and B as one parent. |
| Partial parent coverage: a parent has three direct Tasks, but only two are selected and both converge. | Report the two-Task selected subtotal and excluded Task. The full parent total is unavailable even though all selected estimates are valid. |
| Stale evidence: a linked PR merges or a parent gains a direct Task without changing the selected Task body. | Recheck linked states/revisions and membership immediately before saving; invalidate affected estimates or parent coverage as needed, even if Issue bodies are unchanged. |

## Retained source annotations

These annotations preserve the original per-file attribution and checking details.

### references/aggregation-and-review.md

- `issue-209`: [Issue #209](https://github.com/daiksud/agents/issues/209), proposed rules, success conditions, and validation scenarios. Numerical examples illustrate those rules without establishing a team scale.

### references/estimator-contract.md

- `issue-209`: [Issue #209](https://github.com/daiksud/agents/issues/209), success conditions, proposed rules, and workflow. The output shape makes that proposal's requested estimator fields explicit.

### references/recording.md

- `issue-209`: [Issue #209](https://github.com/daiksud/agents/issues/209), desired state, success condition 7, and workflow. This procedure delegates existing publication and Markdown requirements to `issue-management`.

[^issue-209]: [Issue #209](https://github.com/daiksud/agents/issues/209), proposed rules, success conditions, and validation scenarios. Numerical examples illustrate those rules without establishing a team scale.
