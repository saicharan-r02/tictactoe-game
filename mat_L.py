"""
Matplotlib Dashboard
====================
Displays a 3-panel data visualization dashboard:
  1. Line Chart  — Sine and Cosine waves
  2. Bar Chart   — Category distribution with value annotations
  3. Scatter Plot — Random cluster data with color mapping

Author : Sai Charan
"""

import matplotlib.pyplot as plt
import numpy as np

# ── Style ──────────────────────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-muted')

# ── Data ───────────────────────────────────────────────────────────────────────
x = np.linspace(0, 10, 300)
y_sin = 10 * np.sin(x)
y_cos = 10 * np.cos(x)

categories = ['A', 'B', 'C', 'D']
values     = [15, 30, 45, 100]
bar_colors = ['steelblue', 'tomato', 'mediumseagreen', 'orchid']

# Scatter data — two random clusters
rng = np.random.default_rng(seed=42)
scatter_x = np.concatenate([rng.normal(2, 0.6, 80), rng.normal(5, 0.8, 80)])
scatter_y = np.concatenate([rng.normal(2, 0.6, 80), rng.normal(5, 0.8, 80)])
scatter_c = np.concatenate([np.zeros(80), np.ones(80)])  # cluster labels

# ── Layout ─────────────────────────────────────────────────────────────────────
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Matplotlib Dashboard', fontsize=18, fontweight='bold', y=1.02)

# ── Panel 1 : Line Chart ───────────────────────────────────────────────────────
ax1.plot(x, y_sin,
         label='Sine', color='royalblue', linewidth=2,
         marker='o', markevery=30, markersize=5)
ax1.plot(x, y_cos,
         label='Cosine', color='indianred', linestyle='--', linewidth=2,
         marker='s', markevery=30, markersize=5)
ax1.set_title('Trigonometric Functions', fontweight='bold')
ax1.set_xlabel('X (radians)')
ax1.set_ylabel('Amplitude')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.spines[['top', 'right']].set_visible(False)

# ── Panel 2 : Bar Chart ────────────────────────────────────────────────────────
bars = ax2.bar(categories, values,
               color=bar_colors, alpha=0.85,
               edgecolor='black', linewidth=0.7)
ax2.set_title('Category Distribution', fontweight='bold')
ax2.set_xlabel('Categories')
ax2.set_ylabel('Impact Score')
ax2.spines[['top', 'right']].set_visible(False)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax2.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points',
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

# ── Panel 3 : Scatter Plot ─────────────────────────────────────────────────────
sc = ax3.scatter(scatter_x, scatter_y,
                 c=scatter_c, cmap='coolwarm',
                 alpha=0.7, edgecolors='white', linewidths=0.4, s=60)
ax3.set_title('Cluster Distribution', fontweight='bold')
ax3.set_xlabel('Feature 1')
ax3.set_ylabel('Feature 2')
ax3.spines[['top', 'right']].set_visible(False)
fig.colorbar(sc, ax=ax3, label='Cluster', ticks=[0, 1])

# ── Render ─────────────────────────────────────────────────────────────────────
plt.tight_layout()
plt.show()