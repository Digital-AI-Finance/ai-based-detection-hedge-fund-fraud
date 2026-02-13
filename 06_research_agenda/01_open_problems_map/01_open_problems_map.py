#!/usr/bin/env python3
"""Open Problems Map -- Section 06 Research Agenda.

Grouped visualization of 10 open problems in 3 colour-coded categories
using a horizontal layout with category headers.
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
categories = [
    {
        "name": "Data Challenges",
        "color": mlblue,
        "problems": [
            ("OP1", "Benchmark Datasets"),
            ("OP2", "Cross-Jurisdictional Transfer"),
            ("OP3", "Real-Time Pipelines"),
        ],
    },
    {
        "name": "Methodological",
        "color": mlpurple,
        "problems": [
            ("OP4", "Class Imbalance"),
            ("OP5", "Cold-Start Detection"),
            ("OP6", "Concept Drift Adaptation"),
            ("OP7", "Multi-Modal Fusion"),
        ],
    },
    {
        "name": "Deployment",
        "color": mlorange,
        "problems": [
            ("OP8", "Adversarial Robustness"),
            ("OP9", "Explainability Standards"),
            ("OP10", "Human-AI Collaboration"),
        ],
    },
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 4.5)
ax.axis("off")

y_header = 3.8
y_start = 3.0
row_height = 0.75

for cat_idx, cat in enumerate(categories):
    x_center = cat_idx * 3.5 + 1.5

    # Category header box
    header_box = mpatches.FancyBboxPatch(
        (x_center - 1.45, y_header - 0.22), 2.9, 0.50,
        boxstyle="round,pad=0.08",
        facecolor=cat["color"],
        edgecolor="white",
        linewidth=1.5,
    )
    ax.add_patch(header_box)
    ax.text(x_center, y_header + 0.02, cat["name"],
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="white")

    # Problem items
    for p_idx, (op_id, op_name) in enumerate(cat["problems"]):
        y = y_start - p_idx * row_height

        # Item box
        item_box = mpatches.FancyBboxPatch(
            (x_center - 1.40, y - 0.22), 2.8, 0.50,
            boxstyle="round,pad=0.06",
            facecolor=cat["color"],
            alpha=0.10,
            edgecolor=cat["color"],
            linewidth=1,
        )
        ax.add_patch(item_box)

        # OP id badge
        badge = mpatches.FancyBboxPatch(
            (x_center - 1.30, y - 0.15), 0.55, 0.35,
            boxstyle="round,pad=0.04",
            facecolor=cat["color"],
            alpha=0.85,
            edgecolor="white",
            linewidth=0.5,
        )
        ax.add_patch(badge)
        ax.text(x_center - 1.025, y + 0.02, op_id,
                ha="center", va="center", fontsize=7.5,
                fontweight="bold", color="white")

        ax.text(x_center - 0.55, y + 0.02, op_name,
                ha="left", va="center", fontsize=8.5,
                color="#222222")

ax.set_title("Open Research Problems",
             fontsize=13, fontweight="bold", pad=15, color="#222222",
             y=1.02)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_open_problems_map.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
