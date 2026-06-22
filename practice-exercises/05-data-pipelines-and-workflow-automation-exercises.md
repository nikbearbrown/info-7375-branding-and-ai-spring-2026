# Practice Exercises: Data Pipelines and Workflow Automation

*Chapter 5 of Branding and AI (INFO 7375)*

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before
> completing earlier ones — the tiers scaffold your understanding. Attempt
> every exercise before checking the answer key. For open-ended questions,
> write at least 2–3 sentences before reading the model answer. The act of
> attempting is where the learning happens.

---

## Learning Objectives Covered

1. **Define** a data pipeline as a chain of contracts and explain why each stage of the pipeline constitutes a contract with the downstream stage.
2. **Classify** pipeline architectures into the four categories — ETL, stream-processing, workflow-automation, and inference — and explain when each is appropriate.
3. **Analyze** the Apollo/Reddit API case as a pipeline fragility failure and explain the mechanism by which external dependency changes produce brand damage, not just technical failure.
4. **Apply** the contract documentation habit to a real pipeline, writing at least one upstream contract for each pipeline stage.
5. **Design** a degraded mode hierarchy for a pipeline that has multiple upstream dependencies, specifying at least four levels of graceful degradation.
6. **Build** a workflow automation using n8n nodes and connections to implement a multi-step pipeline with at least one conditional branch.

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A student has built a pipeline that: (1) fetches product reviews from the Amazon Product Advertising API, (2) classifies each review using a GPT-4o-mini API call, (3) stores classified reviews in a Google Sheet, and (4) sends a daily summary email via SendGrid.

Identify every upstream contract in this pipeline. For each contract, name the contractual commitment, a likely change that would break it, and a degraded mode that would allow the pipeline to continue operating with reduced functionality when the contract is broken.

**Approach:**
Step 1: List every external dependency. The pipeline has four: Amazon Product Advertising API, GPT-4o-mini API, Google Sheets API, SendGrid.

Step 2: For each, identify what the pipeline is relying on (the contract).
- Amazon API: reliable access to product reviews at the configured query rate, in the current data schema
- GPT-4o-mini: reliable API access, consistent output format, stable pricing
- Google Sheets: write access, stable row/column structure, API availability
- SendGrid: delivery reliability, consistent sender authentication

Step 3: For each, name a likely change that would break the contract.
- Amazon: rate limit reduction, schema change in review format, API deprecation (Amazon has deprecated API versions before)
- GPT-4o-mini: model deprecation (GPT-4o-mini has already been updated; older versions are retired), output format change
- Google Sheets: API quota reduction, authentication change
- SendGrid: account suspension for spam-score violations, pricing change

Step 4: For each, design a degraded mode.
- Amazon contract broken: switch to a public RSS feed of Amazon reviews (lower fidelity, no direct API rate) and flag outputs as "lower confidence — limited source"
- GPT-4o-mini contract broken: fall back to GPT-3.5-turbo or a local classifier; flag outputs as "backup model — verify"
- Google Sheets contract broken: write to local CSV file; continue pipeline; notify operator via email
- SendGrid contract broken: write summary to a configured webhook URL; flag as "email delivery paused"

**What to notice:** The contract documentation exercise forces you to articulate what you are relying on rather than what you are building. Engineers focus on the happy path; contract documentation focuses on the dependency assumption that will eventually be violated.

---

## Tier 1 — Warm-Up (Exercises 1–8)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them. These should feel straightforward after a careful reading.*

---

**Exercise 1** *(Contrastive Classification)*

For each of the following pipeline descriptions, classify it as ETL, stream-processing, workflow-automation, or inference. Justify each classification in one sentence.

1. A system that reads customer records from a legacy database at midnight, transforms them into a standard schema, and loads them into a data warehouse.
2. A pipeline that processes every new tweet mentioning a brand within 500 milliseconds of posting and updates a live sentiment dashboard.
3. An n8n workflow that triggers when a new form submission arrives, enriches the lead data via a third-party API, and creates a CRM record.
4. A service that receives a document URL, runs it through a language model to generate a summary, and returns the summary via API.
5. A system that collects server log data every hour, joins it with user session data, and exports a report for the analytics team.

