# Session 2 and Visual Language System

This file defines the reusable classroom structure and slide design language for the weekly deck rebuild.

It should be applied starting with Week 1, then repeated consistently.

## Core Weekly Structure

Every weekly deck should make the two-session format visually explicit:

```text
Session 1: Lecture / Demo
BREAK TIME
Session 2: Round Table on YOUR [evidence / tool / workflow / threshold]
Session 2 Reflection: What changed in your project logic?
```

The second session must not be vague studio time. It should include:

1. a concrete upload or drawing action
2. a round-table prompt
3. a short reflection
4. a next-step output

## Slide Visual Language

Use `weeks_v2/rebuild-slide-style.css` for future deck rebuilds.

Suggested YAML addition for rebuilt decks:

```yaml
format:
  revealjs:
    theme: simple
    css: rebuild-slide-style.css
    transition: slide
    slide-number: true
    incremental: true
    width: 1400
    height: 900
    center: true
```

## Color Roles

| Color role | Use |
|---|---|
| Blue | lecture concepts, key terms, evidence logic |
| Green | student activity, studio-lab task |
| Amber | break time, examples, anecdotes |
| Violet | reflection, synthesis, what changed |
| Red | warning, overclaim, weak evidence, risk |

## Reusable Slide Blocks

### Session 1 Header

```markdown
## Session 1: Lecture / Demo

::: {.activity-card}
**Today we learn:** ...

**Why it matters for your studio:** ...
:::
```

### Break Slide

```markdown
## BREAK TIME {.big-break}

Take 10 minutes.

When you come back, upload one image to Slack for Session 2.
```

### Session 2 Header

```markdown
## Session 2: Round Table on YOUR EVIDENCE

::: {.slack-card}
**Slack upload:** Send one image, diagram, screenshot, table, or render to the class channel.

No polished presentation needed. Upload the image and be ready to talk about it for 60-90 seconds.
:::
```

### Activity Slide

```markdown
## Studio-Lab Task

::: {.activity-card}
**Do this now:** ...

**Output before leaving:** ...
:::
```

### Reflection Slide

```markdown
## Session 2 Reflection

::: {.reflection-card}
**What changed?**

- What did today's lecture make you see differently?
- What did your project image reveal?
- What evidence is weaker than you thought?
- What is the next action before the next class?
:::
```

## Slack Visual Sharing Protocol

This should appear in Week 1 and be repeated briefly when needed.

### Why Slack

Slack lowers the friction of visual sharing.

Students do not need to prepare a formal presentation every time. They can:

- send an image
- speak briefly from the image
- receive focused critique
- keep a visible trail of project development

### Student Instruction

```text
Upload one visual to Slack before Session 2 starts.

It can be rough:
- screenshot
- render
- diagram
- table
- photo of sketch
- GIS map
- GH canvas
- spreadsheet chart

Then speak for 60-90 seconds:
1. this is the decision
2. this is the evidence I used
3. this is what I now doubt
4. this is what I need next
```

### Participation Rule

```text
Round-table discussion is part of class participation.

Volunteering to share or respond counts.
If you speak substantively, that can satisfy participation for the session.
If you do not volunteer, expect to be called during the round.
```

## Session 2 Reflection Pattern

Every Session 2 should close with a 3-5 minute reflection. It can be written in notes, Slack thread, or the assignment worksheet.

Use this pattern:

| Prompt | Purpose |
|---|---|
| What did I learn from Session 1? | connects lecture to project |
| What did I see differently in my own work? | prevents abstract listening |
| What changed in my evidence/workflow logic? | converts lecture to action |
| What is still vague? | surfaces blockers |
| What must I do before next class? | creates continuity |

## Anecdote Policy

Anecdotes are useful when they expose a hidden evidence problem.

Use anecdotes sparingly:

- one short story
- one evidence lesson
- one transfer to studio

Do not use anecdotes as entertainment or filler.

### Good Anecdote Pattern

```text
Story: A team trusted a polished simulation screenshot.
Problem: nobody could explain the assumptions.
Evidence lesson: output is not evidence unless the workflow is inspectable.
Studio transfer: your A3 must show input, variation, evaluation, threshold, and design action.
```

## Week 1 Example Insert: Vibes vs Evidence

The Week 1 deck needs a concrete slide sequence that shows how "evidence" often starts as vibes.

Suggested sequence:

1. Everyday vibe example: restaurant feels successful.
2. Product vibe example: camera ad looks convincing.
3. Architecture vibe example: public-space precedent photo looks lively.
4. AI vibe example: generated render looks plausible.
5. Studio transfer: which part of your project is still vibes?

## Tone Cleanup Policy

Some old decks contain useful activities wrapped in playful language such as:

- battle royale
- gladiator arena
- championship
- domination
- victory lap

Do not delete useful mechanics automatically. Translate the wrapper:

| Old wrapper | Keep | Replace with |
|---|---|---|
| Battle Royale | peer testing | Peer Reproducibility Check |
| Gladiator Arena | timed draft review | Draft Workflow Review |
| Championship Training | final polish stations | Final Package Clinic |
| Champion Recognition | selected strengths | Review Highlights |
| Victory Lap | synthesis | Final Reflection |

## Week 1 Minimum Rebuild Target

When Week 1 is rebuilt, it should include:

1. visually clear full-semester overview
2. A1 three-week arc
3. participation and Slack protocol
4. vibes-vs-evidence examples
5. break slide
6. Session 2 round-table on YOUR EVIDENCE
7. Session 2 reflection
8. exit task: A1 has started, not finished

