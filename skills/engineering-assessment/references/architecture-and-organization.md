---
type: Reference
title: Assess Architecture and Organization boundaries
description: Assess meaning, change, runtime, deployment, and ownership boundaries and choices such as Microservices from DDD, Team Topologies, Conway, and Continuous Delivery evidence.
sources:
  - id: ddd-reference
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
  - id: team-topologies-key-concepts
    resource: https://teamtopologies.com/key-concepts
  - id: continuous-delivery-architecture
    resource: https://continuousdelivery.com/implementing/architecture/
  - id: dora-loosely-coupled-teams
    resource: https://dora.dev/capabilities/loosely-coupled-teams/
---

## Assess Architecture and Organization boundaries

Read for assessments involving semantic and delivery boundaries, such as domain models, service decomposition, Microservices, team ownership, or cross-team dependencies. Do not apply to every assessment; use only when the problem concerns boundaries, coupling, or team interaction.

The purpose is not to introduce a particular architecture style or organization chart. Separate dependencies affecting user outcomes into different boundary types and select the smallest improvement currently needed.

### Separate boundary types first

Even when boundaries look like the same line, they answer different questions.

| Boundary | Assessment question | Main evidence |
| --- | --- | --- |
| Domain boundary | Which business problems and knowledge are addressed? | User purposes, business capabilities, terminology, business decisions |
| Bounded Context / semantic boundary | How far does the same model and word meaning apply? | Ubiquitous Language, models, Context Maps, translation/contracts |
| Change boundary | What can be understood, changed, and verified independently? | Actual diffs, test dependencies, co-changes, review waiting |
| Runtime boundary | What executes as separate processes/components? | Runtime topology, inter-process communication, failure propagation |
| Deployment boundary | What can be deployed, released, and rolled back independently? | Pipelines, artifacts, build dependencies, release history, simultaneous deployment needs |
| Repository boundary | In which units are source, history, and automation managed? | Repositories, builds, ownership settings, tooling |
| Team ownership boundary | Who has continuing decision, operations, and improvement responsibility? | Actual responsibility, on-call, change approvals, inquiries, team experience |

One Bounded Context may become one service, repository, or team, but do not make this a design rule. In Eric Evans' DDD, Bounded Context makes model scope explicit; Context Maps handle contact points, translation, and influence between models.[^ddd-reference]

Correspondence such as the following can be tested as a hypothesis, but exact alignment is not a success condition.

```text
semantic boundary
≈ change boundary
≈ deployment boundary
≈ team ownership boundary
```

Domain boundaries concern business problems and knowledge, not this alignment chain itself. Repository and Runtime boundaries may also take different shapes because of current tooling and operational constraints.

### Assess Architecture through independence outcomes

Check actual change, test, and deployment independence rather than architecture styles or service counts.

Continuous Delivery architecture guidance treats testability and deployability as important attributes. It describes loosely coupled, well-encapsulated components that can be verified and delivered without excessive reliance on integration environments or large-scale orchestration. Improve existing systems evolutionarily as needed rather than rebuilding all at once.[^continuous-delivery-architecture]

DORA's Loosely Coupled Teams likewise emphasizes observable results rather than technologies.[^dora-loosely-coupled-teams]

- Major design changes can proceed without requiring changes from other teams.
- Daily work does not depend on fine-grained cross-team coordination.
- Deployments and releases are independent of dependency services.
- Most validation does not require shared integrated test environments.

Mainframes can achieve these outcomes, and Microservices can fail to achieve them. Therefore, many services or separate repositories alone are not evidence of loose coupling.

### DDD does not convert semantic boundaries into architecture counts

Treat DDD Subdomains as problem space and Bounded Contexts as the scope of one model and language.[^ddd-reference]

At minimum, check:

- Whether the same terms mean different things across boundaries.
- Whether models must change together because of domain invariants or technical coupling.
- What to share, translate, or isolate across boundaries.
- Whether decisions or release cadence on one side unnecessarily affect the other.

Do not invent new Subdomains or Bounded Contexts solely to resolve technical coupling. Conversely, independent meaning alone does not require separate runtimes, deployments, or repositories.

### Use Team Topologies from fast flow and cognitive load

Team Topologies is a team-of-teams design approach for fast flow of value, using four team types and three interaction modes as a pattern language.[^team-topologies-key-concepts]

Do not introduce the four types as an organization chart requiring four teams. Investigate current responsibilities and cognitive load, and size necessary roles proportionately.

