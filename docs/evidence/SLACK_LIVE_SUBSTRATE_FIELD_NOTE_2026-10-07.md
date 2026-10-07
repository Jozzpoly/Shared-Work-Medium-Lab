# Slack live-substrate field note — 2026-10-07

**Status:** live private-workspace field observation; exploratory; evidence note, not architecture.

## Why this branch exists

A live Slack workspace connected to Browser ChatGPT exposed enough non-trivial behavior to deserve a durable research record outside Slack itself.

The question is not whether Slack is a useful chat application.

The narrower research question is:

> Can ordinary Slack primitives form a low-ceremony live exchange/event substrate around richer project media, increasing agent discoverability, routing and attention control without making Slack the project world or source of truth?

The live workspace is private. Exact workspace IDs, message timestamps, private permalinks and other transport identifiers are intentionally not copied into this public repository. The observations below were made against real objects and actions; this note preserves scoped findings rather than private transport details.

## Current environment boundary

- Browser ChatGPT is connected to Slack with read/search/action capability.
- A dedicated experimental public-in-workspace channel was created for the field run.
- The ChatGPT Slack app was added to that channel.
- The workspace currently has a Slack paid-feature trial active through 2026-11-05.
- Therefore Lists and other trial-only affordances are donor evidence, **not** Free-plan architectural assumptions.
- OpenAI Work event-triggered Slack tasks were researched but **not configured or exercised in this run**.
- Slack remains an operational surface. Durable project truth continues to live in repository/project-specific sources.

## Qualified / material observations

### 1. Exact object addressability is stronger than search freshness

A message/thread can be recovered directly from its Slack conversation identity plus message timestamp.

Fresh objects and edits were visible through direct reads before Slack search indexed them.

In one controlled mutation probe:

1. search indexed an OLD token;
2. the same message was edited in place to a NEW token;
3. direct read immediately returned NEW;
4. search temporarily continued returning OLD and could not find NEW;
5. later the index converged: OLD disappeared and NEW appeared.

Scoped finding:

> Slack search is an eventually consistent discovery projection, not current object truth. A participant should use search to locate and direct-read to verify an object when freshness matters.

### 2. Message identity survives representation/content mutation

A root message was created, given a thread reply, then rewritten into richer Block Kit representation.

Its Slack message identity remained stable and its thread remained attached.

Scoped finding:

> one Slack object can evolve without breaking local references, but it is mutable and therefore must not be treated as immutable evidence.

### 3. Quiet thread locality and channel visibility can coexist without duplication

A reply inside a thread was later promoted with Slack's reply-broadcast mechanism.

The same reply retained its message identity, remained a thread reply, and became visible on the channel timeline.

It was queryable simultaneously as a thread object and as a deliberately marked/escalated object.

Scoped finding:

> Slack already contains a native "quiet by default -> selectively escalate" primitive that preserves object identity rather than copying content.

This resembles the attention-sovereignty pressure in Quiet Presence, but no claim is made yet that it reduces Owner burden in practice.

### 4. Reactions are a queryable sideband

Reactions can be added without changing message text and can be used in structural search filters.

A multi-facet query over two reactions successfully recovered exactly the message carrying both marks.

Connector-added reactions are attributed to the authenticated Owner account, not to a distinct Browser-agent identity.

Scoped finding:

> reactions can act as cheap handling/attention/discovery facets, but must not be treated as epistemic truth or agent identity.

Because OpenAI's documented Slack event triggers respond to new messages rather than reactions/edits/deletions, reactions are also a candidate quiet sideband. This specific interaction with a live Work trigger remains untested.

### 5. Timeline and search can behave as different sensors over the same channel

A time-bounded direct channel read exposed the main timeline, including top-level objects and a deleted-root tombstone.

A time-bounded channel search over the same period also recovered quiet thread replies.

Filtering for thread replies produced a deeper local event stream.

Scoped finding:

