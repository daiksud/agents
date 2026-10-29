# Local change-record instructions example

Adapt this fragment to the target repository's existing instructions. Replace the example local paths with actual targets and remove this note before adoption. The English PR-body rule below is an explicit adoption choice; resolve conflicting local language instructions before applying it.

```markdown
## Change records

Use the repository's [PR template](.github/pull_request_template.md) and [Engineering Policies](docs/engineering-policies/). Keep descriptions proportional and self-contained: record the problem, actual change and resulting behavior, relevant decisions, and actual validation status. Equivalent headings are welcome; omit unnecessary decision sections.

Every PR reports actual validation status. Execution, method, scope, rigor, and timing are discretionary unless independently required. `Not run` is valid without a required reason or post-merge plan. Distinguish completed, partial, failed, planned, and unperformed checks; preserve required CI and agreed acceptance conditions. Unperformed discretionary checks alone do not block merge.

Templates may contain HTML authoring comments. Remove all HTML comments from actual PR descriptions at creation/update and check again during review and before merge, retaining substantive decisions and validation status.

Keep current cross-cutting or future-guiding policy in revisable topical Engineering Policies with applicability, rationale, relevant alternatives, trade-offs, and the introducing/revising PR link. Historical judgments remain self-contained in PR descriptions and commits even after policies change. Ordinary local changes need no policy document.

Use English Conventional Commit titles and English PR bodies so the final PR title/description can be retained verbatim as the squash subject/body. Keep ordinary commits English, preserve other artifact-language conventions, and do not translate or discard rationale only at merge time. Before merging, confirm the title/body reflect the final reviewed change and contain no HTML comments; retrieve and preserve them when supplying explicit squash messages. Settings adoption is separately authorized: the corresponding defaults are `squash_merge_commit_title = PR_TITLE` and `squash_merge_commit_message = PR_BODY`; this instruction does not authorize changing them or bypassing approvals, CI, or protections.
```
