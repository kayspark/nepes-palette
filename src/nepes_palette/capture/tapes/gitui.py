from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("gitui")
def gitui_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35, output=str(output_dir / f"{theme}.gif"))
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
