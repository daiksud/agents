---
type: Instruction
title: Record Task and parent estimates
description: Define estimate sections, conditional totals, and final Issue saves through issue-management.
sources:
  - id: issue-209
    resource: https://github.com/daiksud/agents/issues/209
---

## Ownership and publication

Read [issue-management](../../issue-management/SKILL.md) and its [Issue records](../../issue-management/references/issue-recording.md), [writing guidance](../../issue-management/references/github-writing.md), and [Markdown quality](../../issue-management/references/markdown-quality.md) before preparing actual Issue updates. Inherit the estimation request and its approved targets; it does not authorize implementation, Issue creation or splitting, or publication of private evidence to another repository.

Preserve each full original body, its scope, acceptance conditions, links, and relevant prior history. Apply verified clarifications to the Task text, not just to an estimate note that leaves contradictory original requirements intact. Maintain one current estimate section rather than appending duplicates. Retain prior results as identified history without presenting them as estimates of changed text.

Prepare all changes as local drafts through the final round. The planned write is one complete-body save per target Task and, when present, one parent save after finalization, not intermediate per-round updates.[^issue-209]

## Task section

Adapt this shape to the repository's body language and established structure. Placeholders describe required content, not actual results; omit inapplicable sections rather than leaving empty filler.

```markdown
## Story point estimate

Agreed estimate: <scale value, or Unestimated — concrete open question>
Scale: <ordered values>; source: <verified policy or requester decision>
Method: <roster of estimator IDs with actual models/families>; facilitator did not vote.
Rules: divergence at two scale steps; nearest numeric median, ties upward; maximum two rounds.
Basis: <Task snapshot/revision, estimation date, and relevant scope>

| Round | Option | Estimator A | Estimator B | Estimator C | Estimator D | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | <base or option ID> | <value> | <value> | <value> | <value> | <range, divergence, or consensus> |
| 2 | <base or option ID> | <value> | <value> | <value> | <value> | <range, divergence, or consensus> |

### Review and clarifications

<Actual divergence causes, verified evidence, requester decisions, and their resolutions.>
<Contradictions found without divergent votes and how they were resolved.>
<Each estimator's explanation for changed or unchanged round-2 values.>

### Remaining uncertainty

<Unanswered question, pending decision Issue/options, assumptions, or verification limitation.>
```

Match estimator columns to the actual roster; remove the fourth column when three were agreed before dispatch. Include round 2 only when executed. Include all actual per-round values, including divergent ones, but use `no response` or `unestimated` for missing/non-numeric results, never `0` unless it was a valid estimate on the team's scale. Identify invalid responses explicitly without converting them into valid votes.

For pending decisions, replace the single agreed estimate with an option table containing each option's estimate or unestimated status and its controlling decision Issue. Include round rows for each option. A resolved case is not an unconditional Task estimate while the policy is pending. Preserve estimator confidence and consequential assumptions with the review notes; confidence does not weight consensus.

Every factual claim adopted into Task text or review notes must have facilitator verification. When evidence remains unavailable, describe the open verification question rather than repeating the unsupported claim as fact. Do not publish confidential source contents or internal execution identifiers merely to fill the template.

## Parent summary

When a parent exists, maintain a summary for the explicitly selected target set; state excluded or unestimated Tasks so a subtotal cannot be mistaken for all parent work. Reference actual Task Issue URLs and preserve unrelated parent content.

```markdown
## Story point summary

Targets: <exact Task set; whether all open direct Tasks or a selected subset>
Scale and source: <same scale and source as the Tasks>
Method: <actual model-family roster, frozen rules, and rounds executed>

| Task | Agreed estimate | Status or decision dependency |
| --- | --- | --- |
| <Task link> | <value or Unestimated> | <confirmed or pending question> |

Estimated subtotal: <sum of eligible estimates>; <estimated count>/<target count> Tasks estimated.
Full total: <sum only when the target set has no unestimated Tasks or unresolved options; otherwise unavailable>.

### Pending options

| Compatible option set | Estimated subtotal | Coverage and outstanding questions |
| --- | --- | --- |
| <decision Issue and option IDs> | <conditional subtotal> | <estimated count and limitations> |

### Update history

- <actual date>: <rounds completed, clarifications, requester decisions, and remaining uncertainty>.
```

Sum each Task once and only on the same scale. A common decision controls every dependent Task consistently: do not select option A for one Task and incompatible option B for another. Add unconditional estimates to each compatible option set once. Never add mutually exclusive estimates together. Label conditional totals as conditional and incomplete sums as subtotals; an unestimated Task is not zero. Do not sum previously estimated Tasks outside the selected set without a separate request.

## Final save procedure

1. Check that final values apply to final Task text and that all published factual claims were verified. Keep unsupported claims out of the saved body. Recompute totals from eligible final Task/option results, excluding unestimated cases.
2. Retrieve current remote bodies immediately before saving. Compare with the preserved originals. Incorporate unrelated concurrent edits without overwriting them; material scope changes invalidate affected estimates. Do not use votes for an obsolete revision or exceed the two-round limit to repair it. Hold affected saves or record unestimated status with the question.
3. Save complete Task and parent drafts to temporary Markdown files. Use the actual common configuration resolved from `issue-management`, without adding YAML/OKF frontmatter to Issue bodies. Run its required rumdl fix, check, diff inspection, and idempotence check; do not post when required formatting cannot pass.
4. Save each final Task body once through `issue-management` from the checked file, not a reconstructed string. Retrieve it and compare the complete body with the final draft. Check headings, tables, links, Alerts if used, and list rendering. Do not report an API HTML check as visual screen inspection.
5. Save and verify the parent after the Task saves are confirmed. If a Task save fails or its result is unknown, retrieve current state before retrying; do not resave already matching bodies. Hold a success-looking parent update and report partial completion rather than claiming a synchronized summary.
6. On a verified content/rendering defect, correct the local source, repeat formatting, and make only the necessary recovery save. Record this exception to the planned single save; it does not authorize routine per-round writes. Open the browser only when requested, following `issue-management`.
7. Report the retrieved Issue URLs, agreed/conditional values, totals and coverage, requester decisions, unresolved questions, and actual save/rendering checks. If writes or checks are unavailable, return permitted drafts and the exact missing capability without claiming publication or closing implementation Issues.

[^issue-209]: [Issue #209](https://github.com/daiksud/agents/issues/209), desired state, success condition 7, and workflow. This procedure delegates existing publication and Markdown requirements to `issue-management`.
