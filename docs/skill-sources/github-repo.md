---
type: Reference
title: GitHub repository sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the github-repo skill.
sources:
  - id: skill-independence
    resource: https://github.com/daiksud/agents/issues/285
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
  - id: standalone-scope
    resource: https://github.com/daiksud/agents/issues/287
  - id: workflow-lockfiles
    resource: https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles
  - id: locking-action-dependencies
    resource: https://docs.github.com/en/actions/how-tos/secure-your-work/lock-workflow-dependencies
  - id: actions-execution-policies
    resource: https://docs.github.com/en/actions/how-tos/administer/control-workflow-execution
  - id: actions-lock-cli
    resource: https://github.com/github/gh-actions-lock
  - id: dependabot-version-updates
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates
  - id: dependabot-options
    resource: https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference
  - id: issue-templates
    resource: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository
  - id: issue-form-syntax
    resource: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
  - id: pr-templates
    resource: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository
  - id: security-policy
    resource: https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy
  - id: branch-update-suggestions
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-suggestions-to-update-pull-request-branches
  - id: automatic-branch-deletion
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches
  - id: apm-install
    resource: https://microsoft.github.io/apm/reference/cli/install/
  - id: apm-virtual-packages
    resource: https://microsoft.github.io/apm/consumer/install-packages/
  - id: apm-skill-bundles
    resource: https://microsoft.github.io/apm/producer/package-relative-links/
---

## Scope

Maintainer reference for [github-repo](../../skills/github-repo/SKILL.md). These records explain source provenance and adoption history. Execution procedures and decision-relevant details remain in the skill and its task-specific references; ordinary execution does not require this document.

Checking dates below are historical records retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Source mapping

The following mapping preserves the original source IDs and annotation scope and records sources for the current bundled guidance.

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

### Supporting repository configuration

Runtime material: [repository-files.md](../../skills/github-repo/references/repository-files.md), the bundled [bug-report form](../../skills/github-repo/assets/issue-templates/bug_report.yml), [feature-request form](../../skills/github-repo/assets/issue-templates/feature_request.yml), [template chooser configuration](../../skills/github-repo/assets/issue-templates/config.yml), and [PR template](../../skills/github-repo/assets/pull_request_template.md).

| Source | Guidance supported |
| --- | --- |
| [^standalone-scope] | Repository settings and supporting files are handled within the installed github-repo bundle. |
| [^dependabot-version-updates][^dependabot-options] | `.github/dependabot.yml`, supported ecosystems, manifest locations, schedules, and preservation of existing update configuration. |
| [^code-owners] | CODEOWNERS placement, eligible owners, base-branch evaluation, and required-review behavior. |
| [^issue-templates][^issue-form-syntax] | Issue-form location and schema, template chooser configuration, default-branch availability, and existing-label prerequisites. |
| [^pr-templates] | PR-template placement and default-branch availability. |
| [^security-policy] | `SECURITY.md` content for supported versions and vulnerability reporting. |

### GitHub Actions dependency lockfiles

Runtime material: [actions-lock.md](../../skills/github-repo/references/actions-lock.md) and the Actions settings in [settings.md](../../skills/github-repo/references/settings.md).

| Source | Guidance supported |
| --- | --- |
| [^workflow-lockfiles] | `.github/workflows/actions.lock`, direct and transitive action coverage, runtime resolution, source identity, and reusable-workflow limits. |
| [^locking-action-dependencies] | Extension installation, generation, workflow changes, dependency review, and lockfile adoption. |
| [^actions-lock-cli] | Current CLI generation and verification behavior, supported hosts, options, and limitations. |
| [^actions-execution-policies] | Require lockfile under Actions policies, targeting and enforcement, and interaction with native SHA requirements. |
| [^actions-settings] | Action allowlists use locked SHAs; lockfile adoption can satisfy the native SHA requirement. |

### Additional repository settings

Runtime material: [settings.md](../../skills/github-repo/references/settings.md).

| Source | Guidance supported |
| --- | --- |
| [^branch-update-suggestions] | Always suggest updating pull request branches provides the update control without requiring an update or new validation. |
| [^ruleset-rules] | Strict required checks enforce an up-to-date branch separately from update suggestions. |
| [^automatic-branch-deletion] | Automatic head-branch deletion after merge, protection constraints, and fork behavior. |

### Standalone installation

User guidance: [README installation](../../README.md#installation). APM's command reference documents `--global` and explicit targets; its package installation guide documents skill subdirectory references.[^apm-install][^apm-virtual-packages] Together they support the documented command `apm install --global --target codex,copilot daiksud/agents/skills/github-repo`. Skills are copied as complete bundles with their internal relative links preserved, so the operational references and assets stay inside that directory.[^apm-skill-bundles]

This is documentation review, not an executed APM installation or compilation. The repository's validation exclusions remain in effect.

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

Bundled material: [Standards](../../skills/github-repo/references/settings.md), [Security](../../skills/github-repo/references/security.md), [Operations](../../skills/github-repo/references/operations.md), [Repository files](../../skills/github-repo/references/repository-files.md), and [Actions lockfiles](../../skills/github-repo/references/actions-lock.md). The skill contains its own setting prerequisites, file-adoption procedures, and delivery requirements. Skill-selection guidance is maintained in the [README](../../README.md#skills-and-github-protection-settings).[^skill-independence][^standalone-scope]

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
[^standalone-scope]: [Standalone github-repo scope](https://github.com/daiksud/agents/issues/287).
[^dependabot-version-updates]: [Configuring Dependabot version updates](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates).
[^dependabot-options]: [Dependabot options reference](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
[^issue-templates]: [Configuring issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository).
[^issue-form-syntax]: [Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms).
[^pr-templates]: [Creating a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).
[^security-policy]: [Adding a security policy](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy).
[^workflow-lockfiles]: [Workflow dependency lockfiles](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles).
[^locking-action-dependencies]: [Locking action dependencies](https://docs.github.com/en/actions/how-tos/secure-your-work/lock-workflow-dependencies).
[^actions-lock-cli]: [github/gh-actions-lock](https://github.com/github/gh-actions-lock).
[^actions-execution-policies]: [Governing execution of GitHub Actions workflows](https://docs.github.com/en/actions/how-tos/administer/control-workflow-execution).
[^branch-update-suggestions]: [Managing suggestions to update pull request branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-suggestions-to-update-pull-request-branches).
[^automatic-branch-deletion]: [Managing automatic deletion of branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-the-automatic-deletion-of-branches).
[^apm-install]: [APM command reference](https://microsoft.github.io/apm/reference/cli/install/).
[^apm-virtual-packages]: [APM package installation](https://microsoft.github.io/apm/consumer/install-packages/).
[^apm-skill-bundles]: [APM package-relative links and skill bundles](https://microsoft.github.io/apm/producer/package-relative-links/).

## Decision recording settings

The [GitHub repository setting path](../../skills/github-repo/references/settings.md#pr-and-merge-message-alignment) locally defines the merge methods, message fields, and readback steps needed within the authorized settings scope. Related skill responsibilities are described in the [README](../../README.md#skills-and-github-protection-settings); github-repo's execution uses its own guidance.[^skill-independence] Consumer file changes retain ordinary PR, review, CI, and main-verification requirements.

The [GitHub repository API](https://docs.github.com/en/rest/repos/repos#update-a-repository) documents both sets of message fields. Installing guidance or copying assets does not apply live settings.

[^skill-independence]: [Independent skill guidance and versioning responsibilities](https://github.com/daiksud/agents/issues/285).
