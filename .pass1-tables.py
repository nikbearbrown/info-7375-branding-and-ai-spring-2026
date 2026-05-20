#!/usr/bin/env python3
"""Pass 1 — render all TABLE comments in branding-and-ai/chapters/*.md to populated tables.

Replacement pattern:
  <!-- → [TABLE: ...] -->\n\n*Figure N.N*\n\n[stub markdown table]\n\n: {.some-class}
becomes:
  [populated markdown table]\n\n*Figure N.N*

Per spec: replace comment + label + stub with new table + label (label preserved, moved
below the table to match the natural reading flow).
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# ---------------------------------------------------------------------------
# Tables — keyed by a unique substring of the [TABLE: ...] comment
# ---------------------------------------------------------------------------
TABLES = {}

# === Ch 01 — Summary integration table (Figure 1.14) ===
TABLES["summary integration table"] = """| Framework | Question It Answers | What Breaks Without It |
|---|---|---|
| **Spence Mechanism** | *Why* brand matters at all in this market | The student treats brand as optional decoration — investing only in build, then wondering why the GitHub no longer separates them from the field |
| **Four-Verb Framework** | *What* the portfolio must demonstrate (Ideate / Build / Brand / Ship) | The student has identity but no market action — a clear sense of who they are with nothing in the world that proves it |
| **Archetype System** | *How* to execute Brand specifically — the role you play in your audience's story | Brand decisions are arbitrary style choices with no strategic foundation; portfolio voice drifts and the audience cannot tell who the work is for |"""

# === Ch 05 — Pipeline taxonomy (Figure 5.2) ===
TABLES["pipeline taxonomy"] = """| Type | Tools | Throughput / Frequency | Typical Use Case | Used in Madison? |
|---|---|---|---|---|
| **ETL** | Airflow · dbt · Fivetran | Batch | Large-dataset warehouse loads — analytics back-end | No |
| **Stream** | Kafka · Flink | Continuous | Real-time fraud detection, low-latency event processing | No |
| **Workflow automation** | n8n · Zapier · Make | Scheduled or event-driven | API glue + orchestration across SaaS endpoints | Yes |
| **Inference** | LangChain · LlamaIndex | On-demand | LLM calls + vector retrieval inside a workflow | Yes (as a step inside the workflow-automation pipeline) |"""

# === Ch 05 — Apollo asymmetry (Figure 5.3) ===
TABLES["three-column comparison — Actor"] = """| Actor | Type of Damage | Duration |
|---|---|---|
| **Reddit** (upstream) | Diffuse reputational damage spread across a platform with hundreds of millions of users | Months-long blowback that recovered |
| **Apollo** (downstream) | Product death + total user loss within thirty days | Permanent |
| **Christian Selig** (personally) | Net positive — public sympathy, transparency rewarded, developer reputation strengthened | Ongoing — the personal brand benefit compounds even as the product is gone |"""

# === Ch 05 — Three-discipline checklist (Figure 5.5) ===
TABLES["three-row checklist — Discipline"] = """| Discipline | What It Catches | How to Implement in n8n |
|---|---|---|
| **Document the contract** | Contract existence, terms, rate limits, and the explicit acknowledgement that the contract is *subject to change* | One-sentence note in the README and in each external-call node's description field — what the service gives, what it costs, what the rate limit is, what the terms allow |
| **Design a degraded mode** | What happens when a contract fails — keeps the failure from becoming a product death | Error-output port on the failing node + a fallback node that returns the degraded result (cached value, alternate source, or informative failure) |
| **Monitor the contract** | Silent contract drift — rate-limit creep, schema deprecation, pricing changes, ToS updates the workflow has no way to detect from a 200 response | Status-page RSS feed piped into your alerting channel + billing alerts on the upstream service + workflow-failure hook for execution-level errors |"""

