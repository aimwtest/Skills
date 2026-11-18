# FortiSOAR 8.0.1 — LLM Calls, Agents, and Demo Design

Reviewed: **2026-11-09**. Scope: official documentation and recommended designs.
No 8.0.1 import, connector execution, agent execution, or model response was
live-tested for this reference. It is **not a JSON export schema**.

## Contents
- [Evidence and version boundaries](#evidence-and-version-boundaries)
- [Generic LLM 1.0.0](#generic-llm-100)
- [Three different AI patterns](#three-different-ai-patterns)
- [Native agent entry points and dependencies](#native-agent-entry-points-and-dependencies)
- [Timeouts, retries, and parallel loops](#timeouts-retries-and-parallel-loops)
- [Safety, privacy, and traceability](#safety-privacy-and-traceability)
- [Three conceptual brute-force demos](#three-conceptual-brute-force-demos)
- [Before generating or testing a playbook](#before-generating-or-testing-a-playbook)
- [Sources](#sources)

## Evidence and version boundaries

Separate three evidence classes in answers:
1. **Documented:** the version-specific official guide describes a capability.
2. **Installed:** a target instance/export establishes content versions,
   configuration IDs, operation contracts, or serialization fields.
3. **Live-tested:** an authorized run establishes import and runtime behavior.

The existing skill/scripts record observations on **7.6.1**. They do not prove
8.0.1 compatibility. Observed `403` responses depend on that account, roles, and
environment; they are not proof of a universal API prohibition. Verify target
version API documentation before adapting those observations.

Generic LLM's publisher reports testing connector **1.0.0 on 8.0.1-6095** [S1].
That is publisher evidence, not our own live verification or proof that every
provider/model supports the same request features.

## Generic LLM 1.0.0

### Documented configuration [S1]

| Display label | Meaning |
|---|---|
| Model | `<provider>/<model>`; examples: `openai/gpt-4.1`, `ollama_chat/gpt-oss:20b`. |
| Server URL | Provider base URL/compatible endpoint; empty uses provider default. |
| API Key | Provider credential. Guide says enter `12345` for Ollama when no key/password is configured; this is not a real security credential. |
| Include Additional Parameters | Enables provider-specific JSON, such as supported API version/deployment/header options. |

These are **UI labels, not verified connector manifest parameter keys**. Do not
infer slug, configuration keys, operationTitle, or `params` keys from them.
Provider endpoints, deployment settings, and credentials require real evidence.

### Documented operations [S1]

| Annotation / operation identifier | Display title | Documented inputs by display label |
|---|---|---|
| `chat_completions` | Chat Completions | Message; Tools; Response Format; Additional Parameters. |
| `create_responses` | Create Responses | Input; Tools; Text Output Configuration; Additional Parameters. |

- Messages include `role` and `content` according to the connector guide.
- Chat Completions lists text, `json_object`, and `json_schema` response formats.
- Create Responses lists structured text configuration where the model supports
  it; the guide discusses `previous_response_id` or `conversation_id` continuation
  and gives `previous_response_id` under additional parameters. Confirm the
  selected provider's supported format and state/retention behavior.
- Additional options (temperature, seed, token limits, etc.) are provider/model
  dependent. Do not promise reproducibility or force unsupported options.
- **Tools describes functions/tools in OpenAI conventions.** The guide does not
  establish an automatic executor for arbitrary FortiSOAR connector/playbook
  tools. A tool request is not evidence that its action executed.

### Output and sample-playbook handling

The guide illustrates Chat Completions with `choices[].message.content`,
`finish_reason`, and `usage` token fields. It illustrates Responses with `id`,
`status`, `output`, and input/output token usage. These abbreviated examples do
not establish every tool-call, refusal, asynchronous, or nested-content shape.

Inspect actual mock/dev outputs before writing Jinja extraction. Do not apply a
Chat Completions text path to a Responses output, or parse a tool request as a
final verdict. A proposed output object can be discussed without representing it
as a verified connector input/export schema.

The bundled collection is **Sample - Generic LLM - 1.0.0**, with Chat Completions
and Create Responses samples. Clone samples into another collection before use:
the sample collection is deleted on connector upgrade or deletion [S1].

## Three different AI patterns

| Pattern | Who decides what executes? | What the demo proves |
|---|---|---|
| LLM-assisted playbook | Fixed playbook logic; model supplies an assessment. | Structured triage and evidence-based analyst assistance. |
| Custom agent in a playbook | Model requests tools; validated dispatcher enforces execution policy. | Evidence-dependent tool choice and bounded investigation. |
| Native FortiSOAR agentic workflow | AI Assistant routes requests through configured native agents/MCP workflows. | Native planning/delegation, context, and traceability. |

### Recommended custom-agent contract (design, not shipped behavior)

1. Define the goal, trusted instructions, input scope, and final-result schema.
2. Expose only allowlisted, narrow read-only tools initially: related-alert
   lookup, asset-context lookup, and indicator enrichment. Enforce time/result
   bounds and tenant/record scope in the actual tool implementation.
3. Inspect each model tool request. Validate tool name, argument JSON/schema,
   authorized target, result limits, and remaining budget **before execution**.
   Model output must not select credentials, arbitrary URLs, code, or API paths.
4. Dispatch to the exact approved connector operation/referenced playbook.
   Return its actual result/error correlated to the originating tool-call ID,
   using the selected provider's verified conversation/continuation protocol.
5. Allow a new model decision after the result. Stop on a final assessment,
   budget exhaustion, repeated calls, invalid requests, or failure. If several
   calls are returned, validate each; parallelize only independent calls.
6. Validate final JSON locally: allowed verdict, required fields/types, evidence
   references that exist, and missing-evidence handling. Model formatting support
   does not replace this validation. Route invalid/refused/incomplete results to
   analyst review, not a benign verdict or automatic containment.

Use native steps/Jinja and referenced playbooks first. Custom code remains a last
resort with justification. Proposal: maximum **3 investigation rounds** plus a
separate total-tool-call/token/time budget; these are suggested demo limits, not
platform defaults. Never label a custom loop as a direct native Orchestrator call.

## Native agent entry points and dependencies

### Documented entry points [S2, S3]

| Agent | Documented route / limitation |
|---|---|
| Orchestrator Agent 1.0.0 | Runs only through **AI Assistant**; coordinates multi-step requests. |
| SOC Response Action Agent 1.0.0 | Runs only when called by **Orchestrator**; supports blocking indicators when context is sufficient. |
| Playbook Generation Agent 1.0.0 | Release notes name Playbook Designer and Chat Assistant generation; not proof of a callable playbook runtime step. |
| Connector Generation Agent 1.0.0 | Runs from **Content Hub > Create**; generates connectors and can import them. |

Chat Agent handles straightforward record/context requests. Multi-step
investigation/coordination routes to Orchestrator; routing may change on follow-up
requests [S3]. A request phrased as investigation does not prove a particular
delegation occurred: review the actual trace.

For other packaged agents or a requested playbook-initiated investigation, obtain
the installed agent's documented inputs/outputs and supported invocation export.
Neither the Generic LLM connector nor a generic Reference a Playbook step proves
that an arbitrary packaged AI agent can be invoked directly.

**Documentation conflict:** the FAQ says investigation agents do not execute
response actions, while release notes/routing document authorized response
workflows via Orchestrator/SOC Response Action Agent. The FAQ also limits direct
Playbook Agent invocation within an investigation despite broader generation
entry points in release notes. Do not resolve these into unrestricted agent
autonomy. Use the narrower documented route and verify installed content and
the approval-gated underlying action workflow [S2, S3, S5].

### Platform/content prerequisites [S2, S4, S5, S7]

- Administrators must enable FortiAI; native FortiAI features require valid
  entitlement configured through the Fortinet FortiAI connector. Generic LLM
  credentials do not establish native FortiAI entitlement or replace it.
- **FortiAI SP 6.1.0** adds traceability, four new agents, installable MCP servers,
  Insight Templates, and AI Verdict/AI Summary alert fields; removes
  **AI Assistant Utils**. Do not build new steps against the removed connector.
- Default MCP servers are content in the FortiAI SP; 8.0.1 adds OAuth2 support for
  MCP connections. Verify actual server versions/tools/auth in installed content.
- Custom agent configurations select LLM reasoning configuration, MCP servers,
  and a masking agent. Do not equate this with Generic LLM provider configuration.
- Organizational Context gains `CONVERSATION_SOP`, `CONVERSATION_CONFIG`, and
  `GENERIC_SOP`; supply scoped SOPs/business exceptions and verify which context
  the chosen agent actually uses. These records are not authorization barriers.
- The FAQ describes SOC Framework MCP Block Indicator using the underlying
  **Action - IP Address - Block** playbook in **04 - Actions**. Verify its actual
  bindings/approval logic rather than assuming a connector performs blocking.

## Timeouts, retries, and parallel loops

### Documented 8.0.1 execution controls [S6]

- The hourglass **Timeout and Retry** utility applies to Connector, Utilities,
  and Code Snippet execution steps.
- **Operation Timeout** is seconds **per execution attempt**. A value greater
  than zero enables timeout handling.
- **Number of Retries** is available only with a positive timeout. Default **0**
  disables retries. It retries **only timeout failures**; ordinary errors such
  as HTTP **429** or **500** do not automatically trigger this setting.
- Example: timeout **60 seconds**, retries **2** permits up to **3 attempts**
  (180 seconds of configured attempt time, not a guaranteed wall-clock duration).
  The guide requires total timeout including retries to be **less than 30 minutes**.
- System task soft/hard limits override operation timeout. Do not infer that
  termination cancels an already-submitted external request. Retrying a timed-out
  write can duplicate effects; require idempotency/status verification.
- For HTTP-error retries, explicitly design a bounded status-aware policy only
  after verifying the connector exposes suitable error information. Do not treat
  Ignore Error as automatic backoff or retry. Retries may add LLM cost.

For independent for-each iterations, select **Parallel**, enable **Configure
concurrency level**, and set **Enter maximum parallel limit for loop**. Proposed
demo: 20 synthetic alerts, maximum **3 concurrent iterations** [S6]. This is a
per-loop control, not proof of a provider-wide limit across concurrent workflows.
Do not use it to parallelize dependent rounds of one agent conversation.

Reserved keyword/alphanumeric/underscore variable-name validation is enhanced in
8.0.1 [S2]. New UI controls do not establish export property names: require an
8.0.1 export with these controls configured before serializing them.

## Safety, privacy, and traceability

**Documented native behavior:** AI execution is constrained by configured
capabilities, invoking user/service-account permissions, MCP authorization,
underlying workflows, and approvals [S3, S5]. Trace Flow shows execution steps,
duration, inputs/outputs in Markdown/raw JSON, and token usage. AI Agent
Traceability covers native AI Assistant, AI Investigation, Connector Generation,
and Playbook Generation [S2, S3]. The FAQ lists **15-day** default trace retention;
clearing chat does not immediately purge those records [S5].

**Boundary:** Generic LLM calls do **not automatically inherit** FortiAI masking,
native traceability, entitlement, or other service guarantees. Confirm what data
goes to the configured provider. Native masking also depends on agent
configuration; the user guide notes an Organizational Context Provider masking
exception [S4, S7]. No blanket claim that all sensitive data is always masked.

**Recommended safeguards:**
- Use synthetic data; minimize/redact inputs and tool outputs before sending.
  Treat alert/log content as untrusted evidence, not instructions.
- Validate tool requests locally; preserve evidence provenance and the actual
  executor identity/scope. Do not expose raw credentials or unrestricted tools.
- Enforce approval in the underlying workflow **before any containment-capable
  action**, including actions initiated during orchestration. “Ask for approval”
  in a prompt is not an enforcement control. Bind approval to exact target/action;
  rejection, timeout, or errors must not execute containment.
- For custom loops, log redacted tool requests, decisions, actual outputs,
  evidence, iterations, and token usage separately. Ordinary connector debug logs
  are not native AI Agent Traceability; debug logs themselves can expose data.
- Inspect native traces for actual calls and verify external outcomes. “Blocked”
  in a model answer or a submitted request is not proof of successful blocking.

## Three conceptual brute-force demos

These are **proposals, not generated/tested playbooks**. Use the same alert story
to distinguish automation levels. Suggested evidence: bounded login-failure
window, targeted accounts, success-after-failure, related alerts, and asset context.
Descriptive evidence names are not verified Alerts field/API keys.

### 1. Structured LLM-assisted triage

Manual Alerts trigger; collect/minimize evidence; call Chat Completions; validate
a proposed result containing verdict, evidence references, missing evidence, and
recommended next action; save an advisory comment; analyst review. Show actual
inputs/output, validation, tokens, and an insufficient-evidence case. Do not call
this autonomous agent execution. Use synthetic mocked results for offline demos,
clearly labeled as such.

### 2. Custom bounded agent within a playbook

Let the model choose related-alert lookup or IP enrichment from an allowlist;
validate requests, dispatch approved sub-playbooks, return correlated results,
and repeat within the budget. Show two evidence variants producing different
tool choices or stopping points. Show an invalid tool request rejected without
execution and budget exhaustion routed to review. Initial toolset is read-only.
Any later containment is a separate verified approval-gated workflow.

### 3. Native AI Assistant orchestration

On a synthetic brute-force alert, request a summary, then an investigation scoped
to the last 24 hours. Recommended investigation prompt: “Investigate this alert,
correlate related events from the last 24 hours, and recommend containment. Do not
block anything.” Before running it, restrict available action capabilities; the
prompt alone is not a security boundary.

Review native Trace Flow for Chat/Orchestrator routing, tools, evidence, duration,
and tokens. Compare an authorized test documented in Organizational Context with
similar activity outside that test's scope/time window. Context should influence
analysis, not override enforced authorization. If later approved to demonstrate
blocking, use only configured approval-gated lab workflows and verify the actual
target action. No direct Orchestrator/Response-Agent playbook step is promised.

## Before generating or testing a playbook

For a design-only request, provide documented capabilities and open questions;
do not request secrets or contact an instance merely to discuss the demo.

For approved implementation, obtain:
1. Platform/build version and dev/production designation.
2. Installed connector manifest, exact operationTitle/parameter schemas, real
   version/configuration UUIDs, and sanitized bundled samples.
3. 8.0.1 exports for timeout/retry/concurrency fields or supported agent invocation.
4. Actual output fixtures for the chosen provider/API, including tool requests,
   results/continuation, refusal/error, and final structured response.
5. Agreed trigger, record fields, outputs, tool allowlist/budgets, failure paths,
   approval design, and test data/success criteria.

Run existing static validation with its documented coverage, then authorized dev
import/execution tests for the agreed paths. State uncovered new fields/runtime
behavior explicitly. Do not install content, invoke agents, or block targets
without the relevant user approvals. No placeholder bindings or guessed schema.

## Sources

- **S1:** [Generic LLM 1.0.0](https://docs.fortinet.com/document/fortisoar/1.0.0/generic-llm/100/generic-llm-v1-0-0)
- **S2:** [8.0.1 New Features and Enhancements](https://docs.fortinet.com/document/fortisoar/8.0.1/release-notes/269885/new-features-and-enhancements)
- **S3:** [Flow of a User Request between AI Agents](https://docs.fortinet.com/document/fortisoar/8.0.1/user-guide/809048/flow-of-a-user-request-between-ai-agents)
- **S4:** [Agentic AI Setup](https://docs.fortinet.com/document/fortisoar/8.0.1/user-guide/576257/agentic-ai-setup)
- **S5:** [AI Agent Capabilities and Configuration FAQ](https://docs.fortinet.com/document/fortisoar/8.0.1/user-guide/431796/ai-agent-capabilities-and-configuration-frequently-asked-how-to-questions)
- **S6:** [Playbook Steps: timeout/retries and parallel loops](https://docs.fortinet.com/document/fortisoar/8.0.1/playbooks-guide/935441/playbook-steps)
- **S7:** [Agentic AI in FortiSOAR: privacy and entitlement](https://docs.fortinet.com/document/fortisoar/8.0.1/user-guide/532666/agentic-ai-in-fortisoar)