> Slack offers several different observational projections over the same underlying conversation. A calm human-facing timeline and a deeper agent event view need not be identical.

### 6. Deletion preserves a tombstone and direct thread relation, but discoverability can degrade

A sacrificial thread root was deleted after receiving a reply.

Direct thread read still returned:
- a tombstone at the original root identity;
- the surviving reply.

Exact keyword search for the reply under the deleted root failed, while broader time-window/thread search could still surface it.

Scoped finding:

> existence, direct recoverability and search discoverability are distinct properties.

### 7. Browser/Owner provenance is flattened by Slack account authority

Messages written by Browser ChatGPT through the connector appear under the Owner's Slack account and carry a "sent using ChatGPT" marker.

This is useful operational provenance but is not enough to claim that the Owner authored the statement epistemically.

Scoped finding:

> Slack identity currently distinguishes account authority and tool origin better than mind/claim origin. A shared medium must not infer Owner judgement merely from Slack's message author field.

### 8. Rich human UI can become lossy for the agent

Block Kit can create useful human-facing cards and controls.

Observed projection differences:

- headers, markdown, context and section fields survive direct connector reads well;
- URL buttons expose their labels in connector reads, but the button URL is not reliably available as searchable link content;
- raw URLs repeated in semantic text remain machine-visible and human-clickable;
- native plan/task-card contents were largely absent from ordinary connector reads and searches even though the plan rendered in Slack.

Scoped finding:

> richer product-native representation is not automatically a richer agent representation. Critical affordances/sources should remain explicitly exposed in machine-legible text unless an exact projection has been verified.

This is a concrete Slack instance of the broader SWM rule: surface is not world.

### 9. Section fields are a promising Free-compatible dual-use envelope

A message built from ordinary Block Kit section fields preserved a compact human card while direct connector read recovered:

- shared referent;
- authority/status;
- origin;
- local lens;
- research question;
- source URL.

Slack search later located the object by a field-contained referent, although the search result body was empty. Exact dereference then recovered the full card.

Scoped finding:

> a useful retrieval path is "search as locator -> exact message dereference", and simple message fields currently outperform richer task-card structures for dual human/agent use.

### 10. Lists expose an unexpected compositional affordance during the current trial

A small derived List was created with referent/kind/state/source rows.

Observed behavior:

- record content can make the List discoverable through generic Slack file search;
- the List can be read through the specialized List action;
- more surprisingly, the generic Slack file reader exposes the List as CSV, including row referents and source links;
- therefore a participant can recover an exchange through:
  generic file search -> File ID -> generic file read -> source permalink -> exact source thread.

This path does not require the participant to know that a specialized List API exists.

Scoped finding:

> this is Shinden-like evidence of capability emerging from composition of ordinary affordances rather than a prescribed workflow.

However Lists are currently trial-only donor evidence and must not become a baseline dependency.

### 11. File transport is a body/capability-chain problem, not simply a Slack capability

Slack successfully issued a signed upload URL and file ID for a proposed evidence packet.

The current Browser execution body could not perform the required raw-byte POST to the Slack upload host.

Scoped finding:

> the Slack capability exists, but this Browser body currently lacks the full transport actuator chain. Capability discovery must distinguish "service cannot" from "current body cannot complete the action path."

### 12. Private draft staging exists outside shared channel reality

Browser ChatGPT can create a Slack draft attached to the channel.

The draft did not appear in channel reads or search and was visible only as Owner-side draft state.

A second draft call produced behavior inconsistent with the tool description; the Slack UI still exposed one channel draft. Multi-draft semantics are therefore not qualified.

Scoped finding:

> drafts are a possible private Owner-attention staging surface, but they are not part of shared channel reality and their capacity semantics require more evidence.

### 13. Slack can persist a future message and emit it later without an active Browser turn

Browser ChatGPT scheduled a bounded probe message for an exact future time.

Slack accepted the schedule, retained it, and later emitted a new ordinary channel message at the requested time without a contemporaneous Browser send action.

