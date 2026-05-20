# Enrichment + Cleanup Log

Run: 2026-05-04 — branding-and-ai

## What changed (most recent → earliest)

### Build pipeline now works end-to-end

`bash build.sh` produces both `output/branding-and-ai.epub` and `output/branding-and-ai.html` from the 16-chapter set. EPUB chapter splits land cleanly on the 16 H1s.

Files added at the book root:

- `metadata.yaml` — pandoc-format metadata (title, author, language, subjects, keywords)
- `styles/kindle.css` — baseline editorial / serif / monochrome stylesheet
- `styles/kindle-book.css` — book-specific overrides
- `build.sh` — pandoc → EPUB + HTML build script (executable)

### Inconsistencies fixed

- **Chapter 8 personal-path was mis-titled.** Both Chapter 8 files had H1 *"Chapter 8 (Startup Brand Path) — Brand Strategy"* — the personal-path file inherited the wrong title from a copy. Corrected to *"Chapter 8 (Personal Brand Path) — Brand Strategy"*. Both chapters now appear distinctly in the TOC.
- **Trailing whitespace normalized** across all 16 chapter files so concatenation in the build pipeline doesn't fuse a paragraph with the next chapter's H1.
- **Inline `[TIMELINE: ...]` comment in chapter 1** that had been concatenated onto the previous figure's caption line was extracted and rendered as Figure 1.4.
- **Stale stub tables** that had been attached to the original `[INFOGRAPHIC: ...]` and `[CHART: ...]` comments (figs 8.4 and 12.10) were removed when those comments were rendered as figures, eliminating the duplicate `*Figure N.N*` labels and `_fill in_` stub rows.

### All Wayback Machine sections authored

Thirteen new `## AI Wayback Machine` sections appended at end-of-chapter for Ch 1–12 plus the 8-startup variant. Each follows the spec format: contextualizing paragraph naming the figure, AI-portrait stub (alt text + italic caption, both pointing at `images/{slug}.jpg`), Run-this prompt block, Wikipedia search hint, three "make the prompt better" variants.

| Ch | Subject | Era | Connection to chapter |
|---|---|---|---|
| 1 | **Thorstein Veblen** (1857–1929) | c. 1880s | *Theory of the Leisure Class* — conspicuous consumption as the pre-Spence root of costly signaling |
| 2 | **Marshall McLuhan** (1911–1980) | c. 1960s | *The medium is the message* — system architecture is the brand |
| 3 | **Carl Jung** (1875–1961) | c. 1910s | The source the twelve-archetype framework borrows from; shadow as load-bearing failure mode |
| 4 | **Adele Goldstine** (1920–1964) | c. 1940s | Wrote the *ENIAC Operator's Manual* (1946) — the foundational PRD; scope defined by what is *out* |
| 5 | **Joan Robinson** (1903–1983) | c. 1940s | Coined *monopsony* — the platform/third-party-developer dynamic the Apollo case exemplifies |
| 6 | **Herbert A. Simon** (1916–Feb 2001) | c. 1970s | *Bounded rationality* + *near-decomposability* — the design rationale for specialized multi-agent systems |
| 7 | **Vannevar Bush** (1890–1974) | c. 1940s | *As We May Think* (1945) — the memex; interface as contract between capability and attention |
| 8 personal | **Helen Lansdowne Resor** (1886–1964) | c. 1920s | JWT pioneer; built her personal brand in advertising as a constraint set, not a description |
| 8 startup | **Bill Bernbach** (1911–1982) | c. 1960s | DDB; *Think Small*, *We Try Harder* — the disruptive-startup move of *naming* what the incumbent refuses to admit |
| 9 | **Cipe Pineles** (1908–1991) | c. 1940s | First independent female art director of major US magazines; visual identity as a system, not a logo |
| 10 | **Joseph Campbell** (1904–1987) | c. 1950s | *The Hero with a Thousand Faces* — the structural source the chapter borrows |
| 11 | **Charles & Ray Eames** (1907–1978; 1912–1988) | c. 1950s | Furniture, film, exhibitions, photography — varied portfolio unified by one design philosophy |
| 12 | **Margaret Bourke-White** (1904–1971) | c. 1930s | First-woman-anywhere assignments at *Life* and the war-correspondent press; presence as designed artifact |

All 13 subjects are pre-2001 dead OR foundational work entirely pre-2001. None overlap the existing botspeak Wayback list (Avram, Ashby, Vygotsky, Deming, Follett, Pask, Wald, Shewhart, Meadows, Wiener, Hopper, Turner, Gödel, Chao). Diversity: 7 men, 5 women, 1 mixed pair (Eameses).

### Tables and figures rendered

