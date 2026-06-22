---
title: "AI Prompt Log Example"
---

# AI Prompt Log Example

## Bounded Task

Draft a small Python function that scores whether a proposed building setback satisfies a 3.0 m minimum.

## Prompt Used

Write a Python function called `setback_clearance_score`. It should take `setback_m` and `required_m`, return whether the proposed setback passes, return the ratio, and give a short status label. Keep the function simple enough to paste into a Grasshopper Python component.

## AI Output Risk

The first draft returned only `True` or `False`. That was too thin for design discussion because it hid near misses and drawing tolerance.

## Manual Verification

Known checks:

- 3.0 m against a 3.0 m rule should pass.
- 2.4 m against a 3.0 m rule should fail.
- 3.75 m against a 3.0 m rule should be comfortably above the requirement.

## Corrected Component

See `verified_setback_score.py`.

## Disclosure Statement

AI helped draft a bounded scoring function. The logic was manually checked against simple known cases before it was used as project evidence.
