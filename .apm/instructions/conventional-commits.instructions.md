---
description: Conventional Commit rules and decision records for agent-created changes.
applyTo: "**/*"
---

# Conventional Commit messages

- Write commit subjects in English as `<type>(<scope>): <description>`. Omit
  `<scope>` when it does not clarify the change.
- Use `feat` for a new feature and `fix` for a bug fix. Use an appropriate
  conventional type such as `build`, `chore`, `ci`, `docs`, `refactor`,
  `perf`, `style`, or `test` for other changes.
- Keep the subject concise and describe the change, not a sequence of edited
  files.
- Mark a breaking change with `!` immediately after the type or scope, and add
  a `BREAKING CHANGE: <description>` footer when the compatibility impact
  needs explanation.
- Include a non-empty commit body. For every non-trivial change, use separate
  `Context:`, `Decision:`, `Considerations:`, and `Impact:` paragraphs.
- Explain why the decision was made, alternatives or risks considered, and the
  resulting behavior. Do not use the body as a line-by-line diff summary.
- For a routine dependency bump, formatter-only change, or typo fix, a
  one- or two-sentence body is sufficient, but it must still state why the
  change was made.
- When an applicable architectural decision record exists, cite it as
  `ADR NNNN` instead of repeating its rationale.
- Use the same decision record in a non-trivial pull request description
  because squash merges preserve the pull request body as the commit body.
