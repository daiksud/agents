---
type: Reference
title: Continuous delivery sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the continuous-delivery skill.
sources:
  - id: copilot-efficiency
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-cache
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching
  - id: copilot-hardening
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-hardening
  - id: github-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
  - id: github-runner-selection
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
  - id: github-self-hosted-labels
    resource: https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels
  - id: github-runner-groups
    resource: https://docs.github.com/en/actions/concepts/runners/runner-groups
  - id: github-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
  - id: github-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
  - id: securitylab-pwn-requests
    resource: https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/
  - id: securitylab-untrusted-input
    resource: https://securitylab.github.com/resources/github-actions-untrusted-input/
  - id: securitylab-building-blocks
    resource: https://securitylab.github.com/resources/github-actions-building-blocks/
  - id: securitylab-new-patterns
    resource: https://securitylab.github.com/resources/github-actions-new-patterns-and-mitigations/
  - id: securitylab-scanner-config
    resource: https://securitylab.github.com/advisories/GHSL-2026-208_kptdev_kpt_repository/
  - id: securitylab-artifact-authorization
    resource: https://securitylab.github.com/advisories/GHSL-2026-225_actions_attest/
  - id: github-action-lockfiles
    resource: https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles
  - id: github-target-security
    resource: https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target
  - id: codeql-supported-languages
    resource: https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
  - id: github-oidc
    resource: https://docs.github.com/en/actions/reference/security/oidc
  - id: copilot-runtime
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md
  - id: github-metadata
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax
  - id: actions-checkout
    resource: https://github.com/actions/checkout
  - id: actions-setup-node
    resource: https://github.com/actions/setup-node
  - id: copilot-cicd
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/instructions/github-actions-ci-cd-best-practices.instructions.md
  - id: copilot-license
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/LICENSE
  - id: github-hosted-runners-public
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories
  - id: github-hosted-runners-private
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories
  - id: github-single-cpu-runners
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners
  - id: github-workflow-default-shell
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun
  - id: github-job-container-shell
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idcontainer
  - id: bash-reference-pipelines
    resource: https://www.gnu.org/software/bash/manual/html_node/Pipelines
  - id: bash-reference-set-builtin
    resource: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
  - id: actions-runner-shell-handler
    resource: https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs
  - id: github-reuse
    resource: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
  - id: github-concurrency
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
  - id: github-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
  - id: agents-phase-design
    resource: https://github.com/daiksud/agents/issues/268
  - id: agents-technical-policy
    resource: https://github.com/daiksud/agents/issues/270
  - id: github-expressions
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/expressions
  - id: github-run-variables
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
  - id: github-artifact-api
    resource: https://docs.github.com/en/rest/actions/artifacts
  - id: actions-download-artifact
    resource: https://github.com/actions/download-artifact/blob/9000827ccba6bdab643e8b6fd33ac0654aef8333/README.md
  - id: actions-upload-artifact
    resource: https://github.com/actions/upload-artifact/blob/cf430e030ddbb5b0abf93d22962f4752f3646cd9/README.md
  - id: agents-staged-ci
    resource: https://github.com/daiksud/agents/issues/242
  - id: gh-qw-check-names
    resource: https://github.com/daiksud/gh-qw/pull/141
  - id: gh-settings-check-names
    resource: https://github.com/daiksud/gh-settings/pull/455
  - id: gh-qw-platforms
    resource: https://github.com/daiksud/gh-qw/pull/137
  - id: gh-qw-ci-metadata
    resource: https://github.com/daiksud/gh-qw/blob/64afba3ce3a32e72dffdcadd4ffdaffc4c034256/.github/actions/ci-metadata/action.yml
  - id: gh-settings-ci-metadata
    resource: https://github.com/daiksud/gh-settings/blob/b79568b604f545823e4a36a4de59c3be5b86d4ed/.github/actions/ci-metadata/action.yml
  - id: agents-continuous-delivery
    resource: https://github.com/daiksud/agents/issues/275
  - id: github-actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: github-artifact-retention
    resource: https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts
  - id: github-environments
    resource: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
  - id: github-configuration-variables
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/variables
  - id: actionlint
    resource: https://github.com/rhysd/actionlint
  - id: zizmor
    resource: https://docs.zizmor.sh/
  - id: github-dependabot-actions
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions
---

