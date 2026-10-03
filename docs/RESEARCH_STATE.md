# Research State

**Status:** direction reset after local Codex setup friction; next phase is broader collaboration/capability architecture review

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

## Next-session gate — full conversation audit required

Do **not** resume implementation or open another capability experiment merely from the current repository summary.

Before the next serious phase, re-read the originating Browser conversation from its beginning as a primary source and reconstruct:

- the actual problem that motivated SWM;
- the progression from the founding browser/semantic-environment experiment into the broader shared-work idea;
- Owner-confirmed needs versus assistant-generated architectural hypotheses;
- points where the assistant narrowed the project too early;
- decisions that were useful, accidental, premature, or contaminated by the experiment setup;
- which current repository documents faithfully preserve the conversation and which may already encode drift;
- the smallest serious next move after that audit.

The repository is an externalized working state, not a substitute for this primary-source audit.

Until that audit is complete, the current direction reset is **provisional** and no new architecture should be treated as established.

## Strategic direction reset — 2026-10-03

The local Codex Desktop path reached a deliberate stop condition: setup and workspace friction became more expensive for the Owner than the experiment was worth.

This is not merely a tooling inconvenience. It is direct evidence against a design direction that requires the Owner to provision, route, debug, or babysit agent bodies.

The campaign is therefore stepping back from the narrow question:

> How do we validate Browser ↔ Codex continuity first?

and returning to the broader North Star:

> How do we increase the Owner's ability to run increasingly ambitious work without proportional growth in AI/context/tool-management burden, while also expanding agent perception, action, continuity, and emergent capability?

### Broader collaboration constraints recovered

Across previous project work, the recurring successful pattern has been:

- Browser ChatGPT as the primary project brain / integrator / Owner interface;
- specialized bodies such as Codex for repo-native execution when they have a clear advantage;
- repositories and artifacts as external authority;
- short continuation prompts when the environment already exposes enough live state;
- Owner involvement mainly for vision, feel, priorities, product judgement, and genuinely consequential choices.

Recurring failures have been:

- Owner acting as courier between surfaces;
- long handoffs becoming stale compressed substitutes for reality;
- local/tool-specific optimization drifting from project intent;
- agent capability being present but undiscoverable or awkward to invoke;
- technical setup and workflow ceremony exceeding the value of the task;
- treating one special surface as mandatory for the whole system.

### New directional consequence

The first useful SWM organism should **not require a fragile specialized body to prove the concept**.

The next phase should look for leverage in the Owner's default, already-used collaboration environment first — especially Browser ChatGPT plus durable shared sources — and treat Codex, Work, Opera, GitHub, future models, and future MCP services as attachable bodies/senses rather than prerequisites.

A specialized body should join when it creates clear net leverage with low Owner setup cost.

### Revised search target

Before another implementation experiment, identify the smallest environmental capability that:

- helps real Browser-led work immediately;
- reduces Owner routing/context-repair burden;
- is usable without bespoke local setup;
- creates or amplifies agent capability rather than only organizing records;
- remains compatible with later Codex/Work/other-agent attachment;
- can be dogfooded by SWM itself.

Candidate directions include shared durable orientation, capability discovery/proprioception, and agent-native project perception, but none is yet selected.

### Current stop rule

Do not spend further Owner attention on repairing the current Codex Desktop workspace path unless later evidence makes that path unusually valuable.

Issue #2 remains useful evidence and can be revisited under better conditions, but it is no longer the campaign's immediate frontier.

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

Re-evaluate the first-build direction from the broader collaboration North Star before starting another setup-heavy experiment.

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

### Browser source verification — 2026-10-03

Browser independently fetched commit `df369fee0631f677c306b1ac4d449ce123ea23e6`, the current research state, Issue #1 and its comments, `AGENTS.md`, and `START_HERE.md`.

The persisted Codex result is internally consistent with those sources and is correctly scoped.

However, the Owner had already pasted the Codex transcript into the Browser chat before this repository verification. Therefore this is **source verification, not a clean blinded Browser return-leg observation**.

Do not claim the full Browser↔Codex loop is validated from this run.

### Next evidence needed

The first recovery used a very capable Codex configuration. That establishes that the environment is sufficient for one strong model, but does not isolate how much capability came from the environment itself.

The next useful experiment is therefore a **fresh lower-capability Codex recovery from inside the repository with minimal human instruction**.

The preferred first probe is a Luna-class Codex configuration at low/light reasoning effort. If it succeeds cleanly, stronger effort is unnecessary. If it fails materially, repeat with a higher Luna effort before concluding that the environment is insufficient.

The run should start with the repository already open so that repository-native instruction discovery is exercised. The human prompt should be intentionally minimal, ideally only:

> Continue consciously from the live project state.

The model should recover the active experiment from repository state, respect the existing evidence boundaries, avoid inventing infrastructure, and persist any material result durably.

This next experiment is tracked in Issue #2.

The Browser↔Codex bridge currently has **one source-verified high-capability Codex recovery**.

### First Luna probe — invocation friction observed

A fresh Luna-class session was given the repository URL and a minimal continuation prompt, but the session started in a generic workspace rather than inside a checkout of this repository.

Luna correctly detected that mismatch and did not claim to possess live repo state. Ordinary web access did not recover the repository. After the Owner explicitly invoked the GitHub connector, Luna recovered the current commit, Issue #2, the orientation files, and the scoped evidence boundaries correctly.

It also correctly refused to treat that run as completion of SWM-0002 because repository-native `AGENTS.md` discovery had not been exercised.

This creates a useful distinction:

- **environment comprehension:** promising at the Luna level once the GitHub sensor was available;
- **body/capability discovery:** still weak enough that the Owner had to manually route the agent to `@GitHub`;
- **in-repo automatic orientation:** still untested.

The next clean test remains a fresh Luna session started with this repository already opened/checked out, with only the minimal continuation prompt.

Automatic instruction discovery, clean lower-capability in-repo reliability, interruption recovery, repeated reliability, and a clean independent Browser return leg remain unproven.

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
