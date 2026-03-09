import argparse
import sys
from pathlib import Path

from .palette import load_palette
from .validate import validate_palette
from .harmony import analyze_harmony


def cmd_validate(args):
    palette = load_palette()

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
    palette = load_palette()
    output = args.output or "swatch.png"
    render_swatch(palette, output)
    print(f"Swatch saved to {output}")


def cmd_generate(args):
    from .generators import generate_all
    palette = load_palette()
    output_dir = Path(args.output_dir) if args.output_dir else Path.cwd().parent
    generate_all(palette, output_dir)


def cmd_capture(args):
    from .capture.runner import (
        TOOL_REGISTRY, generate_tape, run_tape, get_tools_by_phase,
    )
    import nepes_palette.capture.tapes  # noqa: F401 — register all tape builders

    output_dir = Path(args.output_dir) if args.output_dir else Path.cwd().parent

    # Determine which tools to capture
    if args.tool:
        if args.tool not in TOOL_REGISTRY:
            print(f"Error: Unknown tool '{args.tool}'", file=sys.stderr)
            print(f"Available: {', '.join(sorted(TOOL_REGISTRY.keys()))}", file=sys.stderr)
            sys.exit(1)
        tools = [args.tool]
    elif args.phase:
        tools = get_tools_by_phase(args.phase)
        if not tools:
            print(f"Error: No tools for phase '{args.phase}'", file=sys.stderr)
            sys.exit(1)
    elif args.all:
        tools = list(TOOL_REGISTRY.keys())
    else:
        print("Error: Specify a tool name, --phase, or --all", file=sys.stderr)
        sys.exit(1)

    # Filter to VHS-phase tools only (browser/gui not yet implemented)
    vhs_tools = [t for t in tools if TOOL_REGISTRY[t]["phase"] == "vhs"]
    other_tools = [t for t in tools if TOOL_REGISTRY[t]["phase"] != "vhs"]

    if other_tools:
        print(f"  Skipping non-VHS tools (not yet implemented): {', '.join(other_tools)}")

    themes = [args.theme] if args.theme else ["dark", "light"]

    for tool in vhs_tools:
        repo_name = f"{tool}-nepes"
        docs_dir = output_dir / repo_name / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)

        for theme in themes:
            print(f"  Capturing {tool} ({theme})...")

            if args.dry_run:
                tape = generate_tape(tool, theme, docs_dir)
                tape_path = docs_dir / f"capture-{theme}.tape"
                tape_path.write_text(tape)
                print(f"    Tape written to {tape_path} (dry-run)")
            else:
                tape = generate_tape(tool, theme, docs_dir)
                tape_path = docs_dir / f"capture-{theme}.tape"
                try:
                    result = run_tape(tape, tape_path)
                    print(f"    Done: {docs_dir / f'{theme}.png'}")
                except FileNotFoundError as e:
                    print(f"    Error: {e}", file=sys.stderr)
                    sys.exit(1)
                except Exception as e:
                    print(f"    VHS failed: {e}", file=sys.stderr)
                    if hasattr(e, 'stderr'):
                        print(f"    {e.stderr}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(prog="nepes-palette", description="Nepes colorscheme generator and validator")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Check WCAG contrast and color harmony")

    sw = sub.add_parser("swatch", help="Generate palette swatch image")
    sw.add_argument("-o", "--output", help="Output PNG path (default: swatch.png)")

    gen = sub.add_parser("generate", help="Generate tool-specific config files")
    gen.add_argument("-o", "--output-dir", help="Parent directory for generated repos (default: ..)")

    cap = sub.add_parser("capture", help="Capture theme screenshots and GIFs via VHS")
    cap.add_argument("tool", nargs="?", help="Tool name (e.g., bat, nvim)")
    cap.add_argument("--all", action="store_true", help="Capture all tools")
    cap.add_argument("--phase", choices=["vhs", "browser", "gui"], help="Capture tools by phase")
    cap.add_argument("--theme", choices=["dark", "light"], help="Single theme (default: both)")
    cap.add_argument("-o", "--output-dir", help="Parent directory for sub-repos (default: ..)")
    cap.add_argument("--dry-run", action="store_true", help="Write .tape files without running VHS")

    args = parser.parse_args()
    {"validate": cmd_validate, "swatch": cmd_swatch, "generate": cmd_generate, "capture": cmd_capture}[args.command](args)


if __name__ == "__main__":
    main()
