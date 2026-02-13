#!/usr/bin/env python3
"""Boolean Query Structure -- Appendix A0 Search Protocol.

Venn-style diagram showing 3 query blocks combined with AND:
Financial Domain, Fraud Terms, AI/ML Methods.
Center intersection labelled 'Target Literature'.
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

# -- circle positions ---------------------------------------------------------
# Three circles arranged in a triangle pattern
centers = [
    (-0.55, 0.45),   # top-left: Financial Domain
    (0.55, 0.45),    # top-right: Fraud Terms
    (0.0, -0.45),    # bottom: AI/ML Methods
]

circle_data = [
    {
        "center": centers[0],
        "color": mlblue,
        "title": "Financial Domain",
        "terms": ['"hedge fund"', '"investment fund"', '"alternative investment"'],
    },
    {
        "center": centers[1],
        "color": mlpurple,
        "title": "Fraud Terms",
        "terms": ['"fraud"', '"manipulation"', '"anomaly"'],
    },
    {
        "center": centers[2],
        "color": mlgreen,
        "title": "AI / ML Methods",
        "terms": ['"machine learning"', '"deep learning"', '"neural network"'],
    },
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5.5))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.0, 2.2)
ax.set_aspect("equal")
ax.axis("off")

radius = 1.25

for cd in circle_data:
    cx, cy = cd["center"]
    circle = plt.Circle((cx, cy), radius, facecolor=cd["color"],
                         alpha=0.15, edgecolor=cd["color"],
                         linewidth=2)
    ax.add_patch(circle)

    # Title positioned outside the circle
    if cy > 0:
        ty = cy + radius + 0.25
    else:
        ty = cy - radius - 0.25

    if cx < 0:
        tx = cx - 0.3
    elif cx > 0:
        tx = cx + 0.3
    else:
        tx = cx

    ax.text(tx, ty, cd["title"], ha="center", va="center",
            fontsize=11, fontweight="bold", color=cd["color"])

    # Terms listed near the outer edge of each circle
    term_str = "\n".join(cd["terms"])
    if cy > 0:
        term_y = cy + 0.35
    else:
        term_y = cy - 0.35

    ax.text(cx, term_y, term_str, ha="center", va="center",
            fontsize=7.5, color="#444444", linespacing=1.5,
            fontstyle="italic")

# AND connectors
ax.text(-0.0, 1.55, "AND", ha="center", va="center",
        fontsize=9, fontweight="bold", color="#888888",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="#f0f0f0",
                  edgecolor="#cccccc"))
ax.text(-0.85, -0.15, "AND", ha="center", va="center",
        fontsize=9, fontweight="bold", color="#888888",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="#f0f0f0",
                  edgecolor="#cccccc"))
ax.text(0.85, -0.15, "AND", ha="center", va="center",
        fontsize=9, fontweight="bold", color="#888888",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="#f0f0f0",
                  edgecolor="#cccccc"))

# Center intersection label
ax.text(0.0, 0.12, "Target\nLiterature", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#222222",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="#333333", linewidth=1.5, alpha=0.9))

ax.set_title("Boolean Search Query Structure",
             fontsize=13, fontweight="bold", pad=15, color="#222222")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_boolean_query.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
