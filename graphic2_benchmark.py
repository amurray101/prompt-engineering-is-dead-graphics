#!/usr/bin/env python3
"""Graphic 2: IFEval Benchmark Chart for 'Prompt Engineering Is Dead' article."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Design Tokens (matching Graphic 1) ---
BG_COLOR = '#FAFAFA'
TEXT_PRIMARY = '#1A1A1A'       # near-black
TEXT_SECONDARY = '#6B6B6B'     # muted gray
TEXT_DIMMED = '#AAAAAA'        # dimmer gray
ACCENT_GLOW = '#C4882D'       # warm gold (deeper for light bg)
BAR_DEFAULT = '#D0D0D0'       # muted bars
BAR_RISING = '#B8B8B8'        # slightly darker mid-bars
GRID_COLOR = '#E8E8E8'
FONT = 'Helvetica Neue'

# --- Data ---
models = ['Claude 2', 'Claude 3\nOpus', 'Claude 3.5\nSonnet', 'Claude 3.5\nSonnet v2', 'Claude\nOpus 4']
scores = [35, 60, 71, 79, 88]
bar_colors = ['#D0D0D0', '#BFBFBF', '#ABABAB', '#969696', ACCENT_GLOW]

# --- Figure Setup ---
fig, ax = plt.subplots(1, 1, figsize=(12, 6.28), dpi=100)
fig.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)

# --- Title ---
fig.text(0.5, 0.93, 'Instruction Following Over Time',
         fontsize=22, fontweight='bold', color=TEXT_PRIMARY,
         ha='center', va='center', fontfamily=FONT)
fig.text(0.5, 0.885, 'How well models do what you actually asked',
         fontsize=12, color=TEXT_SECONDARY,
         ha='center', va='center', fontfamily=FONT)

# --- Bars ---
x = np.arange(len(models))
bar_width = 0.55

bars = ax.bar(x, scores, bar_width, color=bar_colors, zorder=3,
              edgecolor='none')

# Round the top of bars
for bar in bars:
    bar.set_linewidth(0)

# Glow effect on last bar
last_bar = bars[-1]
glow_rect = patches.FancyBboxPatch(
    (last_bar.get_x() - 0.05, 0),
    last_bar.get_width() + 0.1,
    scores[-1],
    boxstyle="round,pad=0.02",
    facecolor=ACCENT_GLOW,
    alpha=0.08,
    zorder=2
)
ax.add_patch(glow_rect)

# --- Score labels on bars ---
for i, (bar, score) in enumerate(zip(bars, scores)):
    color = TEXT_PRIMARY if i == len(bars) - 1 else TEXT_SECONDARY
    fontweight = 'bold' if i == len(bars) - 1 else 'normal'
    fontsize = 15 if i == len(bars) - 1 else 13
    ax.text(bar.get_x() + bar.get_width() / 2, score + 1.5,
            f'{score}%',
            ha='center', va='bottom',
            fontsize=fontsize, fontweight=fontweight,
            color=color, fontfamily=FONT)

# --- Axes styling ---
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=10, color=TEXT_SECONDARY,
                    fontfamily=FONT, linespacing=1.2)
ax.set_ylabel('Instruction Following Accuracy (IFEval)',
              fontsize=10, color=TEXT_SECONDARY, fontfamily=FONT,
              labelpad=10)
ax.set_xlabel('Model Generation',
              fontsize=10, color=TEXT_SECONDARY, fontfamily=FONT,
              labelpad=10)

# Y-axis
ax.set_ylim(0, 100)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.tick_params(axis='y', colors=TEXT_DIMMED, labelsize=9)
ax.tick_params(axis='x', colors=TEXT_DIMMED, length=0, pad=8)

# Grid
ax.yaxis.grid(True, color=GRID_COLOR, linewidth=0.5, zorder=0)
ax.set_axisbelow(True)

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

# --- Footnote ---
fig.text(0.5, 0.03,
         'Source: Anthropic model cards (approximate scores)',
         fontsize=8, color=TEXT_DIMMED,
         ha='center', va='center', fontfamily=FONT,
         style='italic')

# --- Layout ---
plt.subplots_adjust(top=0.82, bottom=0.18, left=0.1, right=0.95)

# --- Export ---
output_path = '/Users/alexamurray/Documents/New project/.claude/worktrees/goofy-cori/graphic2_benchmark.png'
plt.savefig(output_path, dpi=100, facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"Saved: {output_path}")
