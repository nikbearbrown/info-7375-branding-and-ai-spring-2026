# Chapter Quiz: Data Pipelines and Workflow Automation

*Chapter 5 of Branding and AI (INFO 7375)*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- LO 1 — Define a data pipeline as a chain of contracts rather than a chain of code, and explain why the distinction matters for reliability.
- LO 2 — Identify the four categories of data pipeline and match each to the appropriate use case.
- LO 3 — Explain the Apollo/Reddit case as a model of pipeline fragility cascading into brand damage.
- LO 5 — Document every external dependency in a pipeline using the contracts framework.
- LO 6 — Build error handling and degraded modes into a pipeline so that a contract failure produces graceful degradation rather than a crash.

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

According to the chapter, what is the correct definition of a data pipeline?

A) A collection of Python scripts that pull data from external sources and process it
B) A chain of contracts, each owned by someone else, each subject to change without your consent
C) A set of n8n nodes that connect API calls, transform data, and write to a destination

---

**Question 2** *(Multiple-Choice)*

The Madison Intelligence Agent uses which combination of pipeline types from the chapter's four-category taxonomy?

A) ETL and stream-processing — batch data warehousing plus real-time event ingestion
B) Workflow-automation and inference — an n8n pipeline with an LLM scoring step inside it
C) Stream-processing and inference — a continuous event feed driving LLM completions

---

**Question 3** *(True/False)*

In the Apollo/Reddit case, the public's brand perception of Apollo the product and Christian Selig the developer moved in the same direction — both suffered severe damage from the API pricing change.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

The chapter describes four levels of degraded mode in order of increasing robustness. Which of the following correctly names the lowest level — the minimum viable degraded mode?

A) Graceful staleness — serve the last successful result with a visible timestamp
B) Informative failure — detect the contract failure and show the user a clear message about what is unavailable and why
C) Partial degradation — disable the feature that depends on the broken contract while the rest of the product continues

---

**Question 5** *(True/False)*

The chapter argues that RSS feeds are less desirable as pipeline contracts than platform APIs like Reddit's or Twitter's, because RSS provides richer data and has fewer rate limits.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student builds an n8n pipeline that ingests posts from a social platform's API, scores them for sentiment using an LLM, and writes a daily summary to Google Sheets. Three months after launch, the social platform changes its API from a free tier to a $500/month enterprise tier with no grandfathering. The student's workflow crashes overnight. Users of the student's tool see: "This app is broken." Using the chapter's framing, which analysis is most accurate?

A) This is primarily a business model failure — the student should have charged users before the API pricing changed
B) This is a contract failure: the student depended on a contract they did not own, built no degraded mode for it, and therefore absorbed the full brand damage of an upstream decision — precisely the Apollo pattern
C) This is primarily a technical failure — the student's error-handling was insufficient, which could have been fixed by adding try/catch blocks in the transformation node

---

**Question 7** *(Short-Answer)*

The chapter describes the Heroku free-tier deprecation (November 2022) and the Twitter API rupture (February 2023) alongside the Reddit API change. What single structural property do all three cases share, and what does that shared property imply about choosing external contracts for a pipeline?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

In the Madison Intelligence Agent's n8n workflow, the chapter identifies parallel ingestion branches as a specific design choice that addresses a specific failure mode. What failure mode do parallel branches address, and what would happen without them?

A) Parallel branches prevent duplicate items from being written to the output sheet — without them, the same article would appear multiple times
B) Parallel branches prevent a single source going down from stalling the entire pipeline — without them, one dead API stops all ingestion
C) Parallel branches allow the LLM scoring step to process articles from different sources with different prompt configurations simultaneously

---

**Question 9** *(Short-Answer)*