# === Ch 05 — Degraded-mode taxonomy (Figure 5.6) ===
TABLES["degraded-mode taxonomy"] = """| Mode Name | What It Does | Minimum Implementation | When to Use It |
|---|---|---|---|
| **Informative Failure** | Detects the contract failure and shows the user a clear message about what is unavailable and why, instead of an opaque error | Error output node + user-facing message string | All pipelines — the minimum bar |
| **Partial Degradation** | Disables the feature that depends on the broken contract; the rest of the product continues to work | Conditional branch after the error output that hides or grays out the affected feature | When only one feature depends on the failed contract |
| **Fallback Source** | Replaces the broken source with an alternative when the primary fails (RSS mirror, alt API, queued retry) | Second HTTP Request node wired to the error path of the first | When a genuine alternative data source exists for the same information |
| **Graceful Staleness** | Continues to serve the last successful result, with a visible timestamp indicating staleness | Cache node holding the last good result + UI element showing "last updated at …" | When stale data is meaningfully better than no data — most informational products |"""

# === Ch 05 — Madison design choices (Figure 5.10) ===
TABLES["Madison workflow design choices"] = """| Design Choice | Failure Mode It Addresses | What Happens Without It |
|---|---|---|
| **Parallel ingestion branches** | A single source goes down or rate-limits | Entire pipeline stalls waiting for one dead API; daily output is empty |
| **Seen-URL store** | The same item appears in multiple sources | Same item is scored and written multiple times, inflating apparent results and wasting LLM calls |
| **Run log** | The pipeline silently stops running (cron daemon dies, credentials expire, scheduler skipped) | No visibility into whether the workflow executed today — you find out when a downstream user complains |
| **Six-hour schedule (not real-time)** | Rate-limit exhaustion on high-frequency sources and runaway LLM cost | Hitting API caps mid-day, getting throttled or billed unexpectedly, and producing degraded output for the rest of the window |"""

# === Ch 05 — Pipeline-as-brand summary (Figure 5.12) ===
TABLES["pipeline-as-brand-asset summary"] = """| Pipeline Property | Brand Consequence |
|---|---|
| **Silent, reliable execution** | Product feels trustworthy — the user never thinks about the infrastructure |
| **Undocumented dependency breaks** | The user sees *your product* fail, not the upstream service that actually broke the contract |
| **Informative failure mode** | The user understands what happened and why; the brand survives the incident, sometimes strengthened by it (the Selig effect) |
| **No degraded mode** | The user loses trust in the product entirely — the brand pays the full cost of an upstream change you did not control |
| **Run log + monitoring** | You catch failures before users do — brand-damaging incidents become internal incidents you fix before anyone outside notices |"""

# === Ch 08 — Seven brand components (Figure 8.1) ===
TABLES["seven components of a startup brand strategy"] = """| Component | One-Line Definition | Stripe Example | What Breaks Without It |
|---|---|---|---|
| **Mission** | What the company exists to do, in one specific and testable sentence | *Increase the GDP of the internet* | "What do we build next?" has no answer the team can converge on |
| **Vision** | The world if you succeed, in one or two ambitious-but-directional sentences | Every business, anywhere in the world, can transact online with the reliability of a Fortune 500 | The team optimizes for survival rather than the outcome the company is supposed to produce |
| **Values** | Commitments the company maintains *when maintaining them is costly* | Documentation as product — features delay until docs are done | A new hire cannot predict what the company would do in an ambiguous case; the values are decoration |
| **UVP** | The specific thing, for the specific audience, that nobody else offers in the same way | The cleanest payment API, integrable in seven lines of code, with documentation that doesn't require a PDF | Marketing makes promises the product cannot keep, or the product builds capacity nobody asked for |
| **Archetype** | The strategic role the company plays in its audience's story (Sage / Hero / Caregiver / Rebel / Creator / etc.) | Sage — patient, evidence-based, rewards depth, speaks precisely | Brand decisions cohere by accident if at all; the company drifts visually and verbally as it grows |
| **Voice** | How the company speaks — rhythm, vocabulary, formats it favors and rejects | Precise, intellectually serious, slightly understated; signals the reader has technical depth | Each writer at the company sounds like a different person; the audience cannot recognize the brand across surfaces |
| **Positioning** | Where the company sits relative to competitors *and the actual alternative the customer considers* | Not "vs. PayPal" — vs. *writing your own payment integration* or *not building the feature* | The team competes against the wrong thing; differentiation arguments miss the customer's actual decision |"""

