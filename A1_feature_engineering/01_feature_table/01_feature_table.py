#!/usr/bin/env python3
"""Feature Engineering Table -- Appendix A1.

Enhanced table visualization of 5 feature categories with colour-coded
groups and feature counts displayed as horizontal grouped bars.
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
        "name": "Statistical",
        "color": mlblue,
        "count": 6,
        "features": [
            "Autocorrelation",
            "Sharpe ratio",
            "Max drawdown",
            "Kurtosis",
            "Skewness",
            "Hurst exponent",
        ],
    },
    {
        "name": "Benford's Law",
        "color": mlpurple,
        "count": 3,
        "features": [
            "First-digit chi-sq",
            "Second-digit test",
            "Summation test",
        ],
    },
    {
        "name": "Textual / NLP",
        "color": mlgreen,
        "count": 4,
        "features": [
            "Fog index",
            "Sentiment score",
            "Boilerplate deviation",
            "Topic drift",
        ],
    },
    {
        "name": "Network",
        "color": mlorange,
        "count": 3,
        "features": [
            "Degree centrality",
            "Betweenness",
            "Related-party count",
        ],
    },
    {
        "name": "Temporal",
        "color": mlred,
        "count": 3,
        "features": [
            "Regime probability",
            "Change-point score",
            "Calendar effect",
        ],
    },
]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-0.5, 10)
ax.set_ylim(-0.5, len(categories) + 0.5)
ax.axis("off")

bar_height = 0.60
max_count = max(c["count"] for c in categories)

for i, cat in enumerate(reversed(categories)):
    y = i
    color = cat["color"]

    # Category bar (width proportional to feature count)
    bar_width = (cat["count"] / max_count) * 4.5
    bar = mpatches.FancyBboxPatch(
        (0, y - bar_height / 2), bar_width, bar_height,
        boxstyle="round,pad=0.06",
        facecolor=color,
        alpha=0.85,
        edgecolor="white",
        linewidth=1.5,
    )
    ax.add_patch(bar)

    # Category name and count inside bar
    ax.text(bar_width / 2, y + 0.02,
            f"{cat['name']} ({cat['count']})",
            ha="center", va="center",
            fontsize=9.5, fontweight="bold", color="white")

    # Feature list to the right
    feature_str = ", ".join(cat["features"])
    ax.text(bar_width + 0.3, y + 0.02, feature_str,
            ha="left", va="center",
            fontsize=7.5, color="#444444")

# Total features annotation
total = sum(c["count"] for c in categories)
ax.text(5.0, len(categories) + 0.15,
        f"Total: {total} features across {len(categories)} categories",
        ha="center", va="center",
        fontsize=9, color="#666666",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8f8f8",
                  edgecolor="#cccccc", linewidth=0.8))

ax.set_title("Feature Engineering Categories",
             fontsize=13, fontweight="bold", pad=15, color="#222222",
             y=1.0)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_feature_table.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
