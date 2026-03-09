from pathlib import Path
from ..runner import TapeBuilder, register_tape

SAMPLES_DIR = Path(__file__).parent.parent.parent.parent.parent / "captures" / "samples"

@register_tape("tmux")
def tmux_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder()
    tb.hide()
    tb.type("tmux new-session -d -s capture")
    tb.enter()
    tb.sleep(1)
    tb.type("tmux send-keys -t capture 'bat " + str(SAMPLES_DIR) + "/showcase.py' Enter")
    tb.enter()
    tb.sleep(1)
    tb.type("tmux attach -t capture")
    tb.enter()
    tb.sleep(2)
    tb.show()
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.hide()
    tb.ctrl("b")
    tb.type("d")
    tb.sleep(0.5)
    tb.type("tmux kill-session -t capture")
    tb.enter()
    return tb.build()
