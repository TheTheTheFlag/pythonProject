import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyecharts import options as opts
from pyecharts.charts import Bar

df = pd.DataFrame(np.random.rand(6, 4),
                    index=['one', 'two', 'three', 'four', 'five', 'six'],
                    columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot.barh(stacked=True, alpha=0.5) #stacked=True即可为DataFrame生成堆积柱状图
#df.plot.bar()
plt.show()