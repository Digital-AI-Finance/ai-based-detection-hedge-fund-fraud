#!/usr/bin/env python3
"""Feature Families Radar Chart -- Section 03 Pipeline.

Spider / radar chart comparing five feature families across five quality
dimensions: data requirement, interpretability, fraud coverage,
implementation ease, and robustness.
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import seaborn as sns

# ── colour palette ──────────────────────────────────────────────────
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)

family_colors = [
    mlblue,
    mlpurple,
    mllavender,
    (0 / 255, 160 / 255, 176 / 255),   # teal accent
    (120 / 255, 90 / 255, 180 / 255),  # muted violet
]

# ── data (Low=1, Medium=2, High=3) ─────────────────────────────────
axes_labels = [
    "Data\nRequirement",
    "Interpretability",
    "Fraud\nCoverage",
    "Implementation\nEase",
    "Robustness",
]

families = {
    "Statistical": [1, 3, 2, 3, 2],
    "Benford":     [1, 3, 1, 3, 1],
    "Textual":     [2, 2, 2, 2, 2],
    "Network":     [3, 1, 3, 1, 3],
    "Temporal":    [2, 2, 2, 2, 2],
}

N = len(axes_labels)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # close the polygon

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("white")
fig, ax = plt.subplots(figsize=(6.5, 6.5), subplot_kw=dict(polar=True))

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Gridlines at 1, 2, 3
ax.set_rgrids(
    [1, 2, 3],
    labels=["Low", "Med", "High"],
    angle=0,
    fontsize=8,
    color="#888888",
)
ax.set_ylim(0, 3.5)

# Axis labels
ax.set_thetagrids(
    np.degrees(angles[:-1]),
    labels=axes_labels,
    fontsize=9,
    fontweight="bold",
    color="#333333",
)

# Plot each family
for idx, (name, vals) in enumerate(families.items()):
    values = vals + vals[:1]
    color = family_colors[idx]
    ax.plot(angles, values, linewidth=2, label=name, color=color, zorder=3)
    ax.fill(angles, values, alpha=0.08, color=color, zorder=2)
    ax.scatter(angles[:-1], vals, s=28, color=color, zorder=4, edgecolors="white", linewidths=0.5)

ax.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, -0.14),
    ncol=5,
    fontsize=8.5,
    frameon=False,
)

ax.set_title(
    "Feature Families: Multi-Dimensional Comparison",
    fontsize=13,
    fontweight="bold",
    pad=24,
    color="#222222",
)

# Style the grid
ax.spines["polar"].set_color("#dddddd")
ax.grid(color="#dddddd", linewidth=0.6)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_feature_families.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
