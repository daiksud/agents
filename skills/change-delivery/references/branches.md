---
type: Instruction
title: Branches and integration units
description: Check change protection, prepare branches, and work in independently verifiable integration units.
---

## Branches and integration units

### Execute approved decomposition

Use only Feature → Task Issue hierarchies; Tasks are leaves. Before creating or linking Sub-issues, verify the parent's Feature type, each child's Task type and lack of children, and existing relationships. Record decomposition reasons, scope, order, dependencies, and validation; retrieve saved bodies and links before execution. Creating Sub-issues alone does not approve starting work; apply [Scope and plan](../SKILL.md#scope-and-plan).

- In this session, execute approved decomposed tasks within the requested purpose and success conditions sequentially in the recorded scope and order. Do not add other purposes or other sessions' responsibilities.
- Leave tasks assigned to another session to that session. Before starting a Sub-issue, check Issues, PRs, and working trees for other sessions' progress, avoiding duplicate work. Ask the user if this cannot be determined.
- After decomposition, implement and validate each Sub-issue; parent Issue plans or validation do not substitute for this.

### Small integration units and active workdays

Validate changes early and integrate into main, reducing drift from long-lived branches. Include the following in plans based on CI principles.

- Make each change independently verifiable, reviewable, and integrable. Do not split solely by file counts; form units whose user goals and success conditions can be checked.
- Treat days with recorded change work as active workdays, aiming for daily main integration on active workdays and branches lasting no more than one active workday in principle. Do not assume weekends or other inactive days indicate delay.
- Record work start time, the next integration unit, and validation method in the Issue. After more than one active workday, update confirmed reasons such as waiting for approval/review or failure investigation, and the next integration unit.
- Do not skip approvals, review, or CI to meet the guideline, or merge unverified changes solely for a deadline.
- Update reasons and plans and continue adjustments to decomposition, order, or files within the purpose. Follow [Scope and plan](../SKILL.md#scope-and-plan) for changes needing confirmation. Sub-issue existence alone is not an execution request.
- At the start, check required validation on target main. If main is failing, prioritize [Recovery procedures](review-and-merge.md#post-integration-main-verification-and-recovery) and do not start subsequent work until healthy.

Record active workdays, stagnation, review waits, validation time, and main recovery time from timestamps/URLs in Issues, PRs, and existing Actions. State missing data, substitute timestamps, incomplete results, and unavailability; do not use them for individual evaluation or assertions of improvement effects from single comparisons. Keep project definitions and actual measurements in project documents, Issues, and PRs, without embedding individual results in common skills.

### Check and prepare branches

- At the start, check the current branch and working-tree diffs.
- With execution approval, if on `main`, create and switch to a working branch with `git switch -c <branch>` before file changes.
- If environment restrictions prevent branch creation even with approval, explain why and do not edit until preparation is possible.
- For non-`main` branches not confirmed created by this session, before changes read working-tree diffs, recent commits, related Issues/PRs, and `git worktree list`, checking relationships with this task and potential conflicts with other sessions.
- Branch names or absence of diffs alone do not establish permission to reuse existing branches.
- If evidence for using an existing branch is unavailable, ask the user; until confirmed, do not edit, switch branches, stash, commit, or otherwise change state.
- Make changes, commits, and validation on the working branch in the current working directory.
- Use branch prefixes from this table.

| Change | Prefix |
| --- | --- |
| Feature additions with breaking changes | `breaking/feat/` |
| Bug fixes with breaking changes | `breaking/fix/` |
| Other confirmed breaking changes | `breaking/<type>/`, with the type matching the change's purpose |
| Feature additions without breaking changes | `feat/` |
| Bug fixes without breaking changes | `fix/` |
| Documentation-only changes | `docs/` |
| Others | Choose an appropriate `build/`, `chore/`, `ci/`, `perf/`, `refactor/`, `revert/`, `style/`, or `test/` |

Other prefixes follow the target repository's adopted commit conventions.
Follow [Commit-message instructions](conventional-commits.md) to describe confirmed compatibility impact; the branch prefix does not restrict which commit types may contain a breaking change.