## Scope

The current guidance for continuous delivery on GitHub is in [continuous-delivery](../../skills/continuous-delivery/SKILL.md) and its four bundled references. It covers GitHub settings, Actions workflows, and tools. This catalog preserves source mappings and historical adoption records.

Checking dates below are historical records retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Current settings and tools

| Guidance | Source scope |
| --- | --- |
| [Skill entry point](../../skills/continuous-delivery/SKILL.md) | The repository policy defines `pr.yml`, `push.yml`, and `release.yml`, four-layer responsibilities, shared phase actions, and artifact reuse.[^agents-continuous-delivery] |
| [Workflow design](../../skills/continuous-delivery/references/workflow-design.md) | Artifact availability and retention constraints come from repository settings and artifact-download guidance.[^github-actions-settings][^github-artifact-retention] |
| [Hardening](../../skills/continuous-delivery/references/hardening.md) | Actions policies and default token permissions, deployment environments and their protection rules, and non-sensitive configuration variables.[^github-actions-settings][^github-environments][^github-configuration-variables] |
| [Tooling](../../skills/continuous-delivery/references/tooling.md) | `actionlint` checks workflow syntax and expressions, `zizmor` analyzes CI/CD security, and Dependabot updates Actions references. These are tool candidates selected around existing project configuration.[^actionlint][^zizmor][^github-dependabot-actions] |

## Historical source mapping

The following mapping preserves the original source IDs and annotation scope, with links to the current technical references.

### GitHub Actions efficiency improvements

Current reference: [efficiency.md](../../skills/continuous-delivery/references/efficiency.md).

| Source | Original annotation scope |
| --- | --- |
| [^copilot-efficiency] | Restructured measurement, selection, and validation perspectives from SKILL.md and actions/reporting/patterns/review-rubric. |
| [^github-cache] | Dependency caching reference. Check restoration compatibility and cross-branch access. |
| [^github-syntax] | Workflow syntax. Check filters, concurrency, and queue specifications in the target environment. |

### GitHub Actions safety

Current reference: [hardening.md](../../skills/continuous-delivery/references/hardening.md).

| Source | Original annotation scope |
| --- | --- |
| [^copilot-hardening] | Restructured Hardening and bundled investigation perspectives. Do not adopt safety/severity judgments based only on triggers. |
| [^github-syntax] | Workflow syntax. Authoritative effective-permission calculation and scopes. |
| [^github-secure-use] | Secure use. Evidence for inputs, Secrets, Action pinning, and runner isolation. |
| [^github-oidc] | OIDC reference. Compare actual claims with cloud trust conditions. |
| [^github-runner-selection] | Choosing the runner for a job. Evidence for `runs-on` label/group selection and combined conditions. |
| [^github-self-hosted-labels] | Using labels with self-hosted runners. Evidence for runner types supporting custom labels. |
| [^github-runner-groups] | Runner groups. Group purpose and target runner scope. |
| [^github-commands] | Workflow commands. Check multiline data/environment-file handling. |
| [^github-events] | Events that trigger workflows. Check privileged-event boundaries with untrusted code/artifacts. |

### Security Lab trust-boundary additions

On 2026-11-03 compared all four articles and the two advisories below with the then-current GitHub event, secure-use, workflow-command, cache, lockfile, and CodeQL documentation. This was source/static review, not workflow execution or a security-settings change. Existing permission, input, pinning, runner, artifact, and cache rules were extended in the [historical hardening reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/hardening.md); that revision's entry point distinguished locked Actions from SHA-pinned reusable workflow calls.

