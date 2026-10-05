---
type: Reference
title: Handoff and rechecking after Navigator loss
description: Under common automatic re-pairing conditions, show retained evidence and comparison procedures before resumption.
sources:
  - id: issue-140
    resource: https://github.com/daiksud/agents/issues/140
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
  - id: issue-161
    resource: https://github.com/daiksud/agents/issues/161
---

## Reading conditions

When continuity with a launched Navigator is lost, the Driver pauses subsequent code changes needing checking and reads this before recovery/re-pairing procedures. After confirming continuation is impossible, a new Navigator may be launched without additional user confirmation. Before resuming, share relevant collaboration contracts and material with the replacement. If direct access is impossible, provide contents and hold affected stages until necessary confirmation. Do not read for ordinary initial launch, consultation, planning, or documentation-only work.[^issue-140] [^issue-161]

Common collaboration instructions are authoritative for retrying failed initial launches, avoiding duplicates when launch outcome is unknown, judging launched-Navigator loss, and starting automatic re-pairing. Loss after an initial response is not an initial-launch restart merely because code editing has not begun. Use [Internal communication](agent-communication.md) for message formats and [CLI material](copilot-cli-pairing.md) only in applicable Copilot CLI environments.[^issue-140] [^issue-161]

## Retained evidence and handoff

During recovery investigation, preserve confirmed/unconfirmed scope and check continuation with the original Navigator from actual responses and available states/history. Do not lose existing diffs or invent missing history.[^issue-100]

When confirmed inability to continue leads to automatic re-pairing, record removal of the original Navigator. Delayed responses from it are not new-pair stage evidence; if necessary, hand them to the new Navigator as unverified material. Do not switch back if the former Navigator recovers.[^issue-100] [^issue-161]

Before resuming, the Driver shares the following with the replacement.[^issue-100]

- Original request, acceptance conditions, applicable instructions, scope, and related user decisions.
- Shared ToDos, current TDD stage, planned next work, unresolved findings, and exchange counts on the same issue.
- Branch, HEAD, and worktree state; uncommitted diffs; executed commands, tests, validation, and results.
- Confirmed/unconfirmed stages, evidence of completed items, current final diffs, and adopted/rejected decisions with reasons.
- Related Issues, PRs, reviews, references, available former-Navigator response history, and other retrievable context needed for resumption decisions.

## Comparison before resuming

1. Share necessary assumptions/evidence and confirm actual continuing responses from the replacement. Launch success or state displays are not substitutes.
2. Do not assume missing history/validation succeeded; recheck actual diffs/tests from the first stage the former pair did not confirm.
3. Compare completed-item evidence with current final diffs. Rerun affected validation/checks if targets changed.
4. Retain unresolved findings and the two-exchange limit on the same issue without resetting for replacement. If the new pair cannot continue, use the same process to pass as much context as possible to the next Navigator, repeating automatic re-pairing.

Do not resume code changes until these comparisons finish. Do not replace ordinary PR review, required CI, or merge conditions with pair checks, or treat reading material or launching a replacement alone as completed recovery or successful validation.[^issue-100] [^issue-161]

[^issue-140]: [Issue #140](https://github.com/daiksud/agents/issues/140) on recovery-only detail and retaining mandatory contracts at entry points.
[^issue-161]: [Issue #161](https://github.com/daiksud/agents/issues/161) on automatic re-pairing without user confirmation and transferring as much context as possible.
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) on evidence preservation, retiring the former Navigator, and revalidation from unconfirmed stages.
