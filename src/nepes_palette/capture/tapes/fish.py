from pathlib import Path
from ..runner import TapeBuilder, register_tape, vhs_theme_for

@register_tape("fish")
def fish_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder()
    tb.set("Theme", vhs_theme_for(theme))
    tb.hide()
    tb.type("fish")
    tb.enter()
    tb.sleep(1)
    tb.type(f"source ~/workspace/colorscheme/fish-nepes/nepes-{theme}.fish")
    tb.enter()
    tb.sleep(0.5)
    tb.show()
    tb.type("echo 'Hello from fish shell' && ls -la && set -S")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.type("exit")
    tb.enter()
    return tb.build()