The chapter requires you to document every external dependency using a four-part contract record. Using the Hacker News RSS feed example from Part 4, write the contract documentation record for that single dependency using the four required fields.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter argues that pipeline discipline is simultaneously technical practice and brand strategy: "A pipeline failure is a brand failure." A software engineer responds: "Brand and reliability are separate concerns. A well-designed pipeline with proper error handling is a technical goal. Whether customers trust the brand after a failure depends on how the company communicates — not on the pipeline architecture." Evaluate this argument using the Apollo case. Does the chapter's evidence support or challenge the claim that architecture and brand are genuinely distinct concerns?

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

A nonprofit organization builds an n8n pipeline that pulls volunteer shift data from Salesforce, checks an external weather API to flag shifts that may be affected by bad conditions, and writes a daily briefing to a shared Google Sheet for shift coordinators. Map the three most significant external contracts in this pipeline, identify the failure mode for each, and recommend a degraded mode for the one you consider highest-risk. Use the chapter's contract-documentation format and degraded-mode taxonomy.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter states this as the core definition: "A data pipeline is a chain of contracts, each owned by someone else, each subject to change without your consent." The chapter explicitly frames this as distinct from the code-centric view: "A pipeline is not a piece of code. A pipeline is a *chain of contracts*." The "owned by someone else" and "subject to change without your consent" clauses are the parts the chapter identifies as what engineering curricula typically omit.
*Why the distractors are wrong:*
- A) Describing a pipeline as "Python scripts" is the code-centric view the chapter argues against; it makes the contracts invisible.
- C) Describing a pipeline as "n8n nodes" is a tool-specific description, not the chapter's definitional frame; n8n is one implementation of a workflow-automation pipeline, not the definition of a pipeline.
*Chapter reference:* Part 1 — What "Data Pipeline" Actually Means / What unifies all four: the contract structure

---

**Q2 — B**
*Correct because:* The chapter states: "The Madison Intelligence Agent is a workflow-automation pipeline with an inference step." And: "In Madison's architecture, the inference pipeline runs *inside* the workflow-automation pipeline — it is a step, not a separate system." The chapter also traces the specific workflow: "RSS ingestion → deduplication → LLM scoring → Sheet write. That is types 3 and 4 working together."
*Why the distractors are wrong:*
- A) The chapter explicitly states that ETL and stream-processing pipelines are not used in Madison; it labels both "No" in the comparison table.
- C) The chapter describes stream-processing as "high throughput, low latency, high operational complexity" suited for fraud detection, not for Madison's scheduled marketing intelligence workflow.
*Chapter reference:* Part 1 — The four categories; What unifies all four

---

**Q3 — False**
*Correct because:* The chapter explicitly states the asymmetry: "Apollo *the product* still died... The brand damage to the *product* was total, even as the brand benefit to the *person* was real." The chapter's Figure 5.3 formalizes this: Reddit received "diffuse reputational damage" that recovered; Apollo received "product death + total user loss within thirty days" (permanent); Christian Selig personally received "net positive — public sympathy, transparency rewarded, developer reputation strengthened."
*Chapter reference:* Part 2 — The Apollo Case / What the Apollo case teaches

---

**Q4 — B**
*Correct because:* The chapter describes four levels "in increasing order of robustness," with informative failure listed first as "the minimum viable degraded mode." The chapter defines it as: "The product detects the contract failure and shows the user a clear message about what is unavailable and why, rather than an opaque error." The chapter also calls this "what Selig did" — Selig published his calculations and explained what had changed and why, making the breakage legible to users.
*Why the distractors are wrong:*
- A) Graceful staleness is the fourth level in the chapter's taxonomy — serving cached data — not the minimum.
- C) Partial degradation is the second level — disabling only the affected feature while the rest of the product continues — not the minimum.
*Chapter reference:* Part 3 — The degraded mode requirement

---

**Q5 — False**
*Correct because:* The chapter argues the opposite: RSS is preferred precisely for its stability, not its richness. The chapter states RSS "satisfies all three criteria" of stable contracts: "They have been stable since the early 2000s. They are implemented by thousands of services independently. No single platform can unilaterally change the specification." The chapter explicitly acknowledges the trade-off: "RSS is stable but limited" — richer contracts are usually less stable.
*Chapter reference:* Part 5 — Choosing stable contracts

