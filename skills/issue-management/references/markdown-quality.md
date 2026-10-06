---
type: Instruction
title: Markdown quality for GitHub
description: Define common rumdl configuration, installation permission, GFM structure, formatting before posting, and verification after posting.
sources:
  - id: rumdl-getting-started-installation
    resource: https://rumdl.dev/getting-started/installation/
  - id: rumdl-md060
    resource: https://rumdl.dev/md060/
  - id: rumdl-md076
    resource: https://rumdl.dev/md076/
  - id: github-docs-global-settings-md
    resource: https://github.com/rvben/rumdl/blob/main/docs/global-settings.md
---

## Markdown quality for GitHub

When Issue/PR numbers or commit SHAs follow Japanese text or punctuation, put ASCII spaces before and after them, do not wrap them in code notation, and check automatic links after posting.

Apply when newly posting/updating Issue/PR bodies or comments, and creating/updating repository Markdown. Read-only consultation/explanation does not require formatting or installation.

### Structure and display

- Do not add OKF or YAML frontmatter to GitHub posts. Apply the relevant OKF/Agent Skills format to repository documents.
- Follow destination templates. If unspecified, choose paragraphs, headings, and lists needed for understanding. Do not require fixed headings, unnecessary tables/Alerts, empty sections, or “none” filler.
- Use Emoji, tables, and Alerts where useful for identification, comparison, or important constraints. State pending approval, exclusions, unverified results, and other important information even without decoration.
- Remove unnecessary blank lines between simple-list items, preserving meaningful structures and spacing for multiple paragraphs, code blocks, and nesting.
- rumdl does not choose content structure. Prepare understandable content before mechanical formatting.

### Common configuration

Use [Common rumdl configuration](../assets/rumdl.toml), taking `assets/rumdl.toml` in the loaded skill as the basis.

| Setting | Content |
| --- | --- |
| Disabled | Only MD013, MD033, MD034, and MD041; allow long lines, HTML, bare URLs, and no initial H1 |
| MD060 | Explicitly enable compact formatting to remove extra column-width spaces |
| MD076 | tight removes spacing between simple items; allow-loose-continuation preserves multiparagraph structure |
| Others | Keep defaults such as MD003. Keep MD025 enabled, adjusting title counting only for computation documents below |

Explicitly specify common configuration for GitHub post bodies. Check existing repository configuration without arbitrarily replacing project-specific settings. If existing configuration conflicts with common policy, record resolution in the plan; for changes to purpose, acceptance conditions, or authority, confirm through starting/planning conditions.

### rumdl availability and installation permission

1. Check installed `rumdl --version` and `rumdl config --config <configuration-file> --output json`. Do not ignore warnings or missing required rules.
2. If missing/outdated, prepare the known necessary version in isolation under [Preparing the validation environment](planning.md#preparing-the-validation-environment), recording target, version, location, and reason.
3. Temporary execution involving downloads follows the same criteria. Confirm global configuration changes, additional permissions, costs, or unknown-source installation.
4. After installation, check version/configuration and validate. If refusals/environment restrictions prevent execution, explain unverified scope and hold posts that cannot pass necessary validation.

### From formatting to post-publication checking

1. For updates, retrieve existing bodies and preserve originals. Retain structure, results, and links, saving the complete body in a temporary Markdown file. Check complete bodies for additions too, not just added sections.
2. Specify common configuration with an absolute path and run in this order. Replace `<body-file>` and `<common-configuration>` with actual paths.

   ```bash
   rumdl check --config <common-configuration> --deny-config-warnings --fix <body-file>
   rumdl check --config <common-configuration> --deny-config-warnings <body-file>
   ```

3. Inspect formatted diffs, then format again and confirm no difference. Preserve meaning while fixing remaining findings, and do not post before passing. Repair deformed necessary paragraphs/code structures and revalidate.
4. Post the formatted file with `gh issue create --body-file`, `gh issue edit --body-file`, `gh pr create --body-file`, `gh pr edit --body-file`, `gh issue comment --body-file`, `gh pr comment --body-file`, or corresponding APIs. Do not manually reconstruct formatted strings.
5. Retrieve saved bodies and compare with formatted files. For Issues, follow [Opening the browser after saving an Issue](issue-recording.md#opening-the-browser-after-saving-an-issue), opening once only when requested. Check used headings, tables, Alerts, links, and lists in GitHub rendering, distinguishing unnecessary `li > p` in simple lists from intentional multiple paragraphs. Verify bodies/display regardless of opening; opening success alone is not visual verification. API HTML checks alone must not be reported as visually inspecting the screen.
6. For unnatural display, fix source files and repeat formatting, checks, posting, and retrieval.

Apply the same formatting/checking before saving repository documents, checking frontmatter, heading hierarchy, relative links, and feature steps. If ordinary-concept titles and H1s duplicate under MD025, adjust content heading levels. For `type: Attested Computation` with computation definitions, the specification requires `# Computation`; add `--config 'MD025.front-matter-title = ""'` to existing configuration for that document only. Keep MD025 and duplicate-body-H1 checks enabled; do not avoid this by changing computation H1 to H2. Check specific contracts and validation in the dependency [document-authoring computation material](../../document-authoring/references/computation.md).

### References

- rumdl installation[^rumdl-getting-started-installation]
- MD060: compact formatting[^rumdl-md060]
- MD076: list-item spacing[^rumdl-md076]
- Common configuration inheritance[^github-docs-global-settings-md]

[^rumdl-getting-started-installation]: [rumdl installation](https://rumdl.dev/getting-started/installation/). Evidence for the reference scope and adoption decisions stated in the text.
[^rumdl-md060]: [MD060: compact formatting](https://rumdl.dev/md060/). Evidence for the reference scope and adoption decisions stated in the text.
[^rumdl-md076]: [MD076: list-item spacing](https://rumdl.dev/md076/). Evidence for the reference scope and adoption decisions stated in the text.
[^github-docs-global-settings-md]: [Common configuration inheritance](https://github.com/rvben/rumdl/blob/main/docs/global-settings.md). Evidence for the reference scope and adoption decisions stated in the text.
