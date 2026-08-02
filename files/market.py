import matplotlib.pyplot as plt

a = [120, 79, 80, 89, 106, 130, 149, 114]
b = [119, 110, 128, 91, 109, 139, 116, 123, 70]

plt.xlabel("Market Price Range")
plt.ylabel("Frequency")
plt.title("Share Market Price Distribution")
plt.hist([a, b], bins=[70, 100, 125, 150], rwidth=0.80, color=["blue", "red"], label=["Stock A", "Stock B"])
plt.legend()
plt.show()
