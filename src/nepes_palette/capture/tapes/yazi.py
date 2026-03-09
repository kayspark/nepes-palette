from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("yazi")
def yazi_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35, output=str(output_dir / f"{theme}.gif"))
    tb.hide()
    tb.type("cd ~/workspace/colorscheme/")
    tb.enter()
    tb.sleep(0.5)
    tb.show()
    tb.type("yazi")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.sleep(1)
    tb.type("q")
    return tb.build()
