---
type: Reference
title: GitHub Actions skill sources and application decisions
description: Record fixed imported versions, attribution, checking scope, and judgments revised during integration.
sources:
  - id: copilot-cicd
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/instructions/github-actions-ci-cd-best-practices.instructions.md
  - id: copilot-efficiency
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency
  - id: copilot-hardening
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-hardening
  - id: copilot-runtime
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md
  - id: copilot-license
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/LICENSE
  - id: github-hosted-runners-public
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories
  - id: github-hosted-runners-private
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories
  - id: github-single-cpu-runners
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners
  - id: github-runner-selection
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
  - id: github-self-hosted-labels
    resource: https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels
  - id: github-runner-groups
    resource: https://docs.github.com/en/actions/concepts/runners/runner-groups
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
---

## Imported sources and attribution

On 2026-09-20 checked these four awesome-copilot resources and related material, summarizing/restructuring them in Japanese. Fixed commit: `4f4796f0bf30e105700f97ed8408c12b6aa95e06`. Checking compared material with official specifications, not actual execution of every sample or human approval.

| Source | Imported scope and placement |
| --- | --- |
| CI/CD Best Practices[^copilot-cicd] | Triggers, jobs, reuse, tests, artifacts, deployment/recovery into design; safety/efficiency into corresponding material |
| Efficiency[^copilot-efficiency] | Measurement, candidate selection, validation from SKILL.md, actions.md, reporting.md, patterns.md, review-rubric.md into efficiency |
| Hardening[^copilot-hardening] | Input, trigger, permission, execution-path inspection from SKILL.md/bundled references into safety |
| Runtime Upgrade Conventions[^copilot-runtime] | Warning investigation, compatibility, SHA pinning, small upgrades, artifact validation into upgrades |

Originals are MIT License, Copyright GitHub, Inc. Preserve complete copyright, permission, and disclaimer in [LICENSE.txt](../LICENSE.txt).[^copilot-license]

## Adoption, revision, and rejection

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

## Official checks and reassessment conditions

On 2026-09-20 compared official GitHub workflow syntax, reusable workflows, cache, secure use, events, workflow commands, OIDC, Action metadata, and current checkout/setup-node material. Claims/URLs link through each reference's `sources`/footnotes. Avoid more specification copies; reread target-environment authoritative versions when making version-dependent judgments.

- For filters, required checks, or concurrency, check official specifications in [Efficiency](efficiency.md). Do not assume older environments support `queue: max` or its constraints.
- For permissions, forks, runners, or OIDC, check official specifications and actual settings/claims in [Safety](hardening.md). Do not assume fixed subjects/credential locations.
- For upgrades follow [Runtime upgrades](runtime-upgrades.md), comparing release metadata/notes/full SHA. Check dates alone do not prove latest versions or compatibility.

## Official runner and shell specifications

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

[^copilot-cicd]: GitHub awesome-copilot CI/CD Best Practices Instructions, fixed version above.
[^copilot-efficiency]: GitHub Actions Efficiency and four bundled resources, fixed version above.
[^copilot-hardening]: GitHub Actions Hardening and bundled references, fixed version above.
[^copilot-runtime]: GitHub Actions Runtime Upgrade Conventions, fixed version above.
[^copilot-license]: GitHub awesome-copilot MIT License, fixed version above.
[^github-runner-selection]: [Choosing the runner for a job](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job). Source for label/group selection and combined conditions.
[^github-self-hosted-labels]: [Using labels with self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/apply-labels). Source for custom self-hosted labels.
[^github-runner-groups]: [Runner groups](https://docs.github.com/en/actions/concepts/runners/runner-groups). Source for group purpose and composition.
[^github-hosted-runners-public]: [Standard GitHub-hosted runners for public repositories](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories). Source for public repository runner labels/specifications.
[^github-hosted-runners-private]: [Standard GitHub-hosted runners for private repositories](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories). Source for private labels, specifications, and availability.
[^github-single-cpu-runners]: [Single-CPU runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners). Source for the stated 15-minute limit and unprivileged-container constraints.
[^github-workflow-default-shell]: [Workflow syntax: `defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun). Source for stated default shells and execution commands.
[^bash-reference-pipelines]: [GNU Bash Reference Manual: Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines). Explains pipeline status with pipefail.
[^bash-reference-set-builtin]: [GNU Bash Reference Manual: The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html). Explains conditional-context exceptions for `-e`.
[^github-job-container-shell]: [Workflow syntax: `jobs.<job_id>.container`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idcontainer). Source for stated container shell defaults.
[^actions-runner-shell-handler]: [Actions runner `ScriptHandler.cs`](https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs#L187-L203), [Explicit shell resolution](https://github.com/actions/runner/blob/80bb1fb827fa44d489263061e71ef4adba7ad8cd/src/Runner.Worker/Handlers/ScriptHandler.cs#L205-L233). Unspecified-shell OS selection and Linux/macOS Bash-to-sh search, then explicit-shell resolution. Implementation snapshot checked on 2026-09-21; recheck actual target runners/containers.
