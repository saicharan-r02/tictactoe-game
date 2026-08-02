import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

plt.style.use("classic")
d=sn.load_dataset("car_crashes")
print(d.head())

sn.relplot(x="total",y="speeding",kind="scatter",data=d)
sn.relplot(x="total",y="speeding",hue="abbrev",data=d)
sn.relplot(x="total",y="speeding",hue="abbrev",style="abbrev",data=d)
sn.relplot(x="total",y="speeding",hue="abbrev",style="abbrev",size= "alcohol",sizes=(20,200),data=d)
sn.scatterplot(x="total",y="speeding",hue="abbrev",data=d)
plt.show()