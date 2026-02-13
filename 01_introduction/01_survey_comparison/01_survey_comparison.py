#!/usr/bin/env python3
"""Survey Comparison Heatmap -- Section 01 Introduction.

Compares eight surveys (rows) across six coverage dimensions (columns).
'This Survey' is highlighted as the only one covering all dimensions.
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import seaborn as sns

# ── colour palette ──────────────────────────────────────────────────
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
LIGHT_GRAY = "#e8e8e8"

# ── data ────────────────────────────────────────────────────────────
surveys = [
    "Ngai et al. (2011)",
    "Abdallah et al. (2016)",
    "West & Bhattacharya (2016)",
    "Pourhabibi et al. (2020)",
    "Bao et al. (2020)",
    "Hilal et al. (2022)",
    "Ahmed et al. (2024)",
    "This Survey",
]

dimensions = [
    "Hedge Fund\nFocus",
    "AI / ML\nMethods",
    "Fraud\nTaxonomy",
    "Adversarial\nRobustness",
    "Regulatory\nReadiness",
    "Research\nAgenda",
]

data = np.array(
    [
        [0, 1, 0, 0, 0, 0],  # Ngai
        [0, 1, 0, 0, 0, 0],  # Abdallah
        [0, 1, 0, 0, 0, 0],  # West
        [0, 1, 0, 0, 0, 0],  # Pourhabibi
        [0, 1, 0, 0, 0, 0],  # Bao
        [0, 1, 0, 0, 0, 1],  # Hilal
        [0, 1, 0, 0, 0, 1],  # Ahmed
        [1, 1, 1, 1, 1, 1],  # This Survey
    ],
    dtype=float,
)

# ── figure ──────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))

# Custom colour map: 0 -> light gray, 1 -> mlblue
cmap = mcolors.ListedColormap([LIGHT_GRAY, mlblue])
bounds = [-0.5, 0.5, 1.5]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

sns.heatmap(
    data,
    ax=ax,
    cmap=cmap,
    norm=norm,
    linewidths=1.5,
    linecolor="white",
    cbar=False,
    xticklabels=dimensions,
    yticklabels=surveys,
    annot=False,
    square=False,
)

# Overlay "This Survey" row with mlpurple where value == 1
this_row = len(surveys) - 1
for col_idx in range(len(dimensions)):
    if data[this_row, col_idx] == 1:
        ax.add_patch(
            mpatches.FancyBboxPatch(
                (col_idx + 0.04, this_row + 0.04),
                0.92,
                0.92,
                boxstyle="round,pad=0.02",
                facecolor=mlpurple,
                edgecolor="white",
                linewidth=1.5,
            )
        )

# Cell annotations: checkmark / dash
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        symbol = "\u2713" if data[i, j] == 1 else "\u2014"
        color = "white" if data[i, j] == 1 else "#999999"
        ax.text(
            j + 0.5,
            i + 0.5,
            symbol,
            ha="center",
            va="center",
            fontsize=13,
            fontweight="bold",
            color=color,
        )

# Highlight "This Survey" label
labels = ax.get_yticklabels()
for lbl in labels:
    if "This Survey" in lbl.get_text():
        lbl.set_fontweight("bold")
        lbl.set_color(mlpurple)
ax.set_yticklabels(labels)

ax.set_title(
    "Survey Coverage Comparison",
    fontsize=13,
    fontweight="bold",
    pad=12,
    color="#222222",
)
ax.tick_params(axis="x", labelsize=9, rotation=0)
ax.tick_params(axis="y", labelsize=9)
ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")

# Legend
legend_patches = [
    mpatches.Patch(facecolor=mlblue, edgecolor="white", label="Covered"),
    mpatches.Patch(facecolor=mlpurple, edgecolor="white", label="This Survey"),
    mpatches.Patch(facecolor=LIGHT_GRAY, edgecolor="white", label="Not Covered"),
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
fig.savefig(out_dir / "01_survey_comparison.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
