# Chapter Quiz: The Madison Framework

*Chapter 2 of Branding and AI (INFO 7375)*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- LO 1 — Define the word *agent* with precision, distinguishing between four common usages.
- LO 2 — Describe Madison's five-layer architecture and explain what each layer does, what it takes as input, and what it produces as output.
- LO 3 — Trace the ReAct loop (reason → act → observe) through at least one Madison layer and explain why this pattern outperforms either pure reasoning or pure tool-use.
- LO 4 — Explain why layered architectures are also brand decisions.
- LO 5 — Compare graph-based orchestration against conversation-based orchestration on the dimension of production reliability.

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

In the chapter's four-meaning taxonomy, which definition of "agent" does the Madison framework use?

A) Agent as a single LLM call that returns a result
B) Agent as a long-running autonomous system that plans and executes without human intervention
C) Agent as a specialized role in a larger pipeline with defined inputs and outputs

---

**Question 2** *(Multiple-Choice)*

According to the chapter, what is the primary trade-off between graph-based orchestration (n8n, LangGraph) and conversation-based orchestration (AutoGen)?

A) Graph-based systems handle more complex tasks; conversation-based systems are limited to simpler queries
B) Graph-based orchestration offers predictability and auditability; conversation-based orchestration offers flexibility for novel task sequences
C) Conversation-based orchestration is cheaper to run because agents share context through dialogue instead of structured data contracts

---

**Question 3** *(True/False)*

The ReAct loop pattern requires an LLM to complete all reasoning steps before taking any action, ensuring the plan is coherent before execution begins.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

The chapter names three consequences of designing Madison as a single mega-agent instead of five specialized layers. Which of the following is one of those three?

A) The mega-agent would require a more expensive model license
B) Failure modes blur — when the system produces a wrong answer, the fault cannot be located
C) The mega-agent cannot process natural language inputs from multiple data sources simultaneously

---

**Question 5** *(True/False)*

According to the chapter, Madison's choice of five named layers is purely an engineering decision; its brand implications are secondary and unintentional.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A marketing team using Madison reports that their daily dashboard is showing inflated sentiment scores for a competitor brand — positive sentiment is being counted twice because the same story appears in multiple news feeds. The orchestration layer has already fired and the Performance layer has logged the run as successful. A team member says, "We need to fix the model." A second team member says, "We need to fix the Intelligence Agent's deduplication step." Which team member is applying the chapter's failure-isolation argument correctly, and why?

A) The first team member, because the root cause is the LLM's tendency to over-weight positive tokens in its scoring prompt
B) The second team member, because layered architectures allow fault localization to a named layer — the deduplication logic sits inside the Intelligence Agent, not in the model
C) Neither, because the Performance Agent's success log means the error originated in the orchestration layer's data routing

---

**Question 7** *(Short-Answer)*

The chapter distinguishes Cursor and Devin as products using "the same underlying technology stack" but different architectural commitments. What specific term does the chapter use to describe the dimension along which they differ, and how does each product position itself on that dimension?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

In the Madison Intelligence Agent's ReAct trace shown in the chapter, why does the agent run MD5 hash deduplication before sending articles to the LLM for sentiment scoring?

A) MD5 hashing is required by the Google News API before results can be stored in a Google Sheet
B) Deduplicating first reduces the number of LLM calls needed, lowering token costs and preventing the same story from inflating sentiment scores
C) The chapter recommends MD5 hashing as a security measure to protect brand data before it enters the LLM context

---

**Question 9** *(Short-Answer)*

The chapter states: "Where you place humans in your own pipeline is not a philosophical question — it is a risk-engineering question." Explain what criterion the chapter gives for deciding where human review points should be placed in a multi-agent system.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter claims that "architecture is brand" — that the five-layer decomposition of Madison is simultaneously an engineering decision and a brand decision, because it creates product surfaces customers can name, trust, and buy. A product manager argues: "That's backwards. The brand team decides what surfaces customers interact with, and the engineers build whatever architecture supports those surfaces. Architecture follows brand, not the other way around." Evaluate this argument. Does it succeed as a challenge to the chapter's claim, or does the chapter's account describe a different phenomenon?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

A hospital builds a clinical workflow automation system with three AI-powered layers: a Triage layer (classifies incoming patient requests by urgency), a Routing layer (matches requests to the right department or provider), and a Documentation layer (generates draft clinical notes). The system was designed for technical reasons — to isolate failure modes and reduce redundant LLM calls. Apply the chapter's "architecture is brand" argument to this system. What brand consequences does the three-layer structure produce, and what would a mega-agent version of the same system cost the hospital in terms of customer trust and product legibility?

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — C**
*Correct because:* The chapter explicitly states that Madison uses "meaning 4" — agent as a specialized role in a larger system, "a named component with defined inputs and outputs, optimized for a particular kind of work, coordinated by an orchestration layer." The chapter contrasts this with meaning 3 (autonomous systems like Devin) and meaning 1 (single LLM calls).
*Why the distractors are wrong:*
- A) A single LLM call (meaning 1) is how the chapter describes a prompt-and-response function, not Madison's architecture.
- B) Long-running autonomous systems (meaning 3) describe Devin, which the chapter explicitly contrasts with Madison's orchestrated-pipeline approach.
*Chapter reference:* Section 1 — What "Agent" Actually Means

