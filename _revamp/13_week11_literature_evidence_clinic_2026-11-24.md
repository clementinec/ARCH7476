# Week 11 · Own-project literature evidence clinic · 24 November 2026

## Teaching change

Rebuilt `weeks_v2/week-11.qmd` as 28 content slides plus the title. Every student brings one consequential claim from their own research or studio project, records their abstract-based interpretation, inspects the paper's relevant methods/results/limitations, and explains the consequence for the project. Retaining a supported claim and recording unverified support are valid outcomes. Full text enables appraisal; it does not automatically establish quality or transferability.

All four students (two PhD, two undergraduate) undertake the same task. Session 1 is 8 minutes of brainstorming, 10 minutes of four project pitches, a 10-minute tools demonstration, and a 22-minute source comparison. Session 2 is four four-minute clinics, 20 minutes of revision, eight minutes of pair rechecks, and six minutes saving the A4 record.

Added `templates/evidence-clinic-card.qmd` with the before/after record, source locators, project consequence, next test and peer recheck. Added the optional standalone `site_tools/regex-lab.html`, with four authored pattern demonstrations, explicit false-positive/false-negative discussion, and no external dependencies. Search operators, regex, RIS export and OpenAlex are supporting tools. PRISMA is an optional extension, not the session's completion claim.

The shared real case is Mora & Bardhan (2025), DOI 10.1098/rsos.241337, using the readable PMC HTML article. The course application is labelled as a teaching interpretation; sampling and operating-condition details come from full-text sections 3.1.3 and 4.4. Primary documentation was checked for Google search operators, JavaScript regex, ScienceDirect RIS export, OpenAlex authentication/lookup/search/abstract fields, and PRISMA reporting. OpenAlex key setup is optional and must not delay the reading task.

Updated only the Week 11 schedule section and A4 check-in row. The deck now names all six existing A4 components, including the Feedback + Revision Ledger and Reflection Note, and preserves the runnable capsule requirement. No change to assessment weights, deadlines or grading. The existing landing-page/sidebar pointer already resolves to `weeks_v2/week-11.html`.

## Validation

- Started from current `main` / `origin/main` at `af74746`; fetched again before committing.
- Independent content reviews confirmed the latest user framing, four-student participation, 50 + 50 minute schedule, primary-source distinctions and A4 consistency.
- Rendered the deck, card, schedule and A4 brief with Quarto 1.10.19. The standalone tool is copied by the project resource configuration.
- Parsed the rendered HTML: 29 slides including title, a heading on every content slide, unique slide IDs, consistent table cell counts, exact rendered regex strings, local links and fragments resolving, and matching source/published Regex Lab bytes.
- Removed 20 obsolete search-index anchors from the updated pages after partial rendering; confirmed every unrelated search record remained unchanged.
- Regex Lab JavaScript syntax checked. The authoring review exercised presets, invalid patterns, zero-length Unicode advancement and capped result rendering. User patterns run in a worker with a timeout.
- `git diff --check` passed.
- Fresh visual review remains unavailable: the computer-use browser host was unavailable and an isolated headless Edge attempt aborted (exit 134) before producing a screenshot. No claim of screenshot-based layout verification.

## Publication

Source was pushed to `main` before deployment. Published only the six changed `docs/` files over the latest `gh-pages` tree, preserving all other published files.

- Source commit: `f16dbf7713caf2489e361e2f37f39e9b37772061`.
- Deployment commit: `2e370364f283867f7ef32a0da17c062c1b243d51`, parent `be8e9072d2ac8f4ad9dd5ec50ef3343467e912d4`.
- Each uploaded file's Git blob hash matched its local rendered file. A recursive tree comparison confirmed exactly six changed paths and 227 other published files preserved.
- GitHub Pages run [45301095983](https://github.com/clementinec/ARCH7476/actions/runs/45301095983) completed successfully for the deployment commit.
- The web reader could not access the public deck URL after deployment. Deployment and published-file hashes are verified; a live browser inspection is not claimed.
- Published deck: <https://clementinec.github.io/ARCH7476/weeks_v2/week-11.html>.
- Published card: <https://clementinec.github.io/ARCH7476/templates/evidence-clinic-card.html>.
- Published optional lab: <https://clementinec.github.io/ARCH7476/site_tools/regex-lab.html>.
