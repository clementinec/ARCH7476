---
title: "Starter Kit: GIS Spatial Comparison"
format:
  html:
    toc: true
---

**Launch status:** runnable HKU micro-walkability GeoJSON demo and hosted preview added.

## Purpose

Support site, access, zoning, exposure, and context decisions.

## Minimum Demo Loop

1. candidate sites or design zones
2. spatial layer
3. buffer, overlay, join, or clip
4. map or summary table
5. decision comparison

## Files

- `data/candidate_sites.geojson`
- `data/transit_stops.geojson`
- `data/grocery_points.geojson` — synthetic grocery/convenience points for proximity testing
- `data/noise_corridors.geojson`
- `data/green_spaces.geojson`
- `gis_spatial_comparison_demo.py`
- `outputs/gis_spatial_comparison_preview.html`
- `outputs/gis_site_comparison_map.png`
- `outputs/scored_sites.csv`
- `outputs/selected_site.geojson`

## Demo Run

From this folder:

```bash
python3 gis_spatial_comparison_demo.py
```

Use a Colab or conda environment with `geopandas` installed. The script also has a `shapely` fallback for the packaged data, but a bare system Python will usually be too thin for this route.

The script exports:

- `outputs/scored_sites.csv`
- `outputs/gis_site_comparison_map.png`
- `outputs/gis_spatial_comparison_preview.html`
- `outputs/selected_site.geojson`

## Hosted Preview

Open `outputs/gis_spatial_comparison_preview.html` to inspect the worked example in a browser. The preview is generated from the same script as the scored table and map, so it should be treated as a display surface, not a separate hand-made artifact.

The current worked example is a **teaching sample near HKU**. It uses real-ish WGS84 coordinates and synthetic grocery/convenience points. The 300m catchments are straight-line buffers, not verified walking-network access.

## Student Adaptation Task

Students identify the spatial layer or proximity rule that affects their studio decision.

## Grasshopper Bridge

Use the scored CSV as a simple site-selection input in GH. If students are working with actual Rhino parcels, they can match by `site_id` and use the score to color, filter, or annotate candidate sites. `outputs/selected_site.geojson` is the highest-scoring polygon exported as a minimal geometry handoff.

## Verification Checks

- CRS is stated
- layer source is cited
- map legend is meaningful
- operation sequence is documented
- output supports a design decision
