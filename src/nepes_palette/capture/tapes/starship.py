from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("starship")
def starship_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=10)
    tb.hide()
    tb.type("cd ~/workspace/colorscheme/nepes-palette")
    tb.enter()
    tb.sleep(1)
    tb.show()
    tb.enter()
    tb.sleep(1)
    tb.type("git status")
    tb.enter()
    tb.sleep(1)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
