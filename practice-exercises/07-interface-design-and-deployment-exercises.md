# Practice Exercises — Chapter 7: Interface Design and Deployment

**Course:** INFO 7375 — Branding and AI
**Chapter:** 07 — Interface Design and Deployment
**Exercise File Version:** 1.0

---

## How to Use These Exercises

Work through tiers in order. Tier 1 builds vocabulary; Tier 2 builds application skill; Tier 3 requires synthesis across the full chapter; Tier 4 is a capstone design task with no model answer. Check your answers against the Answer Key before moving to the next tier.

---

## Worked Example

**Scenario:** You are reviewing the interface design for a deployed AI writing assistant called *DraftBot*. The tool uses GPT-4 internally, but the interface presents every generated sentence with 100% confidence: no hedging language, no uncertainty signals, no indication that outputs may be wrong. The visual design is minimal and authoritative — a clean white background, bold typography, and no disclaimer text anywhere. Users report trusting the tool's output implicitly and publishing articles without revision.

**Task:** Identify which of the three misalignment types is present, name the layer where the misalignment lives, and explain the failure mechanism using chapter vocabulary.

**Model Answer:**

**Misalignment type:** Confidence misalignment. The interface presents AI output as more certain than the model actually is. GPT-4 has well-documented hallucination rates; no language model produces 100%-reliable prose. The interface communicates certainty (through its visual register and absence of hedging) that the underlying model cannot deliver.

**Layer:** Brand surface — the tone and visual register of the interface. The clean, authoritative aesthetic encodes a promise of reliability that the model cannot keep. Misalignment also exists at the interaction model layer: the interaction pattern (generate → display → done) skips any verification step that would make model uncertainty legible to the user.

**Failure mechanism:** Users calibrate trust to the interface signal, not to the model's actual capability. When users publish unrevised AI output, the errors that surface publicly attach to the user's professional reputation, not to DraftBot's. The trust collapse, when it comes, is swift — users who have been burned once rarely return. The Google Bard 2023 case in the chapter illustrates the same mechanism at scale: a single factual error in a demo cost Alphabet $100 billion in market cap in a single session, because the interface had primed observers to expect reliable, authoritative output.

**Fix:** Apply the chapter's alignment audit. The right column should specify: hedging language on all generated outputs ("suggested draft — review before publishing"), a confidence indicator on AI-generated sentences, and a visual register (softer typography, a "generated" badge) that signals "starting point" rather than "final answer."

---

## Tier 1 — Remember and Understand

**Exercise 1 — Contrastive Classification**
*(Tests: LO1 — four interface layers)*

The following eight elements belong to the four interface layers described in the chapter. Assign each element to its correct layer, then identify one element that is commonly misassigned to the wrong layer and explain why the misassignment happens.

| Element | Layer (Visual Surface / Interaction Model / Deployment Surface / Brand Surface) |
|---|---|
| A. The hex color of the primary CTA button | |
| B. Whether the tool asks for clarification before generating output | |
| C. Whether the tool is deployed as a Streamlit app or a Gradio demo | |
| D. The tone of the error message when a pipeline fails | |
| E. The font size used for tool output text | |
| F. The sequence of steps the user takes to get a result | |
| G. Whether the tool is accessible at a public URL or requires local install | |
| H. Whether the tool's voice sounds like a "helpful colleague" or a "neutral system" |  |

**Self-check:** Which layer is most often confused with "visual surface"? Why?

---

**Exercise 2 — Three Misalignment Types**
*(Tests: LO2 — three misalignment types)*

Match each case description to the correct misalignment type (Confidence, Capability, Tone) from the chapter. For each match, name the chapter case study that is most analogous.

| Case | Misalignment Type | Analogous Chapter Case |
|---|---|---|
| A. A legal research tool responds to every query with definitive citations, several of which are fabricated. Users submit the citations to courts. | | |
| B. A customer service chatbot uses casual, emoji-filled responses ("hey!! totally got u 😊") for users contacting a funeral services company. | | |
| C. A content moderation AI, after learning from millions of public interactions, begins producing racist and abusive outputs within hours of launch. | | |
| D. A medical symptom-checker presents a ranked list of diagnoses without indicating that it cannot access a patient's history or perform clinical reasoning. | | |

