# Chapter Quiz: AI Intelligence and Multi-Agent Systems

*Chapter 6 of Branding and AI (INFO 7375)*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- LO 1 — Distinguish the four patterns of AI intelligence and explain what each trades away to get what it gains.
- LO 3 — Write a complete agent specification — role, goal, backstory, tools, and anti-hallucination guards.
- LO 4 — Explain why the autonomy/orchestration choice is a brand decision.
- LO 5 — Diagnose the three failure modes of autonomous agents and design a mitigation.

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

In the chapter's four-pattern taxonomy of AI intelligence, what distinguishes Pattern 3 (tool-using agent) from Pattern 2 (chained calls) in terms of who controls the flow?

A) In Pattern 3, a deterministic workflow graph decides the order of operations; in Pattern 2, the LLM decides
B) In Pattern 3, the LLM reasons about what to do next and controls the loop; in Pattern 2, a workflow (e.g., n8n) decides the order of LLM calls
C) In Pattern 3, multiple specialized LLMs are coordinated by an orchestrator; in Pattern 2, a single LLM handles all steps

---

**Question 2** *(Multiple-Choice)*

In the Madison `competitor_analyst` agent specification, what is the architectural significance of setting `allow_delegation=False`?

A) It prevents the agent from calling external APIs, limiting it to in-context reasoning only
B) It restricts the agent from spawning sub-agents or redirecting work — the orchestration layer decides what happens next, not the agent
C) It forces the agent to produce structured JSON output rather than free-text responses

---

**Question 3** *(True/False)*

According to the chapter, the three-component agent specification — role, goal, and backstory — are cosmetic labels that help developers organize their code but do not materially affect LLM behavior.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

What is the mechanism behind "compounding error" — the first failure mode of autonomous agents described in the chapter?

A) The agent's API calls accumulate charges without a cost ceiling, causing the pipeline to run over budget
B) Each step is conditioned on the previous step; if step N−1 was wrong, step N is built on a false foundation, and errors multiply across the chain
C) The agent's reasoning trace is visible to the user, compounding trust damage as the user watches each mistake in real time

---

**Question 5** *(True/False)*

The chapter argues that Architecture A (transparent reasoning trace) is universally superior to Architecture B (orchestrated, opaque delivery) because transparency builds user trust in all contexts.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student builds an autonomous research agent to summarize ten academic papers on a given topic. The agent is given no step ceiling and no cost limit. In a test run, the agent completes step 12 of an estimated 20-step task but has made a factual error at step 5 — it misidentified which study used which methodology. Steps 6–12 use the misattribution as established fact. The agent's step 12 output is a confident, well-written paragraph containing the error. Which failure mode does this scenario exemplify, and what structural mitigation would address it?

A) Cost runaway — the mitigation is a hard step ceiling that stops the agent before it writes the paragraph
B) Compounding error — the mitigation is a validation step inserted between key stages that checks output against the source material before proceeding
C) Trust collapse — the mitigation is making the reasoning trace invisible so users do not see the intermediate steps

---

**Question 7** *(Short-Answer)*

The chapter introduces three anti-hallucination patterns in order of increasing strength: permission to abstain, structured output with null fields, and confidence labeling. The Madison `competitor_analyst` agent uses a variant of the second pattern. What specific instruction in the `competitor_analyst`'s goal field implements this pattern, and what does it prevent?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

The chapter maps archetypes to architecture tendencies. The Explorer archetype's shadow is "aimlessness — no destination, no coherent result." The chapter cites AutoGPT as an example of an Explorer brand with an unmanaged shadow. Why does the chapter treat Architecture A (autonomous, transparent) as a high-risk choice specifically for an Explorer-branded tool?

A) Explorer tools have higher user expectations for visual polish, and Architecture A's exposed reasoning trace looks unfinished
B) The autonomy in Architecture A feels on-brand for Explorer, but the Explorer's shadow — an agent that explores forever without delivering — is exactly what an unconstrained autonomous agent does
C) Explorer tools typically serve technically unsophisticated users who prefer Architecture B's simpler interface

---

**Question 9** *(Short-Answer)*

