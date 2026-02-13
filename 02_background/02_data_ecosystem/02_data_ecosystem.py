#!/usr/bin/env python3
"""Data Ecosystem Layers -- Section 02 Background.

Stacked-layer diagram illustrating the four tiers of data used for
hedge fund fraud detection: returns, regulatory, alternative, synthetic.
"""

import pathlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import seaborn as sns

# ── colour palette ──────────────────────────────────────────────────
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)

# Four layers: bottom-to-top ordering in lists (index 0 = bottom)
layers = [
    {
        "label": "Layer 1 -- Return Data",
        "sources": "Lipper TASS  |  HFR  |  Morningstar",
        "note": "Survivorship bias: +242 bp",
        "color": mllavender,
        "text_color": "#222222",
    },
    {
        "label": "Layer 2 -- Regulatory Filings",
        "sources": "SEC EDGAR: Form ADV, Form D, 13F",
        "note": "",
        "color": (110 / 255, 130 / 255, 200 / 255),  # midpoint
        "text_color": "white",
    },
    {
        "label": "Layer 3 -- Alternative Data",
        "sources": "Sentiment  |  Satellite  |  Web Traffic",
        "note": "$7.5 B market (2024)",
        "color": mlblue,
        "text_color": "white",
    },
    {
        "label": "Layer 4 -- Synthetic Data",
        "sources": "SMOTE  |  GANs  |  VAEs",
        "note": "Privacy-preserving",
        "color": mlpurple,
        "text_color": "white",
    },
]

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("white")
fig, ax = plt.subplots(figsize=(8, 5.5))

layer_h = 1.0
gap = 0.15
x_left = 0.5
x_right = 9.5
box_w = x_right - x_left
corner_r = 0.12

for i, layer in enumerate(layers):
    y_bottom = i * (layer_h + gap)

    # Rounded rectangle for each layer
    rect = mpatches.FancyBboxPatch(
        (x_left, y_bottom),
        box_w,
        layer_h,
        boxstyle=f"round,pad={corner_r}",
        facecolor=layer["color"],
        edgecolor="white",
        linewidth=2,
        zorder=2,
    )
    ax.add_patch(rect)

    # Layer label (bold, left-aligned)
    ax.text(
        x_left + 0.35,
        y_bottom + layer_h * 0.68,
        layer["label"],
        fontsize=11,
        fontweight="bold",
        color=layer["text_color"],
        va="center",
        ha="left",
        zorder=3,
        path_effects=[pe.withStroke(linewidth=0.4, foreground=layer["text_color"])],
    )

    # Sources line
    ax.text(
        x_left + 0.35,
        y_bottom + layer_h * 0.35,
        layer["sources"],
        fontsize=9,
        color=layer["text_color"],
        alpha=0.9,
        va="center",
        ha="left",
        zorder=3,
    )

    # Note (right-aligned, italics)
    if layer["note"]:
        ax.text(
            x_right - 0.35,
            y_bottom + layer_h * 0.50,
            layer["note"],
            fontsize=8.5,
            color=layer["text_color"],
            alpha=0.85,
            va="center",
            ha="right",
            style="italic",
            zorder=3,
        )

    # Upward arrow between layers (except above top layer)
    if i < len(layers) - 1:
        arrow_y = y_bottom + layer_h
        ax.annotate(
            "",
            xy=(5.0, arrow_y + gap * 0.85),
            xytext=(5.0, arrow_y + gap * 0.15),
            arrowprops=dict(
                arrowstyle="-|>",
                color="#aaaaaa",
                lw=1.8,
            ),
            zorder=1,
        )

# Vertical label on left
total_h = len(layers) * layer_h + (len(layers) - 1) * gap
ax.text(
    0.05,
    total_h / 2,
    "Increasing Novelty  \u2192",
    fontsize=9,
    color="#888888",
    rotation=90,
    va="center",
    ha="center",
)

# ── axis formatting ────────────────────────────────────────────────
ax.set_xlim(-0.3, 10.3)
ax.set_ylim(-0.3, total_h + 0.3)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(
    "Data Ecosystem for Hedge Fund Fraud Detection",
    fontsize=13,
    fontweight="bold",
    pad=14,
    color="#222222",
)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_data_ecosystem.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
