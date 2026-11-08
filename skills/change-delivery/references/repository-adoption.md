---
type: Guide
title: Adopt repository change records
description: Apply local change-record conventions and publication checks within approved delivery.
---

## Adopt within the approved change

Keep the current working rules a contributor needs in repository documents, and retain historical judgments and reasons in PRs and commits. Code expresses behavior and structure; tests express observable contracts. Comments beside code explain why a plausible alternative fails a current constraint. Choose only the recording locations needed for the change.

At the start of repository change work, inspect the target's local instructions, effective templates, current documentation, and existing adoption decisions. Accept equivalent arrangements and address confirmed gaps relevant to the approved work. Keep current rules in local files and adoption reasons in PR descriptions and commits. Do not repeatedly ask about a recorded deferral or block unrelated work on adoption.

Show concrete paths and changes before applying adoption. Deliver approved file changes through ordinary branch, PR, review, CI, and merge procedures. If adoption exceeds the approved scope, present the proposal and continue unaffected work. Installation alone does not copy assets, adopt rules, or apply GitHub settings.

## Preserve target conventions

For repositories adopting verbatim PR records, propose English PR bodies. Preserve explicit local choices, resolve language conflicts before publication, and retain the agreed text at merge without translation.

Adapt adopted instructions and local links to the target. Keep consumer rules understandable without the installed agents package; do not copy this distribution repository's entire `AGENTS.md` or its APM/independent-validation exclusions.

## Record content

- Use English [Conventional Commits titles](conventional-commits.md#subjects-bodies-and-footers) for Issues and PRs. Applying the commit convention to these titles is a local policy, not a requirement of the specification. Bodies and comments follow target-repository language conventions.
- Issue bodies state the desired outcome, success conditions, scope, order, validation, and known constraints. PR bodies describe the actual change and resulting behavior, with the confirmed facts, reasons, alternatives, and trade-offs needed to understand the judgment without following links.
- Prefer the target's template. Otherwise use Summary, optional Decisions, and Validation for PRs; equivalent local headings are acceptable. Retain substantive actual validation status, including `Not run` for discretionary checks. Preserve independently required CI and acceptance conditions.
- Remove all HTML comments from actual descriptions. Do not invent reasons or unperformed checks to fill sections. Update the final PR body when review changes content, decisions, or validation, then preserve its title and body verbatim at merge.

## Publish and verify records

1. For updates, retrieve and preserve the existing body. Save the complete intended body in a temporary Markdown file. Use headings, lists, and tables only where they aid understanding; GitHub posts do not use OKF/YAML frontmatter.
2. Check installed rumdl and the applicable configuration. For GitHub posts, use defaults except disabled MD013, MD033, MD034, and MD041; enable compact MD060 and tight MD076 with loose continuations allowed. Honor equivalent target configuration and resolve actual conflicts without overwriting project settings. Known necessary versions may be installed in an isolated temporary environment within existing permissions; additional authority or global changes require confirmation.
3. Format with `rumdl check --config <configuration> --deny-config-warnings --fix <body-file>`, inspect the diff, then check without `--fix`. Confirm formatting again makes no changes. Hold publication if required formatting cannot pass; inability to run it is not success.
4. Post the checked file with a `--body-file` option or corresponding structured API argument. Retrieve the saved body, compare with the file, and check GitHub rendering of the used structures. HTML retrieval alone is not visual screen inspection. For Issue URLs, open once only when the user requests it; do not duplicate a confirmed save to recover a failed opening.
5. Present the confirmed URL and requested content, distinguishing saving, rendering, and opening results. For Issues, present the saved plan body as well. Preserve successful steps when resuming and correct any content/display mismatch before claiming completion.

## Apply settings in their authorized scope

Inspect the target's merge settings and effective branch rules before proposing changes. For requested adoption of verbatim records, allow squash and merge-commit merging, prohibit rebase merging, and use `PR_TITLE` / `PR_BODY` as both methods' title/message defaults. Align branch rules with the authorized methods; show any linear-history conflict before changing that setting. Apply only authorized differences through the supported GitHub settings UI or [repository API](https://docs.github.com/en/rest/repos/repos#update-a-repository), then retrieve settings and compare. When adopting a commit-message check, confirm that its job runs for the target PR events before making it required, and preserve other required checks.

Record which settings were actually verified or applied. File adoption does not itself authorize live settings changes, and explicit merge messages do not establish that repository defaults changed. Preserve required approvals and CI throughout delivery.
