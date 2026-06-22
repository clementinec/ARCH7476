"""GIS spatial comparison demo using small GeoJSON layers.

Run from this folder:
    python3 gis_spatial_comparison_demo.py

Colab note:
    !pip install geopandas shapely matplotlib

Grasshopper bridge:
    Export scored_sites.csv, then import site_id and scores into GH to color
candidate parcels or drive a simple selection component.
"""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
(OUT / ".mplconfig").mkdir(exist_ok=True)
(OUT / ".cache").mkdir(exist_ok=True)
(OUT / ".cache" / "fontconfig").mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(OUT / ".mplconfig"))
os.environ.setdefault("XDG_CACHE_HOME", str(OUT / ".cache"))
os.environ.setdefault("MPLBACKEND", "Agg")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from matplotlib.patches import Polygon as MplPolygon
from shapely.geometry import shape

try:
    import geopandas as gpd
except ModuleNotFoundError:
    gpd = None


DATA = ROOT / "data"
CRS = "EPSG:3857"


def read_layer(name: str) -> gpd.GeoDataFrame:
    if gpd is None:
        raise RuntimeError("geopandas is not installed")
    layer = gpd.read_file(DATA / name)
    # The packaged demo uses abstract local meter coordinates, not longitude/latitude.
    return layer.set_crs(CRS, allow_override=True)


def score_record(site_id: str, current_use: str, geom, stop_geoms, noise_geoms, green_geoms) -> dict:
    centroid = geom.centroid
    nearest_transit_m = min(stop.distance(centroid) for stop in stop_geoms)
    nearest_green_m = min(space.distance(centroid) for space in green_geoms)
    noise_overlap_area = sum(zone.intersection(geom).area for zone in noise_geoms)
    noise_overlap_pct = 100 * noise_overlap_area / geom.area
    access_score = max(0, 100 - nearest_transit_m / 2)
    green_score = max(0, 100 - nearest_green_m / 2)
    noise_score = max(0, 100 - noise_overlap_pct)
    composite_score = 0.40 * access_score + 0.30 * green_score + 0.30 * noise_score
    return {
        "site_id": site_id,
        "current_use": current_use,
        "nearest_transit_m": round(nearest_transit_m, 1),
        "nearest_green_m": round(nearest_green_m, 1),
        "noise_overlap_pct": round(noise_overlap_pct, 1),
        "composite_score": round(composite_score, 1),
        "decision_note": "candidate" if composite_score >= 65 else "needs mitigation or different brief",
        "geometry": geom,
    }


def score_sites_geopandas(
    sites: gpd.GeoDataFrame,
    stops: gpd.GeoDataFrame,
    noise: gpd.GeoDataFrame,
    green: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    stop_geoms = list(stops.geometry)
    noise_geoms = list(noise.geometry)
    green_geoms = list(green.geometry)
    rows = []
    for _, site in sites.iterrows():
        rows.append(score_record(site["site_id"], site["current_use"], site.geometry, stop_geoms, noise_geoms, green_geoms))
    return gpd.GeoDataFrame(rows, geometry="geometry", crs=CRS)


def plot_map_geopandas(scored: gpd.GeoDataFrame, stops: gpd.GeoDataFrame, noise: gpd.GeoDataFrame, green: gpd.GeoDataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 7))
    noise.plot(ax=ax, color="#d46b5c", alpha=0.25, edgecolor="#9c3f34", label="noise exposure")
    green.plot(ax=ax, color="#60a86b", alpha=0.35, edgecolor="#2f7d4f", label="green space")
    scored.plot(
        ax=ax,
        column="composite_score",
        cmap="YlGn",
        edgecolor="#222222",
        linewidth=1.2,
        legend=True,
        legend_kwds={"label": "site score"},
    )
    stops.plot(ax=ax, color="#2f5f9f", markersize=70, marker="^", label="transit stop")
    for _, row in scored.iterrows():
        point = row.geometry.centroid
        ax.annotate(row["site_id"], (point.x, point.y), ha="center", va="center", weight="bold")
    ax.set_title("Candidate sites: access, noise, and green-space comparison")
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(OUT / "gis_site_comparison_map.png", dpi=180)


