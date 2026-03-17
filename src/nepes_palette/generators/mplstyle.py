"""Generate matplotlib style files from the nepes palette."""


def generate_mplstyle(palette: dict, theme: str) -> str:
    """Generate a .mplstyle file for matplotlib."""
    t = palette[theme]
    bases = t["chart_bases"]
    midtones = t["chart_midtones"]
    # 12-color cycle: 6 bases then 6 midtones
    cycle = bases + midtones
    cycle_str = ", ".join(f"'{c}'" for c in cycle)

    if theme == "dark":
        return f"""\
# Nepes Dark — matplotlib style
# Install: cp to ~/.config/matplotlib/stylelib/nepes-dark.mplstyle
# Use: plt.style.use('nepes-dark')

axes.prop_cycle: cycler('color', [{cycle_str}])
axes.facecolor: {t["bg"]}
axes.edgecolor: {t["fg_muted"]}
axes.labelcolor: {t["fg"]}
axes.grid: True

figure.facecolor: {t["bg"]}
figure.edgecolor: {t["bg"]}

text.color: {t["fg"]}

xtick.color: {t["fg_dim"]}
ytick.color: {t["fg_dim"]}

grid.color: {t["bg_hl"]}
grid.alpha: 0.8
grid.linestyle: --

legend.facecolor: {t["bg_alt"]}
legend.edgecolor: {t["border"]}
legend.framealpha: 0.9

savefig.facecolor: {t["bg"]}
savefig.edgecolor: {t["bg"]}
"""
    else:
        return f"""\
# Nepes Light — matplotlib style
# Install: cp to ~/.config/matplotlib/stylelib/nepes-light.mplstyle
# Use: plt.style.use('nepes-light')

axes.prop_cycle: cycler('color', [{cycle_str}])
axes.facecolor: white
axes.edgecolor: {t["fg_subtle"]}
axes.labelcolor: {t["fg"]}
axes.grid: True

figure.facecolor: white
figure.edgecolor: white

text.color: {t["fg"]}

xtick.color: {t["fg_dim"]}
ytick.color: {t["fg_dim"]}

grid.color: {t["bg_alt"]}
grid.alpha: 0.8
grid.linestyle: --

legend.facecolor: white
legend.edgecolor: {t["border"]}
legend.framealpha: 0.9

savefig.facecolor: white
savefig.edgecolor: white
"""
