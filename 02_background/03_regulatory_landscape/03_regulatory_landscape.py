#!/usr/bin/env python3
"""Regulatory Landscape -- Section 02 Background.

Side-by-side US vs EU comparison of regulatory frameworks relevant to
hedge fund fraud detection.
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

# ── data ────────────────────────────────────────────────────────────
us_items = [
    ("Dodd-Frank Act (2010)", "Systemic-risk oversight"),
    ("SEC / DERA", "Data analytics division"),
    ("MIDAS Platform", "Market surveillance system"),
    ("Whistleblower Program", "Financial incentives"),
]

eu_items = [
    ("AIFMD (2011)", "Fund manager regulation"),
    ("National Authorities", "ESMA coordination"),
    ("EU AI Act (2024)", "Risk-based AI governance"),
    ("High-Risk Classification", "Algorithmic finance rules"),
]

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("white")
fig, ax = plt.subplots(figsize=(9, 6))

# Layout constants
col_us_x = 1.5   # centre x for US column
col_eu_x = 7.5   # centre x for EU column
box_w = 3.4
box_h = 0.85
gap_y = 0.35
top_y = 4.5
corner = 0.08


def draw_column(items, cx, color, column_label):
    """Draw a vertical sequence of rounded boxes with down-arrows."""
    y = top_y
    for idx, (title, subtitle) in enumerate(items):
        x0 = cx - box_w / 2
        rect = mpatches.FancyBboxPatch(
            (x0, y),
            box_w,
            box_h,
            boxstyle=f"round,pad={corner}",
            facecolor=color,
            edgecolor="white",
            linewidth=2,
            zorder=3,
        )
        ax.add_patch(rect)

        # Title
        ax.text(
            cx,
            y + box_h * 0.62,
            title,
            fontsize=10,
            fontweight="bold",
            color="white",
            ha="center",
            va="center",
            zorder=4,
            path_effects=[pe.withStroke(linewidth=0.3, foreground="white")],
        )
        # Subtitle
        ax.text(
            cx,
            y + box_h * 0.26,
            subtitle,
            fontsize=8,
            color="white",
            alpha=0.85,
            ha="center",
            va="center",
            zorder=4,
        )

        # Down arrow to next box
        if idx < len(items) - 1:
            ax.annotate(
                "",
                xy=(cx, y - gap_y * 0.15),
                xytext=(cx, y + 0.01),
                arrowprops=dict(
                    arrowstyle="-|>",
                    color=color,
                    lw=1.8,
                    alpha=0.6,
                ),
                zorder=2,
            )

        y -= box_h + gap_y

    # Column header
    ax.text(
        cx,
        top_y + box_h + 0.4,
        column_label,
        fontsize=13,
        fontweight="bold",
        color=color,
        ha="center",
        va="center",
    )
    # Flag emoji-free labels
    return y  # bottom y


bottom_us = draw_column(us_items, col_us_x, mlblue, "United States")
bottom_eu = draw_column(eu_items, col_eu_x, mlpurple, "European Union")

# ── connecting dashed lines (cross-Atlantic) ───────────────────────
connect_pairs = [0, 2]  # indices to connect
y_pos = top_y
for idx in range(len(us_items)):
    mid_y = y_pos + box_h / 2
    if idx in connect_pairs:
        ax.plot(
            [col_us_x + box_w / 2 + 0.1, col_eu_x - box_w / 2 - 0.1],
            [mid_y, mid_y],
            linestyle=":",
            color="#bbbbbb",
            linewidth=1.2,
            zorder=1,
        )
    y_pos -= box_h + gap_y

# Central divider label
mid_x = (col_us_x + col_eu_x) / 2
mid_total_y = top_y + box_h / 2 - (len(us_items) / 2) * (box_h + gap_y)
ax.text(
    mid_x,
    mid_total_y,
    "Cross-border\ncoordination",
    fontsize=8,
    color="#999999",
    ha="center",
    va="center",
    style="italic",
)

# ── axis formatting ────────────────────────────────────────────────
ax.set_xlim(-0.3, 9.8)
ax.set_ylim(min(bottom_us, bottom_eu) - 0.5, top_y + box_h + 1.0)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(
    "Regulatory Landscape: US vs EU",
    fontsize=14,
    fontweight="bold",
    pad=16,
    color="#222222",
)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "03_regulatory_landscape.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
