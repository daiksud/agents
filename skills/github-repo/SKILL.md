---
name: github-repo
description: Use to diagnose, maintain, or apply GitHub repository settings. Covers immutable releases, squash-only merges, main Rulesets, required Actions SHAs, and free security features. Do not use for ordinary Issue/PR operations, workflow-content-only fixes, or general GitHub explanation.
---

# Diagnose and realize GitHub repository settings

Compare personal setting standards with the target repository's effective settings, and realize only the requested scope. The initial version targets one specified repository on GitHub.com. Repositories, branches, and settings below refer to the working target, not the distribution source.

## Entry and responsibilities

Check the complete target `owner/repo`, requested deliverable, execution approval, and target repository policy. APM installation or a diagnosis request does not approve setting changes. Do not impose personal standards on external reviewers as another repository's review policy; present differences and options for policy conflicts.

| Requested deliverable | Path and endpoint |
| --- | --- |
| Answer with diagnosis, comparison, or improvement proposals | Read only, report evidence, judgments, and uncertainties, then stop. Do not start Issue posting or setting changes |
| Issue record of a plan or diagnosis only | Use `issue-management` to save, retrieve, and check display, present the body and URL, then stop. Settings remain unapplied |
| Save a diagnosis document | Use `document-authoring`. For Git-managed files, deliver the document through a supporting Issue plan and `change-delivery`, without applying settings |
| Apply or correct settings | Retain approval in an ordinary `issue-management` plan, and use [Application procedure](references/operations.md) through applying differences and diagnosing again. Do not stop at plan presentation |

Do not create empty commits or PRs for settings-only changes. Hand prerequisite workflows or other files to `github-actions` and `change-delivery`, documents to `document-authoring`, and implementation code to `software-development`. If necessary dependencies are unavailable, stop that operation and state incomplete scope while continuing possible reading. Do not obtain existing execution approval or verified plans again.

## Material to read at each stage

For diagnosis, first read the reading/reporting parts of [Operations and judgments](references/operations.md). Add only target items, without always loading all unrelated material.

| Condition | Reference material |
| --- | --- |
| Releases, merges, main protection, Actions policy | [Setting standards](references/settings.md) |
| Free security features, availability, billing, prerequisites | [Security](references/security.md) |
| Retrieving settings, applying differences, failures, conflicts, reruns, result verification | [Operations and judgments](references/operations.md) |
| Rechecking specifications, adoption reasons, APIs, or free-use conditions | [Sources and application decisions](references/sources.md) |

## Common boundaries

- Investigate public/private visibility, personal/Organization ownership, default branch, permissions, and higher-level policies. Do not replace inaccessible, missing, or unsupported fields with “disabled” or “conforming.”
- Preserve stronger existing protection, required checks, and approval requirements. Do not fix particular Ruleset IDs, check names, or reviewers at distribution destinations.
- Organization-, Enterprise-, or account-wide changes, visibility changes, permission escalation, and starting paid subscriptions or trials are out of scope. Hold operations where costs are unverified.
- Do not include unrelated improvements, bulk vulnerability fixes, dismissing alerts, or automatic merging of fix PRs. Enabling free features and making them merge requirements are separate decisions.
- Preserve evidence before and after application, and judge through retrieval and necessary behavior checks. Distinguish successful, incomplete, inapplicable, and approved exceptions; API success alone is not completion.
