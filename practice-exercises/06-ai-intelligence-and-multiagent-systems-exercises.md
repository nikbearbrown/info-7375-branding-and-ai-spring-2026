# Practice Exercises: AI Intelligence and Multiagent Systems

*Chapter 6 of Branding and AI (INFO 7375)*

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before
> completing earlier ones — the tiers scaffold your understanding. Attempt
> every exercise before checking the answer key. For open-ended questions,
> write at least 2–3 sentences before reading the model answer. The act of
> attempting is where the learning happens.

---

## Learning Objectives Covered

1. **Classify** an AI system into one of four intelligence patterns — single LLM call, chained LLM calls, tool-using agent (ReAct), or multi-agent system — and justify the classification.
2. **Distinguish** autonomous, orchestrated, and conversational multi-agent architectures, and explain the trade-offs of each on the autonomy/orchestration spectrum.
3. **Explain** why naming (role, goal, backstory) in agent specification is load-bearing — not cosmetic — and identify the mechanism by which it shapes agent behavior.
4. **Predict** which of the three autonomous agent failure modes — compounding error, cost runaway, or trust collapse — is most likely for a given architecture, and propose a specific mitigation.
5. **Select** the architecture that matches a given brand archetype and user experience requirement, justifying the selection using the chapter's archetype-to-architecture mapping.
6. **Apply** the three anti-hallucination patterns — permission to abstain, structured output with null fields, confidence labeling — to a real agent specification.

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A startup is building an AI tool that takes a job description URL, researches the company using publicly available information, and produces a two-page company brief for a job seeker. Classify this tool by intelligence pattern, select an architecture, name the failure modes to watch for, and apply at least one anti-hallucination pattern.

**Approach:**

Step 1: Classify the intelligence pattern. The tool needs to: (a) retrieve a job description, (b) identify the company, (c) search for information about the company (web search, LinkedIn, Crunchbase, news), (d) synthesize findings into a brief. Step (c) requires calling external tools (search, scraping), deciding what to search for, and interpreting results. This is the ReAct pattern — the agent reasons about what to search, acts by calling the tool, observes the result, and repeats.

Step 2: Select architecture. A single company brief is a well-scoped task with a clear output format. An autonomous multi-agent architecture would introduce coordination overhead without benefit. An orchestrated architecture with a fixed sequence (research → synthesize → format) matches the task well. But the research step requires dynamic tool use — how many searches depends on what the agent finds. Recommendation: tool-using agent (ReAct) with an orchestrated outer loop. One agent does the research; a second agent synthesizes. Two-agent orchestrated system.

Step 3: Identify failure modes. In an orchestrated system: (a) the research agent may run too many searches before the orchestrator stops it (cost runaway at the research step); (b) the research agent may return confident-sounding company facts that are outdated or incorrect (compounding error if synthesis agent builds on them without verification). Trust collapse is less likely in a one-user, one-job tool — the user is the researcher, not a mass audience.

Step 4: Apply anti-hallucination patterns. The synthesis agent should: (a) require a `sources_verified: bool` field in its output (structured output with null fields — if no sources were verified, the field is false and the brief is labeled "unverified"); (b) include a confidence label on each factual claim ("High confidence: 3 sources confirm" vs. "Low confidence: single source, unverified date").

**What to notice:** The architecture decision is not just a technical choice — it is a user experience choice. An autonomous architecture would let the tool run for ten minutes finding every possible source; an orchestrated architecture delivers a useful brief in two minutes. The user experience requirement (useful brief, fast) drives the architecture choice, not vice versa.

---

## Tier 1 — Warm-Up (Exercises 1–8)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them. These should feel straightforward after a careful reading.*

---

**Exercise 1** *(Contrastive Classification)*

Classify each of the following AI system descriptions into one of the four intelligence patterns from the chapter. Justify each classification in one sentence.

1. A system that takes a customer email, sends it to GPT-4o, and returns the classified category and priority.
2. A system that sends a customer email to GPT-4o for sentiment analysis, then sends the result plus the original email to a second call that generates a draft response, then sends the draft to a third call that checks it for compliance.
3. A system that receives a research question, decides whether to search the web or query an internal database, executes the tool, reads the result, and decides whether to search again or compose a final answer.
4. A system with three agents — a Researcher, a Fact-Checker, and a Writer — that collaborate to produce a news article, with the Fact-Checker able to send corrections back to the Writer.

*(Tests: Four intelligence patterns — classification)*

---

**Exercise 2**

True / False, with explanation: The chapter argues that in an autonomous multi-agent architecture, individual agents make their own decisions about which tasks to pursue and how to complete them, without requiring a pre-defined task sequence.

