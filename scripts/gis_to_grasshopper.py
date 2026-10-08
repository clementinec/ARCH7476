"""
gis_to_grasshopper.py
Convert GeoJSON / Shapefile spatial data into CSV files
that Grasshopper can import with standard Read File + Split Text.

Usage:
    python gis_to_grasshopper.py input.geojson output_folder/
    python gis_to_grasshopper.py input.shp output_folder/ --crs 2326

Outputs:
    points.csv      — centroid x, y and all attribute columns
    polygons.csv    — one row per vertex: id, ring, x, y
    lines.csv       — one row per vertex: id, x, y
    attributes.csv  — one row per feature: id + all properties
    summary.txt     — quick stats for sanity-checking in class

Students open these in Grasshopper with:
    Read File → Split Text (separator = ",") → standard data wrangling
"""

import argparse
import csv
import json
import os
import sys

try:
    import geopandas as gpd
except ImportError:
    sys.exit(
        "geopandas is required.\n"
        "Install:  conda install -c conda-forge geopandas\n"
        "   or:    pip install geopandas"
    )


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def extract_coords(geom):
    """Yield (ring_index, x, y) tuples from any geometry type."""
    gtype = geom.geom_type
    if gtype == "Point":
        yield (0, geom.x, geom.y)
    elif gtype == "MultiPoint":
        for pt in geom.geoms:
            yield (0, pt.x, pt.y)
    elif gtype == "LineString":
        for x, y, *_ in geom.coords:
            yield (0, x, y)
    elif gtype == "MultiLineString":
        for i, line in enumerate(geom.geoms):
            for x, y, *_ in line.coords:
                yield (i, x, y)
    elif gtype == "Polygon":
        for i, ring in enumerate([geom.exterior] + list(geom.interiors)):
            for x, y, *_ in ring.coords:
                yield (i, x, y)
    elif gtype == "MultiPolygon":
        ring_offset = 0
        for poly in geom.geoms:
            for i, ring in enumerate([poly.exterior] + list(poly.interiors)):
                for x, y, *_ in ring.coords:
                    yield (ring_offset + i, x, y)
            ring_offset += 1 + len(list(poly.interiors))


def run(input_path, output_dir, target_crs):
    gdf = gpd.read_file(input_path)
    print(f"Loaded {len(gdf)} features from {input_path}")
    print(f"  Source CRS: {gdf.crs}")

    if target_crs:
        gdf = gdf.to_crs(epsg=target_crs)
        print(f"  Reprojected to EPSG:{target_crs}")

    os.makedirs(output_dir, exist_ok=True)

    attr_cols = [c for c in gdf.columns if c != "geometry"]

    # --- attributes.csv (one row per feature, all properties) ---
    attr_rows = []
    for idx, row in gdf.iterrows():
        attr_rows.append([idx] + [row[c] for c in attr_cols])
    write_csv(
        os.path.join(output_dir, "attributes.csv"),
        ["id"] + attr_cols,
        attr_rows,
    )

    # --- points.csv (centroids) ---
    pt_rows = []
    for idx, row in gdf.iterrows():
        c = row.geometry.centroid
        pt_rows.append([idx, round(c.x, 4), round(c.y, 4)] + [row[col] for col in attr_cols])
    write_csv(
        os.path.join(output_dir, "points.csv"),
        ["id", "x", "y"] + attr_cols,
        pt_rows,
    )

    # --- polygons.csv / lines.csv (vertex-level) ---
    poly_rows = []
    line_rows = []
    for idx, row in gdf.iterrows():
        gtype = row.geometry.geom_type
        for ring, x, y in extract_coords(row.geometry):
            coord = [idx, ring, round(x, 4), round(y, 4)]
            if "Polygon" in gtype:
                poly_rows.append(coord)
            elif "Line" in gtype:
                line_rows.append(coord)
            else:
                pass  # points already handled

    if poly_rows:
        write_csv(
            os.path.join(output_dir, "polygons.csv"),
            ["id", "ring", "x", "y"],
            poly_rows,
        )
        print(f"  polygons.csv: {len(poly_rows)} vertices")

    if line_rows:
        write_csv(
            os.path.join(output_dir, "lines.csv"),
            ["id", "ring", "x", "y"],
            line_rows,
        )
        print(f"  lines.csv: {len(line_rows)} vertices")

    # --- summary.txt ---
    bounds = gdf.total_bounds  # minx, miny, maxx, maxy
    with open(os.path.join(output_dir, "summary.txt"), "w") as f:
        f.write(f"Source: {input_path}\n")
        f.write(f"Features: {len(gdf)}\n")
        f.write(f"CRS: {gdf.crs}\n")
        f.write(f"Geometry types: {gdf.geom_type.unique().tolist()}\n")
        f.write(f"Bounding box:\n")
        f.write(f"  min x: {bounds[0]:.2f}  min y: {bounds[1]:.2f}\n")
        f.write(f"  max x: {bounds[2]:.2f}  max y: {bounds[3]:.2f}\n")
        f.write(f"  width:  {bounds[2]-bounds[0]:.2f}\n")
        f.write(f"  height: {bounds[3]-bounds[1]:.2f}\n")
        f.write(f"Columns: {attr_cols}\n")

    print(f"  points.csv:     {len(pt_rows)} centroids")
    print(f"  attributes.csv: {len(attr_rows)} rows × {len(attr_cols)} columns")
    print(f"  summary.txt:    written")
    print(f"\nDone → {output_dir}/")
    print("Open points.csv in Grasshopper with: Read File → Split Text (separator ',')")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert GIS data to Grasshopper-friendly CSV files"
    )
    parser.add_argument("input", help="Path to .geojson or .shp file")
    parser.add_argument("output", help="Output directory for CSV files")
    parser.add_argument(
        "--crs",
        type=int,
        default=2326,
        help="Target EPSG code (default: 2326 = Hong Kong 1980 Grid)",
    )
    args = parser.parse_args()
    run(args.input, args.output, args.crs)
