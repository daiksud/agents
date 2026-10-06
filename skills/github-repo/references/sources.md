---
type: Guide
title: Repository setting sources and application decisions
description: Separate GitHub specifications from personal standards and recheck availability, APIs, and costs at execution time.
sources:
  - id: personal-policy
    resource: https://github.com/daiksud/agents/issues/152
  - id: security-features
    resource: https://docs.github.com/en/code-security/getting-started/github-security-features
  - id: advanced-security
    resource: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
  - id: release-setting
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
  - id: immutable-release
    resource: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
  - id: code-scanning-api
    resource: https://docs.github.com/en/rest/code-scanning/code-scanning
---

## Specifications and adoption decisions

Five expectations, single-repository scope, free conditions, and preserving existing protection are personal choices, not universal requirements, other-repository review policy, or purchase instructions.[^personal-policy]

Specification checking date at authoring: 2026-09-28. This proves neither human review, target conformance, nor actual setting-application tests. GitHub Docs change; recheck free scope, availability, APIs, permissions, and UI names at execution time, recording observations in target diagnosis.

## Choose necessary material

| Judgment | Official evidence and reading |
| --- | --- |
| Release settings/impact | Separate enablement/nonretroactivity from tag/asset protection and draft publication. Individual immutability is not repository-setting evidence.[^release-setting][^immutable-release] |
| Merge/security settings | Read API permissions, merge fields, individual security_and_analysis/Dependabot contracts.[^repository-api] |
| main protection | Combine Ruleset detail/effective branch rules; the effective-rule API does not prove existence.[^rules-api] |
| Action SHAs | Compare native scope/reuse exceptions with permissions API required fields.[^actions-settings][^actions-permissions-api] |
| Free security | Read standard lists and product availability per feature; do not generalize public-free features to entire products/private repos.[^security-features][^advanced-security] |
| CodeQL setup/results | Separate default/advanced setup, acceptance, completion, analysis.[^code-scanning-api] |

Bundled material: [Standards](settings.md), [Security](security.md), [Operations](operations.md). Use distributed `github-actions` for workflow implementation rather than duplicating Action/container/runner policy.

For official/UI/API disagreements preserve confirmed scope/differences without filling unverified specifications/endpoints. Unknown costs, permissions, or destructive effects justify holding affected operations even within approval.

[^personal-policy]: Issue #152 purposes, standards, acceptance conditions.
[^release-setting]: Repository release-immutability enablement.
[^immutable-release]: Post-publication protected objects and publication steps.
[^repository-api]: Repository/security REST APIs.
[^rules-api]: Ruleset/effective branch-rule REST APIs.
[^actions-settings]: SHA-setting scope/limits.
[^actions-permissions-api]: Actions permissions REST API.
[^security-features]: GitHub security-feature list.
[^advanced-security]: Product composition/availability.
[^code-scanning-api]: Code scanning configuration/execution REST API.
