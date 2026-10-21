"""HKU micro-walkability GIS comparison demo.

Run from this folder:
    python3 gis_spatial_comparison_demo.py

Colab note:
    !pip install geopandas shapely matplotlib pandas

Grasshopper bridge:
    Export outputs/scored_sites.csv, then import site_id and scores into GH to
    color candidate parcels or drive a simple selection component.

Teaching note:
    The geometry is a small teaching sample near HKU using real-ish WGS84
    coordinates. Grocery/convenience points are synthetic and labelled as such.
"""

from __future__ import annotations

import json
import math
import os
from html import escape
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
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon as MplPolygon
from shapely.geometry import shape
from shapely.ops import transform

try:
    import geopandas as gpd
except ModuleNotFoundError:
    gpd = None


DATA = ROOT / "data"
CRS_INPUT = "EPSG:4326"
CRS_WORK = "EPSG:3857"
WALK_RADIUS_M = 300
PREVIEW = OUT / "gis_spatial_comparison_preview.html"
SITE_LABEL_OFFSETS = {
    "A": (58, -14),
    "B": (50, -34),
    "C": (0, 42),
}


def web_mercator(lon: float, lat: float) -> tuple[float, float]:
    radius = 6378137.0
    lon_rad = math.radians(lon)
    lat_rad = math.radians(max(min(lat, 85.05112878), -85.05112878))
    x = radius * lon_rad
    y = radius * math.log(math.tan(math.pi / 4 + lat_rad / 2))
    return x, y


def project_geometry(geom):
    return transform(lambda lon, lat, *_: web_mercator(lon, lat), geom)


def read_layer(name: str) -> gpd.GeoDataFrame:
    if gpd is None:
        raise RuntimeError("geopandas is not installed")
    layer = gpd.read_file(DATA / name)
    return layer.set_crs(CRS_INPUT, allow_override=True).to_crs(CRS_WORK)


def read_features(name: str) -> list[dict]:
    with (DATA / name).open() as handle:
        collection = json.load(handle)
    rows = []
    for feature in collection["features"]:
        rows.append(
            {
                "properties": feature["properties"],
                "geometry": project_geometry(shape(feature["geometry"])),
            }
        )
    return rows


def distance_score(distance_m: float, count: int, count_bonus: int) -> float:
    return min(100, max(0, 100 - distance_m / 3) + count * count_bonus)


def score_record(site_id: str, current_use: str, geom, transit_geoms, grocery_geoms, noise_geoms, green_geoms) -> dict:
    centroid = geom.centroid
    walk_buffer = centroid.buffer(WALK_RADIUS_M)

    nearest_transit_m = min(stop.distance(centroid) for stop in transit_geoms)
    nearest_grocery_m = min(point.distance(centroid) for point in grocery_geoms)
    nearest_green_m = min(space.distance(centroid) for space in green_geoms)

    transit_count = sum(walk_buffer.intersects(stop) for stop in transit_geoms)
    grocery_count = sum(walk_buffer.intersects(point) for point in grocery_geoms)
    green_buffer_pct = 100 * sum(space.intersection(walk_buffer).area for space in green_geoms) / walk_buffer.area
    noise_buffer_pct = 100 * sum(zone.intersection(walk_buffer).area for zone in noise_geoms) / walk_buffer.area

    transit_score = distance_score(nearest_transit_m, transit_count, 8)
    grocery_score = distance_score(nearest_grocery_m, grocery_count, 10)
    green_score = min(100, max(0, 100 - nearest_green_m / 4) + green_buffer_pct * 1.5)
    noise_score = max(0, 100 - noise_buffer_pct * 7)
    composite_score = 0.30 * transit_score + 0.25 * grocery_score + 0.20 * green_score + 0.25 * noise_score

    if composite_score >= 82:
        decision_note = "candidate"
    elif composite_score >= 65:
        decision_note = "review assumptions"
    else:
        decision_note = "weak without mitigation"

    return {
        "site_id": site_id,
        "current_use": current_use,
        "nearest_transit_m": round(nearest_transit_m, 1),
        "transit_stops_300m": int(transit_count),
        "nearest_grocery_m": round(nearest_grocery_m, 1),
        "groceries_300m": int(grocery_count),
        "nearest_green_m": round(nearest_green_m, 1),
        "green_buffer_pct": round(green_buffer_pct, 1),
        "noise_buffer_pct": round(noise_buffer_pct, 1),
        "composite_score": round(composite_score, 1),
        "decision_note": decision_note,
        "geometry": geom,
        "walk_buffer": walk_buffer,
    }


