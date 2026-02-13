#!/usr/bin/env python3
"""Takeaways by Audience -- Section 07 Conclusion.

Matrix/grid: 3 audience groups (columns) x 3 key takeaways each (rows).
Clean table layout with colour-coded headers.
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

# -- data ---------------------------------------------------------------------
audiences = [
    {
        "name": "Practitioners",
        "color": mlblue,
        "takeaways": [
            "Ensemble methods deliver\nbest detection accuracy",
            "Multi-stage pipeline approach\nfor robust coverage",
            "Adversarial testing is\nessential before deployment",
        ],
    },
    {
        "name": "Regulators",
        "color": mlpurple,
        "takeaways": [
            "AI addresses the scale\nof modern surveillance",
            "Explainability requirements\nmust be mandated",
            "Federated learning enables\ncross-border collaboration",
        ],
    },
    {
        "name": "Researchers",
        "color": mlorange,
        "takeaways": [
            "Benchmark datasets are\nthe top priority gap",
            "Multi-modal fusion is\nan untapped opportunity",
            "Adversarial robustness\nneeds formal frameworks",
        ],
    },
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.set_xlim(0, 9)
ax.set_ylim(-0.5, 4.5)
ax.axis("off")

col_width = 2.8
col_gap = 0.15
x_start = 0.25

for col_idx, audience in enumerate(audiences):
    x = x_start + col_idx * (col_width + col_gap)
    color = audience["color"]

    # Header box
    header = mpatches.FancyBboxPatch(
        (x, 3.6), col_width, 0.55,
        boxstyle="round,pad=0.06",
        facecolor=color,
        edgecolor="white",
        linewidth=1.5,
    )
    ax.add_patch(header)
    ax.text(x + col_width / 2, 3.87, audience["name"],
            ha="center", va="center", fontsize=11,
            fontweight="bold", color="white")

    # Takeaway rows
    for row_idx, takeaway in enumerate(audience["takeaways"]):
        y = 2.7 - row_idx * 1.05

        row_box = mpatches.FancyBboxPatch(
            (x, y), col_width, 0.80,
            boxstyle="round,pad=0.05",
            facecolor=color,
            alpha=0.08,
            edgecolor=color,
            linewidth=0.8,
        )
        ax.add_patch(row_box)

        # Row number badge
        badge = mpatches.Circle(
            (x + 0.30, y + 0.40), 0.18,
            facecolor=color, alpha=0.7, edgecolor="white", linewidth=0.5,
        )
        ax.add_patch(badge)
        ax.text(x + 0.30, y + 0.40, str(row_idx + 1),
                ha="center", va="center", fontsize=8,
                fontweight="bold", color="white")

        ax.text(x + 0.65, y + 0.40, takeaway,
                ha="left", va="center", fontsize=8,
                color="#333333", linespacing=1.3)

ax.set_title("Key Takeaways by Audience",
             fontsize=13, fontweight="bold", pad=15, color="#222222",
             y=1.0)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_takeaways_by_audience.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
