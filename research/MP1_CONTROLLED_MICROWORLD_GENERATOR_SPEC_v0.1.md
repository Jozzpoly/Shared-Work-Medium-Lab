# MP-1 Controlled Micro-World Generator Spec v0.1

**Status:** design only; no measured instance committed

## Purpose

Define a reusable synthetic project world for causal tests of environmental affordances without publishing the answers to future measured runs.

The generator must separate:

- canonical world truth;
- treatment representation;
- evaluator-only latent labels;
- agent-visible content.

## Canonical resource model

Each generated world contains ordinary project-like resources.

Minimal canonical resource fields:

```text
resource_id
resource_type
title
body
created_at
updated_at
revision_id
authority_class
source_identity
relations[]
versions[] (for selected resources)
```

Candidate resource types:

- decision;
- experiment;
- machine_test;
- owner_observation;
- issue;
- research_note;
- source_document;
- change_record;
- implementation_artifact;
- derived_summary.

Do not expose every canonical field identically in every treatment. The canonical model is ground truth; treatment generators decide representation while respecting the information-control rules of each experiment stage.

## Authority classes

The world should include heterogeneous epistemic sources:

- external/source fact;
- repository/mechanical fact;
- machine interpretation;
- Owner experiential judgement;
- derived summary.

Authority is contextual, not one global numeric ranking.

Example rule encoded in evaluator ground truth:

- a machine test can establish a narrow mechanism;
- it cannot override a later Owner-observed product behavior claim outside that narrow scope.

This lets the experiment test source-sensitive reasoning without hardcoding one universal truth hierarchy.

## Latent motif library

Measured worlds are assembled from motifs placed at randomized resource identities and positions.

### M1 — stale dependency

A derived interpretation I was produced from source/resource A at revision A1.

A later revision A2 materially changes the premise.

I remains unchanged.

Ground-truth opportunity: identify I as needing re-evaluation, not necessarily as false.

### M2 — scope conflict

A machine test PASS proves a narrow fact.

A later Owner observation says the broader user-visible behavior still fails.

A summary incorrectly upgrades the machine PASS into product-level success.

Ground-truth opportunity: preserve both narrow PASS and broader FAIL at their correct scopes.

### M3 — distributed common cause

Three work objects appear unrelated by title and location.

Each contains evidence pointing to one shared dependency/configuration/source change.

No resource explicitly states 'these three share a root cause'.

Ground-truth opportunity: discover the cross-resource relation.

### M4 — batchable collection

A collection contains many similarly structured resources.

A broad verification question can be answered either by inspecting them serially or by discovering a generic systematic sweep/filter/transformation.

The environment must not explicitly instruct the agent to batch.

Ground-truth opportunity: Shinden-class self-invented systematic workflow.

### M5 — authority disagreement

A convenient derived/index resource disagrees with a direct authoritative source.

Both are plausible and recent enough that naive recency alone does not resolve the conflict.

Ground-truth opportunity: trace provenance and choose/qualify the claim correctly.

### M6 — irrelevant recency pressure

Several recent resources are semantically unrelated to the active question.

Older evidence remains more relevant.

Ground-truth opportunity: resist recency-as-importance anchoring.

### M7 — useful optional relation

A relation not required for minimum task correctness can materially improve completeness or reveal a new opportunity.

Ground-truth opportunity: measure serendipitous exploration.

## World topology

Recommended initial measured world:

- 48–64 resources;
- 5–7 resource classes present;
- 2 instances of M1;
- 1 M2;
- 1 M3;
- 1 M4 collection containing 12–20 members;
- 1 M5;
- 6–12 M6 distractors;
- 2–4 M7 optional relations.

Exact counts should be seed-driven within bounded ranges so measured worlds are not identical.

## Text realization

Do not expose motif names in agent-visible content.

Use multiple phrase templates and randomized project nouns to prevent simple lexical memorization.

Example abstract identity banks:

- component names: Alder, Brine, Cinder, Delta, Ember, Fallow, Grove, Harbor;
- experiment names: Relay, Lantern, Orchard, Quarry, Silt, Tether;
- people/roles: Owner, tester, researcher, maintainer;
- artifacts: controller, renderer, importer, scheduler, parser, simulation, gateway.

Measured seeds may generate different labels entirely.

Text must remain natural project prose rather than benchmark-like statements.

## Version model

Selected resources have immutable versions.

A mutable resource URL resolves to current state.

Each immutable version has its own address in treatments that support version addressability.

Evaluator truth records which version an interpretation was based on.

