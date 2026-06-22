# ARCH7476 Slide Visual Language

One theme drives every weekly deck: `arch7476.scss`. Content lives in the
`.qmd` files; the **look** lives in the theme. To restyle the whole course,
edit `arch7476.scss` only.

This file is the component dictionary. Every class below is something you can
read directly in a deck's markdown and recognise. Use these — do not invent
new classes per deck (that is the divergence we are removing).

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
[Session 2 · Round table]{.kicker}
## Audit the Evidence You Already Use
```

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

## Tone rules (non-negotiable)
- Nurturing, not competitive. **No** gladiator / arena / championship /
  battle / tournament / scoring / coronation language anywhere.
- The high-status move is naming your own weakest link first.
- Audit targets the artifact and its claim, never the person's competence.
