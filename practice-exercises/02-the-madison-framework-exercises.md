# Practice Exercises: The Madison Framework

*Chapter 2 of Branding and AI (INFO 7375)*

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before
> completing earlier ones — the tiers scaffold your understanding. Attempt
> every exercise before checking the answer key. For open-ended questions,
> write at least 2–3 sentences before reading the model answer. The act of
> attempting is where the learning happens.

---

## Learning Objectives Covered

- Define the word *agent* with precision — distinguishing between four common usages and explaining why the distinction matters for system design.
- Describe Madison's five-layer architecture and explain what each layer does, what it takes as input, and what it produces as output.
- Trace the ReAct loop (reason → act → observe) through at least one Madison layer and explain why this pattern outperforms either pure reasoning or pure tool-use.
- Explain why layered architectures are also brand decisions — specifically how the choice of five named layers creates product surfaces a company can sell and a customer can reason about.
- Compare graph-based orchestration (n8n, LangGraph) against conversation-based orchestration (AutoGen) on the dimension of production reliability, not capability.
- Select one Madison layer that fits the archetype identified in Chapter 1 and justify that choice.

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A small startup wants to build an AI tool that monitors competitor blogs and emails the founder a daily briefing. A team member proposes building "one big AI agent" that does everything. A second team member proposes using Madison's layer structure. Walk through the trade-off.

**Approach:**
Step 1: Define what the "mega-agent" would do — read all sources, deduplicate, analyze, write the briefing. One LLM call or a very large context.
Step 2: Identify the three failure problems from the chapter: token costs become unsustainable as context grows; failure modes blur (you cannot tell if the AI misread the article or wrote a bad summary); no product surfaces (you cannot sell or improve individual pieces).
Step 3: Map the same job to Madison layers — Intelligence layer gathers and scores articles, Content layer drafts the briefing, Performance layer tracks what the founder actually reads and acts on. Each layer is inspectable, replaceable, and nameable.
Step 4: Note the brand consequence — the layered design lets you say "our Intelligence layer updated this morning" to a customer, which a mega-agent cannot.

**Answer:** The layered design wins on debuggability, cost efficiency (no redundant context), and brand legibility. The mega-agent wins only on prototype speed — it is faster to build once but breaks opaquely and cannot be improved systematically.

**What to notice:** Architecture is brand. The five-layer choice is simultaneously an engineering decision and a product surface decision.

---

## Tier 1 — Warm-Up (Exercises 1–6)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them. These should feel straightforward after a careful reading.*

---

**Exercise 1**

Name the four meanings of "agent" from the chapter. For each, write one sentence that captures what distinguishes that meaning from the others.

*(Tests: Four meanings of "agent" — precision of definition)*

---

**Exercise 2**

True / False: Madison uses the word "agent" to mean an LLM that autonomously plans its own work, sets its own goals, and reports outcomes to the user without asking for guidance at each step.

*Explain your reasoning in one sentence:*

