#!/usr/bin/env python3
"""Database Coverage -- Section 08 Reproducibility.

Bar chart showing 5 academic databases with their disciplinary focus areas,
colour-coded by focus type. Annotated with search period.
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
databases = ["Scopus", "Web of Science", "IEEE Xplore", "SSRN", "Google Scholar"]
focus_areas = ["Both CS + Finance", "Both CS + Finance", "CS / AI",
               "Finance", "Supplementary"]

# Focus type -> color mapping
focus_colors = {
    "Both CS + Finance": mlpurple,
    "CS / AI": mlblue,
    "Finance": mlorange,
    "Supplementary": mllavender,
}

bar_colors = [focus_colors[f] for f in focus_areas]

# Relative coverage weight (stylised for visual hierarchy)
coverage = [5, 4.5, 3.5, 3, 2]

# -- figure -------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4))

y_pos = np.arange(len(databases))
bars = ax.barh(y_pos, coverage, height=0.55, color=bar_colors,
               edgecolor="white", linewidth=1.2)

# Labels
for i, (db, focus, val) in enumerate(zip(databases, focus_areas, coverage)):
    ax.text(val + 0.1, i, focus, va="center", fontsize=8, color="#555555")

ax.set_yticks(y_pos)
ax.set_yticklabels(databases, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlabel("Relative Coverage", fontsize=9, color="#333333")
ax.set_xlim(0, 7)

ax.set_title("Database Coverage by Discipline",
             fontsize=12, fontweight="bold", pad=10, color="#222222")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(labelsize=8.5)
ax.set_xticks([])

# Search period annotation
ax.text(5.5, 4.6, "Search period: 2000\u20132025",
        fontsize=8, color="#666666", ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                  edgecolor="#cccccc", linewidth=0.8))

# Legend
unique_focuses = list(dict.fromkeys(focus_areas))
legend_patches = [
    mpatches.Patch(facecolor=focus_colors[f], edgecolor="white", label=f)
    for f in unique_focuses
]
ax.legend(handles=legend_patches, loc="lower right", fontsize=7.5,
          frameon=True, framealpha=0.9, edgecolor="#cccccc")

plt.tight_layout()

# -- save ---------------------------------------------------------------------
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_database_coverage.pdf", bbox_inches="tight")
fig.savefig(out_dir / "thumb.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"Saved to {out_dir}")
