---
name: github-repo
description: Recommend, audit, and configure a GitHub.com repository's Settings and repository-operation files. Use for immutable releases, branch rules, Actions permissions and lockfiles, security features, Dependabot, CODEOWNERS, and Issue/PR templates. Do not use for ordinary Issue/PR administration or complete product-pipeline design.
---

# Configure GitHub repository settings and files

Compare the target repository with the recommended practices, explain applicable differences, and implement the requested changes. Work on one specified GitHub.com repository. Repository paths refer to that target; bundled links refer to this skill's own directory.

Cover repository Settings and configuration or contribution files normally placed under `.github`. Respect equivalent existing files in other supported locations. Include workflow changes needed for these practices, without expanding the request into product-specific build, test, release, or deployment design.

## Requirements and prerequisites

- **MUST** is required for an applicable adopted practice. **SHOULD** is recommended unless the target has a justified reason to differ. These are this skill's adoption rules, not universal GitHub requirements. Report policy conflicts and exceptions; do not override the user's scope or stronger protection.
- Determine applicability from the repository's actual features, plan, ownership, and workflow paths. An unavailable feature or unmet prerequisite is not conformance. State the reason and continue independent work.
- Use an authenticated GitHub integration, GitHub CLI, or supported UI with the permissions needed for the operation. Use Git and the target's delivery tools for file changes. Actions locking additionally needs GitHub CLI and `github/gh-actions-lock`, as described in the bundled guide.
- Keep the bundled references and assets with this file. Installation makes the guidance available; it does not adopt templates, modify Settings, or authorize writes.

## Entry and responsibilities

Check the complete target `owner/repo`, requested deliverable, execution approval, and target repository policy. A diagnosis request does not approve file or setting changes. Do not impose these standards on external reviewers as another repository's review policy; present differences and options for policy conflicts.

| Requested deliverable | Path and endpoint |
| --- | --- |
| Answer with diagnosis, comparison, or improvement proposals | Read only, report evidence, judgments, and uncertainties, then stop. Do not start Issue posting or setting changes |
| Issue record of a plan or diagnosis only | [Record the plan](references/operations.md#record-plans), retrieve it, check agreement and display, present the body and URL, then stop. Settings remain unapplied |
| Save a diagnosis document | Save the requested report in the target's format and language. Deliver Git-managed documents through [Approved file changes](references/operations.md#approved-file-changes), without applying settings |
| Add or refine repository files | Use [Approved file changes](references/operations.md#approved-file-changes), preserving existing content and target delivery requirements. File adoption does not authorize unrelated Settings changes |
| Apply or correct settings and files | Retain approval in the plan, complete prerequisite [file changes](references/operations.md#approved-file-changes), then use [Application procedure](references/operations.md#apply-approved-settings) through applying differences and diagnosing again. Do not stop at plan presentation |

Do not create empty commits or PRs for settings-only changes. Deliver prerequisite workflows, documents, or implementation files through the approved file-change path before enforcing dependent settings. If required access or operations are unavailable, hold the affected operation and state incomplete scope while continuing possible reading. Do not obtain existing execution approval or verified plans again.

## Material to read at each stage

For diagnosis, first read the reading/reporting parts of [Operations and judgments](references/operations.md). Add only target items, without always loading all unrelated material.

| Condition | Reference material |
| --- | --- |
| Narrow PR-title/body merge-message alignment diagnosis or authorized application | [PR and merge message alignment](references/settings.md#pr-and-merge-message-alignment); do not expand to unrelated standards |
| Releases, merges, branch protection, required checks, Actions policy | [Setting standards](references/settings.md) |
| Free security features, availability, billing, prerequisites | [Security](references/security.md) |
| Dependabot, CODEOWNERS, Issue/PR templates, security-reporting policy | [Repository files and bundled templates](references/repository-files.md) |
| Introducing or maintaining Actions dependency lockfiles | [Actions locking](references/actions-lock.md) |
| Retrieving settings, applying differences, failures, conflicts, reruns, result verification | [Operations and judgments](references/operations.md) |

For version-dependent judgments, recheck current official specifications for APIs, feature availability, free-use conditions, permissions, and UI names. Record observations in the target diagnosis; historical checks do not establish current applicability.

## Common boundaries

- Investigate public/private visibility, personal/Organization ownership, default branch, permissions, and higher-level policies. Do not replace inaccessible, missing, or unsupported fields with “disabled” or “conforming.”
- Preserve stronger existing protection, required checks, approval requirements, and equivalent configuration. Do not hard-code branch names, Ruleset IDs, check names, package ecosystems, owners, or reporting contacts for installation destinations.
- Organization-, Enterprise-, or account-wide changes, visibility changes, permission escalation, and starting paid subscriptions or trials are out of scope. Hold operations where costs are unverified.
- Do not include unrelated improvements, bulk vulnerability fixes, dismissing alerts, or automatic merging of fix PRs. Enabling free features and making them merge requirements are separate decisions.
- Preserve evidence before and after application, and judge through retrieval and necessary behavior checks. Distinguish successful, incomplete, inapplicable, and approved exceptions; API success alone is not completion.
