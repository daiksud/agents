---
type: Reference
title: OKF v0.2 specification audit and adoption decisions
description: Map norms, use cases, and document-authoring adoption decisions to each pinned specification section, and record differences from the reference implementation.
sources:
  - id: spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Authoritative OKF v0.2
  - id: migration
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62651738dab0b497b0e3fd804c87bcd235f027b8/okf/README.md
    title: Migration and frozen-copy guidance
  - id: frozen-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62651738dab0b497b0e3fd804c87bcd235f027b8/okf/SPEC.md
    title: Frozen specification at the former location
  - id: timestamps
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/commit/3dc3029168d2f98e331feeb4ca05c9178973a9b9
    title: Change to datetimes with UTC offsets
  - id: conformance-edit
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/commit/0b87c52c6ef999286c745e19998fdfcd03d5dbee
    title: Removal of duplicate datetime conformance conditions
  - id: document
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/bundle/document.py
    title: Reference parser and trust/freshness handling
  - id: writer
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/tools/bundle_tools.py
    title: Reference writing process
  - id: viewer
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/viewer/generator.py
    title: Reference viewer link and metadata handling
  - id: attester
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/bundles/acme_retail/attesters/sql_equality.py
    title: Reference SQL attester
---

## Authoritative source and interpretation

The adopted authoritative source is SPEC v0.2 at full SHA `ad30107c31c06aec8a7d5636e0d1058118604e6f` in the migration destination, `open-knowledge-format`. The former location advises that it is a frozen copy and should not guide new development. The inspected frozen SPEC body matched the pinned authoritative source.[^migration][^frozen-spec][^spec]

“Required,” “recommended,” and “optional” below indicate specification strength. Do not confuse authoring requirements with §11 minimum conformance. In particular, authors check optional family formats, but not every deficiency is grounds for rejecting external Bundles.[^spec]

## Section mapping

| Section | Requirements, recommendations, and options | Use case | Local adoption decision |
| --- | --- | --- | --- |
| §1 Motivation | Goals and non-goals. Replacing runtimes, taxonomy registration, or domain schemas is outside scope | Applicability | Retain existing contract formats |
| §2 Terminology | Definitions of Bundle, Concept, ID, Source, Actor, and others | Placement and references | ID is the within-Bundle path without `.md` |
| §3 / §3.1 | Distribution form is optional. Do not use reserved names for concepts | Document placement | Default Bundle is `docs/` |
| §4.1 | `type` required; display items recommended. Unknown types/keys permitted; retaining unknown keys recommended | Ordinary concepts | Additionally require title and description only for self-authored documents |
| §4.2 | Structured Markdown recommended. No fixed body sections | Body authoring | Use GFM alongside feature-specific notation |
| §4.3–4.4 | Examples with and without assets | Resource decisions | Do not invent URIs for abstract concepts |
| §5 preamble | Each family optional. Datetimes use ISO datetime with offsets | Datetime recording | Do not fill in unknown datetimes |
| §5.1 | Source resource required when included. IDs/signals optional; IDs recommended when citing | Source-backed creation and updates | Use sources and stable-ID footnotes |
| §5.2 | generated.by required when included. verified is an event list; a single mapping is also permitted | Creation and content cross-checking | Distinguish creation from cross-checking and history from current content |
| §5.3 | Derive trust tiers from verified. Do not reject unverified documents | Trust display | Do not convert CI success into human verification |
| §5.4 | status is draft / stable / deprecated, default stable | Lifecycle | Do not equate stable with verified |
| §5.5 | stale_after optional; stale at or beyond the deadline | Freshness decisions | Absence is not a guarantee; warn on expiration |
| §6.1 | Bundle-root links recommended; relative links allowed; broken links must be tolerated | Related documents | Adopt file-relative links for GitHub and APM |
| §6.2–6.3 | URLs, Bundle-root and relative paths. references is conventional | Path fields | Use full URLs for external sources; permit scope descriptors |
| §7 | Actor conventions. Human generation and verification require human: | Actor recording | Record only real actors |
| §8 | index optional, with headings and link lists. Frontmatter only for root version declaration | Indexes | Do not force new indexes |
| §9 | log optional, YYYY-MM-DD date headings, newest first | History | Record real dates; do not require bold labels |
| §10.1–10.2 | Computations are separate concepts. runtime required; contract fields defined | Computation contracts | State runtime, parameters, and references |
| §10.3–10.4 | One body computation fence or a file. Consumers specify only declared values | Computation use | Separate definition changes from value specification |
| §10.5 | Informative model of execution, attestation, and presentation | Verification procedures | Do not add execution platforms or store evidence in Bundles |
| §10.6 | verified concerns definitions; attestation concerns one execution | Interpreting proof | Do not treat success of one as proof of the other |
| §11 | Minimum conformance. Do not reject for absent optional families, unknown types/keys, broken links, or missing index | Specification understanding | Do not provide conformance judgments |
| §12 | Root version declaration optional; best effort recommended for unknown versions. ABI and others deferred | Version handling | Retain version declarations; do not mandate unadopted proposals |
| §13.1–13.2 | Migrate timestamps and Citations. Legacy fallback optional | Existing document updates | Check grounds for migration; do not infer Actors |
| Appendix A | Migration worked example | Understanding | Do not copy hypothetical Actors, datetimes, or all families |

