---
type: Instruction
title: Design and ubiquitous language
description: Clarify domain rules, terminology, model boundaries, and dependencies.
---

## Design and ubiquitous language

DDD guides what to model, and XP guides how to discover and evolve that model through small feedback cycles. This environment combines them as the subject of design and the way to proceed.

- Use DDD as the basis of design, and check terminology, rules, invariants, and model boundaries. Express domain rules in the model, separating them from technical processing such as UI, communication, and persistence.
- Distinguish subdomains in the problem space, bounded contexts within which a model's meaning applies, and repositories as code management units.
- Show the relationships among contexts, modules, services, repositories, and owning teams, the reasons for these choices, and dependencies, contracts, and translation across boundaries. Do not require uniform one-to-one mappings or decomposition.
- Record terms, domain definitions, applicable model boundaries, and code names in the glossary `docs/glossary.md`. Align terminology in features, tests, and implementation within the same boundary, and update them together when meaning is added or changed. Ask the user about ambiguous meaning instead of settling it by assumption.
