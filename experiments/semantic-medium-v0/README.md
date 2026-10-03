# Semantic Medium v0 — first deliberate Shinden-style specimen

## Research question

Can one ordinary web surface be useful to a human while also exposing enough stable, semantic structure that a browser agent can treat it almost like a rich API — and can that surface keep its own state projection fresh without Owner maintenance?

This is not a dashboard project and not a commitment to a final SWM architecture.

The specimen exists to test whether **environmental legibility creates emergent capability**.

## Why web is a serious candidate

The founding Shinden experiment did not succeed because the agent had a purpose-built Shinden tool. It succeeded because ordinary web primitives composed unusually well:

- stable URLs;
- repeated semantic structure;
- links from collection to detail;
- tables with meaningful columns;
- browser-native navigation;
- enough regularity for the agent to invent a batch transformation on the fly.

Modern web standards already contain several underused ingredients for a dual human/machine surface:

- native semantic HTML and WAI-ARIA map meaningful page structure, controls, names, state, and live regions into browser accessibility APIs;
- JSON-LD can be embedded directly in HTML as machine-readable linked data;
- Web Linking gives typed relationships between resources;
- HTTP content negotiation allows multiple representations of one resource;
- HTTP validators such as ETag and Last-Modified provide explicit freshness/version semantics;
- server-sent events can push state changes to an open page;
- hypermedia systems such as Hydra explored machine-readable affordances and runtime-discoverable state transitions.

These are reference points, not dependencies. Hydra in particular is useful conceptually but is not a W3C standard and its Community Group closed in 2026.

## Emerging research axis: HTML itself may already be a small action protocol

Standards research after the first live readback suggests a stronger hypothesis than "semantic HTML is easy to read."

Ordinary HTML already bundles several useful layers:

- **native structural semantics** — headings, regions, lists, tables, articles and controls are mapped by browsers into accessibility APIs;
- **hyperlinks** — stable navigation plus typed relations can connect resources without copying them;
- **forms** — HTML forms expose a destination, method, named parameters, values, validation constraints, and a submit action. In other words, a normal human UI can also describe a bounded parameterized operation to an automated client;
- **embedded structured data** — JSON-LD can place a linked-data representation inside the same HTML document;
- **HTTP representation semantics** — one resource can later expose alternate representations without creating a second project world.

This suggests a possible progression:

```text
human-readable HTML
      +
browser accessibility semantics
      +
typed links / stable resource addresses
      +
native forms as discoverable actions
      +
optional structured representations
      ↓
a web surface that is simultaneously UI, observation surface, and partial action vocabulary
```

That is still a hypothesis. Do not add write forms merely to demonstrate it. First establish that read-only semantics produce useful agent behavior; then introduce one safe, reversible action and observe whether an agent discovers it naturally.

## First live findings

### Semantic readback

The specimen was opened through the existing Opera Browser Connector. Its accessibility tree exposed project state, issue objects, a draft pull request, source links, commit history, timestamps, and the refresh control as meaningful browser objects.

This matters because the browser agent did not need a custom SWM parser to recover those structures.

### Freshness

The first version read the declared research state through a raw-content URL. The preview path served stale state even while newer commits were visible.

Switching the state read to GitHub's Contents API fixed the bounded freshness test: a commit-specific frozen copy of the specimen recovered the newly updated canonical project status without editing the page's project-state content.

Scoped result:

- **PASS:** GitHub-backed projection freshness;
- **PASS:** observed live repository facts can be separated from authored interpretation;
- **not proven:** autonomous reconstruction of project meaning;
- **not proven:** cross-source state beyond public GitHub;
- **not proven:** Shinden-class emergent workflow discovery.

The caching failure is useful evidence: a medium must expose freshness and provenance explicitly rather than equating "request succeeded" with "state is current."

## Critical correction: an affordance exists only through an adapter

The native-form probe exposed an important boundary.

In Opera Browser Connector, the accessibility tree clearly exposes a search box, a select control, their human labels, selectable options, and a submit button. However, the connector available to this Browser session exposes only read/navigation operations; it has no click, set-value, select, or submit actuator.

So the environment can contain an action affordance while the current agent body still cannot execute it.

A better working model is therefore:

```text
effective affordance
    =
environment capability
∩ representation exposed by the browser/adapter
∩ actuator exposed to the agent
∩ permissions / trust
```

This prevents a dangerous category error: "the page supports X" does not imply "this agent can do X."

### The same page can progressively expose more capability

Current evidence suggests a useful experimental ladder rather than one universal representation:

