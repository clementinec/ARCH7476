---
title: "Starter Kit: GIS Spatial Comparison"
format:
  html:
    toc: true
---

# GIS Spatial Comparison

**Launch status:** runnable GeoJSON demo added.

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
- `data/noise_zones.geojson`
- `data/green_spaces.geojson`
- `gis_spatial_comparison_demo.py`

## Demo Run

From this folder:

```bash
python3 gis_spatial_comparison_demo.py
```

Use a Colab or conda environment with `geopandas` installed. The script also has a `shapely` fallback for the packaged data, but a bare system Python will usually be too thin for this route.

The script exports:

- `outputs/scored_sites.csv`
- `outputs/gis_site_comparison_map.png`

## Student Adaptation Task

Students identify the spatial layer or proximity rule that affects their studio decision.

## Grasshopper Bridge

Use the scored CSV as a simple site-selection input in GH. If students are working with actual Rhino parcels, they can match by `site_id` and use the score to color, filter, or annotate candidate sites.

## Verification Checks

- CRS is stated
- layer source is cited
- map legend is meaningful
- operation sequence is documented
- output supports a design decision
