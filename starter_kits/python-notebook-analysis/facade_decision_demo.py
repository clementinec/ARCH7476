"""Facade variant comparison demo.

Run from this folder:
    python3 facade_decision_demo.py

Colab note:
    Upload data/facade_variants.csv, keep the same folder structure, then run.

Grasshopper bridge:
    Export the output CSV and read it with LunchBox/TT Toolbox/Panel + Split Text,
    or paste the scoring formulas into a GhPython component.
"""

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


DATA = ROOT / "data" / "facade_variants.csv"


def score_variants(df: pd.DataFrame) -> pd.DataFrame:
    """Create transparent proxy scores from visible facade assumptions."""
    scored = df.copy()
    scored["daylight_proxy"] = (
        100
        * scored["wwr"]
        * (1 - 0.18 * scored["shading_depth_m"])
        * (1 - 0.08 * (1 / (scored["fin_spacing_m"] + 1)))
    ).round(1)
    scored["solar_gain_proxy"] = (
        100
        * scored["wwr"]
        * (1 - 0.55 * scored["shading_depth_m"].clip(upper=1.2))
    ).round(1)
    scored["passes_threshold"] = (
        (scored["daylight_proxy"] >= 42)
        & (scored["solar_gain_proxy"] <= 48)
        & (scored["view_score"] >= 0.55)
        & (scored["estimated_glare_hours"] <= 2.0)
    )
    scored["decision_note"] = scored["passes_threshold"].map(
        {True: "candidate for design development", False: "revise or defend exception"}
    )
    return scored


def plot_tradeoff(scored: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = scored["passes_threshold"].map({True: "#2f7d4f", False: "#b5463c"})
    ax.scatter(
        scored["solar_gain_proxy"],
        scored["daylight_proxy"],
        s=160,
        c=colors,
        edgecolor="#222222",
        linewidth=0.8,
    )
    for _, row in scored.iterrows():
        ax.annotate(row["variant"], (row["solar_gain_proxy"] + 0.6, row["daylight_proxy"] + 0.4))

    ax.axhline(42, color="#4b6f9f", linestyle="--", linewidth=1.2, label="minimum daylight proxy")
    ax.axvline(48, color="#8a5a28", linestyle="--", linewidth=1.2, label="maximum solar gain proxy")
    ax.set_title("Facade variants: daylight against solar gain")
    ax.set_xlabel("Solar gain proxy, lower is better")
    ax.set_ylabel("Daylight proxy, higher is better")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / "facade_variant_tradeoff.png", dpi=180)


def main() -> None:
    variants = pd.read_csv(DATA)
    scored = score_variants(variants)
    scored.to_csv(OUT / "facade_variant_scores.csv", index=False)
    plot_tradeoff(scored)
    print(scored[["variant", "daylight_proxy", "solar_gain_proxy", "passes_threshold", "decision_note"]])
    print(f"\nWrote: {OUT / 'facade_variant_scores.csv'}")
    print(f"Wrote: {OUT / 'facade_variant_tradeoff.png'}")


if __name__ == "__main__":
    main()