# === Ch 08 — Negative-space rubric (Figure 8.3) ===
TABLES["negative-space list evaluation rubric"] = """| Criterion | What "Passes" | What "Fails" | Stripe Example |
|---|---|---|---|
| **Specific** | A new engineer could read the item and make a decision from it | The item cannot be violated because it is too vague | *"No enterprise sales process"* (passes) vs *"We value simplicity"* (fails) |
| **Archetype-consistent** | Item is predictable from the archetype — someone could guess the archetype from the list | Item is random or actively contradicts the archetype | Sage: *"No rapid product proliferation"* (predictable) |
| **Costly** | Saying yes is genuinely tempting — there is real business pressure | Nobody was asking for it anyway, so the "no" is free | *"No celebrity-CEO theatrics — even when press is offered"* |
| **Testable over time** | A reader two years later can check whether the commitment held | Unmeasurable, so the company can claim to be honoring it indefinitely | *"No rapid product proliferation"* — check the 2016–2022 launch cadence and verify |"""

# === Ch 08 — Archetype-to-audience matching (Figure 8.5) ===
TABLES["archetype-to-audience matching"] = """| Audience Type | What They Fear | What They Want | What They Distrust | What They Reward | Archetype Fit |
|---|---|---|---|---|---|
| **Developers** | Being sold to | Competence + reliability + clean interfaces | Marketing-speak, vague claims, "synergy" | Demonstrated depth — code, docs, post-mortems | **Sage** |
| **First-time founders in hostile markets** | Hidden friction surfacing after they've committed | Friction removed before they hit it | Complexity dressed up as comprehensiveness | Anticipatory care — the thing they didn't know to ask for | **Caregiver** |
| **Buyers in incumbent-dominated markets** | Status quo lock-in and the costs the incumbent ignores | An escape route + a credible alternative | The incumbent and anything that smells like it | Disruption + naming the unsaid thing the incumbent refuses to | **Rebel** |"""

# === Ch 08 — Name evaluation worksheet (Figure 8.6) ===
TABLES["name evaluation worksheet"] = """| Candidate Name | Bar Test (Pass / Fail + notes) | Lawyer Test (TESS status) | Domain Test (.com status + cost) | Archetype Alignment (Pass / Fail + one sentence) |
|---|---|---|---|---|
| _________________ | ☐ Pass / ☐ Fail — notes: __________ | ☐ Clear / ☐ Conflict found / ☐ Ambiguous — Class 42 search: __________ | ☐ .com available / ☐ acquirable at $______ / ☐ unavailable | ☐ Pass / ☐ Fail — *Why this name fits (or violates) the archetype:* __________ |
| _________________ | ☐ Pass / ☐ Fail — notes: __________ | ☐ Clear / ☐ Conflict found / ☐ Ambiguous — Class 42 search: __________ | ☐ .com available / ☐ acquirable at $______ / ☐ unavailable | ☐ Pass / ☐ Fail — *Why this name fits (or violates) the archetype:* __________ |
| _________________ | ☐ Pass / ☐ Fail — notes: __________ | ☐ Clear / ☐ Conflict found / ☐ Ambiguous — Class 42 search: __________ | ☐ .com available / ☐ acquirable at $______ / ☐ unavailable | ☐ Pass / ☐ Fail — *Why this name fits (or violates) the archetype:* __________ |
| _________________ | ☐ Pass / ☐ Fail — notes: __________ | ☐ Clear / ☐ Conflict found / ☐ Ambiguous — Class 42 search: __________ | ☐ .com available / ☐ acquirable at $______ / ☐ unavailable | ☐ Pass / ☐ Fail — *Why this name fits (or violates) the archetype:* __________ |
| _________________ | ☐ Pass / ☐ Fail — notes: __________ | ☐ Clear / ☐ Conflict found / ☐ Ambiguous — Class 42 search: __________ | ☐ .com available / ☐ acquirable at $______ / ☐ unavailable | ☐ Pass / ☐ Fail — *Why this name fits (or violates) the archetype:* __________ |"""

