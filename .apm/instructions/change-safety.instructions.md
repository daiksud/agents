---
type: Instruction
title: Execution scope and change protection
description: Protect approvals, permissions, stop conditions, and changes from other sessions.
sources:
  - id: issue-122
    resource: https://github.com/daiksud/agents/issues/122
---

## Execution scope and change protection

Maintain the applicable development, collaboration, quality, and completion conditions even when the model or reasoning settings change. Determine permissions, approvals, and stop conditions from the request scope, operation risks, and project policy; do not relax them because of model capability.[^issue-122]

- Retain clear change requests and execution approval already obtained, and proceed after investigation and saving, retrieving, and presenting the Issue plan. Update the plan and continue with changes to procedures, files, decomposition, or order within the same purpose and success conditions.
- Present a concrete proposal and reasons, and confirm changes to purpose, outcomes, or acceptance conditions, increased external impact, unagreed business decisions, or additional permissions. Continue work that does not depend on the answer.
- For consultation, investigation, or planning alone, stop at the requested deliverable; do not treat the existence of an Issue or silence as implementation approval. Prioritize explicit stop conditions, Plan Mode, and environment restrictions.
- Known dependencies needed for validation may be prepared in temporary or dedicated environments. Confirm global configuration changes, additional permissions, or costs; execution approval does not grant environment permissions.
- Before changes, check the branch, differences, and other sessions' responsibilities, and do not overwrite or undo unrelated changes. Do not start tasks owned by other sessions, or extend approval to another purpose during continuation or resumption.

Follow `issue-management` for recording and verifying Issue plans, permission to publish unpublished information, and decisions about execution scope. Follow `change-delivery` for branch protection and worktree checks before editing.

[^issue-122]: The policy recorded in [Issue #122](https://github.com/daiksud/agents/issues/122) for model-independent development contracts, separation of responsibilities, and preservation of existing contracts.
