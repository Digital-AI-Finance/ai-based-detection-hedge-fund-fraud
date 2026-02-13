#!/usr/bin/env python3
"""Literature Gaps Radar Chart -- Section 04 Literature Review.

Radar chart showing 7 critical assessment dimensions with severity scores
(1 = minor gap, 5 = severe gap). Red fill with alpha, black outline.
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt

# -- colour palette -----------------------------------------------------------
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)
mlorange = (255 / 255, 127 / 255, 14 / 255)
mlgreen = (44 / 255, 160 / 255, 44 / 255)
mlred = (214 / 255, 39 / 255, 40 / 255)

# -- data ---------------------------------------------------------------------
dimensions = [
    "Reproducibility\nCrisis",
    "Benchmark\nGap",
    "Domain\nSpecificity",
    "Class Imbalance\nHandling",
    "Evaluation\nProtocols",
    "Publication\nBias",
    "Overfitting\nRisk",
]

scores = [5, 5, 4, 4, 3, 3, 4]

# -- figure -------------------------------------------------------------------
angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()

# Close the polygon
values = scores + [scores[0]]
angles += [angles[0]]

fig, ax = plt.subplots(figsize=(5.5, 5.5), subplot_kw=dict(polar=True))

# Draw the filled area
ax.fill(angles, values, color=mlred, alpha=0.20)
ax.plot(angles, values, color="black", linewidth=1.8, linestyle="-")
ax.plot(angles, values, "o", color=mlred, markersize=6, zorder=5)

# Configure grid
ax.set_ylim(0, 5.5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=7, color="#666666")

ax.set_xticks(angles[:-1])
ax.set_xticklabels(dimensions, fontsize=8.5, color="#222222")

# Annotate each point with its score
for angle, val in zip(angles[:-1], scores):
    ax.text(angle, val + 0.35, str(val), ha="center", va="center",
            fontsize=9, fontweight="bold", color=mlred)

# Grid styling
ax.grid(color="#cccccc", linewidth=0.5)
ax.spines["polar"].set_color("#cccccc")

ax.set_title("Critical Assessment of Literature Gaps",
             fontsize=12, fontweight="bold", pad=20, color="#222222")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_literature_gaps.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