---

**Exercise 3 — Streamlit vs. Gradio Selection**
*(Tests: LO3 — tool selection)*

The chapter specifies a decision rule for Streamlit vs. Gradio: "If you want visitors to do work with the tool, use Streamlit. If you want visitors to try the model, use Gradio."

For each of the following tools, apply the decision rule and select the correct platform. Write one sentence explaining each choice.

a) A competitor monitoring tool that ingests 15 RSS feeds, runs sentiment analysis, and emails a weekly briefing to the user.
b) A fine-tuned text classifier that labels customer support tickets as "urgent" or "routine." The developer wants to show the model's labeling behavior to a potential client.
c) A pipeline that generates a tailored weekly meal plan from user dietary inputs and shopping preferences.
d) A research team wants to demonstrate the difference in outputs between GPT-4o and Claude 3.5 Sonnet for the same prompt.

---

**Exercise 4 — Minimum Viable Interface**
*(Tests: LO4 — minimum viable interface)*

The chapter defines three required components of a minimum viable interface. For the scenario below, identify which of the three components is missing and explain what specific problem the missing component would prevent.

**Scenario:** A marketing analytics tool displays the following interface:
- Input: a text box for entering a brand name
- Output: a formatted report with sentiment score, top competitor mentions, and trend graph
- No other elements

The tool is deployed publicly. Users have complained that sometimes the report takes 45 seconds to appear and they cannot tell if the tool is working.

*Identify the missing MVI component. What user behavior does the missing component prevent?*

---

**Exercise 5 — Alignment Audit**
*(Tests: LO5 — alignment audit)*

The chapter describes a two-column alignment audit: left column lists interface elements; right column specifies what each element should communicate to a user.

Complete the right column for the following interface elements of a **Sage-archetype AI research briefing tool**:

| Interface Element | What It Should Communicate to the User |
|---|---|
| Page title | |
| Output section header | |
| Button label for generating a report | |
| Error message when a data source is unavailable | |
| Confidence indicator on AI-generated summary sentences | |
| Footer text | |

---

**Exercise 6 — README as Interface**
*(Tests: LO6 — README structure)*

The chapter specifies six elements a README must contain to function as an interface. For the following abbreviated README, identify which of the six elements are present, which are missing, and what information a developer would be unable to determine from the current version.

```
# DataBriefBot

A tool for summarizing competitor news.

## Installation
pip install databriefbot

## Configuration
Set OPENAI_API_KEY in your environment.

## Usage
Run: python main.py --brand "Stripe"
```

---

**Exercise 7 — Historical Reference**
*(Tests: LO1 — Vannevar Bush / memex)*

The chapter opens by connecting the chapter's concerns to Vannevar Bush's 1945 concept of the memex. In two sentences: (a) describe what the memex was intended to do, and (b) explain what specific interface design problem the chapter uses this historical reference to frame.

---

**Exercise 8 — Case Study Identification**
*(Tests: LO2 — three case studies)*

Match each case study to its misalignment type and outcome:

| Case Study | Year | Misalignment Type | Primary Outcome |
|---|---|---|---|
| Google Bard demo | | | |
| Snapchat My AI | | | |
| Microsoft Tay | | | |

---

## Tier 2 — Apply and Analyze

**Worked Example Reference:** See the DraftBot scenario above for the model of how to apply the misalignment framework.

---

**Exercise 9 — Full Interface Analysis**
*(Tests: LO1, LO2 — four layers, three misalignments)*

**Scenario:** *PolicyPal* is an AI tool that answers questions about U.S. immigration law. The interface has the following properties:
- Clean, authoritative visual design with dark navy color scheme
- Responses are presented as numbered legal steps without hedging language
- The tool claims in its header: "Get accurate legal guidance instantly"
- No disclaimer about non-attorney status
- No indication of which legal sources were consulted
- Tone is professional and formal throughout
- Deployed as a public web app

Analyze this interface across all four layers. For each layer, describe whether there is a misalignment and, if so, which type. Then write the three-item alignment audit the designer should have run before launch, specifying the interface change each audit item would have mandated.

