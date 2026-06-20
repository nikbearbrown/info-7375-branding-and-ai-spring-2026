# Chapter Quiz: Product Requirements and Scope

*Chapter 4 of Branding and AI (INFO 7375)*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- LO 1 — Write a one-page PRD that answers four questions — problem, gap, tool, MVP boundary — with enough precision that another engineer can build from it.
- LO 2 — Distinguish between a PRD that specifies *what* a product does versus one that specifies *how* it works.
- LO 3 — Apply the Build-Measure-Learn loop to evaluate whether a proposed feature belongs in v1 or v2.
- LO 4 — Construct an MVP boundary — specifically the "out of scope" column — and defend each exclusion.
- LO 5 — Identify the brand consequence of scope discipline, using Linear as a primary case.

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

According to the chapter (citing Marty Cagan's *Inspired*), what is the core rule governing what belongs in a PRD?

A) The PRD specifies the *what*, not the *how* — product teams decide what the product needs to do; engineers decide how to implement it
B) The PRD specifies both *what* and *how*, because ambiguity in either dimension causes missed deadlines
C) The PRD specifies the *how* in enough detail that engineering can begin without follow-up conversations

---

**Question 2** *(Multiple-Choice)*

Eric Ries defines a minimum viable product as "a version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." According to the chapter, what does "validated" specifically mean in this definition?

A) The learning was confirmed by a user-testing session with at least five participants
B) The learning came from what users *did*, not what they *said*
C) The learning passed a peer review process by the product team before being acted on

---

**Question 3** *(True/False)*

According to the chapter, the "out of scope" column in an MVP boundary is less important than the "in scope" column, because inclusion decisions define what the product is.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

The chapter defines the "$100,000 no" for the worked example of a competitor intelligence tool as refusing to build multi-user account support in v1. What is the chapter's stated reason for this specific refusal?

A) Multi-user accounts are technically complex and would delay the v1 ship date beyond the available timeline
B) Adding multi-user accounts changes the product from a personal intelligence tool to a team intelligence platform, forcing a different design philosophy for every subsequent decision
C) Multi-user accounts are a feature that competitors already offer, and building them would eliminate the product's differentiation

---

**Question 5** *(True/False)*

In the chapter's analysis of Linear, the product's competitive advantage comes primarily from having more features and configuration options than competitors like Jira and Asana.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student writes the following tool section in their PRD: "An AI-powered career coaching platform that helps job seekers land their next role using advanced NLP and personalized recommendations." A second student writes: "A self-hosted n8n workflow that pulls job postings matching a user's target role from three configurable job boards, scores each posting for fit against the user's uploaded resume using the OpenAI API, and writes a ranked daily list to a Google Sheet — total API cost under $15/month." Which tool description passes the chapter's test, and why?

A) The first, because it communicates the product's value clearly to non-technical stakeholders
B) The second, because it names the delivery mechanism, the input, the processing, the output, and the cost envelope — a competent engineer can build from it and a user can evaluate whether it solves their problem
C) The first, because tool descriptions in a PRD should use accessible language rather than technical specifics

---

**Question 7** *(Short-Answer)*

The chapter shows a Build-Measure-Learn loop for a sentiment analysis pipeline. The hypothesis is: "Marketing managers at small B2B companies will use a daily competitor-news summary if it is pre-filtered to fewer than 10 items and scored for sentiment." What behavioral evidence, according to the chapter's logic, would *falsify* this hypothesis — and what would the product team learn from that falsification?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

Linear's product method includes a commitment to "opinionated software" — the product has a specific model of how engineering teams should manage work and is resistant to customization outside that model. According to the chapter's analysis of Linear, what is the brand consequence of this engineering commitment?

A) Linear captures a smaller, more technically sophisticated market, because opinionated software alienates mainstream users
B) Linear has become the product engineers recommend to other engineers who want to escape Jira — the discipline that said no to enterprise customization is the same discipline that produced the coherent experience users love
C) Linear's opinionated approach allows it to charge higher prices than Jira and Asana because enterprise features command premium rates

