---
type: Instruction
title: GitHub Actions workflow design
description: Choose triggers, jobs, reuse, artifacts, deployment, and recovery from requirements and validate execution paths.
---

## Determine execution paths from requirements

For new workflows check who needs which results for which changes. For existing structures first read purpose, required check names, supported OS/runtimes, Secrets/publication permissions, deployment targets, and recovery. Start with small structures passing required validation.

### Events and jobs

- Choose `push`/`pull_request` by comparing validated commits and duplicate runs. For merge queues check required events such as `merge_group`. Do not use `pull_request_target` to bypass insufficient PR-test permissions.
- Match `workflow_dispatch` to manual operations, `workflow_call` to reuse, and `schedule` to recurring work. Check official target-event specifications for default-branch definitions and PR head versus merge ref.
- `needs` expresses actual dependencies. Do not unnecessarily serialize independent checks; check downstream behavior on upstream failure/skip. Separate cleanup/diagnostic-saving conditions from conditions treating mandatory validation as successful.
- Specify shells, working directories, dependency pinning, and appropriate timeouts. Check OS shell differences, service readiness, test isolation, and cleanup. Do not hide mandatory-test failures through indiscriminate retries or `continue-on-error`.
- Whole-workflow path/branch filters with required checks can leave them Pending. With job-level decisions/aggregation, verify necessary validation failures/cancellations propagate to final checks.

### Reuse and data handoff

Consider composite Actions for shared steps and reusable workflows for shared jobs/runner structures. Match existing boundaries; duplication alone does not justify splitting. Contract `workflow_call` input types, requiredness, defaults, outputs, and Secrets, checking caller mappings. Nested calls cannot increase permissions; explicitly check Secret forwarding. Choose `secrets: inherit` after confirming necessary scope.

Pass small values as outputs and files as artifacts; paths alone do not move files between jobs. Check generating commit, target OS/version, content identity, retention, and confidential data. Save only necessary diagnostics in logs/reports, excluding Secrets. Caches support reuse, not authoritative deployment artifacts.

### Deployment and recovery

Promote the same validated artifact between environments. Check job conditions/permissions, environment protection, concurrency conflicts, and responsibility for release decisions. `environment:` alone does not configure manual approval. Choose manual approval, Canary, or blue/green where risks/existing operations fit.

Define post-deployment health checks, observed failures, and recovery artifacts/configuration. Do not assume data migrations are as reversible as code rollback. Check deployment/recovery within existing scope; use `issue-management` for changed release conditions/permissions. Hand approved recovery changes/validation to `change-delivery`.

### Paths to validate

Select necessary events, forks, unrelated changes, dependency-job failures/skips, and cancellation as well as normal paths. Beyond static checks/existing tests, verify required checks, outputs/artifacts, and post-deployment state through authorized GitHub runs. State inaccessible protection settings or unexecuted deployment as unverified. For test design and cleanup, apply [Testing boundaries and cleanup](../../software-development/references/testing.md#no-tests-of-tests); retain deployment-identity, failure-propagation, and security outcomes without asserting internal helper/command sequences or self-testing application runners.

## Runners and shells

Check these only when runners or shells relate to workflow design, changes, or review.

- Before selecting runners, check target `runs-on` label availability, matching candidate providers (GitHub-hosted/self-hosted), groups, and repository access. Do not infer provider from labels. If same-label self-hosted runners are candidates, especially for PR code, check shared-state/network/host-credential boundaries in [Safety](hardening.md); do not finalize solely from labels before confirming GitHub-hosted status.
- Even when `ubuntu-slim` is available, permanently use another runner only after confirming it cannot satisfy necessary processing. Habit, existing examples, or mere desire for performance are not exception reasons.
- For execution-time requirements, compare target-runner measurements with job timeouts in official material at decision time; other runners' times alone do not prove fit. Without measurements retain existing mandatory jobs if present and try representative jobs on nonmandatory trials for new candidates. This is temporary pending suitability, not a permanent exception.
- For exceptions check GitHub.com/GHES, visibility, and plan. On GitHub.com consult applicable [public-runner lists](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories) or [private-runner lists](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories). On GHES check its inventory without applying GitHub.com lists.
- Compare `ubuntu-slim` constraints, recording unmet requirements/concrete constraints in workflow comments or change descriptions. Check [official constraints](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners) at decision time.
- When reporting runner choices, explicitly distinguish this skill's `ubuntu-slim` preference from universal GitHub requirements and official provision/constraint specifications. Record dated specification checks with the target decision.
- For new workflows or approved workflow-level shell migration, always specify top-level `defaults.run.shell: bash`. Step-only `shell: bash` does not satisfy this. For limited existing-workflow changes without approved shell migration, preserve existing shells and report/propose shell policy separately.
- Check Bash availability and command compatibility in every affected job. Where missing on self-hosted runners/containers, provide Bash-equipped runners/images if possible. For package-install steps using existing shells, explicitly specify a shell available before installation (for example `sh`); top-level Bash defaults also affect installation steps.
- If Bash cannot be provided and commands are POSIX-compatible, retain workflow-level Bash and specify `defaults.run.shell: sh` only for that job, recording absence as the reason. For jobs/steps contracted to PowerShell or another shell, retain top-level defaults and override job `defaults.run.shell` or step `shell` with available compatible shells, recording concrete requirements. These are local exceptions necessary for environments/command compatibility. If Bash-specific commands are necessary but Bash unavailable, ask the user which policy/requirements take precedence.
- Explicit `bash` and unspecified shells execute different commands. On Linux/macOS, unspecified shells use `bash -e {0}`, falling back to `sh -e {0}` without Bash; explicit `bash` uses `bash --noprofile --norc -eo pipefail {0}`. Job containers default to `sh` unless overridden. Check the current [workflow shell specification](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun) and [job container specification](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idcontainer) for the target environment.
- When changing unspecified shells to explicit Bash, check pipeline status and existing handlers/output contracts. `pipefail` returns the last nonzero command's status in a pipeline. `errexit` does not immediately exit solely from failures in `if` conditions or nonfinal `&&`/`||` list commands; that exception does not apply after the final `&&`/`||`. Compare actual pipeline positions and surrounding branches with the [Bash pipeline](https://www.gnu.org/software/bash/manual/html_node/Pipelines) and [set builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) specifications. Handle only intended nonzero statuses locally while preserving other failures. Record existing-job-contract reasons for job/step overrides.

```yaml
defaults:
  run:
    shell: bash

jobs:
  check:
    # Confirm provider, runner group, and repository access before selecting this label.
    # Label availability alone does not identify a GitHub-hosted runner.
    runs-on: ubuntu-slim
    steps:
      - name: Check shell
        run: printf '%s\n' "$BASH_VERSION"
```
