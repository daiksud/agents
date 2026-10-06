---
type: Guide
title: OKF basic format and references
description: Explain differences among ordinary concepts, indexes, and logs, and link resolution by Bundle boundaries.
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2
---

## Ordinary concepts and Bundles

A Knowledge Bundle is a directory tree serving as a distribution unit; a Concept is one knowledge document within it. A Concept ID is its Bundle-relative file path without the final `.md`. For a `docs/` Bundle, `docs/behavior/order.feature.md` has ID `behavior/order.feature`. Repository, domain, and Bundle boundaries need not coincide.[^okf-spec]

Ordinary concepts consist of UTF-8 Markdown content with initial YAML frontmatter, opened/closed by `---` on separate lines. Only a nonempty string `type` is mandatory; no type registry exists. Do not reject unknown types or additional keys. `title`, `description`, `resource`, and `tags` are recommended; the following also conforms.[^okf-spec]

```markdown
---
type: Local Idea
---

A concept under consideration.
```

Include `title` and `description` for concepts authored in this environment. `resource` identifies the asset represented by the concept, separate from `sources[].resource` recording evidence. Do not fabricate asset URLs for abstract concepts. Fixed content chapters are not required.[^okf-spec]

## Index and log exceptions

`index.md` and `log.md` are reserved names at any hierarchy level; do not use them for ordinary concepts. Both are optional; absence alone does not justify adding them. Do not give reserved files `type`, `title`, or `description`.[^okf-spec]

Make `index.md` lists of links grouped under headings. Descriptions are recommended to use linked targets' `description`. Normally no frontmatter is present; version declarations are allowed only at Bundle roots. Preserve existing root version declarations during updates.[^okf-spec]

```markdown
---
okf_version: "0.2"
---

# Guides

- [Order handling](behavior/order.feature.md) - Order acceptance conditions.
- [Design decisions](adr/) - Decisions and reasons.
```

In `log.md`, put flat dated updates newest-first. Date headings are actual `YYYY-MM-DD` dates. Initial bold labels are conventional, not mandatory. Log dates group events, separate from metadata recording datetime with UTC offsets.[^okf-spec]

```markdown
# Change log

## 2026-09-11

- Updated order acceptance conditions.

## 2026-09-10

- Added the first guide.
```

Do not interpret headings/footnotes in sample code blocks as outer-document structure.

## Reference resolution

Interpret Markdown links, `resource`, `sources[].resource`, `computation`, `executor.resource`, and `attester.resource` below. `sources[].resource` may also contain scope descriptions without retrieval targets, such as “all queries in project X”; do not treat all as file paths.[^okf-spec]

| Notation | Resolution basis | Example from `docs/guide/page.md` (Bundle `docs/`) |
| --- | --- | --- |
| `/tables/orders.md` | Bundle root | `docs/tables/orders.md` |
| `../tables/orders.md` | Current file's directory | `docs/tables/orders.md` |
| `https://example.com/policy` | External URL | Do not convert to local files |

The specification recommends Bundle-relative links with initial `/`. This environment chooses file-relative links for ordinary GitHub/APM Markdown viewing. When copying specification examples such as `references/...` into subdirectory documents, resolve them again from actual locations, such as `../references/...`.[^okf-spec]

Describe relationship types in text surrounding links. For claim evidence, use [Provenance procedures](provenance.md). `references/` is a conventional location for external material, procedures, or code, not mandatory.[^okf-spec]

Broken links may represent unwritten knowledge and do not invalidate OKF conformance. For this environment's authored documents, publication quality requires repairing local references or explicitly handling uncreated/inaccessible status. Do not arbitrarily follow files or symlinks outside Bundle boundaries to inspect/fix them.[^okf-spec]

[^okf-spec]: Fixed SPEC §§2–4, 6, 8–9, 11–12. This environment's additional conditions are distinguished in the text.