---

**Q2 — B**
*Correct because:* The chapter states directly: "Graph-based orchestration is predictable: every step is defined, every failure is locatable, every path is auditable. Conversation-based orchestration is flexible: agents can handle novel task sequences that no one pre-specified, but the failure modes are harder to isolate and the debugging surface is enormous."
*Why the distractors are wrong:*
- A) The chapter frames the comparison as a production-reliability trade-off, not a complexity ceiling; both approaches can handle complex tasks.
- C) The chapter does not characterize conversation-based orchestration as cheaper; it characterizes it as more flexible but harder to debug and audit.
*Chapter reference:* Section 4 — Orchestration — The Layer That Connects the Loops

---

**Q3 — False**
*Correct because:* The ReAct loop interleaves reasoning and acting — it does not require all reasoning to complete before any action is taken. The pattern is: THOUGHT (reason about what to do), ACTION (call a tool), OBSERVATION (receive result), THOUGHT (update reasoning based on result), ACTION (next step). The chapter explicitly states that "pure chain-of-thought is all reasoning — the model talks to itself but cannot reach into the world," and that ReAct improves on this by interleaving the two.
*Chapter reference:* Section 3 — The ReAct Loop

---

**Q4 — B**
*Correct because:* The chapter names three mega-agent failure modes: token costs become unsustainable, failure modes blur (cannot locate fault when the system is wrong), and the product has no surfaces. "Failure modes blur" is the second of these three explicitly named consequences.
*Why the distractors are wrong:*
- A) Model licensing costs are not among the three failure modes the chapter names for mega-agent design.
- C) The chapter does not claim a mega-agent cannot process multi-source inputs; the failure modes are about cost, debuggability, and product legibility, not input processing capability.
*Chapter reference:* Section 2 — The Five Layers — The Mega-Agent Failure

---

**Q5 — False**
*Correct because:* The chapter explicitly argues the opposite: "the five-layer choice is simultaneously an engineering decision and a brand decision." It states that the same architectural choice that improves debuggability also makes the product saleable, and that "naming is brand strategy." The chapter further argues that engineers should make architectural choices deliberately with brand consequences in mind, not discover brand position after the fact.
*Chapter reference:* Section 2 — Naming Is Brand Strategy; Section 5 — Architecture as Brand

---

**Q6 — B**
*Correct because:* The chapter's failure-isolation argument is precisely that layered architectures allow fault to be located at a named layer. Deduplication in the Intelligence Agent is an explicit step in the chapter's ReAct trace — the MD5 hash and Levenshtein distance check happen before articles reach the LLM. A double-counted story in the news feed is a deduplication failure, not a model failure. Saying "fix the model" is the mega-agent thinking the chapter argues against — it treats the system as a black box.
*Why the distractors are wrong:*
- A) The chapter does not describe a token-weighting mechanism that would cause the LLM to over-count positive sentiment; the root cause in the scenario is upstream in the data pipeline.
- C) The Performance Agent's success log records that the run completed, not that the data was correct; the orchestration layer routes data, it does not validate deduplication results.
*Chapter reference:* Section 2 — The Mega-Agent Failure; Section 3 — The ReAct Loop trace

---

**Q7 — Short-Answer**
*Model answer:* The chapter uses "augmentation-to-delegation spectrum" (or "theory of risk" / "model of agency and trust") as the dimension. Cursor sits on the augmentation end: "the developer stays in the driver's seat at all times," with AI as a collaborator that developers review and approve. Devin sits on the delegation end: "the developer assigns work, Devin executes, the developer reviews outcomes." Cursor's brand is "AI for engineers who want to be better engineers"; Devin's brand is "AI engineers you assign work to."
*Common error:* Describing the difference as capability (Devin is more powerful) rather than architecture and theory of risk — the chapter explicitly states "Same underlying technology stack. Same frontier LLMs."
*Chapter reference:* Section 2 — A Worked Architecture Comparison: Cursor and Devin

---

**Q8 — B**
*Correct because:* The chapter's Intelligence Agent ReAct trace shows the deduplication step with this explicit reasoning: "Deduplicating before scoring saves tokens and prevents counting the same story multiple times." The two mechanisms are MD5 hash on titles and Levenshtein distance on near-matches, reducing 870 articles to 87 unique ones before the LLM scoring call.
*Why the distractors are wrong:*
- A) The Google News API does not require MD5 hashing as a prerequisite; this reverses the causal direction — the agent applies hashing for its own cost and accuracy reasons.
- C) The chapter frames deduplication as a token-cost and data-quality measure, not a security measure.
*Chapter reference:* Section 3 — The ReAct Loop / Intelligence Agent trace

