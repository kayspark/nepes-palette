from pathlib import Path
from ..runner import TapeBuilder, register_tape, vhs_theme_for

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("emacs")
def emacs_tape(theme: str, output_dir: Path) -> str:
    variant = "dark" if theme == "dark" else "light"
    tb = TapeBuilder(output=str(output_dir / f"{theme}.gif"))
    tb.set("Theme", vhs_theme_for(theme))
    tb.type(
        f"emacs -nw -Q -l nepes-{variant}-theme.el "
        f"--eval '(load-theme (quote nepes-{variant}) t)' "
        f"{SAMPLES_DIR}/showcase.py"
    )
    tb.enter()
    tb.sleep(4)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.sleep(1)
    tb.ctrl("x")
    tb.ctrl("c")
    return tb.build()