---

**Q6 — B**
*Correct because:* This scenario is a direct instantiation of the Apollo pattern the chapter analyzes: a well-functioning pipeline depending on an external contract the builder does not own, with no degraded mode, absorbing full downstream brand damage from an upstream pricing decision. The chapter states: "your users do not see 'upstream contract failure.' They see 'this tool stopped working.' The brand damage flows to the name on the front page — which is yours." The chapter also notes "damage flows downhill in a contract chain."
*Why the distractors are wrong:*
- A) The chapter's analysis does not frame Apollo's failure as a business model problem; it frames it as a pipeline discipline problem — the absence of documented contracts and degraded modes.
- C) Try/catch blocks at the node level are error handling, but the chapter's argument is that the architecture-level problem (single-source dependency, no degraded mode) is what produced the brand failure — better error messages would not have saved Apollo.
*Chapter reference:* Part 2 — The Apollo Case; Part 3 — Pipeline as Brand Asset

---

**Q7 — Short-Answer**
*Model answer:* All three cases share the same structural property: each external contract was controlled by a single platform that made a unilateral change when its business model shifted. The chapter names this explicitly: each failed contract "was controlled by a single platform... was cheap or free because the platform had not yet monetized the capability... was changed unilaterally when the business model shifted." The implication for choosing contracts is the chapter's three-criteria stability heuristic: prefer contracts maintained by multiple parties rather than a single platform, stable over a long history, and not dependent on a single company's business model remaining aligned with your use.
*Common error:* Describing the shared property as "they were all free APIs" — the chapter's analysis is about single-platform control and business-model misalignment, not pricing level per se.
*Chapter reference:* Part 2 — A worked pattern: three platform-API ruptures; Part 5 — Choosing stable contracts

---

**Q8 — B**
*Correct because:* The chapter's Figure 5.10 states explicitly for parallel ingestion branches: "A single source goes down or rate-limits → Entire pipeline stalls waiting for one dead API; daily output is empty." The chapter describes the Madison workflow as having "multiple parallel branches, each pulling from a different source: RSS feeds, Google News API, Reddit API. Each branch is a separate HTTP Request node. Each external dependency is isolated. If the Reddit node fails, the RSS branches continue."
*Why the distractors are wrong:*
- A) The seen-URL store (not parallel branches) is what prevents duplicate items; Figure 5.10 attributes that to a different design choice.
- C) The chapter does not describe parallel branches as enabling different LLM prompts per source; branches run different ingestion sources, and LLM scoring is downstream and unified.
*Chapter reference:* Part 4 — Worked Example: Reading the Madison Intelligence Agent's Workflow; Figure 5.10

---

**Q9 — Short-Answer**
*Model answer:* The chapter's required contract-documentation format covers four fields: what the service provides, what it costs, what its rate limit is, and what the terms allow. For the Hacker News RSS feed, the chapter provides this directly as an example: "Hacker News RSS — no auth required, no rate limit documented, stable Atom format since 2006, risk: low." A full four-field record would be: (1) What it provides: RSS/Atom feed of top Hacker News stories with titles, links, and timestamps; (2) What it costs: free, no authentication required; (3) Rate limit: none documented; (4) Terms: publicly accessible, stable Atom format since 2006, risk classified as low because no single platform can unilaterally change the specification.
*What a strong answer includes:*
- All four contract fields present
- The "risk: low" classification with a rationale grounded in the chapter's stability criteria
- Acknowledgment that the format comes from the chapter's contract-documentation discipline
*Chapter reference:* Part 3 — The contract documentation habit; Part 4 — Node 2 description

---

