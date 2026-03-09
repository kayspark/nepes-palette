from pathlib import Path
from ..runner import TapeBuilder, register_tape, vhs_theme_for

@register_tape("gitui")
def gitui_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(output=str(output_dir / f"{theme}.gif"))
    tb.set("Theme", vhs_theme_for(theme))
    tb.hide()
    tb.type("cd ~/workspace/colorscheme/nepes-palette")
    tb.enter()
    tb.sleep(0.5)
    tb.type(f"GITUI_THEME=~/workspace/colorscheme/gitui-nepes/nepes-{theme}.ron gitui")
    tb.enter()
    tb.sleep(2)
    tb.show()
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.sleep(1)
    tb.type("q")
    return tb.build()
