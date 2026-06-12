import matplotlib.pylab as plt

b=[1190,810,528,691,1009,889,416,123,70]
a=["Electronics","Clothing","Groceries","Home Appliances","Furniture","Footwear","Books","Toys","Others"]

plt.title("Category-wise Distribution of Values")
plt.axis("equal")

plt.pie(b,labels=a,autopct="%0.1f%%",radius=1.06,explode=[0,0.1,0.1,0,0,0,0.1,0.1,0.2])
plt.savefig(r"C:\Users\saich\OneDrive\Desktop\python\tictactoe\piechart.png",bbox_inches="tight",pad_inches=4,transparent=True)

plt.show()

