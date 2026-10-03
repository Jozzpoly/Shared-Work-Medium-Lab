# Body × Projection Calibration Protocol v0.1

**Status:** pre-experiment calibration design

## Purpose

Measure what a concrete agent body can actually perceive, operate, persist, and verify before using that body in structural SWM experiments.

Do not infer capability from product names, standards support, or documentation alone.

## Core rule

An environmental affordance is usable only when all relevant layers line up:

```text
environment exposes capability
∩ body observation channel represents it
∩ body actuator can execute it
∩ permissions/trust permit it
∩ effect can be verified
```

A failure at any layer must not be reported as model reasoning failure.

## Calibration fixture

Use one neutral page/environment that contains independent probes for:

### Perception channels

- ordinary visible text;
- semantic headings/regions/lists/tables;
- link URL;
- link relation metadata;
- `<time>` visible text + exact `datetime` value;
- accessibility-only description;
- closed and open native disclosure;
- DOM `data-*` attribute;
- embedded JSON-LD;
- dynamically inserted text after page load;
- screenshot-only visual marker not present as text;
- downloadable source representation where supported.

### Action channels

- ordinary link navigation;
- button press;
- text input/set value;
- select/combo choice;
- GET form submission;
- harmless POST that increments a fixture-local counter;
- file download;
- copy/read clipboard only if the body legitimately exposes it;
- declarative WebMCP tool on the same human-visible form;
- imperative tool exposed only to richer compatible bodies.

### Persistence channels

- same-page JavaScript state;
- URL/query state;
- localStorage/cookie where permitted;
- server-side observer cursor;
- fresh-session recovery from durable external state.

### Verification channels

Every action has an externally visible exact effect:

- counter revision;
- returned resource version;
- changed URL;
- immutable event record;
- ETag/version change.

The body must be able to distinguish 'action requested' from 'effect confirmed'.

## Capability record

Each body calibration produces a machine-readable record conceptually like:

```text
body_id
run_date
model/runtime identity where observable
observation_channels:
  rendered_visual: yes/no/unknown
  accessibility_tree: yes/no/unknown
  dom_source: yes/no/unknown
  structured_metadata: yes/no/unknown
  web_search: yes/no/unknown
actuators:
  navigate: ...
  click: ...
  set_value: ...
  submit_form: ...
  call_webmcp: ...
  repo_read/write: ...
persistence:
  page_local: ...
  session: ...
  external_cursor: ...
verification:
  can_confirm_effect: ...
limitations:
  ...
```

Do not freeze this exact schema yet; it illustrates the categories.

## Calibration outcomes

Use explicit states:

- **verified present** — directly exercised and effect confirmed;
- **verified absent through this adapter** — attempted or tool surface inspected and capability is not exposed;
- **visible but not actionable** — representation exists, actuator absent;
- **documented but unverified** — product/spec says it exists but this body was not empirically tested;
- **unknown** — no evidence.

Never silently upgrade documented support to verified present.

## Current reconnaissance evidence to preserve

From semantic-medium-v0 with the current Opera Browser Connector:

- semantic headings/regions/links/controls are richly visible in accessibility-tree output;
- accessibility descriptions survive;
- closed `<details>` content is not visible while closed;
- JSON-LD and custom `data-*` metadata are not exposed by the AXTree sensor;
- exact `<time datetime>` and link `rel` values were not exposed by that channel;
- form controls advertise conceptual actions in the accessibility representation;
- the connector available to the agent did not expose click/set-value/select/submit actuators;
- direct URL navigation and structural AXTree queries were available.

These observations are scoped to that exact adapter/run and are not universal Browser-agent facts.

## Body classes to calibrate

Initial target classes:

1. human browser;
2. Opera Browser Connector agent;
3. DOM/source-aware browser agent where available;
4. WebMCP-capable ChatGPT browser/site-tool body;
5. repo-native agent;
6. structured HTTP client;
7. optional Cloudflare Browser Rendering observer as an environment-side sensor rather than an autonomous agent.

## Projection equivalence test

When two bodies are meant to inhabit the same underlying resource through different representations, test whether they can recover the same invariant facts.

Example:

```text
human HTML       -> object identity X, source revision R
AXTree           -> object identity X, source revision R
JSON             -> object identity X, source revision R
MCP resource     -> object identity X, source revision R
```

Representation-specific detail may differ.

Failure to recover shared identity/version is evidence that the projections do not yet constitute one shared reality.

## Capability negotiation hypothesis

Long term, the medium may benefit from exposing capabilities in a discoverable way.

But the calibration campaign should not assume a universal capability protocol.

First measure what existing bodies already reveal implicitly or explicitly.

Possible later outputs include:

- human-visible capability status;
- WebMCP/MCP discovery;
- HTTP Allow / link relations;
- repository/tool availability;
- adapter-local introspection.

## Why calibration is separate from MP-1

MP-1 asks whether environmental structure changes behavior.

If body A cannot observe a semantic channel that body B can, that is a body/projection interaction, not evidence that the semantic law itself failed.

Calibration prevents confounding model capability, environment design, and adapter capability.

## Run discipline

- calibrate before measured experiment runs;
- recalibrate after meaningful product/connector updates;
- preserve date/runtime/tool-surface version where observable;
- do not reuse an old calibration as permanent truth;
- if a capability changes mid-campaign, flag affected runs rather than averaging across the change.

## Owner burden

Calibration should be automated wherever possible.

The Owner should not manually click through capability matrices except when a human experiential judgement is itself the thing under test.