---

**Q9 — Short-Answer**
*Model answer:* The chapter states: "Identify the decisions in your system where a wrong answer is expensive and hard to reverse. Put humans there. Automate everything else." The criterion is the combination of two factors — high consequence of error and low reversibility. The chapter frames this as a risk-engineering question: where the downside of automation being wrong is severe and asymmetric, human review belongs in the pipeline.
*What a strong answer includes:*
- The two-factor criterion: consequence severity and reversibility
- The framing as risk engineering, not a philosophical or ethical question
- Recognition that the chapter identifies marketing decisions (content publishing, campaign budget allocation) as examples where these conditions are met
*Chapter reference:* Section 4 — The Human-in-the-Loop Decision

---

**Q10 — Brief-Response**
*Model answer:* The product manager's challenge describes a top-down process (brand strategy drives architecture) and is not wrong as a description of how some organizations work. However, the chapter's claim is different and more fundamental: it is not that engineers should ignore brand teams, but that every architectural choice produces brand consequences regardless of whether those consequences were intended. The chapter's evidence is that Cursor's and Devin's brand positions "emerged from architectural commitments that were probably made for technical reasons and whose brand implications became visible later." The chapter's prescription is that a designer working from scratch has the rare opportunity to run the process deliberately — choosing architecture with intended brand consequences rather than discovering them retroactively. The product manager's account describes a coordination process; the chapter describes a structural mechanism.
*What a strong answer includes:*
- Recognition that the product manager's point describes a real process (brand-first design) but at a different level of analysis
- The chapter's core claim: architecture produces brand consequences whether or not they are intended
- Use of the Cursor/Devin evidence to show the mechanism
*Common error:* Treating the product manager's argument as equivalent to the chapter's and concluding they are the same — the chapter's claim is about structural mechanism, not organizational process.
*Chapter reference:* Section 5 — Architecture as Brand

---

**Q11 — Transfer Brief-Response**
*Model answer:* The three-layer hospital system produces brand consequences directly analogous to Madison's five-layer choice: a clinical administrator can say "The Triage layer is working; the Documentation layer needs review," creating diagnostic and trust surfaces that a black-box mega-agent cannot provide. Each layer can be versioned, audited, and sold or deployed separately — a hospital that already has its own routing system could adopt only the Triage and Documentation layers. A mega-agent version would suffer the chapter's three mega-agent failure modes: blurred failure attribution when a patient is mis-routed (was it a triage error or a routing error?), unsustainable token costs as patient history is re-read in every call, and no named product surface for clinical administrators to reason about, audit, or trust. In a clinical setting, the failure-isolation argument is especially high-stakes because "the fault is somewhere in the model" is not an actionable response to a mis-routed emergency patient.
*What a strong answer includes:*
- At least two of the three mega-agent failure modes applied specifically to the hospital context
- The product-surface / legibility argument: named layers create things clinical staff can name and trust
- Recognition that the failure-isolation consequence is especially consequential in high-stakes domains
*Chapter reference:* Section 2 — The Mega-Agent Failure; Section 5 — Architecture as Brand

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

- Confusing "agent" meanings — treating Madison agents as autonomous systems (meaning 3) when the chapter uses meaning 4 (specialized role in a pipeline). Students from ML backgrounds especially conflate these.
- Treating the ReAct loop as "plan first, then act" — a sequential misreading. The loop's value comes from the interleaving of reasoning and observation; students who misread it will fail Q3 and struggle with the scenario in Q6.
- Treating "architecture is brand" as a metaphor rather than a mechanical claim — the failure here is understanding it as branding language rather than as a structural argument about product surfaces.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name all five Madison layers and their primary function.
- Does not know the difference between graph-based and conversation-based orchestration beyond "one uses graphs."

**Scaffolding adjustments:**

- *For students who score below 5:* Return to Section 2 (Five Layers and the Mega-Agent Failure) and Section 3 (ReAct Loop) before retaking. Write out the Intelligence Agent's ReAct trace from memory before attempting Q6 again.
- *For students who score 10/10 on first attempt:* Attempt Exercise S2 from the chapter (design a sixth Madison layer) — it requires holding all five existing layers in working memory while designing something new, and forces the student to specify failure modes and orchestration choices.

**Grading weight guidance (if used for credit):**
- Section 1 MCQ items: 0.25–0.5% of final course grade each
- Section 2 Short-Answer items: 0.5–1.0% each
- Section 3 Brief-Response items: up to 2.5% each
- Collectively, chapter quizzes should not exceed 5% of overall course grade