The emitted message was then recoverable through both direct channel read and search.

Scoped finding:

> Slack already provides a small persistent temporal actuator: present cognition can deposit a future event that Slack emits later.

This does **not** yet prove delayed cognition. A future Work experiment must still establish whether a scheduled Slack message can appropriately trigger an event-driven ChatGPT task without loops, false activation or attention debt.

### 14. Scheduled local events and visibility escalation are separate actuators

A second temporal probe scheduled a future reply inside an existing thread and requested `reply_broadcast=true`.

At the scheduled time Slack created the reply inside the thread and search recovered it as a thread message. It did **not** appear on the channel timeline.

A later explicit `reply_broadcast` action against that already-created reply immediately projected the same message object onto the channel timeline without changing its message identity.

Scoped finding:

> Slack can separately persist **when** an event should appear and later decide **how visible** the same event should become. In the tested connector path, scheduled thread creation and channel escalation did not collapse into one actuator.

This falsifies the stronger assumption that scheduling a broadcast reply is equivalent to scheduling a reply and later broadcasting it.

## External Slack-platform donor reconnaissance

The following items come from current Slack/OpenAI platform documentation and were **not live-qualified in this field run**. They are donor/capability hypotheses only.

### Incoming webhooks

Slack apps can receive a channel-scoped incoming webhook URL and publish JSON/Block Kit messages, including replies to existing threads when a thread timestamp is known.

Potential relevance:

`lab / CI / Cloudflare runtime -> HTTP event -> Slack -> Browser/Work`

This could provide a cheap universal ingress from systems that do not need the Browser connector itself. Webhook URLs are secrets and must never be stored in public research artifacts.

### Message metadata

Slack supports machine-readable message metadata built around an event type plus payload, explicitly intended for app-to-app/app-to-Slack coordination.

This is conceptually attractive as a parallel channel:

`human-visible event + machine-readable event payload`.

The current ChatGPT Slack connector used here does not expose metadata writes or an `include_all_metadata` read path. Treat this as substrate capability currently outside the Browser body's verified sensor/actuator surface.

### Work Objects

Slack Work Objects model external entities with a stable external reference while the authoritative object remains in its source system. Slack can render the object into conversations/flexpanes and associate related conversations with the same referenced entity.

This independently resembles a core SWM pressure:

> keep source truth external while giving Slack a rich, addressable local projection and conversation context.

Current Slack help material associates important Work Object preview capabilities with paid plans, so treat this as trial/paid donor evidence unless separately verified on Free.

### Slack MCP and Real-time Search

Slack now exposes an official MCP server / agent-oriented tool surface for searching and acting on Slack data, plus real-time search primitives intended for AI applications.

This is significant prior art for treating Slack not merely as a human chat UI but as an agent-readable/actionable environment.

No claim is made that the ChatGPT curated Slack connector in this experiment is internally identical to Slack's public MCP implementation.

### Slackbot MCP Client

Current Slack documentation also describes Slackbot as an MCP client capable of discovering and invoking tools from remote MCP servers.

Potential long-term implication:

`local lab / SWM capability service -> MCP -> Slackbot`

could invert the current relationship: instead of Browser reaching into Slack, an agent living in Slack could reach into project-specific tools.

This path is not configured or live-tested here.

### Slack Code / Agent Sessions

Recent Slack platform/product work provides temporary agent task spaces, agent-session lifecycle, artifacts/previews and multi-agent participation.

This is useful independent donor evidence for a distinction already emerging in SWM:

- a thread can be enough for a small bounded exchange;
- a larger task may deserve a temporary dedicated work surface;
- that surface should not automatically become permanent project topology.

Availability varies by supported agent and rollout. Do not infer that the installed ChatGPT Slack app in this workspace currently supports Slack Code without a live qualification.

### 15. Trial Canvas is directly rich but discovery-shallow

A standalone Canvas donor probe was created during the active paid-feature trial.

