# Session Log · 9 Nov 2026 · Week 9 "Thresholds, Drawn"

Working log for picking the rebuild back up in later weeks. Covers what
changed, why, where it lives, and what is still open.

## Context

- Class size this term is very small. For Week 9 we plan for **two students plus the instructor**: one student is on exam leave, and another has not attended for two weeks.
- The two attending students work at different levels:
  - **PhD, research track:** multi-objective optimisation to choose a site for a shaded pavilion.
  - **Undergraduate, studio track:** massing and volume studies for their own studio project.
- Week 8 covered generative AI / LLMs and reproducibility. Week 9 follows on from it.
- Decision: **flip the class**. Students prepare before class; class time is spent drawing, swapping, and arguing, not listening to a lecture. Thresholds are taught *inside* visual storytelling: every figure shows its threshold explicitly.

## What changed

### Week 9 deck · `weeks_v2/week-09.qmd`

Rebuilt from the old 45-slide "Storytelling, Figures, and Decisions" deck into a 26-slide deck titled **"Thresholds, Drawn"**. Most of the old list slides were removed; the four public-domain anecdote images were kept and reframed.

| Part | Content |
|---|---|
| Before class | Bring one A3 output, write two **diagram briefs** (decision / data / threshold + source / audience / must-show), and try the Threshold Explorer |
| Session 1 | Drawn SVG diagrams, each with one "Ask the room" question: Challenger launch temperature (53°F edge of experience vs 36°F launch); facade knife edge (hard lines vs review bands); flip distance; 800 m walking ring vs the street network; four PM2.5 lines (HK AQO before/after 2022 vs WHO 2005/2021, including the counting-rule point); Snow / Nightingale / Minard read for their thresholds; a menu of five threshold diagram patterns |
| Session 1 · the students' projects | Pavilion siting: a Pareto front cut by two threshold lines, and a UTCI drop vs category-crossing definition. Studio massing: three sections against a 25° daylight line and a GFA target. Two worked briefs. A "same exercise, two depths" slide for undergraduate vs PhD |
| Session 2 · swap studio | Swap ring Student 1 → Student 2 → Instructor → Student 1. Each brief is drawn three ways: **by hand (8 min), with AI (10 min), from the data (10 min)**. Compare all nine drawings (3-second test, threshold placement, visible uncertainty, invented content); defend one line in rotating client / occupant / regulator roles; write the recommendation sentence with its flip distance; four-step reconstruction; exit task |

All example numbers in the drawn diagrams are **illustrative** and labelled as such. The PM2.5 thresholds, UTCI category bounds, and Challenger flight temperatures are real, and the sources are on the slides.

### New tool · `site_tools/threshold-explorer.html`

A stand-alone page (no external libraries) using the Week 3 facade data and the same rules as `starter_kits/spreadsheet-thresholds/live_threshold_workbook.xlsx` (pass / review band at half weight / fail; candidate at 80 or more; two or more fails forces a revision).

- sliders for each threshold, plus a toggle for the review bands
- blind mode for the live "draw the line" exercise
- a flip-distance readout per criterion (how far the threshold moves before the top pick changes)
- a strip plot per criterion, a CSV download for Grasshopper, and "copy my thresholds"
- works at phone width; embedded in the deck via iframe and listed in the sidebar under Tools & Guides

Key numbers it produces (used on the slides): Hybrid 100 / Deep fins 85. Hybrid loses the top pick only if solar gain tightens by about 19% (to 38.9 or below) or facade depth tightens by about 18% (below about 0.62 m). With review bands off, High greenery drops from 55 (review) to 30 (revise).

### Theme and documentation

- `weeks_v2/arch7476.scss`: new section **15b** adds `.diagram` (inline SVG wrapper plus `.src` caption) and `.ask-room` (a single-question prompt line)
- `weeks_v2/VISUAL-LANGUAGE.md`: documents both components
- `_quarto.yml`: Threshold Explorer added to resources and the sidebar; sidebar label changed to "W9: Thresholds, Drawn"
- `schedule.qmd`: Week 9 table row and Week 9 section rewritten (before class / Session 1 / Session 2)

## Commits

| Commit | What |
|---|---|
| `982dc77` | Week 9 rebuild, Threshold Explorer, theme components, schedule, site render |
| `eaefd6d` | Swap studio sized for two students plus the instructor |
| `b45d713` | Project-specific examples (pavilion MOO, studio massing) at two depths |
| `622b888` | (instructor) Weeks 7–8 rebuild, schedule, A3, verification card, theme section 18; source was previously unpushed |
| `d31da6c` | Merge of the two lines of work; schedule conflict resolved; full re-render |

Work branch: `claude/nice-goodall-hjv9ji`, fast-forwarded into `main` at `d31da6c`.

## Publishing · what happened and the rule going forward

- The live site is served from the **`gh-pages`** branch (the built site only). `quarto publish gh-pages` builds from wherever it runs and pushes **only the HTML**.
- Before today, `gh-pages` (published 4 Nov) had newer Weeks 7–8, schedule, A3, verification card, and facade example pages than `main`; their source had not been pushed. A full publish from the repo would have rolled those pages back.
- What we did:
  1. A targeted publish of only the Week 9 files and the sidebar entry (`gh-pages` commit `52003e6`).
  2. The instructor pushed the missing source to `main` (`622b888`).
  3. Merge, full re-render, and a page-by-page text comparison against the live site: everything matched except the intended Week 9 schedule entry.
  4. Full publish of the rebuilt site (`gh-pages` commit `1cfb34e`).
- **Rule:** push source to `main` *before* publishing, and pull before publishing. Never publish from a copy that is not up to date with `main`.
- Rendering used Quarto **1.10.19**, the same version as the previous publishes.

## Open items for upcoming weeks

- [ ] **Orphan kicker slides in other decks.** The pattern `---` / `[kicker]{.kicker}` / `## Title` leaves the kicker on its own near-empty slide (Week 8 had 14 of these in the 4 Nov build). Week 9 avoids it by placing the kicker *after* the `##` heading. Check Weeks 1–8 and 10–12 and fix, or change the theme convention in `VISUAL-LANGUAGE.md`.
- [ ] **Weeks 10–12 for a class of two or three.** Same treatment as Week 9: remove volunteer / random-draw / "waiting role" logic, put the instructor in the rotation, and turn rigid lists into drawn examples with one question each.
- [ ] **Schedule "End-of-Week 9 Class Vote" section** still describes a whole-class vote. The deck replaces it with a one-line clinic / workgroup choice per student; update the schedule text to match.
- [ ] **Replace illustrative numbers with the students' real data** once they share briefs: the pavilion Pareto front (walk time × UTCI reduction per candidate site) and the massing sections (floors, GFA, daylight check).
- [ ] Optional: a pavilion / Pareto mode for the Threshold Explorer (ε-constraint sliders over the student's own site table), which would serve the PhD track in Weeks 10–11.
- [ ] A4 Object Card: carry over the Week 9 recommendation sentence with flip distance ("…this changes if [threshold] moves by [how much]…") into the A4 template and the Week 10 draft review.
