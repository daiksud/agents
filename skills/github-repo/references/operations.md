---
type: Instruction
title: Repository setting operations and judgments
description: Proceed from read-only diagnosis through approved differences and revalidation while preserving permission and failure boundaries.
---

## Read-only diagnosis

1. Match user-specified GitHub.com `owner/repo` with retrieved repository ID, full name, and URL. Do not resolve omissions/ambiguity by operating on another repository. Replace subsequent endpoint `{owner}`, `{repo}`, and `{ruleset_id}` with confirmed values.
2. Check requested deliverables/approval scope. Diagnosis uses only GET/UI reading, without Issue posts, test pushes, workflow starts, or setting changes.
3. Investigate target instructions, visibility, ownership, default branch, permissions, and upper-level policies. Metadata alone does not prove administrative authority.
4. Select expected values/observations from [Setting standards](settings.md) and [Security](security.md). Do not add unrelated items to limited diagnosis; comprehensive diagnosis retains all five items and free features.
5. Check all API pages, needed detail, and UI, recording retrieval time, evidence URLs, and targets. Separate file declarations from effective GitHub settings, and enabled settings from successful execution.

Choose GitHub integrations, `gh api`, or official UI explicitly supporting necessary operations in the environment. GET-only integrations are not update APIs; do not claim unavailable admin APIs/CLIs executed. Check official authentication, API versions, and required parameters; use minimal existing permissions. Do not expose credentials in bodies/logs or bypass authentication/additional permissions.

For official/UI/API disagreements, preserve confirmed scope and differences without inventing missing specifications or endpoints. Hold affected operations when costs, permissions, or destructive effects remain unverified, even within existing execution approval.

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

Do not uniformly interpret 403/404, absent fields, or null as disabled. Even where disabled settings return 404, first independently establish target existence/permissions; remain unverified until permission deficiencies and similar alternatives are excluded. Do not replace unreturned bypass lists with empty arrays.

Do not count exceptions, inapplicable, or unverified items as conforming. Separate completed diagnosis presentation from realization of all standards. Saving Issues/documents and execution approval are separate; stop by [Skill deliverable paths](../SKILL.md).

## Record plans

Search existing Issues before saving a plan. Record the target repository, requested outcome, observed differences, success conditions, scope, order, permissions/costs, validation, and execution approval. Reuse verified plans and retain prior reasons and requester attribution. Assign new Issues to the confirmed requester and choose existing labels by their meaning.

Follow the target's Issue template and language; use concise English Conventional Commits titles. Keep the purpose and decision evidence understandable in the body without following links. Distinguish planned checks from actual results, preserve existing content when updating, and keep private evidence within its approved publication scope.

Save complete drafts to Markdown files and format/check them with rumdl using the target's applicable configuration. Do not add YAML frontmatter to GitHub bodies or replace configuration without agreement. Inspect formatting changes and confirm a second formatting pass makes no further changes. Publish the checked content through a supported API or body-file option, retrieve it, compare it with the draft, and check headings, lists, tables, and links in GitHub rendering. API HTML inspection is not visual screen inspection. Open a browser only when requested. Report the saved body and URL; failed saving or unverified retrieval remains incomplete.

An Issue or plan alone does not authorize execution. A clear change request retains approval through saving and verification. Continue procedure or file adjustments within the same purpose and success conditions; confirm changes to purpose, acceptance conditions, external impact, permissions, or costs before the affected operation.

## Approved file changes

After the supporting plan is saved and verified, protect existing work and prepare a task branch before editing. Follow the target's document formats, implementation contracts, and validation requirements. Record actual results or `Not run` for discretionary checks; never present unexecuted checks as successful.

Deliver approved file changes through commits, a draft PR, required CI and conflict resolution, ordinary review of the current HEAD, and fixes with renewed checks/review when HEAD changes. Preserve target review and approval requirements. Before merging, confirm current-head review, passing required CI, resolved findings, no conflicts, and healthy main. Merge by a permitted squash or merge-commit method without bypassing protections; preserve the final PR title/body verbatim in the resulting commit. Verify required checks on the actual merged-main SHA, synchronize, and clean up the task branch. Prioritize recovery if main fails; PR-side success is not completion. Honor explicit stop conditions and do not release or deploy without authorization.

## Apply approved settings

1. [Record and verify the plan](#record-plans), including differences, permissions, costs, effects, validation, and approval. Inherit confirmed plans/approval without asking again. Hold affected operations until target-policy conflicts, added permissions/costs, or scope changes are resolved.
2. Minimally preserve readable settings as before-state evidence. Retrieve immediately before writes; reassess unexpected differences/other changes. Do not assume atomic comparisons/bulk updates.
3. Complete prerequisites first. For Action pinning, release procedures, existing CI consistency, or other file changes, follow [Approved file changes](#approved-file-changes) through PR/review/CI/main verification. Hold enforcement where execution-path effects remain unverified.
4. Apply settings-only changes here without empty branches/commits/PRs; record differences/results in plans. Do not call everything settings changes to bypass necessary file-change PRs.
5. Apply minimal differences from [Item procedures](settings.md) or [Feature procedures](security.md). Do not mix unrelated defaults into PATCH; for PUT check writable required fields and existing content to preserve. Do not PUT entire GET responses.
6. Retrieve each setting and compare necessary behavior/analysis/workflow results to target SHAs/run URLs. Verify asynchronous completion, not acceptance alone. Do not perform unrequested release, deployment, or destructive trials merely to confirm enablement.
7. Diagnose again, showing before/after, confirmed effects, remaining mandatory items, exceptions/evidence. Do not claim all applied if items remain incomplete.

Free features still require separate Actions/execution-cost checks. Do not bypass Organization/Enterprise enforcement from repositories; inherited conformance needs no change, while conflicts/gaps require reasons/admin actions. Do not achieve application through new bypasses or weaker protection.

## Idempotency, conflicts, and partial failure

On reruns recreate differences from current settings without unnecessary writes to conforming items. Ruleset names alone do not establish identity; compare IDs, sources, targets, and effective rules. After creation timeouts retrieve saved state before resending, avoiding duplicate Rulesets.

Separate succeeded, unstarted, failed application, and applied-but-unverified items. Independent approved work may proceed, without unexplained retries or blanket success claims. Recovery preserves others' updates/stronger protections; avoid mechanically restoring whole snapshots. Report irreversible effects even after reverting settings, such as published immutable-release constraints.

Without administrative operations, show target repository, permissions, official UI paths, expected values, and post-operation checks. Completed manual-operation requests do not prove changed settings; remain incomplete until retrieval is possible.