---

**Question 9** *(Short-Answer)*

The chapter describes two problem statement failure modes: "abstracting the user" and "describing a symptom instead of a cause." The example problem statement that passes the chapter's test includes a specific user, a specific task, a specific frequency, a specific output, and a specific failure mode. Using these five elements, evaluate the following problem statement: "Startup founders need better tools for tracking their company's financial performance."

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter claims that "scope discipline compounds" — each principled refusal to add a feature preserves coherence, which accumulates into brand identity over time. A product manager argues the opposite: "Saying no to features is a false discipline. What actually builds brand identity is execution quality — a product can have many features and still be coherent if each feature is executed well. The problem isn't feature count; it's execution." Evaluate this argument. Does the chapter provide evidence that scope reduction itself (rather than only execution quality) produces brand identity?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

An independent music producer is building a tool to help session musicians track which studios owe them payment for recorded sessions. Apply the four-section PRD structure from the chapter to evaluate the following first draft:

*Problem: Musicians don't always get paid on time. Gap: Existing invoicing tools like FreshBooks aren't designed for music industry workflows. Tool: An AI-powered payment tracking platform for creative professionals. MVP boundary: In scope — payment tracking, invoice generation, reminders. Out of scope — tax filing.*

Identify the most critical failure mode in each of the four sections, using the chapter's specific failure-mode vocabulary. What one revision would most improve this PRD?

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — A**
*Correct because:* The chapter explicitly states: "Marty Cagan, whose book *Inspired* is the most widely-read treatment of product management in the technology industry, gives the PRD's core rule in a single sentence: the PRD specifies the *what*, not the *how*." The chapter reinforces this with examples: specifying SendGrid for email delivery is *how* in *what*'s clothing — it makes a technology decision the PRD had no business making.
*Why the distractors are wrong:*
- B) The chapter argues the opposite: conflating what and how produces worse products because implementation details in the PRD become false constraints that engineers must later fight to change.
- C) The chapter's entire Section 1 is devoted to preventing the *how* from appearing in the PRD; this option inverts the chapter's core rule.
*Chapter reference:* Section 1 — What a PRD Actually Is

---

**Q2 — B**
*Correct because:* The chapter states directly: "Validated means the learning came from what users *did*, not what they *said*. Users reliably tell you they will do things they will not do." The chapter contrasts asking "Would you use this?" (stated intent, not validated) with measuring whether users actually open the Google Sheet three times a week (behavioral evidence, validated).
*Why the distractors are wrong:*
- A) The chapter does not specify a participant threshold for validation; the criterion is behavioral versus stated, not sample size.
- C) Peer review is not mentioned as part of the validated learning cycle; validation in the Build-Measure-Learn loop comes from user behavior, not internal review.
*Chapter reference:* Section 2 — The Build-Measure-Learn Loop

---

**Q3 — False**
*Correct because:* The chapter explicitly states: "The out list is more important than the in list. Inclusion is the default — every feature suggestion gets into the brainstorm. Exclusion requires judgment." The chapter further states that "the things you refuse to build define the product more than the things you build" (the chapter's TL;DR). The $100,000 no section reinforces this: write the out list first, from the $100,000 no down.
*Chapter reference:* Section 1, Section 4 — MVP Boundary; Section 3 — Your $100,000 No

---

**Q4 — B**
*Correct because:* The chapter explains: "Adding [multi-user accounts] changes the product from a personal intelligence tool to a team intelligence platform, and those are different products. The day you build multi-user support, you have stopped building the personal tool and started building the team platform. Every subsequent decision — permissions, audit trails, team-level dashboards, admin interfaces — is a team-platform decision, not a personal-tool decision. The product's point of view has changed. You have opened the door."
*Why the distractors are wrong:*
- A) The chapter explicitly states "The implementation is not technically difficult" — technical complexity is not the reason for refusal.
- C) The chapter's reason for the refusal is about product coherence and design philosophy, not competitive differentiation.
*Chapter reference:* Section 3 — Your $100,000 No

