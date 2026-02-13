#!/usr/bin/env python3
"""Detection Pipeline Architecture -- Section 03 Pipeline.

Vertical flow diagram with five processing stages and two dashed
feedback arrows (investigator feedback and drift-triggered retraining).
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
FEEDBACK_RED = "#cc3333"

# ── stage definitions (top to bottom) ──────────────────────────────
stages = [
    {
        "title": "1. Data Ingestion",
        "details": "Multi-source fusion, entity resolution",
    },
    {
        "title": "2. Feature Engineering",
        "details": "Statistical, Benford, textual, network, temporal",
    },
    {
        "title": "3. Model Selection",
        "details": "Classical ML, DL, anomaly, NLP, GNN, generative",
    },
    {
        "title": "4. Explainability",
        "details": "SHAP, LIME, attention visualization",
    },
    {
        "title": "5. Deployment",
        "details": "Batch / real-time, drift detection, human-in-the-loop",
    },
]

# ── layout constants ───────────────────────────────────────────────
box_w = 5.0
box_h = 0.9
gap = 0.55
cx = 4.0
top_y = 6.0
corner = 0.15

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("white")
fig, ax = plt.subplots(figsize=(7.5, 7.5))

box_positions = []  # store (cx, y_centre) for feedback arrows

for i, stage in enumerate(stages):
    y_top = top_y - i * (box_h + gap)
    x0 = cx - box_w / 2

    rect = mpatches.FancyBboxPatch(
        (x0, y_top),
        box_w,
        box_h,
        boxstyle=f"round,pad={corner}",
        facecolor=mlblue,
        edgecolor="white",
        linewidth=2.5,
        zorder=3,
    )
    ax.add_patch(rect)

    # Title
    ax.text(
        cx,
        y_top + box_h * 0.63,
        stage["title"],
        fontsize=11,
        fontweight="bold",
        color="white",
        ha="center",
        va="center",
        zorder=4,
        path_effects=[pe.withStroke(linewidth=0.3, foreground="white")],
    )
    # Details
    ax.text(
        cx,
        y_top + box_h * 0.28,
        stage["details"],
        fontsize=8.5,
        color="white",
        alpha=0.88,
        ha="center",
        va="center",
        zorder=4,
    )

    y_centre = y_top + box_h / 2
    box_positions.append((cx, y_centre, y_top))

    # Down arrow to next stage
    if i < len(stages) - 1:
        ax.annotate(
            "",
            xy=(cx, y_top - gap * 0.82),
            xytext=(cx, y_top - 0.02),
            arrowprops=dict(
                arrowstyle="-|>",
                color=mlpurple,
                lw=2.0,
            ),
            zorder=2,
        )

# ── feedback arrows (dashed, red) ─────────────────────────────────
# Arrow 1: Deployment (stage 5) -> Feature Engineering (stage 2)
# "Investigator Feedback"
deploy_y = box_positions[4][2] + box_h / 2   # centre of stage 5
feat_y = box_positions[1][2] + box_h / 2     # centre of stage 2
fb_x = cx + box_w / 2 + 0.6  # right side

ax.annotate(
    "",
    xy=(cx + box_w / 2, feat_y),
    xytext=(cx + box_w / 2, deploy_y),
    arrowprops=dict(
        arrowstyle="-|>",
        color=FEEDBACK_RED,
        lw=1.5,
        linestyle="dashed",
        connectionstyle="arc3,rad=-0.35",
    ),
    zorder=1,
)
ax.text(
    fb_x + 0.4,
    (deploy_y + feat_y) / 2 + 0.25,
    "Investigator\nFeedback",
    fontsize=8,
    fontweight="bold",
    color=FEEDBACK_RED,
    ha="center",
    va="center",
    style="italic",
)

# Arrow 2: Deployment (stage 5) -> Model Selection (stage 3)
# "Drift-Triggered Retraining"
model_y = box_positions[2][2] + box_h / 2   # centre of stage 3
fb_x2 = cx - box_w / 2 - 0.6  # left side

ax.annotate(
    "",
    xy=(cx - box_w / 2, model_y),
    xytext=(cx - box_w / 2, deploy_y),
    arrowprops=dict(
        arrowstyle="-|>",
        color=FEEDBACK_RED,
        lw=1.5,
        linestyle="dashed",
        connectionstyle="arc3,rad=0.35",
    ),
    zorder=1,
)
ax.text(
    fb_x2 - 0.5,
    (deploy_y + model_y) / 2 - 0.1,
    "Drift-Triggered\nRetraining",
    fontsize=8,
    fontweight="bold",
    color=FEEDBACK_RED,
    ha="center",
    va="center",
    style="italic",
)

# ── axis formatting ────────────────────────────────────────────────
margin = 1.5
y_min = box_positions[-1][2] - 0.5
y_max = top_y + box_h + 0.8
ax.set_xlim(cx - box_w / 2 - margin - 0.8, cx + box_w / 2 + margin + 0.8)
ax.set_ylim(y_min, y_max)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(
    "End-to-End Detection Pipeline Architecture",
    fontsize=13,
    fontweight="bold",
    pad=14,
    color="#222222",
)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "01_pipeline_architecture.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
