from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd


RNG = np.random.default_rng(42)


def simulate_building_performance(n: int = 200, random_state: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    wwr = rng.uniform(0.2, 0.85, size=n)
    shading_depth_m = rng.uniform(0.0, 1.2, size=n)
    orientation = rng.choice(["N", "E", "S", "W"], size=n)
    glazing_u = rng.uniform(1.2, 3.0, size=n)
    climate = rng.choice(["subtropical", "temperate"], size=n, p=[0.7, 0.3])
    # Simple physics-inspired patterns
    solar_gain = (wwr * (1 - np.clip(shading_depth_m / 1.2, 0, 1)))
    orient_factor = np.select(
        [orientation == "S", orientation == "W", orientation == "E", orientation == "N"],
        [1.15, 1.05, 1.0, 0.9],
        default=1.0,
    )
    climate_coolmult = np.where(climate == "subtropical", 1.0, 0.85)
    cooling_kwh_m2 = 80 + 220 * solar_gain * orient_factor * climate_coolmult + rng.normal(0, 10, n)
    heating_kwh_m2 = np.clip(40 + (3.2 - glazing_u) * 22 + rng.normal(0, 5, n), 0, None)
    eui = cooling_kwh_m2 + heating_kwh_m2 + rng.normal(0, 8, n)
    daylit_area = np.clip(0.3 + 0.9 * wwr - 0.35 * shading_depth_m + rng.normal(0, 0.05, n), 0, 1)
    glare_probability = np.clip(0.55 * wwr - 0.3 * shading_depth_m + rng.normal(0, 0.05, n) + (orientation == "W") * 0.05, 0, 1)
    occupancy_density = rng.uniform(10, 45, n)
    noise_db = np.clip(35 + 0.4 * occupancy_density + rng.normal(0, 3, n), 30, 80)
    satisfaction = np.clip(4.7 - 0.008 * eui + 0.6 * daylit_area - 0.7 * glare_probability + rng.normal(0, 0.2, n), 1.5, 4.9)

    df = pd.DataFrame(
        {
            "wwr": wwr,
            "shading_depth_m": shading_depth_m,
            "orientation": orientation,
            "glazing_u_w_m2k": glazing_u,
            "climate_zone": climate,
            "daylit_area": daylit_area,
            "glare_probability": glare_probability,
            "cooling_kwh_m2": cooling_kwh_m2,
            "heating_kwh_m2": heating_kwh_m2,
            "eui_kwh_m2": eui,
            "occupancy_density_p_per_100m2": occupancy_density,
            "satisfaction_0_5": satisfaction,
            "noise_db": noise_db,
        }
    )
    return df


def simulate_pilot_observations(n: int = 120, random_state: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    t = pd.date_range("2025-03-01 09:00", periods=n, freq="10min")
    cond = np.where(np.arange(n) % 2 == 0, "A", "B")
    base_occ = 20 + 8 * np.sin(np.linspace(0, 3.5 * np.pi, n))
    occupancy = np.clip(base_occ + (cond == "B") * 3 + rng.normal(0, 2.5, n), 0, None).astype(int)
    dwell_mean = np.clip(6 + (cond == "B") * 1.2 + rng.normal(0, 1.0, n), 1, None)
    dwell_std = np.clip(1.2 + rng.normal(0, 0.3, n), 0.2, None)
    temp_c = 23 + 2 * np.sin(np.linspace(0, 2 * np.pi, n)) + rng.normal(0, 0.5, n)
    humidity = np.clip(55 + 5 * np.cos(np.linspace(0, 2.2 * np.pi, n)) + rng.normal(0, 2, n), 35, 85)
    return pd.DataFrame(
        {
            "timestamp": t,
            "condition": cond,
            "occupancy_count": occupancy,
            "dwell_time_mean_min": dwell_mean,
            "dwell_time_std_min": dwell_std,
            "temp_c": temp_c,
            "humidity_pct": humidity,
        }
    )


def simulate_survey_responses(n: int = 60, random_state: int = 123) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    positives = [
        "daylight", "shade", "views", "quiet", "breeze", "green", "spacious", "seating", "cool", "comfortable",
        "wayfinding", "friendly", "vibrant", "natural light", "privacy", "cozy", "accessible", "clean", "lively",
    ]
    negatives = [
        "glare", "heat", "noise", "crowded", "confusing", "dark", "stuffy", "windy", "hot", "cold",
        "expensive", "difficult", "slippery", "dirty", "unsafe",
    ]
    templates = [
        "I love the {pos} and {pos2}",
        "Too much {neg} near the {pos}",
        "More {pos} would help reduce {neg}",
        "The space feels {pos} but sometimes {neg}",
        "Great {pos} and {pos2}, but {neg} at noon",
    ]
    rows = []
    for _ in range(n):
        if rng.random() < 0.6:
            txt = templates[rng.integers(0, len(templates))].format(
                pos=rng.choice(positives), pos2=rng.choice(positives), neg=rng.choice(negatives)
            )
        else:
            txt = f"{rng.choice(['Love','Hate','Prefer','Avoid'])} the {rng.choice(positives+negatives)} here"
        rows.append(txt)
    return pd.DataFrame({"response_text": rows})


def save_default_fake_data(base_dir: str | Path = ".") -> Tuple[Path, Path, Path]:
    base = Path(base_dir)
    data_dir = base / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    b = simulate_building_performance()
    p = simulate_pilot_observations()
    s = simulate_survey_responses()
    bf = data_dir / "building_performance_fake.csv"
    pf = data_dir / "pilot_observations_fake.csv"
    sf = data_dir / "survey_responses_fake.csv"
    b.to_csv(bf, index=False)
    p.to_csv(pf, index=False)
    s.to_csv(sf, index=False)
    return bf, pf, sf


if __name__ == "__main__":
    paths = save_default_fake_data(Path(__file__).resolve().parents[1])
    print("Saved datasets:", paths)

