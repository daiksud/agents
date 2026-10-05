---
type: Instruction
title: GitHub Actions safety
description: Trace trust boundaries of inputs, executed code, permissions, runners, and artifacts to judge risks and fixes.
sources:
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
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
  - id: github-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
  - id: github-oidc
    resource: https://docs.github.com/en/actions/reference/security/oidc
---

## Trace inputs through impact

For audits read the specified scope; for fix requests change approved scope. Do not assign severity solely by matching dangerous syntax; check who controls input, which code runs with which permissions, and what it can reach. Use the source's trigger-specific investigation perspective, judging actual settings/paths.[^copilot-hardening]

### Permissions, authentication, and runners

- Investigate Organization/repository defaults, workflow/job `permissions`, fork settings, and reuse targets. Trigger names alone do not determine `GITHUB_TOKEN` permissions. Start from `permissions: {}` or necessary read permissions, limiting writes to needed jobs. With explicit permissions unspecified scopes become none; `id-token` is write/none.[^github-syntax]
- Trace Secrets through actual receiving jobs, Actions, and reuse targets. Masking does not guarantee leak prevention; do not log/artifact entire contexts, authenticated settings, or transformed secrets. Consider `persist-credentials: false` for unnecessary checkout authentication persistence, checking storage/behavior for the target Action version.[^github-secure-use]
- Where clouds support managed trust conditions, reduce long-lived keys through OIDC. Give only necessary jobs `id-token: write`, comparing actual claims, audience/subject, repository, branch/environment, and cloud role permissions. Do not apply fixed subject examples universally.[^github-oidc]
- `runs-on` labels alone do not identify providers. Check matching GitHub-hosted/self-hosted runners, groups, and repository access, verifying actual routing where persistent self-hosted runners share custom labels. [Runner selection][^github-runner-selection], [self-hosted custom labels][^github-self-hosted-labels], [runner groups][^github-runner-groups]. For untrusted fork-PR code, persistent state, host credentials, internal networks, and shared workspaces add risks. Absence of Secrets alone is not safety; ephemeral registration alone does not guarantee clean hosts. Check actual isolation/erasure. [Secure use][^github-secure-use]

### External input and executed code

Do not interpolate PR titles/bodies, branch names, comments, dispatch inputs, or similar data into `run` or `github-script` code. Use quoted intermediate environment variables, or JavaScript `process.env` as data. For Action inputs, trace whether receivers evaluate them as code.

```yaml
- name: Print PR title as data
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: printf '%s\n' "$PR_TITLE"
```

This demonstrates data handoff, not increased input trust. Do not reinterpret through `eval`, `bash -c`, or generated-script concatenation. Do not write newline-containing external values directly into `GITHUB_ENV`/`GITHUB_OUTPUT`. For multiline formats guarantee delimiters do not appear as standalone value lines; for arbitrary data save files and validate in readers.[^github-commands]

Privileged processing through `pull_request_target`, `workflow_run`, or similar events must not execute PR-derived checkouts, local Actions, build configuration, or dependency-install lifecycle scripts. Trace indirect execution as well as visible shells. Calling from reviewed workflows does not make called PR code trusted.[^github-events]

### Actions, caches, and artifacts

Compare external Actions/reusable workflows with official target-repository releases and full SHAs. Pinning reduces reference mutability, not proof of safe contents. Check inputs, dependency code, network/Secret use where needed. Select dependency, Secret, and static-security checks from existing detection coverage without uniformly adding every tool.

Keep artifacts passed from unprivileged builds to privileged publication untrusted. Match original run, repository, head SHA, event, and conclusion; validate download destinations, extraction paths, contents, and expected formats. Do not execute them as scripts on privileged sides. Completed/successful `workflow_run` alone does not guarantee artifact trust.

Investigate cache creators/refs and restoring jobs' permissions. Prevent untrusted code entering privileged processing through broad restore keys or shared directories. Do not save Secrets/tokens/authentication settings. Even with signatures/attestations, check digest correspondence with allowed creators/workflows.

## Validation and reporting

Check attack strings remain data in isolated tests; do not test leaks or exercise privileges in real environments. For audits show locations, input sources, execution paths, effective permissions, impact, and minimal fixes under `code-review` criteria. Distinguish unreadable settings, unexecuted fixes, and unconfirmed reachability.

[^copilot-hardening]: Restructured Hardening and bundled investigation perspectives. Do not adopt safety/severity judgments based only on triggers.
[^github-syntax]: Workflow syntax. Authoritative effective-permission calculation and scopes.
[^github-secure-use]: Secure use. Evidence for inputs, Secrets, Action pinning, and runner isolation.
[^github-oidc]: OIDC reference. Compare actual claims with cloud trust conditions.
[^github-runner-selection]: Choosing the runner for a job. Evidence for `runs-on` label/group selection and combined conditions.
[^github-self-hosted-labels]: Using labels with self-hosted runners. Evidence for runner types supporting custom labels.
[^github-runner-groups]: Runner groups. Group purpose and target runner scope.
[^github-commands]: Workflow commands. Check multiline data/environment-file handling.
[^github-events]: Events that trigger workflows. Check privileged-event boundaries with untrusted code/artifacts.
