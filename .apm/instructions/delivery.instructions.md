---
type: Instruction
title: Value flow and integration
description: Define principles for delivering small changes safely and maintaining main and a distributable state.
---

## Value flow and integration

### Value flow and learning

In DevOps and Lean, share responsibility for user outcomes from planning through operations, and embed quality, security, and reliability in design and daily work. Choose the most influential constraint from the entire flow, including waiting, work in progress, and rework, and improve through small experiments with an expected change and conditions for reassessment. Avoid optimization that blames people or overloads them, and respect local knowledge and sustainable work.

In CD, maintain a state in which validated changes can be delivered safely when needed. Promote the same artifact across environments, and verify versioned configuration, reproducible distribution, and recovery. Distinguish deployment from release to users, and follow business conditions and existing approvals for release decisions. Automatic production release of every change is not required.

Reassess team responsibilities and relationships for collaboration, service provision, and support according to scale and constraints, considering dependencies that impede value flow and the cognitive load and experience of those responsible. Do not make the four team types a mandatory organization chart.

These are guides for daily decisions; do not perform a comprehensive diagnosis of development practices for ordinary changes. Read `~/.agents/skills/engineering-assessment/references/principles.md` when checking definitions, relationships, or sources.

### Integration and completion

Use small changes that can be validated and integrated independently, aiming for daily integration into main on active workdays. Do not skip approvals, review, or CI for a deadline. Follow [Repository artifact language](language.instructions.md) for commit messages and GitHub artifacts. Use English Conventional Commits, and allow breaking-change types only for `feat` and `fix`.

Associate changes to Git-managed files with an Issue, and squash-merge after validation, review of the latest HEAD, zero findings requiring action, successful required CI, and zero conflicts. Choose the reviewer through “Quick reviewer candidate assessment” in `change-delivery`; Copilot requires Approve when selected. For Codex, confirm normal completion for the latest HEAD and zero findings requiring action, including past findings, without relaxing protection settings.

Do not finish with PR-side success alone; take responsibility through required post-integration main validation, synchronization, and branch cleanup. If main is found failing during change work, prioritize recovery and stop subsequent work until it is healthy. Check the scope of recovery execution through `issue-management`. Follow `change-delivery` for required checks and delivery of recovery changes.

For changes only to GitHub-side repository settings, use `github-repo` to check the plan, approval, and evidence before and after the change, and judge completion by applying the differences and diagnosing again. Do not create empty commits or PRs. If Git-managed files must change as a prerequisite for applying settings, apply ordinary review, CI, and post-integration main verification to those changes.