Write one sentence explaining why the statement is true or false, using the term *orchestration* from the chapter.

*(Tests: Autonomous vs. orchestrated architecture — definition)*

---

**Exercise 3**

The chapter argues that naming — the role, goal, and backstory assigned to an agent — is "load-bearing," not cosmetic. In your own words, explain the mechanism by which an agent's name, role statement, or backstory affects its behavior. Your explanation must reference at least one example from the chapter.

*(Tests: Agent specification naming — load-bearing mechanism)*

---

**Exercise 4**

The chapter describes three failure modes specific to autonomous multi-agent architectures. Name all three, give a one-sentence definition of each, and explain the compounding error probability formula the chapter uses (0.9^n).

*(Tests: Three autonomous failure modes — compounding error, cost runaway, trust collapse)*

---

**Exercise 5**

The chapter maps archetypes to architectures — specifically, it argues that Architecture A (transparent, autonomous-looking) and Architecture B (orchestrated, competent) produce different user experiences. Describe the user experience of each architecture from the user's perspective (not the engineering perspective), and name the archetype each best expresses.

*(Tests: Architecture as brand decision — user experience and archetype fit)*

---

**Exercise 6** *(Contrastive Classification)*

For each of the following multi-agent systems, classify it as autonomous, orchestrated, or conversational. Justify each classification in one sentence.

1. Three agents — Planner, Researcher, Writer — where the Planner assigns tasks and the Researcher and Writer complete them in order without communicating with each other.
2. A customer service system where a human can redirect the AI agent to a different agent (Billing, Technical Support, Returns) in the middle of a conversation.
3. A system where a primary agent receives a business analysis request, decides to spawn additional agents for market analysis and competitor research, receives their results, evaluates whether more research is needed, and iterates until it is satisfied with the information before producing a final report.
4. A code review system where a Review Agent, a Security Agent, and a Style Agent each independently analyze the same PR, and a Synthesizer Agent combines their findings.

*(Tests: Autonomous, orchestrated, and conversational architectures — classification)*

---

**Exercise 7**

The chapter describes three anti-hallucination patterns. Name all three and explain what each pattern does — specifically, how it prevents hallucination or surfaces uncertainty to the user. Do not give examples; explain the mechanism for each pattern.

*(Tests: Anti-hallucination patterns — three mechanisms)*

---

**Exercise 8**

The chapter introduces the Madison MarketMind competitor_analyst agent from the chapter's code section. What four components does the agent specification include? For each component, explain in one sentence what it does in the agent's behavior.

*(Tests: Agent specification — four components: role, goal, backstory, tools, allow_delegation)*

---

## Tier 2 — Application (Exercises 9–16)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations. This is where most of the learning happens. Expect these to take more time than Tier 1.*

---

**Exercise 9** *(Scenario-Based Application — Intelligence Pattern Classification)*

For each of the following tools, classify the intelligence pattern and justify the classification. Then explain what would need to change about the tool to move it to the next level of complexity on the spectrum (single call → chained → ReAct → multi-agent).

1. A tool that takes a product description and returns three marketing headline options.
2. A tool that takes a topic and uses web search to find recent articles, then summarizes each article, then composes a briefing document from all summaries.
3. A tool with five agents — each handling a different stage of the sales pipeline (lead qualification, outreach drafting, follow-up scheduling, deal scoring, CRM entry) — that hand off leads from one agent to the next in a fixed sequence.
4. A tool where a primary agent decides whether to run a legal analysis or a financial analysis on an uploaded contract, calls the appropriate specialized agent, reviews the result, and decides whether the analysis is sufficient or needs supplementation.

*(Tests: Four intelligence patterns — classification and progression)*

---

**Exercise 10** *(Error Analysis)*

> The following agent specification was submitted by a student for a customer support agent.

```python
Agent(
    role="Assistant",
    goal="Help users",
    backstory="You are a helpful AI assistant.",
    tools=[search_tool, email_tool, ticket_tool],
    allow_delegation=True
)
```

1. Identify the three problems with this agent specification using the chapter's criteria.
2. Explain what behavior each problem is likely to produce — not "it will perform poorly" but the specific failure mode.
3. Rewrite the agent specification with a strong role, goal, backstory, and appropriate allow_delegation setting for a customer support agent that handles billing inquiries for a SaaS product.

*(Tests: Agent specification naming — load-bearing; allow_delegation trade-offs)*

---

**Exercise 11** *(Self-Explanation)*

The chapter argues that "architecture is a brand decision" — that choosing between autonomous and orchestrated multi-agent architectures is not just an engineering choice but a brand choice that determines the user experience the tool delivers.