def score_sites_geopandas(sites, transit, groceries, noise, green):
    transit_geoms = list(transit.geometry)
    grocery_geoms = list(groceries.geometry)
    noise_geoms = list(noise.geometry)
    green_geoms = list(green.geometry)
    rows = []
    for _, site in sites.iterrows():
        rows.append(
            score_record(
                site["site_id"],
                site["current_use"],
                site.geometry,
                transit_geoms,
                grocery_geoms,
                noise_geoms,
                green_geoms,
            )
        )
    return gpd.GeoDataFrame(rows, geometry="geometry", crs=CRS_WORK)


def score_sites_plain(sites: list[dict], transit: list[dict], groceries: list[dict], noise: list[dict], green: list[dict]) -> list[dict]:
    transit_geoms = [feature["geometry"] for feature in transit]
    grocery_geoms = [feature["geometry"] for feature in groceries]
    noise_geoms = [feature["geometry"] for feature in noise]
    green_geoms = [feature["geometry"] for feature in green]
    return [
        score_record(
            site["properties"]["site_id"],
            site["properties"]["current_use"],
            site["geometry"],
            transit_geoms,
            grocery_geoms,
            noise_geoms,
            green_geoms,
        )
        for site in sites
    ]


def add_polygon(ax, geom, facecolor, edgecolor, alpha=0.5, linewidth=1.0, linestyle="-") -> None:
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
                linestyle=linestyle,
            )
        )


def point_xy(point):
    return point.x, point.y


def feature_name(feature: dict, fallback: str) -> str:
    return feature.get("properties", {}).get("name", fallback)


def label_geometry(ax, geom, text: str, dx: float = 0, dy: float = 0, **kwargs) -> None:
    point = geom.centroid
    ax.text(point.x + dx, point.y + dy, text, **kwargs)


def plot_map_plain(scored: list[dict], transit: list[dict], groceries: list[dict], noise: list[dict], green: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(8.6, 7.2))
    ax.set_facecolor("#fbfaf7")
    for zone in noise:
        add_polygon(ax, zone["geometry"], "#d46b5c", "#9c3f34", alpha=0.22)
        label_geometry(
            ax,
            zone["geometry"],
            feature_name(zone, "road/noise corridor"),
            0,
            10,
            ha="center",
            va="bottom",
            fontsize=7.5,
            color="#7d3a31",
            alpha=0.78,
            rotation=-8,
        )
    for space in green:
        add_polygon(ax, space["geometry"], "#60a86b", "#2f7d4f", alpha=0.32)
        label_geometry(
            ax,
            space["geometry"],
            feature_name(space, "green/open space"),
            0,
            0,
            ha="center",
            va="center",
            fontsize=7,
            color="#1f5f3e",
            alpha=0.72,
        )
    for row in scored:
        add_polygon(ax, row["walk_buffer"], "none", "#4b6f9f", alpha=1.0, linewidth=1.2, linestyle="--")

    scores = [row["composite_score"] for row in scored]
    norm = plt.Normalize(min(scores), max(scores))
    cmap = plt.get_cmap("YlGn")
    for row in scored:
        add_polygon(ax, row["geometry"], cmap(norm(row["composite_score"])), "#222222", alpha=0.92, linewidth=1.3)
        point = row["geometry"].centroid
        dx, dy = SITE_LABEL_OFFSETS.get(row["site_id"], (0, 0))
        ax.annotate(
            row["site_id"],
            (point.x, point.y),
            xytext=(point.x + dx, point.y + dy),
            ha="center",
            va="center",
            weight="bold",
            fontsize=10,
            bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "#222222", "linewidth": 0.8, "alpha": 0.92},
            arrowprops={"arrowstyle": "-", "color": "#333333", "linewidth": 0.75} if dx or dy else None,
        )

    for stop in transit:
        ax.scatter(*point_xy(stop["geometry"]), color="#2f5f9f", marker="^", s=72)
    for point in groceries:
        ax.scatter(*point_xy(point["geometry"]), color="#9a641f", marker="s", s=55)

    handles = [
        Line2D([0], [0], color="#4b6f9f", linestyle="--", label="300m straight-line catchment"),
        Line2D([0], [0], marker="^", color="w", markerfacecolor="#2f5f9f", label="transit stop", markersize=9),
        Line2D([0], [0], marker="s", color="w", markerfacecolor="#9a641f", label="synthetic grocery point", markersize=8),
        Line2D([0], [0], color="#9c3f34", linewidth=5, alpha=0.5, label="road/noise corridor"),
        Line2D([0], [0], color="#2f7d4f", linewidth=5, alpha=0.5, label="green/open space"),
    ]
    ax.legend(handles=handles, loc="lower left", fontsize=8, frameon=True)
    ax.set_title("HKU micro-walkability teaching map\nfew-block parcel choice: 300m catchment + grocery + green + noise proxies")
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.margins(0.10)
    fig.tight_layout()
    fig.savefig(OUT / "gis_site_comparison_map.png", dpi=180)


