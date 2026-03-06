import argparse
import sys
from pathlib import Path

from .palette import load_palette
from .validate import validate_palette
from .harmony import analyze_harmony

PALETTE_PATH = Path(__file__).parent.parent.parent / "palette.toml"


def cmd_validate(args):
    palette = load_palette(args.palette)

    print("=== WCAG Contrast Check ===\n")
    results = validate_palette(palette)
    failures = [r for r in results if not r["aa"]]
    for r in results:
        status = "PASS" if r["aa"] else "FAIL"
        aaa = " (AAA)" if r["aaa"] else ""
        print(f"  [{status}] {r['theme']:5s} {r['role']:12s} {r['fg']} on {r['bg']}  ratio={r['ratio']}{aaa}")

    print(f"\n  {len(results) - len(failures)}/{len(results)} pass AA, {len(failures)} failures\n")

    print("=== Color Harmony ===\n")
    harmony = analyze_harmony(palette)

    hd = harmony["hue_distribution"]
    print(f"  Hue distribution (7 base colors):")
    print(f"    Gap variance: {hd['gap_variance']} (lower = more even)")
    print(f"    Min gap: {hd['min_gap']:.0f}°  Max gap: {hd['max_gap']:.0f}°  Ideal: {hd['ideal_gap']:.0f}°")

    sc = harmony["saturation_consistency"]
    print(f"\n  Saturation consistency:")
    print(f"    Mean: {sc['mean']}%  Std dev: {sc['std_dev']}%")

    lb = harmony["lightness_balance"]
    print(f"\n  Lightness balance:")
    for theme, data in lb.items():
        print(f"    {theme}: mean={data['mean_lightness']}%  std={data['std_dev']}%")

    if failures:
        print(f"\nWARNING: {len(failures)} color pairs fail WCAG AA contrast ratio (4.5:1)")
        sys.exit(1)


def cmd_swatch(args):
    from .swatch import render_swatch
    palette = load_palette(args.palette)
    output = args.output or "swatch.png"
    render_swatch(palette, output)
    print(f"Swatch saved to {output}")


def cmd_generate(args):
    from .generators import generate_all
    palette = load_palette(args.palette)
    output_dir = Path(args.output_dir) if args.output_dir else Path.cwd().parent
    generate_all(palette, output_dir)


def main():
    parser = argparse.ArgumentParser(prog="nepes-palette", description="Nepes colorscheme generator and validator")
    parser.add_argument("--palette", type=Path, default=PALETTE_PATH, help="Path to palette.toml")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Check WCAG contrast and color harmony")

    sw = sub.add_parser("swatch", help="Generate palette swatch image")
    sw.add_argument("-o", "--output", help="Output PNG path (default: swatch.png)")

    gen = sub.add_parser("generate", help="Generate tool-specific config files")
    gen.add_argument("-o", "--output-dir", help="Parent directory for generated repos (default: ..)")

    args = parser.parse_args()
    {"validate": cmd_validate, "swatch": cmd_swatch, "generate": cmd_generate}[args.command](args)


if __name__ == "__main__":
    main()
