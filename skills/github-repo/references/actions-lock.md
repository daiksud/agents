---
type: Instruction
title: Lock GitHub Actions dependencies
description: Adopt and maintain workflow dependency lockfiles, resolve coverage gaps, and prepare safe enforcement.
---

## Scope and prerequisites

When the target repository uses GitHub Actions, use `gh actions-lock` and commit `.github/workflows/actions.lock` [MUST]. The purpose is to reduce unexpected replacement of dependency Actions, including transitive dependencies. Locking does not prove that the selected dependency code is safe.

Use this procedure only within the requested scope. Diagnosis remains read-only; installation of this skill does not authorize dependency or setting changes. Report unavailable access, unsupported environments, and incomplete coverage through [Operations and judgments](operations.md); do not silently substitute SHA pinning or count an unmet requirement as conforming.

Install GitHub CLI, authenticate to the target host, and install the official extension before an authorized onboarding:

```bash
gh auth login
gh auth status
gh extension install github/gh-actions-lock
```

Reuse an existing authenticated session and extension. The extension supports github.com and GitHub Enterprise Cloud with data residency, but not GitHub Enterprise Server. For host-specific authentication, cross-host token handling, current options, or installation problems, consult the [extension usage guide](https://github.com/github/gh-actions-lock/blob/main/README.md). Never print credentials or obtain broader permissions merely to complete diagnosis.

## Onboard and enforce

1. Inspect every workflow and its Action dependencies, local composites, reusable-workflow calls, and container references. Review the intended versions and original upstream repositories before resolving them. Identify coverage gaps below and preserve the target's existing permissions, validation, and runtime behavior.
2. Run `gh actions-lock` from the target repository checkout. It generates the lockfile and can narrow workflow version references, such as a major tag to a specific version. Do not edit generated lockfile entries manually.
3. Review the complete diff: workflow references, locked commits, repository identities (`owner_id` and `repo_id`), and workflow coverage. Investigate unexpected identity or commit changes before accepting them; regenerating a lockfile is not a security review.
4. Run `gh actions-lock --verify`. Resolve errors and assess warnings against the intended dependency versions. A locked floating reference may legitimately differ from the latest upstream commit; verification is not a requirement to adopt every upstream update.
5. Deliver the reviewed workflows and lockfile together through [Approved file changes](operations.md#approved-file-changes). Complete the target's required review and CI, and confirm the merged files before activating dependent settings. Do not create a release or deployment merely to test adoption.
6. Apply authorized enforcement through [Setting standards](settings.md). Confirm coverage for every targeted workflow and relevant branch or tag, including called reusable workflows. Keep the setting unapplied where preparation is incomplete, report the remaining work, and retrieve the effective setting after application.

Use an existing suitable CI check for `gh actions-lock --verify` when PR verification is requested or required by target policy. A separate workflow is not required. Keep any verifier's credentials minimal, and complete coverage for that workflow too.

## Resolve coverage gaps

| Dependency or policy | Required handling |
| --- | --- |
| External reusable workflow (`jobs.<job_id>.uses`) | Pin the call to a full commit SHA. The caller's lockfile does not lock this call or the called workflow's dependencies; those dependencies require the source repository's own lockfile. An active Require lockfile policy can block the caller when the called workflow is not onboarded. |
| Local Action (`./...`) | It runs from the checked-out workspace and is not followed or locked by the extension. Retaining it with `--ignore-local-actions` is appropriate only when workspace semantics are intentional and it invokes no uncovered Action dependency. Each lockable external Action it invokes needs an entry for the same workflow; another workflow's entries do not suffice. The flag does not create missing pins. Preserve and report unresolved references instead of concealing a gap. |
| Same-repository Action (`$/...`) | It runs from the workflow's own commit and allows its Action dependencies to be locked. `--migrate-local-actions` changes `./...` to `$/...`; these forms are not interchangeable when checkout selects different code. Migrate only after establishing the intended behavior. Otherwise preserve the reference, report the gap, and hold affected enforcement. |
| Container image | Images are outside lockfile coverage. Inspect `docker://` Actions, job containers, and service images separately; use an immutable `@sha256:` digest for images that must be pinned. |
| Workflow without `uses:` | Require lockfile still requires the targeted workflow to be onboarded. Check its workflow entry rather than assuming that having no Action dependencies exempts it. |
| Native full-SHA policy | A workflow onboarded to a lockfile satisfies Require actions to be pinned to a full-length commit SHA. Keep stronger existing policy; do not rewrite every covered Action reference to a SHA merely to satisfy it. External reusable-workflow calls still need separate SHA pinning. |
| Allowed Actions policy | Onboarded workflows are checked against locked SHAs rather than tags. Inspect the existing allowlist before rollout: a tag-only allowance may no longer match. Propose an approved exact-SHA or suitable wildcard entry without silently broadening access or bypassing inherited policy. |

For an uncovered dependency or a changed tool behavior, use the [official onboarding procedure](https://docs.github.com/en/actions/how-tos/secure-your-work/lock-workflow-dependencies) to choose a supported resolution before enforcing the policy.

## Maintain the lockfile

- Run `gh actions-lock` after adding or removing workflows or changing Action dependencies, including dependencies inside composites. Review and commit the generated changes with the source changes. A full-directory run also removes entries for deleted workflows; a scoped run does not clean up other workflows.
- Use Dependabot's `github-actions` updates when enabled by target policy. It updates matching lockfile entries for already onboarded workflows; it does not onboard a new workflow. Review dependency changes even when generated by Dependabot.
- Use `gh actions-lock --relock` only after reviewing why a branch or tag moved and deciding to advance its pin. Ordinary runs retain locked floating references. A moved full-version tag or unreachable recorded commit requires investigation, not blind regeneration.
- Never use `--accept-moved` in automation. Consider it only after investigating the upstream history and confirming that acceptance is within the approved dependency change. Review lockfile diffs for unintended downgrades, which a still-reachable floating-reference commit may not expose automatically.
- Distinguish `--verify` from `--verify-local`: the former checks online provenance and consistency; the latter checks offline coverage only. Do not describe the local check as equivalent protection.
- Keep PR verification and runtime enforcement distinct. The runner uses locked commits for onboarded workflows; Require lockfile also prevents targeted workflows from escaping adoption. Consult the [enforcement procedure](https://docs.github.com/en/actions/how-tos/administer/enforce-workflow-lockfiles) when targeting or policy behavior is unclear.