Explain in your own words — without quoting the chapter — why the architecture decision is a brand decision. Your explanation must:
- Use a specific example of how the same underlying capability (e.g., competitor research) would feel different to a user depending on whether the architecture is autonomous or orchestrated
- Name the brand archetype that maps to each architecture type
- Explain why architecture-archetype misalignment would damage the brand

*(Tests: Architecture as brand decision; archetype-to-architecture mapping — self-explanation)*

---

**Exercise 12** *(Cumulative — Prior Chapter Concept)*

Chapter 5 argued that pipeline resilience requires degraded modes — pre-designed states of reduced functionality when an upstream dependency fails. Chapter 6 describes three autonomous agent failure modes: compounding error, cost runaway, and trust collapse.

For each autonomous failure mode, design a degraded mode using Chapter 5's hierarchy:
1. Which type of failure mode in Chapter 5's taxonomy does each autonomous failure correspond to? (The categories: contract violation, schema change, rate limit, authentication failure, deprecation — or if it doesn't fit, name a new category.)
2. What degraded mode is appropriate for each autonomous failure mode?
3. Is the Chapter 5 degraded mode hierarchy adequate for autonomous agent failures, or does it require new categories? Justify your answer.

*(Tests: Autonomous failure modes; degraded mode hierarchy — integrates Ch. 5 and Ch. 6)*

---

**Exercise 13** *(AI Interaction — with verification requirement)*

First, write your own answer to this question without consulting AI:
"What is the difference between a tool-using agent and a multi-agent system? When does a single agent with many tools become more architecturally complex than a multi-agent system with fewer tools?"

Then ask an AI assistant:
*"In AI systems architecture, what is the difference between a tool-using agent and a multi-agent system? In what situations should you use one vs. the other?"*

When you receive the response:
1. Identify the strongest point in the AI's response.
2. Identify the most significant omission or oversimplification. Does the AI response acknowledge the chapter's "autonomy/orchestration spectrum" framing — that the choice is not binary but involves trade-offs between transparency, cost, and reliability? If not, explain why this omission matters.
3. Write a paragraph that adds the chapter's trade-off framing to the AI's response.
4. Name one specific claim in the AI's response that would benefit from empirical verification, and describe how you would verify it.

*(Tests: Four intelligence patterns; autonomy/orchestration spectrum — AI interaction with verification)*

---

**Exercise 14** *(Failure Mode Analysis — Compounding Error)*

The chapter states that if each agent in a multi-agent system has a 90% accuracy rate, a three-agent pipeline has a 72.9% accuracy rate (0.9³ = 0.729). A team is building a six-agent system where:
- Agent 1 (Data Fetcher): 95% accuracy
- Agent 2 (Classifier): 88% accuracy
- Agent 3 (Researcher): 85% accuracy
- Agent 4 (Fact-Checker): 90% accuracy
- Agent 5 (Writer): 92% accuracy
- Agent 6 (Formatter): 98% accuracy

1. Calculate the compounded accuracy of the full pipeline.
2. Identify the highest-risk agent (the one whose accuracy improvement would most increase overall pipeline accuracy) and justify your identification.
3. Propose a specific anti-hallucination pattern from the chapter that the team could apply at the highest-risk agent to catch errors before they compound.
4. Explain why deploying the fact-checker at step 4 (after researcher) rather than step 2 (after classifier) affects the compounded error rate.

*(Tests: Compounding error failure mode; anti-hallucination patterns — quantitative analysis)*

---

**Exercise 15** *(Archetype-to-Architecture Mapping)*

The chapter describes two architectures producing different user experiences:
- Architecture A: transparent, shows reasoning steps, expressive of autonomy
- Architecture B: orchestrated, reliable, structured output, predictable

For each of the following brand archetypes, identify which architecture fits better and explain why using the chapter's archetype-to-user-experience mapping. Then propose one specific interface element (not just "Streamlit vs. Gradio" — a specific design choice at the interface level) that would reinforce the archetype-architecture alignment.

1. Sage — building a research assistant for academic writers
2. Caregiver — building a mental health journaling companion
3. Rebel — building a tool that challenges mainstream market narratives for activist investors
4. Creator — building a tool that generates variant brand voices for marketing teams

*(Tests: Archetype-to-architecture mapping; architecture as brand decision)*

---

**Exercise 16** *(Anti-Hallucination Pattern Application)*

You are reviewing an agent specification for a legal document analysis agent. The agent reads contracts and identifies potentially problematic clauses for a non-lawyer small business owner.

The agent's current output format is: a free-text paragraph explaining any concerning clauses.