def read_features(name: str) -> list[dict]:
    with (DATA / name).open() as handle:
        collection = json.load(handle)
    rows = []
    for feature in collection["features"]:
        rows.append({"properties": feature["properties"], "geometry": shape(feature["geometry"])})
    return rows


def score_sites_plain(sites: list[dict], stops: list[dict], noise: list[dict], green: list[dict]) -> list[dict]:
    stop_geoms = [feature["geometry"] for feature in stops]
    noise_geoms = [feature["geometry"] for feature in noise]
    green_geoms = [feature["geometry"] for feature in green]
    return [
        score_record(
            site["properties"]["site_id"],
            site["properties"]["current_use"],
            site["geometry"],
            stop_geoms,
            noise_geoms,
            green_geoms,
        )
        for site in sites
    ]


def add_polygon(ax, geom, facecolor, edgecolor, alpha=0.5, linewidth=1.0) -> None:
    geoms = geom.geoms if geom.geom_type == "MultiPolygon" else [geom]
    for poly in geoms:
        ax.add_patch(
            MplPolygon(
                list(poly.exterior.coords),
                closed=True,
                facecolor=facecolor,
                edgecolor=edgecolor,
                alpha=alpha,
                linewidth=linewidth,
            )
        )


def plot_map_plain(scored: list[dict], stops: list[dict], noise: list[dict], green: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(7, 7))
    for zone in noise:
        add_polygon(ax, zone["geometry"], "#d46b5c", "#9c3f34", alpha=0.25)
    for space in green:
        add_polygon(ax, space["geometry"], "#60a86b", "#2f7d4f", alpha=0.35)

    scores = [row["composite_score"] for row in scored]
    norm = plt.Normalize(min(scores), max(scores))
    cmap = plt.get_cmap("YlGn")
    for row in scored:
        add_polygon(ax, row["geometry"], cmap(norm(row["composite_score"])), "#222222", alpha=0.9, linewidth=1.2)
        point = row["geometry"].centroid
        ax.annotate(row["site_id"], (point.x, point.y), ha="center", va="center", weight="bold")

    for stop in stops:
        point = stop["geometry"]
        ax.scatter(point.x, point.y, color="#2f5f9f", marker="^", s=70)

    scalar = cm.ScalarMappable(norm=norm, cmap=cmap)
    fig.colorbar(scalar, ax=ax, shrink=0.65, label="site score")
    ax.set_title("Candidate sites: access, noise, and green-space comparison")
    ax.set_aspect("equal")
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(OUT / "gis_site_comparison_map.png", dpi=180)


def main() -> None:
    if gpd is not None:
        sites = read_layer("candidate_sites.geojson")
        stops = read_layer("transit_stops.geojson")
        noise = read_layer("noise_zones.geojson")
        green = read_layer("green_spaces.geojson")
        scored = score_sites_geopandas(sites, stops, noise, green)
        table = scored.drop(columns="geometry")
        plot_map_geopandas(scored, stops, noise, green)
    else:
        sites = read_features("candidate_sites.geojson")
        stops = read_features("transit_stops.geojson")
        noise = read_features("noise_zones.geojson")
        green = read_features("green_spaces.geojson")
        scored = score_sites_plain(sites, stops, noise, green)
        table = pd.DataFrame([{key: value for key, value in row.items() if key != "geometry"} for row in scored])
        plot_map_plain(scored, stops, noise, green)

    table.to_csv(OUT / "scored_sites.csv", index=False)
    print(table.sort_values("composite_score", ascending=False))
    print("\nUncertainty note: the score weights are a design argument, not a neutral fact.")
    print("Backend note: used geopandas." if gpd is not None else "Backend note: geopandas unavailable; used shapely fallback.")
    print(f"Wrote: {OUT / 'scored_sites.csv'}")
    print(f"Wrote: {OUT / 'gis_site_comparison_map.png'}")


if __name__ == "__main__":
    main()
