# Weeks 11–12 · Plain decks, regex/OpenAlex, final package, LLM judge · 25 November 2026

## Teaching change

Rebuilt `weeks_v2/week-11.qmd` and `weeks_v2/week-12.qmd` in a plain native-Quarto
style modelled on the later CCGL9065 decks: `theme: simple` plus a small
`weeks_v2/plain.css` (big text, one emphasised line, timer chip, dark section
breaks, fragments for reveals). The shared `arch7476.scss` is unchanged, so
Weeks 1–10 are unaffected.

Week 11 (2 × 50 min, 42 slides):

- Session 1: Week 10 feedback receipt check (2½ min each; the Week 10 reviewer
  confirms); abstract-only claim written before any tools; regex from zero
  (not covered earlier in the course) with predict-then-reveal examples and a
  Regex Lab exercise; OpenAlex as its own section (DOI lookup, `oa_url`,
  references, `cites:` filter) with a real record retrieved 25 Nov 2026;
  Mora & Bardhan (2025) worked example with Figs. 2 and 7 (CC BY 4.0).
- Session 2: full-text reading and Before · Found · After; four 3-minute
  clinics; final package walkthrough; fix one thing and log it; Week 12
  preview.
- Removed the self-contradictory "LLM reads only abstracts" slide and most
  defensive hedging.

Week 12 (2 × 50 min, 20 slides): 4-minute quick-fire; an LLM critiques each
Object Card (pre-generated, plus one live run); the room labels each criticism
Grounded / Off-target / Invented; the author rules accept/adapt/defer/reject;
judge-vs-room debrief; final fixes with two ledger entries (room + AI check);
transfer round table; submission check. The LLM gives no scores and has no
effect on marks; students consent beforehand and can opt out.

New: `templates/evidence-clinic-worksheet.qmd` (2-page PDF),
`templates/llm-judge.qmd` (prompt and ground rules),
`templates/judge-scorecard.qmd` (1-page PDF). Regex Lab gained a
"numbers with units" preset. `templates/final-package-checklist.md` gained an
Evidence Trace section, and its threshold items accept a stated qualitative
criterion; the capsule rerun requirement is unchanged. Schedule Weeks 11–12
and the A4 check-in rows for Weeks 11–12 were updated. The 8-item "full loop"
list under Week 11 in the schedule was removed as a duplicate of the A4 brief.
A4 components, weights and deadline are unchanged.

## Validation

- Mora & Bardhan §3.1.3 (five buildings per cluster, 25 total) and §4.4
  (thermostat settings and occupancy schedule unknown) re-checked against the
  PMC full text. Figure files matched to figure numbers from the PMC page; the
  Fig. 7 slide describes panels (a)–(d) from the authors' caption.
- OpenAlex values (W4406352916, gold OA, `oa_url`, cited_by 2, references 33,
  two citing works) retrieved 25 Nov 2026 without a key. Citing works are
  described by title only.
- Every regex shown on slides and in the new preset was run in Node.
- Quarto 1.10.19 rendered both decks, the three new templates, checklist,
  schedule and A4 brief. Local links in all changed pages resolve.
- Headless Edge screenshots of 14 representative slides and rasterised PDFs
  were inspected; fixed a pipe escape in the cheat sheet, timer-link contrast,
  and scorecard layout.
- Removed 44 stale search-index anchors from changed pages; the 581 records
  for other pages are identical to the previous commit.
- `git diff --check` passed.

## Follow-up: why, where, and PRISMA

- Added "Why a literature check, and why now?" (links the Week 2 evidence
  audit to A4's input-source requirement, the 20% evidence-quality criterion
  and the overclaiming failure mode) and "Where today sits in your workflow"
  (find → read → check → record; Weeks 2, 8, 10, 11, 12).
- Added "Where you'll actually use it" for regex (capsule filenames, values in
  a paper, a Sheets column, a PhD literature export) and a when-to-use note
  for OpenAlex. Every pattern was run in Node; the Sheets pattern has no
  capture group, so REGEXEXTRACT returns the whole number.
- Added two PRISMA slides: PRISMA 2020 (27-item checklist, flow diagram) and
  "Today's trail is the first box": 33 references + 2 citing works = 35
  records identified by citation searching; screening and inclusion are shown
  as not done.
- Session 1 re-timed (0–3 why, 3–13 feedback, 13–17 claim, 17–31 regex,
  31–44 OpenAlex + PRISMA, 44–50 worked example); schedule updated to match.
- Diagrams are CSS step boxes rather than Mermaid, which rendered too small.
  Screenshots of the new slides checked.