| Team type | Main role in assessment |
| --- | --- |
| Stream-aligned | Deliver outcomes end to end along one value stream |
| Enabling | Temporarily help other teams gain capabilities and independence |
| Complicated Subsystem | Take on cognitive load of subsystems requiring advanced expertise |
| Platform | Provide internal products/services stream-aligned teams can use with low cognitive load |

Choose interactions by purpose.

| Interaction | Situation |
| --- | --- |
| Collaboration | Time-bounded, high-bandwidth collaboration for discovery or learning new boundaries |
| X-as-a-Service | Use services with stable ownership and expectations at low coordination cost |
| Facilitation | Support capability acquisition or obstacle removal while avoiding permanent dependence |

Do not establish interaction, cognitive load, or autonomy from team names or CODEOWNERS alone. Check actual inquiries, handoffs, waiting, change/operations responsibilities, and stakeholder experience.

### Treat Conway / Inverse Conway as interaction hypotheses

Conway's Law shows that organizational communication structure and system design are not independent. Team Topologies and DORA use this relationship to consider team communication patterns and architecture independence.[^team-topologies-key-concepts][^dora-loosely-coupled-teams]

Do not prescribe Inverse Conway Maneuver as merely aligning staffing with a desired architecture diagram.

1. Observe current communication, change, and deployment dependencies.
2. Express desired outcomes as observable states such as independent change/test/deploy or reduced waiting.
3. Make a small change to responsibility boundaries or interactions.
4. Check effects on flow, coordination, cognitive load, and quality.
5. Choose the next architectural or organizational change from what was learned.

Do not implement team restructuring during assessment. Organize hypotheses, necessary stakeholders, verification methods, and small experiments. Follow [shared plan deliverables](assessment.md#plan-deliverables) for answers, Issue records, documents, and implementation; this focused lens alone does not determine Issue saving or the stopping point.

### Evaluate Microservices as an Architecture choice

Microservices are not a default derived from Bounded Context counts. Evaluate them as an option for currently needed outcomes such as independent change, deployment, scaling, and ownership.

#### Evidence that benefits are needed

- Independent release cadence is actually needed.
- Part of the system needs independent scaling.
- Failure isolation concretely benefits user value or reliability.
- Multiple teams need independent ownership, which current deployment/change boundaries obstruct.
- Technical or organizational coupling is observed that module boundaries alone cannot resolve.

#### Costs accepted at the same time

- Network latency and partial failure.
- Distributed data, transaction, and consistency complexity.
- Operational burden of observability, deployment, service discovery, and dependency management.
- API/event compatibility and versioning.
- Tooling, platforms, and on-call capabilities supporting many deployable units.

DORA also explains that adopting Microservices alone does not guarantee loose coupling, and monoliths can fit current scale and flow.[^dora-loosely-coupled-teams]

If modules or a single deployment meet current requirements, follow Simplicity / YAGNI without anticipating distributed-system costs. Do not confuse room for evolutionary separation at boundaries when needed with implementing currently unnecessary extension points.

### Ground assessment results in evidence

Record architecture/organization judgments as one of:

- **Observed practices/capabilities**: Evidence from actual changes, deployments, interactions, or similar activity.
- **Evidence-backed gaps**: Observable coupling, waiting, or failure affecting the purpose.
- **Unverified**: Missing necessary runtime, ownership, team experience, or other evidence.
- **Not applicable**: No reason at current scale and purpose to separate that boundary or choice.

Do not infer gaps solely from absence of Microservices, absence of four team types, or a single repository.

Target one problematic dependency in the first improvement. Prefer observable small experiments, such as clarifying contracts, creating test seams, removing deployment dependencies, or temporarily changing interaction modes. Do not choose wholesale service decomposition or organizational restructuring first without evidence and incremental learning.

[^ddd-reference]: [DDD Reference — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf). DDD pattern reference including Bounded Context and Context Map. Fixed 2015-03 edition rechecked 2026-09-27.
[^continuous-delivery-architecture]: [Architecture — Continuous Delivery](https://continuousdelivery.com/implementing/architecture/). Testability, deployability, loosely coupled components, and evolutionary architecture decisions. Checked 2026-09-27.
[^dora-loosely-coupled-teams]: [Loosely coupled teams — DORA](https://dora.dev/capabilities/loosely-coupled-teams/). Independent change/test/deploy, communication dependencies, Inverse Conway, and Microservices trade-offs. Checked 2026-09-27.
[^team-topologies-key-concepts]: [Key Concepts — Team Topologies](https://teamtopologies.com/key-concepts). Fast flow, four team types, three interaction modes, cognitive load, and Conway's Law. Checked 2026-09-27.
