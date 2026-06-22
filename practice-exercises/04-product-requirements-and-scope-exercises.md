# Practice Exercises: Product Requirements and Scope

*Chapter 4 of Branding and AI (INFO 7375)*

> **How to use these exercises:**
> Work through each tier in order. Do not skip ahead to later tiers before
> completing earlier ones — the tiers scaffold your understanding. Attempt
> every exercise before checking the answer key. For open-ended questions,
> write at least 2–3 sentences before reading the model answer. The act of
> attempting is where the learning happens.

---

## Learning Objectives Covered

1. **Identify** the four sections of a Product Requirements Document — Problem, Gap, Tool, MVP Boundary — and explain what belongs in each section and what does not.
2. **Apply** the what/how distinction (Cagan's rule) to separate requirements from implementation decisions in a PRD.
3. **Explain** the Build-Measure-Learn loop and distinguish validated learning from stated-intent data.
4. **Define** the $100,000 no concept and explain why it is a requirement-writing discipline rather than a business strategy.
5. **Analyze** the compounding cost of scope creep using the Linear Method case study as a reference.
6. **Produce** a one-page PRD for a real AI tool that specifies problem, gap, tool, and MVP boundary — with at least one explicit $100,000 no.

*Every exercise below maps to at least one of these objectives. The `(Tests: ...)` tag on each exercise identifies which one(s) by full concept name.*

---

## Worked Example

*Study this example before attempting Tier 1. After reading it, close it and try to recall the key steps from memory before moving on.*

**Problem:** A student has written the following PRD section for an AI tool that monitors Hacker News for relevant startup news:

> *"The tool will scrape Hacker News, use GPT-4 to summarize articles, store summaries in Airtable, send a daily digest email via SendGrid, support user preferences for different topics, allow users to rate individual articles, maintain a history of past digests, integrate with Slack, and eventually add Reddit monitoring."*

Evaluate this PRD section against Chapter 4's requirements. Identify what is wrong and explain how to fix it.

**Approach:**
Step 1: Check for what/how violations. The PRD section mixes requirements ("monitor Hacker News for relevant startup news") with implementation decisions ("use GPT-4," "store in Airtable," "send via SendGrid"). These are how decisions the PRD section should not make — the PRD describes what the tool does, not how it does it.

Step 2: Check the MVP Boundary. The section contains at least five distinct features: summarization, storage, email digest, user preferences/ratings, Slack integration, and future Reddit monitoring. The chapter's rule: if the product cannot be described in one sentence and demonstrated in five minutes, the MVP boundary has not been set.

Step 3: Apply the $100,000 no. The chapter asks: what would you refuse to build even if a stakeholder offered $100,000 to add it? User ratings, Slack integration, and Reddit monitoring are all scope-expanding features that a stakeholder might request. The PRD should explicitly decline them.

Step 4: Check for the four sections. The section is entirely Tool — it contains no Problem, no Gap, and no MVP Boundary.

**Corrected PRD skeleton:**
- Problem: Early-stage startup founders waste 30–45 minutes every morning manually reading Hacker News to identify competitor mentions and relevant funding news.
- Gap: No existing tool monitors HN specifically for founder-relevant signals (competitor funding, hiring, product launches) and delivers them in a single digest at a configured time.
- Tool: An automated pipeline that monitors the top 30 HN posts daily, identifies founder-relevant signals, and emails a daily digest with one-sentence summaries to a configured address.
- MVP Boundary: One RSS source (HN top 30), one delivery mechanism (email), fixed topic categories (not user-configurable in v1). Explicit $100,000 no: user ratings — even if stakeholders request it, v1 delivers signals, not user preference modeling.

**What to notice:** The what/how violation is subtle. "Use GPT-4" feels like a tool feature, not an implementation detail — but it is a how. The PRD should say "AI summarization" and leave the model selection to the implementation phase.

---

## Tier 1 — Warm-Up (Exercises 1–8)

*Bloom's Level: Remember / Understand*
*Purpose: Verify that the chapter's core concepts and vocabulary are in place before you apply them. These should feel straightforward after a careful reading.*

---

**Exercise 1** *(Contrastive Classification)*

For each of the following statements, classify it as belonging in one of the four PRD sections (Problem, Gap, Tool, MVP Boundary) or as a how statement that does not belong in any PRD section. Justify each classification in one sentence.

1. "Startup founders spend 45 minutes per day manually curating competitor news from five different sources."
2. "The tool uses LangChain to orchestrate a three-step pipeline: scraping, LLM classification, and Sheets export."
3. "Existing competitor monitoring tools (Mention, Brand24) are designed for enterprise social media monitoring, not for startup-stage technical RSS signals."
4. "The tool will not support multi-user teams in v1, even if enterprise customers request it."
5. "An automated pipeline that monitors configured RSS feeds for competitor signals and exports a ranked daily summary."
6. "The database will use PostgreSQL on Supabase with a row-level security policy per user."

*(Tests: Four PRD sections — classification)*

---

**Exercise 2**

True / False, with explanation: According to the chapter, validated learning from a Build-Measure-Learn cycle means the team learned what users said they wanted in a survey or interview.

Write one sentence explaining why the statement is true or false, using the term *behavior* from the chapter.

*(Tests: Validated learning vs. stated intent)*

---

**Exercise 3**

In your own words, explain what the chapter calls "Cagan's rule" and give one example of a PRD statement that violates it and one that follows it. Use the same underlying feature for both examples.

*(Tests: What/how distinction — Cagan's rule)*

---

**Exercise 4**

The chapter describes the "$100,000 no." Explain:
1. What a $100,000 no is
2. Why the exercise requires naming it before building begins
3. What happens to scope if no $100,000 no is named

*(Tests: $100,000 no concept — definition, timing, and scope consequence)*

---

**Exercise 5**

The chapter uses the Linear Method as a case study in scope discipline. Name the core principle Linear applied, give one specific product decision from the case that exemplified it, and explain the brand consequence — not the engineering consequence, but the brand consequence — of that decision.

*(Tests: Linear Method — scope discipline and brand consequence)*

---

**Exercise 6** *(Contrastive Classification)*

Classify each of the following as an example of the Build-Measure-Learn loop running correctly, or as a common failure mode of the loop. For each failure, name the specific failure mode from the chapter.

1. A team launches an email digest, measures open rate (40%), and concludes users find the content valuable.
2. A team asks 20 users "would you pay for a premium tier?" — 18 say yes — and plans a paid feature.
3. A team adds a Slack integration, measures whether users link their Slack accounts within 7 days of signup, and removes the feature when only 3% do.
4. A team adds sentiment scoring to their RSS pipeline after one enterprise stakeholder says it would "be really useful."
5. A team tracks whether users who receive a daily digest return to the product 5+ days per week, treating daily return visits as evidence of habit formation.

*(Tests: Build-Measure-Learn loop — validated learning vs. stated intent; common failure modes)*

---

**Exercise 7**

The chapter argues that scope creep compounds — each added feature makes the next feature decision harder. Explain the compounding mechanism in your own words. Your explanation must use the term *MVP Boundary* and describe why setting the boundary early is protective.

*(Tests: Scope discipline compounding — MVP Boundary)*

---

**Exercise 8**

The chapter describes the Madison PRD library. In your own words, explain what the Madison PRD library is and what problem it solves that individual PRD writing does not.

*(Tests: Madison as PRD library — concept and function)*

---

## Tier 2 — Application (Exercises 9–16)

*Bloom's Level: Apply / Analyze*
*Purpose: Use the chapter's concepts in realistic situations. This is where most of the learning happens. Expect these to take more time than Tier 1.*

---

**Exercise 9** *(Scenario-Based Application — Four PRD Sections)*

Write a one-page PRD for the following tool:

**Tool concept:** An AI assistant that helps graduate students identify research papers relevant to their thesis by monitoring ten academic RSS feeds (arXiv, Semantic Scholar, Google Scholar Alerts) and producing a weekly summary email.

Your PRD must include:
- Problem (2–4 sentences identifying who has the problem and what it costs them)
- Gap (1–2 sentences identifying why existing tools do not solve it)
- Tool (1–3 sentences describing what the tool does, with no how statements)
- MVP Boundary (3–5 items the tool will do in v1; at least one explicit $100,000 no)

Apply Cagan's rule: no implementation choices in the PRD.

*(Tests: Four PRD sections; what/how distinction; $100,000 no)*

---

**Exercise 10** *(Error Analysis)*

> The following PRD was submitted by a student for a competitor monitoring tool. It contains multiple errors.

```
Product Requirements Document: TechWatch

Problem: Founders and product managers at early-stage startups need to
know what their competitors are doing. They want real-time alerts when
competitor products ship new features. They also want sentiment analysis
and social media monitoring.

Gap: Current tools like Mention and Brand24 do not use AI. Our tool
will use GPT-4o for smarter analysis.

Tool: TechWatch uses LangChain to crawl competitor websites and 
ProductHunt. It stores results in Pinecone and uses cosine similarity 
to find relevant updates. The front-end is built in Streamlit.

MVP Boundary: v1 will include: website monitoring, ProductHunt 
monitoring, Twitter monitoring, LinkedIn monitoring, sentiment 
analysis, competitor feature comparison, export to PDF, Slack 
notifications, and email digest. We will add mobile app in v2.
```

For each of the four PRD sections:
1. Identify the error(s) in that section
2. Classify each error by type (what/how violation, scope creep, stated-intent data, missing $100,000 no, etc.)
3. Write a corrected version of that section

*(Tests: Four PRD sections; what/how distinction; $100,000 no; scope discipline)*

---

**Exercise 11** *(Self-Explanation)*

Explain in your own words why the chapter claims the Problem section is the most important section of the PRD — more important than the Tool section. Your explanation must:
- Use the term *validated learning*
- Reference the Build-Measure-Learn loop
- Describe what happens when a PRD's Problem section is weak or assumed

*(Tests: Problem section priority; validated learning; Build-Measure-Learn loop)*

---

**Exercise 12** *(Cumulative — Prior Chapter Concept)*

Chapter 3 argued that the archetype creates brand coherence by generating consistent decisions and refusals. Chapter 4 argues that the MVP Boundary generates scope coherence by naming explicit refusals ($100,000 nos) before building begins.

Explain the structural parallel between these two concepts:
1. What does the archetype's forcing function do that the MVP Boundary also does?
2. What is the structural consequence in both cases when the forcing function is not named — when the archetype is vague and when the MVP Boundary is absent?
3. What does this parallel suggest about the relationship between brand strategy and product requirements?

*(Tests: MVP Boundary as scope discipline; integrates Ch. 3 archetype forcing function with Ch. 4 scope discipline)*

---

**Exercise 13** *(AI Interaction — with verification requirement)*

First, write your own answer to this question without consulting AI:
"What is the difference between a user requirement and an implementation decision in a PRD? Why does the distinction matter for an AI tool?"

Then ask an AI assistant the following prompt:
*"When writing a Product Requirements Document for an AI tool, what is the difference between what the product should do and how the product should do it? Give three examples of statements that cross the line from requirements into implementation decisions."*

When you receive the response:
1. Identify the strongest point in the AI's response.
2. Identify the most significant error, gap, or oversimplification. Explain why it is wrong using the chapter's vocabulary.
3. Write a corrected version of the problematic statement.
4. State the specific test you would apply to any PRD statement to determine whether it is a what or a how.

*(Tests: What/how distinction — Cagan's rule; AI interaction with critical evaluation)*

---

**Exercise 14** *(Build-Measure-Learn Application)*

A team builds an AI tool that generates first-draft investor update emails from raw notes. They run their first Build-Measure-Learn cycle. Below are five pieces of data they collected:

| Data point | What was measured |
|---|---|
| 68% of users who generated a draft opened it within 2 minutes of generation | Immediate engagement behavior |
| When surveyed, 85% of users said they would "definitely recommend" the tool | Stated intent |
| 12% of users edited the draft for more than 10 minutes before sending | Deep editing behavior |
| Users who sent the generated draft without editing sent it 40% faster than their pre-tool baseline | Time-to-send change |
| In interviews, 7/10 users said they wished the tool would "also summarize the last update for comparison" | Feature request stated intent |

For each data point:
1. Classify it as validated learning or stated intent
2. Explain what action, if any, the team should take based on this data point
3. For stated-intent data points, explain what behavioral measurement would validate or invalidate the stated intent

*(Tests: Validated learning vs. stated intent; Build-Measure-Learn loop)*

---

**Exercise 15** *(Scope Discipline — Linear Case Analysis)*

The chapter uses Linear's development approach as a case study in scope discipline. Consider the following three product decisions a competitor "Velocity" might have made while Linear was applying its methodology:

- Velocity added a calendar integration when three enterprise customers requested it (took 3 weeks)
- Velocity added a time-tracking feature when one customer's CTO mentioned it on a call (took 6 weeks)
- Velocity added a mobile app when their marketing team argued it would increase sign-ups (took 12 weeks)

For each decision:
1. Identify the specific scope discipline principle from the chapter that Velocity violated
2. Estimate the compounding cost of the decision — not in money, but in what the engineering team could not do while building that feature
3. Predict the brand consequence using the chapter's framing — not "they wasted time" but the specific brand signal the decision sends

*(Tests: Scope discipline compounding; Linear Method; brand consequence of scope creep)*

---

**Exercise 16** *($100,000 No Application)*

You are reviewing a PRD for an AI tool that monitors a company's customer support tickets, classifies them by urgency, and surfaces the top 10 issues to a product manager each morning.

The product team has received the following requests and is considering adding them to v1:
1. A customer success manager requests real-time Slack alerts for every ticket marked "urgent"
2. An enterprise prospect offers to pay $50,000 for a feature that exports ticket summaries to their proprietary CRM (SalesConnect)
3. The CTO requests that the tool also monitor internal GitHub issues and Jira tickets alongside customer support
4. A product manager requests a trend-line dashboard showing ticket volume over the past 30 days

For each request:
1. Apply the $100,000 no concept: should this be a $100,000 no, or should it be included in v1?
2. State your reasoning in one sentence per request
3. For each request you accept: verify it does not violate the MVP Boundary of "monitoring customer support tickets, classifying urgency, surfacing top 10 issues"
4. For each request you decline: write the specific language you would put in the MVP Boundary section to make this a documented $100,000 no

*(Tests: $100,000 no concept; MVP Boundary — applied judgment)*

---

## Tier 3 — Synthesis (Exercises 17–19)

*Bloom's Level: Synthesize / Evaluate*
*Purpose: Combine concepts from this chapter with prior chapters, or evaluate the chapter's own claims critically. These require extended reasoning. Budget 20–30 minutes each.*

---

**Exercise 17** *(Cross-Chapter Synthesis — Chs. 3 and 4)*

Chapter 3 argued that the Sage archetype's shadow is dogmatism — the archetype's drive toward depth and rigor, taken too far, produces rigidity. Chapter 4 argues that scope discipline is a product virtue — refusing features that would dilute the MVP boundary makes a better product.

A classmate argues: "These two chapters are in tension. Chapter 3 says the Sage archetype refuses things because of identity — because being a Sage means not doing certain things. Chapter 4 says you should refuse things because of scope discipline — because keeping the scope tight makes the product better. These are different reasons to refuse the same things. A Sage-archetype founder who builds a tightly scoped product might look like they're practicing both virtues, but they could be doing it for either reason. The reasons are different even if the behaviors look the same."

Evaluate this argument. Is the classmate correctly identifying a real tension, or are the two frameworks compatible? Your response should:
- Use specific concepts from both chapters
- Determine whether the two motivations (identity vs. scope discipline) produce different decisions in any case
- Conclude with a precise statement about the relationship between archetype-driven refusals and PRD-driven scope discipline

*(Tests: Archetype forcing function; MVP Boundary; integrates Ch. 3 and Ch. 4)*

---

**Exercise 18** *(Cross-Chapter Synthesis — Chs. 1 and 4)*

Chapter 1 introduced the four-verb framework: Ideate, Build, Brand, Ship. The chapter placed these in sequence, with Build following Ideate. Chapter 4 is the Build chapter — specifically, the document that governs what gets built.

A student argues: "The PRD is part of Ideate, not Build. You write the PRD before you build anything. The PRD is the idea, and building is the execution. So the four-verb framework puts the PRD in the wrong place."

Evaluate this argument. Is the student right that the PRD belongs in Ideate rather than Build? What does this question reveal about the relationship between the two verbs? Your response must use the chapter's framing of the Build-Measure-Learn loop and the validated learning concept to argue for where the PRD actually sits in the creative engineer's workflow.

*(Tests: Four-verb framework position of PRD; Build-Measure-Learn loop — integrates Ch. 1 and Ch. 4)*

---

**Exercise 19** *(Evaluation — Chapter's Own Claim)*

The chapter argues that naming the $100,000 no before building begins is a discipline that prevents scope creep. The Linear Method is offered as evidence that scope discipline produces better products.

A product manager challenges this: "The $100,000 no is a premature optimization. You don't know what to refuse until you've talked to users and built something. Naming refusals before building means you refuse the wrong things — you refuse the features that turn out to matter and build the features that turn out not to. A better approach is to build quickly, measure what users actually do, and then refuse features based on what the data says. The Build-Measure-Learn loop is better than the PRD because the loop uses evidence and the PRD uses guesses."

Evaluate this argument:
1. What is the product manager getting right?
2. What is the product manager getting wrong about the relationship between the PRD and the Build-Measure-Learn loop?
3. Does the chapter present these as alternatives or as complementary? What is the evidence for your reading?

*(Tests: PRD structure; Build-Measure-Learn loop; $100,000 no — stress-tests the chapter's own framing)*

---

## Tier 4 — Challenge (Exercise 20)

*Bloom's Level: Evaluate / Create*
*Purpose: Produce original analysis that extends the chapter's framework into a new domain. There is no single correct answer. Assessment is by rubric.*

*No model answer is provided for Tier 4 exercises. Assessment uses the rubric below.*

---

**Exercise 20** *(Capstone — PRD for Your AI Tool)*

Write a complete one-page PRD for the AI tool you are building in this course. The document should be specific enough that a developer who has never met you could understand what to build and what not to build.

Your PRD must include:
1. **Problem** — 2–4 sentences. Specific person, specific problem, specific cost. No generic "people need X" statements.
2. **Gap** — 1–2 sentences. Why existing tools (name at least one real competitor or substitute) do not solve this problem for this person.
3. **Tool** — 1–3 sentences. What the tool does. No implementation decisions (no model names, no framework choices, no database names).
4. **MVP Boundary** — 4–6 specific items in scope for v1. At least two explicit $100,000 nos — features you are declining even if a stakeholder asks. The boundary should be testable: a reader should be able to look at any proposed feature and determine, from the boundary alone, whether it is in or out of scope.
5. **Validated learning plan** — 2–3 sentences. What behavioral data (not survey responses) will you collect in the first two weeks after launch to determine whether the tool is solving the problem? Name the specific behavior you will measure.

**Rubric:**

| Criterion | Strong | Adequate | Weak |
|---|---|---|---|
| Problem specificity | Names a specific person, specific problem, measurable cost — no generic "users need" language | Names a person and problem but cost is vague or general | Generic problem statement; could apply to any tool |
| What/how distinction | No implementation decisions appear in Problem, Gap, or Tool sections | One or two how statements slip in, but Tool section is mostly clean | Tool section reads like an architecture decision or tech stack choice |
| $100,000 no quality | Two or more $100,000 nos are specific, testable, and genuinely costly to decline | One $100,000 no is specific; the other is vague or trivially not worth building | No explicit $100,000 nos, or nos that apply only to things nobody was asking for |
| MVP Boundary testability | A reader can determine in/out for any proposed feature without asking the author | Most features can be classified but some boundary cases are ambiguous | Boundary is a list of features without scope logic |
| Validated learning plan | Names a specific behavior to measure (not a survey); explains what pass/fail looks like | Names a behavior but does not specify what constitutes evidence of success | Describes a survey or interview rather than a behavioral measurement |

---

## Answer Key

> Attempt all exercises before reading this section.

---

**Exercise 1**
*Model answer:*
1. Problem — identifies who has a problem and what it costs them
2. How — implementation decision; LangChain is a technical choice, not a requirement
3. Gap — explains why existing tools do not solve this problem for this person
4. MVP Boundary — documents a $100,000 no (multi-user support)
5. Tool — describes what the tool does, with no implementation choices
6. How — PostgreSQL, Supabase, and row-level security are all implementation decisions
*Common error:* Students classify statement 5 as "Tool" correctly but classify statement 1 as "Gap" because it mentions competitors implicitly. The Problem section is about the person and the cost; the Gap section is specifically about why existing tools don't solve it.
*Chapter reference:* Four PRD Sections — Ch. 4

---

**Exercise 2**
*Answer:* False
*Model answer:* Validated learning means the team learned something from user *behavior* — what people did with the product — not from what users said they wanted. Stated intent (what users say in surveys or interviews) is systematically unreliable as a measure of what users will actually do; behavior under real conditions is the valid evidence.
*Common error:* Students treat user interviews and surveys as validated learning because they feel like evidence. The chapter's distinction is that stated intent predicts stated intent, not behavior. Only behavior predicts behavior.
*Chapter reference:* "Validated Learning" — Ch. 4

---

**Exercise 3**
*Model answer:* Cagan's rule states that a PRD describes what the product does — the requirements — and explicitly excludes how the product does it. The how decisions belong in the implementation phase, not in the requirements document. A PRD statement that violates Cagan's rule: "The tool will use OpenAI's GPT-4o API to classify competitor news articles into three sentiment categories." The implementation decision (GPT-4o, OpenAI API) is embedded in the requirement. A PRD statement that follows Cagan's rule: "The tool classifies competitor news articles into three sentiment categories (positive, neutral, negative)." The what (classification into three categories) is specified; the how (which model, which API) is not.
*Common error:* Students write "the tool will use AI to classify" thinking this is neutral — but naming a class of technology (AI, ML, NLP) is still a how statement. "Classify" is the what; "AI" is an approach.
*Chapter reference:* What/how distinction (Cagan's rule) — Ch. 4

---

**Exercise 4**
*Model answer:*
1. The $100,000 no is a feature or capability the team commits to not building in the current scope, even if a stakeholder offered $100,000 to add it. It is named before building begins.
2. Naming it before building matters because scope creep is hardest to resist when a stakeholder is present and enthusiastic. Pre-committing to a refusal removes the in-the-moment pressure — the decision is already made.
3. Without a named $100,000 no, every stakeholder request becomes a negotiation under pressure. The scope expands incrementally, each addition feels small, and the compounding cost accumulates before the team recognizes it. The chapter's description: each added feature makes the next decision harder, because the team has less time, less focus, and more to maintain.
*Common error:* Students describe the $100,000 no as a business strategy (we don't want to build that feature) rather than as a scope-discipline tool (we need to pre-commit to a refusal so we can hold the line under pressure).
*Chapter reference:* $100,000 no — Ch. 4

---

**Exercise 5**
*Model answer:* Linear's core principle is scope discipline — shipping less, better, on a fixed cadence, rather than shipping more in response to every request. The specific product decision: Linear declined to build enterprise features (single sign-on, admin controls, custom fields) until the core issue-tracking experience was validated by paying users. The brand consequence: this decision positioned Linear as a product for teams that care about craft — developers and PMs who found existing tools (Jira, Asana) overbuilt and under-focused. The refusal of enterprise complexity was itself a brand signal that attracted the audience Linear wanted. The brand consequence of scope discipline was not just a better product; it was a more legible brand identity.
*Common error:* Students describe Linear's decisions as engineering choices (fewer features = faster code) without connecting them to the brand signal they sent. The chapter argues that scope discipline is a brand decision as well as an engineering decision.
*Chapter reference:* Linear Method case study — Ch. 4

---

**Exercise 6**
*Model answer:*
1. **Failure mode — vanity metric.** Open rate measures whether users saw the email; it does not measure whether the content was valuable or whether they took action based on it. This is a vanity metric masquerading as validated learning.
2. **Failure mode — stated intent.** "Would you pay for X?" is the canonical stated-intent trap. Users consistently overestimate their willingness to pay in surveys; only revealed preference (actually paying) validates willingness to pay.
3. **Correctly running Build-Measure-Learn.** The team measures a behavioral signal (linking Slack within 7 days), establishes a threshold, and acts on the measurement. This is validated learning.
4. **Failure mode — single-stakeholder scope expansion.** Adding a feature because "one enterprise stakeholder said it would be useful" is the stated-intent trap at the stakeholder level. The measurement required is whether users actually use the feature after it is built.
5. **Correctly running Build-Measure-Learn.** Daily return visits is a behavioral measure of habit formation — it measures what users do, not what they say.
*Common error:* Students classify open rate (item 1) as validated learning because it feels like a real metric. The chapter's test: does the metric measure behavior that directly indicates the problem is being solved? Open rate does not.
*Chapter reference:* Validated learning vs. stated intent; Build-Measure-Learn — Ch. 4

---

**Exercise 7**
*Model answer:* Scope creep compounds because each added feature creates maintenance burden, increases cognitive load for the development team, and dilutes focus for the next decision. When the MVP Boundary is set early, it creates a reference point for every subsequent feature request: the question changes from "is this a good idea?" to "is this inside the boundary?" The boundary makes the answer cheaper to arrive at and harder to debate. Without the boundary, every request is evaluated in isolation — and most requests are good ideas in isolation, which is exactly why they are hard to refuse. The boundary is protective because it moves the refusal decision from the moment of request (when pressure is highest) to the planning phase (when pressure is lowest).
*Common error:* Students describe scope creep as a quantity problem (too many features) rather than a decision-making problem (the absence of a reference point that makes individual decisions harder to resist).
*Chapter reference:* Scope discipline compounding; MVP Boundary — Ch. 4

---

**Exercise 8**
*Model answer:* The Madison PRD library is a shared repository of PRDs for the different tools in the Madison multi-agent architecture, maintained as a reference for what each tool does and does not do. The problem it solves: in a multi-agent system, individual agents need to know the scope of adjacent agents — what they can ask for and what they cannot expect. A single PRD for an individual tool solves the scope problem for that tool; the library solves the coordination problem for the system of tools. Without the library, agents make scope assumptions about adjacent agents that may be wrong, producing failures at the integration boundaries.
*Common error:* Students describe the Madison PRD library as a template for writing PRDs rather than as a shared reference that enables multi-agent coordination. The library's function is coordination, not standardization.
*Chapter reference:* Madison as PRD library — Ch. 4

---

**Exercises 9–16**
*Tier 2 — model answers are scenario-dependent and are not abbreviated here. Evaluation criteria:*
- Ex 9: Four sections present; no how statements; explicit $100,000 no named
- Ex 10: All four sections corrected; what/how violations identified by section; scope in MVP Boundary reduced to ≤4 items
- Ex 11: Uses validated learning; describes the Build-Measure-Learn loop; identifies downstream consequence of weak Problem section
- Ex 12: Names the structural parallel (forcing function = exclusion rather than prescription); identifies what fails when neither is named; concludes with a precise statement
- Ex 13: Strongest point acknowledged; AI error identified with chapter vocabulary; corrected version provided; verification test stated
- Ex 14: Behavioral data = validated learning; survey/interview data = stated intent; each stated-intent item paired with a behavioral validation measurement
- Ex 15: Three specific Linear principles identified; compounding cost framed as opportunity cost, not money; brand signal named for each
- Ex 16: $100,000 no reasoning stated per item; accepted items verified against MVP Boundary; declined items have documented boundary language

---

**Exercises 17–19**
*Tier 3 — No abbreviated model answer. Evaluation criteria:*
- Ex 17: Identifies whether archetype refusals and scope refusals produce different decisions in any case; argues for compatibility or tension with evidence from both chapters; ends with precise synthesis claim
- Ex 18: Argues convincingly for where the PRD sits in the four-verb framework using Build-Measure-Learn as evidence; acknowledges the student's point before refuting it
- Ex 19: Correctly identifies what the PM is getting right (loop uses evidence); correctly identifies what is wrong (PRD and loop are complementary, not competing); cites chapter evidence for the relationship

---

**Exercise 20**
*Tier 4 — No model answer. Assessment by rubric in the exercise.*

---

## Self-Assessment Rubric

After reviewing the answer key, evaluate your work:

| Score | Meaning | Next step |
|---|---|---|
| Tier 1: 6–8 correct | Core vocabulary in place | Move to Tier 2 |
| Tier 1: 4–5 correct | Gaps in foundational concepts | Return to Ch. 4 sections on PRD structure and what/how before Tier 2 |
| Tier 2: 6–8 mostly correct | Applying framework well | Attempt Tier 3 |
| Tier 2: 4–5 mostly correct | Gaps in application | Redo Ex 9 and Ex 10 with answer key visible; re-attempt others |
| Tier 3: 2–3 strong | Synthesis developing | Proceed to Tier 4 |
| Tier 3: 0–1 strong | Integration needs work | Re-read answer key rationales; review prior chapters' connection points |

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

*Ex 1 (Contrastive classification):* The most common errors are classifying how statements as Tool (because they describe what the tool does, just with implementation details) and missing that the Gap section is specifically about existing alternatives rather than general market need.

*Ex 6 (Build-Measure-Learn failures):* The vanity metric case (open rate) is the most important exercise in this tier — open rate is the most commonly cited engagement metric and the most commonly misused. Build in class discussion time for why open rate is not validated learning.

*Ex 9 (PRD writing):* Evaluate using three criteria from the rubric: no how statements in the Tool section, specific $100,000 no named (not just "we won't build X if nobody asks"), and MVP Boundary testable. Have students exchange PRDs and attempt to classify proposed features using only the partner's boundary — if they cannot, the boundary is not testable.

*Ex 10 (Error analysis):* The deliberate errors are distributed across all four sections. Do not accept a response that only corrects the MVP Boundary — all four sections need correction.

*Ex 12 (Cumulative — Chs. 3 and 4):* This exercise requires the insight that both the archetype forcing function and the $100,000 no are pre-commitment mechanisms — they move a refusal decision from the pressure moment to the planning moment. Students who miss this parallel have not yet integrated the two chapters.

*Ex 20 (Tier 4):* Grade the validated learning plan most strictly. Students consistently propose surveys or interviews as their measurement mechanism — mark this as "Weak" on the validated learning criterion and require revision. The validated learning plan must name a behavior.

**Common errors to watch for:**
- Writing Tool sections that name the AI model (GPT-4, Claude) as a requirement rather than an implementation choice
- Writing $100,000 nos that no one was going to ask for anyway (trivially inexpensive refusals)
- Treating user interview data as validated learning
- Describing scope discipline as an engineering concern without connecting it to brand coherence

**DEI note:**
All scenarios in this exercise set have been written to avoid cultural, regional, or socioeconomic assumptions about tool users, founders, or industry context.
