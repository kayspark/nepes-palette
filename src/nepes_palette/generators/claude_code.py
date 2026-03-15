"""Generate Claude Code (tweakcc) theme JSON from the nepes palette."""

import json

from nepes_palette.colors import lighten, darken


def _hex_to_rgb(h: str) -> str:
    """Convert #RRGGBB to rgb(R,G,B) format for tweakcc."""
    h = h.lstrip("#")
    return f"rgb({int(h[0:2], 16)},{int(h[2:4], 16)},{int(h[4:6], 16)})"


def generate_claude_code(palette: dict, theme: str) -> str:
    """Generate a tweakcc-compatible theme JSON for Claude Code."""
    t = palette[theme]
    is_dark = theme == "dark"
    label = "Dark" if is_dark else "Light"

    # Shorthand converters
    rgb = _hex_to_rgb

    # Derive shimmer variants (slightly lighter for dark, darker for light)
    def shimmer(hex_color: str) -> str:
        return rgb(lighten(hex_color, 0.15) if is_dark else darken(hex_color, 0.15))

    colors = {
        # UI chrome
        "autoAccept": rgb(t["green"]),
        "bashBorder": rgb(t["fg_muted"]),
        "claude": rgb(t["orange"]),
        "claudeShimmer": shimmer(t["orange"]),
        "claudeBlue_FOR_SYSTEM_SPINNER": rgb(t["blue"]),
        "claudeBlueShimmer_FOR_SYSTEM_SPINNER": shimmer(t["blue"]),
        "permission": rgb(t["yellow"]),
        "permissionShimmer": shimmer(t["yellow"]),
        "planMode": rgb(t["magenta"]),
        "ide": rgb(t["cyan"]),
        "promptBorder": rgb(t["blue"]),
        "promptBorderShimmer": shimmer(t["blue"]),

        # Text
        "text": rgb(t["fg"]),
        "inverseText": rgb(t["bg"]),
        "inactive": rgb(t["fg_muted"]),
        "subtle": rgb(t["fg_subtle"]),
        "suggestion": rgb(t["fg_dim"]),
        "remember": rgb(t["orange"]),

        # Status
        "background": rgb(t["bg"]),
        "success": rgb(t["green"]),
        "error": rgb(t["red"]),
        "warning": rgb(t["orange"]),
        "warningShimmer": shimmer(t["orange"]),

        # Diffs
        "diffAdded": rgb(t["green"]),
        "diffRemoved": rgb(t["red"]),
        "diffAddedDimmed": rgb(t["green_dim"]),
        "diffRemovedDimmed": rgb(t["red_dim"]),
        "diffAddedWord": rgb(t["green_bright"]),
        "diffRemovedWord": rgb(t["red_bright"]),
        "diffAddedWordDimmed": rgb(t["green_dim"]),
        "diffRemovedWordDimmed": rgb(t["red_dim"]),

        # Subagent colors
        "red_FOR_SUBAGENTS_ONLY": rgb(t["red"]),
        "blue_FOR_SUBAGENTS_ONLY": rgb(t["blue"]),
        "green_FOR_SUBAGENTS_ONLY": rgb(t["green"]),
        "yellow_FOR_SUBAGENTS_ONLY": rgb(t["yellow"]),
        "purple_FOR_SUBAGENTS_ONLY": rgb(t["magenta"]),
        "orange_FOR_SUBAGENTS_ONLY": rgb(t["orange"]),
        "pink_FOR_SUBAGENTS_ONLY": rgb(t["magenta_bright"]),
        "cyan_FOR_SUBAGENTS_ONLY": rgb(t["cyan"]),

        # Professional
        "professionalBlue": rgb(t["blue"]),

        # Rainbow
        "rainbow_red": rgb(t["red"]),
        "rainbow_orange": rgb(t["orange"]),
        "rainbow_yellow": rgb(t["yellow"]),
        "rainbow_green": rgb(t["green"]),
        "rainbow_blue": rgb(t["blue"]),
        "rainbow_indigo": rgb(t["blue_bright"]),
        "rainbow_violet": rgb(t["magenta"]),
        "rainbow_red_shimmer": shimmer(t["red"]),
        "rainbow_orange_shimmer": shimmer(t["orange"]),
        "rainbow_yellow_shimmer": shimmer(t["yellow"]),
        "rainbow_green_shimmer": shimmer(t["green"]),
        "rainbow_blue_shimmer": shimmer(t["blue"]),
        "rainbow_indigo_shimmer": shimmer(t["blue_bright"]),
        "rainbow_violet_shimmer": shimmer(t["magenta"]),

        # Mascot / backgrounds
        "clawd_body": rgb(t["orange"]),
        "clawd_background": rgb(t["bg_dim"]),
        "userMessageBackground": rgb(t["bg_alt"]),
        "bashMessageBackgroundColor": rgb(t["bg_dim"]),
        "memoryBackgroundColor": rgb(t["bg_alt"]),

        # Rate limit bar
        "rate_limit_fill": rgb(t["blue"]),
        "rate_limit_empty": rgb(t["bg_hl"]),
    }

    theme_obj = {
        "name": f"Nepes {label}",
        "id": f"nepes-{theme}",
        "colors": colors,
    }

    return json.dumps(theme_obj, indent=2) + "\n"
