from pathlib import Path
from ..runner import TapeBuilder, register_tape

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("bat")
def bat_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder()
    tb.hide()
    tb.type(f"export BAT_THEME='Nepes {'Dark' if theme == 'dark' else 'Light'}'")
    tb.enter()
    tb.sleep(0.5)
    tb.show()
    tb.type(f"bat {SAMPLES_DIR}/showcase.py")
    tb.enter()
    tb.sleep(2)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    return tb.build()
