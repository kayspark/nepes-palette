from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("lsd")
def lsd_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder()
    tb.type("lsd -la --color=always ~/workspace/colorscheme/")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