# === Ch 08 — Name archetypes in the wild (Figure 8.7) ===
TABLES["name archetypes in the wild"] = """| Company Name | Archetype | Why the Name Fits the Archetype | What Would Violate It |
|---|---|---|---|
| **Stripe** | Sage | Simple, precise, no emotional charge; technical register; the word does not promise more than the product delivers | *BlazingFast*, *Conquer*, *Dominate* — speed-as-value, competition as orientation |
| **Notion** | Creator | Blank-slate suggestion; an idea before it has a shape; invites the user to make something | *HyperCharge*, *DisruptBase* — pre-decided outcome, performative urgency |
| **Basecamp** | Rebel | Named after the starting point of an expedition; signals going against established routes; a refusal of the corporate-suite naming convention | *Enterprise Suite*, *CorporateHub* — exactly the convention Basecamp is positioning against |
| **Calm** | Caregiver | Immediate emotional register of relief and safety; the product's purpose is the first impression of the name | *BattleMode*, *HustleHard* — opposite emotional register, would alienate the audience that needs the product |"""

# === Ch 08 — Internal consistency check (Figure 8.9) ===
TABLES["internal consistency check worksheet"] = """| Component Pair | Consistency Question | Pass / Fail | Contradiction Found (if any) | Revision Made |
|---|---|---|---|---|
| **Mission ↔ UVP** | Does the UVP describe a way of doing what the mission says? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **Values ↔ Negative Space** | Can each "no" in the negative-space list be traced back to a specific value? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **Archetype ↔ Voice** | Does the voice sound like something this archetype would actually produce? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **Positioning ↔ UVP** | Does the UVP differentiate from the *actual* alternatives named in positioning? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **Mission ↔ Vision** | Is the vision the world the mission would create if fully realized? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **UVP ↔ Positioning** | Does the positioning make the UVP's differentiation legible to the customer? | ☐ Pass / ☐ Fail | _______________ | _______________ |
| **Values ↔ Archetype** | Are the values expressions of this archetype's core drive? | ☐ Pass / ☐ Fail | _______________ | _______________ |"""

# === Ch 08 — What downstream chapters take (Figure 8.11) ===
TABLES["what each downstream chapter takes from Chapter 8"] = """| Chapter | What It Takes From Chapter 8 | What Goes Wrong If Chapter 8 Is Vague |
|---|---|---|
| **Chapter 9 — Visual Identity** | Archetype + Voice → palette, typography, mood, layout register | Visual decisions become arbitrary aesthetic preferences with no strategic anchor; a visually polished brand the audience cannot read |
| **Chapter 10 — Storytelling** | Mission + Vision + UVP → investor pitch, press narrative, onboarding copy | The story has no spine — every telling differs slightly, and the audience cannot predict what the company is from one surface to the next |
| **Part IV — Portfolio & Launch** | All seven components → portfolio narrative, resume, presentation, launch post | The portfolio reads as a collection of projects rather than a company story; the candidate looks like a builder rather than a founder |"""

# === Ch 12 — Three coherence properties (Figure 12.1) ===
TABLES["three coherence properties"] = """| Property | What It Looks Like When Present | What It Looks Like When Absent | Where It Applies Beyond the Deck |
|---|---|---|---|
| **Argument coherence** | Every element reinforces one claim; each slide leans on the previous one | Ten slides making ten different arguments — the audience leaves remembering nothing | LinkedIn headline → about → featured; resume bullets that all support one role thesis; portfolio narrative |
| **Specific numbers** | *"87 bookings in the first six weeks"* — a claim a reviewer can picture and audit | *"strong early user interest"* — a claim that signals the work was not done | Resume bullets, portfolio outcomes, case-study metrics, follow-up emails |
| **Team weight** | Named founders with specific, relevant prior work — the team slide *is* the pitch at seed stage | *"experienced team of builders"* — generic, signals nothing | The about section, the team slide, the cover note, the first sentence of any bio |"""

