# Chapter Quiz: Interface Design and Deployment

*Chapter 7 of Branding and AI (INFO 7375)*

> **Instructions:** Attempt every question before checking the answer key.
> Do not look at the answers while working — the act of retrieval is the
> learning. If you are unsure, make your best attempt and mark it with (?).
> Review the answer key after completing all questions, not after each one.

---

## Learning Objectives Covered

This quiz assesses the following chapter objectives:

- LO 1 — Distinguish the four layers of interface and explain why failures on layer four are most costly.
- LO 2 — Diagnose interface-brand misalignment, naming the specific promise and the specific system behavior that breaks it.
- LO 3 — Select between Streamlit and Gradio for a given interaction model and justify the selection.
- LO 4 — Apply the three alignment disciplines to a tool's interface.
- LO 6 — Conduct a pre-ship alignment audit.

---

## Section 1 — Recall and Recognition (Questions 1–5)

*Target: Bloom's Remember / Understand*
*Format: Multiple-choice (3 options) and True/False*
*Target difficulty: p = 0.77–0.85*

---

**Question 1** *(Multiple-Choice)*

The chapter describes the Google Bard February 2023 demo failure as the primary case study for interface-brand misalignment. Which of the three misalignment types does it represent?

A) Capability misalignment — the interface implied the tool could perform tasks it could not reliably execute
B) Confidence misalignment — the interface presented output as more certain than the system actually was
C) Tone misalignment — the interface used a register the underlying system could not maintain

---

**Question 2** *(Multiple-Choice)*

A tool's URL is `https://share.streamlit.io/user/abc123xyz`. According to the chapter's four-layer framework, which layer does this affect, and how?

A) Layer 1 (visual surface) — the alphanumeric URL degrades the visual quality of the tool's landing page
B) Layer 3 (deployment surface) — the random alphanumeric string communicates something different about the tool's legitimacy than a named domain would
C) Layer 4 (brand surface) — the URL appears in error messages and undermines the tool's tone

---

**Question 3** *(True/False)*

According to the chapter, confidence misalignment is best fixed by improving the underlying AI system's accuracy before shipping the interface.

☐ True  ☐ False

---

**Question 4** *(Multiple-Choice)*

According to the chapter's framework for selecting between Streamlit and Gradio, which decision criterion determines the correct choice?

A) The developer's familiarity with Python libraries — Streamlit has a simpler API for beginners
B) The interaction model — whether the user's primary job is to "do work" with a tool or to "try the model"
C) The deployment target — Streamlit Community Cloud is free while Gradio requires a Hugging Face account

---

**Question 5** *(True/False)*

The chapter argues that interface quality compounds where feature quality does not, because users encounter the interface on every session but only encounter a specific feature a few times.

☐ True  ☐ False

---

## Section 2 — Application and Analysis (Questions 6–9)

*Target: Bloom's Apply / Analyze*
*Format: Multiple-choice (3 options) and Short-Answer*
*Target difficulty: p = 0.50–0.70*

---

**Question 6** *(Scenario-Based Multiple-Choice)*

A student builds an AI tool that takes a company name and returns a competitive intelligence report based on the last 30 days of news coverage from three pre-configured RSS feeds and the Google News API. The tool's interface includes a free-text prompt box with the label "Ask me anything about your competitors" and a button labeled "Research." A beta user types "What is Company X's patent strategy over the last five years?" and receives a response that is confident but only covers the last 30 days. Using the chapter's misalignment taxonomy, what is the primary failure and what is the minimum interface fix?

A) Tone misalignment — the "ask me anything" copy sets a conversational expectation the structured pipeline cannot match; fix by removing casual phrasing from the interface copy
B) Capability misalignment — the free-text prompt implies general research capability the system does not have; fix by replacing the free-text box with a structured input that reflects the system's actual scope and adding a note specifying the 30-day coverage window
C) Confidence misalignment — the output does not hedge adequately; fix by adding a "verify this report" footer

---

**Question 7** *(Short-Answer)*

The chapter's alignment audit example for the sentiment analysis pipeline identifies five implicit claims and fixes three of them without changing the underlying system. What is the chapter's principle for how interface misalignment should be fixed — specifically, which direction do fixes go (interface toward the system, or system toward the interface), and why?

