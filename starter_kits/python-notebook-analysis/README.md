---
title: "Starter Kit: Python Notebook Analysis"
format:
  html:
    toc: true
---

**Launch status:** runnable script added. Existing notebooks are still available.

## Existing Assets

- `notebooks/01_python_ml_basics.ipynb`
- `notebooks/02_arch_viz_analysis.ipynb`
- fake architecture-flavored CSV files in `data/`
- `data/facade_variants.csv`
- `facade_decision_demo.py`

## Purpose

Support repeatable analysis, visualization, and lightweight modeling for design evidence.

## Minimum Demo Loop

1. design question
2. structured input table
3. analysis or comparison
4. visualization
5. threshold or recommendation

## Demo Run

From this folder:

```bash
python3 facade_decision_demo.py
```

The script exports:

- `outputs/facade_variant_scores.csv`
- `outputs/facade_variant_tradeoff.png`

## Student Adaptation Task

Students replace the demo dataset with their own project data or scenario table.

## Grasshopper Bridge

Read `outputs/facade_variant_scores.csv` back into GH to color variants, filter candidates, or compare slider states against the same thresholds.

## Verification Checks

- notebook runs top to bottom
- units are named
- plots have interpretable labels
- uncertainty or range is shown
- output supports a design action
