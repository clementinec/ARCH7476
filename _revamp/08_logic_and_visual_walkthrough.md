# Weekly Logic and Visual Walkthrough

Purpose: review the rebuilt course materials as an architect would read them: does the sequence help students build a defensible design rationale, and where do slides need concrete visual support rather than more text?

This is not a request to create more lecture work. The recommended fixes are deliberately scoped:

1. keep the existing useful lecture bodies;
2. align the semester sequence across `schedule.qmd`, assignments, and weekly decks;
3. replace adversarial or playful wrappers with graduate-seminar language;
4. add only the missing visual anchors that would make the logic teachable.

## Current Course Logic

The strongest low-work sequence is:

| Phase | Weeks | Assignment | Role in the design rationale |
|---|---:|---|---|
| Recall and diagnose | 1-3 | A1 | What evidence supported a past studio decision, and what was actually assumption, precedent, or judgment? |
| Choose evidence and route | 4-6 | A2 | Which evidence route can realistically support one next design decision? |
| Build and verify | 7-9 | A3 | Can the workflow compare variants/scenarios and produce one interpretable output? |
| Communicate and transfer | 10-12 | A4 | What decision changes, what should happen next, and what can be reused? |

The rebuilt root pages mostly support this. The largest inconsistency was the schedule: it promised an early GH/tool-translation sequence, while the actual decks run evidence audit -> spreadsheet -> GIS -> BIM/BEM -> pathway mapping. That actual sequence is defensible and probably lower-work, so the schedule should follow the decks rather than forcing a new GH-heavy rebuild.

## Global Findings

| Area | Status | Recommended action |
|---|---|---|
| Assignment spine | Solid | Keep A1/A2/A3/A4 structure. It is clearer than the old offering. |
| Schedule/deck alignment | Was inconsistent | Updated `schedule.qmd` to match actual weekly decks. |
| Week 1 | Mostly right direction | Keep structure; soften tone; add/curate better image examples as needed. |
| Weeks 2-7 | Logically usable but visually thin | Add 1-3 anchor visuals per week, not full rebuilds. |
| Weeks 8, 10, 11, 12 | Activity mechanics useful, tone too playful | Translate "battle/champion/gladiator" wrappers into professional clinic/review language. |
| Route coverage | Previously too narrow in some decks | Updated pathway lists to include spreadsheet, GIS, Python, GH, BIM/BEM, and AI-assisted routes. |
| Missing runnable assets | Real gap | Do not promise full GH/simulation/AI demos until starter examples exist. Use visual workflow examples first. |

## Week-by-Week Walkthrough

### Week 1: Why Evidence Needs a Workflow

**Logic status:** good opening. It now makes A1 a three-week arc and introduces the course as studio evidence workflow rather than software shopping.

**Keep:**

- full-semester overview;
- A1 three-week arc;
- Slack visual sharing;
- Session 2 round table;
- vibes-vs-evidence slide sequence.

**Tone fix applied:** language now says what evidence "does not prove yet" instead of "why it fails."

**Minimal visual need:** one completed Total Recall board example.

**Slide description:** show one past studio project on a single board with five labeled zones: `decision`, `original evidence`, `what it supported`, `what it did not show`, `next evidence move`. Use an architectural plan/render fragment, a precedent image, and a small evidence table. This would let students see what A1 actually looks like by Week 3.

### Week 2: Evidence Audit

**Logic status:** good A1 Week 2 continuation. The deck correctly asks students to separate evidence, precedent, assumption, and overclaim.

**Keep:**

- evidence ladder;
- fast audit template;
- common overclaims;
- next-decision pivot.

**Problem:** visually thin. It depends too much on text lists.

**Minimal visual needs:**

1. evidence ladder as a vertical visual;
2. one worked weak-link diagnosis;
3. one architecture-specific overclaim example.

**Slide description:** create a four-card spread using the same studio image repeated four ways: `precedent image`, `site observation`, `simulation output`, `user comment`. Each card shows what it supports and what it cannot support. The visual point: evidence types are not ranked universally; they are fit to a specific claim.

### Week 3: Spreadsheet as Baseline Workflow

**Logic status:** stronger than it may sound. It should be framed as the transparent comparison layer, not "Excel week."

**Keep:**

- workbook pattern;
- chart catastrophe;
- 3-second message test;
- decision matrix example;
- peer swap test.

**Problem:** MArch students may read "spreadsheet" as remedial unless it is tied to generative comparison.

**Minimal visual needs:**

1. before/after chart rescue;
2. three-variant decision matrix;
3. workbook anatomy screenshot/mockup.