1. **human + accessibility-semantic HTML** — broadly useful, and already legible through Opera's accessibility tree;
2. **DOM/source semantics** — typed links, data attributes, JSON-LD, microdata/profile conventions for clients that can inspect them;
3. **WebMCP progressive enhancement** — ordinary forms or page JavaScript can become structured agent tools in browsers that implement the proposed API;
4. **alternate structured representations / server tools** — only where headless or cross-surface access needs them.

The important invariant is not "one serialization for every mind." It is **one underlying project reality with compatible projections**, each degrading gracefully when a richer channel is unavailable.

### WebMCP is unexpectedly close to this experiment

Current WebMCP work by Google and Microsoft explicitly explores turning standard HTML forms into structured tools by adding declarative annotations. Supporting browsers derive a tool name, description, and JSON-Schema-like input contract from the same form that remains visible and useful to a human.

OpenAI's current desktop Site tools use WebMCP, so this is no longer merely a speculative standards idea.

The safe GET-form probe on this branch has therefore been progressively enhanced with WebMCP annotations. It remains a normal form when WebMCP is absent.

This is **not evidence that Opera Browser Connector can invoke WebMCP**; it cannot through the tool surface available in the current Browser session. The point of the probe is to keep the same human interaction usable while allowing richer agent bodies to discover a stronger contract.

### Another boundary: JSON-LD is not the accessibility tree

The main specimen embeds JSON-LD, but a direct Opera accessibility-tree query does not expose that JSON-LD content.

Therefore JSON-LD should not be treated as an invisible "agent API" for every browser agent. It is useful only to clients whose observation path includes DOM/source/structured-data extraction.

This again argues for layered semantic projections rather than assuming that one hidden metadata channel reaches every agent.

## Human-friendly UI can hide the world from a weak agent sensor

A progressive-disclosure probe compared three evidence placements:

- content inside a closed native `<details>`;
- content inside an open `<details open>`;
- content always visible in the document.

Opera's accessibility tree exposed the closed disclosure control itself, but **not the evidence inside it**. It exposed the evidence in the open and always-visible cases.

Because the current Opera connector has no press/click actuator, the closed evidence is effectively inaccessible to this agent even though the page is perfectly valid and usable by a human.

This produces another practical design rule for experimentation:

> Do not hide critical orientation/provenance solely behind interaction that the weakest intended agent body cannot perform.

That does not imply making every page visually flat. It means progressive disclosure needs a semantic fallback: visible summary, direct source link, alternate representation, or a richer agent channel.

## Self-updating interpretation may be an invalidation problem before it is a summarization problem

The current authored `RESEARCH_STATE.md` behaves like a materialized interpretation over changing source reality.

Instead of assuming that "self-updating" means continuously rewriting that document, the specimen now exposes:

- the exact source blob revision of the declared interpretation;
- observed live repository/work-object activity;
- a generic freshness signal when live source objects changed after the interpretation was last edited.

This immediately produced an `attention` signal because live PR activity occurred after the current declared-state revision.

The deeper hypothesis is:

```text
source observations
      ↓
derived / authored interpretation
      ↓
explicit dependencies + revision
      ↓
source changes
      ↓
invalidate / mark stale
      ↓
re-evaluate only when needed
```

That is closer to an epistemic cache with provenance than a magical always-correct summary.

It may eventually let the medium maintain itself with far less rewriting: deterministic sensors can keep observations current, while agent/human interpretations are re-run only when their dependencies materially change.

## Semantic channel matrix: the accessibility tree is useful but lossy

A dedicated probe compared multiple channels carried by the same HTML document through Opera's accessibility-tree sensor.

Observed through the current connector:

| HTML / semantic channel | Visible in accessibility tree? | Observation |
| --- | --- | --- |
| ordinary visible text | yes | baseline |
| visually-hidden accessibility text | yes | survives as semantic text |
| `aria-describedby` | yes | becomes the target object's accessible `description` |
| link `href` | yes | preserved as navigable URL |
| native form controls/options | yes | role, label, value/options, and conceptual actions are exposed |
| `<time datetime="…">` machine value | no | human-visible text survives, exact `datetime` does not |
| link `rel="…"` | no | target URL/name survive, typed relation is absent |
| `data-*` custom attributes | no | custom attribute value is absent |
| embedded JSON-LD | no | absent from this observation channel |
| content inside closed `<details>` | no | disclosure control survives; hidden content does not |

This is a crucial correction to the phrase "HTML behaves like an API."

