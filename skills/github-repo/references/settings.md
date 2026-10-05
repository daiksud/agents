---
type: Instruction
title: GitHub repository setting standards
description: Define expected values and diagnosis for releases, merges, main protection, and Actions policy.
sources:
  - id: personal-policy
    resource: https://github.com/daiksud/agents/issues/152
  - id: release-setting
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
  - id: immutable-release
    resource: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: ruleset-rules
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: code-owners
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  - id: copilot-code-review
    resource: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
  - id: approval-code-owner-exception
    resource: https://github.com/daiksud/agents/issues/165
  - id: actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
---

## Applying standards

These expectations are personal adoption policy, not mandatory specifications for all GitHub users. Separate expected/observed values; follow [Operations and judgments](operations.md) for writes. Diagnose free security per feature in [Separate material](security.md).[^personal-policy]

## Immutable releases

Expect repository release immutability enabled; inspect settings even without releases. Check official UI `Settings` → `General` → `Releases` → `Enable release immutability`; with approval enable and re-display. For APIs check current official read/update support without invented endpoints/fields.[^release-setting]

It applies to future releases; report no retroactivity. Investigate operations assuming post-publication tag/asset updates; if necessary first change to draft creation, all assets attached, then publication. Do not publish merely to validate settings. Check individual immutable display only for approved upcoming releases.[^release-setting][^immutable-release]

Do not migrate through tag/asset deletion/recreation, or confuse reverting settings with undoing published immutable-release restrictions. Do not claim release titles/bodies are uneditable.[^immutable-release]

## Squash-only PR merge

Check three values through `GET /repos/{owner}/{repo}` or `Settings` → `General` → `Pull Requests`.[^repository-api]

| Setting | Expected |
| --- | --- |
| `allow_squash_merge` | `true` |
| `allow_merge_commit` | `false` |
| `allow_rebase_merge` | `false` |

With approval, PATCH only changed values at the same endpoint or UI, then retrieve/check all three. Do not fill absent values with defaults. First check Ruleset/merge-queue compatibility; hold conflicting changes. Do not simultaneously change auto-merge, automatic branch deletion, or commit formats.[^repository-api][^ruleset-rules]

## main Ruleset protection

Expect active branch Rulesets on `refs/heads/main` effectively requiring PRs and preventing deletion/force pushes. Inherited conformance suffices without duplicate repository Rulesets. Legacy branch protection alone does not meet this personal Ruleset standard.[^personal-policy][^ruleset-rules]

1. Check main existence/default branch through `GET /repos/{owner}/{repo}/branches/main` or equivalent. Do not implicitly rename/create/change targets for alternate names, empty repos, or absent main.
2. Fetch all `GET /repos/{owner}/{repo}/rulesets?includes_parents=true` pages and relevant details: target, enforcement, includes/excludes, source, bypass.
3. Fetch all `GET /repos/{owner}/{repo}/rules/branches/main` pages and compare active effective rules. It also returns rules for nonexistent branches, not proof main exists.[^rules-api]
4. Check `pull_request`, `deletion`, `non_fast_forward`, and existing extras; do not miss evaluate/disabled, main exclusion, or unnecessary bypass. Inaccessible bypass information does not establish no exceptions.
5. Add gaps to target-owned Rulesets through `Settings` → `Rules` → `Rulesets` or existing-ID `PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}`. Use new `POST /repos/{owner}/{repo}/rulesets` only when necessary. Preserve out-of-scope conditions, rules, parameters, and exceptions; do not change parent Rulesets.[^rules-api]
6. Retrieve details/effective rules. Initial application excludes deleting legacy protections; leave no protection gap. Do not directly push/delete/force-push main to validate.

Record `required_approving_review_count` and `require_code_owner_review` separately: overall approvals versus applicable Code Owner reviews; one of multiple owners suffices. Do not infer unapproved PRs from settings alone; compare author, applicable CODEOWNERS, review states, and mergeability.[^ruleset-rules][^code-owners]

If the sole applicable Code Owner is the PR author, do not invent other owners/human reviewers because self-approval is impossible. Valid non-owner approval can meet GitHub's effective required count; check approval/mergeability. Enabled Copilot Approvals counted as `APPROVED` may be used. Default comment-only reviews are not approvals, and explicit human-review escalation remains applicable.[^approval-code-owner-exception][^copilot-code-review]

Preserve required checks, approver counts, and CODEOWNERS. Choose new checks from target policy, actual names/issuers/events/success history without blocking nonexistent checks. Enabling CodeQL does not make it mandatory; do not uniformly add unsatisfiable solo approvals, signing, or linear history. Do not add unnecessary bypasses; confirm impact/approval before removing existing exceptions. Record unsupported plans as unavailable without paid upgrades.[^personal-policy][^ruleset-rules]

## Require full SHAs for external Actions

Expect native `Require actions to be pinned to a full-length commit SHA` enabled and workflows conforming, including official Actions and other same-owner repositories. Check `GET /repos/{owner}/{repo}/actions/permissions` `sha_pinning_required` or `Settings` → `Actions` → `General`.[^actions-settings][^actions-permissions-api]

First inspect workflows, local composites, and downstream dependencies, handing fixes to `github-actions`. Pin full SHAs checked against releases; complete approved file PRs/CI/main verification before enforcement. Check active other branches/releases as well as main; unverified paths are not safe.

Apply `PUT /repos/{owner}/{repo}/actions/permissions`, preserving required `enabled` and existing `allowed_actions` from immediate retrieval and setting `sha_pinning_required=true`. Disabled Actions do not justify silent enablement; check reasons/scope. Do not relax allowlists/upper policies. Retrieve settings/workflows afterward.[^actions-permissions-api]

Native settings do not prohibit reusable-workflow tags; diagnose full SHAs separately even when enabled. Do not replace same-repo relative paths with SHAs or confuse container digests with Git references. Use `github-actions` as authoritative implementation policy.[^actions-settings]

[^personal-policy]: Initial five items and existing-protection/scope constraints in Issue #152.
[^release-setting]: Repository enablement and future-release application.
[^immutable-release]: Protected objects, draft-publication steps, existing immutable-release restrictions.
[^repository-api]: Repository retrieval/updates and merge fields.
[^ruleset-rules]: Availability, branch protection, merge rules.
[^rules-api]: Retrieval/updates, inheritance, effective branch rules.
[^code-owners]: CODEOWNERS application, required reviews, multiple-owner approvals.
[^approval-code-owner-exception]: Effective conditions adopted in Issue #165 for sole-owner PR authors.
[^copilot-code-review]: Conditions for enabled Copilot Approve counting toward required approvals.
[^actions-settings]: Native SHA-setting scope and reusable-workflow limits.
[^actions-permissions-api]: Actions permissions reads/updates and required parameters.
