---
name: change-delivery
description: Use to deliver approved repository changes from branch preparation through PR, review, CI, merge, and post-integration main verification. Hand Issue planning to issue-management and code implementation or document creation to the responsible Skill. Do not use for planning alone or read-only review alone.
---

# Deliver approved changes to main

Inherit the Issue plan that `issue-management` saved, retrieved, and verified, and execution approval. Do not treat the existence of an Issue plan alone as execution approval, or require recreating, resaving, or reapproving the same approved purpose and success conditions. Follow the dependency `issue-management` for Issue planning, publication permission, and GitHub Markdown quality. If that dependency is unavailable, do not start delivery; state unverified scope. `docs/` refers to the working repository.

## Material to read at each stage

Do not repeat completed stages; read material needed for the current stage. Resolve bundled links relative to the referring file.

| Stage or condition | Material |
| --- | --- |
| Work protection and branch preparation before editing, execution of approved decomposition | [Branches and integration units](references/branches.md) |
| Drafting commit messages, staging, committing | [Commit messages](references/conventional-commits.md) |
| PR, review, CI, merge, main verification and cleanup, recovery after failure | [Review and merge](references/review-and-merge.md) |
| Issue plans, decisions on publication permission, Issue updates, Markdown quality before and after posting | Corresponding material in the dependency `issue-management` |

## Continuation and completion

- For planning-only requests, stop after `issue-management` saves, verifies, and presents the plan; do not proceed to branches, edits, or PRs before approval. Follow that skill's execution scope for explicit stop conditions, additional permissions, external impact, and changes to purpose or acceptance conditions.
- With execution approval and confirmed saving, check branches, diffs, worktrees, other sessions' responsibilities, and required public-main checks before preparing a branch. Do not ignore conflicts, inability to verify, or failing main; protect and recover work.
- Within the approved scope, proceed through implementation, validation, commits, push, Draft PR, required CI, conflict resolution, ordinary review of a stable latest HEAD, and squash merge. If findings or other changes update HEAD, check required CI and conflicts on the new HEAD before re-review. Do not reinterpret pair checks as ordinary PR review. Also use `software-development` for code changes, `document-authoring` for document creation, and `code-review` only for read-only diff review.
- When changing skill judgments, add reproducible inputs and expected judgments to evaluations. Compare before and after through independent simulated execution using the same inputs and criteria; do not prove judgment quality solely through format checks or keyword matches.
- Execute planned validation, and compare the final diff with the request, related functionality, documents, paths, and commands. Commit in small verifiable units, and push after one TDD cycle or completed document validation and commit.
- During long work, share findings, remaining issues, and next work. Investigate failure causes and evidence-based alternatives; do not repeat the same operation without reason. State reasons and targets when user decisions or additional permissions are needed.
- Do not finish at PR-side success; confirm required validation and distribution at the actual public-main SHA, and own synchronization and branch cleanup. Do not treat failures or unverified results as success; prioritize recovery before resuming subsequent work.
- Report the Issue and PR, outcomes, validation and review, merge, main verification, synchronization, branch cleanup, and remaining issues. Do not treat unexecuted or unobtainable results as success; distinguish incomplete scope from conditions for resumption.

Add a short KPT from the common instructions to the final report after using the skill, honoring the output contract; check results for relevant adopted Try items. Follow [Recording improvements and checking next time](../issue-management/references/issue-recording.md#recording-improvements-and-checking-next-time) in the dependency `issue-management` for improvement records and later checks. Do not leave current delivery incomplete waiting for subsequent improvements, or begin separate changes based solely on improvement proposals.
