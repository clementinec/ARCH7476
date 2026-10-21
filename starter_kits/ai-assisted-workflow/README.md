---
title: "Starter Kit: AI-Assisted Fact-Checking + Workflow Support"
format:
  html:
    toc: true
---

**Launch status:** prompt log and verified function example added.

## Purpose

Show students how AI can help fact-check, explore fuzzy relationships, or draft a small workflow component without becoming unverified evidence.

## Files

- `examples/prompt_log_example.md`
- `examples/verified_setback_score.py`

## Candidate Extensions

Before launch, optionally add one of:

- AI-generated GH Python component
- AI-assisted Python notebook function
- AI-generated workflow documentation
- failed AI output repaired through fact-checking or manual verification

## Minimum Demo Loop

1. task prompt
2. output type: fact-based, relationship-based, or workflow/code
3. generated output
4. failure or risk
5. fact-check, relationship check, or manual calculation
6. corrected workflow component or checked claim
7. reproducibility note
8. disclosure statement

## Student Adaptation Task

Students use AI for one bounded fact-checking, relationship-exploration, or workflow task, then show the final gate that made it trustworthy enough to use.

## Grasshopper Bridge

The verified setback function is intentionally small enough to paste into GhPython. That makes the teaching point clear: AI can help draft a component, but the student must still test units, thresholds, known cases, and the claim being made.

## Verification Checks

- code or component runs
- factual claims are traced to sources where relevant
- relationship claims are checked against a calculation, precedent mechanism, empirical source, or sensitivity test
- units and scale are correct
- output is compared against a manual or known result
- AI role is disclosed
- design judgment remains with the student
