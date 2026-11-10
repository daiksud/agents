---
type: Instruction
title: Commit messages
description: Apply recording and message conventions when staging and committing approved changes.
---

## Commit messages

### Check targets and evidence

- Draft from supplied diffs/change descriptions or requested target diffs. When investigating repositories, use `git status`, `git diff --cached`, and `git diff` to distinguish staged/unstaged work without mixing out-of-scope changes.
- Choose types, scopes, and descriptions from actual purposes and existing terminology, not filenames alone. Use confirmed background in bodies without guessing causes, intentions, alternatives, performance figures, validation, or Issue numbers.
- If information is insufficient, check existing Issues, specifications, and diffs, asking only about unresolved purpose/target. Do not require unnecessary background answers for simple-change drafts.

### Subjects, bodies, and footers

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to record change types and breaking changes. Format subjects as `<type>[optional scope][!]: <description>`, separate the body and footers with blank lines, and mark confirmed breaking changes with `!` or a `BREAKING CHANGE:` footer. Honor the target repository's adopted conventions rather than adding local type or length restrictions. Keep the reasons and evidence understandable from the message itself.

- Write ordinary commit messages, including body and footers, in English. Follow [Repository adoption](repository-adoption.md) for the target's PR-body language. Preserve existing local choices and resolve explicit language conflicts before publication.
- For squash and merge commits, preserve the final PR title and description verbatim as subject/body under [Integrate and merge](review-and-merge.md#integrate-and-merge). Do not replace, summarize, or translate away decisions or validation status at merge time.
- Write specific concise subjects and include the confirmed reasons and constraints needed to understand the change. Links supplement the message; they must not be necessary to understand the judgment. Do not leave unfilled fields or invent comparisons to fill a template.
- Use confirmed related Issue numbers. Use closing directives such as `Closes` or `Fixes` only when resolution by this change is confirmed; partial changes use references such as `Refs`.

### When committing

For drafting-only requests, present copyable messages and stop. Follow [Scope and plan](../SKILL.md#scope-and-plan) for Git operations, and [Branches and integration units](branches.md) for protecting other sessions' work and change units. Do not require approval for every commit within the same approved scope.

1. Treat related approved implementation, tests, and documents as units validating the same purpose. Do not split solely by file counts/extensions or include unrelated cleanup. Presenting decomposition proposals does not approve out-of-scope commits.
2. If staging is needed, check files/diff scope and add only approved targets. Do not stage whole files containing out-of-scope unstaged work. If others' staged changes are mixed in, do not arbitrarily unstage/move or commit them; confirm necessary coordination.
3. After drafting, immediately before committing check the complete staged diff matches approval. Compare every message claim with diffs/confirmed background and exclude unrelated changes or unverified reasons before committing. Check results after creation and follow explicit stop conditions.
4. For hook or other failures, do not claim success; recheck HEAD, status, and staged/unstaged diffs. Compare hook changes with approved scope, then retry ordinary commits after necessary fixes/revalidation and final index checks. Do not automatically bypass hooks or amend.

Historical change decisions belong in PR descriptions and commits even when current policy is revised. Remove all HTML comments from actual PR descriptions before capturing the merge message; preserve substantive content and actual validation status.