The chapter's "Climate Technology Research Analyst" agent specification includes the backstory phrase: "Never rounds up." Explain what work this phrase is doing in the specification and why it is placed in the backstory rather than the goal.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter argues: "The hardest design decision in any agentic system is not which model to use — it is where the AI decides and where it does not." A student counters: "In 2026, the model choice matters more than architecture. GPT-4o versus Claude 3.5 Sonnet versus Gemini 1.5 Pro can mean the difference between a usable and an unusable product. Architecture is secondary." Evaluate this argument. Does it challenge the chapter's central claim, or does it address a different question?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

A legal tech startup builds an AI tool that reviews contracts for compliance violations. The tool is designed for corporate attorneys reviewing high-stakes M&A documents. The founding team is debating between Architecture A (attorney watches the AI reason through each clause in real time, can redirect at any point) and Architecture B (attorney submits a contract, AI runs five specialized agents, delivers a structured compliance report). Using the chapter's archetype-architecture mapping and brand-experience analysis, recommend an architecture and justify it. Name the failure mode your chosen architecture introduces and describe one mitigation.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter states that in Pattern 2 (chained calls), the workflow decides the order and the sequence is "deterministic — n8n decides the order." In Pattern 3, "the LLM reasons about what to do, calls a tool, observes the result, reasons again, and decides whether to call another tool or produce a final answer. The loop is controlled by the LLM, not by a workflow graph."
*Why the distractors are wrong:*
- A) This reverses the description — Pattern 2 (chained) uses a deterministic workflow; Pattern 3 (tool-using) has the LLM control the loop.
- C) Multiple specialized LLMs coordinated by an orchestrator describes Pattern 4 (multi-agent system), not Pattern 3.
*Chapter reference:* Part I, Sections 1.1 — Pattern 2 and Pattern 3

---

**Q2 — B**
*Correct because:* The chapter states: "`allow_delegation=False` is the orchestration commitment in code. This agent cannot hand off to other agents. It does its job and returns. The orchestration layer — not the agent — decides what happens next. This single parameter is the architectural choice that separates Madison's approach from AutoGPT's. AutoGPT agents could spawn sub-agents, set new goals, redirect their own work. Madison agents cannot."
*Why the distractors are wrong:*
- A) `allow_delegation` is about spawning sub-agents and redirecting work, not about API access; the tools list controls what external calls the agent can make.
- C) The structured JSON output requirement is encoded in the goal field, not via `allow_delegation`.
*Chapter reference:* Part III, Section 3.3 — Madison's MarketMind agents

---

**Q3 — False**
*Correct because:* The chapter explicitly argues the opposite: "The naming convention is load-bearing." It states: "These titles act as activation prompts. The LLM has training data that associates 'Competitive Intelligence Analyst' with specific behaviors: sourcing claims, noting uncertainty, producing structured comparisons. The role primes that behavior. The goal and backstory narrow it further. Together they form a specification that is far more reliable than an equivalent system-prompt paragraph, because the LLM recognizes the professional frame and applies it consistently."
*Chapter reference:* Part I, Section 1.3 — The naming convention is load-bearing

---

**Q4 — B**
*Correct because:* The chapter's definition of compounding error is: "An autonomous agent's step N is conditioned on step N−1. If step N−1 was wrong... then step N is built on a false foundation." The chapter's mathematical illustration reinforces this: "A 10% error rate at each step means that after ten steps, the probability of an error-free chain is 0.9^10 ≈ 35%... Errors compound geometrically."
*Why the distractors are wrong:*
- A) This describes cost runaway — the second failure mode — not compounding error.
- C) The visible reasoning trace causing trust damage describes trust collapse — the third failure mode — and the mechanism involves user observation, not error multiplication.
*Chapter reference:* Part III, Section 3.1 — Failure Mode 1: Compounding error

---

**Q5 — False**
*Correct because:* The chapter explicitly states: "Neither architecture is universally correct. A research-collaboration tool benefits from Architecture A — the user wants to be in the loop, to redirect the agent, to feel the collaboration happening. An enterprise reporting tool benefits from Architecture B — the user wants a deliverable, not a process. The choice is the brand decision." The chapter identifies Architecture A's transparency as both a high-trust asset and a liability — when failure is visible, the brand damage is equally visible.
*Chapter reference:* Part II, Section 2.1 — The same capability, felt differently

---

