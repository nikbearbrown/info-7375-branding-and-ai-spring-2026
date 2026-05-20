# Hero image brief — Chapter 23: Case: Build to Trust — Deepa Shenoy

**Subject.** A clean schematic composition rendering the Validation-First Pipeline as a five-stage horizontal flow: *Ingest → Deduplicate → Reconcile → Validate → Publish*, each stage rendered as a discrete card with a labelled gate symbol between cards. The fifth card — *Publish* — is the only card with a saturated mint-green border, signalling *certified data; no publish without passing*. To the upper-left of the pipeline, a small annotated SQL snippet rendered in monospaced micro-type shows the duplicate-transaction-ID dedup query (`ROW_NUMBER() OVER PARTITION BY transaction_id`) — the audit story made literal. A faint *15–20%* annotation appears near the Deduplicate stage as the conversion-inflation figure the framework caught.

**Mood.** Documentary-precise, considered, slightly editorial. The composition should feel like a well-designed reference diagram in a data-engineering technical book rather than a marketing graphic. The mint accent is doing one job and only one job: it appears once, on the publish gate.

**Negative space for title overlay.** Reserve the upper third of the canvas for chapter title and case-tagline overlay. The pipeline sits at lower-centre, weighted across the canvas at small-to-medium scale, leaving the upper portion in deep-navy for typography. The DS monogram appears once at very small scale in the lower margin.

**What the teaching image should make most visually prominent.** The *single mint-green border on the Publish card* — the rest of the pipeline is rendered in indigo-and-navy restraint, and the eye is drawn to the one place where data passes the gate. The visual argument is that *trust is what the gate produces*, and the gate is the only saturated colour in the composition.

**Palette.** Deep Navy `#000024` ground; Navy `#243799` for primary card fills; Indigo `#5A6ED8` for secondary line weight and gate symbols; Mint Accent `#7BFFD8` exclusively on the *Publish* card border (the semantic-accent rule). Crisp white only for typography on the cards. No additional saturated colors.

**Style references.** The reference-diagram register of Stripe's documentation pipelines; the considered restraint of dbt's marketing graphics; the architectural cleanness of *Designing Data-Intensive Applications*' chapter-opener illustrations. Avoid the saturated marketing register of generic data-tooling hero images.

**What to avoid.** No literal Snowflake, dbt, Airflow, Spark, or AWS logos. No human figure. No "AI brain" iconography. No glowing or pulsing effects. No additional mint accents beyond the single Publish-card border. No code on screen except the small dedup-SQL annotation. The five-stage pipeline plus the one annotated SQL fragment plus the mint-bordered publish gate are the entire composition.