The accessibility tree is closer to a **semantic low-bandwidth ABI**: excellent for roles, names, visible structure, links, controls and accessibility descriptions, but intentionally not a lossless DOM serialization.

A useful design implication is to reserve accessibility semantics for information that is genuinely useful to assistive-technology users too. Provenance/authority hints are a good candidate. Arbitrary machine-only protocol data is not; use a richer projection such as WebMCP, DOM metadata, structured representation, or HTTP links for that.

## Prior art points toward four separable problems, not one giant ontology

Several mature or historical web standards solve pieces of the medium problem independently:

- **ResourceSync** describes how a source advertises resources and incremental Change Lists so another system can remain synchronized without repeatedly rereading the full collection.
- **OSLC Tracked Resource Set (TRS)** models a current Base plus an ordered Change Log of creations/modifications/deletions, with a cutoff connecting the two. This is very close to the specimen's emerging "observed world + changes since interpretation" pattern.
- **Web Annotation** models a durable body attached to a target, including selectors and states for targeting a specific segment or state of a changing resource.
- **Memento (RFC 7089)** models present resources, immutable prior states, and maps between them through typed temporal links.
- **OSLC Core Discovery** separates discoverable query capabilities, creation factories, and human delegated dialogs instead of assuming every integration needs one universal interface.

These are not proposed dependencies. They are evidence that synchronization, temporal identity, annotation/provenance, capability discovery, and human UI delegation have been attacked separately before.

The potentially novel composition for an LLM medium is that a reasoning model may bridge these primitives without every relationship needing a rigid client-specific workflow.

A plausible research decomposition is therefore:

```text
world mirror:       Base + incremental changes
interpretations:    annotations/claims bound to exact source states
time:               immutable versions / version navigation
perception:         semantic HTML + accessibility projection
actions:            forms / WebMCP / discovered capabilities
agent coordination: durable environmental traces rather than message relays
```

Again, this is a research map, not an architecture commitment.

## Cognitive/ecological correction: affordance is relational

The native-form experiment accidentally reproduced a classic point from ecological psychology: an affordance is not simply a property of an object; it arises from the relation between an actor's capabilities and the environment.

For SWM, that implies there is no globally true statement such as "this page affords form submission."

More precisely:

```text
affords(agent, action)
    only when
environment exposes action
AND agent's sensor represents it
AND agent's actuator can execute it
AND trust/permissions permit it
```

This also resembles the biological concept of an **Umwelt**: the same external world becomes a different actionable perception–action world for organisms with different sensory and effector capabilities.

That framing is useful because SWM should not try to force all agents into an identical representation. It should preserve one underlying reality while allowing different agent bodies to inhabit different, partially overlapping actionable projections.

## Hyperlinks can double as dependency declarations

A new probe treats ordinary hyperlinks inside the human-authored **Current frontier** block as provisional declared dependencies.

The medium now:

1. reads the current frontier text;
2. extracts exact linked live work objects from that block;
3. compares their live `updated_at` values with the revision time of the authored interpretation;
4. marks the interpretation as a stale candidate when an explicitly linked dependency moved later.

This is intentionally much weaker than a formal dependency graph, but it tests an attractive principle:

> **natural hypertext may carry enough dependency information to support incremental semantic maintenance without a separate Owner-managed schema.**

The first implementation immediately failed in an instructive way: it scoped dependencies too broadly and accidentally pulled historical links from nested subsections into the current frontier.

That is the semantic equivalent of an over-declared build dependency graph: correct enough to notice change, but noisy enough to cause unnecessary invalidation.

After tightening the boundary to the immediate frontier block, the page recovered exactly one current live dependency: draft PR #3.

Because PR #3 has changed after the current `RESEARCH_STATE.md` revision, the page now reports:

`stale candidate — 1 explicitly linked live object(s) changed after interpretation revision`

This is a stronger signal than the earlier coarse “something in the repo changed.”

### Unexpected analogy: project interpretation as an incremental build

Build systems and incremental view-maintenance research provide a useful mental model:

```text
source resources  ─────┐
live work objects ─────┼──> interpretation node
owner decisions   ─────┘          │
                                  ▼
                           derived project view
```

When an input changes, the system need not regenerate every interpretation. It can invalidate the reverse dependents and re-evaluate only what is needed.

The hard problem is the same one build systems face:

- **under-declare dependencies** → stale but apparently valid outputs;
- **over-declare dependencies** → everything constantly invalidates;
- **precise dependencies** → cheap, trustworthy incremental maintenance.