**Slide description:** show a realistic workbook mockup with three tabs: `Evidence Log`, `Variants`, `Output Figure`. The visible sheet compares three facade, access, or massing variants with ranges rather than single fake-precise numbers. A second slide should show a bad chart and the cleaned-up version side by side.

### Week 4: GIS Choices for Architects

**Logic status:** solid. It is a tool-literacy week that helps students decide whether spatial evidence belongs in their pathway.

**Keep:**

- QGIS / ArcGIS / geopandas comparison;
- setup ladder;
- core GIS operations;
- Hong Kong data sources;
- "do not choose GIS because maps look professional."

**Problem:** needs visual examples of decision maps, not just maps.

**Minimal visual needs:**

1. decorative map vs decision map;
2. layer stack diagram;
3. GIS output matched to a studio decision.

**Slide description:** use a site map with three transparent layers: transit access, noise/flood constraint, and zoning boundary. Then show the actual decision question beside it: "Which edge should carry public access?" The map should clearly change a design action, not just provide context.

### Week 5: BIM, BEM, and Building Performance

**Logic status:** technically strong. It explains BIM/BEM translation more clearly than most students will have seen before.

**Keep:**

- BIM vs BEM distinction;
- data priority lists;
- translation gap;
- IFC vs `gbXML`;
- translation-gone-wrong case study.

**Problem:** it is literacy-heavy and may overpromise simulation unless a runnable demo exists.

**Minimal visual needs:**

1. same building, two models: BIM view vs BEM view;
2. translation pipeline with lost/missing data highlighted;
3. "clean-looking output, weak assumptions" example.

**Slide description:** split the slide in half. Left: architectural BIM model with walls, rooms, materials. Right: simplified BEM model with thermal zones, schedules, weather, and HVAC. Use red markers for things that often fail to translate: zoning, schedules, constructions, orientation.

### Week 6: Evidence and Pathway Mapping

**Logic status:** good A2 decision gate. It is the right week to force pathway choice and A4 route declaration.

**Keep:**

- evidence triage;
- pathway comparison;
- pathway commitment sentence;
- warning signs.

**Problem:** needs the Route A / Route B branch visually, otherwise A4 can still feel abstract.

**Minimal visual needs:**

1. Route A vs Route B fork diagram;
2. evidence-pathway matrix example;
3. "one decision, not whole project" guardrail slide.

**Slide description:** show a forked timeline. Route A starts from a past studio board and returns to a redesigned decision. Route B starts from a current studio board and feeds forward into an active studio move. Both converge on the same A4 components.

### Week 7: Method Prototype Studio

**Logic status:** useful. It gives students a professional reason to document their prototype before A3.

**Keep:**

- minimal viable workflow;
- 10-minute method challenge;
- documentation template;
- documentation swap;
- mentor question development.

**Tone fix applied:** "horror / graveyard / harsh truth" language softened to reproducibility lessons and documentation reality checks.

**Problem:** needs stronger A3 generative loop and route-specific examples.

**Minimal visual needs:**

1. A3 loop diagram: `input -> variation -> output -> threshold -> action`;
2. route example cards;
3. reproducibility capsule anatomy.

**Slide description:** create six small route cards: spreadsheet, GIS, Python, GH, BIM/BEM, AI-assisted. Each card shows `input`, `what varies`, `output`, `quality check`. This slide would prevent students from thinking there is only one acceptable technical route.

### Week 8: Reproducibility, Automation Ethics, and Mentor Prep

**Logic status:** content is useful but wrapped in the wrong tone.

**Keep:**

- documentation swap;
- automation ethics scenarios;
- mentor question workshop;
- follow-up template;
- reproducibility package activity.

**Problem:** "Documentation Olympics", "battle royale", "warrior", "evil", and pledge language are not appropriate for the rebuilt MArch-first course.

**Minimal rewrite:** translate wrappers only:

| Current wrapper | Better title |
|---|---|
| Documentation Olympics | Workflow Documentation Clinic |
| Automation Ethics Showdown | Automation Ethics Cases |
| The Automation Tribunal | AI Method Review |
| Reproducibility Battle Royale | Peer Reproducibility Check |
| Victory Checklist | Week 8 Checklist |

**Minimal visual needs:**

1. AI prompt log anatomy;
2. verification ladder for AI-assisted output;
3. mentor question board.

**Slide description:** show an AI-assisted workflow card with four columns: `prompt`, `AI output`, `manual check`, `disclosure note`. Use one architecture example such as AI helping draft a `geopandas` buffer script or a GH Python component, then show what the student must still verify.

### Week 9: Storytelling, Figures, and Decisions

