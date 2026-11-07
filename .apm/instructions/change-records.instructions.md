---
type: Instruction
title: Change records and current engineering policy
description: Keep current working guidance in files and self-contained decision history in commits.
---

## Change records

- Apply [decision-recording](../../skills/decision-recording/SKILL.md) when choosing what belongs in documentation, commits, comments, code, or tests, or introducing this recording practice to a repository.
- Documents describe the current technologies, specifications, rules, editable boundaries, and procedures needed by someone joining today. Keep adoption history, rejected alternatives, and reasons for changes in commit messages. No document path or policy-document name is prescribed.
- PR descriptions record the problem, actual change and resulting behavior, relevant decisions, and actual validation status. Include the facts, constraints, comparisons, and reasons needed to understand the judgment without opening links. Links are supplementary; link-dependent decision records are prohibited. Reflect review conclusions in the final body.
- Validation status is required; execution, method, scope, rigor, and timing are discretionary unless the task or repository independently requires them. `Not run` is valid without a required justification or post-merge plan. Distinguish completed, partial, failed, planned, and unperformed checks. Unperformed validation alone is not a defect, incomplete implementation, or merge blocker. Preserve required CI and explicitly agreed acceptance conditions.
- Templates may contain HTML authoring comments. Remove all HTML comments from actual PR descriptions at creation/update, review, and before merge. Allow squash and merge-commit merging, prohibit rebase merging, and preserve the final title and description verbatim as the commit subject/body with either method. Existing effective protections still govern each merge; adopting guidance alone does not change settings.
- Put Why-not comments beside code whose plausible alternative fails a current constraint. Express processing and structure in simple code, and expected observable behavior and contracts in tests. Update only the recording destinations affected by the change.

The independent skill owns the [PR template](../../skills/decision-recording/assets/pull_request_template.md), [local instruction example](../../skills/decision-recording/assets/agents-decision-records.md), [GitHub settings guide](../../skills/decision-recording/references/github-settings.md), and [Conventional Commits and commitlint guide](../../skills/decision-recording/references/conventional-commits.md). Use `issue-management` for GitHub writing, `change-delivery` for delivery, and `code-review` for review. Accept equivalent local arrangements and make only relevant adoption changes within the requested scope.
