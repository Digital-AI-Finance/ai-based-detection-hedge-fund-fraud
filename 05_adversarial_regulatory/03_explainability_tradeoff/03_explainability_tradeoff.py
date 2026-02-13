#!/usr/bin/env python3
"""Explainability vs Detection Performance -- Section 05 Adversarial & Regulatory.

Scatter plot showing the tradeoff between model explainability (x-axis, 1-5)
and detection performance (y-axis, AUC 0.6-0.9). Regulatory threshold lines
and acceptable-quadrant shading included.
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
models = {
    "Logistic\nRegression": (5.0, 0.68, mlblue),
    "Random\nForest":       (3.5, 0.82, mlgreen),
    "XGBoost":              (3.0, 0.86, mlgreen),
    "Deep\nLearning":       (1.5, 0.82, mlred),
    "Anomaly\nDetection":   (2.0, 0.79, mlorange),
    "GNN":                  (1.5, 0.87, mlpurple),
    "NLP\n(FinBERT)":       (2.0, 0.85, mlorange),
}

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5))

# Shade acceptable quadrant (high explainability >= 2.5 AND high perf >= 0.75)
ax.axhspan(0.75, 0.92, xmin=(2.5 - 0.8) / (5.5 - 0.8), xmax=1.0,
           color=mlgreen, alpha=0.07, zorder=0)

# Threshold lines
ax.axvline(x=2.5, color="#888888", linestyle="--", linewidth=1, alpha=0.7)
ax.axhline(y=0.75, color="#888888", linestyle="--", linewidth=1, alpha=0.7)

ax.text(2.55, 0.615, "Regulatory minimum\nexplainability", fontsize=7,
        color="#666666", va="bottom")
ax.text(0.9, 0.755, "Acceptable\nperformance", fontsize=7,
        color="#666666", va="bottom")

# Plot models
for name, (x, y, color) in models.items():
    ax.scatter(x, y, s=120, c=[color], edgecolors="white", linewidth=1,
              zorder=5)
    # Offset labels to avoid overlap
    offset_x, offset_y = 0.12, 0.012
    if "GNN" in name:
        offset_x = -0.20
        offset_y = -0.025
    elif "Deep" in name:
        offset_x = -0.25
        offset_y = 0.015
    elif "Anomaly" in name:
        offset_x = 0.15
        offset_y = -0.015
    elif "NLP" in name:
        offset_x = 0.15
        offset_y = 0.008
    ax.annotate(name, (x, y), xytext=(x + offset_x, y + offset_y),
                fontsize=7.5, color="#333333", va="center")

# Acceptable-zone label
ax.text(4.2, 0.88, "Ideal Zone", fontsize=9, fontweight="bold",
        color=mlgreen, alpha=0.7, ha="center")

ax.set_xlabel("Explainability Score (1 = opaque, 5 = transparent)",
              fontsize=9, color="#333333")
ax.set_ylabel("Detection Performance (AUC)", fontsize=9, color="#333333")
ax.set_xlim(0.8, 5.5)
ax.set_ylim(0.60, 0.92)
ax.set_title("Explainability vs Detection Performance Trade-off",
             fontsize=12, fontweight="bold", pad=10, color="#222222")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=8)
ax.grid(alpha=0.15, linewidth=0.5)

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "03_explainability_tradeoff.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
