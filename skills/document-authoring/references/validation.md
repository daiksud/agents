---
type: Instruction
title: Markdown and content checks
description: Define pre-publication Markdown quality checks and checks of document content, references, and diffs.
---

## Markdown and content checks

No OKF conformance validation is provided. Follow [Basic format and references](basic-format.md) and [Provenance, trust, and lifecycle](provenance.md) when authoring, preserving existing formats, sources, unknown metadata, and checking history.

- Format and check complete Markdown with rumdl using the existing repository configuration. Do not arbitrarily overwrite project settings. When no configuration exists, use a temporary configuration disabling MD013, MD033, MD034, and MD041, enabling MD060 with `style = "compact"`, and setting MD076 to `style = "tight"` with `allow-loose-continuation = true`. Keep other defaults, including MD025; apply the [computation-specific exception](computation.md) only to computation documents.
- Confirm the installed version and resolved configuration. Run `rumdl check --config <absolute-config-path> --deny-config-warnings --fix <file>`, inspect the diff, then run the same check without `--fix`. Confirm formatting is stable before publication, checking metadata, headings, links, lists, tables, and required format structures.
- If rumdl is missing or outdated, known necessary tools may be installed in an isolated project or temporary environment after checking source, version, and permissions. Confirm global changes, additional permissions/costs, or installations whose provenance is unverified. Inability to execute is not a pass.
- For GitHub posts, use the target template without OKF frontmatter, retain substantive actual validation status, and remove HTML comments from published descriptions. Retrieve saved bodies to verify agreement and rendered structure; API/HTML inspection alone is not visual screen inspection.
- Check categories, terminology, links, documented commands, and diffs.
- For Instructions and Skills, apply [Agent-document separation](agent-documents.md): check that required rules and conditional operational references remain reachable, source mappings survive in maintainer notes, and normal execution does not acquire a blanket read of those notes. Preserve required licenses and attribution.
- For reader-facing technical prose, apply [Review task completion before presentation](technical-writing.md#review-task-completion-before-presentation) to the changed scope. Check usefulness and accuracy before wording, and separate executed walkthroughs from static inspection or unavailable checks; minor spelling or metadata edits do not require a new walkthrough.
- Check feature headings/steps after formatting. Read source content and contract meanings as well.
- Do not report Markdown success as OKF conformance, source truth, human content checking, or proof of computation execution. Distinguish unverified, expired, and unexecutable checks.
