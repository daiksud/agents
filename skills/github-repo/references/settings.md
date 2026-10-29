---
type: Instruction
title: GitHub repository setting standards
description: Define expected values and diagnosis for releases, merges, main protection, and Actions policy.
---

## Applying standards

These expectations are personal adoption policy, not mandatory specifications for all GitHub users. Separate expected/observed values; follow [Operations and judgments](operations.md) for writes. Diagnose free security per feature in [Separate material](security.md).

## Immutable releases

Expect repository release immutability enabled; inspect settings even without releases. Check official UI `Settings` → `General` → `Releases` → `Enable release immutability`; with approval enable and re-display. For APIs check current official read/update support without invented endpoints/fields.

It applies to future releases; report no retroactivity. Investigate operations assuming post-publication tag/asset updates; if necessary first change to draft creation, all assets attached, then publication. Do not publish merely to validate settings. Check individual immutable display only for approved upcoming releases.

Do not migrate through tag/asset deletion/recreation, or confuse reverting settings with undoing published immutable-release restrictions. Do not claim release titles/bodies are uneditable.

## Squash-only PR merge

Check three values through `GET /repos/{owner}/{repo}` or `Settings` → `General` → `Pull Requests`.

| Setting | Expected |
| --- | --- |
| `allow_squash_merge` | `true` |
| `allow_merge_commit` | `false` |
| `allow_rebase_merge` | `false` |

With approval, PATCH only changed values at the same endpoint or UI, then retrieve/check all three. Do not fill absent values with defaults. First check Ruleset/merge-queue compatibility; hold conflicting changes. Do not simultaneously change auto-merge, automatic branch deletion, or commit formats.

## PR and squash message alignment

Use this narrow path when change-record adoption requests diagnosis or application of squash-message defaults. Installation or ordinary development alone does not authorize settings changes. Target-repository template, instruction, and policy edits belong to `change-delivery`, following [Repository adoption](../../change-delivery/references/repository-adoption.md).

1. Follow the reading/reporting steps in [Operations and judgments](operations.md) for the exact repository and scope. Retrieve `GET /repos/{owner}/{repo}` and compare `squash_merge_commit_title` with `PR_TITLE` and `squash_merge_commit_message` with `PR_BODY`. Missing/inaccessible fields remain unverified, not assumed defaults. Check whether squash merging is available; do not silently enable it or alter merge methods.
2. Confirm the final English title and agreed PR-body language are recorded locally. Propose English PR bodies for repositories adopting verbatim squash records; surface explicit local conflicts before applying the choice. Keep the final title/body comment-free and retain their full rationale and actual validation status.
3. For diagnosis-only scope, report observed/expected values and concrete differences, then stop. For authorized settings application, follow the saved-plan, permission, prerequisite, and immediate-before-write checks in [Apply approved settings](operations.md#apply-approved-settings).
4. PATCH only the authorized message-format differences at `/repos/{owner}/{repo}`; include `squash_merge_commit_title: PR_TITLE` when setting `squash_merge_commit_message: PR_BODY`, as required by the API. Preserve other merge methods, auto-merge, branch deletion, CI, security, and protection settings. Do not apply the broader squash-only or other setting standards as part of this narrow request.
5. Retrieve both fields again and compare with the expected values; report successful, failed, or unverified results. API acceptance alone is not verification. These defaults do not prove a merge retained the record: ordinary delivery still checks the final description and actual squash message without authoring comments or last-minute translation.

Recheck the current [GitHub repository API](https://docs.github.com/en/rest/repos/repos#update-a-repository) before version-dependent operations. No live merge or settings mutation is needed merely to validate this guidance.

## main Ruleset protection

Expect active branch Rulesets on `refs/heads/main` effectively requiring PRs and preventing deletion/force pushes. Inherited conformance suffices without duplicate repository Rulesets. Legacy branch protection alone does not meet this personal Ruleset standard.

1. Check main existence/default branch through `GET /repos/{owner}/{repo}/branches/main` or equivalent. Do not implicitly rename/create/change targets for alternate names, empty repos, or absent main.
2. Fetch all `GET /repos/{owner}/{repo}/rulesets?includes_parents=true` pages and relevant details: target, enforcement, includes/excludes, source, bypass.
3. Fetch all `GET /repos/{owner}/{repo}/rules/branches/main` pages and compare active effective rules. It also returns rules for nonexistent branches, not proof main exists.
4. Check `pull_request`, `deletion`, `non_fast_forward`, and existing extras; do not miss evaluate/disabled, main exclusion, or unnecessary bypass. Inaccessible bypass information does not establish no exceptions.
5. Add gaps to target-owned Rulesets through `Settings` → `Rules` → `Rulesets` or existing-ID `PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}`. Use new `POST /repos/{owner}/{repo}/rulesets` only when necessary. Preserve out-of-scope conditions, rules, parameters, and exceptions; do not change parent Rulesets.
6. Retrieve details/effective rules. Initial application excludes deleting legacy protections; leave no protection gap. Do not directly push/delete/force-push main to validate.

Record `required_approving_review_count` and `require_code_owner_review` separately: overall approvals versus applicable Code Owner reviews; one of multiple owners suffices. Do not infer unapproved PRs from settings alone; compare author, applicable CODEOWNERS, review states, and mergeability.

If the sole applicable Code Owner is the PR author, do not invent other owners/human reviewers because self-approval is impossible. Valid non-owner approval can meet GitHub's effective required count; check approval/mergeability. Enabled Copilot Approvals counted as `APPROVED` may be used. Default comment-only reviews are not approvals, and explicit human-review escalation remains applicable.

Preserve required checks, approver counts, and CODEOWNERS. Choose new checks from target policy, actual names/issuers/events/success history without blocking nonexistent checks. Enabling CodeQL does not make it mandatory; do not uniformly add unsatisfiable solo approvals, signing, or linear history. Do not add unnecessary bypasses; confirm impact/approval before removing existing exceptions. Record unsupported plans as unavailable without paid upgrades.

## Require full SHAs for external Actions

Expect native `Require actions to be pinned to a full-length commit SHA` enabled and workflows conforming, including official Actions and other same-owner repositories. Check `GET /repos/{owner}/{repo}/actions/permissions` `sha_pinning_required` or `Settings` → `Actions` → `General`.

First inspect workflows, local composites, and downstream dependencies, handing fixes to `github-actions`. Pin full SHAs checked against releases; complete approved file PRs/CI/main verification before enforcement. Check active other branches/releases as well as main; unverified paths are not safe.

Apply `PUT /repos/{owner}/{repo}/actions/permissions`, preserving required `enabled` and existing `allowed_actions` from immediate retrieval and setting `sha_pinning_required=true`. Disabled Actions do not justify silent enablement; check reasons/scope. Do not relax allowlists/upper policies. Retrieve settings/workflows afterward.

Native settings do not prohibit reusable-workflow tags; diagnose full SHAs separately even when enabled. Do not replace same-repo relative paths with SHAs or confuse container digests with Git references. Use `github-actions` as authoritative implementation policy.
