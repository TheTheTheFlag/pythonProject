import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(8)
y = np.array([1,5,3,6,2,4,5,6])

df = pd.DataFrame({"x-axis": x,"y-axis": y})

sns.barplot("x-axis","y-axis",palette="RdBu_r",data=df)
plt.xticks(rotation=90)
plt.show()

#五种预设seaborn主题：darkgrid，whitegrid，dark，white，和ticks，利用set_style()来修改，不过这个修改是全局性的，会影响后面所有的图像。
#sns.set_style('dark')