*(Tests: Four pipeline categories — ETL, stream, workflow automation, inference)*

---

**Exercise 2**

True / False, with explanation: The chapter argues that a pipeline stage's "contract" is primarily a legal agreement between the pipeline operator and the data source.

Write one sentence explaining why the statement is true or false, using the chapter's definition of pipeline as "a chain of contracts."

*(Tests: Pipeline as chain of contracts — definition)*

---

**Exercise 3**

In your own words, explain the Apollo/Reddit API case as described in the chapter. Your explanation must name:
1. The specific numbers involved (API call volume, implied cost, timeline)
2. The mechanism by which a technical dependency change became brand damage
3. Why this case illustrates pipeline fragility rather than a business dispute

*(Tests: Apollo/Reddit case — pipeline fragility mechanism)*

---

**Exercise 4**

The chapter describes four levels in a degraded mode hierarchy. List them in order from the most functional to the least functional, and give a one-sentence description of each. Use the chapter's terminology.

*(Tests: Degraded mode hierarchy — four levels)*

---

**Exercise 5**

The chapter describes the "independence property" of n8n pipelines. In your own words, explain what the independence property means and why it matters for pipeline resilience.

*(Tests: Independence property — n8n pipeline architecture)*

---

**Exercise 6** *(Contrastive Classification)*

Classify each of the following pipeline failure scenarios as: (a) contract violation, (b) data schema change, (c) rate limit change, (d) authentication failure, or (e) API deprecation. For each, name the degraded mode from the chapter's hierarchy that would be most appropriate.

1. The Twitter/X API raises its price from $100/month to $42,000/month overnight, making the pipeline economically unviable.
2. A weather data API changes the field name `temp_celsius` to `temperature_c` in its response JSON, causing the pipeline to fail on every record.
3. A pipeline's OAuth token expires and the API begins returning 401 errors on all requests.
4. The Heroku free tier is deprecated; the pipeline's deployment environment disappears.
5. A financial data provider's API begins returning an additional field `confidence_score` that the pipeline's schema validation rejects as unexpected.

*(Tests: Contract violation categories; degraded mode hierarchy)*

---

**Exercise 7**

The chapter distinguishes between contract monitoring and contract documentation. In your own words, explain the difference between these two activities and explain why contract documentation must precede contract monitoring.

*(Tests: Contract documentation vs. contract monitoring — sequence and relationship)*

---

**Exercise 8**

n8n uses three core concepts: nodes, connections, and workflows. Define each in one sentence and explain, in a fourth sentence, how the three concepts together enable workflow automation.

*(Tests: n8n nodes, connections, workflows — definitions)*

---

## Tier 2 — Application (Exercises 9–16)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations. This is where most of the learning happens. Expect these to take more time than Tier 1.*

---

**Exercise 9** *(Scenario-Based Application — Contract Documentation)*

You are building the following pipeline:
- Source: Google News RSS feed (public, no authentication)
- Processing Step 1: GPT-4o-mini classifies each article as relevant or not relevant to a configured topic
- Processing Step 2: A second GPT-4o-mini call generates a one-sentence summary of relevant articles
- Storage: Airtable database (authenticated via API key)
- Delivery: n8n HTTP Request node sends a Slack message with the daily summary