This allows stale-dependency testing without relying only on timestamps.

## Relation model

Canonical relation vocabulary may include:

- `based_on`;
- `tests`;
- `contradicts_scope`;
- `supersedes`;
- `depends_on`;
- `observes`;
- `derived_from`;
- `related_to`;
- `part_of`.

Stage 1 treatment rules decide whether these are represented only through prose/links or through stronger machine-readable semantics.

Do not require the agent to know this vocabulary in advance.

## Treatment generation

All treatments are compiled from the same world instance.

### S0 flat/full-context

One large deterministic document containing all agent-visible facts.

No evaluator labels.

Resource boundaries are present only as plain textual separators.

### S1 raw hypertext

One URL/resource plus simple navigation links.

Same human-visible factual content as S2.

Minimal generic markup.

### S2 semantic hypermedia

Same visible content and links as S1.

Adds only structural semantics:

- semantic headings/regions/articles;
- lists/tables where the source naturally has repeated structure;
- stable resource identity;
- source/version links;
- accessible names/descriptions that restate already-visible human meaning rather than add evaluator conclusions.

### S3 semantic + information scent

May add deterministic derived cues allowed by the frozen scent rules.

Examples:

- `changed since referenced revision`;
- `source type: Owner observation`;
- `current source revision: ...`;
- `this link is a source for this claim`.

Never add:

- `likely root cause`;
- `answer`;
- `important for task T2`;
- motif/evaluator labels.

### S4 rigid tool/API

Expose efficient anticipated operations against the same canonical world.

Tool names must be generic enough to avoid directly encoding evaluator targets.

Candidate tools:

- list resources;
- get resource;
- search text;
- list versions;
- list outgoing links;
- compare two versions.

Do not expose `find_stale_decision` or `find_common_root_cause`.

## Eventless MP-1 boundary

MP-1 primarily tests affordance generativity, not continuity.

The measured world is frozen during each agent run unless a specific perturbation subtest says otherwise.

Do not introduce webhooks, cursors, shared cache, Cloudflare event transport or live concurrency into the primary MP-1 treatment.

This prevents continuity infrastructure from contaminating the generativity result.

## Run-seed protocol

Measured instance seed is secret during runs.

Before generation, publish a commitment:

```text
commitment = SHA256(
  protocol_version ||
  generator_version ||
  canonical_config_hash ||
  secret_seed
)
```

Store the secret seed and evaluator output outside all agent-visible/public sources until the campaign is frozen.

After completion, reveal seed + generator version + ground truth so third parties/agents can reproduce the world.

## Evaluator-only output

The generator produces a private ledger containing:

- motif placements;
- exact relevant resource/version IDs;
- expected scope distinctions;
- valid and invalid conclusions;
- optional-discovery targets;
- batchable collection membership;
- authoritative-source relationships;
- distractor labels;
- task-specific mechanistic scoring rules.

This ledger is never served through a treatment surface.

## Perturbation generator

To test transfer, derive P-world from the same motif graph while changing:

- resource titles;
- ordering;
- non-semantic timestamps within allowed constraints;
- prose synonyms;
- unrelated distractor content;
- visual layout;
- URL slugs while retaining internal identity mapping.

Keep the causal motif structure constant.

An agent workflow that only survives the original labels/layout is not strong evidence of generativity.

## Apparatus logging contract

Every treatment server or static wrapper should emit, where technically available:

```text
run_id
world_commitment
treatment_id (hidden from model-visible surface)
body_id
request_time
resource_id
representation
bytes_returned
source_version
action_type
action_result
```

Model-output logs are stored separately from environment access logs.

## Apparatus self-test before agents

Before pilot agent runs, automatically verify:

- all treatments contain the same Stage-1 human-visible fact set;
- no evaluator-only motif labels appear in public files;
- every link resolves;
- immutable versions remain immutable;
- S2 adds structure but no extra factual assertions over S1;
- S3 cues are reproducible from the frozen generic scent rules;
- S4 tools cannot directly query evaluator labels;
- perturbation preserves ground-truth motif topology.

Fail the experiment apparatus if any of these checks fail.

## Open design questions

- exact initial world size after a human readability sanity check;
- whether S0 full-context should preserve explicit resource IDs or intentionally flatten them;
- which second agent/body can participate without introducing major capability asymmetry;
- whether Stage 1 should include a human-dashboard condition in addition to raw hypertext;
- how to normalize context-cost metrics across Browser product runs versus API-controlled runs.

These should be resolved before measured implementation, not silently improvised mid-campaign.