**Logic status:** strong. This is one of the cleaner decks after Week 1.

**Keep:**

- two-slide challenge;
- story structure;
- figure rescue;
- object card priorities;
- thresholds and counter-arguments;
- recommendation sentence drill.

**Problem:** needs A3 due / A4 launch framing and a few concrete threshold examples.

**Minimal visual needs:**

1. before/after figure rescue;
2. object card anatomy;
3. threshold examples across project types.

**Slide description:** build one object-card mockup with a dominant recommendation, one comparison figure, one threshold sentence, and one limitations note. A second slide can show thresholds: access time, daylight hours, cost premium, heat gain, survey confidence.

### Week 10: Draft Workflow Review

**Logic status:** the review mechanics are useful, but the deck tone is the biggest mismatch in the course.

**Keep:**

- 6-8 minute presentation timing;
- Q&A format;
- feedback integration matrix;
- object fair preparation logic.

**Problem:** "gladiator arena", live scoring, combat, coronation, and victory language should be removed or translated. The current wrapper makes critique feel like spectacle.

**Minimal rewrite:** convert the deck into a professional draft review:

| Current wrapper | Better title |
|---|---|
| Gladiator Arena | Draft Workflow Review |
| Combat Rules | Review Format |
| Live Combat Analytics | Review Notes |
| Hall of Fame Moments | Useful Review Moves |
| Emergency Improvement Strategy Lab | Feedback Integration Lab |
| Gladiator's Creed | Exit Revision Plan |

**Minimal visual needs:**

1. draft review checklist;
2. feedback matrix example;
3. A4 package gap map.

**Slide description:** show a one-page review sheet with the six items critics inspect: `decision`, `variants/scenarios`, `workflow`, `output`, `threshold`, `limit`. The slide should make the review feel architectural and professional, not competitive.

### Week 11: Final Package Polish

**Logic status:** useful final-production content under too much championship language.

**Keep:**

- visual polish lab;
- content refinement workshop;
- message clarity clinic;
- Q&A preparation;
- final submission checklist.

**Problem:** final package components are not foregrounded enough. Networking content is useful but should not displace the A4 package.

**Minimal rewrite:** convert "championship training" into "Final Package Clinic."

**Minimal visual needs:**

1. A4 component exploded view;
2. object card wall/readability mockup;
3. final QA checklist.

**Slide description:** show four A4 components as linked documents: `Practice Case`, `Research Brief`, `Object Card`, `Reproducibility Capsule`. Draw arrows showing which component answers which question: what changed, how you know, what viewers see, how someone inspects the method.

### Week 12: Object Fair

**Logic status:** event structure exists, but the language is over-celebratory.

**Keep:**

- presentation timing;
- Q&A;
- professional review;
- peer reflection;
- transfer-forward prompt.

**Problem:** "championship" framing is unnecessary. The final class should feel like a professional review and synthesis.

**Minimal rewrite:** convert to "Object Fair: Final Review and Transfer."

**Minimal visual needs:**

1. run-of-show slide;
2. final evidence loop criteria slide;
3. transfer-forward reflection.

**Slide description:** show the final loop as a clean diagram: `design decision -> variants/scenarios -> workflow -> evidence output -> threshold -> design action -> limit`. This should be the evaluation frame for every final presentation.

## Priority Order

Do not rebuild everything at once.

1. **Tone-align Weeks 8, 10, 11, 12.** This is the largest perception problem and mostly a wrapper rewrite.
2. **Add one worked A1 board to Week 1.** This is the highest-value missing visual.
3. **Add visual anchors to Weeks 2, 3, 5, and 7.** These weeks explain invisible logic and need examples.
4. **Add Route A/B and pathway matrix visuals to Week 6.** This controls A4.
5. **Add threshold/object-card visuals to Week 9.** This prepares A4 without heavy new content.
6. **Only then build runnable GH/simulation/AI examples.** These are valuable but should not be promised until ready.

## What Not To Do

- Do not make GH the entire course unless a full GH teaching sequence exists.
- Do not delete the spreadsheet/GIS/BIM/BEM material; it is part of a realistic evidence workflow course.
- Do not add many new readings or long theory slides.
- Do not turn every week into a full formal presentation.
- Do not keep the competition/championship wrapper for graduate students.

## Immediate Edits Already Made

- `schedule.qmd` now matches the actual week sequence.
- Week 1 language is softer and more constructive.
- Week 2 pathway list includes spreadsheet, GIS, Python, GH, BIM/BEM, and AI-assisted routes.
- Week 3, Week 5, Week 6, and Week 7 pathway references were broadened to match the course routes.
- Week 7 reproducibility language was softened.
