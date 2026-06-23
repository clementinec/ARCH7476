"""Preset simulation / proxy test demo.

This is not an energy simulation. It is a transparent proxy for a Week 5
classroom discussion: does a facade change plausibly reduce overheating risk
enough to justify further development?

Run from this folder:
    python3 facade_heat_proxy_demo.py

Grasshopper bridge:
    The same columns can be exported from sliders or panels in GH, then the
    resulting CSV can be read back into GH as scenario scores.
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


DATA = ROOT / "data" / "facade_scenarios.csv"


def heat_proxy(row: pd.Series) -> pd.Series:
    shading_factor = max(0.25, 1 - 0.55 * row["shading_depth_m"])
    solar_delta_t = row["solar_exposure_w_m2"] * row["wwr"] * shading_factor * 0.010
    internal_delta_t = row["internal_gain_w_m2"] * 0.08
    ventilation_offset = row["ventilation_ach"] * row["operable_area_ratio"] * 1.8
    ta_proxy_c = row["outdoor_temp_c"] + solar_delta_t + internal_delta_t - ventilation_offset
    overheat_index = max(0, ta_proxy_c - 28.0) * 2.5
    return pd.Series(
        {
            "shading_factor": round(shading_factor, 2),
            "ta_proxy_c": round(ta_proxy_c, 1),
            "overheat_index": round(overheat_index, 1),
            "passes_threshold": ta_proxy_c <= 34.5,
        }
    )


def plot_results(scored: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.8))
    colors = scored["passes_threshold"].map({True: "#2f7d4f", False: "#b5463c"})
    ax.bar(scored["scenario"], scored["ta_proxy_c"], color=colors)
    ax.axhline(34.5, color="#222222", linestyle="--", linewidth=1.2, label="class threshold")
    ax.set_title("Facade heat proxy: estimated air temperature by scenario")
    ax.set_ylabel("Ta proxy, deg C")
    ax.set_ylim(28, max(scored["ta_proxy_c"]) + 2)
    ax.legend(loc="upper right")
    ax.grid(axis="y", alpha=0.25)
    fig.autofmt_xdate(rotation=25)
    fig.tight_layout()
    fig.savefig(OUT / "facade_heat_proxy_chart.png", dpi=180)


def main() -> None:
    scenarios = pd.read_csv(DATA)
    scored = pd.concat([scenarios, scenarios.apply(heat_proxy, axis=1)], axis=1)
    scored["decision_note"] = scored["passes_threshold"].map(
        {True: "keep as candidate", False: "revise shading, WWR, or ventilation"}
    )
    scored.to_csv(OUT / "facade_heat_proxy_scores.csv", index=False)
    plot_results(scored)
    print(scored[["scenario", "ta_proxy_c", "overheat_index", "passes_threshold", "decision_note"]])
    print("\nUncertainty note: coefficients are classroom placeholders, not calibrated physics.")
    print(f"Wrote: {OUT / 'facade_heat_proxy_scores.csv'}")
    print(f"Wrote: {OUT / 'facade_heat_proxy_chart.png'}")


if __name__ == "__main__":
    main()