Apply all three anti-hallucination patterns from the chapter:
1. **Permission to abstain:** Rewrite the agent's goal statement and output instructions to explicitly grant the agent permission to say it does not know or cannot analyze a clause.
2. **Structured output with null fields:** Design a structured output schema (as a JSON object description) that requires the agent to produce a structured analysis with null fields for information it cannot determine.
3. **Confidence labeling:** Add confidence labeling to the structured output schema, with specific criteria for what constitutes High, Medium, and Low confidence in this domain.

Then explain why the original free-text paragraph format is specifically dangerous for a legal analysis tool (hint: connect to the brand surface layer from Ch. 7 — what does a confident-sounding legal paragraph promise that the agent may not be able to deliver?).

*(Tests: Three anti-hallucination patterns applied to a real agent specification)*

---

## Tier 3 — Synthesis (Exercises 17–19)

*Bloom's Level: Synthesize / Evaluate*
*Purpose: Combine concepts from this chapter with prior chapters, or evaluate the chapter's own claims critically. These require extended reasoning. Budget 20–30 minutes each.*

---

**Exercise 17** *(Cross-Chapter Synthesis — Chs. 2 and 6)*

Chapter 2 introduced the Madison framework's five-layer architecture and described the Intelligence Layer as following the ReAct loop: Reason → Act → Observe. Chapter 6 deepens the intelligence pattern taxonomy to include single call, chained, ReAct, and multi-agent.

A student argues: "Chapter 2's Madison framework is designed around the ReAct pattern. But Chapter 6 says there are four intelligence patterns and the choice between them is an architectural decision. This means Chapter 2 is presenting one architectural choice as if it were the default. A Madison architecture could use any of the four patterns; the chapter just chose ReAct for the worked example."

Evaluate this argument:
1. Is the student correct that Chapter 2 implicitly assumes ReAct?
2. Is there a reason why the Madison framework's Intelligence Layer is specifically suited to ReAct rather than the other three patterns?
3. What would a Madison Intelligence Layer using chained calls (instead of ReAct) look like, and what would be gained and lost?

*(Tests: ReAct loop; four intelligence patterns; Madison Intelligence Layer — integrates Ch. 2 and Ch. 6)*

---

**Exercise 18** *(Cross-Chapter Synthesis — Chs. 3 and 6)*

Chapter 3 introduced the shadow failure mode: the archetype's core strength, taken too far, produces predictable failure. Chapter 6 describes three autonomous agent failure modes and one orchestrated architecture trade-off (rigidity).

Construct a parallel analysis:
1. Map each autonomous failure mode (compounding error, cost runaway, trust collapse) to a shadow failure mode from Chapter 3's archetype table. Which archetype's shadow most closely parallels each autonomous failure mode in its mechanism?
2. Map the orchestrated architecture trade-off (rigidity, hidden failures, specification cost) to an archetype shadow. Which archetype's shadow most closely parallels the orchestrated architecture's failure mode?
3. What does this parallel suggest about the relationship between architecture choice and archetype expression? Is it possible to choose an architecture that is architecturally misaligned with the brand archetype even if the archetype-to-architecture mapping from the chapter is followed correctly?

*(Tests: Autonomous failure modes; archetype shadows — integrates Ch. 3 and Ch. 6)*

---

