---
type: Reference
title: GitHub repository sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the github-repo skill.
sources:
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
  - id: security-features
    resource: https://docs.github.com/en/code-security/getting-started/github-security-features
  - id: advanced-security
    resource: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
  - id: code-scanning-api
    resource: https://docs.github.com/en/rest/code-scanning/code-scanning
  - id: personal-policy
    resource: https://github.com/daiksud/agents/issues/152
  - id: release-setting
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
  - id: immutable-release
    resource: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
  - id: ruleset-rules
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: code-owners
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  - id: copilot-code-review
    resource: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
  - id: approval-code-owner-exception
    resource: https://github.com/daiksud/agents/issues/165
  - id: actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: repository-adoption
    resource: https://github.com/daiksud/agents/issues/254
---

## Scope

Maintainer reference for [github-repo](../../skills/github-repo/SKILL.md). These records explain source provenance and adoption history. Execution procedures and decision-relevant details remain in the skill and its task-specific references; ordinary execution does not require this document.

Checking dates below are historical records retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Source mapping

The following mapping preserves the original source IDs and annotation scope for each runtime document and former source catalog.

### Repository setting operations and judgments

Runtime material: [operations.md](../../skills/github-repo/references/operations.md).

| Source | Original annotation scope |
| --- | --- |
| [^repository-api] | Repository/security permissions, reads/updates, response meanings. |
| [^rules-api] | Ruleset inheritance, bypass information, effective rules, updates. |
| [^actions-permissions-api] | Administrative permissions and Actions permissions read/update contracts. |

### Diagnosing and enabling free security features

Runtime material: [security.md](../../skills/github-repo/references/security.md).

| Source | Original annotation scope |
| --- | --- |
| [^security-features] | Standard free/product feature lists; check changes/additions at execution time. |
| [^advanced-security] | Code Security/Secret Protection boundaries and availability. |
| [^repository-api] | Retrieval/application conditions for security_and_analysis and Dependabot settings. |
| [^code-scanning-api] | Default setup retrieval/update and scan results. |

### GitHub repository setting standards

Runtime material: [settings.md](../../skills/github-repo/references/settings.md).

| Source | Original annotation scope |
| --- | --- |
| [^personal-policy] | Initial five items and existing-protection/scope constraints in Issue #152. |
| [^release-setting] | Repository enablement and future-release application. |
| [^immutable-release] | Protected objects, draft-publication steps, existing immutable-release restrictions. |
| [^repository-api] | Repository retrieval/updates and merge fields. |
| [^ruleset-rules] | Availability, branch protection, merge rules. |
| [^rules-api] | Retrieval/updates, inheritance, effective branch rules. |
| [^code-owners] | CODEOWNERS application, required reviews, multiple-owner approvals. |
| [^approval-code-owner-exception] | Effective conditions adopted in Issue #165 for sole-owner PR authors. |
| [^copilot-code-review] | Conditions for enabled Copilot Approve counting toward required approvals. |
| [^actions-settings] | Native SHA-setting scope and reusable-workflow limits. |
| [^actions-permissions-api] | Actions permissions reads/updates and required parameters. |

### Repository setting sources and application decisions

Former source catalog: `skills/github-repo/references/sources.md`. Its adoption and checking records are preserved below.

| Source | Original annotation scope |
| --- | --- |
| [^personal-policy] | Issue #152 purposes, standards, acceptance conditions. |
| [^release-setting] | Repository release-immutability enablement. |
| [^immutable-release] | Post-publication protected objects and publication steps. |
| [^repository-api] | Repository/security REST APIs. |
| [^rules-api] | Ruleset/effective branch-rule REST APIs. |
| [^actions-settings] | SHA-setting scope/limits. |
| [^actions-permissions-api] | Actions permissions REST API. |
| [^security-features] | GitHub security-feature list. |
| [^advanced-security] | Product composition/availability. |
| [^code-scanning-api] | Code scanning configuration/execution REST API. |

## Adoption and previous checking records

### Specifications and adoption decisions

Five expectations, single-repository scope, free conditions, and preserving existing protection are personal choices, not universal requirements, other-repository review policy, or purchase instructions.[^personal-policy]

Specification checking date at authoring: 2026-09-28. This proves neither human review, target conformance, nor actual setting-application tests. GitHub Docs change; recheck free scope, availability, APIs, permissions, and UI names at execution time, recording observations in target diagnosis.

### Choose necessary material

| Judgment | Official evidence and reading |
| --- | --- |
| Release settings/impact | Separate enablement/nonretroactivity from tag/asset protection and draft publication. Individual immutability is not repository-setting evidence.[^release-setting][^immutable-release] |
| Merge/security settings | Read API permissions, merge fields, individual security_and_analysis/Dependabot contracts.[^repository-api] |
| main protection | Combine Ruleset detail/effective branch rules; the effective-rule API does not prove existence.[^rules-api] |
| Action SHAs | Compare native scope/reuse exceptions with permissions API required fields.[^actions-settings][^actions-permissions-api] |
| Free security | Read standard lists and product availability per feature; do not generalize public-free features to entire products/private repos.[^security-features][^advanced-security] |
| CodeQL setup/results | Separate default/advanced setup, acceptance, completion, analysis.[^code-scanning-api] |

Bundled material: [Standards](../../skills/github-repo/references/settings.md), [Security](../../skills/github-repo/references/security.md), [Operations](../../skills/github-repo/references/operations.md). Use distributed `github-actions` for workflow implementation rather than duplicating Action/container/runner policy.

For official/UI/API disagreements preserve confirmed scope/differences without filling unverified specifications/endpoints. Unknown costs, permissions, or destructive effects justify holding affected operations even within approval.

[^repository-api]: [repository-api](https://docs.github.com/en/rest/repos/repos).
[^rules-api]: [rules-api](https://docs.github.com/en/rest/repos/rules).
[^actions-permissions-api]: [actions-permissions-api](https://docs.github.com/en/rest/actions/permissions).
[^security-features]: [security-features](https://docs.github.com/en/code-security/getting-started/github-security-features).
[^advanced-security]: [advanced-security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security).
[^code-scanning-api]: [code-scanning-api](https://docs.github.com/en/rest/code-scanning/code-scanning).
[^personal-policy]: [personal-policy](https://github.com/daiksud/agents/issues/152).
[^release-setting]: [release-setting](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes).
[^immutable-release]: [immutable-release](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).
[^ruleset-rules]: [ruleset-rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).
[^code-owners]: [code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
[^approval-code-owner-exception]: [approval-code-owner-exception](https://github.com/daiksud/agents/issues/165).
[^copilot-code-review]: [copilot-code-review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review).
[^actions-settings]: [actions-settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

## Consumer change-record adoption

[Issue #254](https://github.com/daiksud/agents/issues/254) adds a narrow [squash-message setting path](../../skills/github-repo/references/settings.md#pr-and-squash-message-alignment) for `PR_TITLE` / `PR_BODY`.[^repository-adoption] Diagnosis and authorized application remain separate; other merge, CI, security, and protection settings are preserved. Consumer template, instruction, and policy edits stay with [repository adoption](../../skills/change-delivery/references/repository-adoption.md) in ordinary change delivery. The [GitHub repository API](https://docs.github.com/en/rest/repos/repos#update-a-repository) documents the fields and requires the title field when setting the message field; this documentation change applies no live settings.

[^repository-adoption]: Owner-requested adoption guidance and scope in Issue #254; builds on Issue #253 rather than replacing its reusable template or Engineering Policies authoring reference.
