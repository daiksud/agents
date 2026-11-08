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

## PR merge methods

In `Settings` → `General` → `Pull Requests`, allow squash and merge-commit merging, and prohibit rebase merging. For both enabled methods, select `Pull request title and description` as the default message. The corresponding fields in `GET /repos/{owner}/{repo}` and [repository update API](https://docs.github.com/en/rest/repos/repos#update-a-repository) have these expected values:

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

First inspect workflows, local composites, and downstream dependencies. Pin full SHAs checked against releases; complete approved file PRs/CI/main verification before enforcement. Check active other branches/releases as well as main; unverified paths are not safe.

Apply `PUT /repos/{owner}/{repo}/actions/permissions`, preserving required `enabled` and existing `allowed_actions` from immediate retrieval and setting `sha_pinning_required=true`. Disabled Actions do not justify silent enablement; check reasons/scope. Do not relax allowlists/upper policies. Retrieve settings/workflows afterward.

Native settings do not prohibit reusable-workflow tags; diagnose full SHAs separately even when enabled. Do not replace same-repo relative paths with SHAs or confuse container digests with Git references. Preserve the target's workflow behavior, permissions, runtime compatibility, and existing validation when changing dependency references.
