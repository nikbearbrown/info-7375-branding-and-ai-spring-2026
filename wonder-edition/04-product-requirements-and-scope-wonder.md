# Module 4 — Product Requirements and Scope: Wonder Edition
## Companion Chapter

> **Wonder Edition:** This companion transforms Module 4's core concepts into a curiosity-driven narrative. Read it alongside the chapter, not instead of it.

---

## The Strange Question

Linear is a project management tool with fewer features than Jira, fewer features than Asana, and fewer features than most of its direct competitors. It has repeatedly declined enterprise customization requests — deals worth tens of thousands of dollars per year — because those customizations conflicted with its product philosophy.

Linear grew to $35 million in ARR.

Engineers recommend it to other engineers specifically because it does less. The product that said no more often is the product people choose. How does refusing to build things become the source of a product's appeal?

---

## First Intuition

The intuitive answer is that Linear just executed better on fewer things — higher quality, faster performance, cleaner design. This intuition comes from experience with products that fail not from scope but from poor execution: the feature exists but it is buggy, slow, or hard to find. The lesson feels like: do fewer things, but do them well.

Under this model, the right approach is to prioritize ruthlessly and then execute excellently on the prioritized list. Features get added when the quality bar is met. The out list is a queue, not a refusal.

> **► Planning prompt:** Before reading further, state your current explanation for why a product with fewer features would be preferred over one with more features, when the user needs the additional features. What prior experience with software products shapes your assumption? Predict what would happen to Linear's user base if it added the enterprise customizations competitors offer. Write your prediction before continuing.

---

## The Surprise

But Linear's team did not decline those enterprise customization requests because they could not execute on them. The argument was not "we are not ready yet." The argument was "building this feature would damage the product for the users who chose us." The enterprise requests were technically feasible, economically attractive, and strategically rejected.

The result was not a smaller user base — it was a more coherent one. Engineers who chose Linear chose it specifically because it had a point of view about how engineering work should be managed. Adding configurable multi-workflow support would have made Linear more useful to the enterprise prospect and simultaneously less useful to the engineer who recommended it. The product would have acquired one customer type while alienating the customer type that drove its growth.

The chapter's central case: the things a product refuses to build define it more than the things it builds. Every feature Linear added in v1 could have been duplicated by a competitor. Every feature it refused could not be imitated without adopting Linear's point of view — and adopting Linear's point of view meant also adopting Linear's constraints.

> **► Monitoring prompt:** In your own words, describe what your initial prediction assumed about how product quality and feature scope interact. What specific part does Linear's enterprise refusal evidence contradict? What does your current model still fail to explain about why the refusal attracted users rather than losing them?

---

## The Hidden Structure

Therefore, scope discipline in a Product Requirements Document is not primarily a capacity management tool. It is an identity statement. The out list — the explicit record of what the product will not do — is the mechanism that prevents the accumulated incoherence that comes from responding to every feature request with yes.

The PRD structures this through four sections: Problem (who has the pain, how often, what it costs), Gap (what exists and where it fails the specific user), Tool (what exactly will be built, in one user-parseable sentence), and MVP Boundary (the in list and, critically, the out list with the $100,000 no at the top). The $100,000 no is the feature a real user will request, with a real argument, that the builder declines because including it would open a door to a different product with a different philosophy.

It is tempting to think that the MVP boundary is a temporary restriction — a queue of features waiting until the team has capacity. But the Build-Measure-Learn loop from Eric Ries's Lean Startup shows why this framing is wrong. The correct model holds that the MVP's purpose is validated learning, not minimum effort. The smallest thing that tests the core hypothesis is smaller than the smallest thing most builders ship as a "minimum." The key distinction is between minimum as "least effort" and minimum as "tightest test of one assumption" — the second is structurally smaller and produces faster learning.

The PRD also enforces the what/how distinction Marty Cagan formalized in Inspired: the document specifies what the product does, not how it does it. A PRD that names the implementation technology ("uses GPT-4o-mini with temperature 0.2") has made an engineering decision inside a product document. That decision, once in the PRD, gets treated as a requirement. When the implementation needs to change — and it always does — the PRD becomes a source of false constraints.

