---
type: Instruction
title: Purpose, goals, means, and standards
description: Decide from actors' purposes and observable goals, and handle common standard candidates.
sources:
  - id: kent-beck-toil-struggle
    resource: https://newsletter.kentbeck.com/p/take-my-toil-leave-me-my-struggle
---

## Purpose, goals, means, and standards

Build systems and features story-first, beginning by describing who can do what, in which situation, after completion. Before design decisions, clarify the actors and the distinctions below, and show which goals and standards in that story guide the choice of means.

| Category | Meaning |
| --- | --- |
| Purpose | The state or value an actor wants to achieve, or the problem they want to resolve |
| Goal | Observable specifications, constraints, and success conditions by which achievement can be judged |
| Means | Systems, features, models, code, and technologies that meet the goals |
| Standard | Decision criteria and priorities used repeatedly to choose means that meet goals across multiple projects |

Ask the user about business uncertainties that affect the outcome, and investigate technical uncertainties from evidence. Do not turn assumptions into agreed purposes or goals.

When the user chooses an implementation policy involving tradeoffs, ask them why if the reason is unclear, and check whether it is a criterion applicable across projects. Follow `issue-management` procedures for recording common standard candidates for the conditions for candidate Issues and handling unresolved questions.

### Preserve productive struggle

Completing a deliverable is not the only possible value of work. Kent Beck distinguishes *toil* that consumes time without meaningful learning from *struggle* that develops understanding, confidence, and capability.[^kent-beck-toil-struggle]

- Use the user's expressed purpose and context to distinguish a completed outcome from a purpose of learning or practice, or both. For learning, make success observable through relevant practice or demonstrated understanding instead of treating the aspiration itself as a goal. Do not classify all difficult tasks as human-owned or ask for a preference before every action.
- For outcome-oriented or expressly autonomous requests, do the authorized work, including difficult reasoning. Automate repetitive or mechanical toil where useful, while making important decisions, tradeoffs, and validation evidence understandable. Do not withhold solutions, manufacture friction, or return tedious work to the user for presumed educational benefit.
- When the user's purpose is learning through exploration, preserve room for their reasoning: frame the problem, offer focused questions, incremental hints, examples, and small experiments, and give feedback on their proposals. Exploration to investigate options or recommend a solution remains outcome-oriented work. Supply the answer or take over when requested, rather than enforcing a lesson.
- Keep the existing boundaries for business decisions, user approvals, code review, tests, CI, integration, and publication. Learning goals neither transfer decision authority to agents nor waive delivery obligations.

[^kent-beck-toil-struggle]: [Kent Beck: Take My Toil, Leave Me My Struggle](https://newsletter.kentbeck.com/p/take-my-toil-leave-me-my-struggle). Apply the distinction to the user's goal instead of treating every challenge as a mandatory learning exercise.