---

**Exercise 10 — Error Analysis**
*(Tests: LO3, LO4 — common design errors)*

A student has deployed their AI tool with the following interface design rationale:

*"I chose Gradio because it was the fastest to deploy. My tool is a career coach that conducts multi-turn conversations with users about their job search strategy. The conversation runs for 8–10 turns on average. The interface shows only the current message exchange — no conversation history is visible. There is no loading indicator. When the model is thinking, the input box goes grey. That's the status signal."*

Identify three specific interface design errors in this rationale. For each error:
- Name the chapter concept the error violates
- Explain the specific user experience failure the error produces
- Propose the minimum change that would fix it

---

**Exercise 11 — Self-Explanation: Deployment Surface Trade-offs**
*(Tests: LO3 — deployment surface decisions)*

In your own words (no more than 150 words), explain the following claim from the chapter: "The deployment surface is not a technical decision — it is a brand decision."

Use a specific example to illustrate: describe one scenario where choosing the wrong deployment surface would contradict an AI tool's brand positioning, even if the tool's underlying model performed correctly.

---

**Exercise 12 — Cumulative Exercise: Ch. 6 → Ch. 7**
*(Tests: LO1-LO2 combined with Ch. 6 multi-agent architecture)*

In Chapter 6, you learned that multi-agent systems require explicit role/goal/backstory naming because naming is "load-bearing" — the agent's behavior is shaped by how its role is described. In Chapter 7, the chapter argues that the interface layer is also "load-bearing" in an analogous sense: the interface shapes what users expect and how they interpret outputs.

**Task:** Design a two-row comparison table showing how the "load-bearing" property operates at (a) the agent specification level (Ch. 6) and (b) the interface level (Ch. 7) for the same tool — a market research AI agent. For each row, specify: what is defined, what it loads-bearing for, and what the failure looks like when it is done carelessly.

---

**Exercise 13 — AI Interaction + Verification**
*(Tests: LO5 — alignment audit applied)*

Run the following prompt with an AI assistant (Claude, ChatGPT, or equivalent):

*"I am designing a Streamlit interface for an AI tool that drafts LinkedIn posts from bullet-point inputs. My target user is a job-seeker with a Creator archetype. Design the interface layout, specifying: (a) required UI elements, (b) tone of all visible text (button labels, headers, placeholder text), and (c) one element that signals AI involvement without undermining confidence."*

After receiving the response:
1. Evaluate the AI's output against the chapter's three minimum viable interface components. Does the AI's design satisfy all three?
2. Check whether the tone specification matches a Creator archetype's brand surface. Name one element that is archetypal and one that is not.
3. Write the one change you would make to the AI's design before using it.

---

**Exercise 14 — Misalignment Pathway Prediction**
*(Tests: LO2 — misalignment types)*

**Scenario:** A startup is building an AI financial advisor called *WealthSage*. Their archetype is Sage. The interface is designed with warm, casual language: "Hey! Let's figure out your money together 😊" The tool makes personalized investment recommendations without displaying any uncertainty range or noting that it cannot access the user's actual account data.

Predict: which misalignment type will produce the first user complaint, and which will produce the most serious long-term damage to the brand. Explain the difference using the chapter's failure mechanism.

---

**Exercise 15 — Four-Layer Interface Audit for Madison**
*(Tests: LO1, LO5 — four layers + alignment audit)*

The chapter describes the Madison Intelligence Agent as the reference tool throughout the course. Using what you know about Madison's design (from Chapter 2: Sage archetype, developer-first positioning, 870 articles/day, n8n pipeline, GPT-4o-mini sentiment layer):

For each of the four interface layers, write one specific design decision Madison should make and one decision it should avoid. Format as a two-column table: "Decision to Make" | "Decision to Avoid."

---

**Exercise 16 — Bard $100B Analysis**
*(Tests: LO2 — confidence misalignment)*

The chapter states: "In February 2023, Google's AI chatbot Bard gave a factually incorrect answer in a demo. Alphabet's stock dropped, erasing approximately $100 billion in market capitalization in a single session."

The chapter identifies this as a confidence misalignment case.

