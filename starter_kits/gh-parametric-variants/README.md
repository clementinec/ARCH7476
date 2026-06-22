---
title: "Starter Kit: GH Parametric Variants"
format:
  html:
    toc: true
---

# GH Parametric Variants

**Launch status:** bridge notes and example metric CSV added. Native GH/Rhino files are still needed.

## Purpose

Give students a concrete generative design loop:

input geometry -> parameter variation -> multiple variants -> metric export -> threshold decision

## Required Files To Build

- Rhino base file
- Grasshopper definition
- screenshot of the GH canvas
- screenshot of variant outputs
- exported CSV of variant metrics: `outputs/facade_variant_metrics_example.csv` is currently a code-side example
- example Object Card figure

## Current Support Files

- `variant_log_template.csv`
- `outputs/facade_variant_metrics_example.csv`
- `grasshopper_bridge_notes.md`

## Demo Scenario

Facade shading or aperture variation.

Suggested variables:

- shading depth
- fin spacing
- aperture ratio
- rotation angle

Suggested outputs:

- solar exposure proxy
- daylight proxy
- view/opening ratio
- material quantity proxy

## Student Adaptation Task

Students replace the demo geometry or variable range with their own studio decision.

## Verification Checks

- units are stated
- sliders have realistic ranges
- exported values match visible variants
- at least three variants are compared
- one threshold or comparison rule is stated