| Pass | Output | Detail |
|---|---|---|
| Pass 1 | 22 markdown tables | Across chapters 01, 05, 08-personal, 12 |
| Pass 2 | 14 SVG/PNG figure pairs (IMAGE/FIGURE/DIAGRAM) | All in editorial monochrome warm-grayscale, Georgia serif, 1px borders, no rounded corners. PNGs at 2× the SVG viewBox |
| Pass 2b | 7 SVG/PNG figure pairs (INFOGRAPHIC/CHART/TIMELINE) | Originally out-of-scope per literal token list; rendered in the same style for consistency |
| Pass 2c | 2 SVG/PNG figure pairs (CALLOUT BOX + the inline TIMELINE) | Caught the missing comments — pull-quote (1.2) and signal-collapse timeline (1.4) |
| Pass 3 | 13 Wayback Machine sections | Authored from scratch — none existed before |

### Per-chapter results

00-frontmatter.md — 0 tables / 0 figures / no Wayback (front matter)
00-introduction.md — 0 tables / 0 figures / no Wayback (intro)
01-the-creative-engineer.md — 1 table / 7 figures (1.1–1.5, 1.8, 1.10, 1.12, 1.13) / Wayback: Thorstein Veblen
02-the-madison-framework.md — 0 tables / 0 figures / Wayback: Marshall McLuhan
03-jungian-brand-archetypes-as-a-system.md — 0 tables / 0 figures / Wayback: Carl Jung
04-product-requirements-and-scope.md — 0 tables / 0 figures / Wayback: Adele Goldstine
05-data-pipelines-and-workflow-automation.md — 6 tables / 6 figures (5.1, 5.4, 5.7, 5.8, 5.9, 5.11) / Wayback: Joan Robinson
06-ai-intelligence-and-multiagent-systems.md — 0 tables / 0 figures / Wayback: Herbert A. Simon
07-interface-design-and-deployment.md — 0 tables / 0 figures / Wayback: Vannevar Bush
08-personal-brand-path-brand-strategy.md — 7 tables / 4 figures (8.2, 8.4, 8.8, 8.10) / Wayback: Helen Lansdowne Resor
08-startup-brand-path-brand-strategy.md — 0 tables / 0 figures / Wayback: Bill Bernbach
09-visual-identity-systems.md — 0 tables / 0 figures / Wayback: Cipe Pineles
10-brand-storytelling.md — 0 tables / 0 figures / Wayback: Joseph Campbell
11-portfolio-as-product.md — 0 tables / 0 figures / Wayback: Charles & Ray Eames
12-professional-presence-and-launch.md — 8 tables / 4 figures (12.2, 12.6, 12.10, 12.11) / Wayback: Margaret Bourke-White
99-back-matter.md — 0 tables / 0 figures / no Wayback (back matter)

## Summary

Total chapters processed: 16
Total tables rendered: 22
Total figures generated (SVG+PNG pairs): 23
Total Wayback Machine subjects added: 13

## Action items the build pass cannot complete on its own

### Generate 13 portrait .jpg files

The Wayback Machine stubs reference these AI-redrawn portrait files:

- `images/thorstein-veblen.jpg` (Ch 1) — c. 1880s, monochrome portrait
- `images/marshall-mcluhan.jpg` (Ch 2) — c. 1960s, monochrome portrait
- `images/carl-jung.jpg` (Ch 3) — c. 1910s, monochrome portrait
- `images/adele-goldstine.jpg` (Ch 4) — c. 1940s, monochrome portrait
- `images/joan-robinson.jpg` (Ch 5) — c. 1940s, monochrome portrait
- `images/herbert-simon.jpg` (Ch 6) — c. 1970s, monochrome portrait
- `images/vannevar-bush.jpg` (Ch 7) — c. 1940s, monochrome portrait
- `images/helen-lansdowne-resor.jpg` (Ch 8 personal) — c. 1920s, monochrome portrait
- `images/bill-bernbach.jpg` (Ch 8 startup) — c. 1960s, monochrome portrait
- `images/cipe-pineles.jpg` (Ch 9) — c. 1940s, monochrome portrait
- `images/joseph-campbell.jpg` (Ch 10) — c. 1950s, monochrome portrait
- `images/charles-and-ray-eames.jpg` (Ch 11) — c. 1950s, monochrome portrait of the pair
- `images/margaret-bourke-white.jpg` (Ch 12) — c. 1930s, monochrome portrait

Until those files exist, the EPUB references them but cannot embed them. The HTML proof shows them as broken images.

### Add a cover image

`build.sh` looks for `cover.jpg` at the book root. KDP wants 1600×2560 JPEG, RGB, ≤50 MB. The EPUB builds without it; cover is required only for KDP upload.

### Voice flag

This book has no per-book `style/` voice samples yet, so drafts here remain `voice-unanchored` per `book.md` §Voice. The 13 Wayback sections were written in workshop voice; voice review is recommended before final publish.

## Build commands

```
cd books/branding-and-ai
./build.sh
```

Outputs land in `output/`: `branding-and-ai.epub` (KDP-ready), `branding-and-ai.html` (proofing mirror), and `combined.md` (archival concatenated source).