---

## Try Looking At It This Way

**Target:** PRD scope discipline — the principle that the out list is more strategically important than the in list, and that explicit refusals enforce product identity.

**Base:** A constitutional Bill of Rights.

**Features:**
- The PRD's in list corresponds to enumerated powers — both specify what is explicitly authorized.
- The PRD's out list corresponds to protected rights — both specify what cannot be done regardless of apparent benefit.
- The $100,000 no corresponds to a constitutional constraint that cannot be waived by simple majority — both resist the immediate pressure of short-term benefit to preserve long-term integrity.

**Commonalities:** A constitution's power comes not from what it authorizes but from what it prohibits. A government that could override rights whenever a majority agreed would quickly find majority preferences eroding those rights. The constraint is load-bearing precisely because it applies even when overriding it seems locally beneficial. The PRD out list operates the same way: its value is not in the first item excluded but in its resistance to the accumulation of exceptions. "Just this once" is the mechanism by which both constitutions and product scope collapse.

**Boundaries:** A constitution is enforced by a separate judiciary with coercive power. A PRD's out list is enforced only by the commitment of the people who wrote it. There is no external mechanism preventing a team from adding features. The PRD is a voluntary constraint, which means its value depends entirely on the team's willingness to use it as an arbiter rather than a historical document.

**Conclusions:** An out list that everyone treats as permanent protects the product's coherence the same way a constitutional right protects a minority from majority override — by pre-committing to a limit before the pressure to override it arrives.

---

## Where The Analogy Breaks

Unlike a constitutional amendment process, a PRD's out list has no formal mechanism for revision. A feature excluded in v1 can be added in v2 without any deliberate process — the team simply starts building it. This matters because the constitution analogy might suggest that changing the out list is difficult or requires special process. In practice, it requires only a decision. The protection the out list provides is entirely social and psychological: a team that treats the out list as a contract is protected from scope creep; a team that treats it as a wishlist is not. The PRD is only as durable as the team's commitment to using it as an arbiter.

---

## Small Discovery

**Raw data:** A restaurant operates in a neighborhood with heavy foot traffic. It started with a focused menu: eight items, all variations on one cuisine, no substitutions, no customization. In year two, responding to customer requests, it added a kids' menu, gluten-free alternatives for every item, two items from a neighboring cuisine, and a catering option for office lunches.

Kitchen staff tracked order error rates (wrong dish delivered) and average ticket preparation time:

| Period | Menu size (items) | Order error rate | Average preparation time |
|--------|-------------------|-----------------|--------------------------|
| Year 1 (original) | 8 | 2.1% | 7.2 minutes |
| Year 2, Q1 (early additions) | 14 | 3.8% | 9.1 minutes |
| Year 2, Q4 (full expansion) | 22 | 6.4% | 14.3 minutes |

Yelp reviews over the same period: Year 1 average rating 4.7. Year 2 Q4 average rating 4.2.

**Pattern search:** Revenue increased in Year 2 because more menu items attracted more customer types. Error rates and preparation times both increased. The rating fell. What does this pattern suggest about the relationship between menu expansion and the quality of the core experience?

**Prediction:** In Year 3, if the restaurant removes the additions and returns to eight items, would the error rate and preparation time return to Year 1 levels? Would the rating recover? Write your prediction before continuing.

---

The Year 2 data shows that each addition imposed a coordination cost on the whole system. A kitchen optimized for eight items develops muscle memory and rapid execution for those specific dishes. Adding catering, gluten-free alternatives, and cuisine variations requires the kitchen to hold more variations in working memory, creates more possible error states, and slows every station. The rating decline is not because any individual item got worse — it is because the experience of every item got slightly slower and slightly less reliable as the system adapted to a wider problem space.