a) Explain specifically what property of the *interface* (not the model) made a single factual error produce a $100B market cap loss. What had the interface communicated to observers before the error occurred?

b) Describe what the interface should have included — using the chapter's alignment audit vocabulary — that would have reduced (though not eliminated) the market reaction.

c) The chapter also covers Microsoft Tay (capability misalignment) and Snapchat (tone misalignment). Rank the three cases by severity of brand damage and explain your ranking using the three misalignment types.

---

## Tier 3 — Synthesize and Evaluate

**Exercise 17 — Interface Coherence Across Chapters**
*(Tests: LO1-LO6, cross-chapter synthesis)*

You have now completed the core tool-building sequence: Chapter 4 (PRD and scope), Chapter 5 (data pipeline), Chapter 6 (AI agents), Chapter 7 (interface and deployment). The chapter argues that the interface is where all prior decisions become visible to the user.

**Task:** Write a 400-word analysis arguing that interface design failures are often downstream symptoms of earlier upstream decisions — scope decisions in Ch. 4, pipeline contract failures in Ch. 5, or agent naming problems in Ch. 6 — rather than independent interface errors.

Use at least one specific example from each of chapters 4, 5, and 6 to ground your argument. Your analysis should conclude with a claim about when in the build sequence interface problems should be diagnosed.

---

**Exercise 18 — Cross-Archetype Interface Comparison**
*(Tests: LO2, LO5 — misalignment + alignment audit)*

Compare the interface requirements for the same underlying AI capability — a sentiment analysis engine — deployed for two different archetypes:

**Brand A:** Creator archetype. Target user: content marketing team. Use case: evaluating emotional tone of draft blog posts before publication.

**Brand B:** Sage archetype. Target user: market research analyst. Use case: analyzing quarterly earnings call transcripts for sentiment shifts.

For each brand, specify:
1. The visual register (describe without naming colors — describe mood and density)
2. The tone of output text
3. Whether to use Streamlit or Gradio, and why
4. One confidence signal that fits the archetype
5. One interface element that would be correct for the other archetype but wrong for this one

---

**Exercise 19 — Coherence Failure Diagnosis**
*(Tests: LO1, LO2, LO5 — full chapter integration)*

**Scenario:** A student deploys an AI tool called *MindfulPath* — a journaling and emotional reflection assistant. The brand strategy from Chapter 8 specifies Caregiver archetype, warm voice, human-centered design, and positions the tool for users managing anxiety.

The student's deployed interface has the following properties:
- Dark mode with neon green accents
- System output uses second-person imperative commands: "Now write about your earliest memory of this feeling."
- Loading screen shows a spinning gear and the message "Processing your emotional data"
- Confidence labels on AI responses: "Accuracy: 87%"
- README opens with: "Installation: pip install mindfulpath. Requires Python 3.9+."

Diagnose all misalignments across all four interface layers. For each misalignment, name the layer, the misalignment type, and the specific fix. Then write a revised README opening (first four sentences) that functions as an interface in the Caregiver archetype register.

---

## Tier 4 — Evaluate and Create (Capstone)

**Exercise 20 — Full Interface Design for Your Tool**
*(Tests: LO1-LO6 — full chapter application)*

**Task:** Design the complete interface specification for the AI tool you have been building throughout Chapters 4–7.

Your specification must address all four interface layers explicitly. It must include:

