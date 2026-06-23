---
title: "Starter Kit: Spreadsheet Thresholds"
format:
  html:
    toc: true
---

**Launch status:** baseline support. Live workbook, browser preview, filled matrix, and GH-facing score export are present.

## Purpose

Provide the low-code floor for comparison, sensitivity, and threshold logic.

## Minimum Demo Loop

1. alternatives or variants
2. criteria
3. source values or ranges
4. comparison table
5. threshold
6. recommendation

## Files

- `decision_matrix_template.csv` — blank structure for student use
- `decision_matrix_filled_example.csv` — filled facade decision example
- `variant_scores.csv` — summary export that can be read back into GH by variant name
- `live_threshold_workbook.xlsx` — live Excel demo with editable thresholds, formulas, color rules, and score chart
- `live_threshold_workbook_preview.html` — browser preview embedded in the Week 3 deck
- `build_live_threshold_workbook.py` — repeatable builder for the Excel workbook

## Student Adaptation Task

Students create a transparent comparison table for their variants or evidence sources.

## Live Demo

Open `live_threshold_workbook.xlsx`, go to the `Criteria` sheet, and change the yellow threshold cells. The `Decision_Matrix` sheet updates pass/review/fail status with color, and `Variant_Scores` updates the compact table and score chart.

The richer version uses five criteria across five facade variants. It also includes a `Score_Rules` sheet, so the class can change what counts as a candidate and see the recommendation shift.

## Grasshopper Bridge

Students can export GH slider values and calculated metrics to CSV, then use the same threshold table to decide whether a variant is a candidate, a revision, or an exception that needs stronger evidence.

For the Week 3 bridge demo, `decision_matrix_filled_example.csv` is the auditable long table and `variant_scores.csv` is the compact output table for Grasshopper: variant name, pass/review/fail counts, score, status, and action.

## Verification Checks

- units are named
- formulas are visible
- color coding has a legend
- threshold is explicit
- recommendation follows the table
