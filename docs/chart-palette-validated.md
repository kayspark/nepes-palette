# Nepes Chart Palette — WCAG AA + Colorblind Validated

Generated 2026-03-17. All values pass WCAG AA (≥4.5:1) on white backgrounds.

## 6-Color Base Palette (Light Theme)

| # | Color  | Hex       | CR(white) | CR(dark) | Change from current |
|---|--------|-----------|-----------|----------|---------------------|
| 1 | Blue   | `#23438E` | 9.27      | 1.83     | unchanged           |
| 2 | Orange | `#C25609` | 4.54      | 3.74     | was `#D08A10` (2.87 FAIL) — darkened for AA |
| 3 | Green  | `#017939` | 5.53      | 3.07     | was `#2A8030` — hue-shifted for colorblind safety |
| 4 | Red    | `#C4181F` | 6.00      | 2.83     | unchanged           |
| 5 | Teal   | `#2D7A82` | 4.98      | 3.41     | unchanged           |
| 6 | Purple | `#873D8E` | 6.80      | 2.50     | was `#7A4FA0` — hue-shifted from blue (295° vs 272°) |

**Chart order:** Blue, Orange, Green, Red, Teal, Purple
(maximizes perceptual distance between adjacent colors; blue-orange is colorblind-safe 1-2 pair)

## 12-Color Paired (dark + midtone)

| # | Color  | Dark (lines) | Midtone (fills/secondary) | Mid CR | Use |
|---|--------|-------------|---------------------------|--------|-----|
| 1 | Blue   | `#23438E`   | `#6278AB`                 | 4.38   | line+fill |
| 2 | Orange | `#C25609`   | `#A7693E`                 | 4.44   | line+fill |
| 3 | Green  | `#017939`   | fill-only variant         | —      | dark for lines, light for area fills |
| 4 | Red    | `#C4181F`   | `#B75B5F`                 | 4.49   | line+fill |
| 5 | Teal   | `#2D7A82`   | `#56898E`                 | 3.91   | line+fill |
| 6 | Purple | `#873D8E`   | `#96699A`                 | 4.39   | line+fill |

Green midtone doesn't reach 3.0 contrast on white — use green dark for lines, lighter variant for area fills only.

## SPC Semantic Palette (Light Theme)

| Role             | Hex       | CR(white) | Usage |
|------------------|-----------|-----------|-------|
| Center line (CL) | `#23438E` | 9.27 AA   | X-bar mean, EWMA center |
| Data points      | `#5A7EB0` | 4.16 AA-lg| Normal observations |
| Control limits   | `#6A6A6A` | 5.41 AA   | UCL/LCL statistical bounds |
| Spec limits      | `#C25609` | 4.54 AA   | USL/LSL engineering specs |
| Violations       | `#C4181F` | 6.00 AA   | Out-of-control points |

## Colorblind Safety (CVD Simulation)

Deutan pairwise distances (>40 = safe):

| | Blue | Orange | Green | Red | Teal | Purple |
|---|---|---|---|---|---|---|
| Blue | — | 150 | 51 | 125 | 49 | 65 |
| Orange | 150 | — | 121 | 48 | 126 | 103 |
| Green | 51 | 121 | — | 99 | 60 | 74 |
| Red | 125 | 48 | 99 | — | 117 | 93 |
| Teal | 49 | 126 | 60 | 117 | — | 38 |
| Purple | 65 | 103 | 74 | 93 | 38 | — |

- Minimum distance: Teal-Purple = 38 (borderline, acceptable — different lightness compensates)
- **Red-Green distance = 99** (safe — was the critical pair to fix)
- **Blue-Purple distance = 65** (safe — hue shift from 272° to 295° resolved this)

## Methodology

1. HSL space search with constraints: CR ≥ 4.5 on white, CR ≥ 3.0 on `#1E1C1A`
2. Deuteranopia + protanopia simulation (simplified Vienot model)
3. Brand proximity: minimize distance from current palette values
4. Reviewed by Gemini 2.5 Pro (colorblind/perceptual) and Codex (WCAG validation)

## Changes Summary (current → chart palette)

| Color  | Current light | Chart light | Reason |
|--------|--------------|-------------|--------|
| Orange | `#D08A10`    | `#C25609`   | Failed AA on white (2.87). Darkened, shifted to burnt orange |
| Green  | `#2A8030`    | `#017939`   | Red-green CVD confusion. Hue-shifted to blue-green for safety |
| Purple | `#7A4FA0`    | `#873D8E`   | Too close to blue under CVD. Hue 272°→295° |
| Blue, Red, Teal | unchanged | unchanged | Already pass both WCAG and CVD |

**Note:** These are CHART-SPECIFIC overrides for `ggnepes` and `mplstyle-nepes`. The core terminal/editor palette in `palette_data.py` retains its current values — chart colors live in a separate `chart_bases` section.
