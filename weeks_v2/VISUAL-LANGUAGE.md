# ARCH7476 Slide Visual Language

One theme drives every weekly deck: `arch7476.scss`. Content lives in the
`.qmd` files; the **look** lives in the theme. To restyle the whole course,
edit `arch7476.scss` only.

This file is the component dictionary. Every class below is something you can
read directly in a deck's markdown and recognise. Use these shared classes.
When a new teaching layout is needed, add a reusable component to
`arch7476.scss` and document it here; avoid per-deck styles and inline layout
rules. New components are opt-in so existing decks retain their appearance.

## Deck front matter (use verbatim)

```yaml
format:
  revealjs:
    theme: [default, arch7476.scss]
    transition: slide
    slide-number: true
    incremental: true
    width: 1400
    height: 900
    center: false          # Swiss = top-left aligned, not vertically centred
    footer: "Week N · feeds A_"
```

## Colour roles (meaning, not decoration)

| Role | Token | Used for |
|---|---|---|
| Concept | `--role-concept` (blue) | lecture concept, key term, evidence logic |
| Activity | `--role-activity` (green) | "do this now", studio-lab task, walk-through |
| Example | `--role-example` (amber) | example, anecdote, break |
| Reflect | `--role-reflect` (violet) | reflection, synthesis, what changed |
| Warn | `--role-warn` (red) | overclaim, weak evidence, risk |
| Signal | `--signal` (vermilion) | the one accent: links, current state, emphasis |

## Components

### Kicker + title (Swiss header)
```markdown
## Audit the Evidence You Already Use

[Session 2 · Round table]{.kicker}
```

Keep the slide heading before the kicker in Quarto source. A kicker between a
slide separator and the next heading can become a separate, almost-empty slide.

### Labels (chips)
`[Session 1]{.label .concept}` · `.activity` · `.example` · `.reflect` · `.warn`

### Cards (left-ruled panels)
`.concept-card` `.activity-card` `.example-card` `.reflection-card`
`.warning-card` `.slack-card`. First bolded line may use `[…]{.card-title}`.

```markdown
::: {.activity-card}
[Do this now]{.card-title}
Mark evidence, precedent, assumption, and uncertainty on your image.
:::
```

### The four-step reconstruction — `.recall-4step`
The course's recurring engine. **Same four prompts every week; only the
OBJECT changes** (past decision → tool/route → prototype → package). Always
state the object in the lead-in line.

**IMPORTANT:** every `:::` marker must be on its OWN line. A one-line
`::: {.step}text :::` does NOT parse as a div — it leaks as literal text.

```markdown
**Reconstruct your [BIM/BEM screenshot]:**

::: {.recall-4step}
::: {.step}
**Did** the real steps you took, in order
:::
::: {.step}
**Assumed** the hidden inputs at each step
:::
::: {.step}
**Risk** where you did not check / could break
:::
::: {.step}
**Verify** what you would check if you did it again
:::
:::
```

### Spine rail — `.spine-rail`
Persistent logic. Mark the live node with `.is-current`.
Nodes: Decision · Evidence · Variation · Output · Threshold · Action.

```markdown
::: {.spine-rail}
[Decision]{.node} [Evidence]{.node .is-current} [Variation]{.node} [Output]{.node} [Threshold]{.node} [Action]{.node}
:::
```

### Tool / instrument panel — `.tool-panel`
The "show a tool running" frame. Four zones. Use it only when the slide names
a runnable contract, export target, or verification target.

```markdown
::: {.tool-panel}
::: {.zone .input}
**Input** site polygon + transit layer
:::
::: {.zone .operation}
**What varies** buffer distance 200–600 m
:::
::: {.zone .output}
**Output** access-coverage % per option
:::
::: {.zone .check}
**Quality check** CRS stated, counts spot-checked
:::
:::
```

### Session 2 modes — `.walkthrough-card` vs `.audit-card`
Two distinct modes. **Walk-through** = celebrated, opt-in, "teach your
strongest tool". **Audit** = universal, reciprocal, examine the work not the
person. Keep them visually and sequentially separate (teach first, then audit).

### Small parts
- `::: {.source-note} … :::` — a compact source/date line below the main content; use direct primary-source links and keep the teaching point in the body.
- `[feeds A2]{.feeds-tag}` — links Session 2 work to its assignment.
- `::: {.grading-note} … :::` — how the week's participation is graded.
- `## BREAK {.big-break}` — full-bleed dark break moment.

### Progress & flow components (multi-class — mind the dots)

**Every extra class needs its own dot.** Write `{.step .done}`, never
`{.step done}` — pandoc silently drops a bare word, so the state class never
applies and the component looks orphaned.

