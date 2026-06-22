---
title: "Starter Kit: Preset Simulation / Proxy Test"
format:
  html:
    toc: true
---

# Preset Simulation / Proxy Test

**Launch status:** runnable proxy demo added. Still needs an optional Ladybug/Radiance walkthrough.

## Purpose

Provide a runnable Week 5 example that tests a design claim without requiring a full custom simulation model.

## Current Demo Route

- `data/facade_scenarios.csv`
- `facade_heat_proxy_demo.py`

From this folder:

```bash
python3 facade_heat_proxy_demo.py
```

The script exports:

- `outputs/facade_heat_proxy_scores.csv`
- `outputs/facade_heat_proxy_chart.png`

## Candidate Extensions

Choose one before launch if deeper tooling is needed:

- GH + Ladybug solar/shading comparison
- VELUX or Radiance daylight preset
- EnergyPlus Simple Glazing scenario comparison
- spreadsheet-based proxy test for heat, light, or access logic

## Minimum Demo Loop

1. claim
2. variable/range
3. preset or proxy test
4. output
5. uncertainty note
6. adopt/defer threshold

## Student Adaptation Task

Students define the smallest test that can reduce uncertainty around their design decision.

## Grasshopper Bridge

Students can generate the scenario table from GH sliders, run the proxy, then bring the scored CSV back into GH for variant filtering. The important point is that the coefficients remain visible and debatable.

## Verification Checks

- assumptions are visible
- input range is plausible
- output is interpretable
- no black-box "simulation proves it" language
- result is tied to a design action
