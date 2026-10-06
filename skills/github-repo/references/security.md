---
type: Instruction
title: Diagnosing and enabling free security features
description: Inventory free applicable features for the target repository, checking prerequisites and costs before realization.
sources:
  - id: security-features
    resource: https://docs.github.com/en/code-security/getting-started/github-security-features
  - id: advanced-security
    resource: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: code-scanning-api
    resource: https://docs.github.com/en/rest/code-scanning/code-scanning
---

## Determine free scope per feature

Expect all security features free and applicable to the target repository enabled. Investigate standard free features and free GitHub Code Security/Secret Protection applicability, not bulk `advanced_security` enablement. Public-free does not imply private-free; check ownership, subscriptions, languages, dependency ecosystems, and upper-level policies.[^security-features][^advanced-security]

Compare official lists/UI at execution time, inventorying additions beyond the starting table. Classify each as configurable, enabled by default, needing workflows/prerequisites, inapplicable, outside free scope, or unverified, reflecting [Common judgments](operations.md). Default-enabled status inaccessible for the target is not confirmed conformance. Do not invent APIs/workflows for features without enablement switches.[^security-features]

| Inventory target | Retrieval, application, rechecking |
| --- | --- |
| Dependency graph | Check security settings/graph, status, supported manifests; if configurable enable/recheck. Zero dependencies differs from disabled |
| Dependabot alerts | Check `GET /repos/{owner}/{repo}/vulnerability-alerts` or UI; apply `PUT` to the same endpoint. Interpret HTTP after existence/permissions checks, then retrieve |
| Dependabot security updates | Check `GET /repos/{owner}/{repo}/automated-security-fixes` `enabled`, `paused`, and dependencies; apply same-endpoint `PUT`. Enabled-but-paused is not confirmed executable; show causes/remaining work |
| Secret scanning / repository-level push protection | Check `security_and_analysis.secret_scanning`, `secret_scanning_push_protection`, or UI. Check free conditions/secret-scanning prerequisites; enable only necessary fields through `PATCH /repos/{owner}/{repo}`, then retrieve |
| Code scanning / CodeQL | Check `GET /repos/{owner}/{repo}/code-scanning/default-setup`, workflows, analysis for setup/languages. Only when default setup fits, same-endpoint `PATCH` with `state=configured` or UI; check configuration and actual analysis |
| Copilot Autofix / AI code detection | Check availability, settings, dependencies on existing scans; enable/recheck if free/configurable. Licenses or scan results alone do not establish enablement |
| Dependency review | Check availability and PR dependency diffs; without switches record provision. Merge blocking by dependency-review-action is separate workflow/policy work |
| Additional secret-scanning features | Check UI/official availability for non-provider patterns, validity checks, AI secret detection, custom patterns, delegated bypass, and similar items. Record free/configurable status and operational decisions; omit no available items |
| Other free features | Compare private vulnerability reporting, dependency submission, artifact attestations, and similar items with official/target availability. Separate repository settings, defaults, file changes, account/Organization features |

Use official feature/product lists and API HTTP/response/permission specifications as evidence; the table alone proves neither free scope nor effectiveness.[^security-features][^advanced-security][^repository-api][^code-scanning-api]

## Enablement prerequisites and order

- Separate free licenses from Actions/runner/storage execution costs. Do not start billing/trials; hold unknown additional costs. Do not disable existing paid features merely because outside free scope.
- Meet graph/scanning prerequisites first; retrieve/apply/retrieve per feature without assuming atomic bulk APIs. Do not arbitrarily merge security-update PRs.
- Do not replace existing advanced CodeQL setup with default setup. Check languages, builds, environments; hand workflows to `github-actions`/`change-delivery`. Without supported languages, record reasoned inapplicability without dummy code. Distinguish configured, successful analysis, and zero alerts.[^code-scanning-api]
- Account-level push protection alone does not establish repository settings. Do not change account/Organization-wide settings; record out-of-scope dependencies if needed.[^security-features]
- Present proposals for unagreed exception approvers, patterns, external information transmission, or similar decisions, while continuing independent free features. Do not silently exclude decision-dependent features.
- Do not fabricate SECURITY.md contacts/intake arrangements or empty settings for SBOM/Advisory Database usage features. Do not automatically add version-update cadence, automatic alert dismissal, or mandatory scans to initial standards.

## Completion checks

Show retrieved settings, necessary analysis/workflow results, and default-provision evidence per feature. Read-only diagnosis does not run additional scans, push test secrets, or add simulated vulnerabilities. Do not infer failed/inaccessible settings from existing alerts.

`security_and_analysis` requires appropriate permissions; absence/null is not disabled evidence. Do not copy alert bodies, secret values, or private dependencies into public Issues/logs; record only necessary targets, feature names, states, and permission-protected references.[^repository-api]

[^security-features]: Standard free/product feature lists; check changes/additions at execution time.
[^advanced-security]: Code Security/Secret Protection boundaries and availability.
[^repository-api]: Retrieval/application conditions for security_and_analysis and Dependabot settings.
[^code-scanning-api]: Default setup retrieval/update and scan results.
