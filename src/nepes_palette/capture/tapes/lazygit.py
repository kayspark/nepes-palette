from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("lazygit")
def lazygit_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35, output=str(output_dir / f"{theme}.gif"))
    tb.hide()
    tb.type("cd ~/workspace/colorscheme/nepes-palette")
    tb.enter()
    tb.sleep(0.5)
    tb.type(f"LG_CONFIG_FILE=~/workspace/colorscheme/lazygit-nepes/nepes-{theme}.yml lazygit")
    tb.enter()
    tb.sleep(2)
    tb.show()
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.sleep(1)
    tb.type("2")
    tb.sleep(1)
    tb.type("q")
    return tb.build()