*Your answer:*

_____________________

---

**Question 8** *(Multiple-Choice)*

In the Microsoft Tay case, the chapter identifies the capability misalignment as "structural." What does the chapter mean by this, and how does it differ from a capability misalignment caused by a system bug?

A) A structural misalignment means the system code contained a flaw that could be patched; a bug-caused misalignment requires a full rebuild
B) A structural misalignment means the architecture itself could not deliver the claimed capability for the actual deployment population — even a perfectly functioning system would fail because the capability the interface implied was incompatible with open public input
C) A structural misalignment affects all users uniformly; a bug-caused misalignment affects only specific input types or edge cases

---

**Question 9** *(Short-Answer)*

The chapter introduces the "alignment audit" as a two-column exercise. Describe the content of each column and explain what a row where the right column says "sometimes" or "not for this kind of user" requires the engineer to do before shipping.

*Your answer:*

_____________________

---

## Section 3 — Synthesis and Evaluation (Questions 10–11)

*Target: Bloom's Evaluate / Create*
*Format: Brief-Response*
*Target difficulty: p = 0.30–0.50*

---

**Question 10** *(Brief-Response)*

The chapter distinguishes Layer 4 (brand surface) from Layers 1–3 and argues that failures on Layer 4 are more costly. A designer argues: "Layer 4 is a consequence of Layers 1–3 being well-designed. If the visual surface, interaction model, and deployment surface are all coherent and accurate, the brand surface takes care of itself — you don't need to design it separately." Evaluate this argument using the Bard and Snapchat cases.

*Your response (2–4 sentences):*

_____________________

---

**Question 11** *(Transfer — Brief-Response)*

An emergency dispatch software company wants to add an AI feature that suggests which emergency unit to dispatch based on incoming 911 call transcripts. The feature's interface design team is debating between two options: (A) a Gradio-style interface where the dispatcher types the call summary and sees the AI's top recommendation instantly, or (B) a Streamlit-style structured interface with input fields for incident type, location, caller description, and available units — then a ranked recommendation with a confidence score and a one-sentence explanation for each suggestion. Apply the chapter's four-layer interface analysis and alignment disciplines to recommend one option, naming the specific capability claims, confidence signals, and failure mode considerations that drive the choice.

*Your response (2–4 sentences):*

_____________________

---

## Answer Key

> Read this section only after completing all questions.

---

**Q1 — B**
*Correct because:* The chapter explicitly classifies Bard as a confidence misalignment case: "The interface — polished, confident, presented at a Google press event — promised a system capable of accurate, verified, trustworthy responses, and the error exposed that the system was a research preview." The chapter also states: "The interface's confidence level has to be calibrated to the system's actual reliability. A research preview should look like a research preview, not like a finished Google product." The error itself was a research error, but the damage came from the confident presentation — bullet points with no source citations, no hedging, no uncertainty.
*Why the distractors are wrong:*
- A) Capability misalignment is the Tay case — the interface implied a system capable of safe public learning that could not handle adversarial inputs.
- C) Tone misalignment is the Snapchat case — a visual and interaction model redesign that broke the brand's existing relationship with users.
*Chapter reference:* Section 2 — Confidence Misalignment; Section 3 — Google Bard, February 2023

---

**Q2 — B**
*Correct because:* The chapter identifies Layer 3 (deployment surface) as "what the user encounters before the UI loads" and explicitly includes "the URL itself — a random alphanumeric string on a free tier says something different than a named domain." The chapter frames the deployment surface as the layer that answers the user's "is this real?" question before they have seen the visual interface.
*Why the distractors are wrong:*
- A) The URL is part of Layer 3 (deployment surface), not Layer 1 (visual surface), which covers buttons, forms, layouts, colors, and typography rendered inside the tool.
- C) The chapter attributes Layer 4 (brand surface) to error messages, empty states, confidence signals, and tone in copy — not to the URL structure.
*Chapter reference:* Section 1 — Layer 3: The deployment surface

---

**Q3 — False**
*Correct because:* The chapter explicitly states the fix direction: "The fix is not to make the system more accurate. The fix is to make the interface honest about the system's accuracy." The chapter lists interface-level fixes: "Confidence scores, 'verify with source' footers, 'this answer may not be complete' banners on edge cases — any of these costs almost nothing to implement and repairs the misalignment at the UI layer rather than requiring a system overhaul."
*Chapter reference:* Section 2 — Confidence Misalignment

