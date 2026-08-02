import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

plt.style.use("seaborn-v0_8")
d=sn.load_dataset("diamonds")
print(d.head())

sn.relplot(x="carat",y="price",kind="line",data=d)
sn.relplot(x="price",y="price",hue="cut",data=d)
sn.relplot(x="carat",y="price",hue="cut",style="cut",data=d)
sn.relplot(x="carat",y="price",data=d)
sn.relplot(x="carat",y="price",hue="cut",style="cut",size= "depth",sizes=(20,200),data=d)
sn.scatterplot(x="carat",y="price",hue="cut",data=d)
plt.show()