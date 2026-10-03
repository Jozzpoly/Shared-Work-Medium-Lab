# Research State

**Status:** early live campaign; repository bootstrap started  
**Last material update:** 2026-10-03

## Live truth

The project is no longer only a conversation. This public repository is now the first shared substrate used to develop and observe the system itself.

This does **not** mean GitHub is the final Project World.

GitHub is currently useful because it already provides:
- durable public references;
- version history;
- repository-native access for Codex;
- direct access for Browser through the GitHub connector;
- issues, commits, PRs, and Actions as existing inspectable objects;
- a place where the lab can later grow executable code.

## Current leading architectural hypothesis

The first useful organism likely needs two coupled loops.

### Epistemic loop

**refer → orient → verify source**

A participant should be able to:
- identify the exact thing;
- recover its role in the current project state;
- trace important claims back to appropriate sources/authority.

The currently suspected high-leverage properties are:
- addressable reality / stable shared referents;
- recoverable orientation;
- source and authority lineage.

### Operational loop

**sense capability → act → verify effect**

A participant should be able to:
- know which relevant capabilities/bodies are available;
- choose an appropriate action surface;
- distinguish confirmed effect from assumed effect, failure, interruption, or unknown liveness.

This is the beginning of agent operational self-awareness / proprioception.

## First capability bridge candidate

Browser ↔ Codex remains the strongest first candidate because the pair already exists in real work:

- Browser often has broader project/Owner context;
- Codex has stronger repository-native execution;
- today the Owner often acts as a manual bridge between them.

The desired property is **not** a hardcoded Browser→Codex workflow.

The goal is to create shared primitives from which that workflow can emerge:
- one exact shared referent;
- enough orientation to understand why it matters;
- links to the relevant source/authority;
- a place for new repo-native evidence to attach.

## Public/private boundary

The repository is intentionally public.

Current policy is deliberately light:
- public by default for lab code, research, protocols, synthetic specimens, and non-sensitive development history;
- do not force a public/private split where it adds cost for no benefit;
- preserve the ability to attach private sources or a private data layer later when real data justifies it;
- never treat public GitHub storage as a requirement for all future project-world data.

No second private repository is currently required.

## Cloudflare

Cloudflare is **not rejected**.

It should be introduced as soon as a durable capability actually benefits from it — for example a persistent service, authenticated/private data surface, MCP endpoint, webhook/event receiver, or other always-available network body.

It is intentionally not being added before there is a concrete service to host.

## Material evidence from previous collaboration

The campaign is grounded in recurring real patterns:

- semantic browser structure enabled an unplanned high-leverage workflow;
- long handoffs and dead chats create Owner recovery burden;
- machine PASS and Owner experiential FAIL can both be valid at different scopes;
- Browser and Codex have complementary strengths but fragmented context;
- very short "continue" instructions work well when task identity and current truth are already recoverable;
- chat UI liveness is not a reliable proxy for tool/run liveness.

## Current frontier

Use the repository itself as the first self-hosting environment.

The first question is not "which database do we need?"

It is:

> Can a simple shared referent in this repository already reduce context transfer and let Browser and Codex coordinate around the same work object without turning the Owner into a courier?

GitHub Issue #1 is the first live specimen.

## Deliberately unresolved

Not decided yet:
- formal object schema;
- database/storage architecture;
- MCP API;
- Cloudflare topology;
- event system;
- universal task lifecycle;
- rich UI/sidebar;
- multi-provider agent integration;
- cross-project memory;
- whether Issues remain useful once the lab grows.

These remain hypotheses until real friction forces a decision.