For SWM, natural source links may provide part of that graph automatically. Agent-generated interpretations could eventually record additional dependencies they actually consulted.

This may be a more promising route to “self-updating project state” than continuously asking an LLM to rewrite a monolithic summary.

## Working hypothesis: the Web already contains most of the primitive "physics"

A nonconventional way to frame the experiment is that SWM may not need to invent a large protocol at all. The Web already supplies many orthogonal primitives:

- **identity/addressability:** URIs;
- **observation:** representations over HTTP;
- **human + weak-agent semantics:** native HTML and accessibility mappings;
- **relations:** hyperlinks and typed Web Links;
- **actions:** HTTP methods, forms, and progressively WebMCP;
- **freshness / concurrency:** validators such as ETag plus conditional requests such as `If-Match`;
- **time/versioning:** immutable version URLs and Memento-style temporal relations;
- **incremental world synchronization:** ResourceSync / OSLC TRS-style base + change logs;
- **claims attached to sources:** Web Annotation-style body/target/state patterns;
- **capability discovery:** OSLC/WebMCP-like discoverable query/action descriptions;
- **coordination:** durable traces in the shared environment rather than mandatory direct agent-to-agent messaging.

The research question may therefore be less:

> What new protocol should SWM invent?

and more:

> What minimal composition of existing web primitives creates a sufficiently rich **perception–action environment** that LLM agents spontaneously exploit it beyond the workflows we explicitly designed?

This also suggests a useful criterion: prefer primitives that compose orthogonally. A new feature is valuable when it increases the space of possible agent behavior more than it increases the number of prescribed workflows.

## Write safety may already have a web-native answer

If/when the specimen gains write actions, HTTP conditional requests deserve first-class testing.

A state-changing action can carry a precondition tied to the representation the agent actually observed (for example an ETag / `If-Match`). If another actor changed the target meanwhile, the server can reject the stale write rather than silently overwriting newer reality.

That is attractive for multi-agent work because it encodes:

> act only if the world is still the world I reasoned about.

This is a stronger safety primitive than relying on an agent to remember to re-check state immediately before every write.

No write path is added by v0 yet.

## New live findings: attention, observation cursors, and transport interoception

### Semantic topology can act as external attention

The current Opera adapter can query the accessibility tree structurally before returning content to the model.

On one healthy read of the current specimen:

- full accessibility-tree payload: **19,910 characters**;
- the `Changes since declared interpretation` region only: **2,393 characters**;
- only links inside that semantic region: **215 characters**.

That is roughly an **8.3×** reduction for the whole relevant region and a **92×** reduction for the final addressable change object compared with ingesting the whole page.

This is not a universal benchmark; it is one measured specimen + adapter. But it demonstrates a different kind of leverage from summarization:

> a semantically shaped environment can let the agent **move its attention to a small slice of the world before spending model context on the slice**.

That resembles active perception and information-foraging more than a static dashboard. The environment is not merely storing knowledge; its topology helps decide where to look next.

### Transport state is itself observable

A fetch-diagnostics probe confirmed that the page can observe useful HTTP/GitHub transport metadata:

- successful HTTP status;
- GitHub rate-limit remaining/limit/reset headers;
- an ETag validator.

So source-budget and source-version state can become part of the medium's own interoception instead of hidden infrastructure.

A conditional-observation probe then performed:

1. ordinary GET → **200** + ETag;
2. second GET with `If-None-Match: <observed ETag>`;
3. source response → **304 Not Modified**.

Scoped result:

- **PASS — observation-version binding:** the source can explicitly confirm that the representation the agent reasoned from is still unchanged;
- **not a request-budget optimization in this observation:** GitHub rate remaining moved from 54 to 53 across the conditional request.

This matters even without writes: a reasoning step can carry an exact validator rather than only "I read this recently."

### A tiny observer cursor can externalize continuity

A first browser-local cursor stored only coarse snapshot timestamps for branch / Issue / PR activity.

A deliberate PR comment was then added.

On the immediately following observation the coarse cursor reported **no change**, even though the comment existed. A later direct read showed the PR timestamp had advanced, so the exact cause may be propagation/cache lag or endpoint timing rather than a permanent semantic mismatch.

Either way, the experiment exposed a real weakness:

> periodically comparing summary timestamps can temporarily miss environmental traces.

A second probe therefore used the repository's public **event stream** as a change log.

Sequence:

1. first visit stored latest event id `22882559342`;
2. a harmless PR comment was added;
3. next visit saw new latest event `16340979308`;
4. the medium recovered exactly **1 new trace**:
   `IssueCommentEvent · #3 — Experiment: self-updating semantic project surface`.

No model memory or Owner-written handoff was needed to identify what happened between visits.

This is a tiny but real form of externalized continuity:

```text
observer cursor
      +
environmental change log
      ↓
only unseen traces
      ↓
selective re-orientation
```

Current limits are severe and explicit:

- cursor is only browser-local `localStorage`;
- GitHub public event history is finite and not a durable complete log contract for SWM;
- the probe fetches only one bounded event window;
- it does not yet decide which traces are semantically relevant.

But it demonstrates the mechanism.

### Working correction

A future agent should not need to "remember the project" in one giant internal context.

A more promising target may be:

> remember / externalize a compact observation cursor, then let the environment provide the delta and enough information scent to decide what deserves deeper re-reading.

That is materially different from both giant handoffs and perpetual full-project summarization.

## Information scent: links can carry why-to-look, not only where-to-go

The change-frontier links were progressively enhanced with accessibility descriptions explaining **why each object was surfaced**.

A structural Opera query over only links inside the change frontier now returns a compact object like:

```text
name:
  PR #3 — Experiment: self-updating semantic project surface

url:
  .../pull/3

description:
  Reason surfaced: draft pull request changed after the declared
  project interpretation revision; observed ...
```

The returned observation was **363 characters** in this probe.

This is a useful distinction:

- **address** answers "where is it?";
- **identity/name** answers "what is it?";
- **information scent / description** answers "why might it be worth spending attention on?".

The description is carried with ordinary accessibility semantics and is also useful to human screen-reader users. It is not hidden agent-only prompt text.

A promising read-side design pattern is therefore:

```text
cheap environmental cue
       ↓
agent estimates relevance
       ↓
only then acquire expensive evidence
```

That is closer to active perception / information foraging than to pushing a complete context dump into every agent turn.

## Progressive semantic resolution

The experiments suggest a possible perception ladder:

```text
L0  source health / cursor / changed dimensions
L1  identities + links + reasons-to-attend
L2  compact object summaries / deltas
L3  exact source fragments
L4  full source / wider project reconstruction
```

The environment should make moving downward cheap and reversible.

The important property is not that every agent must use these exact levels. It is that **high-cost context acquisition becomes an action the agent can choose**, rather than an unconditional prerequisite for doing any work.

## v0 hypothesis

A small page backed directly by live GitHub state may already provide more useful agent affordance than another project summary.

The first page therefore:

1. fetches live public repository state on load;
2. refreshes itself periodically and when the tab becomes active after being stale;
3. exposes freshness and failures explicitly instead of silently showing old state;
4. uses native semantic HTML first — headings, sections, articles, lists, links, buttons, time elements, definition lists;
5. exposes exact source links rather than copying source truth;
6. mirrors a small live state graph into embedded JSON-LD for clients that inspect DOM/source;
7. stays read-only so the first test isolates perception/orientation rather than permissions and write semantics.

## What is intentionally absent

- no accounts;
- no custom backend;
- no database;
- no task schema;
- no orchestrator;
- no MCP server;
- no attempt to encode all project knowledge;
- no manual Owner-maintained status fields inside the page.

## Primary experiment

Give a fresh browser-capable agent the page URL and a broad instruction such as:

> Enter this project environment, orient yourself, and decide what is worth investigating or doing next.

Do **not** teach it the page structure.

Observe three levels:

- **orientation:** can it reconstruct what the project is and what changed?
- **self-directed navigation:** does it find the relevant sources and choose useful views/actions itself?
- **emergence:** does it invent a useful transformation, comparison, or workflow that the page did not explicitly prescribe?

The third level is the real Shinden-class signal.

## Anti-success conditions

Treat the experiment as weak or failed if:

- the page is only a prettier README;
- the Owner must manually keep it current;
- the agent needs a procedure explaining where to click;
- the page replaces source truth with stale summaries;
- success depends on hidden prompt-specific wording;
- adding structure reduces exploratory freedom more than it increases capability.

## Next layers only if evidence demands them

Potential later experiments include:

- same-resource JSON representation / content negotiation;
- richer typed links and action affordances;
- event-driven refresh from repository webhooks;
- SSE or another live change channel;
- write actions with explicit preconditions and provenance;
- MCP exposure generated from the same underlying state model;
- cross-source projections beyond GitHub.

Do not add these because they are technically attractive. Add them when v0 friction identifies a concrete missing sense or actuator.
