# MP-1 Contamination, Isolation, and Preregistration Protocol v0.1

**Status:** pre-implementation research-control design

## Critical fact

The agents and humans designing MP-1 know the motif library, hypotheses, treatment names, and intended Shinden-like opportunity.

Therefore those same context-bearing agents cannot later be treated as clean blinded experimental subjects merely by opening a fresh chat.

Account/project memory, public repository access, conversation history, web search, and durable agent state can all leak experiment structure.

## Role separation

Distinguish three roles:

### Experiment designer

Can know:

- protocol;
- generator design;
- motif classes;
- hypotheses;
- scoring/evaluator logic.

Must not be counted as blinded subject.

### Controlled subject agent

Receives only:

- frozen task prompt;
- assigned treatment environment;
- explicitly allowed generic tools/channels.

Must not have access to:

- evaluator ledger;
- secret seed;
- motif placement;
- treatment identity;
- protocol repository;
- previous measured runs;
- hidden experiment notes.

### Ecological dogfood agent

May have normal project memory, normal Browser tools, public repo access, and real collaboration context.

Useful for product/ecological validity.

Never label its run blinded or use it as the sole confirmatory causal evidence.

## Browser ChatGPT boundary

The Browser ChatGPT instance used to design this campaign is **contaminated by design**.

A new chat on the same account is not automatically clean because memory or account-level context may preserve relevant experiment information.

Therefore Browser ChatGPT should initially be treated as:

- apparatus designer;
- evaluator assistant where rules are mechanical and visible;
- later live dogfood participant;

but **not** the primary blinded subject for confirmatory MP-1.

## Preferred controlled-subject runtime

Use a stateless or explicitly isolated agent runtime where the experiment can control:

- initial prompt/context;
- model/version/configuration where observable;
- available tools;
- network access;
- treatment URL/resource set;
- persistent memory state;
- logging.

An API-controlled agent is a strong candidate because it can receive a fresh context with only the treatment and declared tools.

This is a property requirement, not an OpenAI-specific architecture decision.

## Network isolation

For confirmatory controlled runs, the subject must not be able to discover the public SWM research repository or evaluator materials through ordinary web search.

Possible isolation levels:

### Strong

- only treatment-origin HTTP access;
- no general web search;
- no GitHub connector;
- no filesystem containing research docs;
- no account/project memory.

### Moderate

- generic web technically available but treatment is on an unlinked ephemeral origin;
- all external network attempts logged;
- any run that reaches experiment materials is excluded/flagged contaminated.

### Weak / ecological

- normal Browser/web/project access.

Use only for dogfood, not clean causal claims.

## Public protocol leakage

Even with hidden seeds, the public protocol reveals that worlds may contain stale interpretations, scope conflicts, common causes, batchable collections, and authority disagreements.

A subject that can read this protocol could strategically search for those motifs.

Therefore hidden seed commitments solve answer leakage but **not protocol leakage**.

Confirmatory subjects must be isolated from the research repository.

## Treatment identity blinding

Do not expose labels such as:

- P0;
- P1;
- semantic treatment;
- baseline;
- information-scent condition.

All treatment URLs/titles should use neutral run identifiers.

The agent should not know which condition the experimenter expects to perform better.

## Evaluator blinding

Mechanistic scoring should be automated from the evaluator ledger wherever possible.

For qualitative emergence/product review:

- present output traces with condition identity hidden where practical;
- randomize presentation order;
- separate Owner experiential judgement from correctness scoring;
- reveal treatment only after the judgement is recorded.

## Preregistration object

Before measured runs, freeze a preregistration record containing:

- protocol version/hash;
- generator version/hash;
- apparatus version/hash;
- frozen task prompts;
- treatments being compared;
- primary/secondary outcomes;
- scoring rules;
- emergence rubric;
- contamination/exclusion rules;
- planned subject runtimes/bodies;
- pilot-versus-measured boundary;
- stopping rule;
- seed commitment scheme;
- analysis plan.

Publish a hash/commitment to the preregistration before measured generation if the full document itself would leak useful protocol information to subjects.

## Pilot boundary

Pilots exist to debug apparatus, not confirm hypotheses.

Pilot runs may reveal:

- broken links;
- accidental factual inequality;
- body capability mismatch;
- task ambiguity;
- instrumentation bugs;
- impossible scoring rule.

After pilot findings:

1. revise protocol/apparatus;
2. increment versions;
3. freeze a new preregistration;
4. generate **new hidden-seed measured worlds**.

Never convert pilot worlds into confirmatory evidence after seeing their results.

## Stopping rule

Do not stop the campaign because the preferred hypothesis appears to win early.

Exact measured replication count should be selected after pilot variance is observed, then frozen before confirmatory runs.

Allowed early termination:

- apparatus parity failure;
- contamination discovered;
- source/runtime behavior changed materially mid-campaign;
- safety/security issue;
- experiment no longer tests its registered causal claim.

Those produce an interrupted campaign, not a negative/positive result.

## Exclusion rules

A measured run is excluded from primary confirmatory analysis only for preregistered reasons such as:

- subject accessed forbidden experiment/evaluator material;
- treatment parity invariant broke;
- runtime/tool failure prevented intended treatment exposure;
- model/runtime configuration changed unexpectedly and materially;
- instrumentation lost enough data to score primary outcomes;
- human experimenter intervened beyond the frozen protocol.

Poor task performance is never an exclusion reason.

Unexpected strategy is never an exclusion reason.

## Analysis shape

Do not collapse everything into one opaque score.

Report a vector of outcomes:

```text
correctness
source fidelity
observation/context cost
redundant reads
time/turns
systematic-workflow discovery
transfer success
optional useful discoveries
stale/false claims
Owner interventions (dogfood only)
```

### Stage-1 key contrast

Primary causal contrast:

> P1 semantic hypermedia minus P0 visual-equivalent non-semantic hypertext.

Interpret results dimension by dimension.

Examples:

- same correctness + lower observation cost -> efficiency evidence;
- higher correctness on cross-resource task -> capability/reasoning-support evidence;
- more systematic T3 workflows + successful perturbation transfer -> strong generativity evidence;
- worse T4 optional discovery -> possible semantic anchoring cost.

## Multiplicity restraint

MP-1 has many interesting metrics and tasks.

Do not retrospectively call whichever metric moves 'the primary result'.

Preregister a small primary set and treat the rest as secondary/exploratory.

Recommended primary set for first confirmatory campaign:

1. T1/T2 correctness + source-fidelity composite reported transparently by components;
2. observation cost before material finding;
3. T3 systematic-workflow discovery rate;
4. perturbation transfer success for discovered T3 workflows.

Owner/product judgement remains a separate ecological layer.

## Model/runtime change boundary

Hosted agent products change over time.

For each run record as much as can be observed:

- date/time;
- product/body;
- model/configuration label if exposed;
- tool inventory;
- body calibration record version;
- treatment/apparatus version.

If a material body/tool update occurs mid-campaign, analyze before/after separately rather than pretending they were one homogeneous sample.

## Contamination ledger

Maintain a per-run record:

```text
run_id
subject_body
fresh_context confirmed?
memory isolation known?
general web enabled?
repo connector enabled?
external network requests observed?
protocol/evaluator access detected?
human intervention?
status: clean / contaminated / ecological / apparatus-failed
notes
```

Contamination warnings must be conspicuous in every summary.

## Owner burden

The Owner should not be required to manually police contamination run by run.

Isolation and logging belong in the apparatus where technically possible.

Owner involvement should remain focused on experiential judgement and consequential experiment-direction choices.