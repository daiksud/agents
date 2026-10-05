---
type: Instruction
title: Commit messages
description: Commit messages follow the Conventional Commits specification.
sources:
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: commit-message-storyteller
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/commit-message-storyteller/SKILL.md
  - id: conventional-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/conventional-commit/SKILL.md
  - id: git-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/git-commit/SKILL.md
---

## Commit messages

### Check targets and evidence

- Draft from supplied diffs/change descriptions or requested target diffs. When investigating repositories, use `git status`, `git diff --cached`, and `git diff` to distinguish staged/unstaged work without mixing out-of-scope changes.[^git-commit]
- Choose types, scopes, and descriptions from actual purposes and existing terminology, not filenames alone. Use confirmed background in bodies without guessing causes, intentions, alternatives, performance figures, validation, or Issue numbers.[^commit-message-storyteller]
- If information is insufficient, check existing Issues, specifications, and diffs, asking only about unresolved purpose/target. Do not require unnecessary background answers for simple-change drafts.

### Subjects, bodies, and footers

- Title format is `<type>[(scope)][!]: <description>` (`[]` is optional), with a space after the colon.[^conventional-commits]
- Use `feat` for features, `fix` for bugs, and appropriate other types such as `docs`, `refactor`, `test`, or `chore`. Scope is a noun for an existing area/module, omitted if unnecessary (for example `fix(parser): handle empty input`).[^conventional-commits]
- Write specific concise English imperative subjects without final periods. Aim for 72 characters overall, without mechanical truncation or new enforced checks.[^commit-message-storyteller]
- Add bodies to supplement problems, reasons, impact, or decision constraints unclear from subjects/diffs. Simple changes may use subjects alone; do not leave unfilled fields or response prose.[^commit-message-storyteller]
- Add bodies/footers only as needed, separated from preceding sections by blank lines. Footers use `Token: value` or `Token #value`, replacing token spaces with `-` (except `BREAKING CHANGE`).[^conventional-commits]
- Use confirmed related Issue numbers. Use closing directives such as `Closes` or `Fixes` only when resolution by this change is confirmed; partial changes use references such as `Refs`.
- This environment permits breaking changes only with `feat` or `fix`. This is a local convention differing from the standard's allowance of any type for breaking changes.[^conventional-commits]
- For breaking changes, put `!` immediately before `:` and explain in the title, or add `BREAKING CHANGE: <description>` in the footer. Explain compatibility impact and known migration methods; absence of Issue references does not justify removing necessary explanations.[^conventional-commits]

### When committing

For drafting-only requests, present copyable messages and stop. Follow “Planning and execution scope” in the dependency `issue-management` for Git operations, and [Branches and integration units](branches.md) for protecting other sessions' work and change units. Do not require approval for every commit within the same approved scope.

1. Treat related approved implementation, tests, and documents as units validating the same purpose. Do not split solely by file counts/extensions or include unrelated cleanup. Presenting decomposition proposals does not approve out-of-scope commits.[^git-commit]
2. If staging is needed, check files/diff scope and add only approved targets. Do not stage whole files containing out-of-scope unstaged work. If others' staged changes are mixed in, do not arbitrarily unstage/move or commit them; confirm necessary coordination.
3. After drafting, immediately before committing check the complete staged diff matches approval. Compare every message claim with diffs/confirmed background and exclude unrelated changes or unverified reasons before committing. Check results after creation and follow explicit stop conditions.[^conventional-commit]
4. For hook or other failures, do not claim success; recheck HEAD, status, and staged/unstaged diffs. Compare hook changes with approved scope, then retry ordinary commits after necessary fixes/revalidation and final index checks. Do not automatically bypass hooks or amend.[^git-commit]

### Sources and application decisions

Checked fixed versions of three GitHub awesome-copilot resources, summarizing/restructuring commit-message-storyteller's purpose/reason writing guidance,[^commit-message-storyteller] conventional-commit's diff checks/structure,[^conventional-commit] and git-commit's purpose-based units and failure handling.[^git-commit]

Integrate with existing approval/change protection in this environment. Do not adopt fixed XML, unconditional commits after drafting, repeated “Story told” explanations, or removal of all footers without Issues. 72 characters guides readability; no uniform body-length limit is established.

[^git-commit]: Git Commit. Adopt actual-diff/purpose-based units and hook-failure handling, applying staging examples under existing change protection.
[^commit-message-storyteller]: Commit Message Storyteller. Adopt purpose/background/impact and subject writing, without guessing unverified background or fixed output formats.
[^conventional-commits]: Conventional Commits 1.0.0. Standard syntax, types, scopes, bodies, footers, and breaking changes.
[^conventional-commit]: Conventional Commit. Adopt diff/message agreement and structure, without XML or automatic execution from drafts.
