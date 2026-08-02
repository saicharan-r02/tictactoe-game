import matplotlib.pyplot as plt

a=[1,3,5,7,9,11,13,15,18]
b=[39,50,48,61,37,49,56,29,30]

plt.xlabel("Days") 
plt.ylabel("Tempuratur")
plt.title("Data")
plt.scatter(a,b,color="black",linewidth=2)
plt.show()