**Q6 — B**
*Correct because:* The scenario exactly matches the chapter's description of compounding error: a wrong answer at an early step (step 5, misattributed methodology) becomes the foundation for all subsequent steps (6–12), and the final output is confidently wrong. The chapter's stated mitigation for compounding error is the orchestrated-system's inserted validation steps: "A chained or orchestrated system can insert validation steps between each LLM call, checking that the output meets a structural requirement before passing it to the next step."
*Why the distractors are wrong:*
- A) A step ceiling would stop the agent earlier but would not address the root cause (the unchecked error at step 5) — the paragraph might be written by step 8 with the same error.
- C) Making the reasoning trace invisible addresses trust collapse visibility, not the actual error propagation.
*Chapter reference:* Part III, Section 3.1 — Failure Mode 1: Compounding error

---

**Q7 — Short-Answer**
*Model answer:* The specific instruction in the `competitor_analyst`'s goal that implements the null-field pattern is: "If you cannot verify a data point, set it null and explain limitations." This prevents hallucination by giving the agent explicit permission and instruction to leave fields empty when it lacks verified information, rather than filling them with fabricated but plausible-sounding data. The chapter notes this is an "anti-hallucination instruction built directly into the agent's specification" — placed inside the goal rather than as a separate validation step, so the agent applies the constraint before generating output rather than after.
*Common error:* Citing the backstory phrase "Prefers evidence and transparency over guessing" instead of the specific null-field instruction in the goal — both are anti-hallucination elements, but the null-field instruction is the structured-output implementation.
*Chapter reference:* Part III, Section 3.3 — Madison's MarketMind agents

---

**Q8 — B**
*Correct because:* The chapter states: "An Explorer tool is a high-risk candidate for Architecture A: the autonomy feels on-brand, but the shadow failure (the agent that explores forever and delivers nothing) is the Explorer's shadow in literal form. AutoGPT was, implicitly, an Explorer brand with an unmanaged shadow." The chapter's definition of the Explorer's shadow is "aimlessness — perpetual searching that never commits." An autonomous agent with no step ceiling or goal-convergence check is structurally the same as an Explorer operating in shadow mode.
*Why the distractors are wrong:*
- A) The chapter does not frame Architecture A's exposed trace as looking unfinished; it frames it as a user-experience choice (collaborative vs. competent) with brand implications.
- C) The chapter does not associate Explorer tools with unsophisticated users; it focuses on the architectural shadow risk.
*Chapter reference:* Part II, Section 2.2 — Mapping architecture to archetype

---

**Q9 — Short-Answer**
*Model answer:* "Never rounds up" is a tie-breaker principle for edge cases that the goal cannot fully enumerate. The chapter explains that the backstory "is the tie-breaker for edge cases the goal did not anticipate" — it provides the LLM with a principle for resolving ambiguous situations where the goal's specific instructions do not apply. Placed in the backstory (rather than the goal), it functions as a meta-rule: whenever the agent faces any tradeoff between a complete-looking answer and an honest incomplete one, honesty wins. The goal encodes what to do; the backstory encodes what kind of agent this is when the goal doesn't cover the situation.
*What a strong answer includes:*
- The backstory's function as a tie-breaker for unanticipated edge cases
- The distinction between goal (specific task instructions) and backstory (meta-principle for ambiguous situations)
- The Sage-archetype connection: "never rounds up" directly addresses the Sage shadow (dogmatism / overconfidence)
*Chapter reference:* Part IV, Section 4.3 — A worked specification

---

**Q10 — Brief-Response**
*Model answer:* The student's argument is correct that model choice matters but misidentifies what it determines — it addresses capability (whether the model can do the task at all) rather than reliability, debuggability, and cost-predictability (whether the system behaves consistently in production). The chapter's claim is not that model choice is irrelevant but that architecture determines *where failures happen and how they are handled*. A more capable model running in an autonomous pattern with no validation steps still fails via compounding error; a less capable model in an orchestrated pattern with validation steps fails locally and visibly. The two questions — which model? and where does the AI decide? — are orthogonal. The chapter's claim is that students tend to over-invest in model selection and under-invest in the architectural boundary between AI judgment and deterministic control.
*What a strong answer includes:*
- Acknowledgment that model capability is real and relevant
- The distinction between capability (model question) and reliability/debuggability (architecture question)
- The orthogonality argument: a better model in a bad architecture still has bad reliability
*Chapter reference:* The chapter's TL;DR and Summary — "it is not about which model to use"