*(Tests: Madison's use of "agent" — Meaning 4, agent as specialized role in a pipeline)*

---

**Exercise 3**

In your own words, explain what the ReAct loop is as described in this chapter, without quoting it. Your explanation should name all three components (reason, act, observe) and explain why the loop outperforms either reasoning alone or tool-use alone.

*(Tests: ReAct loop — the small machine inside each Madison layer)*

---

**Exercise 4**

The chapter describes three problems that would break a "mega-agent" design. Classify each of the following symptoms as caused by which problem (token costs, failure blur, or no product surfaces):

- A customer asks "can I just buy the part of your tool that monitors news, not the content generation?" and the vendor has no way to offer that.
- After a wrong recommendation appears in the output, the team spends three days trying to determine whether the issue was bad data ingestion, a bad analysis, or a bad write-up.
- Running the tool costs $0.85 per execution in the first week and $3.20 per execution in the fourth week with the same usage.

*(Tests: Mega-agent failure modes vs. layered architecture benefits)*

---

**Exercise 5**

Name Madison's five agent layers. For each, write one sentence stating: what task it performs, what it takes as its primary input, and what it produces as output.

*(Tests: Five-layer architecture — input/output for each layer)*

---

**Exercise 6**

The chapter distinguishes graph-based orchestration (n8n, LangGraph) from conversation-based orchestration (AutoGen). What is the single most important difference between them on the dimension of production reliability?

*(Tests: Graph-based vs. conversation-based orchestration — production reliability)*

---

## Tier 2 — Application (Exercises 7–14)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations. This is where most of the learning happens. Expect these to take more time than Tier 1.*

---

**Exercise 7** *(Scenario-Based Application)*

A software team is building an AI-powered customer support tool for a healthcare company. The tool needs to answer patient questions, escalate urgent issues to human agents, track which questions were most common, and generate weekly summaries for the support manager. Map this tool onto Madison's five layers. For each layer you use, name what it would do in this specific context. If you would not use a layer, explain why.

*(Tests: Five-layer architecture applied to a new domain — mapping real tasks to named layers)*

---

**Exercise 8** *(Error Analysis)*

> The following explanation of the ReAct loop was submitted by a student. It contains an error.

```
The ReAct loop works by separating reasoning from action into two 
completely independent phases. First, the model finishes all its 
reasoning — it thinks through the entire problem and produces a 
complete plan. Then, in a separate phase, it executes all the 
actions in that plan. The observation from each action is only 
reviewed after all actions are complete, in a final review step. 
This separation is why ReAct outperforms naive tool-use.
```

1. Identify exactly where the error occurs.
2. Explain the misconception that caused it — what did the student misunderstand about the ReAct pattern?
3. Write a corrected version of the problematic sentences.

*(Tests: ReAct loop — the interleaving of thought, action, and observation)*

---

**Exercise 9** *(AI Interaction — with verification requirement)*

First, write your own answer to this question without consulting AI:
"Why does Madison's architecture use five separate named layers instead of a single unified agent?"

Then read the following AI-generated response:

*AI response:* "Madison uses five separate layers primarily for scalability. A single agent becomes slower and more expensive as the product grows because it has to handle everything in sequence. Five layers allow the work to be distributed across multiple processes running in parallel, so the system can handle higher volumes of data. This is similar to microservices architecture in traditional software engineering, where splitting functions into separate services allows horizontal scaling."

1. Identify the strongest point in the AI's response.
2. Identify the most significant error, gap, or oversimplification. Explain why it is wrong using concepts from this chapter.
3. Write a corrected version of the problematic sentence or paragraph.
4. State the specific evidence or test you would use to verify the corrected claim before trusting it.

*(Tests: Five-layer architecture rationale — brand and failure-isolation reasoning vs. scalability framing)*

---

**Exercise 10** *(Self-Explanation)*

The chapter argues that "layered architecture is brand architecture." In 2–3 sentences, explain why the choice to name five layers instead of building a mega-agent is simultaneously an engineering decision and a brand decision. Your explanation must use the term *product surface* correctly.

*(Tests: Architecture as brand decision — product surfaces and customer legibility — self-explanation)*

---

**Exercise 11** *(Cumulative — prior chapter concept)*

In Chapter 1, you learned about the Spence signaling mechanism and the four-verb framework (Ideate, Build, Brand, Ship). In this chapter, you are working with Madison's five-layer architecture. A startup is building a Madison-based marketing tool and is trying to decide whether to invest in making the five layers visible and nameable to customers, or to hide them behind a simple "generate my marketing report" interface. Using the Spence mechanism and the Brand verb from Chapter 1, argue which approach produces a stronger separating signal for the startup, and why.

*(Tests: Five-layer architecture as product surface + Spence signaling and Brand verb from Chapter 1 — interleaved)*

---

**Exercise 12** *(Scenario-Based Application)*

You are advising a team that is deciding between graph-based orchestration (using n8n) and conversation-based orchestration (using AutoGen) for a daily competitor-monitoring tool. The tool runs at 6 AM every day, pulls from ten RSS feeds, scores articles, and writes a report to a Slack channel. The team's CTO argues for AutoGen because it can "handle unexpected task sequences." Using the chapter's production-reliability argument, evaluate the CTO's reasoning and recommend which approach the team should use.

*(Tests: Graph-based vs. conversation-based orchestration — production reliability for a specific use case)*

---

**Exercise 13** *(Error Analysis)*

> The following student analysis identifies an archetype-to-layer match. It contains an error.

```
I have a Caregiver archetype. The chapter says Caregiver brands are 
organized around service, compassion, and removing friction for others. 
The Madison layer that best fits me is the Performance layer, because 
the Performance layer is about measuring and optimizing outcomes — 
and a Caregiver wants to make sure the product is performing well 
for the people who depend on it. The failure mode to watch for is 
martyrdom, where I focus so much on users' comfort that I forget 
to maintain my own product.
```

1. Identify exactly where the error occurs.
2. Explain the misconception — what did the student misunderstand about the Caregiver archetype's alignment with Madison layers?
3. Write a corrected analysis.

*(Tests: Archetype-to-layer alignment — Caregiver vs. Experience layer)*

---

**Exercise 14** *(Scenario-Based Application)*

Write a five-step ReAct trace for the Madison Performance Agent as it runs a Thompson sampling experiment on two different email subject line variants for a client. Use the format from the chapter (THOUGHT → ACTION → OBSERVATION → THOUGHT → ACTION). You may invent plausible data. Label each step correctly and explain at the end what distinguishes this ReAct trace from a simple script that just runs the experiment.

*(Tests: ReAct loop traced through the Performance layer — Thompson sampling applied)*

---

## Tier 3 — Synthesis (Exercises 15–16)

*Bloom's Level: Analyze / Evaluate*
*Purpose: Connect this chapter's concepts to a concept from a prior chapter. These questions have no single correct answer — a strong response requires judgment, not formula-following.*

---

**Exercise 15** *(Cross-Chapter Synthesis)*

As introduced in Chapter 1: The Creative Engineer, the Spence signaling mechanism explains why costly signals separate candidates in a market. In this chapter, you are working with Madison's five-layer architecture and the concept that architecture is a brand decision.

A solo developer is building a marketing intelligence tool for small businesses. She is considering two approaches: (A) a well-documented five-layer Madison-style architecture with named components that clients can inspect; (B) a simpler pipeline that hides all complexity behind a polished interface. Using the Spence mechanism from Chapter 1 and the architecture-as-brand argument from this chapter, analyze which approach creates a stronger long-term brand signal. What does the architecture choice communicate about the developer's expertise, and how does that communication compound over time?

*This question connects five-layer architecture as brand signal to the Spence signaling mechanism.*

*What distinguishes a surface answer from a strong one:*
- Applies the separating equilibrium concept to product architecture, not just personal branding
- Uses "product surface" correctly to show what customers can inspect, trust, and buy
- Explains why the compounding effect of architecture-as-brand differs from a one-time signal

*(Tests: Five-layer architecture as brand decision + Spence signaling mechanism — Ch. 2 + Ch. 1)*

---

**Exercise 16** *(Cross-Chapter Synthesis)*

As introduced in Chapter 1: The Creative Engineer, the twelve Jungian archetypes each have a shadow — the specific failure mode produced when the archetype's strength is taken too far. In this chapter, you are working with the architecture-as-brand argument and the autonomy/orchestration choice.

A developer has an Explorer archetype. Their shadow is aimlessness — perpetual searching that never commits. They are designing their Madison-based tool and feel drawn to conversation-based orchestration (AutoGen) because it "handles unexpected task sequences" and feels exploratory and free. Using both the Explorer shadow from Chapter 1 and the orchestration comparison from this chapter, explain the specific risk this developer faces. What architectural choice would you recommend, and what guardrails would you add?

*This question connects the Explorer archetype's shadow to the conversation-based orchestration failure mode.*

*What distinguishes a surface answer from a strong one:*
- Names the specific failure mode that conversation-based orchestration enables (emergent, unpredictable task sequences) and connects it to the Explorer shadow (aimlessness) as the *same failure expressed in code*
- Recommends a specific architectural mitigation, not just "be careful"
- Explains how graph-based orchestration functions as an archetype guardrail, not just a technical preference

*(Tests: Graph-based vs. conversation-based orchestration + Explorer archetype shadow — Ch. 2 + Ch. 1)*

---

## Tier 4 — Challenge (Exercise 17)

*Bloom's Level: Evaluate / Create*
*Purpose: Transfer beyond what was explicitly taught. This exercise is genuinely difficult. Solvable with the tools introduced in this chapter, but not by following a formula or imitating a worked example.*

---

**Exercise 17** *(Transfer Challenge)*

The chapter ends with a "Still Puzzling" note: the exact boundary between "agent as role" and "agent as autonomous system" has not stabilized. Devin claims autonomy but runs in a sandboxed environment with humans reviewing most pull requests. Madison uses orchestrated roles, but the LLM inside each layer makes local decisions that look agentic.

Design a taxonomy that resolves this ambiguity. Your taxonomy should use at least three dimensions (not a binary), correctly classify Madison, Cursor, Devin, and one additional system of your choosing, and be specific enough that a developer building a new tool could use it to determine where their system sits. Then: given your taxonomy, identify at which point on at least one dimension an orchestrated Madison-style architecture becomes indistinguishable from an autonomous system — and what the brand consequences of crossing that threshold would be.

*A strong response will address:*
- Three specific dimensions (not just "how autonomous is it?") that collectively distinguish the space
- An honest placement of all four named systems on each dimension, with evidence for each placement
- A specific threshold on at least one dimension where orchestration and autonomy become equivalent — and why that threshold matters for brand trust

*(Tests: Four meanings of agent + architecture as brand decision applied to a novel taxonomy problem)*

---

## Answer Key

> Attempt all exercises before reading this section.
> For Tier 3 and Tier 4, your answer does not need to match the model exactly —
> use the "what a strong answer includes" criteria to evaluate your own response.

---

**Worked Example**
*No answer needed — the worked example is its own model.*

---

**Ex 1**
*Model answer:* Meaning 1 — a single LLM call ("I built an agent that summarizes emails"); essentially a prompt-in, response-out function. Meaning 2 — an LLM with tools and a loop (can call APIs, observe results, reason, take another action). Meaning 3 — a long-running autonomous system that plans its own work and reports outcomes (Devin-style). Meaning 4 — a specialized role in a larger system with defined inputs and outputs, coordinated by an orchestration layer (how Madison uses the word).
*Common error:* Students often conflate Meanings 2 and 3, treating any LLM that can call tools as "autonomous." The critical distinction is whether the system plans its own next goal or executes a defined role.
*Chapter reference:* Section 1 — What "Agent" Actually Means

---

**Ex 2**
*Answer:* False
*Correct because:* Madison uses Meaning 4 — agents as specialized roles in a coordinated pipeline. The chapter explicitly states: "Madison uses meaning 4. All five of its agents are specialized roles in a coordinated pipeline, not autonomous problem-solvers."
*Common error:* Students who have seen "agent" used to mean autonomous systems will answer True. The chapter specifically flags this mismatch and defines Madison's usage precisely.
*Chapter reference:* Section 1 — What "Agent" Actually Means, paragraph ending "Madison uses meaning 4"

---

**Ex 3**
*Model answer:* The ReAct loop is a pattern in which an LLM alternates between reasoning (thinking about what to do next, in natural language) and acting (calling a tool, querying an API, modifying state), and then observing the result before reasoning again. Pure reasoning without action lets the model plan but not do anything in the world. Pure tool-use without reasoning produces reactive responses without a coherent plan. ReAct's interleaving lets reasoning inform better action choices, and observations update reasoning based on real-world feedback — producing better plans and more adaptive execution than either alone.
*What a strong answer includes:*
- The interleaving mechanism — not just that all three exist, but that each feeds the next
- Why observations matter: they update reasoning in light of real-world feedback, not just signal completion
*Chapter reference:* Section 3 — The ReAct Loop

---

**Ex 4**
*Model answer:* "Can I just buy the part that monitors news?" → no product surfaces. "Three days to find the fault" → failure blur. "Cost tripling over four weeks" → token costs (redundant context accumulation over repeated executions).
*Common error:* Students swap failure blur and no product surfaces, treating "can't isolate the failing part" as a surface issue. Failure blur is specifically about debugging — not knowing where an error occurred. No product surfaces is about customer legibility and commercial partitioning.
*Chapter reference:* Section 2 — The Mega-Agent Failure

---

**Ex 5**
*Model answer:* Intelligence — analyzes market data and consumer sentiment; input: news feeds, social data; output: scored, ranked intelligence briefs. Content — creates marketing materials; input: brand brief + audience parameters; output: headline variants, copy drafts. Research — uncovers customer insights; input: survey data, customer records; output: synthetic personas, segmentation analysis. Experience — enhances customer interactions; input: customer journey data, interaction history; output: personalized recommendations, concierge responses. Performance — measures and optimizes outcomes; input: experiment results, conversion data; output: optimized allocation decisions, performance reports.
*Common error:* Students often describe what each layer does without naming inputs and outputs. The chapter emphasizes the input/output specification as what makes each layer inspectable and independently replaceable.
*Chapter reference:* Section 2 — The Five Layers

---

**Ex 6**
*Model answer:* Graph-based orchestration is predictable: every step is defined in advance, every path is explicit, every failure is locatable because the workflow graph defines the control flow. Conversation-based orchestration is flexible but unpredictable: agents can handle novel sequences that were not pre-specified, but failure modes are harder to isolate and the debugging surface is enormous. The key production-reliability difference is that graph-based systems fail at *named locations* you can inspect and fix; conversation-based systems fail diffusely across an emergent conversation that may never have been anticipated.
*Common error:* Students often say "graph-based is better" without explaining the mechanism. The stronger answer names specifically why predictability matters for production — not capability benchmarks, but debuggability and mean time to recovery.
*Chapter reference:* Section 4 — Orchestration

---

**Ex 7**
*Model answer:* Intelligence — monitors incoming support ticket categories, flags spikes in question type or urgency signals. Content — drafts responses to common questions (FAQ-style), generates the weekly summary for the support manager. Research — analyzes patterns in patient questions to surface the most frequently confused topics; generates synthetic patient personas for training material. Experience — handles the conversational interface for patients, escalates to human agents when urgency signals exceed a threshold. Performance — tracks which response types resolved issues, measures escalation rate, runs experiments on response formats. The Performance and Experience layers are the most critical here — Experience is the brand-facing layer patients interact with, and Performance closes the feedback loop.
*Common error:* Students often skip the Performance layer in healthcare contexts because "measuring outcomes" sounds secondary. In this scenario, Performance is critical for identifying dangerous response patterns (escalation failures, unresolved queries).
*Chapter reference:* Section 2 — The Five Layers

---

**Ex 8**
*Where the error occurs:* "First, the model finishes all its reasoning — it thinks through the entire problem and produces a complete plan. Then, in a separate phase, it executes all the actions in that plan. The observation from each action is only reviewed after all actions are complete."
*The misconception:* The student described a plan-then-execute pattern, which is the opposite of ReAct's interleaving. In ReAct, reasoning and action are tightly coupled — each observation feeds immediately back into the next reasoning step, not into a final review. The student described batch reasoning followed by batch execution.
*Corrected version:* "The ReAct loop interleaves reasoning, action, and observation at each step. After each action, the observation is fed immediately back into the next reasoning step — the model updates its plan based on what it found before taking the next action. This interleaving is what distinguishes ReAct from plan-then-execute patterns."
*Chapter reference:* Section 3 — The ReAct Loop

---

**Ex 9**
*Model answer:* Strongest point: the parallelism observation is partially correct — parallel branches in a layered system can improve throughput. The significant error: the AI attributes the five-layer choice primarily to scalability/parallelism, missing the chapter's actual three reasons: token cost efficiency (specialized agents process less redundant context), failure isolation (layered systems fail at named locations), and product legibility (named layers create surfaces customers can trust and buy). The parallel-processing argument is real but secondary and not the primary motivation the chapter gives. Corrected sentence: "Madison uses five separate layers primarily because doing so isolates failures to inspectable locations, reduces token costs by specializing context, and creates product surfaces that customers can understand, pay for, and trust — not primarily for parallel scaling." To verify: read Madison's architecture documentation and the chapter's "Mega-Agent Failure" section, which names three specific failure modes that the mega-agent produces.
*What a strong answer includes:*
- Identifies the three specific reasons from the chapter (failure isolation, token cost, product surface) as the correct primary motivations
- Acknowledges the partial truth in the scalability argument without letting it substitute for the real argument
- A verification step that references a specific section of the chapter, not just "re-read it"
*Chapter reference:* Section 2 — The Mega-Agent Failure and Section 5 — Architecture as Brand

---

**Ex 10**
*Model answer:* Naming five layers instead of building a mega-agent creates five *product surfaces* — identifiable components that a customer can discuss, a CFO can budget, a developer can version, and a sales team can sell separately. These surfaces are simultaneously the result of engineering choices made for failure-isolation reasons and the things customers interact with, trust, and pay for. Architecture without surfaces is engineering without a customer; surfaces without architecture are marketing without reliability.
*Common error:* Students often describe product surfaces as "features customers can see" — which is imprecise. Product surfaces are specific enough to name, version, and price independently. The distinction matters because a single-page interface over a mega-agent has visible features but no surfaces — the customer cannot reason about what went wrong, buy a subset, or compare versions.
*Chapter reference:* Section 2 — Naming Is Brand Strategy; Section 5 — Architecture as Brand

---

**Ex 11**
*Model answer:* The five-layer architecture creates a separating signal because it demonstrates a level of engineering judgment that a simpler pipeline does not. A startup that shows customers named, inspectable layers with defined contracts is communicating something about the quality and rigor of their build — that is a costly signal in the Spence sense, because it requires real design discipline to produce. The Brand verb requires audience specification, positioning, and making the work recognizable to the right people. The five-layer architecture, by creating nameable product surfaces, does Brand work automatically — it gives enterprise customers something to evaluate, compare, and trust. A polished interface over a mega-agent hides the build, which pools all hidden-complexity products together and produces no separating signal.
*Common error:* Students often say the five-layer architecture "looks more professional" — which is true but misses the Spence mechanism. The stronger answer explains *why* it separates: because it is costly to produce, and the cost correlates with engineering discipline that customers actually want.
*Chapter reference:* Chapter 1 — Spence Mechanism, Brand Verb; Chapter 2 — Architecture as Brand

---

**Ex 12**
*Model answer:* The CTO's reasoning about "unexpected task sequences" is not wrong — AutoGen does handle them better. But the chapter's production-reliability argument says that for a daily pipeline with a defined output (news articles → Slack report), predictability is more important than flexibility. The tool runs at 6 AM every morning; the marketing director trusts it to have a report ready. A graph-based n8n workflow that fails at a named location can be fixed before the 6 AM run is complete. A conversation-based orchestration that "handles unexpected sequences" can produce a report that is correct on Mondays and wrong on Thursdays with no obvious diagnosis path. Recommendation: n8n for this use case. The CTO should reserve conversation-based orchestration for exploratory tasks where the right sequence is genuinely unknowable in advance.
*Common error:* Students often recommend AutoGen to be technically ambitious. The chapter explicitly argues that for production reliability on defined, recurring tasks, graph-based orchestration wins. The test is not "which is more capable" but "which fails more predictably."
*Chapter reference:* Section 4 — Orchestration; Madison's production reliability rationale

---

**Ex 13**
*Where the error occurs:* "The Madison layer that best fits me is the Performance layer."
*The misconception:* The student correctly identified the Caregiver archetype and shadow but mismatched it to the layer. The Caregiver's core drive is service and removing friction for others — which maps directly to the Experience layer (customer interactions, journey transformation). The Performance layer is about optimization and measurement, which fits a more analytically-driven archetype.
*Corrected analysis:* "I have a Caregiver archetype. The Madison layer that best fits me is the Experience layer — this is where customer interactions happen, where friction is removed and people are guided. The Experience layer is the place where the Caregiver's core commitment to service is most directly expressed. The failure mode to watch for is martyrdom: I might over-engineer the customer experience until the product becomes unsustainably complex to maintain."
*Chapter reference:* Section 6 — How to Read Madison for Your Own Design; archetype-to-layer alignment

---

**Ex 14**
*Model answer:*
THOUGHT: I need to allocate clicks between Subject Line A and Subject Line B for this week's email campaign. I'll use Thompson sampling to balance exploration and exploitation.
ACTION: Pull current performance data — A: 42 sends, 11 opens (26% rate); B: 38 sends, 14 opens (37% rate).
OBSERVATION: B has higher open rate but smaller sample. The beta distributions overlap significantly — need more data before committing.
THOUGHT: Thompson sampling says sample from each distribution and send to the variant whose sampled value is higher. B's sampled value is likely to be higher given the rate, but A still wins some samples.
ACTION: Run Thompson sample — result: allocate 60% of remaining sends to B, 40% to A.
OBSERVATION: Allocation set. Scheduling 240 sends to B and 160 to A for remaining campaign window.
*What distinguishes this from a script:* The THOUGHT steps show the model updating its allocation strategy based on observed data rather than following a fixed if/else rule. A script would apply a predetermined threshold; the ReAct trace shows the agent reasoning about statistical overlap and adapting its allocation dynamically.
*Chapter reference:* Section 3 — ReAct Loop traced through Performance Layer

---

**Ex 15 — Synthesis**
*Model answer:* A well-documented five-layer architecture produces a stronger long-term brand signal by creating product surfaces that are inspectable, nameable, and demonstrably costly to produce. By the Spence mechanism, a signal works because its cost-structure correlates with underlying productive capacity — and building a coherent five-layer system is genuinely harder than wrapping a mega-agent in a polished UI. The customer who sees named layers can audit the Intelligence layer's data sources, compare the Content layer's output quality across versions, and hold the vendor accountable at each layer — none of which is possible with a polished black-box interface. Over time, the five-layer architecture compounds: each layer creates a separate reputation asset that the vendor can improve independently, which means the brand gets stronger with each layer upgrade. The polished interface over a mega-agent cannot compound in the same way.
*What a strong answer includes:*
- Applies the separating equilibrium concept to product architecture — the five-layer design is harder to fake
- Uses "product surface" correctly to show what customers can inspect and trust
- Explains the compounding effect: each named layer is a separate trust-building surface
*Common error:* A surface answer says "the five-layer design looks more professional." The stronger answer explains the mechanism — product surfaces create inspection points, which customers use to evaluate the quality claim.
*Chapter reference:* Chapter 2 — Architecture as Brand; Chapter 1 — Spence Mechanism

---

**Ex 16 — Synthesis**
*Model answer:* The Explorer's shadow is aimlessness — perpetual searching that never commits, novelty mistaken for progress. Conversation-based orchestration (AutoGen) is the architectural form of the Explorer shadow: agents can handle unexpected sequences, redirect each other, and explore emergent paths that were never pre-specified. For an Explorer archetype developer, this feels right — it expresses their natural drive toward discovery. But the architectural failure mode of conversation-based orchestration is exactly the shadow activated: the system explores endlessly, handles "unexpected task sequences" by creating new ones, and may never converge on a reliable output. The recommended choice is graph-based orchestration (n8n) with explicit graph boundaries that prevent scope creep. The guardrails: define the task graph before building, use hard step ceilings, and add a completion condition that the Explorer cannot override. The architecture should externalize the discipline the archetype does not naturally impose.
*What a strong answer includes:*
- Names the specific failure mode of conversation-based orchestration and shows it as the Explorer shadow in code
- Recommends a specific mitigation (graph-based with hard ceilings) rather than just "be careful"
- Explains why the architecture is a guardrail, not just a preference
*Common error:* A surface answer says "Explorer archetypes should use graph-based orchestration." The stronger answer explains *why* — the shadow and the architectural failure mode are the same structure.
*Chapter reference:* Chapter 2 — Orchestration; Chapter 1 — Explorer archetype and shadow

---

**Ex 17 — Challenge**
*No model answer provided.*
*A strong response will address:*
- Three specific dimensions (e.g., goal-setting locus: who decides the agent's next goal; failure surface: where errors appear and who sees them; task-space coverage: how much of the task space was specified in advance)
- An honest placement of Madison, Cursor, Devin, and a fourth system on each dimension, with specific evidence
- A threshold on at least one dimension where orchestration becomes indistinguishable from autonomy — for example, an orchestrated system with enough self-modification capability at the agent level may become practically autonomous even with a formal orchestrator
*This question is intentionally open-ended. Discuss your response with a peer or instructor to evaluate your reasoning.*

---

## Self-Assessment Rubric

After reviewing the answer key, evaluate your work:

| Score | Meaning | Next step |
|---|---|---|
| Tier 1 complete, most correct | Core concepts in place | Move to Tier 2 |
| Tier 2 mostly correct | Applying concepts well | Move to Tier 3 |
| Tier 2 struggling (>2 wrong) | Gaps in application | Return to flagged sections, then redo Tier 2 |
| Tier 3 attempted and close | Strong conceptual understanding | Proceed to Tier 4 |
| Tier 3 missed the integration | Concepts learned in isolation | Revisit the prior chapter referenced in the question |
| Tier 4 attempted seriously | Ready for advanced work | Compare with a peer or discuss with instructor |

---

## Instructor Notes

**Bloom's distribution for this chapter:**

| Tier | Exercises | Bloom's Level | % of Set |
|---|---|---|---|
| Tier 1 — Warm-up | Ex 1–6 | Remember / Understand | ~35% |
| Tier 2 — Application | Ex 7–14 | Apply / Analyze | ~47% |
| Tier 3 — Synthesis | Ex 15–16 | Analyze / Evaluate | ~12% |
| Tier 4 — Challenge | Ex 17 | Evaluate / Create | ~6% |

**Suggested point distribution:**
- Tier 1: 5 points per item
- Tier 2: 10 points per item
- Tier 3: 15 points per item
- Tier 4: 20 points (optional extension or extra credit)

**Worked example note:**
The worked example targets the mega-agent failure modes. If students struggle with Ex 4 after completing it, ask them to re-read the "Mega-Agent Failure" section and describe each failure in their own words before attempting the exercise again.

**Error analysis exercise (Ex 8):**
The deliberate error is the plan-then-execute misconception of ReAct. Watch for students who describe ReAct as "planning first, then acting" — this is the exact error the exercise targets.

**AI interaction exercise (Ex 9):**
The AI response contains a correct but incomplete answer — parallel processing is real but secondary. Students who accept it have missed the three primary reasons (failure isolation, token cost, product surface).

**Self-explanation exercise (Ex 10):**
Watch for students who describe product surfaces as "features the user sees." Product surfaces are specifically components that can be sold, versioned, and debugged independently — not just visible UI elements.

**Cumulative exercise (Ex 11):**
This exercise requires the Spence signaling mechanism from Chapter 1. If students have not retained that concept, use the failure as a teaching moment: ask what makes a signal separating (cost-structure), then ask how the five-layer architecture is costly to produce.

**Common errors to watch for:**
- Conflating Meaning 3 (autonomous system) with Meaning 4 (specialized role) in the agent definition
- Describing ReAct as plan-then-execute rather than interleaved loops
- Mismatching archetypes to layers based on surface similarity rather than the chapter's alignment guide

**DEI note:**
All scenarios in this exercise set have been written to avoid cultural, regional, or socioeconomic assumptions.
