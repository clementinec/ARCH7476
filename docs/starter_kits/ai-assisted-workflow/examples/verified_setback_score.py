"""Verified micro-component for an AI-assisted workflow.

Classroom use:
    Treat this as an example of a small function that AI might draft, but that
    still needs manual verification before it becomes evidence.

Grasshopper bridge:
    Paste setback_clearance_score into a GhPython component. Inputs can be
    sliders for setback_m and required_m; output can drive object color.
"""


def setback_clearance_score(setback_m: float, required_m: float = 3.0) -> dict:
    """Return a simple clearance score for a setback rule."""
    if required_m <= 0:
        raise ValueError("required_m must be positive")
    ratio = setback_m / required_m
    passes = ratio >= 1.0
    if ratio >= 1.25:
        status = "comfortably passes"
    elif passes:
        status = "passes but keep tolerance visible"
    elif ratio >= 0.85:
        status = "near miss; test drawing tolerance"
    else:
        status = "fails"
    return {
        "setback_m": round(setback_m, 2),
        "required_m": round(required_m, 2),
        "ratio": round(ratio, 2),
        "passes": passes,
        "status": status,
    }


def _manual_checks() -> None:
    assert setback_clearance_score(3.0, 3.0)["passes"] is True
    assert setback_clearance_score(2.4, 3.0)["passes"] is False
    assert setback_clearance_score(3.75, 3.0)["status"] == "comfortably passes"


if __name__ == "__main__":
    _manual_checks()
    for value in [2.4, 2.8, 3.0, 3.75]:
        print(setback_clearance_score(value, 3.0))
