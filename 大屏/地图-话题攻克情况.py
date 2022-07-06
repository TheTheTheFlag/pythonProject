import os
import numpy as np
import pandas as pd
import time
from pandas import Series, DataFrame
from datetime import datetime
from numpy import random
from pyecharts.charts import Bar, Map
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.options import MapItem

df = pd.read_excel('d:/WJ/用户画像输入/话题列表.xls')
df[['状态', '创建人', '归属地市']] = df[['状态', '创建人', '归属地市']].applymap(lambda x: str(x).strip())

# 所有数据
df_All = df
df_count_All = df_All.groupby('归属地市')['序号'].count()
x_All = df_count_All.index
y_All = df_count_All.values
df_1 = df[df.状态 == '收集中']
df_1_count = df_1.groupby('归属地市')['序号'].count()
df_1_x = df_1_count.index
df_1_y = df_1_count.values
df_2 = df[df.状态 == '攻克中']
df_2_count = df_2.groupby('归属地市')['序号'].count()
df_2_x = df_2_count.index
df_2_y = df_2_count.values
df_3 = df[df.状态 == '已攻克']
df_3_count = df_3.groupby('归属地市')['序号'].count()
df_3_x = df_3_count.index
df_3_y = df_3_count.values
df_4 = df[df.状态 == '已关闭']
df_4_count = df_4.groupby('归属地市')['序号'].count()
df_4_x = df_4_count.index
df_4_y = df_4_count.values

# Y轴坐标数据处理，和全量数据的Y轴数据保持一致，缺失地市补成0
list1 = [[x_All[i], int(y_All[i])] for i in range(len(x_All))]
list2 = [[df_1_x[i], int(df_1_y[i])] for i in range(len(df_1_x))]
list3 = [[df_2_x[i], int(df_2_y[i])] for i in range(len(df_2_x))]
list4 = [[df_3_x[i], int(df_3_y[i])] for i in range(len(df_3_x))]
list5 = [[df_4_x[i], int(df_4_y[i])] for i in range(len(df_4_x))]

dict_a = dict(list1)
dict_b = dict(list2)
dict_c = dict(list3)
dict_d = dict(list4)
dict_e = dict(list5)

ls_sjz = [[x, dict_b[x]] if x in dict_b else [x, 0] for x in dict_a]
ls_gkz = [[x, dict_c[x]] if x in dict_c else [x, 0] for x in dict_a]
ls_ygk = [[x, dict_d[x]] if x in dict_d else [x, 0] for x in dict_a]
ls_ygb = [[x, dict_e[x]] if x in dict_e else [x, 0] for x in dict_a]

print("收集中话题：%s" % ls_sjz)
print("攻克中话题：%s" % ls_gkz)
print("已攻克话题：%s" % ls_ygk)
print("已关闭话题：%s" % ls_ygb)

# X轴坐标数据处理，将X轴输出为列表格式
num_list = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        num_list.append(k[i])
city = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        city.append(k[i - 1])

# 基础数据
city = df_3_x
values2 = df_3_y
# list1 = [[city[i],values2[i]] for i in range(len(city))]
list1 = [[city[i] + "市", int(values2[i])] for i in range(len(city))]
c = (
    Map(
        # 初始化配置项
        init_opts=opts.InitOpts(width="900px", height="500px", chart_id='六月话题')
    )
        .add("话题情况", list1, "浙江")
        # 全局配置项
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True, trigger="item"),
        title_opts=opts.TitleOpts(title="浙江各地市攻克话题数"), visualmap_opts=opts.VisualMapOpts(max_=25)
    )
        .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True, position="right", formatter="{b} : {c}", rotate=0)
    )
        .render("浙江各地市攻克话题数.html")

    # .render()
)
MapItem(
)
# 打开html
os.system("浙江各地市攻克话题数.html")
