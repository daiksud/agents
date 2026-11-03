---
type: Instruction
title: GitHub Actions safety
description: Trace trust boundaries of inputs, executed code, permissions, runners, and artifacts to judge risks and fixes.
---

## Trace inputs through impact

For audits read the specified scope; for fix requests change approved scope. Do not assign severity solely by matching dangerous syntax; check who controls input, which code runs with which permissions, and what it can reach. Investigate each trigger through actual settings and execution paths.

### Permissions, authentication, and runners

- Investigate Organization/repository defaults, workflow/job `permissions`, fork settings, and reuse targets. Trigger names alone do not determine `GITHUB_TOKEN` permissions. Start from `permissions: {}` or necessary read permissions, limiting writes to needed jobs. With explicit permissions unspecified scopes become none; `id-token` is write/none.
- Trace Secrets through actual receiving jobs, Actions, and reuse targets. Masking does not guarantee leak prevention; do not log/artifact entire contexts, authenticated settings, or transformed secrets. Consider `persist-credentials: false` for unnecessary checkout authentication persistence, checking storage/behavior for the target Action version.
- Where clouds support managed trust conditions, reduce long-lived keys through OIDC. Give only necessary jobs `id-token: write`, comparing actual claims, audience/subject, repository, branch/environment, and cloud role permissions. Do not apply fixed subject examples universally.
- `runs-on` labels alone do not identify providers. Check matching GitHub-hosted/self-hosted runners, groups, and repository access, verifying actual routing where persistent self-hosted runners share custom labels. For untrusted fork-PR code, persistent state, host credentials, internal networks, and shared workspaces add risks. Absence of Secrets alone is not safety; ephemeral registration alone does not guarantee clean hosts. Check actual isolation/erasure.

### External input and executed code

Do not interpolate PR titles/bodies, branch names, comments, dispatch inputs, or similar data into `run` or `github-script` code. Use quoted intermediate environment variables, or JavaScript `process.env` as data. For Action inputs, trace whether receivers evaluate them as shell commands, templates, or other code, including a second evaluation after GitHub expression expansion. Commit messages, author names/emails, and filenames can also carry untrusted input; validate the expected format and use data APIs or argument arrays rather than command concatenation.

```yaml
- name: Print PR title as data
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: printf '%s\n' "$PR_TITLE"
```

This demonstrates data handoff, not increased input trust. Do not reinterpret through `eval`, `bash -c`, or generated-script concatenation. Do not write newline-containing external values directly into `GITHUB_ENV`/`GITHUB_OUTPUT`. For multiline formats guarantee delimiters do not appear as standalone value lines; for arbitrary data save files and validate in readers.

### Privileged processing and approval boundaries

Use `pull_request_target` when trusted base-side logic needs privileges to label or comment on PRs. Keep processing limited to validated data; do not mix PR-changeable code with privileged execution. Run untrusted builds/tests in isolated, minimally privileged `pull_request` jobs, then pass only the data needed by a separate privileged consumer when necessary. Separation does not promote that data to trusted code.

Privileged processing through `pull_request_target`, `workflow_run`, `issue_comment`, or similar events must not execute PR-derived checkouts, local Actions, build configuration, or dependency-install lifecycle scripts. Trace indirect execution through test discovery, formatter plugins/configuration, imported modules, generated files, and executable search paths as well as visible shells. Calling from reviewed workflows does not make called PR code trusted.

Treat tool configuration as a trust boundary even without executing PR code: a scanner can send its token to a PR-selected server before analysis. Keep credential destinations, plugin/module loading, and executable paths under trusted base-side configuration; verify configuration precedence and prevent PR files or inputs from overriding them. Processing a file as data is insufficient if it can redirect authenticated behavior.

