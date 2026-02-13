#!/usr/bin/env python3
"""Literature Search Funnel -- Section 08 Reproducibility.

PRISMA-style funnel diagram showing descending stages of literature
screening from 500 initial publications to 105 final corpus.
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- data ---------------------------------------------------------------------
stages = [
    ("Initial Publications", 500),
    ("Full-Text Review", 120),
    ("Core Papers", 80),
    ("+ Contextual", 25),
    ("Final Corpus", 105),
]

# Widths proportional to count (normalized)
max_count = 500
colors = [mllavender, mlblue, mlpurple, mlorange, mlgreen]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 5.5))
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, len(stages) + 0.5)
ax.axis("off")

y_positions = list(reversed(range(len(stages))))
bar_height = 0.65

for i, ((label, count), y, color) in enumerate(zip(stages, y_positions, colors)):
    # Width proportional to count, minimum width for visibility
    width = max(1.5, (count / max_count) * 8.0)
    x_center = 5.0
    x_left = x_center - width / 2

    # Draw bar (trapezoid effect via rounded rectangle)
    bar = mpatches.FancyBboxPatch(
        (x_left, y - bar_height / 2), width, bar_height,
        boxstyle="round,pad=0.08",
        facecolor=color,
        edgecolor="white",
        linewidth=2,
    )
    ax.add_patch(bar)

    # Count label inside bar
    text_color = "white" if color in (mlblue, mlpurple, mlgreen) else "#222222"
    ax.text(x_center, y + 0.02, f"{count}",
            ha="center", va="center",
            fontsize=16, fontweight="bold", color=text_color)

    # Stage label to the right
    ax.text(x_center + width / 2 + 0.3, y + 0.02, label,
            ha="left", va="center",
            fontsize=9.5, color="#333333")

    # Connecting arrow between stages (except last)
    if i < len(stages) - 1:
        next_y = y_positions[i + 1]
        ax.annotate("", xy=(x_center, next_y + bar_height / 2 + 0.05),
                     xytext=(x_center, y - bar_height / 2 - 0.05),
                     arrowprops=dict(arrowstyle="->", color="#999999",
                                     linewidth=1.2))

ax.set_title("Literature Search Funnel",
             fontsize=13, fontweight="bold", pad=12, color="#222222")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_search_funnel.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