1. **Layer specification** — for each of the four layers, list three concrete decisions you have made
2. **Alignment audit** — a completed two-column audit with at least eight interface elements
3. **Deployment surface decision** — Streamlit or Gradio, with a written justification that references your archetype (from Chapter 8 if you have it, or from Chapter 3 if not)
4. **Minimum viable interface checklist** — confirm that all three required MVI components are present
5. **README draft** — first six elements (following the chapter's six-element structure)
6. **Misalignment pre-check** — for each of the three misalignment types, write one sentence explaining how your interface avoids it

**Evaluation criteria (no model answer — assessed by rubric):**

| Dimension | Developing | Proficient | Exemplary |
|---|---|---|---|
| Layer coverage | Fewer than 3 layers addressed | All 4 layers addressed | All 4 layers addressed with specific, non-generic decisions |
| Alignment audit | Audit present but generic | Audit present, archetype-specific | Audit present, archetype-specific, with explicit misalignment check |
| Deployment justification | Platform named but not justified | Platform justified by functional criteria | Platform justified by functional criteria AND archetype alignment |
| MVI completeness | 1-2 of 3 components present | All 3 MVI components present | All 3 present with specific implementation detail |
| README quality | Installation-only README | 4-5 of 6 elements present | All 6 elements present, functions as Sage/archetype-appropriate brand artifact |
| Misalignment pre-check | Generic disclaimers | All 3 types addressed | All 3 types addressed with specific design choices that prevent each |

---

## Answer Key

### Tier 1

**Exercise 1 — Layer Classification**

| Element | Layer |
|---|---|
| A. Hex color of primary CTA button | Visual surface |
| B. Whether tool asks for clarification before generating | Interaction model |
| C. Streamlit vs. Gradio deployment choice | Deployment surface |
| D. Tone of error message | Brand surface |
| E. Font size of output text | Visual surface |
| F. Sequence of steps the user takes | Interaction model |
| G. Public URL vs. local install | Deployment surface |
| H. "Helpful colleague" vs. "neutral system" voice | Brand surface |

**Commonly misassigned:** Brand surface elements (D, H) are often misassigned to "visual surface." The error occurs because tone is expressed through visual language (font weight, color, spacing), but tone is a brand decision, not a visual one. The brand surface governs what the tool communicates about itself; the visual surface governs how that communication is rendered.

**Chapter reference:** §1, "Four Interface Layers."
**Common error:** Treating all visible elements as "visual surface." The visual surface is limited to aesthetic rendering; the other layers govern behavior, access, and brand communication.

---

**Exercise 2 — Misalignment Types**

| Case | Misalignment Type | Analogous Chapter Case |
|---|---|---|
| A. Legal citations, some fabricated | Confidence misalignment | Google Bard 2023 |
| B. Emoji responses for funeral services | Tone misalignment | Snapchat My AI 2018 |
| C. Racist outputs after public interaction | Capability misalignment | Microsoft Tay 2016 |
| D. Medical diagnoses without clinical data | Confidence misalignment | Google Bard 2023 |

**Chapter reference:** §2.1–2.3.
**Common error:** Classifying Case D as capability misalignment. The tool does not claim clinical reasoning capability — but it presents diagnoses *as if* they were clinically grounded. The gap between presented confidence and actual capability is the confidence misalignment definition.

---

**Exercise 3 — Streamlit vs. Gradio**

a) Streamlit. Users need to do sustained work — multi-source ingestion, scheduling, email output. The tool is a workflow, not a demo.
b) Gradio. The developer wants to show the model's behavior; the client is trying the model, not using a workflow tool.
c) Streamlit. The user is completing a task (building a meal plan) that requires inputs and produces a structured output they will act on.
d) Gradio. The research team wants to try two models and compare outputs — the classic "try the model" use case.

**Chapter reference:** §3, "Streamlit vs. Gradio."
**Common error:** Choosing Streamlit for (b) because the classifier sounds like "doing work." The key question is whether the *visitor* does work or *tries* the model; in (b), the client is evaluating model behavior, not using a pipeline.

---

**Exercise 4 — Missing MVI Component**

**Missing component:** Loading/status indicator. The chapter specifies that a minimum viable interface requires: input mechanism, output display, and status feedback. Users cannot determine whether the tool is processing their request. Without the status indicator, users may submit duplicate requests (assuming the first failed), leave before results appear, or lose trust in the tool after the first slow experience.

**Chapter reference:** §4, "Minimum Viable Interface."
**Common error:** Identifying the missing component as "error handling." Error handling is important but is not one of the three MVI components. The three MVI components are input, output, and status.

---

**Exercise 5 — Alignment Audit (Sage archetype)**

Sample answers — acceptable answers must be Sage-register: precise, informative, non-promotional.