Labels, maintainer comments, actor membership, and workflow-run approval do not certify all future changes on a PR branch. Bind any review authorization to the exact commit SHA and recheck it before use; never resolve an approved mutable branch to newer code. A fixed SHA identifies bytes, not their safety or permission to execute them with privileges. `issue_comment` and `pull_request_target` do not inherit the ordinary fork-PR workflow approval gate. Inspect vulnerable workflow versions on other supported base branches too.

For `workflow_run`, allowlist the intended upstream workflow and inspect `github.event.workflow_run.event` for the expected initiating event, plus its repository, head SHA/ref, and conclusion. `github.event_name` identifies the consumer event (`workflow_run`), not its origin. A branch filter, matching workflow name, or `github.repository_owner` alone cannot authenticate the producer: a PR can change upstream workflow definitions/triggers. For example, a trusted-push consumer requires `github.event.workflow_run.event == 'push'` together with trusted repository/ref checks; a PR-result consumer deliberately accepts `pull_request` and keeps its output untrusted.

### Actions, caches, and artifacts

Compare external Actions/reusable workflows with official target-repository releases and full SHAs, reviewing changes before updating pins. A verified-creator badge verifies identity, not safe behavior. Actions can access `github.token` without an explicit token input, so audit every Action in a privileged job and its transitive dependencies, not only the step receiving a Secret.

Where supported and adopted, `.github/workflows/actions.lock` locks covered action dependencies, including transitive Actions and source-repository identity. Generate/update it with `gh actions-lock` and review its diff. It does not pin reusable workflow calls: keep those at full SHAs and check dependency locking in the called repository. Otherwise retain verified full-SHA pins and inspect nested references. Locks/pins do not establish safe contents or constrain runtime downloads, package dependencies, inputs, or runner images; verify container digests and fetched dependencies separately.

Keep artifacts passed from unprivileged builds to privileged processing untrusted. Select the artifact from the triggering run ID, matching repository, head SHA, event, and conclusion. Extract into a fresh temporary directory outside the workspace and executable/configuration paths; reject traversal, unexpected files, and links escaping that directory before use. Do not let extraction overwrite trusted scripts or load PR-produced binaries, modules, plugins, or configuration in privileged jobs. Read only bounded, expected data with strict schema/type checks. Validate a positive PR number and correlate it with the run through trusted GitHub API metadata before directing privileged API calls; artifact-supplied identifiers alone are not authorization. For writes, independently authorize the destination repository, PR/head branch, and operation against trusted metadata; valid branch syntax or equality with an artifact-supplied SHA does not establish that relationship. Completed/successful runs and matching digests establish neither content safety nor permission to publish a PR artifact.

Investigate cache creators/refs, effective cache access, and restoring jobs' permissions, including implicit setup-Action caching. `permissions: {}` restricts `GITHUB_TOKEN`, not every cache capability. Current GitHub.com defaults make default-branch caches read-only for low-trust triggers such as `pull_request_target`, `issue_comment`, and `workflow_run`; explicit write-capable `cache-mode` can override this. Check target-platform support and actual overrides, including reusable workflows. Explicitly cap the calling job at `cache-mode: read` or `none` where appropriate; an omitted caller limit can permit a called workflow to request writes. Ordinary `pull_request` caches are merge-ref scoped, not automatically writable into the base branch. Prevent low-trust cache content reaching privileged execution through shared paths or broad restore keys. Do not save Secrets/tokens/authentication settings. Digests/signatures/attestations require correspondence with allowed creators/workflows and do not prove safe contents.

## Validation and reporting

Select dependency, Secret, and static-security checks from existing coverage without uniformly adding every tool. CodeQL supports the `actions` language for workflow and Action metadata YAML; verify the target setup/version actually scans it, since application-language scanning alone does not cover these boundaries. Static findings complement execution-path review and do not prove absence of vulnerabilities.

Check attack strings remain data in isolated tests; do not test leaks or exercise privileges in real environments. For audits show locations, input sources, execution paths, effective permissions, impact, and minimal fixes under `code-review` criteria. Distinguish unreadable settings, unexecuted fixes, and unconfirmed reachability.
