---
title: "Grasshopper Bridge Notes"
---

## Minimal Component Map

| Workflow part | GH/Rhino equivalent | Export target |
|---|---|---|
| Variant name | Panel or slider label | `variant` |
| Window-to-wall ratio | Area window / area facade | `wwr` |
| Shading depth | Number Slider in meters | `shading_depth_m` |
| Fin spacing | Number Slider in meters | `fin_spacing_m` |
| View score | visible opening area / target opening area | `view_score` |
| CSV export | Panel -> Stream Contents, TT Toolbox, LunchBox, or Elefront | `facade_variant_metrics_example.csv` |

## Why This Matters

Grasshopper components are packed functions. The point is not to abandon GH; it is to make each component's input, operation, output, and assumption visible enough that a student can eventually rewrite or debug the logic.

## In-Class Check

Before a variant table becomes evidence, ask:

- Do the sliders use plausible architectural ranges?
- Does the exported CSV match the visible variants on screen?
- Which metric is a proxy rather than a measured result?
- What design decision would change if the threshold changed by 10 percent?
