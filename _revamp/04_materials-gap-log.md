# Materials Gap Log

This log protects existing work and identifies where the rebuild needs new lecture/demo material.

## Reuse Map

| Existing source | Reuse level | Rebuild use |
|---|---:|---|
| `weeks/week-01.qmd` | High | Total Recall / evidence audit base |
| `assignments/assignment-01.qmd` | High | A1 Total Recall source material |
| `weeks/week-02.qmd` | Medium | evidence types and audit language |
| `weeks/week-03.qmd` | Medium | spreadsheet as documentation/threshold support |
| `weeks/week-04.qmd` | Medium | GIS route overview |
| `weeks/week-05.qmd` | High | move BIM/BEM early; add tool translation frame |
| `weeks/week-06.qmd` | Medium | evidence/workflow map |
| `weeks/week-07.qmd` | Medium | prototype documentation and reproducibility |
| `weeks/week-08.qmd` | Medium | uncertainty and pilot language |
| `weeks/week-08-engaging.qmd` | Low-medium | salvage documentation and AI ethics sections; reduce tone |
| `weeks/week-09.qmd` | Medium-high | thresholds, figure rescue, recommendation language |
| `weeks/week-10.qmd` | Medium | draft defense base |
| `weeks/week-10-engaging.qmd` | Low | archive as old offering; replace tone |
| `weeks/week-11.qmd` | Medium | final package workshop |
| `weeks/week-11-engaging.qmd` | Low | archive as old offering; salvage checklists only |
| `weeks/week-12.qmd` | Medium | Object Fair final prompt |
| `weeks/week-12-engaging.qmd` | Low | archive as old offering; reduce championship language |
| `lectures/ml-to-python-overview.qmd` | Medium | optional Python/ML route |
| `notebooks/01_python_ml_basics.ipynb` | Medium | optional code-heavy support |
| `notebooks/02_arch_viz_analysis.ipynb` | High | figure/object-card workflow support |
| `assets/DCP_7476_Draft_HGuo.docx` | High | policy anchor |
| `assets/ARCH7476_HONGSHAN GUO.pdf` | High | original promise/opening deck |

## Gaps To Build

| Priority | Gap | Needed artifact | Suggested owner action |
|---:|---|---|---|
| 1 | Total Recall board | A1 worksheet/template | Create one-page PDF/slide template |
| 1 | Tool translation matrix | Week 2 worksheet | Build matrix comparing BIM/BEM/GH/GIS/Python/AI for one decision |
| 1 | GH starter workflow | Week 3 demo files | Build 2-3 simple GH definitions with screenshots |
| 1 | AI-assisted GH/Python verification | Week 8 handout | Build prompt log + failure/verification checklist |
| 1 | A4 branch declaration | Week 6 worksheet | Build route A/B declaration form |
| 2 | Preset simulation demo | Week 5 demo | Build one VELUX/Radiance/EnergyPlus Simple Glazing example |
| 2 | Workflow prototype examples | Week 7 examples | Build one example per supported route |
| 2 | Threshold examples | Week 9 handout | Build adopt/defer examples from facade/site/daylight/circulation |
| 2 | Final package templates | Week 11 package | Build Practice Case, Research Brief, Object Card, Capsule templates |
| 3 | Mentor dialogue guide | Week 8/9 handout | Build email/script + report template |
| 3 | Undergrad scaffold | All assignments | Build "minimum viable" version of each deliverable |

## Supported Workflow Tracks: Recommendation

Do not support too many fully. The course can mention many tools, but should officially support a smaller set.

Recommended supported tracks:

| Track | Current support level | Launch support target | Why |
|---|---|---|---|
| GH parametric workflow | Not yet supported | Full | central to generative design expectation |
| GH + Ladybug/Honeybee or preset daylight/solar | Not yet supported | Full or partial | strong architecture fit; needs demo materials |
| GIS workflow | Partial | Partial | useful for site projects; existing material available |
| Python notebook workflow | Partial | Partial | existing notebooks available; not all students expected to code |
| AI-assisted GH/Python workflow | Not yet supported | Method overlay | responds to vibe coding idea while requiring verification |
| Spreadsheet workflow | Baseline | Baseline | useful for thresholds, sensitivity, and reproducibility |

## Lecture Sufficiency Audit

| Week | Current material enough for first 50? | What is missing |
|---|---|---|
| 1 | Yes with edits | Total Recall template and strong worked example |
| 2 | Partial | new tool translation frame and project matrix |
| 3 | No | GH live demo and starter definitions |
| 4 | Mostly | tighten evidence ranges around student project decisions |
| 5 | No | preset simulation/proxy test handout and demo |
| 6 | Partial | A4 branch declaration and workflow scope examples |
| 7 | Partial | route-specific prototype examples |
| 8 | No | AI/vibe coding examples and verification checklist |
| 9 | Partial | stronger numeric threshold cases |
| 10 | Partial | professional review deck replacing tournament tone |
| 11 | Partial | DCP-aligned final package templates |
| 12 | Yes with tone edits | final reflection prompts |

## Second-Half Studio-Lab Prompt Bank

These prompts can be reused whenever a student says the weekly lens does not apply.

### Universal Fallback

- Why does this lens not apply to your decision?
- What evidence type is more relevant instead?
- What would a critic ask you to prove?
- What variable could still be named?
- What output would help someone make the decision?
- What is the smallest workflow that could produce that output?

### Evidence Prompts

- What evidence is strongest?
- What evidence is weakest but visually persuasive?
- What evidence is missing because it is hard to collect?
- What would count as enough evidence for this decision?
- What uncertainty should be shown rather than hidden?

### Workflow Prompts

- What is the input?
- What is the operation?
- What is the output?
- What is the quality check?
- What breaks if someone else reruns it?
- What part is judgment rather than computation?

### Studio Decision Prompts

- What design action follows from the output?
- What would make you reject the current option?
- What would make you narrow the parameter range?
- What would make you ask for more evidence?
- What stakeholder would disagree with your interpretation?

### Share-Out Prompts

- Show the decision in one image.
- Name the evidence in one sentence.
- Show the workflow in three boxes.
- State the threshold in one sentence.
- Name the limit you do not want to hide.