| Interface Element | What It Should Communicate |
|---|---|
| Page title | "Intelligence briefing" or tool name + purpose statement — communicates scope precisely |
| Output section header | "Analysis" or "Briefing" — not "Your Results!" — signals that output is analytical, not celebratory |
| Button label | "Generate briefing" not "Go!" or "Get insights" — precise verb, not hype |
| Error message (source unavailable) | "Source unavailable: [source name] could not be reached. Briefing generated from [N] of [N] sources." — informative, not apologetic |
| Confidence indicator | "Based on [N] articles from [date range]" — provides epistemic grounding without false precision |
| Footer text | Attribution and methodology note — "Analysis generated by [model], processed [N] articles" — consistent with Sage transparency |

**Chapter reference:** §5, "Alignment Audit."
**Common error:** Writing generic output labels ("Your Results") that fit any archetype rather than Sage-specific register.

---

**Exercise 6 — README Audit**

**Present:** Installation instructions (partial), configuration (partial), basic usage command.
**Missing:**
1. What the tool does and who it is for (purpose statement)
2. Architecture overview (how it works)
3. Limitations or known failure modes
4. Live demo URL or example output
5. Contributing guidelines or license

A developer reading this README cannot determine: what problem DataBriefBot solves, how it processes news, what its output looks like, whether it has API rate limits, or whether it is production-ready.

**Chapter reference:** §6, "README as Interface."
**Common error:** Treating installation and usage as sufficient README content. The chapter specifies six elements; technical setup is only two of them.

---

**Exercise 7 — Vannevar Bush / Memex**

(a) The memex (Memory Extender) was a hypothetical device Bush described in 1945 that would allow a researcher to store all their books, records, and communications and retrieve any item rapidly via associative trails — a mechanical precursor to hypertext and search.

(b) The chapter uses this reference to frame the problem of interface design as a problem of making complex AI capability accessible and legible to humans — the same core challenge Bush identified: powerful information systems fail users if the interface to them is opaque, slow, or misaligned with how humans think.

**Chapter reference:** Introduction / historical framing.

---

**Exercise 8 — Case Study Matching**

| Case Study | Year | Misalignment Type | Primary Outcome |
|---|---|---|---|
| Google Bard demo | 2023 | Confidence misalignment | ~$100B market cap loss in one session |
| Snapchat My AI | 2018 | Tone misalignment | User backlash, brand damage, PR crisis |
| Microsoft Tay | 2016 | Capability misalignment | Racist/abusive outputs; tool shut down within 24 hours |

**Chapter reference:** §2.1–2.3.

---

### Tier 2

**Exercise 9 — PolicyPal Interface Analysis**

**Visual surface:** Misalignment. The dark navy authority aesthetic signals legal certainty; no visual cues for uncertainty or non-attorney status. Fix: add a header disclaimer badge using muted, non-authoritative visual weight.

**Interaction model:** Misalignment (confidence). No clarification step, no source-citation display, numbered steps presented as definitive procedure without branching or caveats. Fix: add a "this is general guidance, not legal advice" interstitial.

**Deployment surface:** No misalignment described (public web app is appropriate for this use case, assuming the tool is intended to be broadly accessible). Note: deployment surface would become misaligned if the tool required legal-professional credentials but lacked any gating.

**Brand surface:** Confidence misalignment. "Get accurate legal guidance instantly" is a capability claim the tool cannot satisfy — legal guidance requires attorney review; accuracy is not guaranteed. Tone mismatch: formal voice is appropriate for Ruler/Sage, but the claim in the header is Innocent (simple, good, accurate) while the actual legal domain requires Sage (nuanced, limited, source-cited).

**Three-item alignment audit:**
1. Header text: "Get accurate legal guidance instantly" → Should communicate: "Understand your legal options — not a substitute for attorney advice"
2. Response format: Numbered steps with no hedging → Should include: explicit "consult an attorney" cue at minimum once per response
3. Source attribution: None displayed → Should show: statute or regulation cited, with version date

---

**Exercise 10 — Three Interface Design Errors**

Error 1 — Wrong platform choice.
- Chapter concept violated: Streamlit vs. Gradio selection rule. A multi-turn career coaching conversation is "doing work with the tool," not "trying the model." Gradio is appropriate for demos; Streamlit is appropriate for sustained workflows.
- User experience failure: Gradio's interface is optimized for single-turn or short demo use; multi-turn conversations are poorly supported. Session context may not persist reliably. The user experience will feel fragile.
- Minimum fix: Redeploy on Streamlit with a conversation history panel.

