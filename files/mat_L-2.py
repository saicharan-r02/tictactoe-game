import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(data, cmap='magma')

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Intensity Scale", rotation=-90, va="bottom")

for i in range(len(data)):
    for j in range(len(data)):
        text = ax.text(j, i, f"{data[i, j]:.1f}",
                       ha="center", va="center", color="w", fontsize=8)

ax.set_title("Feature Correlation Heatmap")
plt.show()