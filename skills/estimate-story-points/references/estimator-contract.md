---
type: Instruction
title: Independent estimator contract
description: Define common inputs, read-only boundaries, and per-Task outputs for independent story-point estimators.
sources:
  - id: issue-209
    resource: https://github.com/daiksud/agents/issues/209
---

## Dispatch and isolation

Before dispatch, the facilitator follows the [skill entry point](../SKILL.md) and freezes the rules. Use the same substantive prompt, Task text, source snapshot, scale, and option definitions for every estimator in a round; vary only estimator identity and selected model/effort. Confirm actual separate contexts and different model families through execution-tool evidence, not the estimator's self-description alone.[^issue-209]

Keep the roster and execution evidence in the facilitator's local record. An accepted model/effort request does not prove the runtime honored it. Record requested and confirmed settings separately, leaving unavailable metadata unknown. Do not fabricate a successful launch, completed response, family, or context.

Remove existing estimate sections and peer votes from the common input packet. Estimators may read only approved source snapshots that do not expose peer estimates; they must not browse old estimate sections, parent summaries, other estimators' outputs, or shared scratch files. Ask for missing evidence in the returned ambiguities rather than opening an unrestricted source. The facilitator handles necessary additional source retrieval and verification for everyone.

Collect all responses before aggregating or discussing values. Do not send early responses to estimators still working. In round 2, reuse the same estimators, with their own prior answers allowed, and share only round-1 ranges and the clarification list as peer information. Hiding individual peer votes is a working hypothesis from the proposal, not an established guarantee against anchoring.[^issue-209]

## Common prompt template

Replace placeholders with actual task-scoped values. Source links do not replace the verified content snapshot.

```text
Role: independent estimator {estimator_id}; round {round_number}.

Estimate every Task in the packet on the supplied scale. You are not the
facilitator. Do not edit files, Issues, PRs, or settings; do not post comments,
ask the requester questions, or launch other agents. Use only the approved
read-only packet and return your own result without reading peer estimates.

Scale, source, and calibration: {scale_and_evidence}
Frozen rules and roster size: {rules}
Task IDs, body revisions, and current text: {task_packet}
Verified source facts and permitted source snapshots: {evidence_packet}
Pending decisions, option IDs, and compatible option combinations: {options}
Round 2 only: round-1 ranges and verified/requester-approved clarifications:
{ranges_and_clarifications}

For each Task, report work items, assumptions, risks, ambiguities, confidence,
and one scale value. For pending decisions, return a separate value for each
supplied option; never choose an option or combine mutually exclusive work.
Use null with a concrete question when information does not support a value.
Do not convert points into hours. Distinguish observed facts from assumptions.
For round 2, explain why each value changed or stayed the same. Do not aim to
match the earlier range, other agents, or a majority.

Return the YAML structure below. Do not add a retrospective, an Issue edit,
or a claim that the facilitator has verified your factual statements.
```

## Output shape

This is a shape example, not a real estimation result. Use stable Task and option IDs supplied by the facilitator. Replace all placeholders and return every target exactly once.

```yaml
estimator_id: estimator-a
round: 1
tasks:
  - issue: "owner/repository#123"
    body_revision: "snapshot-1"
    cases:
      - option: base
        points: 3
        confidence: medium
        work_items:
          - "Describe the actual work included in this case."
        assumptions:
          - "State an assumption explicitly, or use an empty list."
        risks: []
        ambiguities: []
        claims:
          - statement: "A factual statement relevant to this estimate."
            evidence: "An approved source identifier and precise location."
        change_reason: null
```

For a Task without pending decisions, return one `base` case. Otherwise, replace it with one case per supplied option or compatible option combination. Include the controlling decision Issue in assumptions. Do not add a `base` value that guesses which option will be selected.

`points` is a numeric member of the supplied scale or `null`; do not return intervals, off-scale values, `?`, or infinity as numeric votes. `confidence` is `low`, `medium`, or `high`, and does not weight votes. Keep all list fields, using empty lists where appropriate. A `null` value requires a concrete ambiguity explaining what is needed. `change_reason` is required per case in round 2, including when the value is unchanged.

Claims are leads for facilitator verification, not established facts. Missing Tasks, duplicate cases, unknown options, mismatched body revisions, malformed outputs, and incomplete responses cannot be silently corrected into valid votes or dropped to create convergence. Report the affected Tasks and resolve the input or execution problem without changing the frozen rules.

[^issue-209]: [Issue #209](https://github.com/daiksud/agents/issues/209), success conditions, proposed rules, and workflow. The output shape makes that proposal's requested estimator fields explicit.
