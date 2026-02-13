#!/usr/bin/env python3
"""Priority Matrix -- Section 06 Research Agenda.

Scatter plot: Feasibility (x) vs Impact (y) for 10 open problems,
coloured by category. Quadrant lines at (3, 3).
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- data ---------------------------------------------------------------------
# (label, feasibility, impact, category_color, category_name)
problems = [
    ("OP1",  3, 5, mlblue,   "Data"),
    ("OP2",  2, 4, mlblue,   "Data"),
    ("OP3",  4, 3, mlblue,   "Data"),
    ("OP4",  3, 5, mlpurple, "Method"),
    ("OP5",  4, 3, mlpurple, "Method"),
    ("OP6",  3, 4, mlpurple, "Method"),
    ("OP7",  3, 4, mlpurple, "Method"),
    ("OP8",  2, 5, mlorange, "Deploy"),
    ("OP9",  3, 4, mlorange, "Deploy"),
    ("OP10", 2, 4, mlorange, "Deploy"),
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5.5))

# Quadrant shading
ax.axhspan(3, 5.7, xmin=(3 - 0.7) / (5.3 - 0.7), xmax=1.0,
           color=mlgreen, alpha=0.06, zorder=0)

# Quadrant lines
ax.axvline(x=3, color="#bbbbbb", linestyle="--", linewidth=1)
ax.axhline(y=3, color="#bbbbbb", linestyle="--", linewidth=1)

# Quadrant labels
ax.text(1.3, 5.35, "High Impact\nLow Feasibility", fontsize=7,
        color="#999999", ha="center", style="italic")
ax.text(4.5, 5.35, "HIGH PRIORITY", fontsize=8,
        color=mlgreen, ha="center", fontweight="bold")
ax.text(1.3, 1.4, "Low Priority", fontsize=7,
        color="#999999", ha="center", style="italic")
ax.text(4.5, 1.4, "Quick Wins", fontsize=7,
        color="#999999", ha="center", style="italic")

# Plot points
for label, feas, impact, color, cat in problems:
    ax.scatter(feas, impact, s=160, c=[color], edgecolors="white",
              linewidth=1.2, zorder=5)
    # Smart offset to reduce overlap
    dx, dy = 0.15, 0.15
    if label == "OP4":
        dx, dy = -0.20, 0.18
    elif label == "OP1":
        dx, dy = 0.18, -0.20
    elif label == "OP8":
        dx, dy = -0.22, 0.15
    elif label == "OP10":
        dx, dy = -0.22, -0.15
    elif label == "OP7":
        dx, dy = 0.18, -0.15
    ax.annotate(label, (feas, impact),
                xytext=(feas + dx, impact + dy),
                fontsize=8, fontweight="bold", color="#333333")

# Legend
from matplotlib.patches import Patch
legend_items = [
    Patch(facecolor=mlblue, edgecolor="white", label="Data Challenges"),
    Patch(facecolor=mlpurple, edgecolor="white", label="Methodological"),
    Patch(facecolor=mlorange, edgecolor="white", label="Deployment"),
]
ax.legend(handles=legend_items, loc="lower right", fontsize=8, frameon=True,
          framealpha=0.9, edgecolor="#cccccc")

ax.set_xlabel("Feasibility (1 = difficult, 5 = achievable)",
              fontsize=9, color="#333333")
ax.set_ylabel("Impact (1 = minor, 5 = transformative)",
              fontsize=9, color="#333333")
ax.set_xlim(0.7, 5.3)
ax.set_ylim(0.7, 5.7)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_title("Research Priority Matrix",
             fontsize=12, fontweight="bold", pad=10, color="#222222")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=8)
ax.grid(alpha=0.15, linewidth=0.5)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_priority_matrix.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
