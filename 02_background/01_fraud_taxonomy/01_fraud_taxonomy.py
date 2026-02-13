#!/usr/bin/env python3
"""Fraud Taxonomy -- Section 02 Background.

Horizontal bar chart ranking five hedge fund fraud types by detection
difficulty (1-5 scale), with colour gradient and case-study annotations.
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
fraud_types = [
    "Regulatory Fraud",
    "Performance Fabrication",
    "Strategy Misrepresentation",
    "Allocation Fraud",
    "Market Manipulation",
]
difficulty = [2, 3, 3, 4, 5]
cases = [
    "Filing fraud, AML violations",
    "e.g., Madoff",
    "Style drift, hidden leverage",
    "Cherry-picking trades",
    "Insider trading, spoofing",
]

# Sort by difficulty ascending for visual impact
order = np.argsort(difficulty)
fraud_types = [fraud_types[i] for i in order]
difficulty = [difficulty[i] for i in order]
cases = [cases[i] for i in order]

# ── colour gradient (low -> mlblue, high -> mlpurple) ──────────────
cmap = mcolors.LinearSegmentedColormap.from_list("ml", [mlblue, mlpurple])
norm = mcolors.Normalize(vmin=1, vmax=5)
bar_colors = [cmap(norm(d)) for d in difficulty]

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.barh(
    fraud_types,
    difficulty,
    color=bar_colors,
    edgecolor="white",
    linewidth=0.8,
    height=0.62,
    zorder=3,
)

# Difficulty labels inside bars
for bar, d in zip(bars, difficulty):
    ax.text(
        bar.get_width() - 0.15,
        bar.get_y() + bar.get_height() / 2,
        f"{d}/5",
        va="center",
        ha="right",
        fontsize=11,
        fontweight="bold",
        color="white",
        zorder=4,
    )

# Case annotations to the right of bars
for bar, case in zip(bars, cases):
    ax.text(
        bar.get_width() + 0.12,
        bar.get_y() + bar.get_height() / 2,
        case,
        va="center",
        ha="left",
        fontsize=8.5,
        color="#555555",
        style="italic",
    )

# ── axis formatting ────────────────────────────────────────────────
ax.set_xlabel("Detection Difficulty", fontsize=11, color="#333333")
ax.set_xlim(0, 6.5)
ax.set_title(
    "Hedge Fund Fraud Taxonomy by Detection Difficulty",
    fontsize=13,
    fontweight="bold",
    pad=12,
    color="#222222",
)
ax.tick_params(axis="y", labelsize=10)
ax.tick_params(axis="x", labelsize=9)
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.grid(axis="x", alpha=0.25)
ax.grid(axis="y", visible=False)
sns.despine(left=True, bottom=True)

# Colour-bar legend
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, orientation="vertical", fraction=0.025, pad=0.02)
cbar.set_label("Difficulty", fontsize=9)
cbar.set_ticks([1, 2, 3, 4, 5])
cbar.ax.tick_params(labelsize=8)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_fraud_taxonomy.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
