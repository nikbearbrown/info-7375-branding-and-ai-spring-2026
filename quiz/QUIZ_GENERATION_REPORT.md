# Quiz Generation Report — INFO 7375: Branding and AI

**Generated:** 2026-06-20
**Course:** INFO 7375 — Branding and AI (Spring 2026)
**Guidelines applied:** `scripts/cowork-quiz.md`

---

## Summary

13 quiz files were generated, one per instructional chapter. All quizzes follow the three-section structure, Bloom's Taxonomy distribution, psychometric targets, and answer key requirements specified in `cowork-quiz.md`.

---

## Files Generated

| Quiz File | Chapter | Questions | Status |
|---|---|---|---|
| `01-the-creative-engineer-quiz.md` | Ch 1 — The Creative Engineer | 11 | Complete |
| `02-the-madison-framework-quiz.md` | Ch 2 — The Madison Framework | 11 | Complete |
| `03-jungian-brand-archetypes-as-a-system-quiz.md` | Ch 3 — Jungian Brand Archetypes as a System | 11 | Complete |
| `04-product-requirements-and-scope-quiz.md` | Ch 4 — Product Requirements and Scope | 11 | Complete |
| `05-data-pipelines-and-workflow-automation-quiz.md` | Ch 5 — Data Pipelines and Workflow Automation | 11 | Complete |
| `06-ai-intelligence-and-multiagent-systems-quiz.md` | Ch 6 — AI Intelligence and Multi-Agent Systems | 11 | Complete |
| `07-interface-design-and-deployment-quiz.md` | Ch 7 — Interface Design and Deployment | 11 | Complete |
| `08-personal-brand-path-brand-strategy-quiz.md` | Ch 8 (Personal Brand Path) — Brand Strategy | 11 | Complete |
| `08-startup-brand-path-brand-strategy-quiz.md` | Ch 8 (Startup Brand Path) — Brand Strategy | 11 | Complete |
| `09-visual-identity-systems-quiz.md` | Ch 9 — Visual Identity Systems | 11 | Complete |
| `10-brand-storytelling-quiz.md` | Ch 10 — Brand Storytelling | 11 | Complete |
| `11-portfolio-as-product-quiz.md` | Ch 11 — Portfolio as Product | 11 | Complete |
| `12-professional-presence-and-launch-quiz.md` | Ch 12 — Professional Presence and Launch | 11 | Complete |

**Total questions generated:** 143 (11 per chapter × 13 chapters)

---

## Files Skipped

| File | Reason Skipped |
|---|---|
| `00-introduction.md` | Navigation/frontmatter document — no instructional content; only chapter summaries |
| `00-frontmatter.md` | Explicitly excluded per instructions |
| `99-back-matter.md` | Explicitly excluded per instructions |
| `00-introduction-theory-roadmap-archive.md` | Explicitly excluded per instructions |

---

## Structure Applied Per Quiz

Every quiz follows the three-section structure from `cowork-quiz.md`:

**Section 1 — Recall & Recognition (Q1–Q5)**
- 3 MCQ (3-option) + 2 True/False
- Bloom's level: Remember / Understand
- Psychometric target: p = 0.77–0.85
- Each question tests recall of a named mechanism, specific number, or defined concept from the chapter

**Section 2 — Application & Analysis (Q6–Q9)**
- 2 MCQ (3-option) + 2 Short-Answer (scenario-grounded)
- Bloom's level: Apply / Analyze
- Psychometric target: p = 0.50–0.70
- Each MCQ uses a chapter-specific scenario; each Short-Answer names the exact mechanism and asks students to apply it

**Section 3 — Synthesis & Evaluation (Q10–Q11)**
- 1 Brief-Response (counter-argument evaluation) + 1 Transfer Brief-Response (novel scenario)
- Bloom's level: Evaluate / Create
- Psychometric target: p = 0.30–0.50
- Q10 always presents a plausible counter-argument; Q11 always applies chapter frameworks to a context not explicitly covered in the chapter

---

## Anti-Hallucination Notes

All questions are grounded in named chapter artifacts:

- Specific numbers cited: Peng et al. 56% productivity finding (Ch 1), Tropicana 20% sales drop (Ch 9), Madison 870 articles/day throughput (Ch 6, 11, 12), Stripe seven-lines-of-code UVP (Ch 8), Airbnb $600K raised from a 10-slide deck (Ch 12), Bud Light best-selling beer position lost (Ch 10), Brittany Chiang 6,000+ forks (Ch 11), WCAG AA 4.5:1 ratio (Ch 9)
- Named case studies: Pepsi 2008 "BreathTaking" document (Ch 9), Tropicana 2009 repackaging (Ch 3, 9), Gap 2010 (Ch 3), New Coke 1985 (Ch 3), Pepsi *Live for Now* 2017 (Ch 10), Bud Light/Dylan Mulvaney 2023 (Ch 10), Jaguar "Copy Nothing" 2024 (Ch 10), Apollo/Reddit API pricing (Ch 5), Tay 2016 / Bard 2023 / Snapchat 2018 (Ch 7)
- Named frameworks and terms: Spence signaling / separating vs. pooling equilibrium (Ch 1), four-verb framework Ideate/Build/Brand/Ship (Ch 1, 12), ReAct loop (Ch 2), `allow_delegation=False` (Ch 6), Build-Measure-Learn loop (Ch 4), degraded modes (Ch 5), Madison five layers (Ch 2, 6), three-test framework for archetypes (Ch 3), negative-space list (Ch 8), 10/20/30 Kawasaki rule (Ch 12), three compounding channels (Ch 11), customer-as-hero Miller framework (Ch 10)

No questions introduce named facts, statistics, or case studies that are not present in the chapter text.

---

## Bloom's Distribution Summary (Across All Quizzes)

| Level | Question Types | Count per Quiz | Percentage |
|---|---|---|---|
| Remember / Understand | MCQ + True/False (Section 1) | 5 | 45% |
| Apply / Analyze | MCQ + Short-Answer (Section 2) | 4 | 36% |
| Evaluate / Create | Brief-Response (Section 3) | 2 | 18% |

---

## Notes on Chapter 8 Dual Path

Chapter 8 exists in two parallel versions — Personal Brand Path and Startup Brand Path — each covering the same brand strategy framework from different perspectives (individual vs. company). Both quizzes were generated. Content overlap is minimal: the Personal Brand Path quiz centers on the seven-component framework, Stripe negative-space analysis, and the one-page document constraint; the Startup Brand Path quiz centers on the eight-component framework (adds negative space as an explicit component), the three naming tests, the coherence check, and the reverse-engineering method. Instructors may assign one or both depending on which path students are following.

---

*Report generated by Claude Code (claude-sonnet-4-6)*