Section summaries follow the pinned SPEC. Local adoption decisions are document-authoring operational policies, not OKF conformance validation.[^spec]

## Changes to datetime handling

The datetime change unified formerly date-only `stale_after`, source update datetimes, and usage periods as datetimes with UTC offsets. Log date headings are excluded. The reference Python implementation removed PyYAML's implicit timestamp conversion to retain datetime notation as strings.[^timestamps][^document]

A consumer MUST concerning datetimes in §11 during the change was removed by a later deduplication commit. The adopted final version describes datetime formats in §5; do not cite strong rejection or ignoring rules from older commit text as current conformance conditions. The reference implementation's `is_stale` ignores values lacking offsets or `T`; distinguish that implementation behavior too.[^conformance-edit][^document]

## Do not make reference implementations normative

| Target | Observed behavior and limits | Local treatment |
| --- | --- | --- |
| document.py | validate checks only type truthiness. Retains unknown keys in mappings and normalizes verified mappings | Reference parser success does not guarantee document content or quality |
| bundle_tools.py | Writes supplied frontmatter and supplements generated. Does not automatically merge existing content. BigQuery protection in web pass compares source counts | Read diffs; this is not a general guarantee against same-count source replacement or unknown-key loss |
| viewer/generator.py | Ignores leading `/` links, extracts limited body `.md` links. Display data centers on known keys. Does not exclude log as reserved | Viewer display does not prove reference/unknown metadata completeness or reserved-file conformance |
| sample sql_equality.py | Does not inspect bound values; compares SQL and results in receipts. Does not retrieve job results again | Do not call this complete execution proof; check necessary evidence per contract |

These are findings from reading fixed-SHA code, not reproducing upstream execution or cloud connections.[^document][^writer][^viewer][^attester]

Specification samples include expressions not straightforwardly matching body rules, such as `team:` source authors or indented computation examples. Do not elevate sample values into independent mandatory requirements; prioritize normative text when authoring. Do not automatically delete or convert extensions in external materials. Future runtime protocols, ABI, cache, and semantic-layer templates are deferred in §12; do not mix unadopted proposals into v0.2 requirements.[^spec]

[^migration]: Migration and frozen-copy guidance in the former README.
[^frozen-spec]: Inspected frozen SPEC.
[^spec]: Authoritative SPEC v0.2. Normative and informative provisions classified according to its text.
[^timestamps]: Datetime unification change and reasons.
[^document]: Reference parser, trust tiers, and freshness logic.
[^conformance-edit]: Subsequent removal of duplicate conformance conditions.
[^writer]: Reference writing code.
[^viewer]: Reference viewer code.
[^attester]: Reference SQL attester code.
