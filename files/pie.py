import os
from typing import cast
from matplotlib.patches import Wedge
from matplotlib.text import Text
import matplotlib.pyplot as plt

# Data
values = [1190,810,528,691,1009,889,416,123,70]
categories = [
    "Electronics","Clothing","Groceries","Home Appliances",
    "Furniture","Footwear","Books","Toys","Others"
]

# Segments to pull out for emphasis
explode=[0.05,0.10,0.10,0,0,0,0.10,0.10,0.20]

# Curated color palette
colors=[
    '#4C72B0','#DD8452','#55A868','#C44E52',
    '#8172B3','#937860','#DA8BC3','#8C8C8C','#CCB974'
]

# Plot
fig,ax=plt.subplots(figsize=(10,7))
fig.patch.set_facecolor('#F8F8F8')

# autopct is set, so ax.pie always returns a 3-tuple here
wedges,texts,autotexts=cast(
    tuple[list[Wedge],list[Text],list[Text]],
    ax.pie(values,labels=categories,autopct='%0.1f%%',radius=1.06,explode=explode,colors=colors,startangle=140,wedgeprops=dict(edgecolor='white',linewidth=1.5))
    )

# Style percentage labels
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

# Style category labels
for text in texts:
    text.set_fontsize(10)

ax.set_title('Category-wise Distribution of Sales Values',fontsize=15,fontweight='bold',pad=20)

# Add a legend outside the pie
ax.legend(wedges,categories,title='Categories',loc='center left',bbox_to_anchor=(1,0,0.5,1),fontsize=9)
plt.tight_layout()

# Save relative to the script's location so it works on any machine
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'piechart.png')
plt.savefig(output_path,bbox_inches='tight',dpi=150,facecolor=fig.get_facecolor())
plt.show()
