# Branding and AI: Building the Creative Engineer

*A textbook for graduate students, technical practitioners, and instructors at the intersection of AI engineering and brand strategy.*

**Authors:** [Nik Bear Brown](https://www.linkedin.com/in/nikbearbrown/) & [Nina Harris](https://www.linkedin.com/in/nina-harris-524ab7108/)
**Publisher:** Bear Brown, LLC
**Course of record:** INFO 7375 — Northeastern University, College of Engineering
**Status:** First edition, 2026

[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC--BY--NC--4.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Edition](https://img.shields.io/badge/edition-1.0-green.svg)](#)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](#)

---

## What this book argues

The cost of building software has collapsed. The cost of being seen has not.

For two decades, "I built a working app" was a costly signal — it separated capable engineers from less capable ones because production took weeks of evening work. AI tooling has deprecated that signal. A 2023 study of GitHub Copilot found developers shipped a working HTTP server 56% faster with the tool than without. By the 2024 Stack Overflow Developer Survey, 82% of working developers were using AI tools to write code.

When the cost of producing a signal collapses, the signal stops separating. What rises in value is the work that did *not* get cheap: identifying a problem worth solving, positioning a solution clearly, and shipping to real users.

This book treats those skills as a unified technical discipline — the practice of the **Creative Engineer** — and walks the reader through twelve weeks of structured work that produces a deployed AI tool, a documented brand strategy, a portfolio that compounds, and a launch package ready for hiring conversations or fundraising.

---

## Who this book is for

- **Graduate students in AI / CS / engineering programs** preparing to enter a labor market that increasingly rewards integrated engineering-and-brand profiles. If you have shipped code but cannot yet defend why the work matters in a thirty-second pitch, this book is written for you.
- **Working engineers** considering a career move — to a startup, to founding, or to a new technical specialization — who want a structured framework for repositioning their public profile.
- **Instructors** teaching at the intersection of AI engineering and product / brand strategy. The book maps cleanly onto a 14-week semester (representative mapping in Chapter 0).
- **Self-learners** interested in the integrated framework. The book is readable cover-to-cover; the embedded exercises require access to an LLM (Claude or equivalent) and the willingness to ship public artifacts.

The book does **not** assume prior coursework in marketing, branding, or design. It does assume comfort with at least one programming language, the command line, and APIs.

---

## Table of contents

### Front matter
- Title page · Copyright · Dedication · Preface

### Introduction
- The labor-market shift, the central claim, how the book is organized, how to read it.

### Part I — Foundation
1. The Creative Engineer
2. The Madison Framework
3. Jungian Brand Archetypes as a System

### Part II — Build
4. Product Requirements and Scope
5. Data Pipelines and Workflow Automation
6. AI Intelligence and Multi-Agent Systems
7. Interface Design and Deployment *(midterm gate)*

### Part III — Brand
*(Chapter 8 forks: Personal Brand path | Startup Brand path)*

8. Brand Strategy
9. Visual Identity Systems

### Part IV — Launch
10. Brand Storytelling
11. Portfolio as Product
12. Professional Presence and Launch

### Back matter
- Acknowledgments · About the Authors · Notes · Glossary · References · Index

---

## What's in this repository

```
.
├── README.md                          # this file
├── 00-frontmatter.md                  # title, copyright, dedication, preface
├── 00-introduction.md                 # central claim + chapter map
├── chapters/                          # the twelve chapters (Markdown)
│   ├── 2026-05-02-chapter-01-the-creative-engineer.md
│   ├── 2026-05-02-chapter-02-the-madison-framework.md
│   ├── ...
│   └── 2026-05-02-chapter-12-professional-presence-and-launch.md
├── exercises/                         # running-project exercise tracks
│   ├── 2026-05-02-running-project-planning.md
│   └── 2026-05-02-self-as-project-exercises.md
├── 99-back-matter.md                  # acknowledgments, glossary, references
├── outline.md                         # full chapter outline + dependency map
├── lectures/                          # week-by-week lecture materials (course)
│   ├── week-1/ ... week-14/
└── images/                            # hero image briefs (per chapter)
```

Note: the original Canvas course exports, the Madison framework clone, and internal research notes used during drafting are not included in this repository. They live in a separate (private) workshop repo.

---

## How to use this book

### As a self-learner

Read front to back. The dependencies are real — the archetype you commit to in Chapter 1 informs the Madison-tool selection in Chapter 2, which becomes the design reference for the build sequence in Chapters 4–7, and so on. Skipping ahead is possible but loses the compounding.

Run the exercises. Every chapter ends with a copy-paste-ready prompt for Claude (or another LLM). The exercises are not optional. The reading without the doing produces understanding without the artifact, and the artifact is what the labor market rewards.

By the end of the book you will have:
- A deployed AI tool at a public URL
- A one-page personal brand strategy
- An archetype-aligned visual identity system
- A portfolio integrating the AI tool as a centerpiece case study
- A two-version resume + finalized LinkedIn + 10/20/30 pitch deck

### As an instructor

The book maps onto a 14-week semester with two assessment weeks (midterm pitch after Chapter 7; final presentations after Chapter 12). The course and the book do not run in the same order — the book teaches in logical-dependency sequence; the course teaches in build-priority sequence. We provide a representative semester mapping in the Introduction; build a semester-specific mapping for your own deployment.

The exercise system ships with one default running-project track ("Self-as-Project") plus alternates. See `exercises/2026-05-02-running-project-planning.md` for the full options.

We have taught this material as INFO 7375: Branding and AI at Northeastern University's College of Engineering. Instructors adopting the book are welcome to contact us for the course's slide decks, rubrics, and assessment materials.

### As a working engineer

The Build → Brand → Launch arc compresses cleanly into a personal sprint. Treat the book as a structured 8–12 week side project. The "Self-as-Project" exercise track is designed for exactly this use case.

---

## How to read each chapter

Each chapter follows a four-move structure:

1. **Hook** — open in a specific scene, datum, or puzzle
2. **Unfold** — force the central concept specific
3. **Deep-dive** — one mechanism explained from first principles
4. **Synthesize** — return to the hook with new understanding; close

Each chapter pairs with a real-world case (a brand-deployment success or a brand-failure-mode incident). Cases include Anthropic vs. OpenAI brand positioning, Linear's $100K no, Reddit's 2023 API rupture, Google Bard's $100B launch error, the Pepsi 2008 logo redesign, Airbnb's 2009 seed pitch deck, and others — all sourced to primary documents linked in-text.

Each chapter ends with a **What would change my mind** statement (a falsifiable test for the chapter's argument) and a **Still puzzling** statement (something the authors do not yet fully understand). These are not disclaimers; they are calibration commitments.

---

## Linked resources

- **Madison framework** (the technical reference architecture): [github.com/humanitariansai/madison](https://github.com/humanitariansai/madison)
- **Bear Brown LLC** (publisher / textbook workshop): [bearbrown.co](https://bearbrown.co)
- **Humanitarians AI** (Madison's developer community): [humanitarians.ai](https://humanitarians.ai)
- **INFO 7375 course at Northeastern**: contact the authors for current syllabus and enrollment info

---

## Errata, corrections, and feedback

If you find a factual error, broken link, or unclear passage, please open an issue in this repository with:

- The chapter number and section heading
- A direct quote of the problem text
- What you believe the correction should be
- A primary source for the correction, where applicable

The book follows an explicit hard-rules discipline: no fabricated sources, no invented quotes, no statistics without primary citation. We take errata seriously and will issue corrections in subsequent printings and in the online edition.

For substantive disagreements with the book's arguments — rather than factual errors — we welcome public criticism and engagement on Substack, LinkedIn, or in published reviews. We have flagged the limits of our argument throughout the chapters; the field is moving fast and we expect the bet the book is making to be tested against real outcomes over the next several years.

---

## Contributing

This is primarily a single-edition textbook, not an ongoing open-source project. We are not currently accepting pull requests for new chapters or major rewrites.

We *do* accept:
- Errata corrections (open an issue)
- Translations (contact the authors directly before starting)
- Adaptations for non-graduate-engineering audiences (contact the authors)
- Citation additions where a stronger primary source exists for an existing claim
- Glossary refinements where a definition is unclear or out of date

Adaptations of the embedded LLM exercises for ChatGPT, Gemini, or other tools are welcome and can be submitted as additions to the `exercises/` directory.

---

## License

The text of this book is © 2026 Nik Bear Brown & Nina Harris, published by Bear Brown, LLC.

Code samples, exercise prompts, and the structural framework presented in this repository are licensed under [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — free for educational and non-commercial use with attribution.

The Madison framework, referenced extensively throughout the book, is released by [Humanitarians AI](https://humanitarians.ai) under its own open-source license; references in this book are made under fair use for educational purposes.

Trademarks of third-party products discussed in case studies (Stripe, Anthropic, OpenAI, Google, Linear, Cursor, Tropicana, Pepsi, Gap, Snapchat, Airbnb, and others) remain the property of their respective owners.

Student work cited in the book — including AdverseAI, PositionPulse, and other named projects — appears with the permission of the students who built it and remains their intellectual property.

Commercial licensing inquiries: contact Bear Brown, LLC.

---

## Citation

If you cite this book in academic or professional work, please use:

> Brown, Nik Bear, and Nina Harris. *Branding and AI: Building the Creative Engineer.* Boston: Bear Brown, LLC, 2026.

For chapter-level citations:

> Brown, Nik Bear, and Nina Harris. "Chapter 1: The Creative Engineer." In *Branding and AI: Building the Creative Engineer.* Boston: Bear Brown, LLC, 2026.

---

## Contact

- **Nik Bear Brown** — Northeastern University, College of Engineering · [bearbrown.co](https://bearbrown.co) · [LinkedIn](https://www.linkedin.com/in/nikbearbrown/)
- **Nina Harris** — Northeastern University, College of Engineering (Adjunct) · [LinkedIn](https://www.linkedin.com/in/nina-harris-524ab7108/)

For course adoption inquiries, instructor materials, and bulk licensing: contact the authors directly via the LinkedIn links above.

---

*Now go ship.*