Error 2 — No conversation history display.
- Chapter concept violated: Minimum viable interface (output display). In a multi-turn conversation, the visible output is the entire conversation history, not just the current message. Showing only the current turn leaves the user without context for the AI's next response.
- User experience failure: Users cannot reference earlier exchanges, cannot tell whether the AI "remembers" prior turns, and cannot verify coherence of advice across the session.
- Minimum fix: Display full conversation thread in a scrollable panel.

Error 3 — Grey input box as status signal is insufficient.
- Chapter concept violated: Minimum viable interface (status feedback). A greyed-out input box communicates "input unavailable" but does not communicate "processing." Users cannot distinguish "tool is thinking" from "tool has failed."
- User experience failure: After 5–10 seconds of silence, users will assume the tool has crashed and either refresh (losing session) or abandon.
- Minimum fix: Add an explicit loading indicator ("Thinking...") during model inference.

---

**Exercise 11 — Deployment Surface as Brand Decision**

The deployment surface determines how users first encounter and form expectations about the tool. A tool deployed as a polished Streamlit app with a branded URL signals that the tool is a production-quality product users should work with; a tool deployed as a Gradio demo at a `huggingface.co` URL signals that the tool is experimental and the user should try it. These are different brand signals that arrive before the user reads a single word of interface copy.

**Example:** A Ruler-archetype B2B pricing intelligence tool deployed as a Gradio demo contradicts its brand positioning. The Ruler archetype promises authority, prestige, and production-grade reliability. A Gradio demo URL signals prototype, experiment, and community model — the opposite of the Ruler's brand register. Even if the underlying model performs identically, the deployment surface has already damaged the brand impression.

---

**Exercise 12 — Cumulative: Ch. 6 → Ch. 7**

| Level | What Is Defined | Load-Bearing For | Failure When Done Carelessly |
|---|---|---|---|
| Agent specification (Ch. 6) | Role, goal, and backstory of each agent in the multi-agent pipeline | Agent's behavior, scope decisions, and output format | Generic role ("Assistant") → agent drifts outside intended scope; outputs are unpredictable; orchestrator loses control |
| Interface layer (Ch. 7) | Visual register, interaction pattern, tone, and deployment context of the user-facing surface | User's expectation formation, trust calibration, and interpretation of AI outputs | Generic interface (no archetype signal, no uncertainty indicators) → user misreads model capability; trust miscalibrated; single failure causes disproportionate damage |

Both definitions are load-bearing because both shape behavior downstream — at the agent level, the behavior of the AI; at the interface level, the behavior of the user. The failure mode in both cases is underspecification leading to unpredictable, trust-eroding outcomes.

---

**Exercise 13 — AI Interaction + Verification**

*(Student-generated exercise — sample verification criteria)*

**MVI check:** The AI's design should include (1) a text input for bullet points, (2) a formatted output display for the generated post, and (3) a generation status indicator. If the AI omitted the status indicator, the design fails the MVI check.

**Archetype check:** Creator archetype brand surface should signal generative energy — expressive labels ("Draft my post"), output formatted for immediate use, visual hierarchy that emphasizes the output. A Sage-register design (technical labels, minimal visual hierarchy, confidence scores) is archetypal for a different archetype and wrong here.

**One change:** Accept the AI's design as a starting point, not a final specification. The most common AI error in this exercise is producing a generic interface and labeling it as archetype-aligned without actually grounding tone choices in Creator-archetype characteristics.

---

**Exercise 14 — WealthSage Misalignment Prediction**

**First user complaint:** Tone misalignment. The casual emoji register ("Hey! Let's figure out your money together 😊") will produce the first complaint within days of launch from users who interpret financial advice as a high-stakes, serious context. The Sage archetype itself commits to a precise, analytical register; casual language directly contradicts both the archetype and the domain gravity.

**Most serious long-term damage:** Confidence misalignment. Personalized investment recommendations without uncertainty ranges or disclosure that the tool lacks account access will produce the most severe long-term brand damage. When a user makes a financial decision based on the tool's confident output and loses money, the tool is the proximate cause of a real-world harm. This produces regulatory risk, media attention, and irreparable trust collapse — the mechanism the Bard $100B case illustrates, applied to individual rather than institutional trust.

