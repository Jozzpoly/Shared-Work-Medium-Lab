# Web-Agent Experiment Harness Donor Audit v0.1

**Status:** apparatus donor research; no adoption decision

## Why this audit exists

MP-1 requires a controlled browser-agent environment, fresh/isolated subject contexts, explicit observation/action channels, deterministic resets, run logging, and reproducible scoring.

Building all of that from scratch would add large non-research engineering cost and create avoidable bugs.

Existing web-agent benchmark infrastructure should therefore be treated as donor material.

## BrowserGym

BrowserGym is a gym-like Chromium environment for web agent research.

Relevant properties:

- custom tasks can be created by subclassing `AbstractBrowserTask`;
- task setup/reset and validation are explicit;
- observation space can expose screenshot, DOM object, accessibility-tree object, page URL/history, focused element, last action/error and elapsed time;
- action spaces include browser primitives such as click, fill, select, press, hover and coordinate actions;
- the environment is designed to host multiple web benchmarks under one interface.

### Why it fits MP-1

BrowserGym could become the **controlled subject-body harness** while our generated P0/P1 treatment world remains independent.

This would let MP-1 test:

- AXTree-visible semantic differences;
- DOM-visible semantic differences;
- identical action primitives across treatments;
- screenshot parity;
- deterministic task reset;
- fresh browser contexts;
- action/observation logging.

### Important boundary

BrowserGym is an experimental harness, not the SWM runtime or medium.

Adopting it for MP-1 should create **zero architectural dependency** on BrowserGym for the eventual project.

## WebArena

WebArena demonstrated a self-hosted, resettable, realistic web environment rather than relying on unstable live websites.

Important donor lessons:

- self-hosted worlds improve reproducibility;
- web tasks should have explicit functional validation;
- environment state must be reset between evaluations;
- accessibility-tree observations are already a common browser-agent representation.

MP-1's controlled micro-world is intentionally smaller and more causal than WebArena, but the same reproducibility principle applies.

## WorkArena / WorkArena++

WorkArena generates large numbers of knowledge-work task instances from reusable task templates, while WorkArena++ composes atomic tasks into larger reasoning/planning workflows.

Donor lesson:

> separate reusable world/task generators from individual instances rather than hand-authoring a tiny fixed benchmark.

This aligns with MP-1's hidden-seed generated worlds and perturbation testing.

## WebArena-Verified

WebArena-Verified is especially relevant to the scoring apparatus.

It moved away from fragile substring matching and LLM-as-judge evaluation toward:

- audited tasks/reference answers/evaluators;
- deterministic/type-aware response checks;
- network-event validation;
- captured network traces that can be replayed/evaluated offline.

### Why this matters

MP-1 independently arrived at a similar principle:

> score what the agent actually did and what state it reached, using deterministic traces whenever possible.

A HAR/network-trace layer may therefore be a better generic behavioral evidence source than inventing a custom log for every browser action.

Possible MP-1 composition:

```text
hidden-seed world generator
        ↓
P0/P1 static treatment server
        ↓
BrowserGym controlled browser
        ↓
subject agent
        ↓
BrowserGym action/observation trace
+ HAR/network trace
        ↓
deterministic MP-1 evaluator
```

## AgentLab

AgentLab sits above BrowserGym as an experiment framework for running/evaluating web agents across benchmarks.

Potential donor value:

- experiment execution;
- parallelization;
- unified result collection;
- comparing multiple agent configurations.

Do not adopt until we inspect whether its experiment abstractions help MP-1 without forcing benchmark assumptions that obscure our custom environment treatment.

## What MP-1 should probably build itself

Even if BrowserGym/AgentLab are used, MP-1 still needs custom project-specific research components:

- hidden-seed micro-world generator;
- P0/P1 treatment compiler;
- parity verifier;
- motif/evaluator ground-truth ledger;
- contamination/commitment logic;
- MP-1 systematic-workflow scorer;
- treatment-independent provenance/source-fidelity scorer.

Those are the actual research apparatus.

## What MP-1 should avoid rebuilding

Unless donor inspection finds a blocking mismatch, avoid custom-building:

- Chromium lifecycle management;
- low-level browser click/fill/select implementation;
- screenshot capture;
- AXTree extraction;
- DOM observation plumbing;
- basic task reset/step loop;
- generic browser video/network trace infrastructure;
- parallel experiment runner.

## New controlled-body candidate

A BrowserGym-based subject runtime currently looks stronger for **confirmatory MP-1** than the user's normal Browser ChatGPT product context because:

- it can run fresh isolated browser contexts;
- observation/action channels are explicit;
- network access can be constrained by the apparatus;
- it is easier to record complete behavioral traces;
- task reset is controllable;
- it is independent from the user's account-level ChatGPT project memory.

The LLM driving BrowserGym can still be changed independently.

This would let Browser ChatGPT remain what it is best at here:

> design/research + later ecological dogfood, rather than pretending to be an uncontaminated benchmark subject.

## Apparatus decision gate

Before implementation, perform a small donor spike to answer:

- can BrowserGym expose enough AXTree difference between our P0/P1 pages?;
- can we constrain external navigation/network for clean controlled subjects?;
- can HAR/network traces be captured or integrated cleanly?;
- can task validation remain fully custom/deterministic?;
- can subject model calls be controlled independently of BrowserGym?;
- can we instrument total observation payload delivered to the subject?;
- can the harness run our pixel-equivalent treatments without adding material UI differences?

If yes, reuse.

If no, identify the smallest missing layer and extend/replace only that layer.

## Current judgement

Strong donor candidate, not selected dependency.

The existence of BrowserGym/WebArena-Verified materially lowers the expected cost of building a scientifically credible MP-1 apparatus.

That makes it more plausible to spend effort on the actual research variable — environmental affordances — instead of browser automation plumbing.