Observed behavior:

- the specialized Canvas read returns full Markdown plus section IDs;
- generic Slack file read also returns the full Canvas as Markdown;
- a targeted section replacement changed one paragraph without rewriting unrelated content;
- a fresh read preserved the same observed section IDs in this specimen, despite the connector's conservative instruction to refresh IDs before each mutation;
- generic file search found the Canvas reliably by title;
- search by a unique token stored only in the Canvas body did not find it.

Scoped finding:

> Canvas is a strong direct long-form object once its File ID is known, but its content is a weak discovery surface in the current connector. Again, shallow locator -> rich dereference is stronger than assuming one search surface exposes the full object.

Canvas is a paid/trial donor here, not a Free baseline dependency.

### 16. Natural-language query input did not demonstrate semantic retrieval in this connector

Two search probes used only natural-language descriptions of:
- the actor/world/private-evidence cross-lab signal;
- the identity/authority versus representation/projection signal.

Without lexical keywords, the connector returned a broad chronological set from the channel rather than clearly ranking the intended signal first.

Scoped finding:

> do not assume that a `natural_language_query` field or the presence of Slack AI proves useful semantic retrieval in this Browser path. Explicit referents, facets and exact source links remain the more reliable discovery mechanisms.

Slack's separate Real-time Search API documents semantic retrieval under supported conditions, but that platform capability is not evidence that this connector invocation exercised it.

### 17. ChatGPT app presence is not Slack Agent presence

The live Slack UI was opened directly at the `Agents & tools` surface.

It reported:

> Your org doesn't have any agents yet.

This is true even though the normal ChatGPT app is installed and appears in the workspace sidebar.

Current product research also distinguishes the standard ChatGPT Slack app/connector from the separate ChatGPT Agents app for ChatGPT workspace agents.

Scoped finding:

> app presence, connector capability and Slack-native Agent presence are distinct capability classes. Do not infer Agent Sessions or Slack Code capability merely because the ChatGPT app/connector is installed.

For this Owner's current personal Plus setup, the separate ChatGPT workspace-agent route is not a baseline: current OpenAI documentation requires organizational ChatGPT plans and paid/admin Slack setup.

### 18. Candidate generation is a different problem from routing

A reread of the current-truth-topology research sharpened the role a shared live layer would actually have to earn.

PR #9's T0/T1/T2-style work can test whether an agent chooses the right authority plane or route **after relevant candidates exist**. Its own interpretation ceiling explicitly does not establish cross-project capability routing.

Earlier Medium work also separated:

- **candidate generation** — does the relevant other project/world enter the candidate set at all?
- **routing** — once candidates exist, which one should be inspected?

Live project-local front doors reduce orientation cost inside a known world, but they cannot by themselves make an unknown relevant other world cognitively available.

This produced a new Slack field signal:

`swm://exchange/peripheral-candidate-generation-004`

Scoped hypothesis:

> a sparse, source-linked, time-decaying event/scent stream may provide peripheral cross-project candidate generation without mirroring local project state or maintaining a central capability registry.

The receiver still decides relevance under its own local goal.

Ecological success remains strict:

> an agent pursuing a non-SWM goal independently notices a relevant scent, follows the source, and materially advances its own work without Owner routing.

No such fresh-subject PASS exists yet.

### 19. Free Slack retention may be useful decay, not merely loss

Current Slack Free documentation limits visible/searchable message and file history to the most recent 90 days; workspace data older than one year may be permanently deleted depending on retention settings.

For durable project truth this is unacceptable, so Slack must not be the archive.

For **peripheral scent**, however, natural decay may be desirable:

- recent material changes remain ambiently reachable;
- old local churn disappears from the shared peripheral surface;
- durable evidence stays in project repositories/local media;
- a stale shared feed is less likely to harden into a second project history.

This is a design hypothesis, not a reason to rely on deletion for correctness. Any event worth durable preservation must still return to its authoritative project/source.