**Exercise 19** *(Evaluation — Chapter's Own Claim)*

The chapter claims that "architecture is a brand decision" — that the choice between autonomous and orchestrated architectures is not just an engineering trade-off but a brand commitment that shapes the user experience and therefore the brand signal.

A software engineer challenges this: "Architecture is a technical decision made for technical reasons: reliability, cost, latency, maintainability. If an orchestrated architecture is more reliable and cheaper to run, you use it. If an autonomous architecture is faster to build and achieves the same output quality, you use it. The user doesn't know the architecture. They know the interface. The brand is in the interface, not in the architecture. The chapter is confusing infrastructure with product."

Evaluate this argument:
1. What is the engineer getting right?
2. What is the engineer getting wrong about the relationship between architecture and user experience?
3. Identify a specific scenario from the chapter where the architecture choice was visible to the user — where the user could tell the difference between Architecture A and Architecture B — and explain why the distinction mattered for brand.
4. What would need to be true for the engineer's claim to be correct? Under what conditions is architecture genuinely hidden from users?

*(Tests: Architecture as brand decision — stress-tests the chapter's central claim)*

---

## Tier 4 — Challenge (Exercise 20)

*Bloom's Level: Evaluate / Create*
*Purpose: Produce original analysis that extends the chapter's framework into a new domain. There is no single correct answer. Assessment is by rubric.*

*No model answer is provided for Tier 4 exercises. Assessment uses the rubric below.*

---

**Exercise 20** *(Capstone — Architecture Specification for Your AI Tool)*

Design the complete AI intelligence architecture for the tool you are building in this course. Your submission should include:

1. **Intelligence pattern classification** — classify your tool as single call, chained, ReAct, or multi-agent. Justify the classification with specific reference to what your tool does at each step.

2. **Architecture specification** — if multi-agent: specify whether autonomous, orchestrated, or conversational; justify the choice using the autonomy/orchestration trade-offs from the chapter. If single call or chained: explain why adding tool use or multi-agent coordination would not be warranted for your tool's use case.

3. **Agent specifications** — if your tool uses agents: write a full specification for each agent using the four components (role, goal, backstory, tools, allow_delegation). Each specification should follow the chapter's naming-as-load-bearing principle — the role and backstory should constrain behavior, not just describe it.

4. **Failure mode analysis** — for your specific architecture, identify which failure mode is most likely (compounding error, cost runaway, trust collapse, or orchestration rigidity). Explain why this architecture is at higher risk for that failure mode than the others.

5. **Anti-hallucination implementation** — apply at least two of the three anti-hallucination patterns to your tool's output. Show the specific implementation: for structured output, show the JSON schema; for confidence labeling, define the confidence levels for your domain; for permission to abstain, write the specific language in the agent's goal statement.

6. **Archetype-architecture alignment check** — using your archetype from Chapters 1 and 3 and the chapter's archetype-to-architecture mapping, confirm or challenge whether your architecture choice is aligned with your archetype. If misaligned, explain the trade-off you are accepting and why.

**Rubric:**

| Criterion | Strong | Adequate | Weak |
|---|---|---|---|
| Intelligence pattern justification | Classification is justified with specific reference to what the tool does at each step; alternatives are dismissed with reasons | Classification given with one-sentence justification | Classification given without justification |
| Architecture choice | Autonomous/orchestrated/conversational choice is justified using the chapter's trade-off framework; specific trade-offs named | Architecture named; one trade-off mentioned | Architecture named without trade-off analysis |
| Agent specification quality | Role and backstory are behavioral constraints, not descriptions; allow_delegation setting is justified | Role and backstory are present; allow_delegation set but not justified | Generic role ("assistant") and backstory ("helpful AI") |
| Failure mode identification | Most-likely failure mode identified with mechanism; architecture-specific explanation (not generic) | Failure mode identified without mechanism | Generic "the AI might make mistakes" without naming the specific failure mode |
| Anti-hallucination implementation | Two or more patterns applied with specific implementation shown; patterns match the failure risks identified | Two patterns applied without full implementation detail | One pattern named without implementation |
| Archetype-architecture alignment | Alignment confirmed or challenged with specific reasoning; misalignment trade-offs named explicitly | Alignment addressed but reasoning is generic | Archetype not connected to architecture choice |

---

## Answer Key

> Attempt all exercises before reading this section.

---

**Exercise 1**
*Model answer:*
1. Single LLM call — one input, one LLM call, one output; no iteration, no tools, no multiple calls
2. Chained LLM calls — the output of each call becomes input for the next; three sequential calls, but no tool use and no agent-level decision-making about whether to continue
3. Tool-using agent (ReAct) — the agent reasons about which tool to use, acts by calling the tool, observes the result, and decides whether to continue iterating. The "decides whether to search again" is the key ReAct signal.
4. Multi-agent system — three or more agents with defined roles, capable of communicating with each other; the feedback loop (Fact-Checker → Writer) and the distinct role separation are the multi-agent signals
*Common error:* Students classify item 2 as a tool-using agent because it involves multiple steps. The distinction: chained calls have a pre-defined sequence; the ReAct pattern requires the agent to make a decision about whether to call a tool and which tool to call, based on observing prior results.
*Chapter reference:* Four intelligence patterns — Ch. 6

---

**Exercise 2**
*Answer:* True (with qualification)
*Model answer:* In autonomous multi-agent architectures, agents do make their own decisions about what tasks to pursue — the defining characteristic is that the orchestrator does not pre-define the sequence of steps. However, the chapter clarifies that "autonomous" refers to the absence of a fixed task sequence, not the absence of any constraints — agents still operate within their role and goal specifications. In orchestrated architectures, by contrast, the task sequence is pre-defined and agents execute assigned steps rather than deciding independently.
*Common error:* Students answer True without the qualification — treating autonomous as "fully unconstrained." The chapter's distinction is task-sequence autonomy, not specification-level autonomy. Agents in autonomous systems are still governed by role, goal, and backstory.
*Chapter reference:* Autonomous vs. orchestrated architecture — Ch. 6

---

**Exercise 3**
*Model answer:* The mechanism is that the role, goal, and backstory provide the LLM with the contextual frame it uses to interpret ambiguous instructions and make decisions at ambiguity boundaries. When an agent faces a choice not explicitly specified (which source to prioritize, how much detail to include, how to handle a conflicting result), it resolves the ambiguity by asking, implicitly, "what would an agent with this role and backstory do?" The chapter's example: a `competitor_analyst` agent with a backstory that references financial market analysis will interpret ambiguous competitive intelligence through a financial lens; the same agent with a backstory referencing consumer brand analysis will interpret the same input differently. The name is not cosmetic because LLM behavior at decision boundaries is constrained by the in-context specification.
*Common error:* Students say "the agent follows the instructions" — which is true but not the mechanism. The mechanism is that the naming affects behavior at *ambiguity boundaries* — the cases where no explicit instruction applies. Generic role descriptions ("helpful assistant") provide no constraint at ambiguity boundaries; specific role descriptions ("competitive intelligence analyst with a focus on startup funding rounds") provide significant constraint.
*Chapter reference:* Agent specification naming — load-bearing — Ch. 6

---

**Exercise 4**
*Model answer:*
1. Compounding error — each agent in a pipeline may make a small error; errors compound multiplicatively across agents. If each agent has 90% accuracy, three agents produce 0.9 × 0.9 × 0.9 = 0.729 accuracy (72.9%). The final output is built on layers of small errors that the final agent cannot detect because it does not know which of its inputs were wrong.
2. Cost runaway — autonomous agents can iterate indefinitely when they judge the current state insufficient. Without a token budget or step limit, an agent that "keeps looking for more information" can consume hundreds of API calls before producing output. The cost is invisible until the API bill arrives.
3. Trust collapse — when an autonomous agent produces visible errors (especially in a domain where users can verify accuracy), users lose trust not just in the specific output but in the system as a whole. Trust is rebuilt slowly; a single visible error can trigger permanent user departure.
Formula: 0.9^n. For n = 3 agents, 0.9³ = 0.729. For n = 5 agents, 0.9⁵ = 0.590. The probability compounds downward with each additional agent.
*Common error:* Students describe compounding error only qualitatively without using the formula. The formula is the chapter's central quantitative contribution to this section — it makes the risk concrete.
*Chapter reference:* Three autonomous failure modes; 0.9^n formula — Ch. 6

---

**Exercise 5**
*Model answer:*
Architecture A (transparent/autonomous): the user sees the system's reasoning process — intermediate steps, web search queries, reasoning traces. The user experience is expressive: "the system is working through this the way I would." This matches the Rebel archetype — transparent, showing its work, willing to let the user see the reasoning rather than just the conclusion. It also matches Creator — the user can see the process of creation, not just the output.
Architecture B (orchestrated/competent): the user submits a query and receives a structured, reliable result. The system's internal steps are invisible. The user experience is authoritative: "the system knows what it's doing and delivers." This matches the Sage archetype — competent, trustworthy, presenting conclusions rather than working notes — and the Ruler archetype, which prioritizes reliability and consistency.
*Common error:* Students describe Architecture A as "better for power users" and Architecture B as "better for casual users" — a capability framing rather than an archetype framing. The chapter's point is that the architecture choice encodes a brand promise, not a user sophistication segmentation.
*Chapter reference:* Architecture A/B user experiences; archetype-to-architecture mapping — Ch. 6

---

**Exercise 6**
*Model answer:*
1. Orchestrated — the Planner pre-defines the task sequence and assigns tasks; agents execute assigned tasks in order without peer communication
2. Conversational — a human can redirect between agents mid-conversation; the interaction model is dialogue-based with human agency over routing
3. Autonomous — the primary agent makes its own decisions about what to research, whether to iterate, and when it is satisfied; no pre-defined sequence
4. Orchestrated — four agents each perform a fixed, pre-defined analysis; a Synthesizer agent aggregates. The sequence is pre-defined (all four analyze, Synthesizer combines); no agent decides what to investigate next
*Common error:* Students classify item 4 as autonomous because the agents seem to "decide" what to analyze. The distinction: in orchestrated systems, the scope of each agent's task is fixed by the system design; in autonomous systems, agents decide the scope themselves. The four agents in item 4 each have a fixed, pre-defined scope.
*Chapter reference:* Autonomous, orchestrated, conversational architectures — Ch. 6

---

**Exercise 7**
*Model answer:*
1. Permission to abstain — the agent's goal specification explicitly grants it permission to say it does not know, cannot determine, or is uncertain. This prevents the default LLM behavior (producing a confident-sounding answer regardless of actual knowledge) by making abstention an explicitly sanctioned response.
2. Structured output with null fields — the agent is required to produce a structured JSON or typed output where fields can be null when the agent cannot determine a value. This makes uncertainty visible in the data structure rather than hiding it in fluent prose that sounds certain.
3. Confidence labeling — each claim or output field is accompanied by a confidence level (High, Medium, Low, or a numeric score). This surfaces uncertainty to the user at the claim level, rather than leaving the user to infer confidence from the text.
*Common error:* Students describe anti-hallucination as "fact-checking" — asking the model to verify its own outputs. The chapter's patterns are distinct: they prevent confident-sounding hallucination from reaching the user by structuring the output to surface uncertainty, not by asking the model to self-verify.
*Chapter reference:* Three anti-hallucination patterns — Ch. 6

---

**Exercise 8**
*Model answer:* The Madison MarketMind competitor_analyst agent specification includes:
1. **role** — defines the agent's functional identity within the multi-agent system; shapes how the agent interprets its tasks relative to other agents
2. **goal** — specifies the measurable objective the agent is trying to achieve; constrains what counts as "done" for this agent
3. **backstory** — provides the contextual frame the agent uses to interpret ambiguous situations; this is the load-bearing component that constrains behavior at decision boundaries
4. **tools** — the external capabilities the agent can invoke (search, scraping, API calls); defines the action space available to the agent
5. **allow_delegation** — boolean that controls whether the agent can spawn or task subordinate agents; set to False prevents unauthorized scope expansion into multi-agent behavior
*Common error:* Students omit allow_delegation or treat it as a minor technical setting. The chapter's argument is that allow_delegation=True is a significant architectural decision — it enables the agent to expand the scope of the system dynamically, which enables cost runaway.
*Chapter reference:* Madison MarketMind agent specification — Ch. 6

---

**Exercises 9–16**
*Tier 2 — evaluation criteria (abbreviated):*
- Ex 9: Each tool classified correctly; upgrade path named (what specific capability addition moves it up the spectrum)
- Ex 10: Three problems: generic role (no behavioral constraint), generic goal ("help users" is not measurable), generic backstory (no domain context); allow_delegation=True for a billing agent enables scope expansion — should be False; rewritten spec has specific role (Billing Support Specialist), specific goal (resolve billing inquiry in one interaction), domain-specific backstory
- Ex 11: Autonomous → transparent process visible → user experiences uncertainty or serendipity → Rebel/Creator; Orchestrated → hidden steps → reliable structured output → Sage/Ruler; misalignment example named with mechanism
- Ex 12: Compounding error ≈ contract violation (each agent relies on prior agent's output as a "contract"); cost runaway ≈ no rate limit / no circuit breaker; trust collapse ≈ a brand damage pattern that has no exact Ch. 5 equivalent (new category: "visible output quality failure"); degraded mode for each named
- Ex 13: AI response likely covers tool-use, agent coordination, task decomposition; omission test: does it cover autonomy/orchestration spectrum trade-offs? Addition paragraph should name the three failure modes and explain that multi-agent systems are not just "more powerful" — they introduce compounding risk
- Ex 14: 0.95 × 0.88 × 0.85 × 0.90 × 0.92 × 0.98 = 0.549 (approximately 54.9%); highest-risk agent = Agent 3 (Researcher, 85% — the multiplicative impact of improving 85% to 90% is larger than improving 98% to 99%); anti-hallucination pattern: structured output at Agent 3 output with null fields for unverifiable claims; Fact-Checker at step 4 catches errors from Agent 3 but not from Agents 1-2; moving it to step 2 would catch Agent 1 errors earlier in the chain
- Ex 15: Sage/Architecture B (structured, reliable, hidden steps) → interface: each output section has a source citation; Caregiver/Architecture B (predictable, gentle) → interface: each response ends with an optional "would you like to explore this more?" prompt; Rebel/Architecture A (transparent) → interface: reasoning trace is visible and collapsible; Creator/Architecture A (process visible) → interface: intermediate drafts are shown alongside final output
- Ex 16: Permission to abstain goal statement: "Analyze the contract for potentially problematic clauses. If a clause is beyond your legal analysis capability or requires jurisdiction-specific expertise you do not have, say so explicitly — do not infer a legal conclusion from insufficient information." Structured output: `{clause_text, concern_type, confidence, jurisdiction_note, recommendation, abstain_reason}` where abstain_reason is populated when the agent cannot analyze the clause. Confidence levels: High = clause language is standard and concern is documented in legal literature; Medium = concern likely but depends on jurisdiction; Low = flagging for human review, not a legal conclusion. Danger of free-text: a confident legal paragraph implies legal expertise; if wrong, it is confidence misalignment (Ch. 7 concept) in a domain with legal liability.

---

**Exercises 17–19**
*Tier 3 — No abbreviated model answer. Evaluation criteria:*
- Ex 17: Student is partially right (Ch. 2 does present ReAct as the default for the Intelligence Layer); justify why ReAct is specifically suited (needs tool use for research, web access, API calls — single call or chained cannot do this); chained Madison Intelligence Layer would mean fixed research steps rather than dynamic tool selection — gains predictability, loses adaptability to novel queries
- Ex 18: Compounding error ~ Sage's dogmatism (the system's prior outputs are treated as authoritative input for the next step, without questioning); cost runaway ~ Magician's shadow (the agent pursues transformation indefinitely, unable to stop); trust collapse ~ no direct archetype parallel, but most closely resembles the consequence of any archetype drifting into shadow (the recognition asset collapses when a visible failure breaks the pattern); orchestration rigidity ~ Ruler's shadow (order enforced so tightly that flexibility disappears)
- Ex 19: Engineer is right that users often cannot perceive the architecture; engineer is wrong about the user experience difference (Architecture A's visible reasoning is experientially different from Architecture B's clean output — user CAN tell the difference at the interface level); specific scenario: the comparison of Cursor (architecture visible, reasoning shown) vs. Devin (autonomous, black-box) in Ch. 2 — users treated the two very differently; conditions for engineer's claim to be correct: architecture is completely hidden behind a polished interface, outputs are identical in quality and presentation, no failure mode produces architecture-visible behavior

---

**Exercise 20**
*Tier 4 — No model answer. Assessment by rubric in the exercise.*

---

## Self-Assessment Rubric

After reviewing the answer key, evaluate your work:

| Score | Meaning | Next step |
|---|---|---|
| Tier 1: 6–8 correct | Core vocabulary in place | Move to Tier 2 |
| Tier 1: 4–5 correct | Gaps in foundational concepts | Return to intelligence patterns and failure modes sections before Tier 2 |
| Tier 2: 6–8 mostly correct | Applying framework well | Attempt Tier 3 |
| Tier 2: 4–5 mostly correct | Gaps in application | Redo Ex 9 and Ex 14 with answer key; re-attempt others |
| Tier 3: 2–3 strong | Synthesis developing | Proceed to Tier 4 |
| Tier 3: 0–1 strong | Integration needs work | Re-read Ch. 2 and Ch. 3 connection points |

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

*Ex 3 (Naming as load-bearing):* The key insight students miss is that load-bearing naming matters specifically at *ambiguity boundaries* — where no explicit instruction applies. Generic names fail because they give the LLM no constraint when the situation is ambiguous. This is worth extended discussion in class.

*Ex 4 (Failure modes with formula):* Require students to calculate 0.9^n for at least one value. The formula makes the compounding error risk concrete in a way that qualitative description does not. Students who describe compounding error without using the formula are giving an incomplete answer.

*Ex 10 (Error analysis — agent specification):* The three errors are: generic role, generic goal, generic backstory. Allow_delegation=True is a fourth issue that strong students should catch. The backstory error is the most important — students often write descriptive backstories ("you are an expert in X") when behavioral backstories ("you have seen 10,000 billing disputes and you know that most misunderstandings come from...") are what constrains behavior.

*Ex 14 (Compounding error quantitative):* The arithmetic is straightforward; the interesting question is which agent to improve. Students often say "improve the worst agent" without considering the multiplicative impact. Agent 3 (85%) is the highest-leverage target because improving it from 85% to 90% multiplies the improvement across the full pipeline.

*Ex 16 (Anti-hallucination in legal domain):* This exercise connects to Ch. 7's confidence misalignment concept. Students should independently make this connection — if they do not, use it as a teaching moment: the chapter's "confidence misalignment" is exactly what a free-text legal paragraph produces when the system is uncertain.

*Ex 19 (Evaluation):* This is the most contested Tier 3 exercise — the engineer's argument has real merit. The chapter's claim is strongest when architecture produces visible differences in user experience (Architecture A vs. B comparison). The claim is weakest when the architecture is fully hidden behind a polished interface. Strong student responses will acknowledge this conditionality.

**Common errors to watch for:**
- Classifying chained calls as ReAct (the key distinction: ReAct requires the agent to decide whether to call a tool and which tool, based on observations — chained calls have a pre-defined sequence)
- Treating "allow_delegation=True" as a neutral technical setting rather than an architectural scope-expansion decision
- Describing anti-hallucination as "fact-checking" rather than as uncertainty-surfacing design patterns
- Disconnecting architecture choice from archetype expression — treating the two as separate decisions

**DEI note:**
The chapter's cases (Cursor, Devin, CrewAI) are drawn from the North American AI tools ecosystem. For students with different industry context, the intelligence pattern taxonomy and failure mode framework apply universally — encourage substitution of local or domain-relevant examples in Tier 3 exercises.
