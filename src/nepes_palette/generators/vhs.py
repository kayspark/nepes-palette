"""Generate VHS terminal theme from the nepes palette."""

import json


def generate_vhs(palette: dict, theme: str) -> str:
    """Generate a VHS theme JSON file for the given theme."""
    t = palette[theme]
    a = t["ansi"]
    name = "Nepes Dark" if theme == "dark" else "Nepes Light"

    obj = {
        "name": name,
        "black": a["black"],
        "red": a["red"],
        "green": a["green"],
        "yellow": a["yellow"],
        "blue": a["blue"],
        "purple": a["magenta"],
        "cyan": a["cyan"],
        "white": a["white"],
        "brightBlack": a["bright_black"],
        "brightRed": a["bright_red"],
        "brightGreen": a["bright_green"],
        "brightYellow": a["bright_yellow"],
        "brightBlue": a["bright_blue"],
        "brightPurple": a["bright_magenta"],
        "brightCyan": a["bright_cyan"],
        "brightWhite": a["bright_white"],
        "foreground": t["fg"],
        "background": t["bg"],
        "selectionBackground": t["selection"],
        "cursorColor": t["cursor"],
    }

    return json.dumps(obj, indent=2) + "\n"
