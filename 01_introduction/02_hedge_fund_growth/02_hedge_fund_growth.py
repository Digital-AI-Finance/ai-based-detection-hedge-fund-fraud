#!/usr/bin/env python3
"""Hedge Fund AUM Growth (2000-2025) -- Section 01 Introduction.

Line chart with shaded area showing the rise of hedge fund assets under
management, annotating major fraud events (Madoff 2008, Archegos 2021).
"""

import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── colour palette ──────────────────────────────────────────────────
mlblue = (0 / 255, 102 / 255, 204 / 255)
mlpurple = (51 / 255, 51 / 255, 178 / 255)
mllavender = (173 / 255, 173 / 255, 224 / 255)

# ── data (approximate industry AUM, $ trillions) ───────────────────
years = np.array([2000, 2003, 2006, 2007, 2008, 2010, 2013, 2015, 2018, 2020, 2022, 2025])
aum = np.array([0.5, 0.8, 1.5, 1.9, 1.4, 1.9, 2.6, 3.0, 3.2, 3.6, 3.8, 4.5])

# Smooth interpolation for visual polish
from numpy.polynomial.polynomial import Polynomial

years_fine = np.linspace(years.min(), years.max(), 300)
poly = Polynomial.fit(years, aum, deg=6)
aum_fine = poly(years_fine)

# ── figure ──────────────────────────────────────────────────────────
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(8, 4.5))

# Shaded area
ax.fill_between(years_fine, 0, aum_fine, color=mlblue, alpha=0.12)
# Main line
ax.plot(years_fine, aum_fine, color=mlblue, linewidth=2.5, zorder=3)
# Data markers
ax.scatter(years, aum, color=mlblue, s=36, zorder=4, edgecolors="white", linewidths=0.8)

# ── event annotations ──────────────────────────────────────────────
events = [
    {"year": 2008, "label": "Madoff Collapse\n(2008)", "y_text": 3.2},
    {"year": 2021, "label": "Archegos\n(2021)", "y_text": 4.3},
]

for ev in events:
    ax.axvline(ev["year"], color=mlpurple, linestyle="--", linewidth=1.2, alpha=0.7, zorder=2)
    ax.annotate(
        ev["label"],
        xy=(ev["year"], poly(ev["year"])),
        xytext=(ev["year"] + 0.3, ev["y_text"]),
        fontsize=9,
        fontweight="bold",
        color=mlpurple,
        arrowprops=dict(
            arrowstyle="-|>",
            color=mlpurple,
            lw=1.2,
            connectionstyle="arc3,rad=-0.15",
        ),
        ha="left",
        va="bottom",
        zorder=5,
    )

# ── axis formatting ────────────────────────────────────────────────
ax.set_xlabel("Year", fontsize=11, color="#333333")
ax.set_ylabel("Assets Under Management ($ Trillions)", fontsize=11, color="#333333")
ax.set_title(
    "Global Hedge Fund AUM Growth (2000 \u2013 2025)",
    fontsize=13,
    fontweight="bold",
    pad=12,
    color="#222222",
)
ax.set_xlim(1999, 2026)
ax.set_ylim(0, 5.2)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1fT"))
ax.xaxis.set_major_locator(mticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))
ax.tick_params(labelsize=9, colors="#555555")
ax.grid(axis="y", alpha=0.3)
ax.grid(axis="x", alpha=0.15)
sns.despine(left=True, bottom=True)

plt.tight_layout()

# ── save ────────────────────────────────────────────────────────────
out_dir = pathlib.Path(__file__).parent
fig.savefig(out_dir / "02_hedge_fund_growth.pdf", bbox_inches="tight")
fig.savefig(
    out_dir / "thumb.png",
    dpi=150,
    bbox_inches="tight",
)
plt.close(fig)
print(f"Saved to {out_dir}")