### 20. Workflow Builder suggests a deterministic reflex layer before cognition

The active Slack trial exposes Workflow Builder. Current Slack documentation supports event triggers including emoji reactions, message events/keywords, schedule, webhooks, channel/user events and List-related changes, with ordinary Slack actions such as sending a message as workflow steps.

This suggests a compositional circuit:

`quiet object / reaction -> deterministic Slack workflow -> new activation message -> event-driven Work -> LLM cognition`

The important property is **selective wake**:

- ordinary thread traffic can remain quiet;
- reactions/edits can remain sideband state;
- one deliberately chosen event can be converted into a fresh message only when cognition is warranted.

This would make Workflow Builder a lightweight reflex/router in front of an expensive reasoning body rather than an AI workflow engine.

It has **not** been live-built or connected to Work in this run. Workflow Builder is paid/trial-only. If the mechanism proves valuable, a minimal custom Slack app / event receiver could later reproduce only the justified reflex on Free instead of making Workflow Builder architectural infrastructure.

### 21. Drafts are not yet a qualified private attention gate

Earlier draft probes were verified immediately after creation as:
- present in `Drafts & Sent`;
- absent from channel reads;
- absent from search.

More than an hour later, two of those same draft texts appeared as ordinary channel messages with new message timestamps around 23:05 CEST.

The transition cause is currently unknown.

A new control draft, `SWM_DRAFT_LIFECYCLE_PROBE_J3K9`, was then created and immediately rechecked. It was again private: one item in `Drafts & Sent`, absent from channel read and search.

Scoped correction:

> draft creation is real private staging at creation time, but long-lived draft lifecycle/commit semantics are **unqualified**. Do not use drafts as a critical attention-sovereignty primitive until the delayed publication transition is explained or shown not to recur.

### 22. The connector explicitly reports semantic search unavailable for this user

The Slack search action contract states:

> Semantic search is not available for this user.

This explains the earlier natural-language-only probes that returned broad chronological candidates rather than the intended cross-lab signal.

Scoped consequence:

> explicit referents, source doors, reaction facets, temporal cursors and exact dereference are not merely conservative preferences; they are the currently verified discovery substrate for this Browser body.

Do not infer semantic retrieval from the presence of a `natural_language_query` field or from Slack AI availability elsewhere in the product.

### 23. Tool/skill availability is still not action reachability

The installed skill catalog includes Trigger Tree (Codex-local documentation-discovery telemetry) and skills for parallel/subagent workflows.

The current Browser runtime exposes no actual subagent spawn/delegate actuator, and Trigger Tree's telemetry depends on Codex-local project hooks/scripts that this Browser body does not possess.

This repeats a now-common boundary:

`capability definition exists -> current body can discover it -> current body still may not be able to exercise it`.

This is relevant to Medium's operational proprioception goal: discovery must include the exact executable action path and effect-verification seam, not merely names of tools/skills.

### 24. Opera exposes an existing human-generated peripheral substrate

The Opera connector provides:
- open-tab topology;
- accessibility reads of those tabs;
- browser history up to seven days old.

A bounded 7-day history inspection during this run contained recent traces across multiple active project/chat/source surfaces. Crucially, some URLs exposed specific experimental Pages and CI/source objects, not merely project names.

This suggests a strong counter-hypothesis to purpose-built cross-project event infrastructure:

> the Owner's ordinary browsing behavior already leaves recency-weighted environmental traces that an agent can use as candidate-generation scent.

This resembles stigmergic coordination more closely than a central capability registry: no explicit handoff or relevance score is required.

Boundaries:
- browser history is not project truth;
- open tabs can be stale;
- unrelated/private browsing must not be promoted into project context merely because it is observable;
- the current observation is from one Owner/body and does not establish transfer to other agents;
- a purpose-built Shared Medium layer earns its role only if it adds useful reachability beyond this natural working-set substrate.

### 25. Bot-origin scents require an explicit sensory contract

