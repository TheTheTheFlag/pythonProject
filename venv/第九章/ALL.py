import numpy as np
import pandas as pd
import time
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from datetime import datetime

df = pd.read_excel('d:/kol.xlsx')
df[['创建人', '归属地市']] = df[['创建人', '归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'], format='%Y-%m-%d %H:%M:%S')
# 重置日期列时间格式为00:00:00
df['创建时间'] = df['创建时间'].apply(lambda x: x).dt.normalize()
# 使用pd_date_range筛选指定日期的数据
# 所有数据
df_All = df
df_count_All = df_All.groupby('归属地市')['序号'].count()
x_All = df_count_All.index
y_All = df_count_All.values
# 4月数据
df_Apr = df[df['创建时间'].isin(pd.date_range('2021-4-1', '2021-4-30'))]
df_count_Apr = df_Apr.groupby('归属地市')['序号'].count()
x_Apr = df_count_Apr.index
y_Apr = df_count_Apr.values
# 5月数据
df_May = df[df['创建时间'].isin(pd.date_range('2021-5-1', '2021-5-31'))]
df_count_May = df_May.groupby('归属地市')['序号'].count()
x_May = df_count_May.index
y_May = df_count_May.values
# 6月数据
df_Jun = df[df['创建时间'].isin(pd.date_range('2021-6-1', '2021-6-30'))]
df_count_Jun = df_Jun.groupby('归属地市')['序号'].count()
x_Jun = df_count_Jun.index
y_Jun = df_count_Jun.values

from matplotlib.font_manager import FontProperties  # 显示中文，并指定字体
myfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)
sns.set(font=myfont.get_name())
#创建一个新的Figure
#fig = plt.figure()
fig = plt.figure(figsize=(15,15))
# 定义4*2=8张图,全量饼图
ax1 = fig.add_subplot(8, 2, 1)
def make_autopct(values):
    def my_autopct(pct):
        total = sum(y_All)
        val = int(round(pct * total / 100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


plt.pie(y_All, labels=x_All, autopct=make_autopct(y_All))
# 全量条形图
ax2 = fig.add_subplot(8, 2, (3,4))
ax2 = sns.barplot(x=x_All, y=y_All, data=df_All, palette="pastel")  # seaborn画柱状图 data可以删除
plt.xticks(fontsize=16)  # 设置x和y轴刻度值字体大小
plt.yticks(fontsize=16)
# plt.yticks(np.arange(0, 300, 50))   #设置y轴标签
plt.xlabel("全量地市", fontsize=16)  # 设置x轴和y轴标签字体大小
plt.ylabel("全量话题数", fontsize=16)
x = np.arange(len(x_All))  # 在柱状图上插入数值
y = np.array(list(y_All))
for a, b in zip(x, y):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=16)

# 4月饼图
ax3 = fig.add_subplot(8, 2, 5)


def make_autopct(values):
    def my_autopct(pct):
        total = sum(y_Apr)
        val = int(round(pct * total / 100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


plt.pie(y_Apr, labels=x_Apr, autopct=make_autopct(y_Apr))
# 4月条形图
ax4 = fig.add_subplot(8, 2, (7,8))
ax4 = sns.barplot(x=x_Apr, y=y_Apr, data=df_Apr, palette="pastel")  # seaborn画柱状图 data可以删除
plt.xticks(fontsize=16)  # 设置x和y轴刻度值字体大小
plt.yticks(fontsize=16)
# plt.yticks(np.arange(0, 300, 50))   #设置y轴标签
plt.xlabel("4月地市", fontsize=16)  # 设置x轴和y轴标签字体大小
plt.ylabel("4月话题数", fontsize=16)
x = np.arange(len(x_Apr))  # 在柱状图上插入数值
y = np.array(list(y_Apr))
for a, b in zip(x, y):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=16)

# 5月饼图
ax5 = fig.add_subplot(8, 2, 9)


def make_autopct(values):
    def my_autopct(pct):
        total = sum(y_May)
        val = int(round(pct * total / 100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


plt.pie(y_May, labels=x_May, autopct=make_autopct(y_May))
# 5月条形图
ax6 = fig.add_subplot(8, 2, (11,12))
ax6 = sns.barplot(x=x_May, y=y_May, data=df_May, palette="pastel")  # seaborn画柱状图 data可以删除
plt.xticks(fontsize=16)  # 设置x和y轴刻度值字体大小
plt.yticks(fontsize=16)
# plt.yticks(np.arange(0, 300, 50))   #设置y轴标签
plt.xlabel("5月地市", fontsize=16)  # 设置x轴和y轴标签字体大小
plt.ylabel("5月话题数", fontsize=16)
x = np.arange(len(x_May))  # 在柱状图上插入数值
y = np.array(list(y_May))
for a, b in zip(x, y):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=16)

# 6月饼图
ax7 = fig.add_subplot(8, 2, 13)


def make_autopct(values):
    def my_autopct(pct):
        total = sum(y_Jun)
        val = int(round(pct * total / 100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


plt.pie(y_Jun, labels=x_Jun, autopct=make_autopct(y_Jun))
# 6月条形图
ax8 = fig.add_subplot(8, 2, (15,16))
ax8 = sns.barplot(x=x_Jun, y=y_Jun, data=df_Jun, palette="pastel")  # seaborn画柱状图 data可以删除
plt.xticks(fontsize=16)  # 设置x和y轴刻度值字体大小
plt.yticks(fontsize=16)
# plt.yticks(np.arange(0, 300, 50))   #设置y轴标签
plt.xlabel("6月地市", fontsize=16)  # 设置x轴和y轴标签字体大小
plt.ylabel("6月话题数", fontsize=16)
x = np.arange(len(x_Jun))  # 在柱状图上插入数值
y = np.array(list(y_Jun))
for a, b in zip(x, y):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=16)

#plt.show()
plt.savefig('D:/figpath.PNG')