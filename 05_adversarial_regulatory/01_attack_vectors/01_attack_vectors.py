#!/usr/bin/env python3
"""Adversarial Attack Vectors -- Section 05 Adversarial & Regulatory.

Four-quadrant diagram showing attack vectors with colour-coded quadrants,
key statistics, and brief descriptions.
"""

import pathlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- quadrant data ------------------------------------------------------------
quadrants = [
    {
        "title": "Data Poisoning",
        "stat": "5\u201312% degradation",
        "desc": "Corrupt training data to\nweaken model accuracy",
        "color": mlred,
        "xy": (0.25, 0.75),
    },
    {
        "title": "Evasion Attacks",
        "stat": "10.6% mean AUC drop",
        "desc": "Craft inputs that bypass\ntrained classifiers",
        "color": mlorange,
        "xy": (0.75, 0.75),
    },
    {
        "title": "Model Extraction",
        "stat": "Reverse engineering",
        "desc": "Query model to reconstruct\ndecision boundaries",
        "color": mlpurple,
        "xy": (0.25, 0.25),
    },
    {
        "title": "Strategic Timing",
        "stat": "Regime exploitation",
        "desc": "Exploit market regime\ntransitions to evade detection",
        "color": mlblue,
        "xy": (0.75, 0.25),
    },
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5.5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Draw quadrant backgrounds
for q in quadrants:
    x, y = q["xy"]
    rect_x = 0.02 if x < 0.5 else 0.52
    rect_y = 0.02 if y < 0.5 else 0.52
    rect = mpatches.FancyBboxPatch(
        (rect_x, rect_y), 0.46, 0.46,
        boxstyle="round,pad=0.02",
        facecolor=q["color"],
        alpha=0.12,
        edgecolor=q["color"],
        linewidth=1.5,
    )
    ax.add_patch(rect)

# Draw content in each quadrant
for q in quadrants:
    x, y = q["xy"]
    ax.text(x, y + 0.10, q["title"], ha="center", va="center",
            fontsize=12, fontweight="bold", color=q["color"])
    ax.text(x, y + 0.01, q["stat"], ha="center", va="center",
            fontsize=10, fontweight="bold", color="#222222")
    ax.text(x, y - 0.10, q["desc"], ha="center", va="center",
            fontsize=8, color="#555555", linespacing=1.4)

# Center label
center_box = mpatches.FancyBboxPatch(
    (0.35, 0.42), 0.30, 0.16,
    boxstyle="round,pad=0.03",
    facecolor="white",
    edgecolor="#333333",
    linewidth=2,
    zorder=10,
)
ax.add_patch(center_box)
ax.text(0.50, 0.50, "Adversarial\nThreats", ha="center", va="center",
        fontsize=11, fontweight="bold", color="#222222", zorder=11)

# Divider lines
ax.plot([0.50, 0.50], [0.02, 0.40], color="#cccccc", linewidth=1, ls="--")
ax.plot([0.50, 0.50], [0.60, 0.98], color="#cccccc", linewidth=1, ls="--")
ax.plot([0.02, 0.33], [0.50, 0.50], color="#cccccc", linewidth=1, ls="--")
ax.plot([0.67, 0.98], [0.50, 0.50], color="#cccccc", linewidth=1, ls="--")

ax.set_title("Adversarial Attack Vectors",
             fontsize=13, fontweight="bold", pad=12, color="#222222")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_attack_vectors.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
