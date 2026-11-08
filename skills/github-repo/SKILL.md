---
name: github-repo
description: Use to diagnose, maintain, or apply GitHub repository settings. Covers immutable releases, squash and merge-commit methods, PR-based commit messages, main Rulesets, required Actions SHAs, and free security features. Do not use for ordinary Issue/PR operations, workflow-content-only fixes, or general GitHub explanation.
---

# Diagnose and realize GitHub repository settings

Compare personal setting standards with the target repository's effective settings, and realize only the requested scope. The initial version targets one specified repository on GitHub.com. Repositories, branches, and settings below refer to the working target, not the distribution source.

## Entry and responsibilities

Check the complete target `owner/repo`, requested deliverable, execution approval, and target repository policy. APM installation or a diagnosis request does not approve setting changes. Do not impose personal standards on external reviewers as another repository's review policy; present differences and options for policy conflicts.

| Requested deliverable | Path and endpoint |
| --- | --- |
| Answer with diagnosis, comparison, or improvement proposals | Read only, report evidence, judgments, and uncertainties, then stop. Do not start Issue posting or setting changes |
| Issue record of a plan or diagnosis only | [Record the plan](references/operations.md#record-plans), retrieve it, check agreement and display, present the body and URL, then stop. Settings remain unapplied |
| Save a diagnosis document | Save the requested report in the target's format and language. Deliver Git-managed documents through [Approved file changes](references/operations.md#approved-file-changes), without applying settings |
| Apply or correct settings | Retain approval in a saved and verified plan, and use [Application procedure](references/operations.md#apply-approved-settings) through applying differences and diagnosing again. Do not stop at plan presentation |

Do not create empty commits or PRs for settings-only changes. Deliver prerequisite workflows, documents, or implementation files through the approved file-change path before enforcing dependent settings. If required access or operations are unavailable, hold the affected operation and state incomplete scope while continuing possible reading. Do not obtain existing execution approval or verified plans again.

## Material to read at each stage

For diagnosis, first read the reading/reporting parts of [Operations and judgments](references/operations.md). Add only target items, without always loading all unrelated material.

| Condition | Reference material |
| --- | --- |
| Narrow PR-title/body merge-message alignment diagnosis or authorized application | [PR and merge message alignment](references/settings.md#pr-and-merge-message-alignment); do not expand to unrelated standards |
| Releases, merges, main protection, Actions policy | [Setting standards](references/settings.md) |
| Free security features, availability, billing, prerequisites | [Security](references/security.md) |
| Retrieving settings, applying differences, failures, conflicts, reruns, result verification | [Operations and judgments](references/operations.md) |

For version-dependent judgments, recheck current official specifications for APIs, feature availability, free-use conditions, permissions, and UI names. Record observations in the target diagnosis; historical checks do not establish current applicability.

## Common boundaries

- Investigate public/private visibility, personal/Organization ownership, default branch, permissions, and higher-level policies. Do not replace inaccessible, missing, or unsupported fields with “disabled” or “conforming.”
- Preserve stronger existing protection, required checks, and approval requirements. Do not fix particular Ruleset IDs, check names, or reviewers at distribution destinations.
- Organization-, Enterprise-, or account-wide changes, visibility changes, permission escalation, and starting paid subscriptions or trials are out of scope. Hold operations where costs are unverified.
- Do not include unrelated improvements, bulk vulnerability fixes, dismissing alerts, or automatic merging of fix PRs. Enabling free features and making them merge requirements are separate decisions.
- Preserve evidence before and after application, and judge through retrieval and necessary behavior checks. Distinguish successful, incomplete, inapplicable, and approved exceptions; API success alone is not completion.
