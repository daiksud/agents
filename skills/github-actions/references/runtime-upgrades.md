---
type: Instruction
title: Upgrading Action internal runtimes
description: Identify deprecation-warning sources and compatibility, upgrading and validating Actions without confusing application runtimes.
sources:
  - id: copilot-runtime
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md
  - id: github-metadata
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax
  - id: actions-checkout
    resource: https://github.com/actions/checkout
  - id: actions-setup-node
    resource: https://github.com/actions/setup-node
---

## Identify warning sources

Retrieve run warnings, target SHA, event, runner, and steps, tracing direct/indirect Actions. JavaScript Action `runs.using` in `action.yml`/`action.yaml` is its internal runtime, separate from `setup-node` `node-version` or application `engines`. Inspect inner Actions in composites/reusable workflows.[^github-metadata]

For warning removal alone, do not update unrelated application Node.js, locks, build settings, or job structures. Hiding warnings through environment variables or replacing runtime declarations without Action support is not a permanent fix. Without compatible releases, show constraints, upstream status, alternatives, and uncertainties.[^copilot-runtime]

## Compare compatibility and references

1. Check current complete SHA/version comment/metadata and target stable releases/notes. Resolve tag commits in official repositories; for annotated tags trace tag objects to commits, without pinning shortened SHAs or tag names alone.
2. Check target-version runner requirements, OS/architecture, and GitHub.com/GHES support. Old self-hosted runners do not imply authority to upgrade them.
3. Check inputs, removals/defaults, outputs, checkout authentication/fork conditions, caches, and artifact names/content/retention/signatures. Internal-runtime descriptions alone do not prove unchanged behavior; checkout/setup-node defaults also change by version.[^actions-checkout][^actions-setup-node]
4. Update compatible full SHAs with correct version comments. Search other workflows/composites/reuse targets and align necessary callers; do not uniformly replace references with different compatibility needs.
5. Upgrade/validate small groups of related Actions, reading [Safety](hardening.md) when permissions, inputs, authentication, or cache boundaries change. Do not copy old example SHAs or fixed recommended majors.

Commands for reading target evidence (replace repository/tag with actual values):

```bash
gh release view TAG --repo OWNER/ACTION
gh api repos/OWNER/ACTION/commits/TAG --jq .sha
```

Missing releases or unconfirmed version-comment/commit relationships are not verified.

## Separate validation

| Check | Evidence obtained |
| --- | --- |
| Static | Consistency of YAML, expressions, full SHAs, version comments, inputs, and runner requirements |
| Local | Application builds/tests work in that local environment |
| GitHub execution | Updated Actions execute for target SHA/event/runner with expected warnings, outputs, artifacts, and similar results |

For approved changes select representative and affected paths, recording run URLs, SHAs, and conclusions. Check artifacts/signatures for consumer-required content beyond generation success. For changed defaults such as fork rejection, check affected paths too. Local success alone does not validate Action execution; state inaccessible/unexecuted results and remaining checking methods. Apply the source's small upgrades/behavior preservation through these distinctions.

[^github-metadata]: Metadata syntax. Authoritative Action internal `runs.using`.
[^copilot-runtime]: Summarized Runtime Upgrade Conventions source investigation, compatible upgrades, and behavior preservation. Do not adopt old SHA/version examples or equate local checks with real execution.
[^actions-checkout]: Check authentication, forks, and runner requirements in target checkout releases/metadata/README.
[^actions-setup-node]: Check cache/input changes in target setup-node releases/metadata/README.
