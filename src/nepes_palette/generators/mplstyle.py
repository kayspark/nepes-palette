"""Generate matplotlib style files from the nepes palette."""


def _q(hex_color: str) -> str:
    """Quote a hex color for mplstyle format."""
    return f'"{hex_color}"'


def generate_mplstyle(palette: dict, theme: str) -> str:
    """Generate a .mplstyle file for matplotlib."""
    t = palette[theme]
    bases = t["chart_bases"]
    midtones = t["chart_midtones"]
    # 12-color cycle: 6 bases then 6 midtones
    cycle = bases + midtones
    # mplstyle cycler format: cycler('color', ['#hex', '#hex', ...])
    cycle_items = ", ".join(f'"{c}"' for c in cycle)

    label = "Dark" if theme == "dark" else "Light"
    bg = _q(t["bg"]) if theme == "dark" else "white"
    fg = _q(t["fg"])
    fg_dim = _q(t["fg_dim"])
    edge = _q(t["fg_muted"]) if theme == "dark" else _q(t["fg_subtle"])
    grid = _q(t["bg_hl"]) if theme == "dark" else _q(t["bg_alt"])
    legend_bg = _q(t["bg_alt"]) if theme == "dark" else "white"
    legend_edge = _q(t["border"])

    return f"""\
# Nepes {label} — matplotlib style
# Install: cp to ~/.config/matplotlib/stylelib/nepes-{theme}.mplstyle
# Use: plt.style.use('nepes-{theme}')

axes.prop_cycle: cycler('color', [{cycle_items}])
axes.facecolor: {bg}
axes.edgecolor: {edge}
axes.labelcolor: {fg}
axes.grid: True

figure.facecolor: {bg}
figure.edgecolor: {bg}

text.color: {fg}

xtick.color: {fg_dim}
ytick.color: {fg_dim}

grid.color: {grid}
grid.alpha: 0.8
grid.linestyle: --

legend.facecolor: {legend_bg}
legend.edgecolor: {legend_edge}
legend.framealpha: 0.9

savefig.facecolor: {bg}
savefig.edgecolor: {bg}
"""
