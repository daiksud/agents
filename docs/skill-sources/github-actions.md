---
type: Reference
title: GitHub Actions sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the github-actions skill.
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
---

## Scope

Maintainer reference for [github-actions](../../skills/github-actions/SKILL.md). These records explain source provenance and adoption history. Execution procedures and decision-relevant details remain in the skill and its task-specific references; ordinary execution does not require this document.

Checking dates below are historical records retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Source mapping

The following mapping preserves the original source IDs and annotation scope for each runtime document and former source catalog.

### GitHub Actions efficiency improvements

Runtime material: [efficiency.md](../../skills/github-actions/references/efficiency.md).

| Source | Original annotation scope |
| --- | --- |
| [^copilot-efficiency] | Restructured measurement, selection, and validation perspectives from SKILL.md and actions/reporting/patterns/review-rubric. |
| [^github-cache] | Dependency caching reference. Check restoration compatibility and cross-branch access. |
| [^github-syntax] | Workflow syntax. Check filters, concurrency, and queue specifications in the target environment. |

### GitHub Actions safety

Runtime material: [hardening.md](../../skills/github-actions/references/hardening.md).

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

### Upgrading Action internal runtimes

Runtime material: [runtime-upgrades.md](../../skills/github-actions/references/runtime-upgrades.md).

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

Runtime material: [workflow-design.md](../../skills/github-actions/references/workflow-design.md).

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

Originals are MIT License, Copyright GitHub, Inc. Preserve complete copyright, permission, and disclaimer in [LICENSE.txt](../../skills/github-actions/LICENSE.txt).[^copilot-license]

### Adoption, revision, and rejection

| Topic | Integrated judgment |
| --- | --- |
| Overlap among four sources | One skill for entry/common safety/validation conditions; read task-specific detail |
| Work boundaries | Original hardening edit prohibition applies only to audits/review. Connect fix plans/publication permission to issue-management and approved changes to change-delivery without extra severity/report/Issue procedures |
| Permissions | Do not adopt “tokens always default write,” “event names alone grant all Secrets,” or “fork PRs are unconditionally safe.” Check effective permissions, passed Secrets, code provenance, runners |
| Untrusted output | Unprivileged-build artifacts remain untrusted, even in privileged workflow_run; validate without executing as code |
| Action pinning | Full SHA/release/comment agreement; do not copy mutable-tag or mismatched examples |
| Design | Do not uniformly require develop/release branches, manual approval, Canary, particular services, or every checking tool |
| Efficiency | A few evidence-based improvements and separate measurements; no fixed three items or 1.25× wait threshold |
| Matrices | Preserve undocumented supported environments until contracts/actual use are checked |
| Skips/cancellation | Do not break required checks with path filters or require cancellation everywhere; check pending replacement and queue in target environments |
| Caches | Run-ID keys or saving node_modules are not universal patterns; check compatibility, storage cost, trust |
| Upgrades/validation | Separate internal/application runtimes; local success does not replace actual Action runs |

These are this skill's application decisions, not wholesale adoption.

### Official checks and reassessment conditions

On 2026-09-20 compared official GitHub workflow syntax, reusable workflows, cache, secure use, events, workflow commands, OIDC, Action metadata, and current checkout/setup-node material. The source mapping above preserves the claim scope and URLs formerly recorded in runtime references. Avoid more specification copies; reread target-environment authoritative versions when making version-dependent judgments.

- For filters, required checks, or concurrency, check official specifications in [Efficiency](../../skills/github-actions/references/efficiency.md). Do not assume older environments support `queue: max` or its constraints.
- For permissions, forks, runners, or OIDC, check official specifications and actual settings/claims in [Safety](../../skills/github-actions/references/hardening.md). Do not assume fixed subjects/credential locations.
- For upgrades follow [Runtime upgrades](../../skills/github-actions/references/runtime-upgrades.md), comparing release metadata/notes/full SHA. Check dates alone do not prove latest versions or compatibility.

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