- `.progress-ladder` with `.step`, `.step .done`, `.step .current` — the
  semester-progress strip at the top of a deck.
- `.artifact-strip` with `.artifact` — what this week takes in / changes / outputs.
- `.tool-ledger` with `.slot .core` / `.slot .peer` / `.slot .explore` — the
  three Session-2 roster lanes.
- `.bridge-flow` with `.node`, `.node .current` — a small left-to-right flow.
  Note: this uses `.current`, while `.spine-rail` uses `.is-current`.

### Section dividers — `.section-slide`

Use a dark divider to mark a change in teaching mode. Include a numbered
stage and one sentence explaining its purpose. The same class can be applied
to the title slide through `title-slide-attributes: {class: section-slide}`.
Content follows normal document flow; these components do not clip overflow
or use a fixed height to force content onto a slide.

```markdown
## Explain your A2 {.section-slide background-color="#2F6F5E"}

[02]{.section-number}

[Use feedback to choose the next test of your workflow.]{.section-lead}
```

### Process — `.process-chain` and `.process-step`

Three or four equal-weight stages automatically share the available width.
Use the existing `.label` role classes, then a bold heading in its own
paragraph, then one short explanation. Number the stages in the labels when
order matters. Keep the same terms when the process returns later.

```markdown
:::: {.process-chain}
::: {.process-step}
[01 · Start]{.label .concept}

**A2 proposal**

Name the decision and the workflow you selected.
:::
::: {.process-step}
[02 · Test]{.label .activity}

**One small run**

Change one input and record the output.
:::
::: {.process-step}
[03 · Record]{.label .reflect}

**Project page**

Show the result, its check, and the next test.
:::
::::
```

### A single takeaway — `.takeaway`

Place one short explanatory sentence beneath a visual or example. This is
larger text with the signal-coloured rule; it should explain the implication
of what the student just saw.

```markdown
::: {.takeaway}
This test tells us whether changing the shading depth changes the output.
:::
```

### Staged practical notes — `.practice-note`

Connect a mechanism to a consequence and an action. Show the main diagram or
explanation first, then reveal **Why it matters** and **Do this** on two advances.
Use this in place of the slide's takeaway, keeping the note short and specific to
the student's task. It stays in normal flow; reduced-motion users get the staged
reveal without movement, and both rows are visible when printed.

```markdown
:::: {.practice-note .fragment .fade-up data-fragment-index="0"}
**Why it matters:** the supplied project context shapes the comparison.

::: {.fragment .fade-up data-fragment-index="1"}
**Do this:** provide scale, orientation and relevant constraints with the plan.
:::
::::
```

### Activity instructions — `.task-meta`, `.task-steps`, `.task-output`

State the duration, group size, and starting material in `.task-meta`.
Use a numbered list in `.task-steps` and a concrete completion condition in
`.task-output`. The list class works on an `ol` or a wrapper around it.
Keep instructions visible together with `.nonincremental`. Split long
instructions across explicitly numbered slides instead of shrinking text.

```markdown
::: {.task-meta}
6 minutes each · groups of three · open your submitted A2
:::

::: {.task-steps .nonincremental}
1. Explain the decision and chosen workflow for three minutes.
2. Listen to feedback for two minutes.
3. Record one next test for one minute.
:::

::: {.task-output}
**Done:** each student has one written next test in their project notes.
:::
```

### Work status — `.status-tag`

Use a text label as well as colour. These describe the state of the work,
not a grade or a general claim of scientific validity.

- `[Planned]{.status-tag .status-planned}` — the run has not happened yet.
- `[Output saved]{.status-tag .status-tested}` — a run produced an output;
  show it and state whether its check passed, failed, or is pending.
- `[Attempted · blocked]{.status-tag .status-blocked}` — an attempted step failed;
  show the failing step, error, and next repair.

### A project-page example — `.example-sheet` and `.page-line`

Use `.example-sheet` for a readable example of what students should write.
Begin with a label naming the example. Each `.page-line` contains two child
divs: the section name and its content. This keeps labels and content aligned
even when the content includes links. Use three to five short rows per slide.

```markdown
::::: {.example-sheet}
[Project page · example]{.label .example}

:::: {.page-line}
::: {}
**Decision**
:::
::: {}
Choose a shading depth for the west facade.
:::
::::

:::: {.page-line}
::: {}
**Next test**
:::
::: {}
Compare the output at 0.5 m and 1.0 m with all other inputs fixed.
:::
::::
:::::
```

## Tone rules (non-negotiable)
- Nurturing, not competitive. **No** gladiator / arena / championship /
  battle / tournament / scoring / coronation language anywhere.
- The high-status move is naming your own weakest link first.
- Audit targets the artifact and its claim, never the person's competence.
