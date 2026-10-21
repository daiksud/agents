---
type: Instruction
title: Aggregate estimates and review disagreement
description: Define scale-step divergence, median consensus, fact checking, and round limits.
---

## Frozen rules

Fix the scale, roster, threshold, consensus rule, and round limit before reading estimates. Apply the following defaults to each Task and, when decisions are pending, independently to each option case.

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

For divergent Tasks, begin with the highest and lowest estimates' work items and assumptions. Also inspect the remaining Tasks for contradictions, stale evidence, and omitted work. Before computing any parent total, compare included work items and scope ownership across all target Tasks (and other relevant direct Tasks) for duplicated shared work. Check every factual estimator claim before copying it into an Issue; do not treat agreement among agents as verification.

| Cause | Facilitator action |
| --- | --- |
| Missing fact or stale reference | Retrieve the current authoritative Issue, PR, or file read-only. Record the source and verified fact in the local Task draft. |
| Different scope interpretations | Identify the difference. Clarify from already approved scope, or ask the requester where a new scope choice is required. |
| Shared work in multiple Tasks | Compare work items, dependencies, and ownership across Tasks. Clarify which Task owns the work, asking the requester when needed. A changed Task text triggers a full round 2; if ownership remains unresolved, leave affected estimates unestimated rather than subtracting points or publishing a misleading total. |
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