The Slack search action defaults to `include_bots=false`.

A controlled check against an existing Slack bot DM produced:
- `include_bots=false` -> no result;
- `include_bots=true` -> exact bot message recovered.

This matters for the proposed external-ingress path:

`runtime / CI / webhook / custom app -> Slack scent`

because those events are likely app/bot-origin.

Scoped finding:

> an emitter can succeed while the receiving agent's default search sensor silently excludes the emitted class.

For bot/app scents, candidate-generation probes must explicitly verify the actual perception path. Channel-delta reads and Work event triggers require their own empirical qualification; do not infer them from search behavior.

## Cross-project signals observed during the field run

These are **candidate relations**, not shared architecture.

### Live experimentation -> research memory

Combat and ReflexBrain independently create pressure for a low-ceremony way to preserve observations from live intervention without prematurely freezing a universal ontology.

Candidate question:

> can one lightweight observation envelope carry a referent, Owner observation, evidence/source and local interpretation while letting each lab retain its own meaning?

### Actor/world boundary

ReflexBrain, LLM Live NPC and Companion independently defend distinctions between world truth, actor-relative evidence/private state, internal proposal/intent and world action/outcome.

Candidate question:

> can shared traces preserve those stages without accidentally granting private knowledge or imposing one cognition architecture?

### Identity/authority != representation/projection

FrameMatter, Jozzue Vehicles Sandbox and Planet Matter independently separate authoritative/logical identity from current physical/render/storage/surface representation.

The Slack field run produced an analogous pressure: one message identity has multiple lossy and eventually-consistent projections.

Candidate question:

> is authority/identity independent of replaceable projection a recurring design invariant across these projects and the Medium itself, or is this an over-generalization of superficially similar separations?

Keep this falsifiable.

## Current working model

The strongest current model is not "Slack becomes the Medium".

It is:

- project/repository/world state remains the durable/local authority;
- each lab can develop its own medium appropriate to its research;
- Slack can serve as a live exchange/event/peripheral-vision layer between them;
- a Slack thread can be a local exchange window around one referent;
- search can locate candidates;
- direct read verifies current object state;
- reactions can provide quiet handling facets;
- reply broadcast can selectively raise visibility;
- trial-only derived projections such as Lists may teach us useful patterns without becoming dependencies.

## Important nonclaims

This run does **not** prove that:

- Slack improves project outcomes;
- another agent will independently discover and use these affordances;
- Owner attention cost is reduced;
- cross-project signals will remain useful rather than becoming noise;
- Work event activation selects good moments to think;
- the current Slack trial capabilities survive downgrade;
- Slack should become canonical infrastructure;
- the provisional `swm://...` referent convention is a final namespace;
- the current observation-envelope shape should become a schema.

## Next high-value gates

1. In Work, run one tightly bounded real Slack event-trigger experiment and measure false activation, missed value and Owner attention cost.
2. Qualify the strongest external-ingress candidate: a minimal incoming-webhook app feeding one sparse lab/runtime event into the live exchange surface.
3. Test whether a scheduled Slack message can serve as a deliberate future wake signal once the Work event leg exists.
4. Test fresh-agent recovery using only generic affordances:
   search -> locator -> exact dereference -> source verification.
5. Treat message metadata, Work Objects, Slack MCP, Slackbot MCP and Slack Code as donor capabilities until their exact plan/body boundaries are live-qualified.
6. Keep trial-only Lists as donor research and deliberately test what remains after the paid trial ends.
7. Do not expand channel topology unless real traffic creates pressure. In particular, avoid mirroring the project tree into one channel per lab by default.
8. Alternate live ecological dogfood with controlled probes. Do not let Slack feature exploration become the new project goal.

## Privacy / evidence boundary

Exact private Slack identifiers and permalinks are intentionally omitted from this public note.

The private workspace currently contains the live specimens and exact transport references. This public branch records scoped mechanics and research implications only.

