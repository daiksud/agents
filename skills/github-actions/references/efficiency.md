---
type: Instruction
title: GitHub Actions efficiency improvements
description: Choose causes of waiting and usage from execution history and improve while preserving required validation and trust boundaries.
sources:
  - id: copilot-efficiency
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-cache
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching
---

## Measure causes and choose a few improvements

Check workflows, required checks, supported-environment documents, and run/job/step history. For new workflows define baseline validation through [Design](workflow-design.md). For existing workflows investigate caches, duplicate triggers, unnecessary runs, and long dependency paths, choosing a few evidence-based changes effective for the purpose. Missing configuration alone does not prove waste.[^copilot-efficiency]

Read-only examples for the working repository:

```bash
gh run list --limit 20 --json databaseId,workflowName,event,headSha,status,conclusion,createdAt,updatedAt,url
gh run view RUN_ID --json jobs,event,headSha,conclusion,url
gh run view RUN_ID --log-failed
```

Replace `RUN_ID` with an actual target ID. If retrieval is unavailable, treat this as static analysis of supplied files.

### Separate effects

| Observation | Judgment |
| --- | --- |
| Elapsed time until required PR results are available | Do queues, serial dependencies, or long jobs delay users? |
| Sum of job execution times | Does total runner usage decrease? Do not convert to prices without checking OS/billing conditions |
| Avoided run/job/matrix execution counts | Was processing omitted while preserving required validation? |

Align events, changes, runners, matrices, cache states, and sampling periods before/after, retaining confounders. Separate expected effects from measurements; missing data is neither zero nor confirmed improvement.

### Checks for each change

- **Caching**: Investigate download/save/extraction costs and hit rates. Include compatibility values such as lockfiles, OS, architecture, and tool versions in keys; validate dependencies after partial-match restoration. Avoid duplicating setup Actions' built-in caches. Do not save Secrets/authenticated settings; check creator/reader trust boundaries in [Safety](hardening.md). PRs may read base/default-branch caches.[^github-cache]
- **Duplicate runs**: Compare push/PR runs for the same change without losing necessary branch-protection, release, schema, migration, or shared-library validation.
- **Path decisions**: Skipping whole workflows may leave required checks Pending. Even with job-level decisions/aggregation, propagate required-validation failures to final results. Include dependencies, lockfiles, configuration, and workflows themselves, checking changed-file comparison bases, limits, and retrieval-failure behavior. Running all checks after workflow changes alone does not prove waste.[^github-syntax]
- **Concurrency**: Check cancellation of old PR validation, including workflow and PR/ref identifiers in groups. Do not uniformly enable mid-production-deployment cancellation. Even `cancel-in-progress: false` replaces the default pending slot; separately check queue semantics when all deployments must be retained. Consider `queue: max` where supported, checking limits and incompatibility with `cancel-in-progress: true`.
- **Matrices**: Investigate contracts guaranteed by each combination. Undocumented support requirements alone do not justify removal; check users, dependencies, and history. State retained/lost guarantees when reducing.
- **Parallelism/job consolidation**: Compare critical paths, startup/setup costs, and artifact handoffs. Parallelism may shorten elapsed time while increasing total usage. Do not substitute fixed multipliers for acceptable waiting/cost decisions.
- **Write-back jobs**: Check publication conditions/permissions for autoformatting and similar work. For changes to labels/manual operations, also validate event reassessment without arbitrarily changing agreements.

### Validate behavior and effects

For approved changes, use safe existing working branches to check related/unrelated changes, workflow changes, and cancellation during consecutive updates. First pushes on new branches alone do not validate path decisions. Audit-only requests propose validation without test pushes/dispatches.

Check cold/warm caches and required checks/artifacts. Investigate unexpected skips/runs as defects even when YAML appears valid. Report improvements, preserved guarantees, validated runs, measurements, and uncertainties.

[^copilot-efficiency]: Restructured measurement, selection, and validation perspectives from SKILL.md and actions/reporting/patterns/review-rubric.
[^github-cache]: Dependency caching reference. Check restoration compatibility and cross-branch access.
[^github-syntax]: Workflow syntax. Check filters, concurrency, and queue specifications in the target environment.
