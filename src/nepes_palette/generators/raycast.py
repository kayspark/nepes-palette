"""Generate Raycast theme from the nepes palette."""

import json


def generate_raycast(palette: dict, theme: str) -> str:
    """Generate a Raycast theme JSON for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"
    appearance = "dark" if theme == "dark" else "light"

    theme_data = {
        "name": f"Nepes {name}",
        "appearance": appearance,
        "colors": {
            "background": t["bg"],
            "backgroundSecondary": t["bg_alt"],
            "text": t["fg"],
            "textSecondary": t["fg_dim"],
            "tint": t["blue"],
            "loader": t["blue"],
            "selection": t["bg_hl"],
            "separator": t["border"],
            "red": t["red"],
            "orange": t["orange"],
            "yellow": t["yellow"],
            "green": t["green"],
            "blue": t["blue"],
            "purple": t["magenta"],
        },
    }

    return json.dumps(theme_data, indent=2) + "\n"
