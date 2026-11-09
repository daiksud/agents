---
type: Instruction
title: GitHub repository setting standards
description: Define required and recommended values for releases, pull requests, branch protection, and Actions policy.
---

## Contents

- [Applying standards](#applying-standards)
- [Immutable releases](#immutable-releases)
- [PR merge methods](#pr-merge-methods)
- [PR and merge message alignment](#pr-and-merge-message-alignment)
- [PR branch maintenance](#pr-branch-maintenance)
- [Branch Ruleset protection](#branch-ruleset-protection)
- [Required checks and fresh approvals](#required-checks-and-fresh-approvals)
- [Actions dependency policies](#actions-dependency-policies)
- [Default workflow permissions](#default-workflow-permissions)

## Applying standards

Use the MUST/SHOULD meanings in the entry point. Separate expected and observed values; follow [Operations and judgments](operations.md) for writes. Diagnose security per feature in [Security](security.md), and complete prerequisite [repository files](repository-files.md) or [Actions locking](actions-lock.md) before dependent enforcement.

## Immutable releases

**MUST:** Enable release immutability to prevent replacement of published release tags and assets. Inspect settings even without releases. Check official UI `Settings` → `General` → `Releases` → `Enable release immutability`; with approval enable and re-display. For APIs check current official read/update support without invented endpoints/fields.

It applies to future releases; report no retroactivity. Investigate operations assuming post-publication tag/asset updates; if necessary first change to draft creation, all assets attached, then publication. Do not publish merely to validate settings. Check individual immutable display only for approved upcoming releases.

Do not migrate through tag/asset deletion/recreation, or confuse reverting settings with undoing published immutable-release restrictions. Do not claim release titles/bodies are uneditable.

## PR merge methods

**SHOULD:** Preserve PR decision records by allowing squash and merge-commit merging, prohibiting rebase merging, and selecting `Pull request title and description` for both enabled methods in `Settings` → `General` → `Pull Requests`. Respect an explicitly adopted narrower merge policy. The corresponding fields in `GET /repos/{owner}/{repo}` and [repository update API](https://docs.github.com/en/rest/repos/repos#update-a-repository) have these expected values:

| Field | Expected value |
| --- | --- |
| `allow_squash_merge` | `true` |
| `allow_merge_commit` | `true` |
| `allow_rebase_merge` | `false` |
| `squash_merge_commit_title` | `PR_TITLE` |
| `squash_merge_commit_message` | `PR_BODY` |
| `merge_commit_title` | `PR_TITLE` |
| `merge_commit_message` | `PR_BODY` |

Compare repository settings with effective branch rules and any merge queue. Required linear history prevents merge commits; allowed merge methods must agree across the repository and target ruleset. Include these related differences when adoption of both methods is requested. Apply only the requested scope, preserve unrelated protections, and retrieve the resulting settings. Do not fill absent values with defaults.

## PR and merge message alignment

Use this narrow path for message-format diagnosis or application. Inspect all four squash/merge title/body fields against `PR_TITLE` / `PR_BODY` in the [setting table](#pr-merge-methods). Missing fields remain unverified. Message-format-only requests do not authorize unrelated merge-method or protection changes.

Keep the final title/body self-contained, aligned with the reviewed change, and free of HTML comments. Respect the agreed language; never translate or summarize away the record at merge. For template and instruction edits, inspect existing rules, preserve equivalent local headings, and deliver only approved differences through [Approved file changes](operations.md#approved-file-changes).

For diagnosis, report exact differences. For authorized application, use [Apply approved settings](operations.md#apply-approved-settings): send only approved fields with `PATCH /repos/{owner}/{repo}`, including the corresponding title field when setting a message field, then retrieve them with `GET /repos/{owner}/{repo}`. These are editable defaults: during delivery retrieve the final PR title, body, and HEAD immediately before merge, pass them as `commit_title`, `commit_message`, and `sha` to the [merge API](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request), and compare the resulting commit's subject/body with that record. Installation of the skill alone does not change settings.

## PR branch maintenance

**SHOULD:** Enable `Always suggest updating pull request branches` under `Settings` → `General` → `Pull Requests` to make base-branch updates visible. Read and update `allow_update_branch` through the repository API, then retrieve it. The suggestion does not synchronize branches, rerun tests, or prevent merging a stale branch; assess those requirements separately below.

**SHOULD:** Enable `Automatically delete head branches` (`delete_branch_on_merge=true`) when merged work branches have no ongoing purpose. Respect persistent-branch workflows and branch protections. Retrieve the setting; do not merge or delete a test branch just to demonstrate it.

## Branch Ruleset protection

**MUST:** Protect the integration branch with active Rulesets requiring PRs and preventing deletion and force pushes. Use the requested integration branch, otherwise the confirmed default branch. Inherited conformance suffices without duplicate repository Rulesets. Preserve legacy protection while adding an applicable Ruleset; unavailable plans remain unavailable without upgrades.

1. Check the branch exists through `GET /repos/{owner}/{repo}/branches/{branch}` or equivalent. Do not implicitly rename/create/change targets for alternate names or empty repositories.
2. Fetch all `GET /repos/{owner}/{repo}/rulesets?includes_parents=true` pages and relevant details: target, enforcement, includes/excludes, source, bypass.
3. Fetch all `GET /repos/{owner}/{repo}/rules/branches/{branch}` pages and compare active effective rules. It also returns rules for nonexistent branches, not proof the target exists.
4. Check `pull_request`, `deletion`, `non_fast_forward`, and existing extras; do not miss evaluate/disabled, target exclusions, or unnecessary bypass. Inaccessible bypass information does not establish no exceptions.
5. Add gaps to target-owned Rulesets through `Settings` → `Rulesets` or existing-ID `PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}`. Use new `POST /repos/{owner}/{repo}/rulesets` only when necessary. Preserve out-of-scope conditions, rules, parameters, and exceptions; do not change parent Rulesets.
6. Retrieve details/effective rules. Initial application excludes deleting legacy protections; leave no protection gap. Do not directly push/delete/force-push the protected branch to validate.

Record `required_approving_review_count` and `require_code_owner_review` separately: overall approvals versus applicable Code Owner reviews; one of multiple owners suffices. Do not infer unapproved PRs from settings alone; compare author, applicable CODEOWNERS, review states, and mergeability.

If the sole applicable Code Owner is the PR author, do not invent other owners/human reviewers because self-approval is impossible. Valid non-owner approval can meet GitHub's effective required count; check approval/mergeability. Enabled Copilot Approvals counted as `APPROVED` may be used. Default comment-only reviews are not approvals, and explicit human-review escalation remains applicable.

Preserve required checks, approver counts, and CODEOWNERS. Choose new checks from target policy, actual names/issuers/events/success history without blocking nonexistent checks. Enabling CodeQL does not make it mandatory; do not uniformly add unsatisfiable solo approvals, signing, or linear history. Do not add unnecessary bypasses; confirm impact/approval before removing existing exceptions. Record unsupported plans as unavailable without paid upgrades.

## Required checks and fresh approvals

**MUST, when the repository uses CI:** Configure the agreed checks under the branch Ruleset's required status checks. Confirm actual check names, expected source Apps, relevant PR events, and successful runs before enforcing them. If no suitable check exists, report the prerequisite; do not invent a check name. A skipped/neutral status can satisfy GitHub's status rule, so inspect whether the existing check actually covers the intended work.

**MUST, when using required checks:** Require the branch to be up to date before merging (`strict_required_status_checks_policy=true`), or preserve an existing merge queue that validates the current base plus queued changes. Strict mode needs at least one configured required check to have an effect. Do not enable a queue without compatible `merge_group` checks. Enabling the update suggestion alone does not satisfy this rule.

**SHOULD, when approval is required:** Prevent old approvals from silently covering new changes by dismissing stale approvals or requiring approval of the latest reviewable push. Choose a viable policy for the actual reviewers, preserve stronger requirements, and retrieve effective rules afterward. Code Owner requirements also depend on the [target's CODEOWNERS](repository-files.md).

## Actions dependency policies

**MUST, when Actions is used:** Adopt `gh actions-lock` through [Actions locking](actions-lock.md), and enable native `Require actions to be pinned to a full-length commit SHA` in `Settings` → `Actions` → `General`. A valid lockfile satisfies this policy for locked Actions; readable tag references do not need redundant literal-SHA rewrites. External reusable-workflow call references are not locked and need separate full-SHA pinning.

Check `GET /repos/{owner}/{repo}/actions/permissions` `sha_pinning_required` or the UI. Complete prerequisite file PRs and checks before enforcement; examine active branches and called workflows as well as the default branch. Unverified execution paths are not ready for enforcement. Disabled Actions do not justify silent enablement.

Apply `PUT /repos/{owner}/{repo}/actions/permissions`, preserving required `enabled` and existing `allowed_actions` from immediate retrieval and setting `sha_pinning_required=true`. Do not relax allowlists or upper-level policies. Retrieve settings/workflows afterward. Native SHA enforcement does not cover reusable-workflow call references or prove lockfile coverage.

**SHOULD, after lockfile adoption:** Enable `Require lockfile` for the intended workflows through `Settings` → `Actions` → `Policies`. Check feature availability and existing policy targets. Confirm every targeted workflow and called source workflow has been onboarded before making the policy Active; a workflow without Action dependencies still needs onboarding. This policy is separate from SHA enforcement. Retrieve policy scope/enforcement and verify affected runs without disabling either policy to hide a failure.

## Default workflow permissions

**MUST, when Actions is used:** Set `Settings` → `Actions` → `General` → `Workflow permissions` to read repository contents and packages, reducing default `GITHUB_TOKEN` privileges. This is a default, not a maximum: workflow/job `permissions` can grant more. Inspect actual needs and make any necessary explicit permissions changes before restricting a workflow that relies on the old default.

Read `GET /repos/{owner}/{repo}/actions/permissions/workflow`; set `default_workflow_permissions=read` through the corresponding `PUT`, preserving the separate approval setting and unrelated behavior. Retrieve the result. Do not treat the repository default as proof that every job has minimal permissions.
