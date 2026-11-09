---
title: "Template: AI-Assisted Fact-Checking Card"
format:
  html:
    toc: true
---

Use this template whenever AI assists a factual claim, relationship interpretation, workflow, script, GH component, analysis step, figure text, or documentation.

For the Week 8 lab, audit one bounded architectural decision. If your chosen step did not use AI, write **“AI not used”** and complete the decision, input/output, verification, judgment, and reproducibility sections. No new account or paid model is required.

## Task And AI Role

- What architectural decision does this step affect?
- What did you ask AI to do?
- Why was AI useful here: fact-checking, relationship exploration, code/workflow drafting, writing structure, or debugging?
- What tool and model name were visible in the interface? Record the mode/setting and date used; write **unknown** where the interface does not disclose them.
- What exact material did you give it?
- Where are the saved inputs, prompt/output transcript, and any tool results it used? Record file locations or links; keep non-shareable material in the permitted course location.

## Output Type

| Type | Applies? | Required check |
|---|---|---|
| Fact-based reiteration | yes / no | verify against cited source, standard, datasheet, or primary reference |
| Relationship hypothesis / interpretation | yes / no | compare against engineering/science logic, empirical evidence, sensitivity test, or bounded calculation; text generation does not itself validate building performance or user experience |
| Workflow/code component | yes / no | run it, test known cases, inspect units/ranges, and check edge cases |
| Writing/structure support | yes / no | verify claims, sources, and tone; do not treat phrasing as evidence |

## Prompt Log

| Step | Prompt summary | Output summary | Accept / revise / reject / pending |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Generated Output

- File/component/text produced:
- Where it appears in the workflow:
- What it affects:

## Verification / Final Gate

Choose one check small enough to perform. State the expected result **before** testing. A model repeating or approving its own answer is not an independent check.

| Check attempted | Expected result and basis | Observed result or blocker | Status |
|---|---|---|---|
|  |  |  | passed / failed / pending |

| Check | How you checked | Result |
|---|---|---|
| factual source check |  | pass / fail / pending / not applicable |
| relationship or mechanism check |  | pass / fail / pending / not applicable |
| syntax / execution |  | pass / fail / pending / not applicable |
| units / scale |  | pass / fail / pending / not applicable |
| output plausibility |  | pass / fail / pending / not applicable |
| comparison with manual result or known case |  | pass / fail / pending / not applicable |

## Judgment And Design Consequence

- Decision: **accept / revise / reject / pending** — and why?
- Revised or qualified claim/component, or the claim you have withdrawn:
- What changes in the architectural decision as a result?
- What remains unchecked, and what must happen before you rely on it?
- Date, peer feedback used, and next action:
- Saved artifact and dated project-page/local-entry location (website publication is optional):

## Reproducibility Note

- Can the same prompt and inputs reproduce the exact output? yes / no / uncertain
- If not, what stable artifact did you save: generated code, transcript, table, image, or checked result?
- What should a reader trust: the AI output itself, or your checked version?

## Failure Log

- What was wrong in the AI output?
- What did you change?
- What remains untrusted or only partially checked?

## Disclosure Statement

> AI assisted with [task]. I treated it as [fact-based / relationship-hypothesis / workflow-drafting] support. I checked it by [method], with [result]. I [accepted / revised / rejected / left pending] the output because [reason]. I do not rely on AI for [unsupported claim or judgment].
