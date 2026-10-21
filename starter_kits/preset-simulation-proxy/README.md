---
title: "Starter Kit: Preset Simulation / Proxy Test"
format:
  html:
    toc: true
---

**Launch status:** runnable proxy demo plus optional EnergyPlus two-week CLI case.

## Purpose

Provide runnable Week 5 examples that test a design claim without requiring a full custom simulation model.

## Week 5 Demo Routes

| Route | Setup | Use in class |
|---|---|---|
| Proxy heat test | Python only | guaranteed fallback for everyone |
| EnergyPlus two-week case | EnergyPlus installed locally | optional real-simulator CLI demonstration |

## Proxy Route

- `data/facade_scenarios.csv`
- `facade_heat_proxy_demo.py`

From this folder:

```bash
python3 facade_heat_proxy_demo.py
```

The script exports:

- `outputs/facade_heat_proxy_scores.csv`
- `outputs/facade_heat_proxy_chart.png`

## EnergyPlus Two-Week Case

Use this route after EnergyPlus is installed:

```bash
python run_energyplus_two_week_case.py
```

See the [EnergyPlus two-week case](energyplus_two_week_case.md) for installation notes, macOS/Windows path examples, the raw CLI command, and the expected output structure. The EnergyPlus route runs outside GH first so students can inspect the model, weather, setpoints, and outputs before adding a translation layer.

![EnergyPlus two-week control check](outputs/energyplus_two_week/monitored_outputs.png){.resource-preview-image}

Checked outputs:

- [monitored output CSV](outputs/energyplus_two_week/monitored_outputs.csv)
- [run summary](outputs/energyplus_two_week/two_week_summary.txt)

## Optional Extensions

- GH + Ladybug solar/shading comparison
- VELUX or Radiance daylight preset
- EnergyPlus envelope or glazing scenario comparison using a student-owned model

## Minimum Demo Loop

1. claim
2. variable/range
3. preset, proxy, or EnergyPlus CLI test
4. output
5. uncertainty note
6. adopt/defer threshold

## Student Adaptation Task

Students define the smallest test that can reduce uncertainty around their design decision.

## Grasshopper Bridge

Students can generate the scenario table from GH sliders, run the proxy or EnergyPlus check, then bring the scored CSV back into GH for variant filtering. The important point is that the assumptions, setpoints, and outputs remain visible and debatable before the workflow becomes a GH component chain.

## Verification Checks

- assumptions are visible
- input range is plausible
- output is interpretable
- no black-box "simulation proves it" language
- result is tied to a design action