---

**Q5 — False**
*Correct because:* The chapter states that Linear "does fewer things than its competitors" and that its product "by design, does fewer things than its competitors." Linear's advantage comes from scope discipline and coherent experience: "Teams that adopt Linear's model find the product exceptional." The chapter explicitly says the brand attraction is "not because Linear has more features — it has fewer — but because Linear's constraints produce a coherent experience."
*Chapter reference:* Section 3 — The Linear Case

---

**Q6 — B**
*Correct because:* The chapter's test for a tool description is: "Read your tool description to someone who has not heard your pitch. Ask them what the tool does. If they cannot tell you — if they have to ask clarifying questions — the description is not specific enough." The second description passes this test: it names the delivery mechanism (n8n workflow), the input (job boards), the processing (OpenAI API scoring against resume), the output (Google Sheet), and the cost ($15/month). The first description — "AI-powered career coaching platform" — is marketing language the chapter explicitly bans.
*Why the distractors are wrong:*
- A) The chapter explicitly calls "AI-powered platform" language a "press release sentence" that "tells the reader nothing about what the product does."
- C) The chapter does not value accessibility over specificity in tool descriptions; the test is whether an engineer can build from it and a user can evaluate it.
*Chapter reference:* Section 1, Section 3 — Tool

---

**Q7 — Short-Answer**
*Model answer:* The hypothesis would be falsified if marketing managers stop opening the Google Sheet regularly after the novelty of the first week wears off — specifically, if the open rate drops to near zero after two weeks of use. The chapter identifies three possible causes of this falsification: the intelligence is not actionable, the format is wrong, or the cadence is wrong. The product team would need to distinguish between these causes — by talking to non-opening users, observing their workflow, or A/B testing format and cadence changes — before updating the hypothesis and rebuilding. Simply observing that users stopped opening the sheet tells you the hypothesis failed; it does not tell you which element to fix.
*Common error:* Saying the falsification would be "if no one signs up" — that would falsify the customer discovery, not the core product hypothesis about daily usage behavior.
*Chapter reference:* Section 2 — The Build-Measure-Learn Loop

---

**Q8 — B**
*Correct because:* The chapter traces the specific mechanism: "Linear has become the product that engineers recommend to other engineers when they want to escape Jira. The recommendation happens not because Linear has more features — it has fewer — but because Linear's constraints produce a coherent experience. The discipline that said no to the enterprise customization is the same discipline that produced the product engineers love." The chapter describes this as "scope discipline compounds" — each refusal preserves coherence, which accumulates into brand identity.
*Why the distractors are wrong:*
- A) The chapter does not describe Linear as serving a smaller, technically sophisticated market; it describes Linear as successful through word-of-mouth to a "$35 million ARR" scale.
- C) The chapter does not claim Linear charges premium prices because of enterprise features; it notes Linear declined enterprise customization requests even when they would have been "worth significant annual contracts."
*Chapter reference:* Section 3 — The Linear Case

---

**Q9 — Short-Answer**
*Model answer:* The problem statement "Startup founders need better tools for tracking their company's financial performance" fails both failure modes named in the chapter. First, "startup founders" abstracts the user — the chapter requires a specific user at the level of "marketing managers at Series-B SaaS companies with no dedicated analytics team." Second, "need better tools" describes a symptom (a gap in tooling), not a cause — the chapter requires a specific task, a specific frequency, a specific cost, and a specific consequence of the current inadequacy. A revised statement following the chapter's five-element format might be: "Founders of pre-Series-A startups (one to five person teams, no CFO) spend three to five hours per month manually compiling cash runway estimates from bank exports and spreadsheets, because existing accounting tools require an accountant to interpret and do not produce the single-number runway estimate investors ask for in every meeting."
*What a strong answer includes:*
- Names both failure modes (abstract user, symptom not cause) by the chapter's labels
- Applies the five elements (specific user, task, frequency, output, failure mode) as the repair
*Chapter reference:* Section 1 — Problem

---

