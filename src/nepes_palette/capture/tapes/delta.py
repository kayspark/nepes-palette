from pathlib import Path
from ..runner import TapeBuilder, register_tape

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("delta")
def delta_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35)
    tb.hide()
    tb.type("export GIT_PAGER='delta --dark'") if theme == "dark" else tb.type("export GIT_PAGER='delta --light'")
    tb.enter()
    tb.sleep(0.5)
    tb.show()
    tb.type(f"cat {SAMPLES_DIR}/showcase.diff | delta")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
