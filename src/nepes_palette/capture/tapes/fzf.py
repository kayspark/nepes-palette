from pathlib import Path
from ..runner import TapeBuilder, register_tape

@register_tape("fzf")
def fzf_tape(theme: str, output_dir: Path) -> str:
    tb = TapeBuilder(width=120, height=35, output=str(output_dir / f"{theme}.gif"))
    tb.hide()
    tb.type(f"source ~/workspace/colorscheme/fzf-nepes/nepes-{theme}.sh")
    tb.enter()
    tb.sleep(0.5)
    tb.show()
    tb.type("find ~/workspace/colorscheme -name '*.py' | fzf --preview 'bat --color=always {}'")
    tb.enter()
    tb.sleep(2)
    tb.type("palette")
    tb.sleep(1)
    tb.screenshot(str(output_dir / f"{theme}.png"))
    tb.ctrl("c")
    return tb.build()