**Q10 — Brief-Response**
*Model answer:* The product manager's argument is partially valid — execution quality matters — but the chapter provides specific evidence that scope reduction itself produces brand effects independent of execution quality. The Linear case shows that Linear declined enterprise customization requests that "would have been worth significant annual contracts" — these were not execution failures but principled scope refusals. The result was not just a well-executed product but a coherent identity that "engineers recommend to other engineers." The chapter's compounding mechanism works through coherence — each refusal preserves the model of the product in users' minds — which is a different mechanism from execution quality. A product can execute features well and still lose coherence if the features are in tension with each other. The counter-evidence the product manager would need to provide is a product with many features, each executed well, that accumulates the same strong word-of-mouth brand identity as Linear — and the chapter's implicit claim is that no such product exists in the same way.
*What a strong answer includes:*
- Acknowledgment that execution quality is real and relevant
- The specific Linear evidence: declined contracts, word-of-mouth growth, coherence mechanism
- The coherence vs. execution quality distinction
*Common error:* Treating the product manager's argument as a full rebuttal without engaging the specific Linear evidence.
*Chapter reference:* Section 3 — The Linear Case; scope discipline compounds

---

**Q11 — Transfer Brief-Response**
*Model answer:* The PRD has four distinct failure modes. The Problem section abstracts the user ("musicians" without specifying type, frequency, or context — session musicians at independent studios, session musicians at major labels, and touring musicians face different payment timelines and workflows). The Gap section names only one competitor and uses a vague failure mode ("isn't designed for music industry workflows" says nothing specific about what FreshBooks gets wrong for this user). The Tool section uses marketing language — "AI-powered payment tracking platform for creative professionals" — that the chapter would call a press release sentence; there is no delivery mechanism, no specific output, no cost envelope. The MVP boundary's out list has only one item (tax filing), which is not a disciplined out list — the chapter requires at least five exclusions and a named $100,000 no. The single highest-value revision would be rewriting the problem statement with a specific user (e.g., "session musicians at independent recording studios who are owed between three and eight invoice payments at any given time"), a specific task (tracking which studios have paid, which are overdue, and by how much), and the specific cost of the current manual process.
*What a strong answer includes:*
- Applies the chapter's failure-mode vocabulary to each section (abstract user, symptom not cause, marketing language, missing out list)
- Identifies the problem statement as the highest-priority fix, consistent with the chapter's logic that specificity in the problem statement enables testing
*Chapter reference:* Section 1 — all four PRD sections; Section 3 — Your $100,000 No

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

- Treating the out-of-scope list as less important than the in-scope list — students consistently underinvest in exclusions. Q3 targets this directly.
- Confusing "validated" in Build-Measure-Learn with "user-tested" or "peer-reviewed" — the chapter's definition is behavioral, not procedural. Q2 and Q7 probe this.
- Writing "how" content in PRD tool descriptions — technology specifics smuggled into what-level descriptions. Q6 provides a worked contrast.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot distinguish between a symptom and a cause in a problem statement; all problem statements produced are framed as gaps or wishes.
- Cannot explain why Linear's competitive advantage comes from having fewer features — conflates scope discipline with execution quality.

**Scaffolding adjustments:**

- *For students who score below 5:* Return to Section 1 (the four PRD sections, specifically the Problem and MVP Boundary with examples of weak vs. strong versions) and Section 3 (the Linear case, scope discipline compounds). These two sections carry the majority of the chapter's testable content.
- *For students who score 10/10 on first attempt:* Attempt Exercise C1 from the chapter — evaluate Cagan's argument that high-fidelity prototypes replace PRDs as the primary discovery tool. This requires holding the chapter's PRD argument in tension with a legitimate expert challenge.

**Grading weight guidance (if used for credit):**
- Section 1 MCQ items: 0.25–0.5% of final course grade each
- Section 2 Short-Answer items: 0.5–1.0% each
- Section 3 Brief-Response items: up to 2.5% each
- Collectively, chapter quizzes should not exceed 5% of overall course grade
