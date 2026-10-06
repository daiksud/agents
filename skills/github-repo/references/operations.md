---
type: Instruction
title: Repository setting operations and judgments
description: Proceed from read-only diagnosis through approved differences and revalidation while preserving permission and failure boundaries.
sources:
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
---

## Read-only diagnosis

1. Match user-specified GitHub.com `owner/repo` with retrieved repository ID, full name, and URL. Do not resolve omissions/ambiguity by operating on another repository. Replace subsequent endpoint `{owner}`, `{repo}`, and `{ruleset_id}` with confirmed values.
2. Check requested deliverables/approval scope. Diagnosis uses only GET/UI reading, without Issue posts, test pushes, workflow starts, or setting changes.
3. Investigate target instructions, visibility, ownership, default branch, permissions, and upper-level policies. Metadata alone does not prove administrative authority.
4. Select expected values/observations from [Setting standards](settings.md) and [Security](security.md). Do not add unrelated items to limited diagnosis; comprehensive diagnosis retains all five items and free features.
5. Check all API pages, needed detail, and UI, recording retrieval time, evidence URLs, and targets. Separate file declarations from effective GitHub settings, and enabled settings from successful execution.

Choose GitHub integrations, `gh api`, or official UI explicitly supporting necessary operations in the environment. GET-only integrations are not update APIs; do not claim unavailable admin APIs/CLIs executed. Check official authentication, API versions, and required parameters; use minimal existing permissions. Do not expose credentials in bodies/logs or bypass authentication/additional permissions.[^repository-api][^rules-api][^actions-permissions-api]

## Judgment and reporting

For each item record expected/current values, evidence, judgment, proposals, permissions/cost/side effects, and rechecking. No large custom score or dedicated format is required, but preserve these distinctions.

| Judgment | Meaning |
| --- | --- |
| Conforming | Confirmed effective settings meet expectations |
| Needs change | Confirmed evidence-based differences |
| Inapplicable | Confirmed reasons such as no target language |
| Unavailable | Confirmed reasons such as outside free scope or unsupported plans |
| Unverified | Permissions, retrieval failures, unknown costs, or similar gaps prevent judgment |
| Approved exception | Difference from standards with target, reason, approver, and approval evidence recorded |

Do not uniformly interpret 403/404, absent fields, or null as disabled. Even where disabled settings return 404, first independently establish target existence/permissions; remain unverified until permission deficiencies and similar alternatives are excluded. Do not replace unreturned bypass lists with empty arrays.[^repository-api][^rules-api]

Do not count exceptions, inapplicable, or unverified items as conforming. Separate completed diagnosis presentation from realization of all standards. Saving Issues/documents and execution approval are separate; stop by [Skill deliverable paths](../SKILL.md).

## Apply approved settings

1. Save/verify purpose, differences, permissions, costs, effects, validation, and approval through ordinary `issue-management` planning. Inherit confirmed plans/approval without asking again. Hold affected operations until target-policy conflicts, added permissions/costs, or scope changes are resolved.
2. Minimally preserve readable settings as before-state evidence. Retrieve immediately before writes; reassess unexpected differences/other changes. Do not assume atomic comparisons/bulk updates.
3. Complete prerequisites first. For Action pinning, release procedures, existing CI consistency, or other file changes, use responsible Skills and `change-delivery` through PR/review/CI/main verification. Hold enforcement where execution-path effects remain unverified.
4. Apply settings-only changes here without empty branches/commits/PRs; record differences/results in plans. Do not call everything settings changes to bypass necessary file-change PRs.
5. Apply minimal differences from [Item procedures](settings.md) or [Feature procedures](security.md). Do not mix unrelated defaults into PATCH; for PUT check writable required fields and existing content to preserve. Do not PUT entire GET responses.
6. Retrieve each setting and compare necessary behavior/analysis/workflow results to target SHAs/run URLs. Verify asynchronous completion, not acceptance alone. Do not perform unrequested release, deployment, or destructive trials merely to confirm enablement.
7. Diagnose again, showing before/after, confirmed effects, remaining mandatory items, exceptions/evidence. Do not claim all applied if items remain incomplete.

Free features still require separate Actions/execution-cost checks. Do not bypass Organization/Enterprise enforcement from repositories; inherited conformance needs no change, while conflicts/gaps require reasons/admin actions. Do not achieve application through new bypasses or weaker protection.

## Idempotency, conflicts, and partial failure

On reruns recreate differences from current settings without unnecessary writes to conforming items. Ruleset names alone do not establish identity; compare IDs, sources, targets, and effective rules. After creation timeouts retrieve saved state before resending, avoiding duplicate Rulesets.

Separate succeeded, unstarted, failed application, and applied-but-unverified items. Independent approved work may proceed, without unexplained retries or blanket success claims. Recovery preserves others' updates/stronger protections; avoid mechanically restoring whole snapshots. Report irreversible effects even after reverting settings, such as published immutable-release constraints.

Without administrative operations, show target repository, permissions, official UI paths, expected values, and post-operation checks. Completed manual-operation requests do not prove changed settings; remain incomplete until retrieval is possible.

[^repository-api]: Repository/security permissions, reads/updates, response meanings.
[^rules-api]: Ruleset inheritance, bypass information, effective rules, updates.
[^actions-permissions-api]: Administrative permissions and Actions permissions read/update contracts.