**Difference:** Tone misalignment produces complaints and a PR problem that can be corrected by a redesign. Confidence misalignment produces real-world harm that cannot be undone by redesign — the trust collapse attaches to specific damage events, not to the interface's style.

---

**Exercise 15 — Madison Four-Layer Audit**

| Layer | Decision to Make | Decision to Avoid |
|---|---|---|
| Visual surface | Information-dense layout, monospace or serif body text, restrained color (one accent color only) | Bright colors, decorative graphics, large hero images, marketing-page aesthetic |
| Interaction model | Show pipeline status as briefing is being assembled; expose source count and deduplication rate in the output | Hide processing steps; present output as appearing instantly without intermediary signals |
| Deployment surface | Deploy at a custom domain with Streamlit (users do work — they configure the pipeline and receive briefings) | Deploy as a Gradio demo (signals prototype status, contradicts professional developer-first positioning) |
| Brand surface | Technical, precise language ("870 articles processed, 90% deduplicated"); source attribution visible; limitations noted | Hype language ("comprehensive intelligence"); absence of source provenance; confidence overclaiming |

---

**Exercise 16 — Bard $100B Analysis**

a) The interface had communicated to observers — through Google's own promotional framing, through the event format (a major public demo), and through the tool's visual authority signals — that Bard was production-ready and reliable. The interface encoded a promise of accuracy that one factual error instantly falsified. The market's reaction was not to the error itself but to the gap between the interface's promise and the reality the error revealed. A $100B loss requires not just an error but a prior misaligned expectation that the error collapses.

b) The interface should have included, per the alignment audit vocabulary: a confidence qualifier on every AI response, explicit source attribution, and language establishing that Bard is a "language assistant" rather than a "knowledge system" — each of these would have moderated the expectation the error fell against.

c) **Ranking by brand damage severity:**
1. Microsoft Tay (capability misalignment) — tool shut down in 24 hours; complete operational failure; Microsoft's reputation for enterprise AI reliability damaged substantially
2. Google Bard (confidence misalignment) — $100B single-session market cap loss; Bard delayed; long-term positioning against OpenAI set back
3. Snapchat My AI (tone misalignment) — user backlash and PR crisis, but no market cap event and no operational shutdown; most recoverable

**Reasoning:** Capability misalignment produced total product failure (Tay could not be used in any form); confidence misalignment produced massive financial damage but the tool survived; tone misalignment produced brand damage but was the most correctable with redesign.

---

## Self-Assessment Rubric

Before moving to Chapter 8, verify you can do the following without referring to the chapter:

- [ ] Name the four interface layers and give one example of an element in each
- [ ] Match each of the three chapter case studies to its misalignment type and primary outcome
- [ ] Apply the Streamlit/Gradio decision rule to a novel tool scenario in under 60 seconds
- [ ] List the three components of a minimum viable interface
- [ ] Describe the two-column alignment audit and explain what each column contains
- [ ] Name the six elements a README must contain to function as an interface

---

## Instructor Notes

**Prerequisite dependencies:** Chapter 3 (archetype) is required context for Exercises 5, 12, 14, and 15. Students who have not committed to an archetype will produce generic alignment audit responses. Exercise 12 also requires Chapter 6 multi-agent vocabulary.

**Highest-yield exercises for class discussion:** Exercise 16 (Bard $100B analysis) generates the richest discussion because students initially focus on the model error rather than the interface's role in creating the conditions for the market reaction. Redirect discussion to: "What did the interface promise before the error occurred?"

**Common confusion:** Students frequently conflate the brand surface with the visual surface. The distinction matters most in Exercises 1, 5, and 19: tone is a brand surface decision expressed through visual choices, but changing the visual surface without changing the brand surface does not resolve a tone misalignment.

**Tier 4 grading note:** Exemplary responses to Exercise 20 will demonstrate that interface decisions are downstream of archetype decisions — the best submissions will explicitly reference their Chapter 8 brand strategy as the governing constraint on every interface choice.