This is the PRD's out list argument in a food-service domain. The restaurant's refusal to add items in Year 1 was the same discipline as Linear's refusal to add enterprise customizations. Both refusals preserved the coherence of the core experience. Both refusals felt like leaving revenue on the table. Both were the mechanism that made the core product excellent. The kitchen's error rate is the product-quality analogue of what the chapter calls incoherence accumulation — each "yes" to a new feature imposes a small coordination cost on the whole, and the costs compound.

---

## What This Changes

A student who has internalized this chapter can now answer a question that would have confused them before: why does adding features — things users asked for, things competitors have, things that seem obviously valuable — sometimes make a product worse? The answer is that each addition imposes coordination costs on every existing feature and signals a point of view that may conflict with the existing product's identity.

What looks different now in a real product decision: a user request that generates a "yes, good idea" reaction should now trigger a second question: "does this feature belong in v1 given the hypothesis we are testing, and does including it change who this product is for?" Those are different from "is this a good feature?" — which almost always gets a yes.

**Practice Bridge:** Before writing the first line of pipeline code in Chapter 5, a student needs a one-page PRD with four sections completed: a specific problem statement with a named user, frequency, and cost; a gap analysis naming three competitors and their failure modes; a tool description in one sentence parseable by a non-technical user; and an MVP boundary with the $100,000 no as the first item in the out column. That document is the gate to Chapter 5.

What this chapter leaves open: how to identify the $100,000 no before the enterprise prospect arrives to request the feature. The chapter gives the principle but the identification requires knowing what the product's core is — which requires having users. Chapter 5's pipeline builds the thing users can encounter, and the first user feedback is what makes the $100,000 no visible in practice rather than theory.

---

## Wonder Questions

1. Linear's scope discipline produced a product that engineers recommend to other engineers specifically because it does less. What is the mechanism — not the outcome, but the specific causal chain — by which refusing features causes word-of-mouth recommendation?

2. The PRD distinguishes between what a product does (belongs in the document) and how it does it (belongs with engineering). If a user's core need is "I want results in under three seconds," is response time a what or a how? What are the implications of your answer for how to write the tool description?

3. The Build-Measure-Learn loop requires knowing which assumption is being tested before building. If a team builds an MVP without stating the falsifiable hypothesis first, what specific problem does this create at the Measure step?

4. The chapter says the out list is more important than the in list. But the out list only works if the team treats it as a contract. What specific decision pattern — repeated enough times — turns an out list from a contract into a historical document? What would you watch for to detect this transition early?

5. A competitor enters your market with a product that includes everything in your out list and matches the quality of your in list. Does this falsify the chapter's argument about scope discipline — or does the competitor's entry raise a different question? What is the question?

---

> **What the concept is:** A Product Requirements Document is a written contract with future decision-making — it specifies what the product will do, for whom, and explicitly what it will not do, creating a pre-committed constraint that resists the accumulation of incoherence under pressure.
>
> **What it explains:** Why Linear grew to $35M ARR by saying no to enterprise deals; why scope creep degrades products that are technically excellent; why the out list is the mechanism that makes a product's identity durable rather than provisional.
>
> **What it does NOT mean:** It does not mean features in the out list should never be built. It means they should not be built in v1, before the core hypothesis is validated. A feature excluded in v1 can become the right addition in v3 — after validated learning shows the core is working and the addition extends rather than redirects it.
>
> **What comes next:** Chapter 5 builds the data pipeline that the PRD specifies. The MVP boundary the student defined here is exactly what Chapter 5 implements — the scope decision becomes the build specification, and the $100,000 no becomes the first thing the engineer avoids building.

---

## Author Notes

**Core misconception targeted:** The belief that the out list is a temporary queue — features waiting until capacity allows — rather than a strategic commitment that preserves the product's identity and user coherence.

**Analogy base domain:** Constitutional Bill of Rights; the specific boundary flagged is that constitutional amendments require formal process while PRD revisions require only a team decision, making the PRD's protection entirely social rather than structural.

**Bloom's arc:** The Strange Question (Remember) → The Surprise (Analyze) → The Hidden Structure (Understand/Apply) → Small Discovery (Apply/Evaluate) → What This Changes (Evaluate/Create)
