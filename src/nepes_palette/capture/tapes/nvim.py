from pathlib import Path
from ..runner import TapeBuilder, register_tape

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("nvim")
def nvim_tape(theme: str, output_dir: Path) -> str:
    bg = "dark" if theme == "dark" else "light"
    tb = TapeBuilder(output=str(output_dir / f"{theme}.gif"))
    tb.type(f"nvim -c 'set background={bg}' -c 'colorscheme nepes' {SAMPLES_DIR}/showcase.py")
    tb.enter()
    tb.sleep(3)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.sleep(1)
    tb.type("gg")
    tb.sleep(0.5)
    tb.type("G")
    tb.sleep(0.5)
    tb.type(":q!")
    tb.enter()
    return tb.build()
