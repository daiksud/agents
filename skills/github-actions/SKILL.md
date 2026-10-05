---
name: github-actions
description: Use for GitHub Actions workflow creation or changes, failure investigation, review, efficiency or safety improvements, and Action internal-runtime upgrades. Also use issue-management and change-delivery for changes. Do not use for Issue/PR operations alone, application implementation alone, or CI/CD conceptual explanation alone.
---

# Design and validate GitHub Actions

Handle workflows that let developers receive necessary validation without excessive waiting and deliver trustworthy artifacts. Repository paths below refer to the working repository.

## Request and reference material

First check whether the request is design/investigation only, review, or includes changes. For changes, also use `issue-management` for Issue plans, publication permission, and execution scope, and `change-delivery` for approved changes through branches, PRs, required CI, and post-integration main verification. For Issue planning alone, `issue-management` can stop after saving, retrieving, checking body and display, and presenting the URL even without `change-delivery` or `software-development` installed.

For application code fixes, reproduce regressions and fix them through `software-development` TDD. For workflow-configuration-only fixes, do not start application-code TDD, but define minimal validation appropriate to the configuration failure first. Follow `document-authoring` for documents and `code-review` for read-only review procedures and findings. If `issue-management` is unavailable, do not post Issues or substitute another Skill; show unsaved drafts and restrictions. If `change-delivery` is unavailable, do not edit workflows or substitute another Skill; show incomplete validation and main verification. If `software-development` is unavailable, do not edit application code; show reproduction details and incomplete scope. If applicable dependencies are uninstalled, check installation methods in the usage environment. Do not proceed from consultation or audits alone to editing, Issue posting, PR creation, or execution triggers.

Read only applicable material, combining it when multiple areas are involved.

| Work or reading condition | Material |
| --- | --- |
| New workflows, triggers, job dependencies, reuse, deployment structure, runner/shell selection or changes | [Workflow design](references/workflow-design.md) |
| Security audits or changes involving permissions, external input, authentication, untrusted code, artifact/cache trust boundaries | [Safety](references/hardening.md) |
| Slow CI, duplicate runs, caching, skip conditions, parallelization, matrix improvements | [Efficiency improvements](references/efficiency.md) |
| Action version upgrades, internal-runtime deprecation warnings, runner compatibility | [Runtime upgrades](references/runtime-upgrades.md) |
| Checking provenance, adoption reasons, or version-dependent claims | [Sources and application decisions](references/sources.md) |

## Common judgments

1. Investigate `.github/workflows/`, called local Actions, reusable workflows and scripts, lock files, required checks, and supported environments. If execution history or settings are inaccessible, separate static knowledge from uncertainties.
2. Define the request's purpose and observable success conditions. Preserve existing required validation, supported environments, and release conditions; do not mix unrelated job redesign or optimization into upgrades.
3. For each change, check effective `permissions`, Secret destinations, executed-code provenance, runners, external input, and referenced Actions, artifacts, and caches. Do not judge safety solely by trigger name or fork status. Read safety material when boundaries are affected.
4. Pin external Actions and external reusable workflows to full commit SHAs checked against releases in the target repository, and verify agreement with version comments. Do not reuse example SHAs as recommended versions. Use verified digests for container references, and check the checkout provenance for same-repository relative references.
5. Choose minimal changes and validation meeting the purpose. Do not uniformly require manual approval, particular branching strategies, large matrices, or Canary.
6. For runner/shell selection or changes, read [Runners and shells in workflow design](references/workflow-design.md#runners-and-shells), checking actual available runners, provider/repository access, shell compatibility, and existing contracts.

## Outcomes and checks

For design/investigation, show evidence and proposals; for review, findings with reproduction conditions and impact; for changes, diffs and validation results. Match reporting formats to the request and existing skills.

- Statically check YAML syntax, Actions expressions, references, dependencies, and effects on required checks. Use available existing lint or actionlint; an ordinary YAML parser alone does not validate the Actions specification.
- Distinguish local tests from GitHub execution. For approved changes, compare target SHA, event, runner, and run URL, checking necessary artifacts or post-deployment state as well as execution results.
- Do not treat failed, canceled, unexecuted, or unobtainable results as success. If execution validation is impossible, show unverified scope and checking methods.
- Separate expected effects from measurements. CI success does not prove overall safety or performance improvement.
