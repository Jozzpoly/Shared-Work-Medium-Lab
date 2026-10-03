# Research State

**Status:** first Codex recovery observed; independent Browser readback pending

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

### First implemented capability bridge

A root `AGENTS.md` now gives Codex a lightweight repository-native orientation contract:

- recover the project from `START_HERE.md` and live repository state;
- follow source/authority distinctions;
- inspect Issue #1 as the current shared referent;
- avoid giant context dumps and premature infrastructure.

This is intentionally a **map**, not a substitute for the project.

### First observed Codex recovery — 2026-10-03

The Owner supplied the repository URL and asked Codex to recover the project, consciously continue the current work without an additional handoff, and persist any material result in the repository.

**Source version:** [`f7a84c2f4e0c39c0e65a2bc5cf52efcdb6eaae34`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/commit/f7a84c2f4e0c39c0e65a2bc5cf52efcdb6eaae34).

Codex cloned that version, read all six tracked files, followed `AGENTS.md` and `START_HERE.md`, and independently retrieved [Issue #1](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/1) and its [initial capability-bridge comment](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/1#issuecomment-5963506774). Live GitHub searches returned that single issue and no pull requests. No executable code, build configuration, or test suite existed at this version.

The recovered task was the issue's **First bounded task**: determine the minimum additional repository structure needed to receive one precise investigation without an Owner-written campaign handoff. The repository's latest frontier explicitly asked for this fresh Codex observation. This run therefore continued the existing experiment rather than selecting a new architecture.

**Bounded judgement:** no additional receiving structure or code is needed for this specimen. The entry files supplied purpose and authority rules; Issue #1 supplied a precise investigation, constraints, and a legitimate no-code outcome. Codex did not need the founding Browser conversation to answer that bounded task. The missing artifact was the observation and its result, now recorded in this existing state document and attached to the same issue. This adds evidence, not a new task schema, service, or mandatory form.

Observed scope:

| Question | Observation / limit |
| --- | --- |
| Can Codex find and follow the orientation map? | Yes in this run, after cloning and explicitly locating and reading `AGENTS.md`. Automatic instruction discovery was **not** independently tested: the chat began outside the repository. |
| Can it recover the frontier without an Owner-written handoff? | Yes. The recovered frontier came from the versioned documents and live Issue #1; the Owner supplied no additional project context. |
| Can it make a bounded repo-native judgement? | Yes: existing primitives suffice for this first investigation; persist the result and defer infrastructure. This is a research judgement for one specimen, not proof of general sufficiency. |
| Can the result survive the Codex session? | The return path is this versioned document and an issue-linked result. The issue comment must carry the published commit reference and report remote readback; a local edit alone does not establish persistence. Interrupted execution was not exercised. |
| Has Browser recovered the result independently? | Not observed in this run. No Browser participant has yet confirmed recovery from the published objects. |
| Has Owner burden been reduced? | No campaign handoff or low-level technical decision was requested during this run. A quantified improvement, repeated reliability, and Owner experiential acceptance remain unmeasured. The Owner still initiated this run. |

### Access friction observed

Repository files alone did not contain the issue body or discussion. A participant needs an actual issue-reading capability; the reference does not imply access.

In this environment, the initial Git clone failed in Windows Schannel. A command-scoped `git -c http.sslBackend=openssl clone ...` succeeded. Local `gh` reads returned HTTP 401, while the authenticated GitHub connector successfully read repository metadata, Issue #1, its comments, and issue/PR searches. The connector reported push permission as available, but a reported permission is not evidence of a completed write.

These are environment-specific observations, not reasons to build a backend. The existing Git and connector surfaces were sufficient to recover the shared object. A future participant should check its own capabilities and distinguish an access failure from a missing object or missing project context.

### Next evidence needed

A fresh Browser participant should enter through the repository and [Issue #1](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/1), recover this Codex result without the Owner copying it, and attach a short source-linked readback to the same issue. The readback should identify:

1. which version/result it actually read;
2. the no-additional-structure judgement and its scope;
3. what remains untested;
4. the smallest justified next experiment, or that no new implementation is justified yet.

This is an evidence request, **not a dispatched task or an automatic wakeup**. No new service or workflow is required to attempt it. Keep Issue #1 open while this readback is pending. If access or interpretation fails, record the specific failed source/action before proposing an addition.

The Browser↔Codex bridge now has **one observed Codex recovery**, but is **not yet validated as a complete working collaboration loop**. A Browser readback would establish one return leg; it would still not prove automatic dispatch, interruption recovery, repeated reliability, or product-level acceptance.

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