def plot_map_geopandas(scored, transit, groceries, noise, green) -> None:
    transit_plain = [{"geometry": row.geometry, "properties": {"name": row.get("name", "transit stop")}} for _, row in transit.iterrows()]
    groceries_plain = [{"geometry": row.geometry, "properties": {"name": row.get("name", "synthetic grocery point")}} for _, row in groceries.iterrows()]
    noise_plain = [{"geometry": row.geometry, "properties": {"name": row.get("name", "road/noise corridor")}} for _, row in noise.iterrows()]
    green_plain = [{"geometry": row.geometry, "properties": {"name": row.get("name", "green/open space")}} for _, row in green.iterrows()]
    scored_plain = scored.to_dict("records")
    plot_map_plain(scored_plain, transit_plain, groceries_plain, noise_plain, green_plain)


def write_selected_site_geojson(scored_table: pd.DataFrame, scored_records) -> None:
    winner_id = scored_table.sort_values("composite_score", ascending=False).iloc[0]["site_id"]
    for row in scored_records:
        if row["site_id"] == winner_id:
            geom = row["geometry"]
            break
    else:
        return
    output = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"site_id": winner_id, "selection_rule": "highest composite_score"},
                "geometry": json.loads(gpd.GeoSeries([geom], crs=CRS_WORK).to_crs(CRS_INPUT).to_json())["features"][0]["geometry"]
                if gpd is not None
                else None,
            }
        ],
    }
    if output["features"][0]["geometry"] is not None:
        (OUT / "selected_site.geojson").write_text(json.dumps(output, indent=2), encoding="utf-8")


