# 柱状堆叠图
import pyecharts.options as opts
import os
import numpy as np
import pandas as pd
import time
from pandas import Series, DataFrame
from datetime import datetime
from numpy import random
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

df = pd.read_excel('d:/WJ/SR/kol2.xlsx')
df[['状态', '创建人', '归属地市']] = df[['状态', '创建人', '归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'], format='%Y-%m-%d %H:%M:%S')
# 重置日期列时间格式为00:00:00
df['创建时间'] = df['创建时间'].apply(lambda x: x).dt.normalize()
# 使用pd_date_range筛选指定日期的数据
# 所有数据
df_All = df
df_count_All = df_All.groupby('归属地市')['序号'].count()
x_All = df_count_All.index
print("创建地市：%s" % x_All)
y_All = df_count_All.values
df_1=df[df.状态=='收集中']
df_1_count = df_1.groupby('归属地市')['序号'].count()
df_1_x = df_1_count.index
df_1_y = df_1_count.values
df_2=df[df.状态=='攻克中']
df_2_count = df_2.groupby('归属地市')['序号'].count()
df_2_x = df_2_count.index
df_2_y = df_2_count.values
df_3=df[df.状态=='已攻克']
df_3_count = df_3.groupby('归属地市')['序号'].count()
df_3_x = df_3_count.index
df_3_y = df_3_count.values
df_4=df[df.状态=='已关闭']
df_4_count = df_4.groupby('归属地市')['序号'].count()
df_4_x = df_4_count.index
df_4_y = df_4_count.values
list1 = [[df_1_x[i]+"市",int(df_1_y[i])] for i in range(len(df_1_x))]
print("收集中话题数：%s" % list1)
list2 = [[df_2_x[i]+"市",int(df_2_y[i])] for i in range(len(df_2_x))]
print("攻克中话题数：%s" % list2)
list3 = [[df_3_x[i]+"市",int(df_3_y[i])] for i in range(len(df_3_x))]
print("已攻克话题数：%s" % list3)
list4 = [[df_4_x[i]+"市",int(df_4_y[i])] for i in range(len(df_4_x))]
print("已关闭话题数：%s" % list4)
city = ['丽水', '台州', '嘉兴', '宁波', '杭州', '温州', '湖州', '省公司', '绍兴', '舟山', '衢州','金华']
y1=[26, 97, 49, 211, 163, 65, 28, 1, 142, 36, 70, 122]
y2=[2, 5, 2, 6, 16, 23, 2, 0, 4, 2, 3, 7]
y3=[2, 6, 15, 5, 3, 20, 0, 4, 5, 2, 2, 9]
y4=[0, 0, 6, 5, 2, 6, 5, 1, 0, 3, 1, 3]

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(city)
    .add_yaxis('收集中', y1, stack='stack1')
    .add_yaxis('攻克中', y2, stack='stack1')
    .add_yaxis('已攻克', y3, stack='stack1')
    .add_yaxis('已关闭', y4, stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='话题情况'),
                     xaxis_opts=opts.AxisOpts(name='地市'),
                     yaxis_opts=opts.AxisOpts(name='话题'),
                     visualmap_opts=opts.VisualMapOpts(max_=100),
                     toolbox_opts=opts.ToolboxOpts(),
                     datazoom_opts=opts.DataZoomOpts())
)

bar.render('D:/KOL话题情况堆叠图.html')
os.system("D:/KOL话题情况堆叠图.html")