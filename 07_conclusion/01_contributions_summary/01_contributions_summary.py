#!/usr/bin/env python3
"""Contributions Summary -- Section 07 Conclusion.

Three-panel horizontal layout showing the paper's three key contributions
with large text numbers and coloured panels.
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

# -- panel data ---------------------------------------------------------------
panels = [
    {
        "label": "C1",
        "title": "Pipeline Taxonomy",
        "icon": "\u2699",          # gear
        "number": "5",
        "unit": "Stages",
        "color": mlblue,
    },
    {
        "label": "C2",
        "title": "Adversarial Assessment",
        "icon": "\u26A0",          # warning / shield
        "number": "10.6%",
        "unit": "AUC Degradation",
        "color": mlpurple,
    },
    {
        "label": "C3",
        "title": "Research Roadmap",
        "icon": "\u2691",          # flag / map
        "number": "10",
        "unit": "Open Problems",
        "color": mllavender,
    },
]

# -- figure -------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))

for ax, panel in zip(axes, panels):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Background panel
    bg = mpatches.FancyBboxPatch(
        (0.05, 0.05), 0.90, 0.90,
        boxstyle="round,pad=0.05",
        facecolor=panel["color"],
        alpha=0.12,
        edgecolor=panel["color"],
        linewidth=2,
    )
    ax.add_patch(bg)

    # Contribution label badge
    badge = mpatches.FancyBboxPatch(
        (0.05, 0.82), 0.20, 0.14,
        boxstyle="round,pad=0.03",
        facecolor=panel["color"],
        edgecolor="white",
        linewidth=1,
    )
    ax.add_patch(badge)
    ax.text(0.15, 0.89, panel["label"], ha="center", va="center",
            fontsize=9, fontweight="bold", color="white")

    # Title
    ax.text(0.50, 0.75, panel["title"], ha="center", va="center",
            fontsize=10, fontweight="bold", color=panel["color"])

    # Large number
    text_color = "#222222" if panel["color"] == mllavender else panel["color"]
    ax.text(0.50, 0.48, panel["number"], ha="center", va="center",
            fontsize=32, fontweight="bold", color=text_color)

    # Unit label
    ax.text(0.50, 0.22, panel["unit"], ha="center", va="center",
            fontsize=10, color="#555555")

fig.suptitle("Key Contributions",
             fontsize=13, fontweight="bold", y=1.02, color="#222222")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_contributions_summary.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
