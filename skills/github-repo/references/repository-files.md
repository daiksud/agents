---
type: Instruction
title: Repository configuration files
description: Configure dependency updates, ownership, contribution templates, and vulnerability reporting with their GitHub prerequisites.
---

## Adopt existing configuration

Inspect the target's default branch, existing files, applicable community-health defaults, enabled features, and maintainers. Keep equivalent configuration and the target's language. Add only the missing files needed for the requested scope; file changes do not themselves enable dependent GitHub settings.

Check effective inherited templates before adding local files. A valid local Issue template or `.github/ISSUE_TEMPLATE/config.yml` prevents GitHub from using the entire inherited Issue-template directory; preserve the intended submission choices.

## Dependabot version updates

Repositories with supported dependencies SHOULD configure version updates in `.github/dependabot.yml` on the default branch. Match each ecosystem and directory to actual manifests. Preserve existing schedules, grouping, ignore rules, and registry choices unless changing them is requested. Consult the [options reference](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference) for current ecosystem support.

For GitHub Actions, use `package-ecosystem: github-actions` and `directory: /`, even though workflows are under `.github/workflows`. This example covers only Actions; its weekly schedule is a starting example, not a replacement for an existing cadence:

```yaml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
```

Version-update configuration is separate from enabling Dependabot alerts and security updates. Inspect the saved configuration and recognized manifests, then check update-job results and resulting PRs when available. A file's presence or an absence of update PRs does not prove successful coverage. Keep ordinary review and required checks for dependency updates.

## Code owners

Repositories SHOULD use CODEOWNERS to identify responsible maintainers and route reviews. Prefer `.github/CODEOWNERS` for new configuration; respect an existing effective file. GitHub searches `.github/`, the repository root, then `docs/`, and uses the first file found. PRs use the file from their base branch.

Use real users or visible teams with explicit write access to the target. Include ownership of CODEOWNERS itself. Replace `@OWNER` below with a verified maintainer before saving; add path-specific rules only where responsibilities differ:

```text
* @OWNER
/.github/CODEOWNERS @OWNER
```

Later matching patterns take precedence. Check effective ownership of representative paths and CODEOWNERS itself, and inspect GitHub's reported syntax errors. A nonexistent owner or insufficient access does not assign ownership. Draft PRs receive automatic owner review requests when marked ready.

If owner approval is intended as a merge requirement, configure the corresponding Ruleset or branch-protection condition after confirming an eligible approver and feature availability. The file alone does not enforce approval; one of multiple owners can satisfy the owner requirement. Do not invent reviewers or impose an unsatisfiable approval requirement on a solo repository. Compare the effective rule and actual PR mergeability separately from file validity.

## Issue and PR templates

Repositories using Issues for reports and proposals SHOULD provide concise Issue templates. Repositories accepting PRs SHOULD provide a concise PR template. Keep equivalent existing templates; use the bundled starting points only where they add missing guidance:

| Bundled file | Target location |
| --- | --- |
| [Bug report](../assets/issue-templates/bug_report.yml) | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| [Feature request](../assets/issue-templates/feature_request.yml) | `.github/ISSUE_TEMPLATE/feature_request.yml` |
| [Template chooser](../assets/issue-templates/config.yml) | `.github/ISSUE_TEMPLATE/config.yml` |
| [PR template](../assets/pull_request_template.md) | `.github/pull_request_template.md` |

Merge templates into the default branch before expecting them to appear. Issue Forms use YAML and do not apply to PRs. If Issues are disabled, do not enable them merely to install templates without an applicable request.

- Require only the problem or desired outcome initially; make reproduction details, environment, and solution ideas optional unless the target needs them. Avoid mandatory questionnaires and long checklists.
- Keep a blank-Issue entry with `blank_issues_enabled: true` unless the target deliberately restricts public submissions. Setting it to `false` still leaves a maintainer-only blank option for users with write access or higher.
- Add labels, assignees, projects, and contact links only after verifying their existence, permissions, and intended use. Issue Forms do not create missing labels.
- Keep PR guidance to Summary, optional Decisions, and actual Validation results. Remove authoring HTML comments from submitted bodies. Templates guide authors; they do not enforce review, CI, or lasting body completeness.

Check YAML/schema validity and the saved default-branch files. When available, inspect the Issue chooser and unsubmitted Issue/PR creation forms for the intended fields, blank option, and prefilled PR body. Do not submit dummy Issues or PRs merely to validate templates; distinguish static checks from observed UI behavior.

## Security policy

Maintained projects SHOULD provide `.github/SECURITY.md`, or an equivalent effective security policy, stating supported versions or branches and a real private vulnerability-reporting channel. Confirm the maintainers' support scope and monitored destination; do not invent mailboxes, service commitments, or a vulnerability response process.

Use this outline only after replacing both placeholders with confirmed information:

```markdown
# Security policy

## Supported versions

<Maintained versions or branches.>

## Report a vulnerability

<Verified private reporting URL or monitored contact.>
```

If using GitHub private vulnerability reporting, verify it is available and enabled before advertising that route. The Markdown file does not enable the feature. Check the effective policy shown on the Security page and the reporting destination without submitting a test vulnerability. If the channel is undecided, report the missing decision instead of publishing a nonfunctional policy.
