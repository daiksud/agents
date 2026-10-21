---
type: Instruction
title: Commit messages
description: Commit messages follow the Conventional Commits specification.
---

## Commit messages

### Check targets and evidence

- Draft from supplied diffs/change descriptions or requested target diffs. When investigating repositories, use `git status`, `git diff --cached`, and `git diff` to distinguish staged/unstaged work without mixing out-of-scope changes.
- Choose types, scopes, and descriptions from actual purposes and existing terminology, not filenames alone. Use confirmed background in bodies without guessing causes, intentions, alternatives, performance figures, validation, or Issue numbers.
- If information is insufficient, check existing Issues, specifications, and diffs, asking only about unresolved purpose/target. Do not require unnecessary background answers for simple-change drafts.

### Subjects, bodies, and footers

- Write the entire commit message, including body and footers, in English under [Repository artifact language](../../../.apm/instructions/language.instructions.md). This also applies to squash commits; a repository-language PR body must not be copied unchanged into an English commit message.
- Title format is `<type>[(scope)][!]: <description>` (`[]` is optional), with a space after the colon.
- Use `feat` for features, `fix` for bugs, and appropriate other types such as `docs`, `refactor`, `test`, or `chore`. Scope is a noun for an existing area/module, omitted if unnecessary (for example `fix(parser): handle empty input`).
- Write specific concise English imperative subjects without final periods. Aim for 72 characters overall, without mechanical truncation or new enforced checks.
- Add bodies to supplement problems, reasons, impact, or decision constraints unclear from subjects/diffs. Simple changes may use subjects alone; do not leave unfilled fields or response prose.
- Add bodies/footers only as needed, separated from preceding sections by blank lines. Footers use `Token: value` or `Token #value`, replacing token spaces with `-` (except `BREAKING CHANGE`).
- Use confirmed related Issue numbers. Use closing directives such as `Closes` or `Fixes` only when resolution by this change is confirmed; partial changes use references such as `Refs`.
- This environment permits breaking changes only with `feat` or `fix`. This is a local convention differing from the standard's allowance of any type for breaking changes.
- For breaking changes, put `!` immediately before `:` and explain in the title, or add `BREAKING CHANGE: <description>` in the footer. Explain compatibility impact and known migration methods; absence of Issue references does not justify removing necessary explanations.

### When committing

For drafting-only requests, present copyable messages and stop. Follow “Planning and execution scope” in the dependency `issue-management` for Git operations, and [Branches and integration units](branches.md) for protecting other sessions' work and change units. Do not require approval for every commit within the same approved scope.

1. Treat related approved implementation, tests, and documents as units validating the same purpose. Do not split solely by file counts/extensions or include unrelated cleanup. Presenting decomposition proposals does not approve out-of-scope commits.
2. If staging is needed, check files/diff scope and add only approved targets. Do not stage whole files containing out-of-scope unstaged work. If others' staged changes are mixed in, do not arbitrarily unstage/move or commit them; confirm necessary coordination.
3. After drafting, immediately before committing check the complete staged diff matches approval. Compare every message claim with diffs/confirmed background and exclude unrelated changes or unverified reasons before committing. Check results after creation and follow explicit stop conditions.
4. For hook or other failures, do not claim success; recheck HEAD, status, and staged/unstaged diffs. Compare hook changes with approved scope, then retry ordinary commits after necessary fixes/revalidation and final index checks. Do not automatically bypass hooks or amend.
