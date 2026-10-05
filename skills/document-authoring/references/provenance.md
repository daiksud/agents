---
type: Guide
title: OKF provenance, trust, and lifecycle
description: Show claim/source mappings, generation versus verification, and handling content updates and freshness.
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2
---

## Connect claims to sources

For externally grounded documents, record material in a `sources` list. In this environment, link individual claims to footnotes with stable `id` values rather than only general related-material links. Each source requires `resource` when present; `id` and `title` are optional, but `id` is recommended for cited sources.[^okf-spec]

```markdown
---
type: Guide
title: Order retention period
description: Identify the authoritative source for checking retention periods.
sources:
  - id: retention-policy
    resource: https://example.com/policies/retention
    title: Retention policy
---

The retention policy defines order retention periods.[^retention-policy]

[^retention-policy]: Retention policy.
```

This is a format example, not proof of actual retention periods or retrieval results. Replace it with read material and actual claims when authoring.

Footnote labels join to `sources[].id`; do not determine sources by parsing footnote prose. Use IDs whose meanings survive reordering, without depending on position numbers such as `sources[0]`. This environment checks duplicate IDs, undefined footnotes, and sources without matching footnotes. Do not force footnotes for sources not cited in content.[^okf-spec]

Source `resource` may be external URLs, Bundle-relative/file-relative paths, or population/scope descriptions. Do not reject scope descriptions as nonexistent files. Preserve distributed material's external sources as complete URLs, and pin Git implementation evidence with complete SHAs. The latter is this environment's reproducibility choice.[^okf-spec]

## Preserve objective signals

Source `author`, `usage_count`, and `last_modified` are optional objective signals, not trust scores. `last_modified` is the source's own update time, separate from concept creation. Do not record viewing times as source update times.[^okf-spec]

When recording `usage_count`, connect observed counts to observation periods. Put `usage_window: { from, to }` at the same level as `sources`; periods on individual sources override the shared period. Do not compare scheduled execution counts and human views as rankings of equal precision. Unknown counts are not zero.[^okf-spec]

If internal concepts are sources, follow their `sources` to trace evidence. v0.2 does not standardize dedicated external-data-lineage fields. Do not delete custom keys from existing documents or add custom evaluation values as OKF-standard trust judgments.[^okf-spec]

## Separate generation and verification

`generated` represents creation of current content; `verified` represents checking events against sources/assets. All are optional; record only evidence-based values. `generated.by` is mandatory when present; `generated.at` is the last meaningful-change time. Do not make formatting alone appear to update facts.[^okf-spec]

`verified` accepts a list of `{ by, at }` or a single mapping with the same meaning. Single mappings are not nonconforming. The latest `at` indicates the latest check, but content updates and rechecking are independent.[^okf-spec]

```yaml
verified: { by: 'human:reviewer-id', at: '2026-09-11T09:00:00+09:00' }
```

Do not copy this into documents without actual verification. Identify verifier, time, and target content from actual evidence.

| Record | Meaning |
| --- | --- |
| No `verified` | Unverified; usable, but do not claim verified |
| Verification only by non-`human:` Actors | machine-confirmed |
| Verification by `human:<id>` present | human-reviewed |

Actors are `<producer>/<version>` for agents/tools, `human:<id>` for people, and `process:<id>` for automation. Use `human:` for human creation/verification. Do not substitute CI success for human checking, or record static-only CI as content comparison. Trust levels are not access controls.[^okf-spec]

## Status, datetimes, and expiry

`status` is `draft` (possibly unreviewed/incomplete), `stable` (usable), or `deprecated` (retained for history/links). Omission means `stable`, not human verification.[^okf-spec]

Use ISO 8601 datetimes with UTC offsets, such as `2026-09-11T09:00:00+09:00` or `2026-09-11T00:00:00Z`, for `generated.at`, `verified[].at`, `sources[].last_modified`, `usage_window.from/to`, and `stale_after`. Do not assume time zones for old date-only values; check evidence.[^okf-spec]

`stale_after` is an absolute time; expiry occurs when `now >= stale_after`, including exactly at expiry. Expired/unverified status alone is not a syntax error. Absence of expiry does not prove freshness; do not add expiry solely by convention.[^okf-spec]

## Updates and migration

1. First read existing `sources`, unknown keys, `generated`, `verified`, expiry, and content. Do not change citation IDs due to reordering.
2. Identify changed claims and their evidence. Even with equal source counts, check existing sources have not been replaced with different material.
3. Do not mechanically update generation/checking times or expiry for minor corrections. For meaning changes, verify actual generation facts and preserve prior checking history, explicitly stating in content or similar places that it checked pre-change content.
4. Add new `verified` events only after rechecking. If checking targets/scope cannot be recorded, retain uncertainty rather than reporting current content verified.
5. Migrate v0.1 content `Citations` to `sources` and footnotes after checking evidence. Old `timestamp` alone does not identify Actors; do not fabricate `generated.by`. Do not force rewrites merely to accept external v0.1 material.
6. Check saved diffs for lost sources, unknown keys, or history, and for altered datetime notation/values through YAML reading/writing.

These are this environment's update procedures based on specification preservation recommendations and generation/verification semantics. The specification defines no history-version-identification schema; use existing history management without requiring custom keys as norms.[^okf-spec]

[^okf-spec]: Fixed SPEC §§4.1, 5, 7, 11, 13. This environment's update procedures and additional checks are application decisions.
