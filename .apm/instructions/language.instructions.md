---
type: Instruction
title: Repository artifact language
description: Choose artifact language from artifact type and target repository conventions.
---

## Repository artifact language

This is the shared source of truth for language when using these Instructions and Skills in a target repository. The English prose of `daiksud/agents` is the language of these guidance files, not a blanket English requirement for artifacts created elsewhere.

| Artifact | Required language and format |
| --- | --- |
| Commit messages, including squash commits | Always English for subject, body, and footers; use Conventional Commits |
| Code comments, including docstrings | Always English; preserve the project's comment format |
| Issue and PR titles | Always English; use Conventional Commits |
| Issue and PR bodies and comments | Follow the target repository's language, English or Japanese |
| PR review comments, including review summaries and replies | Follow the target repository's language, English or Japanese |
| Repository documentation, including Markdown and feature documents | Follow the target repository's language, English or Japanese |

### Determine the target repository's language

1. Read explicit target-repository instructions, such as `AGENTS.md`, contributor guides, and applicable templates. Apply artifact- or path-specific language instructions to repository-language artifacts.
2. Where instructions do not specify a language, inspect established maintained content for the relevant artifact or path: nearby documentation, README, recent Issue/PR bodies, and review discussions. Use the consistent English or Japanese convention; do not infer prose language from programming-language statistics.
3. In a mixed repository, preserve the established convention of the artifact or area being updated. For a new artifact, use the closest relevant maintained examples, then the repository's predominant maintained prose if those provide no direction.
4. If explicit instructions conflict or neither English nor Japanese has a clear applicable convention, state the evidence and ask the user which repository convention to apply before publishing the affected artifact. Continue work that does not depend on that answer. Conversation language alone does not override repository conventions.

The always-English rows remain English in a Japanese repository. Preserve identifiers, commands, required syntax, exact quotations, and purposeful language examples when translation would change their meaning. A Japanese example in these English guidance files illustrates an artifact for a Japanese repository; it does not set the language of every target repository.
