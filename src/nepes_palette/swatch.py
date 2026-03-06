"""Render the full Nepes palette as a labeled PNG grid."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.patches as mpatches  # noqa: E402
from pathlib import Path  # noqa: E402


def _luminance(hex_color: str) -> float:
    """Relative luminance (ITU-R BT.709) from a hex color string."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    # Linearize sRGB
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def _text_color(hex_color: str) -> str:
    """Return black or white text depending on background luminance."""
    return "#000000" if _luminance(hex_color) > 0.18 else "#FFFFFF"


def _draw_row(
    ax: plt.Axes,
    y: float,
    colors: list[tuple[str, str]],
    cell_w: float,
    cell_h: float,
    x_start: float = 0.0,
) -> None:
    """Draw a horizontal row of labeled color cells.

    *colors* is a list of (label, hex_value) tuples.
    """
    for i, (label, hex_val) in enumerate(colors):
        x = x_start + i * cell_w
        rect = mpatches.FancyBboxPatch(
            (x, y), cell_w, cell_h,
            boxstyle="round,pad=0.01",
            facecolor=hex_val,
            edgecolor="#40404040",
            linewidth=0.5,
        )
        ax.add_patch(rect)
        tc = _text_color(hex_val)
        cx, cy = x + cell_w / 2, y + cell_h / 2
        ax.text(cx, cy + cell_h * 0.12, label,
                ha="center", va="center", fontsize=5.5,
                fontweight="bold", color=tc)
        ax.text(cx, cy - cell_h * 0.15, hex_val.upper(),
                ha="center", va="center", fontsize=4.5,
                fontfamily="monospace", color=tc)


def _section_label(ax: plt.Axes, y: float, text: str) -> None:
    """Draw a left-aligned section heading."""
    ax.text(0.05, y + 0.02, text, fontsize=7, fontweight="bold",
            color="#888888", va="bottom")


def render_swatch(palette: dict, output: str | Path, *, dpi: int = 200) -> None:
    """Render the full palette as a labeled PNG swatch grid.

    Parameters
    ----------
    palette : dict
        Parsed palette (from ``load_palette``).
    output : str | Path
        Destination PNG path.
    dpi : int
        Output resolution.
    """
    cell_h = 0.38
    row_gap = 0.06
    section_gap = 0.22

    # Collect all sections in order (bottom-up drawing, so build list top-down
    # then reverse y).
    sections: list[tuple[str, list[list[tuple[str, str]]]]] = []

    # -- Brand colors --
    brand = palette["brand"]
    sections.append(("Brand Colors", [
        [(k, v) for k, v in brand.items()],
    ]))

    # -- Dark theme --
    dark = palette["dark"]
    dark_bg = [(k, dark[k]) for k in
               ("bg_deep", "bg", "bg_dim", "bg_alt", "bg_hl", "bg_overlay")
               if k in dark]
    dark_fg = [(k, dark[k]) for k in
               ("fg", "fg_dim", "fg_subtle", "fg_muted")
               if k in dark]
    dark_core = []
    for name in ("blue", "red", "green", "orange", "magenta", "cyan", "yellow"):
        for suffix in ("", "_dim", "_bright"):
            key = name + suffix
            if key in dark:
                dark_core.append((key, dark[key]))
    dark_utility = [(k, dark[k]) for k in
                    ("cursor", "selection", "border", "comment")
                    if k in dark]

    dark_ansi = palette["dark"]["ansi"]
    ansi_normal = [(k, dark_ansi[k]) for k in
                   ("black", "red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")]
    ansi_bright = [(k, dark_ansi[k]) for k in
                   ("bright_black", "bright_red", "bright_green",
                    "bright_yellow", "bright_blue", "bright_magenta",
                    "bright_cyan", "bright_white")]

    sections.append(("Dark  |  Background Ramp", [dark_bg]))
    sections.append(("Dark  |  Foreground Ramp + Utility", [dark_fg + dark_utility]))
    sections.append(("Dark  |  Core Colors", [dark_core]))
    sections.append(("Dark  |  ANSI 16", [ansi_normal, ansi_bright]))

    # -- Light theme --
    light = palette["light"]
    light_bg = [(k, light[k]) for k in
                ("bg_deep", "bg", "bg_dim", "bg_alt", "bg_hl", "bg_overlay")
                if k in light]
    light_fg = [(k, light[k]) for k in
                ("fg", "fg_dim", "fg_subtle", "fg_muted")
                if k in light]
    light_core = []
    for name in ("blue", "red", "green", "orange", "magenta", "cyan", "yellow"):
        for suffix in ("", "_dim", "_bright"):
            key = name + suffix
            if key in light:
                light_core.append((key, light[key]))
    light_utility = [(k, light[k]) for k in
                     ("cursor", "selection", "border", "comment")
                     if k in light]

    light_ansi = palette["light"]["ansi"]
    l_ansi_normal = [(k, light_ansi[k]) for k in
                     ("black", "red", "green", "yellow", "blue",
                      "magenta", "cyan", "white")]
    l_ansi_bright = [(k, light_ansi[k]) for k in
                     ("bright_black", "bright_red", "bright_green",
                      "bright_yellow", "bright_blue", "bright_magenta",
                      "bright_cyan", "bright_white")]

    sections.append(("Light  |  Background Ramp", [light_bg]))
    sections.append(("Light  |  Foreground Ramp + Utility", [light_fg + light_utility]))
    sections.append(("Light  |  Core Colors", [light_core]))
    sections.append(("Light  |  ANSI 16", [l_ansi_normal, l_ansi_bright]))

    # -- Layout calculation --
    # Find max columns across all rows to set figure width
    max_cols = max(
        len(row) for _, rows in sections for row in rows
    )
    fig_w = max(max_cols * 0.95, 8.0)

    # Calculate total height
    total_h = 0.3  # top margin
    for _, rows in sections:
        total_h += section_gap  # section label
        total_h += len(rows) * (cell_h + row_gap)
    total_h += 0.3  # bottom margin

    fig, ax = plt.subplots(figsize=(fig_w, total_h))
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, total_h)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#F5F5F5")

    # Draw top-down
    y = total_h - 0.3
    for title, rows in sections:
        y -= section_gap
        _section_label(ax, y, title)
        for row in rows:
            y -= cell_h + row_gap
            cell_w = min((fig_w - 0.2) / len(row), 1.4) if row else 1.0
            _draw_row(ax, y, row, cell_w, cell_h, x_start=0.1)

    fig.savefig(str(output), dpi=dpi, bbox_inches="tight",
                pad_inches=0.15, facecolor=fig.get_facecolor())
    plt.close(fig)