| Source | Adopted scope beyond existing guidance |
| --- | --- |
| [^securitylab-pwn-requests] | Preserve privileged metadata automation; isolate PR builds and keep their output untrusted. Trace install hooks and other execution paths. |
| [^securitylab-untrusted-input] | Include less obvious inputs and second-stage template evaluation inside Actions; passing an input does not make its downstream interpretation safe. |
| [^securitylab-building-blocks] | Review Action updates, implicit token access, and transitive dependencies; verified creators and immutable references do not certify code. |
| [^securitylab-new-patterns] | Bind approvals to commits, inspect other base branches, authenticate upstream events, and prevent artifact/cache content reaching privileged execution. |

The 2026 scanner advisory shows a PR-controlled host setting leaking a scanner token before code analysis; trusted tool configuration and credential destinations must survive input/configuration precedence.[^securitylab-scanner-config] The artifact-metadata advisory separately shows that valid branch syntax and an unchanged SHA do not authorize a write destination. Match repository, PR/head branch, and intended operation through trusted metadata instead of trusting artifact identifiers.[^securitylab-artifact-authorization]

The 2026-11-03 revision recorded these corrections to the source examples:

- Inspect `github.event.workflow_run.event`, not Part 4's `github.event_name != 'pull_request'`, which sees the consumer event. Workflow names, branch filters, actor checks, and base-repository ownership alone do not establish producer trust. Correlate run metadata and intended event/ref; keep PR output untrusted.[^github-events][^securitylab-new-patterns]
- Retain quoted intermediate environment variables for script input, as the checked documentation recommended. Part 4's warning about environment/output injection did not justify banning this data handoff; validate values before writing command files or interpreting them downstream.[^github-secure-use][^github-commands]
- Do not adopt Part 1's passive-checkout examples as a general exemption: formatters can load PR-controlled plugins/configuration. Use trusted logic and trace indirect execution. The checked guidance included checkout protections, but these did not justify mixing PR-changeable code with privileges.[^github-target-security]
- Recheck cache behavior rather than assume every low-trust trigger can poison default-branch caches. At that time, such triggers defaulted to read-only there, with explicit write-capable overrides; inspect called workflows and cap caller cache access. Ordinary PR caches were merge-ref scoped.[^github-cache]
- Use adopted `actions.lock` coverage for direct/transitive Actions and repository identity; it excludes reusable workflow calls and their dependencies in other repositories. Pin calls to full SHAs and inspect the called repository's lockfile. The lockfile does not govern other build inputs.[^github-action-lockfiles]
- The checked CodeQL documentation supported GitHub Actions workflow and Action metadata YAML. Confirm `actions` analysis in the actual setup; application-language analysis or a clean result alone does not establish workflow safety.[^codeql-supported-languages]

### Upgrading Action internal runtimes

Current reference: [tooling.md](../../skills/continuous-delivery/references/tooling.md).

| Source | Original annotation scope |
| --- | --- |
| [^github-metadata] | Metadata syntax. Authoritative Action internal `runs.using`. |
| [^copilot-runtime] | Summarized Runtime Upgrade Conventions source investigation, compatible upgrades, and behavior preservation. Do not adopt old SHA/version examples or equate local checks with real execution. |
| [^actions-checkout] | Check authentication, forks, and runner requirements in target checkout releases/metadata/README. |
| [^actions-setup-node] | Check cache/input changes in target setup-node releases/metadata/README. |

### GitHub Actions skill sources and application decisions

Former source catalog: `skills/github-actions/references/sources.md`. Its adoption and checking records are preserved below.