---

**Q4 — B**
*Correct because:* The chapter's decision rule is: "Ask: what is the user's job when they use this tool? If the user's job is to *do work* — choose Streamlit. If the user's job is to *try the model* — choose Gradio." Both Streamlit Community Cloud and Hugging Face Spaces are described as free tiers, so deployment cost is not a differentiating factor.
*Why the distractors are wrong:*
- A) Developer familiarity is not mentioned as the decision criterion; the chapter frames the choice as an interaction model decision, not a preference decision.
- C) Both platforms have free tiers; the chapter explicitly states both are "sufficient for a course project," so this is not a differentiating factor.
*Chapter reference:* Section 4 — How to Choose

---

**Q5 — True**
*Correct because:* The chapter states this mechanism explicitly: "interface quality compounds where feature quality does not. A confusing feature is noticed once and avoided. A confusing interface is re-encountered on every visit, degrading the relationship with the tool every time. A misaligned interface — one that promises things the system cannot deliver — compounds *against* you: each session confirms that the tool cannot do what it appeared to offer."
*Chapter reference:* Why This Chapter

---

**Q6 — B**
*Correct because:* The chapter's definition of capability misalignment is: "The interface implies the tool can do things it cannot reliably do." A free-text prompt labeled "Ask me anything about your competitors" implies general conversational research capability across any time range. The system can only process 30-day news coverage from three sources — a much more limited scope. The chapter's fix principle for capability misalignment is: "make the interface describe what the system can actually do, with enough specificity that the user's mental model matches the system's actual capability." A structured input replacing the free-text box and an explicit 30-day coverage note achieve this.
*Why the distractors are wrong:*
- A) Tone misalignment concerns the register (warm vs. formal) of the output, not the scope of capability implied by the interaction model.
- C) Adding a "verify this report" footer addresses confidence, not the more fundamental problem that the user asked a five-year question and got a 30-day answer.
*Chapter reference:* Section 2 — Capability Misalignment

---

**Q7 — Short-Answer**
*Model answer:* The chapter's principle is that interface fixes go in the direction of the interface toward the system — not the system toward the interface. The chapter states: "Do not fix the system — that comes later, in the Build-Measure-Learn loop. Fix the interface now, so the system and the interface are making the same promises." The reasoning is that changing the system is expensive and requires another iteration of the build cycle; the goal before shipping is to ensure what the user sees is honest about what the system can do. The alignment audit's explicit design philosophy is: narrow the claim, add a qualifier, restrict the input, or add an uncertainty signal — all of these modify the interface, not the system.
*What a strong answer includes:*
- The direction (interface toward system, not system toward interface)
- The reason (system changes are expensive; interface changes are cheap)
- The chapter's explicit instruction: "Do not fix the system — that comes later, in the Build-Measure-Learn loop"
*Chapter reference:* Section 5 — The Alignment Audit

---

**Q8 — B**
*Correct because:* The chapter describes Tay's misalignment as structural: "the interface implied a system that could safely learn from arbitrary public input. The system could not... Every tweet at Tay was a capability test. The capability failed immediately and completely." The chapter contrasts this with a system bug: Tay's learning mechanism was working correctly — it was learning from the inputs it received. The capability the interface implied (safe, beneficial learning from any public user) was architecturally incompatible with open public access, not broken by a code error.
*Why the distractors are wrong:*
- A) A structural misalignment cannot be patched at the code level; the chapter's account makes clear the issue was the interface's implied capability being incompatible with the deployment population, not a code defect.
- C) The chapter does not frame structural misalignment as affecting all users uniformly; Tay's failure was triggered by adversarial users specifically, not by all users.
*Chapter reference:* Section 3 — Microsoft Tay, March 2016

---

