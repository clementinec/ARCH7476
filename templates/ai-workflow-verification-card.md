---
title: "Template: AI-Assisted Fact-Checking Card"
format:
  html:
    toc: true
---

Use this template whenever AI assists a factual claim, relationship interpretation, workflow, script, GH component, analysis step, figure text, or documentation.

## Task And AI Role

- What did you ask AI to do?
- Why was AI useful here: fact-checking, relationship exploration, code/workflow drafting, writing structure, or debugging?
- What tool/model did you use?
- What exact material did you give it?

## Output Type

| Type | Mark one | Required check |
|---|---|---|
| Fact-based reiteration | yes / no | verify against cited source, standard, datasheet, or primary reference |
| Relationship-based simulation | yes / no | compare against engineering/science logic, empirical evidence, sensitivity test, or bounded calculation |
| Workflow/code component | yes / no | run it, test known cases, inspect units/ranges, and check edge cases |
| Writing/structure support | yes / no | verify claims, sources, and tone; do not treat phrasing as evidence |

## Prompt Log

| Step | Prompt summary | Output summary | Accepted / rejected / revised |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Generated Output

- File/component/text produced:
- Where it appears in the workflow:
- What it affects:

## Verification / Final Gate

| Check | How you checked | Result |
|---|---|---|
| factual source check |  | pass / fail / not applicable |
| relationship or mechanism check |  | pass / fail / not applicable |
| syntax / execution |  | pass / fail / not applicable |
| units / scale |  | pass / fail / not applicable |
| output plausibility |  | pass / fail / not applicable |
| comparison with manual result or known case |  | pass / fail / not applicable |

## Reproducibility Note

- Can the same prompt and inputs reproduce the exact output? yes / no / uncertain
- If not, what stable artifact did you save: generated code, transcript, table, image, or checked result?
- What should a reader trust: the AI output itself, or your checked version?

## Failure Log

- What was wrong in the AI output?
- What did you change?
- What remains untrusted or only partially checked?

## Disclosure Statement

> AI assisted with [task]. I treated it as [fact-based / relationship-based / workflow-drafting] support. I checked it by [method]. I do not rely on AI for [unsupported claim or judgment].
