"""Generate Google Chrome theme from the nepes palette."""

import json


def _hex_to_rgb(hex_color: str) -> list[int]:
    h = hex_color.lstrip("#")
    return [int(h[i:i+2], 16) for i in (0, 2, 4)]


def generate_chrome(palette: dict, theme: str) -> str:
    """Generate a Chrome theme manifest.json for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"

    frame = _hex_to_rgb(t["bg_deep"])
    toolbar = _hex_to_rgb(t["bg"])
    tab_bg = _hex_to_rgb(t["bg_dim"])
    tab_text = _hex_to_rgb(t["fg"])
    ntp_bg = _hex_to_rgb(t["bg"])
    ntp_text = _hex_to_rgb(t["fg"])
    button = _hex_to_rgb(t["fg_dim"])
    bookmark_text = _hex_to_rgb(t["fg_dim"])
    omnibox_bg = _hex_to_rgb(t["bg_alt"])
    omnibox_text = _hex_to_rgb(t["fg"])
    border = _hex_to_rgb(t["border"])

    manifest = {
        "manifest_version": 3,
        "version": "1.0",
        "name": f"Nepes {name}",
        "description": f"Nepes corporate colorscheme — {name.lower()} variant",
        "theme": {
            "colors": {
                "frame": frame,
                "frame_inactive": _hex_to_rgb(t["bg_deep"]),
                "frame_incognito": _hex_to_rgb(t["bg_deep"]),
                "frame_incognito_inactive": _hex_to_rgb(t["bg_deep"]),
                "toolbar": toolbar,
                "tab_background_inactive": tab_bg,
                "tab_text": tab_text,
                "bookmark_text": bookmark_text,
                "ntp_background": ntp_bg,
                "ntp_text": ntp_text,
                "button_background": [0, 0, 0, 0],
                "omnibox_background": omnibox_bg,
                "omnibox_text": omnibox_text,
                "toolbar_button_icon": button,
                "toolbar_top_separator": border,
                "toolbar_bottom_separator": border,
            },
            "tints": {
                "buttons": [-1.0, -1.0, -1.0],
            },
            "properties": {
                "ntp_background_alignment": "bottom",
            },
        },
    }

    return json.dumps(manifest, indent=2) + "\n"