---

**Q11 — Transfer Brief-Response**
*Model answer:* Architecture B (orchestrated, opaque delivery with structured compliance report) is the appropriate choice for corporate attorneys reviewing M&A documents. The chapter maps Ruler-archetype tools (authority, order, reliability) to Architecture B — attorneys reviewing high-stakes documents need a competent, trustworthy deliverable, not a collaborative exploration. The archetype for a contract compliance tool is closer to Sage or Ruler: authoritative, reliable, evidence-first. Architecture A's visible reasoning trace creates a trust-collapse risk: if the attorney watches the AI reason through a clause incorrectly in real time, the visible failure is more damaging in a high-stakes legal context than in a research-collaboration context. The primary failure mode Architecture B introduces is hidden failure — a wrong compliance finding delivered confidently, with no visible reasoning trace to help the attorney catch it. The mitigation is the chapter's null-field anti-hallucination pattern: each compliance flag should include a confidence level (verified / inferred / unverifiable) and a source citation, so the attorney knows which findings require independent verification.
*What a strong answer includes:*
- Architecture B recommendation with a brand/archetype justification
- Named failure mode for the chosen architecture (hidden failure for orchestrated systems)
- A specific mitigation grounded in the chapter's anti-hallucination patterns
*Chapter reference:* Part II, Section 2.1 (architecture as brand experience); Part IV, Section 4.2 (anti-hallucination patterns)

---

## Self-Assessment Rubric

After reviewing the answer key, score yourself:

| Score | Meaning | Next step |
|---|---|---|
| 9–10 / 10 (or equivalent) | Strong retention — ready to move on | Proceed to the next chapter |
| 7–8 / 10 | Partial mastery — specific gaps present | Return to the sections flagged in wrong answers |
| 5–6 / 10 | Foundational gaps | Reread the chapter, then retake the quiz |
| Below 5 / 10 | Chapter concepts not yet consolidated | Reread, then work through the worked exercises before retaking |

*Note: Section 3 questions are weighted more heavily. Getting Q10 and Q11 wrong while getting Sections 1–2 right is a signal of surface-level knowledge — not mastery.*

---

## Instructor Notes

**Bloom's distribution for this quiz:**

| Level | Questions | % of Quiz |
|---|---|---|
| Remember / Understand | Q1–Q5 | ~45% |
| Apply / Analyze | Q6–Q9 | ~36% |
| Evaluate / Create | Q10–Q11 | ~18% |

**Psychometric targets:**
- Section 1 items: p-value target 0.77–0.85; r_pb >= 0.30
- Section 2 items: p-value target 0.50–0.70; r_pb >= 0.30
- Section 3 items: p-value target 0.30–0.50; r_pb >= 0.40

**Common errors to watch for in student work:**

- Conflating the three failure modes — particularly confusing "compounding error" (step-chain accumulation) with "trust collapse" (user experience of visible failure). Q4 and Q6 both probe this distinction.
- Treating `allow_delegation=False` as a tool-access restriction rather than a flow-control commitment. Q2 targets this specifically.
- Believing Architecture A is universally better because transparency sounds like a virtue — Q5 directly targets this.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name all four AI intelligence patterns in order from simplest to most complex.
- Cannot describe the mechanism of compounding error using the chapter's mathematical illustration (0.9^n).

**Scaffolding adjustments:**

- *For students who score below 5:* Return to Part I (four patterns) and Part III (three failure modes). Read the Madison `competitor_analyst` code annotation carefully — it is the chapter's most concrete artifact and Q2 and Q7 both depend on understanding it.
- *For students who score 10/10 on first attempt:* Attempt Exercise C2 (the 2027 architecture challenge) — it requires predicting how the autonomy/orchestration trade-off changes if autonomous agents achieve parity on production-reliability metrics.

**Grading weight guidance (if used for credit):**
- Section 1 MCQ items: 0.25–0.5% of final course grade each
- Section 2 Short-Answer items: 0.5–1.0% each
- Section 3 Brief-Response items: up to 2.5% each
- Collectively, chapter quizzes should not exceed 5% of overall course grade
