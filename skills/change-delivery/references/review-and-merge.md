---
type: Instruction
title: Review and merge
description: Define PR creation, review responses, CI checks, rebasing, squash merge, and workspace cleanup.
---

## Review and merge

### PRs and review

- With no explicit stop condition, approved change execution, and pushed diffs, PR creation is the immediate default stage, not optional extra work. Create a draft without asking again whether PR creation is permitted.
- Continue after PR creation through CI/conflicts, review, fixes, revalidation, merge, and post-integration checks. CI/review waits are not completion; check through available waiting/retrieval means.
- Create draft PRs after pushing, linked to target Issues/Sub-issues.
- Assign PRs to the requester confirmed in the Issue. Ask if unidentified; do not unconditionally equate authenticated users with requesters.
- At creation, check label names/descriptions and apply appropriate labels.
- Follow [Writing Issues and PRs](../../issue-management/references/github-writing.md) for titles/bodies and [Change records](../../../.apm/instructions/change-records.instructions.md) for reporting versus execution. Use the [reusable template](../assets/pull_request_template.md) if no target template exists; encourage equivalent fields in downstream repositories, preserving existing headings and conventions. Do not bulk-copy templates or migrate policies merely because the package is installed. Keep this repository's `.github/pull_request_template.md` and reusable asset identical when changing either.
- At creation and every update, remove all HTML comments and retain substantive actual validation status. `Not run` is valid without required reasons or a post-merge plan; incomplete execution alone is not a merge blocker. Preserve independently required CI and acceptance conditions.
- Posting, updates, and review replies follow `issue-management` “Markdown quality for GitHub”: format/check complete bodies and verify saved agreement/display.
- If review changes purpose, outcomes, acceptance conditions, or external impact, including reductions, save/present concrete proposals and confirm through `issue-management` “Planning and execution scope.” Record and continue adjustments meeting the same success conditions.
- Within approval, update PR bodies alongside review responses changing content, reasons, results, or important constraints.
- Reassess labels if content changes.
- On drafts prioritize Copilot Code Review through [Quick reviewer candidate assessment](#quick-reviewer-candidate-assessment). For Codex follow “Alternative review.” Only read-only candidate checks may precede CI completion; formal review-request APIs used as assessment/request below wait for stable-HEAD checks.
- Before ordinary review requests, confirm successful required CI on current HEAD and no conflicts with current base. Also check repository-required pre-review automation, without uniformly adding nonrequired CodeQL or similar checks.
- If required CI fails or conflicts exist, fix, validate, commit, and push before review requests. Repeat checks on new HEAD until successful/resolved.
- With no configured CI, apply the existing merge exception under [When CI is unconfigured](#when-ci-is-unconfigured), distinguishing it from execution success.
- Record current HEAD with successful required CI/no conflicts as the review target and request ordinary review for it. For Copilot use “Requesting Copilot Code Review” below.
- Prioritize target repository review Instructions, guides, Skills, and templates for external reviewers. Do not give locally APM-installed `daiksud/agents` `code-review` as additional instructions to other repositories' Copilot/Codex reviewers. Point to originals only when reviewer material exists in the target repository. For `daiksud/agents` itself, `skills/code-review/SKILL.md` is its own policy and may be referenced.
- After initial/re-review requests, self-review until external review completes.
- If self-review, findings, base updates, or conflict resolution change reviewed HEAD, fix, validate, commit, and push, then verify new required CI/no conflicts before re-review. Old-HEAD reviews do not complete new HEAD.
- Assess findings from current requirement/contract discrepancies, evidence, triggering conditions, and impact, classifying formal fixes, optional suggestions, investigation, or no action. Severity, urgency, likelihood, and cost guide priority/fixes; reviewer classification/approval alone does not decide adoption.
- Many prerequisites, low frequency, or difficult reproduction alone do not justify no action. Evidence-based contract discrepancies with concrete impact remain formal findings even under limited conditions. Investigate inadequate conditions/evidence without speculative fixes.
- Evaluate “Suppressed comments” by the same criteria, without deciding solely from suppression labels or Copilot Approve. For missing Approve follow “Suppressed findings and missing Approve.”
- Follow “Reply placement and publication procedure” below, separating individual responses from overall explanations.
- Fix, validate, commit, and push actionable findings, then confirm new required CI/no conflicts before re-review.
- Changes to reviewed commits through self-review, CI fixes, rebase, or base updates require the same stable-HEAD checks before latest-commit review requests.
- Repeat review/fixes until zero actionable findings.
- With Copilot, completion requires Approve on the latest commit. With Codex selected through quick assessment, apply Codex completion conditions. Candidate assessment does not replace completed review.

### Retrying reviews without results

Apply this policy to the selected review service, regardless of product.

1. Record the PR, complete target HEAD, review service, request evidence, and request time. Before every retry, retrieve the latest review results, findings, and request history, and confirm the target HEAD and current required CI/conflict checks.
2. If at least 10 minutes have passed since the most recent request and no review result has returned for that request and target HEAD, request review again on the same PR through the selected service's supported request method. Running status alone does not prevent retry. Wait at least 10 minutes from each immediately preceding request before the next retry, including requests made by other sessions.
3. If a result has returned for the latest request, assess it under the ordinary completion/finding rules instead of retrying for elapsed time. Changed HEAD requires the ordinary stable-HEAD checks and latest-HEAD review; do not reuse an old result as completion. A retry does not establish service failure, completion, approval, or permission to switch reviewers.
4. Before resending after a request timeout, check whether it was saved and use its recorded time. If the latest results/request history cannot be retrieved, or the most recent request time cannot be established, hold retries and report the uncertainty and resumption condition. Preserve explicit quota/disabled-service restrictions and human-review requirements. Check results through available tools; do not ask the user to inspect a review product's screen.

### Quick reviewer candidate assessment

This selects a candidate, not a guarantee of quota, execution success, or completed review. Codex installation alone also does not complete review; verify execution after requesting.

Assessments potentially starting ordinary review occur after current-HEAD required CI/no conflicts. Read-only Copilot `suggestedReviewerActors` or Codex Connector installation checks may precede CI completion, but fallback formal-request APIs in environments without candidate queries wait for stable-HEAD checks.

| State | Meaning |
| --- | --- |
| `available` | Copilot candidate/request acceptance, or Codex Connector installation confirmed for the target repo (including the requester-confirmed `daiksud/*` exception). May select as reviewer |
| `unavailable` | No Copilot candidate, absent/out-of-scope Connector, or explicit service-specific unavailability is confirmed. Exclude for this selection |
| `unknown` | Permissions, retrieval failures, incomplete lists, or unsupported checking prevent judgment. Do not assert absence/unavailability |

Perform the checks below at most once per service. Check Copilot first; if selectable, do not investigate Codex. Retain judgment, repo, authentication conditions, evidence, and checking time within the task; do not search settings, subscriptions, quotas, or other APIs again under unchanged conditions. New PRs update Copilot's PR-specific assessment; repo/authentication/installation changes update relevant assessments. HEAD changes alone do not repeat Connector checks. Do not add persistent caches or dedicated settings.

Keep explicit quota-limit errors separate from candidate assessment, retaining evidence, time, affected user/billing entity, and confirmed scope in task context. Treat as `unavailable` while applicability to the same entity/quota is confirmed; HEAD/PR changes or `available` candidates alone do not discard evidence or justify requests again. Reassess with reliable evidence of quota renewal/recovery or user/billing-entity changes. Do not generalize PR-specific errors, generic 403/422, network failures, or permission gaps to account-wide quota limits; unclear scope remains unknown. Follow [Retrying reviews without results](#retrying-reviews-without-results) for running requests; preserve the restrictions on switching services and on requests whose latest state cannot be retrieved.

For existing requests on the same HEAD, first check history, Bot state, and completed reviews. For Copilot follow [Checking execution after Copilot requests](#checking-execution-after-copilot-requests). Apply [Retrying reviews without results](#retrying-reviews-without-results), including when execution is running. Candidate-search limits do not apply to ordinary progress checking of accepted reviews/CI.

- If unrequested and Copilot is `available`, request Copilot.
- If Copilot is `unavailable` or `unknown` and Codex `available`, choose Codex. Distinguish “no candidate/unavailable” from “candidate unverifiable”; do not require extra proof of permanent unavailability or reapproval for switching. Do not switch services to bypass running requests or requests whose latest state cannot be retrieved; apply [Retrying reviews without results](#retrying-reviews-without-results).
- If neither is `available`, stop searching. Self-review and CI checks may continue, but do not claim completed external review or mergeability. Report installation/permission/checking blockers without relaxing protections.

#### Retrieve Copilot candidates once

Query target PR `suggestedReviewerActors`, a reviewer-candidate API; do not substitute Issue-assignee `suggestedActors`.

Replace `OWNER`, `REPO`, and `PR_NUMBER` with targets. The following reads only and does not request review.

```bash
OWNER=daiksud
REPO=agents
PR_NUMBER=123

gh api graphql \
  -f owner="$OWNER" -f name="$REPO" -F number="$PR_NUMBER" \
  -f query='
    query($owner: String!, $name: String!, $number: Int!) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          suggestedReviewerActors(first: 100, query: "copilot") {
            nodes {
              reviewer {
                __typename
                ... on Bot { login }
              }
            }
            pageInfo { hasNextPage }
          }
        }
      }
    }
  ' \
  --jq '
    if ((.errors // []) | length) > 0
       or .data.repository.pullRequest == null then "unknown"
    else
      .data.repository.pullRequest.suggestedReviewerActors
      | if (.nodes | type) != "array" then "unknown"
        elif any(.nodes[]?.reviewer;
          .__typename == "Bot"
          and .login == "copilot-pull-request-reviewer") then "available"
        elif .pageInfo.hasNextPage == false then "unavailable"
        else "unknown"
        end
    end
  '
```

Command/GraphQL failures are `unknown`. No candidates excludes Copilot for this selection without proving subscription-wide unavailability. Missing candidates with remaining pages are also `unknown`; do not fetch more pages for exploration.

Where candidate queries are unavailable, after confirming no existing request, the formal API in “Requesting Copilot Code Review” may be used once as assessment/request. Record successful acceptance; do not resend merely to confirm acceptance. For subsequent waits apply [Retrying reviews without results](#retrying-reviews-without-results). Only explicit quota-limit/disabled-service errors establish `unavailable`; generic 403/422/network failures alone do not establish service unavailability. Do not search other candidate APIs after failure.

#### Check Codex Connector installation for the target repo

For repositories owned by `daiksud`, the requester confirms that Codex is installed. Treat Codex as `available` without checking GitHub App installations. When Codex is selected, directly request `@codex review` after the required current-HEAD CI/conflict and existing-request checks and the Ready-state check in [Alternative review](#alternative-review). Still verify actual review execution, completion, findings, and required approvals; posting a request is not evidence of a completed review.

For other repository owners, check whether `ChatGPT Codex Connector` (slug `chatgpt-codex-connector`) is installed for the target repo. First reuse already verified installation or same-task successful events below. Otherwise use one available authenticated GitHub Apps settings view or existing tool returning target-repo installation. Without supported checking, use `unknown` instead of trial-and-error calls.

Existing tools include reading GitHub-returned data/known events from successful existing operations on the target repo under the same task/authentication. If `performed_via_github_app.slug` is `chatgpt-codex-connector` and repo, time, and current successful operation are matched, reuse as `available` evidence. This is an operating assessment based on access limited to both App/user permissions, separate from direct installation-list retrieval or guaranteed review success. Self-claims in comment bodies or past-task records do not substitute; do not change labels/post comments merely to check.

Confirmed installation means `available`; confirmed absence/out-of-scope in complete target lists means `unavailable`. For account-level information, require matching owner and All repositories or target inclusion in Selected repositories; otherwise `unknown`. Explicit suspension/disablement means `unavailable`. Public App pages, past Bot comments, and local `codex login status` are not current target-repo installation evidence.

Do not use `GET /repos/{owner}/{repo}/installation` with ordinary `gh` user tokens as a general App list; it requires the target App's own JWT. `GET /user/installations` also covers the authenticated App's installations, not unrelated Apps. Without these authentication conditions, do not continue searching tokens/APIs/browser-internal APIs.

### Alternative review

This procedure owns requests/completion decisions. Read `code-review` only when reviewing diffs, without starting requests/fixes/merge from that skill.

The user-selected operating policy for this workflow requires Codex review requests, including retries, to use a PR that is Ready for review (`isDraft == false`). After current-HEAD required CI succeeds and conflicts are resolved, mark a draft Ready if needed, then retrieve its state before posting `@codex review`. Hold the request while it remains a draft or its state cannot be verified. Ready does not establish review completion, approval, or permission to merge.

1. Record reasons for Codex selection, Copilot/Codex judgments, evidence URLs/results, and time in the PR. Preserve explicit unavailability discovered after Copilot requests and follow the same selection. Distinguish unavailability from unverified candidates without reapproval for each switch.
2. Disagreement with findings, missing Approve, elapsed waiting, or temporary retrieval failure alone do not justify switching. For same-service retries follow [Retrying reviews without results](#retrying-reviews-without-results); waiting alone does not authorize switching services.
3. Request `@codex review` in a PR comment. Add original paths/application instructions only when target-repository reviewer Instructions/guides/Skills exist and are externally readable. Do not add locally APM-installed common `code-review` or material merely because originals exist in another repository. Without target-specific reviewer material, defer to Codex's ordinary review. Check request comments before/after sending, investigating possible saved requests after timeouts before resending. Request again for confirmed nonsending, changed HEAD, reruns after resolved failures, or under [Retrying reviews without results](#retrying-reviews-without-results).

### Codex completion assessment

Review remains incomplete until all conditions below pass. Re-review after fixes/rebases change HEAD.

| Target | Required evidence |
| --- | --- |
| Author/execution result | Compare actual Codex Bot summaries, review bodies, findings, and sessions linked to request comments, explicitly confirming normal completion. Exclude failures, interruptions, and running work |
| Target commit | Reviewed SHA matches current complete HEAD. Resolve shortened SHAs uniquely through repository commits; do not infer from request-time HEAD alone |
| Remaining findings | Check past ordinary/body findings as well as current ones. Track actionable findings inherited from Copilot through fixes, published replies, and Resolve |
| Merge conditions | Check CI, conflicts, published replies, thread resolution, and required repository approvals. Switching to Codex does not relax protections |

👀, 👍, comment counts, or third-party “completed” claims alone do not establish normal completion, target SHA, or resolved findings. Unknown SHAs or failed retrieval remain incomplete; record uncertainties/resumption conditions.

Codex's “no major issues” is a scoped review result; officially described P0/P1-focused review does not guarantee all quality. Do not describe Copilot Approve and Codex normal completion as identical approval events.

### When Copilot requests human review

If Copilot summaries, review bodies, or findings explicitly escalate to human checking/judgment, such as “human review required,” distinguish this from ordinary absence of Approve or Copilot unavailability.

- Do not treat human-review requests as `unavailable`, or substitute Codex Review or another Bot.
- Do not add arbitrary users, teams, or third parties as reviewers. Normally use the requester confirmed in the Issue/PR; request only that person if identifiable and requestable on GitHub. Do not unconditionally equate authenticated users or repository owners with requesters.
- If the requester is unidentified/unrequestable, or another human decision is needed, return needed judgments/reasons to the requester/user without guessing replacements.
- Do not merge while required human review remains unresolved. If requester review fixes change HEAD, return to ordinary latest-HEAD review procedures.

### Required Approve and CODEOWNERS assessment

Check Ruleset `required_approving_review_count` and `require_code_owner_review` separately. The former is overall required approvals; the latter concerns Code Owners for changed paths. With multiple Code Owners, one owner's Approve meets that condition. Do not infer blocking from settings alone; compare PR author, applicable CODEOWNERS, latest review state, and GitHub mergeability.

If the sole applicable Code Owner is the PR author, do not wait for self-approval or nonexistent other owners. GitHub's effective assessment permits valid non-owner approval to meet the required count in this case; check another valid Approve and GitHub mergeability, then proceed. If Copilot Approvals is enabled and its latest-HEAD review is `APPROVED` and counted toward required approval, it suffices. Default comment-only Copilot reviews are not Approve.

This exception does not bypass explicit Copilot human-review requests, unresolved Request changes, requirements for another actor to approve the latest push, or other unmet GitHub protections. If protections remain unmet, identify actual conditions without weakening CODEOWNERS or requesting arbitrary humans.

### Suppressed findings and missing Approve

Judge “Suppressed comments” by the same criteria as ordinary findings regardless of Approve. This section defines only merge handling when latest-commit Copilot review completes without Approve. Preserve mandatory Copilot Approve; obtaining it does not prove finding validity.

1. Check reviewed commit, completion, and Approve, confirming no unresolved formal findings including past ordinary/suppressed findings. “Zero new comments” alone is insufficient. Incomplete reviews or failed retrieval are neither approval nor no findings.
2. Evaluate suppressed findings against current requirements/contracts, evidence, triggering conditions, and impact. Return formal findings to ordinary handling; investigate insufficient evidence. If necessary evidence is unobtainable, show gaps/unverified scope and return to user judgment without re-review merely for Approve. Do not promote optional/no-action findings that meet contracts to mandatory fixes solely for approval.
3. Fix, validate, commit, and push formal findings within approval without additional confirmation. For changed purpose, outcomes, acceptance conditions, external impact, or permissions, confirm under `issue-management` “Planning and execution scope.”
4. If no unresolved formal findings or investigations remain but Approve is absent, record fixes/validation or reasons for optional/no-action judgments in an overall review comment linked to the target review. Verify publication under “Reply placement and publication procedure” below, then request re-review once. Do not request before confirmed publication; on resumption inspect published comments/request history to avoid duplicates.
5. If that re-review still withholds Approve for the same optional/no-action findings, do not repeat approval-only fixes or automatic requests. Retain finding judgments and present evidence, completed responses, and options for user judgment. Evaluate new findings by the same criteria without resetting repetition limits on the same issue.

### Reply placement and publication procedure

Separate replies so reviewers can check individual responses and overall explanations in appropriate places.

| Target | Placement and content |
| --- | --- |
| Individual thread findings | In that thread, record response, change commit, and validation, or reasons for no action |
| Findings only in review bodies, such as `Suppressed comments` | In an overall review comment, link the review and record fixes/commits/validation for formal findings, or reasons for optional/no-action judgments. Do not change necessity based on Approve or substitute a reply thread |
| Overall review explanation | In an overall review comment, link the target review and give the explanation; do not mix into individual threads |

1. Check findings and respond under existing fix criteria. Report actual validation for fixes, complete commits and push, and gather reply evidence. Independently required checks remain required.
2. Group individual replies in a pending review and prepare necessary overall comments. Do not force unnecessary overall comments; if no individual replies exist, prepare only overall comments.
3. Submit the replies, including necessary overall comments; otherwise submit only individual replies. Submit overall-only comments as reviews too.
4. Retrieve published individual/overall replies after submission and verify targets/content. Pending replies or successful submit requests do not substitute for publication verification.
5. Resolve only threads with confirmed published actions or no-action reasons. Do not Resolve failed/unverified posts. On resumption check published replies without duplicate successful posting.

If APIs/UI cannot group individual replies in pending reviews and submit them, report the restriction. Post individual replies to target threads and separately record overall explanations as overall review comments linked to target reviews. Do not substitute individual threads for overall explanations; preserve publication-before-Resolve order. If overall comments also cannot be posted, report incomplete work, posted scope, and means needed to resume.

### Rebase and merge

- Rebase target-branch updates into working branches, keeping Git history linear.
- After rebasing, select relevant validation and report what actually ran; rerun independently required checks and push remotely.
- For rebased published history use `git push --force-with-lease`; check unknown remote updates without overwriting.
- Immediately before merge, confirm latest-commit review completed, zero findings requiring action, passing CI, and zero conflicts. Apply “Required Approve and CODEOWNERS assessment”; sole-owner authorship alone does not justify waiting for self-approval.
- Immediately before merge, recheck latest main SHA and required checks/distribution validation triggered by its push. Initial checks do not substitute; wait for running/unverified results and prioritize recovery on failures without merging ordinary PRs. Approved recovery PRs resolving that failure are exempt from this main-success condition, while meeting their own reviews/checks/approvals. Use existing unconfigured-CI exceptions only if CI is absent.
- Once all conditions pass, confirm the PR is Ready for review (mark it Ready if still a draft), then squash-merge.
- Verify the final description matches the reviewed change, retains relevant decisions and actual validation status, and contains no HTML comments. Update it before merge if needed. If an applicable Engineering Policy changed, verify the topical document ends with this real PR link.
- Preserve the final title and body as squash subject and body using `PR_TITLE` / `PR_BODY`; follow [Commit-message instructions](conventional-commits.md). Retrieve both immediately before merging and pass their contents without template comments or a replacement summary:

  ```bash
  PR_TITLE="$(gh pr view "$PR_NUMBER" --repo "$OWNER/$REPO" --json title --jq .title)"
  PR_BODY="$(gh pr view "$PR_NUMBER" --repo "$OWNER/$REPO" --json body --jq .body)"
  gh pr merge "$PR_NUMBER" --repo "$OWNER/$REPO" --squash \
    --match-head-commit "$REVIEWED_HEAD" --subject "$PR_TITLE" --body "$PR_BODY"
  ```

  Check successful retrieval and description content before running merge; these variables are text, never shell code. Required approvals/checks still apply.
- Confirm the PR merged and target history is linear.

### Post-integration main verification and recovery

Change owners also own post-merge verification. PR integration-candidate and merged-main SHAs differ; PR CI alone does not verify main.

1. Compare squash-merge SHA with required checks triggered by that main push. For projects with distribution validation, also check installation paths for the same published SHA.
2. Wait for running checks. Failed, canceled, unexecuted, or unobtainable results are not success; record reasons/unverified scope. Required CI not starting is not an “unconfigured CI” exception.
3. On failure, stop ordinary work and record impact, detection time, last healthy SHA, failed checks/logs. If a causative change exists, make a revert/minimal fix a separate recovery PR. If evidence confirms temporary external-service/runner failure requiring no repository changes, record evidence/retry reasons and revalidate required checks/distribution paths on the same main SHA after recovery. Do not create empty recovery PRs; stop subsequent work until success is confirmed. Continue investigation when causes are unknown without assuming external failures. Without changes, skip steps 4–6 and proceed to step 7 after revalidation.
4. Save/retrieve/present recovery plans requiring repository changes in Issues, judging execution scope through `issue-management` “Planning and execution scope.” Do not reapprove regression fixes within the original request or clear recovery requests. Confirm recovery changing purposes, acceptance conditions, external impact, or authority; do not extend approval to unrelated incidents. After confirming scope, protect diffs/worktree usage, `git switch main`, `git pull --ff-only`, and create a dedicated recovery branch from that main. If another worktree uses main, leave it unchanged, compare `origin/main` SHA fetched through `git fetch origin` with the failed target, and create a dedicated recovery branch from that SHA at the current location. Check unknown main updates first; do not bypass checkout protection or add recovery changes to merged former working branches.
5. For defects, add the smallest reproducible validation and confirm failure before fixes and success afterward. Use `software-development` for code and selected or independently required evaluations for skill judgments, honoring repository-specific exclusions. For unreproducible external failures or similar cases, record evidence/unverified scope without claiming failed tests were created.
6. Merge recovery PRs through ordinary latest-HEAD review, published replies, Resolve, required approvals, and checks. Do not weaken protection/checks to appear healthy.
7. Record the time all required checks/distribution paths pass for the recovery commit (or the same revalidated main SHA without changes), and confirm health before resuming. Do not claim recovery/overall completion while unverifiable.

Measure main recovery time from failure detection until all recovery-commit required checks (including required distribution validation) pass, separate from time restoring installed environments such as APM to healthy SHAs. For external failures without changes, explicitly define the endpoint as all same required checks passing on the same main SHA. Do not add common pass/fail thresholds; record project goals/measurements.

Briefly record incident impact, occurrence/detection/recovery times, confirmed causes, missed-detection reasons, added validation, and remaining improvements. Do not infer unknown causes/times or blame people.

### When CI is unconfigured

- Preserve existing merge exceptions in projects without CI. Record actual validation status (including `Not run`), absent CI, treatment as an exception, and strong recommendation to configure CI in the PR. Do not turn the exception into a universal local-execution requirement.
- This does not mean CI executed successfully or CD was achieved. After merge, show confirmed scope/limits such as local checks.
- Do not apply to existing required CI, failed/canceled/unexecuted jobs, or inaccessible results. Do not relax protection rules; check approval scope if settings must change.

### Post-merge workspace cleanup

- After confirmed merge, check for no uncommitted changes, then `git switch main`.
- Run `git pull --ff-only` on main; on failure investigate without forcibly overwriting local changes/history.
- If another worktree uses main, instead run `git fetch origin` and compare `origin/main`, merge SHA, and main validation, then `git switch --detach origin/main` at the current location and proceed to deletion below. Do not alter other worktrees/their main or bypass checkout protection. In this case verify remote-main/current-location synchronization for completed cleanup, separately reporting other worktree local main unupdated.
- Check and delete merged remote/local branches. Before deletion check corresponding PR merge state, branch-tip/final-PR-commit agreement, and usage through `git worktree list`.
- Do not delete branches with post-merge commits or used by other worktrees; report why retained. Exclude main and merge-target branches.
- Delete remote branches with `git push origin --delete <branch>` and local ones with `git branch -d <branch>`; do not repeat already-completed deletion.
- If squash merge causes `git branch -d` rejection, recheck PR merge and tip agreement before `git branch -D <branch>`.
- After `git fetch --prune origin`, use `git status --short --branch`, `git branch -vv`, and `git ls-remote --heads origin` to verify main synchronization, working tree, and absence of deletion targets.
- Report incomplete main updates/deletion and reasons separately from merged status.

### Checking execution after Copilot requests

After requesting Copilot review, do not judge execution only from `requested_reviewers` and completed reviews. Copilot may be running after acceptance even with empty `requested_reviewers` and no review submission yet. Empty arrays do not establish “unrequested,” “stopped,” or “unavailable.”

Check state in this order.

1. Record current complete HEAD first. Also retain target HEAD when requesting, and compare later to confirm no changes.
2. Check Copilot submissions through `GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews`. Matching `commit_id` establishes results for current HEAD. Explicit quota-limit bodies are not normal completion; retain evidence/scope under “Quick reviewer candidate assessment.” Preserve actual states such as `APPROVED`/`COMMENTED`; “Approval recommended” in prose is not `APPROVED`.
3. Without completed latest-HEAD review, check PR Issue events/timeline. Copilot `review_requested` with its `requested_reviewer.login` signals requested; `copilot_work_started` with `performed_via_github_app.slug == "copilot-pull-request-reviewer"` is a candidate execution-start signal.
4. Use `copilot_work_started` as running evidence only when after Copilot `review_requested` for current HEAD and HEAD has not changed since. Use retained request SHA/time if available; on resumption without them, check timeline order of latest-HEAD updates, subsequent `review_requested`, and `copilot_work_started`. If correspondence cannot be established, use `unknown`, not asserted running.
5. With matching current-HEAD `copilot_work_started`, treat execution as running and apply [Retrying reviews without results](#retrying-reviews-without-results). Running status does not prevent the 10-minute retry; do not switch to another service merely because of elapsed waiting.
6. Missing `copilot_work_started` alone does not prove unexecuted; permissions, paging, or propagation delays may obscure it. Combine available request API success, current-HEAD `review_requested`, existing progress displays, and other evidence to assess accepted/unknown.
7. After HEAD changes, old-HEAD events/submissions do not establish latest-HEAD running/completion. Recheck latest request history and `commit_id`.

For example, the following can check current execution state.

```bash
gh api "repos/$OWNER/$REPO/issues/$PR_NUMBER/events?per_page=100" --paginate \
  --jq '.[] |
    select(
      .event == "review_requested"
      or .event == "copilot_work_started"
    ) |
    {
      event,
      created_at,
      requested_reviewer: .requested_reviewer.login,
      app: .performed_via_github_app.slug
    }'

gh api "repos/$OWNER/$REPO/pulls/$PR_NUMBER/reviews" \
  --jq '.[] |
    select(.user.login == "copilot-pull-request-reviewer[bot]") |
    {state, submitted_at, commit_id, body, html_url}'
```

Treat Issue-event `copilot_work_started` as an operational progress signal, not a permanent public API contract. Where inaccessible, judge through other evidence without asserting unexecuted. Because this event lacks HEAD, always combine with occurrence after current-HEAD `review_requested` and unchanged HEAD.

### Requesting Copilot Code Review

Set the same `OWNER`, `REPO`, and `PR_NUMBER` as quick assessment, normally requesting once through the official CLI. Do not remove other existing reviewers.

```bash
gh pr edit "$PR_NUMBER" --repo "$OWNER/$REPO" --add-reviewer "@copilot"
```

Use the formal REST path below only when needed, such as environments lacking the dedicated CLI. Fixed Bot IDs or PR Node IDs are unnecessary.

```bash
gh api --method POST \
  "repos/$OWNER/$REPO/pulls/$PR_NUMBER/requested_reviewers" \
  -f 'reviewers[]=copilot-pull-request-reviewer[bot]'
```

CLI/API success means acceptance, separate from execution start/normal completion. Follow “Checking execution after Copilot requests.” Do not automatically resend via API after CLI failures/timeouts; first check existing requests/execution. Empty reviewer/review arrays alone do not establish failure. Retrieve state if acceptance is unclear, then apply [Retrying reviews without results](#retrying-reviews-without-results), retaining any saved request time. Hold retries if latest results/request history remain inaccessible; do not switch request paths merely to bypass uncertainty.