# === Ch 12 — Outcome vs responsibility bullets (Figure 12.3) ===
TABLES["outcome vs. responsibility bullets"] = """| Responsibility (Not Hireable) | Outcome (Hireable) |
|---|---|
| Worked with the team on data engineering tasks. | Built a data pipeline ingesting 870 articles per day with a 90% deduplication rate, reducing manual curation time by four hours per week. |
| Helped develop an AI product for the course. | Shipped Madison Intelligence Agent — an n8n + GPT-4o-mini pipeline used by 12 beta users, with a 56% reported reduction in competitor-research time. |
| Contributed to frontend development. | Designed and shipped a React dashboard with sub-100ms time-to-interactive on slow 3G, used in production by every Madison beta user. |
| Worked on pipeline design and automation. | Re-architected a brittle Python script into an n8n workflow with documented contracts and three degraded modes; eliminated all four pipeline-failure incidents from the prior quarter. |
| Supported brand and launch activities. | Wrote the launch post (1,200 reads in week one), built the brand-strategy document, and delivered the final pitch that produced two job interviews. |"""

# === Ch 12 — ATS resume checklist (Figure 12.4) ===
TABLES["ATS-optimized resume format checklist"] = """| Requirement | Why It Matters |
|---|---|
| **Single column** | Two-column layouts confuse ATS parsers — text gets read out of order, sometimes garbled, sometimes dropped entirely |
| **Standard section headers** (*Experience*, *Education*, *Skills*, *Projects*) | ATS systems are trained on exact strings — *"Where I've Worked"* may not be parsed as work history |
| **Standard fonts only** (Times New Roman, Arial, Calibri, Georgia) | Unusual fonts may not render on the parsing system; the resume becomes unreadable to the filter |
| **Save as PDF + .docx** | Different ATS systems have different format preferences — submit both whenever possible |
| **No headers/footers with critical info** | Some parsers skip header and footer regions entirely; the contact line at the top of the page is safer than a header |
| **Keywords from the job description** | ATS scores against role vocabulary — if you did the work, use the field's exact words for it (programming languages, tools, methodologies, role titles) |"""

# === Ch 12 — Archetype-to-platform fit (Figure 12.5) ===
TABLES["archetype-to-platform fit"] = """| Archetype | Recommended Primary | Secondary | Avoid | Cadence Note |
|---|---|---|---|---|
| **Sage** | LinkedIn + Blog/Substack | GitHub | Twitter/X | Monthly long-form; comments must add data or argument, never just praise |
| **Hero** | LinkedIn + Twitter/X | GitHub | Substack | Weekly project updates; show the wins, name the metrics |
| **Creator** | Portfolio + GitHub | LinkedIn | Twitter/X | Quarterly case studies; the artifact is the post |
| **Rebel** | Twitter/X + Substack | GitHub | LinkedIn | Weekly short takes; named positions, not hot takes |
| **Caregiver** | LinkedIn | Portfolio | Twitter/X | Monthly substantive engagement; the comments matter more than the posts |
| **Everyman** | LinkedIn | GitHub | Substack | Weekly community engagement; show up reliably, not loudly |"""

# === Ch 12 — Slide-by-slide structure guide (Figure 12.7) ===
TABLES["slide-by-slide structure guide"] = """| Slide | Name | One-Line Content Spec | Speaking Time | The Single Most Important Element |
|---|---|---|---|---|
| 1 | **Title + positioning** | Your name, tool name, one sentence positioning both — *"I build AI tools that help X do Y; T is the first one"* | ~1 min | The positioning sentence — not the name |
| 2 | **Problem** | One specific moment, one person, one pain — with a number that makes it real | ~2 min | The opening sentence that puts the audience inside the problem |
| 3 | **Solution (the tool)** | What the user does, what they get, what changes — in user-facing terms, not architecture | ~2 min | One screenshot or demo GIF |
| 4 | **How it works** | Architecture overview the audience can follow — trigger, pipeline, AI layer, output | ~2 min | One labeled diagram, not a stack list |
| 5 | **Demo or evidence** | The live URL, screenshots of real use, real output — and one specific user quote if you have it | ~3 min | Real data the tool has actually processed |
| 6 | **Brand position** | Archetype + audience + voice — *why* the tool looks and reads the way it does | ~2 min | The named archetype and the one thing the brand refuses to do |
| 7 | **Validation** | Specific numbers, even small ones; specific feedback, even from two users | ~2 min | The specific metric — *"56% reduction in five-person beta"* not *"strong interest"* |
| 8 | **Roadmap** | One or two next-version items — each connected back to the problem slide | ~1 min | The argument for *why* the next version matters |
| 9 | **You as the team** | Your archetype, the four-verb framework applied to your work, portfolio URL | ~2 min | The portfolio URL on the slide and the archetype-aligned one-sentence about-you |
| 10 | **The ask** | Specific request — *"a machine-learning role at a startup building user-facing AI products"* | ~1 min | The specific ask sentence, said directly, not trailed off into thanks |"""

