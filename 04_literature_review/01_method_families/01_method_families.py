#!/usr/bin/env python3
"""Method Families Performance Comparison -- Section 04 Literature Review.

Grouped horizontal bar chart comparing 7 method families on reported AUC
ranges (min-max bars with mean point).
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- data ---------------------------------------------------------------------
families = [
    "Classical Statistical",
    "Tree-Based Ensemble",
    "Deep Learning",
    "NLP / Text-Based",
    "Graph Neural Networks",
    "Semi-Supervised",
    "Synthetic Augmented",
]

lo = np.array([0.65, 0.85, 0.75, 0.83, 0.85, 0.80, 0.82])
hi = np.array([0.70, 0.88, 0.82, 0.87, 0.87, 0.84, 0.86])
means = (lo + hi) / 2

metric_labels = [
    "AUC",
    "F1",
    "AUC",
    "AUC",
    "AUC",
    "AUC",
    "AUC",
]

colors = [mllavender, mlgreen, mlred, mlorange, mlpurple, mlblue, (0.55, 0.55, 0.75)]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4.5))

y_pos = np.arange(len(families))

for i, (low, high, mean, color) in enumerate(zip(lo, hi, means, colors)):
    ax.barh(i, high - low, left=low, height=0.55, color=color, alpha=0.75,
            edgecolor="white", linewidth=0.8)
    ax.plot(mean, i, "o", color="white", markersize=7, zorder=5)
    ax.plot(mean, i, "o", color=color, markersize=5, markeredgecolor="white",
            markeredgewidth=0.5, zorder=6)
    ax.text(high + 0.005, i, f"{low:.2f}\u2013{high:.2f} ({metric_labels[i]})",
            va="center", fontsize=7.5, color="#333333")

ax.set_yticks(y_pos)
ax.set_yticklabels(families, fontsize=8.5)
ax.set_xlabel("Reported Performance Score", fontsize=9, color="#333333")
ax.set_xlim(0.58, 0.98)
ax.xaxis.set_major_locator(mticker.MultipleLocator(0.05))
ax.invert_yaxis()

ax.set_title("Method Family Performance Comparison",
             fontsize=12, fontweight="bold", pad=10, color="#222222")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="both", labelsize=8)
ax.grid(axis="x", alpha=0.25, linewidth=0.5)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_method_families.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
