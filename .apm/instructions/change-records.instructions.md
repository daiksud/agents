---
type: Instruction
title: Change records and current engineering policy
description: Separate PR decision history, actual validation status, and living Engineering Policies.
---

## Change records

- PR descriptions record the problem, actual change and resulting behavior, relevant decisions, and actual validation status. Keep them proportional and self-contained enough to preserve the judgment made at the time even after linked policies change. Update them to the final reviewed change before merge.
- Validation status is required; execution, method, scope, rigor, and timing are discretionary unless the task or repository independently requires them. `Not run` is valid without a required justification or post-merge plan. Distinguish completed, partial, failed, planned, and unperformed checks. Unperformed validation alone is not a defect, incomplete implementation, or merge blocker. Preserve required CI and explicitly agreed acceptance conditions.
- Templates may contain HTML authoring comments. Remove all HTML comments from actual PR descriptions at creation/update, review, and before merge, retaining substantive content including validation status. Preserve the final title and description in the squash subject/body using `PR_TITLE` / `PR_BODY` under `change-delivery`.
- For repositories adopting this model, keep currently effective cross-cutting or future-guiding decisions in topical `docs/engineering-policies/` documents, with applicability, rationale, relevant alternatives, trade-offs, and the introducing/revising PR. Revise the same topical document when policy changes. Historical judgments remain in PR descriptions and commits; ordinary local changes need no policy document.

Use `issue-management` for detailed PR writing, `change-delivery` for the reusable template and merge procedure, `code-review` for review, and `document-authoring` for policy authoring. At the start of repository change work, inspect local instructions, PR templates, current policies, and prior adoption decisions under [Repository adoption](../../skills/change-delivery/references/repository-adoption.md). Accept equivalent arrangements; propose concrete gap-filling changes within authorized scope, preserve prior decisions including deferral, and continue unrelated work. Installation alone does not adopt files or settings.
