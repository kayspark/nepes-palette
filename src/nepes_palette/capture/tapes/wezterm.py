from pathlib import Path
from ..runner import TapeBuilder, register_tape

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("wezterm")
def wezterm_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35)
    tb.type(f"bat --theme='ansi' {SAMPLES_DIR}/showcase.py")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