| Source | Original annotation scope |
| --- | --- |
| [^copilot-cicd] | GitHub awesome-copilot CI/CD Best Practices Instructions, fixed version above. |
| [^copilot-efficiency] | GitHub Actions Efficiency and four bundled resources, fixed version above. |
| [^copilot-hardening] | GitHub Actions Hardening and bundled references, fixed version above. |
| [^copilot-runtime] | GitHub Actions Runtime Upgrade Conventions, fixed version above. |
| [^copilot-license] | GitHub awesome-copilot MIT License, fixed version above. |
| [^github-runner-selection] | [Choosing the runner for a job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job). Source for label/group selection and combined conditions. |
| [^github-self-hosted-labels] | [Using labels with self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels). Source for custom self-hosted labels. |
| [^github-runner-groups] | [Runner groups](https://docs.github.com/en/actions/concepts/runners/runner-groups). Source for group purpose and composition. |
| [^github-hosted-runners-public] | [Standard GitHub-hosted runners for public repositories](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories). Source for public repository runner labels/specifications. |
| [^github-hosted-runners-private] | [Standard GitHub-hosted runners for private repositories](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories). Source for private labels, specifications, and availability. |
| [^github-single-cpu-runners] | [Single-CPU runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners). Source for the stated 15-minute limit and unprivileged-container constraints. |
| [^github-workflow-default-shell] | [Workflow syntax: `defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun). Source for stated default shells and execution commands. |
| [^bash-reference-pipelines] | [GNU Bash Reference Manual: Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines). Explains pipeline status with pipefail. |
| [^bash-reference-set-builtin] | [GNU Bash Reference Manual: The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html). Explains conditional-context exceptions for `-e`. |
| [^github-job-container-shell] | [Workflow syntax: `jobs.<job_id>.container`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idcontainer). Source for stated container shell defaults. |
| [^actions-runner-shell-handler] | [Actions runner `ScriptHandler.cs`](https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs#L187-L203), [Explicit shell resolution](https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs#L205-L233). Unspecified-shell OS selection and Linux/macOS Bash-to-sh search, then explicit-shell resolution. Implementation snapshot checked on 2026-09-21; recheck actual target runners/containers. |

### GitHub Actions workflow design

Current reference: [workflow-design.md](../../skills/continuous-delivery/references/workflow-design.md).

| Source | Original annotation scope |
| --- | --- |
| [^copilot-cicd] | Summarized design, tests, artifacts, and deployment perspectives of CI/CD Best Practices without fixed structures or universal release methods. |
| [^github-syntax] | Workflow syntax. Authoritative event filters, job dependencies, and condition behavior. |
| [^github-reuse] | Reuse workflows. Authoritative input, Secret, and permission call contracts. |

## Adoption and previous checking records

### Imported sources and attribution

On 2026-09-20 checked these four awesome-copilot resources and related material, summarizing/restructuring them in Japanese. Fixed commit: `4f4796f0bf30e105700f97ed8408c12b6aa95e06`. Checking compared material with official specifications, not actual execution of every sample or human approval.

| Source | Imported scope and placement |
| --- | --- |
| CI/CD Best Practices[^copilot-cicd] | Triggers, jobs, reuse, tests, artifacts, deployment/recovery into design; safety/efficiency into corresponding material |
| Efficiency[^copilot-efficiency] | Measurement, candidate selection, validation from SKILL.md, actions.md, reporting.md, patterns.md, review-rubric.md into efficiency |
| Hardening[^copilot-hardening] | Input, trigger, permission, execution-path inspection from SKILL.md/bundled references into safety |
| Runtime Upgrade Conventions[^copilot-runtime] | Warning investigation, compatibility, SHA pinning, small upgrades, artifact validation into upgrades |

The imported originals were distributed under the MIT License, Copyright GitHub, Inc. The corresponding notice is preserved in the [historical LICENSE.txt](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/LICENSE.txt).[^copilot-license]

### Historical adoption decisions

| Topic | Integrated judgment |
| --- | --- |
| Overlap among four sources | One skill for entry/common safety/validation conditions; read task-specific detail |
| Work boundaries | The original hardening edit prohibition was limited to audits/review. The Issue #268 revision placed scope, inspection, editing, validation, and reporting in the entry point without requiring other skills |
| Permissions | Do not adopt “tokens always default write,” “event names alone grant all Secrets,” or “fork PRs are unconditionally safe.” Check effective permissions, passed Secrets, code provenance, runners |
| Untrusted output | Unprivileged-build artifacts remain untrusted, even in privileged workflow_run; validate without executing as code |
| Action pinning | Full SHA/release/comment agreement; do not copy mutable-tag or mismatched examples |
| Design | Do not uniformly require develop/release branches, manual approval, Canary, particular services, or every checking tool |
| Efficiency | A few evidence-based improvements and separate measurements; no fixed three items or 1.25× wait threshold |
| Matrices | Preserve undocumented supported environments until contracts/actual use are checked |
| Skips/cancellation | Do not break required checks with path filters or require cancellation everywhere; check pending replacement and queue in target environments |
| Caches | Run-ID keys or saving node_modules are not universal patterns; check compatibility, storage cost, trust |
| Upgrades/validation | Separate internal/application runtimes; local success does not replace actual Action runs |

These were the imported skill's application decisions, not wholesale adoption.

### Historical standalone phase-oriented design

Issue #268 replaced mandatory skill dependencies and the old Commit/Acceptance adoption model. The [historical entry point](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/SKILL.md) and four task-specific references used Japanese and covered phase-oriented design together with investigation, change, and reporting procedures.[^agents-phase-design]

On 2026-11-06, source review covered Composite Action metadata, reusable workflows, status functions, artifact retrieval and identity, run attempts, and the retained lockfile, cache-access, and runner guidance. This was documentation/source inspection, not execution of the proposed workflow.[^github-metadata][^github-reuse][^github-expressions][^actions-download-artifact][^actions-upload-artifact][^github-run-variables][^github-artifact-api] At that comparison, the pinned download-action README described configurable digest-mismatch handling with an error default, while the general artifact tutorial described a warning.[^actions-download-artifact][^github-artifacts]

### Technical design policy

Issue #270 records the refinement to a standalone Japanese technical design policy organized around Workflow, Job, Composite Action, and Step. The skill keeps `SKILL.md` and four references covering workflow design, safety, efficiency, and Action runtime upgrades.[^agents-technical-policy]

### Historical staged CI adoption

The following records describe the earlier policy and its 2026-10-31 checking scope. Issue #268 later superseded its prescribed workflow names, Draft/Ready operations, and Commit/Acceptance orchestration. That revision did not change the historical records or establish that consumer repositories had migrated.[^agents-phase-design]

The [historical workflow-design reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/workflow-design.md) and [historical efficiency reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/efficiency.md) contain later revisions of this guidance. Issue #242 records a selected shared policy for adopting repositories, not a universal GitHub requirement or permission to replace their validation with a copied workflow.[^agents-staged-ci]

The original 2026-10-25 record used a common `pass` context and listed four gh-qw CI targets. Later naming decisions, implemented in gh-qw #141 and gh-settings #455, used distinct native `ci-pr` and `ci-push` aggregates and separate `prlint`; the workflow file stem, workflow name, and aggregate job/check name agreed. The shared guidance at that revision followed those names.[^gh-qw-check-names][^gh-settings-check-names] gh-qw #137 retired Linux ARM64 and Intel Mac support. At the recorded revision its matrix retained Linux amd64, macOS arm64, and Windows amd64, while gh-settings retained both process and public-Action candidate acceptance. Later adoption must check current contracts rather than restore a historical target list.[^gh-qw-platforms][^gh-qw-ci-metadata][^gh-settings-ci-metadata]

| Choice | Rationale and tradeoff |
| --- | --- |
| Common orchestration with local composite Actions | Consistent dependencies and artifact interfaces permit reuse while local commands and matrices retain repository-specific coverage. This avoids both blanket workflow copies and a new configuration framework. |
| Build once, then accept the transferred candidate | Testing the same bytes makes acceptance evidence apply to the candidate. Source/platform identity and digest checks detect a wrong handoff; they do not establish current-HEAD freshness or permission to merge. |
| Ready after Commit, with Acceptance in the same run | Review can begin after fast feedback, while `needs` keeps acceptance tied to that run. A Ready PR can still fail acceptance; review readiness and successful validation are different facts. |
| Native concurrency and explicit aggregate results | Cancellation reduces superseded work without maintaining custom freshness/recovery coordination. GitHub does not guarantee dispatch ordering, and default dependency skips require an explicit final result check. |

These are the policy's tradeoffs.[^agents-staged-ci] GitHub's dependency rules and `always()` support evaluating failed or skipped prerequisites; concurrency does not supply an atomic latest-HEAD guarantee.[^github-syntax][^github-concurrency] Artifact transfer has a separate integrity concern: the documented digest-mismatch behavior can be only a warning, so adoption must check the selected Action's behavior and make mismatches fail.[^github-artifacts]

**Adoption limits as of 2026-10-31:** the merged product workflows deliberately rerun code validation on metadata edits. That behavior in #141/#455 is an implementation gap relative to #242's selected title/body isolation contract, not evidence that isolation is already implemented.[^gh-qw-check-names][^gh-settings-check-names][^agents-staged-ci] Workflow adoption must preserve required-check semantics while isolating those edits, including cancellation and skipped-success replacement. Fork/Dependabot PRs without Draft/Ready permissions remain outside this selected policy's supported path; privileged fallbacks would change its trust boundary.[^agents-staged-ci][^github-events]

This guidance change does not alter actual workflows, live required contexts, review/merge policy, releases, or global APM deployment. Required-context migration remains a separately authorized settings operation. On 2026-10-31 the source comparison covered the cited repository metadata, PR records, and official dependency, event, concurrency, and artifact documentation. It was a source review, not execution of the proposed workflow contract. Later workflow adoption must distinguish static checks from actual GitHub runs when assessing stage flow, failures, metadata isolation, artifact reuse, and retained platforms.[^agents-staged-ci]

### Historical official checks

On 2026-09-20 compared official GitHub workflow syntax, reusable workflows, cache, secure use, events, workflow commands, OIDC, Action metadata, and then-current checkout/setup-node material. The source mapping above preserves the claim scope and URLs formerly recorded in the references.

The [historical efficiency reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/efficiency.md) covered filters, required checks, and concurrency; the [historical safety reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/hardening.md) covered permissions, forks, runners, and OIDC; the [historical runtime-upgrade reference](https://github.com/daiksud/agents/blob/23aa0c80918d1195db2592019aeaa125b6f6d622/skills/github-actions/references/runtime-upgrades.md) covered release metadata, notes, and full SHAs. These records do not establish present availability or compatibility.

### Official runner and shell specifications

On 2026-09-22 checked GitHub.com public/private hosted-runner lists, Single-CPU constraints, and `defaults.run.shell` syntax. Private lists described standard `ubuntu-latest` as 2 CPU/8 GB and public lists as 4 CPU/16 GB. Values/features/availability change; check visibility, plan, label, and current official specifications at selection time. Check GHES inventories separately.

On 2026-09-22 checked [Runner selection][^github-runner-selection], [self-hosted labels][^github-self-hosted-labels], and [runner groups][^github-runner-groups]. Scope covered `runs-on` label/group conditions, custom-label configuration, and group targets, not actual Organization/repository inventories/access. Check target settings when selecting jobs.

- `ubuntu-slim` appears in GitHub.com public/private standard lists; on 2026-09-22 it was described as 1 CPU/5 GB, 15-minute job limit, unprivileged containers. Filesystem mounts, Docker-in-Docker, and some low-level kernel features are unavailable. These determine actual suitability, not universal runner-selection requirements. [Public lists][^github-hosted-runners-public], [private lists][^github-hosted-runners-private], [Single-CPU runners][^github-single-cpu-runners]
- `runs-on` selects labels/groups; with both, only runners matching both qualify. Self-hosted runners may have custom labels, and groups comprise larger/self-hosted runners. Labels alone therefore may not establish hosted versus self-hosted; check provider/group/repository access. [Runner selection][^github-runner-selection], [self-hosted labels][^github-self-hosted-labels], [runner groups][^github-runner-groups]
- Unspecified Linux/macOS shells use `bash -e {0}`, falling back to `sh -e {0}` without Bash. Explicit `shell: bash` uses `bash --noprofile --norc -eo pipefail {0}`. [Workflow syntax][^github-workflow-default-shell] Bash `pipefail` returns the last nonzero command's status in pipelines. [Bash manual][^bash-reference-pipelines] Bash `-e` does not immediately exit solely from failures in `if` conditions or nonfinal `&&`/`||` list commands, but that exception does not apply after the final `&&`/`||`. [Bash manual][^bash-reference-set-builtin] On explicit-Bash migration check pipeline statuses and surrounding branches/handlers, explicitly permitting only intended intermediate nonzero statuses while preserving other failures.
- Job `container` defaults to `sh`, overridable through workflow/job `defaults.run.shell` or step `shell`. Check container Bash availability before workflow-level Bash defaults. [Job container syntax][^github-job-container-shell]
- Runner implementation searches Bash then falls back to `sh` for unspecified shells, selecting declared shells when explicit. The fixed implementation checked on 2026-09-21 uses separate branches. [ScriptHandler.cs][^actions-runner-shell-handler]
- Check Bash/command compatibility for every affected runner/container. Provide Bash-equipped runners/images if possible; package-install steps need explicit pre-install-available step shells such as `sh`, since Bash defaults also apply to them. If installation is impossible and processing POSIX-compatible, retain workflow Bash and set only the affected job `defaults.run.shell: sh`, recording absence. [Workflow syntax][^github-workflow-default-shell]
- For jobs/steps contracted to PowerShell or other shells, retain workflow Bash and override job `defaults.run.shell` or step `shell` with available compatible shells, recording requirements. If Bash syntax is necessary but unavailable, ask which policy/job requirement takes precedence. [Workflow syntax][^github-workflow-default-shell]
- Do not infer GHES/self-hosted labels from hosted lists; check registered target labels. Unavailable `ubuntu-slim` is a concrete selection constraint.

[^agents-continuous-delivery]: [Continuous-delivery skill scope](https://github.com/daiksud/agents/issues/275).
[^github-actions-settings]: [Managing GitHub Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).
[^github-artifact-retention]: [Downloading workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts).
[^github-environments]: [Managing deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments).
[^github-configuration-variables]: [Configuration variables](https://docs.github.com/en/actions/concepts/workflows-and-actions/variables).
[^actionlint]: [actionlint documentation](https://github.com/rhysd/actionlint).
[^zizmor]: [zizmor documentation](https://docs.zizmor.sh/).
[^github-dependabot-actions]: [Keeping Actions up to date with Dependabot](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions).
[^copilot-efficiency]: [copilot-efficiency](https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency).
[^github-cache]: [github-cache](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching).
[^github-syntax]: [github-syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
[^copilot-hardening]: [copilot-hardening](https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-hardening).
[^github-secure-use]: [github-secure-use](https://docs.github.com/en/actions/reference/security/secure-use).
[^github-oidc]: [github-oidc](https://docs.github.com/en/actions/reference/security/oidc).
[^github-runner-selection]: [github-runner-selection](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job).
[^github-self-hosted-labels]: [github-self-hosted-labels](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels).
[^github-runner-groups]: [github-runner-groups](https://docs.github.com/en/actions/concepts/runners/runner-groups).
[^github-commands]: [github-commands](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands).
[^github-events]: [github-events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).
[^securitylab-pwn-requests]: [securitylab-pwn-requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/).
[^securitylab-untrusted-input]: [securitylab-untrusted-input](https://securitylab.github.com/resources/github-actions-untrusted-input/).
[^securitylab-building-blocks]: [securitylab-building-blocks](https://securitylab.github.com/resources/github-actions-building-blocks/).
[^securitylab-new-patterns]: [securitylab-new-patterns](https://securitylab.github.com/resources/github-actions-new-patterns-and-mitigations/).
[^securitylab-scanner-config]: [securitylab-scanner-config](https://securitylab.github.com/advisories/GHSL-2026-208_kptdev_kpt_repository/).
[^securitylab-artifact-authorization]: [securitylab-artifact-authorization](https://securitylab.github.com/advisories/GHSL-2026-225_actions_attest/).
[^github-target-security]: [github-target-security](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target).
[^github-action-lockfiles]: [github-action-lockfiles](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles).
[^codeql-supported-languages]: [codeql-supported-languages](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/).
[^github-metadata]: [github-metadata](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax).
[^copilot-runtime]: [copilot-runtime](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md).
[^actions-checkout]: [actions-checkout](https://github.com/actions/checkout).
[^actions-setup-node]: [actions-setup-node](https://github.com/actions/setup-node).
[^copilot-cicd]: [copilot-cicd](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/instructions/github-actions-ci-cd-best-practices.instructions.md).
[^copilot-license]: [copilot-license](https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/LICENSE).
[^github-hosted-runners-public]: [github-hosted-runners-public](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories).
[^github-hosted-runners-private]: [github-hosted-runners-private](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories).
[^github-single-cpu-runners]: [github-single-cpu-runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners).
[^github-workflow-default-shell]: [github-workflow-default-shell](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun).
[^bash-reference-pipelines]: [bash-reference-pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines).
[^bash-reference-set-builtin]: [bash-reference-set-builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html).
[^github-job-container-shell]: [github-job-container-shell](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idcontainer).
[^actions-runner-shell-handler]: [actions-runner-shell-handler](https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs).
[^github-reuse]: [github-reuse](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).
[^agents-phase-design]: [Standalone Japanese github-actions refinement](https://github.com/daiksud/agents/issues/268).
[^github-expressions]: [Status check functions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions).
[^actions-download-artifact]: [download-artifact README at the checked commit](https://github.com/actions/download-artifact/blob/9000827ccba6bdab643e8b6fd33ac0654aef8333/README.md).
[^actions-upload-artifact]: [upload-artifact README at the checked commit](https://github.com/actions/upload-artifact/blob/cf430e030ddbb5b0abf93d22962f4752f3646cd9/README.md).
[^github-run-variables]: [Run ID and run attempt variables](https://docs.github.com/en/actions/reference/workflows-and-actions/variables#default-environment-variables).
[^github-artifact-api]: [Artifact REST API](https://docs.github.com/en/rest/actions/artifacts#list-workflow-run-artifacts).
[^github-artifacts]: [github-artifacts](https://docs.github.com/en/actions/tutorials/store-and-share-data).
[^agents-technical-policy]: [GitHub Actions technical design policy](https://github.com/daiksud/agents/issues/270).
[^agents-staged-ci]: [agents-staged-ci](https://github.com/daiksud/agents/issues/242).
[^gh-qw-check-names]: [gh-qw-check-names](https://github.com/daiksud/gh-qw/pull/141).
[^gh-settings-check-names]: [gh-settings-check-names](https://github.com/daiksud/gh-settings/pull/455).
[^gh-qw-platforms]: [gh-qw-platforms](https://github.com/daiksud/gh-qw/pull/137).
[^gh-qw-ci-metadata]: [gh-qw-ci-metadata](https://github.com/daiksud/gh-qw/blob/64afba3ce3a32e72dffdcadd4ffdaffc4c034256/.github/actions/ci-metadata/action.yml).
[^gh-settings-ci-metadata]: [gh-settings-ci-metadata](https://github.com/daiksud/gh-settings/blob/b79568b604f545823e4a36a4de59c3be5b86d4ed/.github/actions/ci-metadata/action.yml).
[^github-concurrency]: [github-concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).
