#!/usr/bin/env python3
"""Regulatory Readiness Heatmap -- Section 05 Adversarial & Regulatory.

Heatmap: 5 method families (rows) x 5 readiness dimensions (columns).
Rating scale 1 = Low, 2 = Medium, 3 = High.
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- data ---------------------------------------------------------------------
methods = [
    "Linear Models",
    "Tree Ensembles",
    "Deep Learning",
    "Hybrid",
    "Anomaly Detection",
]

dimensions = [
    "Adversarial\nRobustness",
    "Intrinsic\nExplainability",
    "Post-hoc\nExplainability",
    "Regulatory\nCompliance",
    "Deployment\nMaturity",
]

data = np.array([
    [1, 3, 3, 3, 3],  # Linear
    [2, 2, 3, 3, 3],  # Trees
    [1, 1, 2, 1, 2],  # Deep
    [2, 2, 3, 2, 3],  # Hybrid
    [2, 1, 2, 2, 2],  # Anomaly
])

rating_labels = {1: "Low", 2: "Medium", 3: "High"}

# -- custom colour map: white(1) -> mllavender(2) -> mlblue(3) ---------------
cmap = mcolors.LinearSegmentedColormap.from_list(
    "readiness", ["#ffffff", mllavender, mlblue], N=256
)
norm = mcolors.Normalize(vmin=0.5, vmax=3.5)

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4))

sns.heatmap(
    data,
    ax=ax,
    cmap=cmap,
    norm=norm,
    linewidths=2,
    linecolor="white",
    cbar=False,
    xticklabels=dimensions,
    yticklabels=methods,
    annot=False,
    square=False,
)

# Annotate cells with rating text
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        val = data[i, j]
        text_color = "white" if val == 3 else "#222222"
        ax.text(
            j + 0.5, i + 0.5,
            f"{val} ({rating_labels[val]})",
            ha="center", va="center",
            fontsize=8.5, fontweight="bold",
            color=text_color,
        )

ax.set_title("Method Family Regulatory Readiness",
             fontsize=12, fontweight="bold", pad=12, color="#222222")
ax.tick_params(axis="x", labelsize=8.5, rotation=0)
ax.tick_params(axis="y", labelsize=9, rotation=0)
ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")

# Legend bar
from matplotlib.patches import Patch
legend_patches = [
    Patch(facecolor="#ffffff", edgecolor="#cccccc", label="1 = Low"),
    Patch(facecolor=mllavender, edgecolor="#cccccc", label="2 = Medium"),
    Patch(facecolor=mlblue, edgecolor="#cccccc", label="3 = High"),
]
ax.legend(handles=legend_patches, loc="lower center",
          bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=False, fontsize=8.5)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_readiness_heatmap.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
