#!/usr/bin/env python3
"""Graphic 1: Three-Era Timeline for 'Prompt Engineering Is Dead' article."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# --- Design Tokens ---
BG_COLOR = '#FAFAFA'
CARD_BG = '#F0F0F0'
TEXT_PRIMARY = '#1A1A1A'       # near-black
TEXT_SECONDARY = '#6B6B6B'     # muted gray
TEXT_DIMMED = '#AAAAAA'        # dimmer gray for past eras
ACCENT = '#1A1A1A'            # dark accent for "Today"
ACCENT_GLOW = '#C4882D'       # warm gold (slightly deeper for light bg)
DIVIDER_COLOR = '#D0D0D0'
FONT = 'Helvetica Neue'

# --- Figure Setup (exact 1200x628) ---
fig, ax = plt.subplots(1, 1, figsize=(12, 6.28), dpi=100)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.set_xlim(0, 12)
ax.set_ylim(0, 6.28)
ax.axis('off')

# --- Title ---
ax.text(6, 5.45, 'The Evolution of AI Understanding',
        fontsize=22, fontweight='bold', color=TEXT_PRIMARY,
        ha='center', va='center', fontfamily=FONT)
ax.text(6, 5.05, 'From rigid pattern-matching to genuine comprehension',
        fontsize=12, color=TEXT_SECONDARY,
        ha='center', va='center', fontfamily=FONT)

# --- Timeline bar ---
bar_y = 3.3
bar_left = 1.5
bar_right = 10.5

# Draw thin timeline line
ax.plot([bar_left, bar_right], [bar_y, bar_y],
        color=DIVIDER_COLOR, linewidth=2, solid_capstyle='round')

# --- Three eras ---
eras = [
    {
        'x': 3.0,
        'time': '18 months ago',
        'label': 'Literal.\nRobotic.\nWrong room.',
        'dot_color': TEXT_DIMMED,
        'time_color': TEXT_DIMMED,
        'label_color': TEXT_DIMMED,
        'label_size': 13,
        'time_size': 10,
    },
    {
        'x': 6.0,
        'time': '6 months ago',
        'label': 'Warmer.\nStill needed\nnudging.',
        'dot_color': TEXT_SECONDARY,
        'time_color': TEXT_SECONDARY,
        'label_color': TEXT_SECONDARY,
        'label_size': 13,
        'time_size': 10,
    },
    {
        'x': 9.0,
        'time': 'Today',
        'label': 'Gets the\nsubtext.\nFirst try.',
        'dot_color': ACCENT_GLOW,
        'time_color': ACCENT_GLOW,
        'label_color': TEXT_PRIMARY,
        'label_size': 15,
        'time_size': 11,
    },
]

for era in eras:
    x = era['x']

    # Dot on timeline
    dot_size = 10 if era['time'] == 'Today' else 7
    ax.plot(x, bar_y, 'o', color=era['dot_color'], markersize=dot_size,
            zorder=5)

    # Glow effect for "Today"
    if era['time'] == 'Today':
        ax.plot(x, bar_y, 'o', color=ACCENT_GLOW, markersize=18,
                alpha=0.15, zorder=4)
        ax.plot(x, bar_y, 'o', color=ACCENT_GLOW, markersize=26,
                alpha=0.06, zorder=3)

    # Time label above
    ax.text(x, bar_y + 0.35, era['time'],
            fontsize=era['time_size'],
            fontweight='bold' if era['time'] == 'Today' else 'normal',
            color=era['time_color'],
            ha='center', va='bottom', fontfamily=FONT)

    # Description below
    ax.text(x, bar_y - 0.5, era['label'],
            fontsize=era['label_size'],
            fontweight='medium' if era['time'] == 'Today' else 'regular',
            color=era['label_color'],
            ha='center', va='top', fontfamily=FONT,
            linespacing=1.4)

# --- Subtle gradient arrow on timeline pointing right ---
arrow_x = bar_right + 0.15
ax.annotate('', xy=(arrow_x, bar_y), xytext=(arrow_x - 0.4, bar_y),
            arrowprops=dict(arrowstyle='->', color=TEXT_DIMMED, lw=1.5))

# --- Export ---
output_path = '/Users/alexamurray/Documents/New project/.claude/worktrees/goofy-cori/graphic1_timeline.png'
plt.savefig(output_path, dpi=100, facecolor=BG_COLOR, edgecolor='none')
plt.close()
print(f"Saved: {output_path}")
