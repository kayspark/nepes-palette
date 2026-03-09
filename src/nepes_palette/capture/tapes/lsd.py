from pathlib import Path
from ..runner import TapeBuilder, register_tape, vhs_theme_for

@register_tape("lsd")
def lsd_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder()
    tb.set("Theme", vhs_theme_for(theme))
    tb.type("lsd -la --color=always ~/workspace/colorscheme/")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