**Q10 — Brief-Response**
*Model answer:* The Apollo case challenges the engineer's clean separation between architecture and brand. Selig's personal brand improved precisely because his architecture included a transparency layer — he documented the math, published the calculation, and made the contract failure legible to users. That transparency was an architectural choice (how he built his public communication about the pipeline's dependency), not just a PR response after the fact. The chapter's argument is stronger than "companies should communicate better after failures" — it is that the architecture determines whether a failure is legible at all. An informative-failure degraded mode is an architectural choice that produces a brand outcome: users who understand what happened preserve trust; users who see an opaque crash do not. Architecture and brand communication are entangled at the design stage, not separable concerns.
*What a strong answer includes:*
- The specific Apollo evidence: Selig's transparency was an architecture-adjacent choice that produced brand benefit
- The chapter's mechanism: architecture determines legibility of failure, which determines brand outcome
- Acknowledgment that the engineer's point has merit (communication matters) while identifying where it underestimates the architectural dependency
*Chapter reference:* Part 2 — What the Apollo case teaches; Part 3 — The degraded mode requirement (informative failure)

---

**Q11 — Transfer Brief-Response**
*Model answer:* The three significant external contracts are: (1) Salesforce API — provides volunteer shift data; failure mode: Salesforce authentication expires or API rate-limits, leaving the briefing with no data; (2) Weather API — provides weather forecasts tied to shift locations; failure mode: the weather service is unavailable or changes its free-tier terms, breaking the flag logic; (3) Google Sheets API — writes the daily briefing; failure mode: Google credentials expire or quota is exceeded, preventing output. The highest-risk contract is the Salesforce integration, because it is a paid enterprise platform with single-vendor control, authentication credentials that expire, and potentially rich but fragile terms — matching the chapter's three unstable-contract criteria. The recommended degraded mode is graceful staleness: cache the last successful shift export with a visible timestamp, and continue serving the weather-flagged briefing from cached data while surfacing an alert to coordinators that the data is stale and from what date.
*What a strong answer includes:*
- Names at least three contracts with their specific failure modes
- Identifies which is highest-risk with reasoning from the chapter's stability criteria
- Recommends a specific named degraded mode (informative failure, partial degradation, fallback source, or graceful staleness) with a brief justification
*Chapter reference:* Part 3 — contract documentation and degraded modes; Part 5 — Choosing stable contracts

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

- Treating the Apollo case as a business failure rather than a contract-design failure — students will say "the lesson is don't depend on one platform's API" without engaging the degraded-mode argument. Q3 and Q6 probe this distinction.
- Conflating informative failure with error handling in the code — students conflate graceful error messages with the architectural degraded-mode concept. Q4 targets this.
- Misremembering which Madison design choice prevents which failure mode — parallel branches vs. seen-URL store vs. run log are distinct solutions to distinct problems. Q8 targets this specifically.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot explain the Apollo/Reddit case beyond "the API got expensive" — lacks the chain-of-contracts framing and the brand-damage asymmetry (product vs. person).
- Cannot name more than two of the four degraded-mode levels or cannot order them by robustness.

**Scaffolding adjustments:**

- *For students who score below 5:* Return to Part 2 (Apollo case) and Part 3 (the three disciplines — contract documentation, degraded mode, monitoring). These two sections carry most of the testable content. Read Figure 5.3 (Apollo brand damage asymmetry) and Figure 5.6 (degraded-mode taxonomy) as anchor points.
- *For students who score 10/10 on first attempt:* Attempt Exercise C2 from the chapter — design a fifth degraded mode that does not fit the four named categories. This requires genuine understanding of why the four levels exist as levels, not just memorization of their names.

**Grading weight guidance (if used for credit):**
- Section 1 MCQ items: 0.25–0.5% of final course grade each
- Section 2 Short-Answer items: 0.5–1.0% each
- Section 3 Brief-Response items: up to 2.5% each
- Collectively, chapter quizzes should not exceed 5% of overall course grade