For each stage, write a formal contract documentation entry with:
1. The upstream dependency name and URL/endpoint
2. The specific commitment the pipeline relies on (what the dependency promises)
3. The most likely change that would break this contract (based on the chapter's discussion of real API changes)
4. The degraded mode the pipeline should enter when the contract is broken

*(Tests: Contract documentation habit applied to a real pipeline)*

---

**Exercise 10** *(Error Analysis)*

> The following pipeline description was submitted by a student. It contains a significant architectural error in how the pipeline handles failures.

```
My competitor monitoring pipeline works as follows:

1. An n8n schedule trigger fires every morning at 7 a.m.
2. n8n fetches headlines from 5 RSS feeds (TechCrunch, VentureBeat,
   Wired, Hacker News, Product Hunt).
3. For each headline, n8n calls GPT-4o-mini to classify relevance.
4. Relevant headlines are stored in Google Sheets.
5. If any step fails, n8n sends me an email alert.

I chose this architecture because the email alert means I will always
know when something goes wrong, so I can fix it manually. Since I
check email every morning, the maximum downtime is 24 hours.
```

1. Identify the architectural error. What concept from the chapter does this design violate?
2. Explain what happens to the pipeline's users (the people who read the daily summary) during a 24-hour downtime event.
3. Redesign the failure-handling step using the chapter's degraded mode hierarchy. What specific degraded mode would prevent a total pipeline blackout?

*(Tests: Degraded mode hierarchy; pipeline as chain of contracts)*

---

**Exercise 11** *(Self-Explanation)*

The chapter argues that the Apollo/Reddit API case is "a lesson in pipeline architecture, not just in API pricing." Explain in your own words — without quoting the chapter — what architectural lesson the case illustrates and why it is a lesson about how pipelines should be built, not just about business strategy. Your explanation must:
- Name the structural vulnerability the case exposed
- Explain why the vulnerability was invisible until the change happened
- Connect the architectural vulnerability to the brand damage it produced

*(Tests: Apollo/Reddit pipeline fragility; contract documentation habit — self-explanation)*

---

**Exercise 12** *(Cumulative — Prior Chapter Concept)*

Chapter 4 introduced the Build-Measure-Learn loop. The loop requires measuring user behavior — which requires the pipeline that delivers the product to users to be running reliably. Chapter 5 argues that degraded modes allow the pipeline to continue operating at reduced functionality rather than failing completely.

Explain the relationship between these two concepts:
1. What specifically fails in the Build-Measure-Learn loop when the pipeline enters total failure (no degraded mode) vs. graceful degradation?
2. What does the degraded mode hierarchy buy the team in terms of their ability to run the Build-Measure-Learn loop?
3. If a pipeline has no contract documentation, can the team run the Build-Measure-Learn loop reliably? Why or why not?

*(Tests: Degraded mode hierarchy; contract documentation — integrates Ch. 4 Build-Measure-Learn with Ch. 5 pipeline resilience)*

---

**Exercise 13** *(AI Interaction — with verification requirement)*

First, write your own answer to this question without consulting AI:
"What is the difference between a data pipeline that 'works' and a data pipeline that is 'resilient'? Why does resilience matter for a brand-facing AI tool?"

Then ask an AI assistant:
*"What are best practices for making a data pipeline resilient to upstream API failures? List at least five practices with brief explanations."*

When you receive the response:
1. Identify the strongest point in the AI's response.
2. Identify the most significant gap — specifically, does the AI response include the concept of degraded modes (reduced functionality as an explicit design choice)? If not, explain why this is a significant omission using the chapter's framing.
3. Write an addition to the AI's response that incorporates the chapter's degraded mode concept in a way that complements the AI's list.
4. Name one specific claim in the AI's response you would verify before trusting it, and describe how you would verify it.

*(Tests: Degraded mode hierarchy; pipeline resilience — AI interaction with verification)*

---

**Exercise 14** *(Twitter API Case — Brand Damage Mechanism)*

The chapter discusses the Twitter API rupture of February 2023, when Elon Musk's Twitter increased API prices dramatically. Apply the chapter's pipeline-as-brand-damage framework to this case:

1. Name the specific brands that experienced damage when the Twitter API pricing changed.
2. Identify the pipeline stage at which the brand damage originated (which contract was broken, and what was it committed to deliver?).
3. Explain why the brand damage was asymmetric — why the tool builders suffered brand damage but Twitter did not suffer proportional brand damage from the same event.
4. Apply the contract documentation habit retroactively: what would a well-documented contract for a Twitter API dependency have said, and how would a degraded mode have limited the brand damage?

*(Tests: Apollo/Reddit and Twitter API cases — pipeline fragility and brand damage mechanism)*

---

**Exercise 15** *(Degraded Mode Design)*

Design a complete degraded mode hierarchy for the following pipeline:

**Pipeline:** A daily AI briefing tool for marketing teams. The pipeline:
- Fetches news from three sources: NewsAPI (paid tier, authenticated), Google News RSS (free, public), Twitter/X filtered stream (authenticated, paid tier)
- Classifies and scores each article using GPT-4o-mini
- Exports ranked articles to a Notion database
- Sends a formatted email via SendGrid at 8 a.m. each business day

Design at least four degraded mode levels. For each level, specify:
1. Which dependency/dependencies have failed
2. What the pipeline can still deliver
3. What it labels its output (how does it communicate the degraded state to users?)
4. At what point it should escalate to the next degraded level (the trigger for further degradation)

*(Tests: Degraded mode hierarchy — four levels designed for a real pipeline)*

---

**Exercise 16** *(n8n Workflow Design)*

Design (in prose, not code) an n8n workflow that implements the following logic:

A startup wants to monitor their three competitors' product pages (three URLs). Each morning, the workflow should:
1. Check each URL for new content
2. If new content is found, send the new content to GPT-4o-mini for a one-sentence summary
3. If no new content is found on a URL, skip that URL and continue
4. Collect all summaries from URLs that had new content
5. If at least one summary exists, send a Slack message with all summaries
6. If no new content was found on any URL, send a Slack message saying "No competitor updates today"

Specify:
1. Each n8n node needed (name the node type and its configuration)
2. Each connection between nodes
3. Where the conditional branch occurs and how it is implemented in n8n
4. The independence property: how does this workflow design allow individual URL failures to not block the entire workflow?

*(Tests: n8n nodes, connections, workflows; independence property)*

---

## Tier 3 — Synthesis (Exercises 17–19)

*Bloom's Level: Synthesize / Evaluate*
*Purpose: Combine concepts from this chapter with prior chapters, or evaluate the chapter's own claims critically. These require extended reasoning. Budget 20–30 minutes each.*

---

**Exercise 17** *(Cross-Chapter Synthesis — Chs. 4 and 5)*

Chapter 4 introduced the $100,000 no: a feature or dependency the team explicitly refuses before building begins. Chapter 5 argues for contract documentation: explicitly writing down what each upstream dependency is expected to deliver before the pipeline is built.

A student argues: "Contract documentation is a form of $100,000 no applied to infrastructure. When you document a contract and its degraded mode, you are pre-committing to what the pipeline will do when the dependency fails — which is a refusal to let the pipeline fail completely, just as the $100,000 no is a refusal to expand scope."

Evaluate this argument. Is this a useful analogy or a misleading one? Your response should:
- Identify what is structurally similar between the two concepts
- Identify where the analogy breaks down
- Conclude with a precise statement about what the two concepts share and where they are genuinely different

*(Tests: Contract documentation; $100,000 no — integrates Ch. 4 and Ch. 5)*

---

**Exercise 18** *(Cross-Chapter Synthesis — Chs. 3 and 5)*

Chapter 3 argued that archetype drift damages brand by violating the implicit promise the brand has made to its audience. Chapter 5 argues that pipeline failures damage brand by violating the implicit promise the tool has made to its users.

Construct the strongest possible version of the following claim: "Pipeline resilience is brand strategy, not just infrastructure engineering." Your argument should:
- Use the Apollo/Reddit case as evidence
- Use the archetype drift mechanism from Chapter 3 to explain the brand damage pathway
- Identify what the pipeline's "implicit promise" is and how it parallels the archetype's implicit promise
- Conclude with one specific design decision that serves both pipeline resilience and brand coherence simultaneously

*(Tests: Pipeline as brand commitment; archetype drift mechanism — integrates Ch. 3 and Ch. 5)*

---

**Exercise 19** *(Evaluation — Chapter's Own Claim)*

The chapter argues that "every upstream dependency is a contract" and that contract documentation and degraded modes are necessary for any production pipeline. A senior engineer challenges this:

"This is over-engineering for student projects. Degraded modes add code complexity. Contract documentation adds maintenance overhead. For a solo developer building a course project that three instructors will use for five months, the cost of degraded modes exceeds the cost of the occasional failure. The right architecture for a course project is the simplest one that works — not the most resilient one. The chapter's advice is designed for production systems, not prototypes."

Evaluate this argument:
1. What is the engineer getting right?
2. What is the engineer getting wrong about the chapter's intent?
3. Is there a threshold — by user count, by duration of operation, by dependency criticality — below which the chapter's contract documentation and degraded mode advice genuinely does not apply?
4. How should the chapter's advice be calibrated for a course project vs. a production system?

*(Tests: Contract documentation; degraded mode hierarchy — stress-tests the chapter's scope of applicability)*

---

## Tier 4 — Challenge (Exercise 20)

*Bloom's Level: Evaluate / Create*
*Purpose: Produce original analysis that extends the chapter's framework into a new domain. There is no single correct answer. Assessment is by rubric.*

*No model answer is provided for Tier 4 exercises. Assessment uses the rubric below.*

---

**Exercise 20** *(Capstone — Pipeline Architecture and Contract Documentation for Your Tool)*

Design the complete pipeline architecture for the AI tool you are building in this course. Your submission should include:

1. **Pipeline stage diagram** — a prose or table description of every stage in your pipeline, from data source to user-facing output. Include every external dependency at each stage.

2. **Contract documentation** — for every external dependency (APIs, data sources, LLM providers, deployment platforms), write a contract entry with:
   - Dependency name and endpoint
   - What the pipeline relies on from this dependency (the contractual commitment)
   - The most likely breaking change based on the chapter's discussion of real API changes
   - The degraded mode the pipeline will enter

3. **Degraded mode hierarchy** — design at least four levels of degraded operation for your specific pipeline. For each level, specify what has failed, what the pipeline still delivers, and how the output is labeled.

4. **Independence property** — describe how your pipeline design allows one stage to fail without blocking all subsequent stages. If your pipeline is currently sequential (one failure stops everything), propose one specific architectural change that would add independence.

5. **Brand damage assessment** — using the Apollo/Reddit case as a template, identify the specific upstream dependency change in your pipeline that would cause the most brand damage if it occurred without warning. Explain the mechanism: which contract breaks, what the user experiences, and why this would damage the brand rather than just disrupting the tool.

**Rubric:**

| Criterion | Strong | Adequate | Weak |
|---|---|---|---|
| Contract documentation completeness | Every external dependency has a documented contract with all four elements | Most dependencies documented; one or two missing elements | Dependencies listed but contractual commitments not specified |
| Degraded mode specificity | Four or more degraded mode levels each with specific triggers, deliverables, and labeling | Three levels designed with some specificity | Degraded modes named but not operationally defined |
| Independence property | At least one specific architectural change described that adds independence; the change is implementable | Independence discussed but architectural change not specified | No independence property analysis |
| Brand damage identification | Names the highest-risk dependency with mechanism (contract break → user experience → brand signal) | Names a risk but mechanism is incomplete | Generic "the pipeline might fail" without specificity |
| Integration with prior chapters | Uses vocabulary or concepts from at least two prior chapters (archetype, PRD boundary, validated learning) in the analysis | Uses one prior chapter concept | Analysis is isolated to Ch. 5 concepts only |

---

## Answer Key

> Attempt all exercises before reading this section.

---

**Exercise 1**
*Model answer:*
1. ETL — batch processing at midnight, transform, load to warehouse; scheduled, not real-time
2. Stream-processing — real-time processing within milliseconds; event-driven
3. Workflow automation — trigger-based (form submission), multi-step orchestration with external service calls
4. Inference — receives input, runs model, returns output via API; the pipeline IS the model call
5. ETL — scheduled hourly collection, transformation (join), report export; batch, not real-time
*Common error:* Students classify item 3 as ETL because it has extraction and transformation. The distinction is trigger-based orchestration with branching logic and external calls — the defining characteristic of workflow automation — vs. scheduled batch loading into a warehouse.
*Chapter reference:* Four pipeline categories — Ch. 5

---

**Exercise 2**
*Answer:* False
*Model answer:* The chapter defines a pipeline as a chain of contracts in an architectural sense — each stage makes an implicit commitment to the next stage about what it will deliver (data format, availability, latency). These are not legal agreements; they are structural dependencies that hold the pipeline together. When an upstream stage changes what it delivers, it breaks the downstream stage's assumption — the contract is violated whether or not there is a legal agreement.
*Common error:* Students infer "contract" means legal formality because the chapter uses precise language. The chapter's meaning is architectural dependency, not legal obligation.
*Chapter reference:* Pipeline as chain of contracts — Ch. 5

---

**Exercise 3**
*Model answer:*
1. Numbers: Apollo made approximately 7 billion API calls per month to Reddit. Reddit's pricing change would have implied approximately $20 million per year in API costs. Reddit gave 30 days notice before the pricing took effect.
2. Mechanism: Apollo was a third-party Reddit client — its product was entirely built on Reddit data. When Reddit broke the API contract (by making it economically non-viable), Apollo's product ceased to exist. Apollo's users, who had built a workflow around Apollo's interface, experienced the brand damage: they lost a tool they relied on, not because Apollo failed to build a good product, but because Apollo's product had no redundancy or degraded mode when its single upstream contract was violated.
3. Why pipeline fragility rather than business dispute: Apollo had no degraded mode. The pipeline was: Reddit API → Apollo client → user experience. When the first link was severed, the entire pipeline stopped. A resilient pipeline design would have built fallback access or gradual degradation; Apollo's architecture had no independence property.
*Common error:* Students describe the case as "Reddit being greedy" — a business analysis — rather than identifying the architectural vulnerability: 100% dependence on a single upstream data source with no contract documentation and no degraded mode.
*Chapter reference:* Apollo/Reddit API case — Ch. 5

---

**Exercise 4**
*Model answer:*
1. Informative failure — the pipeline detects a contract violation and immediately notifies the operator with a specific failure description. The pipeline stops, but the operator knows exactly why.
2. Partial degradation — the pipeline continues operating by dropping the failed dependency and running on remaining sources; output is labeled to indicate reduced fidelity.
3. Fallback source — the pipeline switches from the preferred data source to a pre-configured secondary source; output is labeled "backup source."
4. Graceful staleness — the pipeline delivers the most recent successfully retrieved data, clearly labeled with the retrieval date and a staleness warning.
*Common error:* Students list the four levels without distinguishing them from each other — particularly conflating partial degradation and fallback source. Partial degradation = fewer sources; fallback source = different source for the same data.
*Chapter reference:* Degraded mode hierarchy — Ch. 5

---

**Exercise 5**
*Model answer:* The independence property means that in n8n workflows, the failure of one branch or node does not automatically propagate to other branches. If a workflow fetches from three RSS feeds, a failure on one feed fetch does not prevent the other two from completing. Independence is architecturally enforced by how n8n handles errors at the node level — a node can be configured to continue the workflow even if it errors, routing to an error handler rather than stopping everything. This matters for pipeline resilience because it allows the workflow to deliver partial results (partial degradation) rather than total failure when one of several sources is unavailable.
*Common error:* Students describe independence as a feature they must explicitly code, when the chapter argues it is a design principle achievable through node-level error handling and workflow branching in n8n.
*Chapter reference:* Independence property — Ch. 5

---

**Exercise 6**
*Model answer:*
1. Rate limit/pricing change. Degraded mode: fallback source (if an alternative Reddit data source exists) or graceful staleness (deliver yesterday's analysis labeled "API unavailable — using cached data").
2. Data schema change. Degraded mode: informative failure immediately — the pipeline should detect that the expected field is missing and alert the operator with the specific field name and API version.
3. Authentication failure. Degraded mode: informative failure — the 401 error is specific and actionable; the operator can resolve it by refreshing the token. Partial degradation is not appropriate because this affects all requests, not just some.
4. API deprecation (Heroku free tier). Degraded mode: this is an infrastructure failure, not a data source failure. The appropriate response is redeploy to an alternative platform (not a degraded mode within the pipeline, but a pipeline recovery action). The chapter's degraded mode hierarchy applies to data source failures, not deployment environment failures.
5. Data schema change (unexpected field). Degraded mode: partial degradation — configure the schema validator to pass records that fail on unexpected new fields rather than rejecting them; flag records with the new field for operator review.
*Common error:* Students classify item 4 (Heroku deprecation) as a rate limit change because it involves pricing. This is a deployment environment failure, not a data contract violation — the category is different.
*Chapter reference:* Contract violation categories; degraded modes — Ch. 5

---

**Exercise 7**
*Model answer:* Contract documentation is the practice of explicitly writing down, before building, what each upstream dependency is expected to deliver — the commitment, the likely breaking change, and the degraded mode. Contract monitoring is the practice of detecting when a contract has been violated — alerting when the expected data format changes, when the response rate drops, when authentication fails. Documentation must precede monitoring because you cannot write a monitor that detects a violation of a commitment you have not articulated. Monitors test specific conditions; those conditions must be defined before the monitor can be written. A team that starts monitoring without documentation will write monitors for the symptoms they have already experienced, not for the class of contract violations the pipeline is structurally vulnerable to.
*Common error:* Students describe contract monitoring as the more important activity because "documentation is just paperwork." The chapter's argument is that documentation is the prerequisite that makes monitoring specific and actionable rather than generic.
*Chapter reference:* Contract documentation and monitoring — Ch. 5

---

**Exercise 8**
*Model answer:* A **node** is a single unit of work in n8n — it represents one action, such as fetching data from an API, transforming a value, or sending a message. A **connection** is a directed link between two nodes that passes data from the output of one node to the input of the next. A **workflow** is the complete directed graph of nodes and connections that defines a multi-step automated process. Together, nodes define what work gets done at each step, connections define the order and data flow, and workflows define the complete process as a configurable, reusable unit that can be triggered, scheduled, or called from other workflows.
*Common error:* Students define a workflow as "a collection of nodes" without defining the connection as a structural element. Connections are not implicit; they are explicit data-passing links that determine how outputs from one node become inputs for the next.
*Chapter reference:* n8n nodes, connections, workflows — Ch. 5

---

**Exercises 9–16**
*Tier 2 — evaluation criteria (abbreviated):*
- Ex 9: Contract documentation entries include all four elements for all five stages; degraded modes are specific and use chapter terminology
- Ex 10: Identifies "email alert + manual fix" as informative failure without degraded mode — the pipeline has no graceful degradation; redesign names at least one degraded level
- Ex 11: Names single-dependency concentration as the structural vulnerability; explains why it was invisible until the change happened; connects to brand damage via user experience disruption
- Ex 12: Total failure = no behavioral data during downtime, Build-Measure-Learn loop paused; graceful degradation = reduced fidelity data continues, loop continues at lower confidence; no contract documentation = monitoring gaps mean failures are discovered reactively, not proactively
- Ex 13: AI typically covers retry logic, timeouts, circuit breakers — and may omit degraded modes as explicit design choices; addition should name the four degraded levels and explain the user-communication aspect
- Ex 14: Apollo (the tool), third-party Twitter clients suffered brand damage; contract broken at source layer; asymmetric damage because Twitter is the data source, not dependent on itself; contract documentation would have named "API pricing stability" as a risk
- Ex 15: Four levels designed with specific triggers, deliverables, and labeling; highest-risk dependency identified
- Ex 16: n8n workflow design includes: Schedule trigger → three parallel HTTP Request nodes (one per competitor URL) → three IF nodes (new content check) → three GPT-4o-mini nodes (conditional) → Merge node → IF node (at least one summary?) → two branches (Slack message or "no updates" Slack message); independence property: each URL branch operates independently

---

**Exercises 17–19**
*Tier 3 — No abbreviated model answer. Evaluation criteria:*
- Ex 17: Strong response identifies the structural parallel (both are pre-commitment mechanisms for refusals) and the breakdown point (PRD $100,000 no is about feature scope; contract documentation is about dependency assumptions — different domain, different decision type). Neither is reducible to the other.
- Ex 18: Constructs the claim using Apollo/Reddit (explicit pipeline failure → brand damage); maps archetype drift mechanism to pipeline failure mechanism (implicit promise violated → user experience broken → brand signal damaged); names one specific design decision that serves both (e.g., labeling degraded outputs as "backup source" serves both pipeline honesty and brand transparency)
- Ex 19: Engineer is right that degraded modes add complexity; engineer is wrong about the chapter's intent (chapter explicitly acknowledges course project context); threshold analysis should identify user count, dependency criticality, and operational duration as relevant variables

---

**Exercise 20**
*Tier 4 — No model answer. Assessment by rubric in the exercise.*

---

## Self-Assessment Rubric

After reviewing the answer key, evaluate your work:

| Score | Meaning | Next step |
|---|---|---|
| Tier 1: 6–8 correct | Core vocabulary in place | Move to Tier 2 |
| Tier 1: 4–5 correct | Gaps in foundational concepts | Return to contract documentation and degraded mode sections before Tier 2 |
| Tier 2: 6–8 mostly correct | Applying framework well | Attempt Tier 3 |
| Tier 2: 4–5 mostly correct | Gaps in application | Redo Ex 9 and Ex 15 with answer key; re-attempt others |
| Tier 3: 2–3 strong | Synthesis developing | Proceed to Tier 4 |
| Tier 3: 0–1 strong | Integration needs work | Re-read connection points between Chs. 3, 4, and 5 |

*Check your syllabus for which tiers are assigned for this chapter.*

---

## Instructor Notes

**Bloom's distribution for this chapter:**

| Tier | Exercises | Bloom's Level | % of Set |
|---|---|---|---|
| Tier 1 — Warm-up | Ex 1–8 | Remember / Understand | ~40% |
| Tier 2 — Application | Ex 9–16 | Apply / Analyze | ~40% |
| Tier 3 — Synthesis | Ex 17–19 | Synthesize / Evaluate | ~15% |
| Tier 4 — Challenge | Ex 20 | Evaluate / Create | ~5% |

**Suggested point distribution:**
- Tier 1: 5 points per item
- Tier 2: 10 points per item
- Tier 3: 20 points per item
- Tier 4: 30 points (rubric-graded)

**Exercise notes:**

*Ex 3 (Apollo/Reddit):* The most important exercise in Tier 1. Students who describe this as a business dispute have not understood the chapter's framing. Require students to use the word "architecture" in their explanation.

*Ex 6 (Contrastive classification):* Item 4 (Heroku deprecation) is a deliberate edge case — it is an infrastructure failure, not a data contract violation, and the degraded mode hierarchy does not apply in the same way. Students who apply the four degraded levels to deployment environment failure have missed this distinction.

*Ex 10 (Error analysis):* The error is subtle — the student's pipeline has an informative failure mode (email alert) but no degraded mode. This is actually a common architecture for simple pipelines and feels reasonable. The chapter's point is that for user-facing tools, the informative failure serves the operator, not the users, who experience a 24-hour outage.

*Ex 12 (Cumulative — Chs. 4 and 5):* This exercise is the core integration point for Part II. Students who have understood both chapters should be able to articulate that the Build-Measure-Learn loop depends on the pipeline running long enough to accumulate behavioral data — and that pipeline resilience is therefore a prerequisite for validated learning.

*Ex 18 (Tier 3 — Chs. 3 and 5):* The strongest student responses will identify that both archetype drift and pipeline failure damage brand through the same mechanism: an implicit promise made to users is violated. The pipeline's implicit promise is "this tool will deliver reliably"; the archetype's implicit promise is "this brand will behave consistently." Both promises are violated by the same structural failure: no pre-committed degraded mode or forcing function.

*Ex 20 (Tier 4):* The most common weakness is the independence property section — students describe independence as a concept without proposing a specific architectural change. Require at least one implementable change (e.g., "add a try/catch block at the GPT-4o-mini node that falls back to GPT-3.5-turbo") before accepting the submission.

**Common errors to watch for:**
- Treating contract documentation as optional for "simple" pipelines
- Conflating partial degradation and fallback source in the hierarchy
- Describing the Apollo/Reddit case as a business dispute rather than an architectural fragility case
- Designing degraded modes that stop the pipeline but notify the operator, without providing any user-facing degraded output

**DEI note:**
The chapter's case studies (Apollo, Twitter/X, Heroku) involve industry-specific events. Students outside the US tech startup context may have less familiarity with these cases. Encourage students to substitute local or domain-specific equivalent cases for Tier 3 exercises if these cases are not familiar.
