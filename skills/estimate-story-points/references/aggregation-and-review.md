---
type: Instruction
title: Aggregate estimates and review disagreement
description: Define scale-step divergence, median consensus, fact checking, round limits, and reproducible review scenarios.
sources:
  - id: issue-209
    resource: https://github.com/daiksud/agents/issues/209
---

## Frozen rules

Fix the scale, roster, threshold, consensus rule, and round limit before reading estimates. Apply the following defaults from Issue #209 to each Task and, when decisions are pending, independently to each option case.[^issue-209]

| Rule | Judgment |
| --- | --- |
| Valid responses | Every estimator in the frozen roster returns one scale value for the same Task revision and option. Missing, invalid, or `null` values are not votes. |
| Divergence | Find the lowest and highest values' positions in the ordered scale. A gap of at least two positions diverges; numerical distance is not the threshold. |
| Consensus | Only after review, and only without divergence or an unresolved material question, choose the scale value numerically closest to the median of the votes. For an even count, the median is the arithmetic midpoint of the middle two sorted values. On equal distance, choose the larger scale value. |
| Rounds | At most two. Round 2 occurs only if review changes any Task text, and then includes every target Task with the same roster. Do not run round 2 merely to obtain preferred numbers. |
| Final result | Use the final eligible round, not a mixture or average across rounds. After round 2, divergence leaves that Task or option unestimated with an open question. |

For the illustrative scale `0.5, 1, 2, 3, 5, 8`, votes `2, 3, 2, 3` are one step apart: median `2.5`, consensus `3`. Votes `3, 5, 3, 5` also differ by one step, so consensus is `5`. Votes `2, 5, 3, 5` differ by two steps and must not be collapsed into a consensus. These are examples, not a default organizational scale.

Consensus is a tie-break after examining assumptions, not evidence of objective effort, an average hiding disagreement, or a confidence-weighted vote. Agreement can coexist with contradictory completion conditions or shared factual errors.

## Review every Task

For divergent Tasks, begin with the highest and lowest estimates' work items and assumptions. Also inspect the remaining Tasks for contradictions, stale evidence, and omitted work. Check every factual estimator claim before copying it into an Issue; do not treat agreement among agents as verification.

| Cause | Facilitator action |
| --- | --- |
| Missing fact or stale reference | Retrieve the current authoritative Issue, PR, or file read-only. Record the source and verified fact in the local Task draft. |
| Different scope interpretations | Identify the difference. Clarify from already approved scope, or ask the requester where a new scope choice is required. |
| Policy question | Ask the requester and record their decision and rationale. Do not make the policy decision as a technical assumption. |
| Contradictory completion conditions | Resolve from authoritative requirements or requester clarification even when votes do not diverge. |
| Decision pending in another Task | Name the dependency and options, and obtain separate estimates per compatible option case. Leave the decision pending. |
| Unsupported or incorrect claim | Verify independently of the estimator's assertion. Correct disproved claims; do not publish unsupported claims as facts. A material question still lacking evidence keeps the affected result unestimated. |
| Different judgments with no justified text change | Record the unresolved assumptions. Do not edit text cosmetically or repeat voting simply to remove divergence. |

Keep reviews, requester answers, and clarified bodies local until finalization. Mark a clarification as a verified fact, an approved decision, or a still-open question; do not turn a proposed decision into an approved one. Ask only questions that need requester authority and continue independent review where possible.

## Re-estimation and stopping

If review changes any Task text, provide every estimator with the revised packet for all targets, the range for each round-1 case, and the clarification list. Do not expose individual peer votes, peer identities attached to votes, a suggested result, or a selected majority. When an option is newly defined, mark its previous range unavailable rather than inventing one.

Validate round-2 responses against those exact drafts. Keep reasons for changed and unchanged values. A new material ambiguity after round 2 is recorded as an open question without a numeric estimate; do not amend the scope and present an old vote as covering it, or start a third round. A Task still divergent without any review-driven text change remains unestimated after round 1.

When a value exceeds a documented organizational Task-granularity limit, propose a split through [issue-management](../../issue-management/SKILL.md). Do not create or split Issues automatically, and preserve its Feature-to-Task, leaf-Task hierarchy. When no limit is documented, report that the granularity check is unknown; do not invent a limit or block otherwise valid estimation solely for that reason.

## Review scenarios

These are reproducible document-review inputs and expected judgments, not records of executed estimator runs. Unless stated otherwise, use the illustrative scale above, four independently confirmed model families, a fixed roster, and no outstanding material ambiguity.

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

[^issue-209]: [Issue #209](https://github.com/daiksud/agents/issues/209), proposed rules, success conditions, and validation scenarios. Numerical examples illustrate those rules without establishing a team scale.