def build_preview_html(table: pd.DataFrame, backend_note: str) -> None:
    sorted_table = table.sort_values("composite_score", ascending=False)
    rows = "\n".join(
        "<tr>"
        f"<td>{escape(str(row.site_id))}</td>"
        f"<td>{escape(str(row.current_use))}</td>"
        f"<td class='num'>{row.transit_stops_300m}</td>"
        f"<td class='num'>{row.groceries_300m}</td>"
        f"<td class='num'>{row.green_buffer_pct:.1f}</td>"
        f"<td class='num'>{row.noise_buffer_pct:.1f}</td>"
        f"<td class='score'>{row.composite_score:.1f}</td>"
        f"<td><span class='pill {status_class(row.decision_note)}'>{escape(str(row.decision_note))}</span></td>"
        "</tr>"
        for row in sorted_table.itertuples()
    )
    PREVIEW.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {{ margin: 0; font-family: Inter, Arial, sans-serif; background: #f7f4ee; color: #243447; }}
.wrap {{ padding: 16px; }}
.tab {{ display: inline-block; background: #243447; color: white; padding: 6px 10px; font-size: 12px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; }}
h1 {{ margin: 10px 0 6px; font-size: 18px; }}
p {{ margin: 0 0 10px; color: #5d6872; font-size: 13px; }}
.grid {{ display: grid; grid-template-columns: 1.1fr .9fr; gap: 14px; align-items: stretch; }}
.panel {{ background: white; border: 1px solid #ddd5c8; box-shadow: 0 1px 4px rgba(0,0,0,.06); }}
.map {{ width: 100%; height: 100%; min-height: 390px; object-fit: contain; background: white; }}
table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
th {{ background: #243447; color: white; text-align: left; font-weight: 700; padding: 7px 8px; }}
td {{ border: 1px solid #e6dfd4; padding: 6px 8px; vertical-align: top; }}
.num, .score {{ text-align: right; font-variant-numeric: tabular-nums; }}
.score {{ font-weight: 800; }}
.pill {{ display: inline-block; border-radius: 999px; padding: 2px 8px; font-size: 11px; font-weight: 800; white-space: nowrap; }}
.candidate {{ background: #d9ead3; color: #2f6336; }}
.review {{ background: #fce5cd; color: #8a4f13; }}
.weak {{ background: #f4cccc; color: #8b2722; }}
.note {{ margin-top: 10px; padding: 8px 10px; background: #eaf2f8; border-left: 4px solid #4b6f9f; font-size: 12px; }}
code {{ background: #ecece6; padding: 1px 4px; border-radius: 3px; }}
@media (max-width: 900px) {{ .grid {{ grid-template-columns: 1fr; }} .map {{ min-height: 260px; }} }}
</style>
</head>
<body>
<div class="wrap">
  <span class="tab">HKU micro-walkability · teaching sample</span>
  <h1>GIS spatial comparison preview</h1>
  <p>Ultra-zoomed teaching excerpt near HKU with synthetic grocery/convenience points. The buffer is straight-line distance, not a verified walking network.</p>
  <div class="grid">
    <div class="panel"><img class="map" src="gis_site_comparison_map.png" alt="HKU micro walkability map"></div>
    <div class="panel">
      <table>
        <thead><tr><th>site</th><th>use</th><th>transit</th><th>grocery</th><th>green %</th><th>noise %</th><th>score</th><th>decision</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
  <div class="note">Run command: <code>python3 gis_spatial_comparison_demo.py</code>. {escape(backend_note)} Teaching question: does the 300m catchment measure real access, or just distance on a map?</div>
</div>
</body>
</html>
""",
        encoding="utf-8",
    )


def status_class(decision_note: str) -> str:
    if decision_note == "candidate":
        return "candidate"
    if decision_note == "review assumptions":
        return "review"
    return "weak"


def table_without_geometry(records) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {key: value for key, value in row.items() if key not in {"geometry", "walk_buffer"}}
            for row in records
        ]
    )


def main() -> None:
    if gpd is not None:
        sites = read_layer("candidate_sites.geojson")
        transit = read_layer("transit_stops.geojson")
        groceries = read_layer("grocery_points.geojson")
        noise = read_layer("noise_corridors.geojson")
        green = read_layer("green_spaces.geojson")
        scored = score_sites_geopandas(sites, transit, groceries, noise, green)
        scored_records = scored.to_dict("records")
        table = table_without_geometry(scored_records)
        plot_map_geopandas(scored, transit, groceries, noise, green)
        backend_note = "Backend: geopandas."
    else:
        sites = read_features("candidate_sites.geojson")
        transit = read_features("transit_stops.geojson")
        groceries = read_features("grocery_points.geojson")
        noise = read_features("noise_corridors.geojson")
        green = read_features("green_spaces.geojson")
        scored_records = score_sites_plain(sites, transit, groceries, noise, green)
        table = table_without_geometry(scored_records)
        plot_map_plain(scored_records, transit, groceries, noise, green)
        backend_note = "Backend: shapely fallback."

    table.to_csv(OUT / "scored_sites.csv", index=False)
    if gpd is not None:
        write_selected_site_geojson(table, scored_records)
    build_preview_html(table, backend_note)
    print(table.sort_values("composite_score", ascending=False))
    print("\nUncertainty note: 300m buffers are straight-line proxies, not verified walking-network access.")
    print("Backend note: used geopandas." if gpd is not None else "Backend note: geopandas unavailable; used shapely fallback.")
    print(f"Wrote: {OUT / 'scored_sites.csv'}")
    print(f"Wrote: {OUT / 'gis_site_comparison_map.png'}")
    print(f"Wrote: {PREVIEW}")


if __name__ == "__main__":
    main()
