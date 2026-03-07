"""Generate Slack sidebar theme from the nepes palette."""


def generate_slack(palette: dict, theme: str) -> str:
    """Generate a Slack sidebar theme string for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"

    def strip(color: str) -> str:
        return t[color].lstrip("#")

    values = ",".join([
        strip("bg_deep"),      # Column BG
        strip("bg_hl"),        # Menu BG Hover
        strip("blue"),         # Active Item
        strip("fg"),           # Active Item Text
        strip("bg_alt"),       # Hover Item
        strip("fg_dim"),       # Text Color
        strip("green"),        # Active Presence
        strip("red"),          # Mention Badge
    ])

    return f"""\
# Nepes {name} — Slack sidebar theme
# Paste into Slack → Preferences → Themes → Custom
# Column BG, Menu BG Hover, Active Item, Active Item Text, Hover Item, Text Color, Active Presence, Mention Badge
{values}
"""
