#!/usr/bin/env python3
"""Model-Families vs Fraud-Types Suitability Heatmap -- Section 03 Pipeline.

Heatmap showing how well six model families map onto five hedge fund
fraud types (0=not suitable, 1=partial, 2=well-suited).
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# ── colour palette ──────────────────────────────────────────────────
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)

# ── data ────────────────────────────────────────────────────────────
model_families = [
    "Classical ML",
    "Deep Learning",
    "Anomaly Detection",
    "NLP",
    "GNN",
    "Generative",
]

fraud_types = [
    "Perf.\nFabrication",
    "Allocation\nFraud",
    "Strategy\nMisrep.",
    "Market\nManip.",
    "Regulatory\nFraud",
]

# Suitability matrix: 0 = not suitable, 1 = partial, 2 = well-suited
data = np.array(
    [
        [2, 1, 1, 0, 1],  # Classical ML
        [2, 1, 1, 1, 1],  # Deep Learning
        [2, 2, 1, 1, 0],  # Anomaly Detection
        [0, 0, 2, 0, 2],  # NLP
        [1, 1, 1, 2, 1],  # GNN
        [1, 0, 0, 0, 0],  # Generative
    ],
    dtype=float,
)

# ── custom 3-level colour map: white(0), mllavender(1), mlblue(2) ──
cmap = mcolors.ListedColormap(["#f5f5f5", mllavender, mlblue])
bounds = [-0.5, 0.5, 1.5, 2.5]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

# Rating labels
rating_labels = {0: "Not Suited", 1: "Partial", 2: "Well-Suited"}

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("white")
fig, ax = plt.subplots(figsize=(7, 5))

sns.heatmap(
    data,
    ax=ax,
    cmap=cmap,
    norm=norm,
    linewidths=2,
    linecolor="white",
    cbar=False,
    xticklabels=fraud_types,
    yticklabels=model_families,
    annot=False,
    square=False,
)

# Cell annotations with text and value
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        val = int(data[i, j])
        text = rating_labels[val]
        color = "white" if val == 2 else ("#444444" if val == 1 else "#bbbbbb")
        ax.text(
            j + 0.5,
            i + 0.5,
            text,
            ha="center",
            va="center",
            fontsize=8,
            fontweight="bold" if val == 2 else "normal",
            color=color,
        )

ax.set_title(
    "Model Family Suitability by Fraud Type",
    fontsize=13,
    fontweight="bold",
    pad=14,
    color="#222222",
)
ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")
ax.tick_params(axis="x", labelsize=9, rotation=0)
ax.tick_params(axis="y", labelsize=10)

# Legend
import matplotlib.patches as mpatches

legend_patches = [
    mpatches.Patch(facecolor="#f5f5f5", edgecolor="#cccccc", label="Not Suited (0)"),
    mpatches.Patch(facecolor=mllavender, edgecolor="#cccccc", label="Partial (1)"),
    mpatches.Patch(facecolor=mlblue, edgecolor="#cccccc", label="Well-Suited (2)"),
]
ax.legend(
    handles=legend_patches,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.10),
    ncol=3,
    frameon=False,
    fontsize=9,
)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "03_model_families.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
