import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-muted')

x = np.linspace(0, 10, 100)
y_sin = 10*np.sin(x)
y_cos = 10*np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 100]
bar_colors = ['steelblue', 'tomato', 'mediumseagreen', 'orchid']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Matplotlib Dashboard', fontsize=16, fontweight='bold', y=1.02)

# --- Line Chart ---
ax1.plot(x, y_sin, label='Sine', color='royalblue', linewidth=2, marker='o', markevery=10, markersize=5)
ax1.plot(x, y_cos, label='Cosine', color='indianred', linestyle='--', linewidth=2, marker='s', markevery=10, markersize=5)
ax1.set_title('Trigonometric Functions')
ax1.set_xlabel('X (radians)')
ax1.set_ylabel('Amplitude')
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Bar Chart ---
bars = ax2.bar(categories, values, color=bar_colors, alpha=0.85, edgecolor='black', linewidth=0.7)
ax2.set_title('Category Distribution')
ax2.set_xlabel('Categories')
ax2.set_ylabel('Impact Score')

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax2.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5), textcoords='offset points',
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()