# === Ch 12 — Opening line comparison (Figure 12.8) ===
TABLES["opening line comparison"] = """| Generic Opening (Loses the Room) | Scene Opening (Earns Attention) |
|---|---|
| *"Hi, I'm [name] and today I'll be presenting my AI tool."* | *"It's 7:45 Tuesday. A marketing manager opens her laptop. Forty-five minutes of tab-switching later, she still doesn't know what her competitors shipped last night. My tool does it in ninety seconds."* |
| *"I built a career-search assistant for this course."* | *"Three months ago a classmate applied to 47 jobs in six weeks. She got two callbacks. The problem wasn't her resume — it was that she was applying to the wrong 47 jobs."* |
| *"Today I'll walk you through my project and brand strategy."* | *"There are 412 AI writing tools on Product Hunt right now. Only one of them was designed specifically for technical documentation writers who hate marketing copy. Here's how I found that gap."* |"""

# === Ch 12 — Post-course plan template (Figure 12.9) ===
TABLES["post-course plan template"] = """| Commitment Type | Specific Commitment | Deadline | Done / Not Done |
|---|---|---|---|
| **Portfolio addition 1** | _____________________ | _____________________ | ☐ |
| **Portfolio addition 2** | _____________________ | _____________________ | ☐ |
| **Portfolio addition 3** | _____________________ | _____________________ | ☐ |
| **Published piece 1** | _____________________ | _____________________ | ☐ |
| **Published piece 2** | _____________________ | _____________________ | ☐ |
| **Published piece 3** | _____________________ | _____________________ | ☐ |
| **Relationship engagement 1–5** | _____________________ | _____________________ | ☐☐☐☐☐ |"""

# === Ch 12 — Where each verb lives (Figure 12.12) ===
TABLES["where each verb lives in the book"] = """| Verb | Chapters | Primary Artifact Produced | Signal It Creates |
|---|---|---|---|
| **Ideate** | Ch 4 (Career PRD) | Problem specification + audience definition | *"This person knows what to build before building."* |
| **Build** | Ch 5–7 (Pipeline, AI layer, Interface) | Deployed AI tool | *"This person can execute."* |
| **Brand** | Ch 8–10 (Strategy, Visual Identity, Storytelling) | Brand strategy doc + visual system + published content | *"This person knows who the work is for."* |
| **Ship** | Ch 11–12 (Portfolio, Launch) | Deployed portfolio + presentation + resume + launch post | *"This person gets it in front of people."* |"""


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------
def apply():
    # Pattern: comment + blank + figure label + blank + stub-table + blank + : {.class}
    pat = re.compile(
        r'(<!--\s*→\s*\[TABLE:[^\n]*?-->)\s*\n+'
        r'(\*Figure[^\n]*\*)\s*\n+'
        r'(\|.*?\n+: \{[^}]*\})',
        re.DOTALL,
    )

    files = sorted(CH.glob('*.md'))
    total = 0
    for f in files:
        text = f.read_text()
        new_text = text
        replaced_in_file = 0

        def replace(m):
            nonlocal replaced_in_file
            comment, label, _stub = m.group(1), m.group(2), m.group(3)
            # Find which table key matches this comment
            for key, table in TABLES.items():
                if key in comment:
                    replaced_in_file += 1
                    return f"{table}\n\n{label}"
            print(f"!!! NO MATCH for comment in {f.name}: {comment[:80]}")
            return m.group(0)  # unchanged

        new_text = pat.sub(replace, text)
        if new_text != text:
            f.write_text(new_text)
            total += replaced_in_file
            print(f"  {f.name}: {replaced_in_file} tables rendered")
    print(f"\nTOTAL tables rendered: {total}")
    return total


if __name__ == '__main__':
    apply()
