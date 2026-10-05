---
type: Guide
title: Staged code review within the pair
description: Show checks for each Driver/Navigator Red / Green / Refactor stage without confusing them with ordinary review.
---

## Staged review within the pair

A Navigator asked to perform Driver/Navigator pair checks under the common instructions applies this skill's investigation and finding criteria to the selected TDD stage's purpose. Do not substitute them for ordinary PR review, required CI, approval, or merging; reviewers remain read-only.

A Navigator who finds user decisions qualifying as common standard candidates within the pair hands them to the Driver without copying unpublished decisions, reasons, or exceptions to public destinations. The Driver records candidate Issues under `issue-management` publication permission and recording procedures; the Navigator does not post.

- In **Red**, compare original requirements, minimal test diffs, and failure results. Check that expectations match contracts and failure is intentional due to unimplemented target behavior; environment deficiencies or test errors are not Red. Do not treat missing implementation or unstarted tests outside the selected item as defects.
- In **Green**, check contracts, regressions, and necessity from minimal implementation and new/related test results. Identify weakened expectations used to pass tests, unrequested features, or generalization. Temporary duplication is not a defect if its reasons and design improvements are tracked into Refactor in the same cycle.
- In **Refactor**, check resolution of carried design improvements or judgments that they need no action, preservation of behavior and validation effectiveness, and that rules with differing meanings were not forced into common structures. Do not demand changes when no improvement is needed, or artificial Red or unnecessary tests for behavior-preserving cleanup.
- When targets change, recheck that diffs, test results, and review results refer to the same code state. Distinguish findings requiring action, optional suggestions, and items carried into Refactor in the same cycle; Driver answers or fixes alone do not establish resolution.