**Q9 — Short-Answer**
*Model answer:* The left column lists every implicit promise the interface makes — not what the README or pitch says, but what a user will infer from the visual surface, interaction model, deployment surface, and brand surface. The right column asks: "Can the underlying system keep this promise, reliably, for the population of users who will use the tool?" When the right column answer is "sometimes" or "not for this kind of user," the chapter requires the engineer to fix the interface before shipping: "Remove the claim, add a qualifier, narrow the input, or add an explicit uncertainty signal." The chapter is explicit that this is done before deployment, not retrospectively after users encounter the mismatch.
*What a strong answer includes:*
- Left column content: implicit promises inferred from all four interface layers
- Right column content: system capability check per promise
- The required response to "sometimes" or "not for this kind of user": fix the interface, not the system, before shipping
*Chapter reference:* Section 5 — The Alignment Audit

---

**Q10 — Brief-Response**
*Model answer:* The designer's argument fails on both case studies. In the Bard case, Layers 1–3 were well-executed — the visual surface was polished, the interaction model was clear, the deployment was professional — and the failure was entirely on Layer 4 (brand surface): confident bullet points with no source attribution or hedging. All three prior layers being coherent did not prevent the Layer 4 failure. In the Snapchat case, the interface redesign was competent on Layers 1–3 (the new visual surface worked, the interaction model was valid, the deployment was standard), but the brand surface had changed the signal Snapchat sent to its existing users — from "private, ephemeral, personal" to "organized content platform." Layer 4 must be designed explicitly, not inherited from the quality of the other layers.
*What a strong answer includes:*
- Evidence from both cases that Layers 1–3 being good did not prevent Layer 4 failure
- The specific Layer 4 element that failed in each case (Bard: overconfident copy; Snapchat: brand-signal change)
- The conclusion that Layer 4 requires deliberate design
*Chapter reference:* Section 3 (Bard, Snapchat cases); Section 1 (Layer 4 description)

---

**Q11 — Transfer Brief-Response**
*Model answer:* Option B (Streamlit-style structured interface) is the appropriate choice for this context. The dispatcher's job is to "do work" — assess an emergency and make a dispatching decision — which maps to Streamlit's interaction model for structured, reliable, inspectable outputs rather than Gradio's model-probe pattern. More critically, the chapter's three alignment disciplines all point toward Option B: surfacing uncertainty is essential (confidence scores and explanations allow the dispatcher to override when the AI's confidence is low), matching capability claims (structured input fields specify exactly what the system takes in, preventing over-inference from an open prompt), and making error states recoverable (a ranked list with explanations is auditable; an instant top recommendation is not). Option A's Gradio-style "type and see" interface implies general conversational dispatch intelligence the system does not have and hides the AI's reasoning from the dispatcher at a moment when that reasoning is legally and operationally critical.
*What a strong answer includes:*
- Framework choice (Streamlit) with the chapter's interaction-model rationale
- At least two of the three alignment disciplines applied to the scenario
- The failure mode of Option A identified using chapter vocabulary
*Chapter reference:* Section 4 (Streamlit vs. Gradio); Section 2 (three alignment disciplines); Section 5 (alignment audit)

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

- Classifying Bard as capability misalignment (the error was factual) rather than confidence misalignment (the interface presented uncertain outputs as certain). Q1 directly probes this.
- Believing the fix for interface misalignment is to improve the system rather than adjust the interface. Q3 and Q7 both target this.
- Treating the Streamlit/Gradio choice as a preference rather than an interaction model decision. Q4 targets this.

**Signs a student needs to return to the chapter before this quiz:**

- Cannot name all four interface layers in order and assign a concrete example to each.
- Cannot distinguish the three misalignment types using the case studies (Bard = confidence, Snapchat = tone, Tay = capability).

**Scaffolding adjustments:**

- *For students who score below 5:* Return to Sections 1 (four layers), 2 (three misalignment types), and 5 (alignment audit). Read each case study in Section 3 with the specific misalignment type in mind before re-reading Section 2's definitions.
- *For students who score 10/10 on first attempt:* Attempt Exercise C2 from the chapter — design a pre-deployment testing protocol for an AI tool intended for public use, including adversarial test cases. This extends the Tay case analysis to a protocol-design problem.

**Grading weight guidance (if used for credit):**
- Section 1 MCQ items: 0.25–0.5% of final course grade each
- Section 2 Short-Answer items: 0.5–1.0% each
- Section 3 Brief-Response items: up to 2.5% each
- Collectively, chapter quizzes should not exceed 5% of overall course grade
