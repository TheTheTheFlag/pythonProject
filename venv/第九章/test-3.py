import numpy as np
import pandas as pd
import time
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from datetime import datetime

df = pd.read_excel('d:/kol.xlsx')
df[['创建人','归属地市']] = df[['创建人','归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'],format = '%Y-%m-%d %H:%M:%S')
#重置日期列时间格式为00:00:00
df['创建时间'] = df['创建时间'].apply(lambda x: x).dt.normalize()
#使用pd_date_range筛选指定日期的数据
last_m = df[df['创建时间'].isin(pd.date_range('2021-6-1', '2021-6-30'))]

df_count = last_m.groupby('归属地市')['序号'].count()

x_count = df_count.index
y_count = df_count.values

def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height), # put the detail data
                    xy=(rect.get_x() + rect.get_width() / 2, height), # get the center location.
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def auto_text(rects):
    for rect in rects:
        ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')


labels = x_count
men_means = y_count
women_means = [25, 32, 34, 20, 25]

index = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rect1 = ax.bar(index - width / 2, men_means, color ='lightcoral', width=width, label ='Men')
#rect2 = ax.bar(index + width / 2, women_means, color ='springgreen', width=width, label ='Women')

ax.set_title('Scores by gender')
ax.set_xticks(ticks=index)
ax.set_xticklabels(x_count)
ax.set_ylabel('Scores')

ax.set_ylim(0, 50)
# auto_label(rect1)
# auto_label(rect2)
auto_text(rect1)
#auto_text(rect2)


plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #解决负号“-”显示为方块的问题


ax.legend(loc='upper right', frameon=False)
fig.tight_layout()
plt.savefig('2.tif', dpi=300)
plt.show()
