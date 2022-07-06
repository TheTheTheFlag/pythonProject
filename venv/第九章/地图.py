import numpy as np
import pandas as pd
import time
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import os

from pandas import Series, DataFrame
from datetime import datetime
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.faker import Faker


df = pd.read_excel('d:/WJ/SR/KOL.xlsx')
df[['创建人','归属地市']] = df[['创建人','归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'],format = '%Y-%m-%d %H:%M:%S')
#重置日期列时间格式为00:00:00
df['创建时间'] = df['创建时间'].apply(lambda x: x).dt.normalize()
#使用pd_date_range筛选指定日期的数据
df_Jun = df[df['创建时间'].isin(pd.date_range('2021-6-1', '2021-6-30'))]

df_count = df_Jun.groupby('归属地市')['序号'].count()
#df_count = df_count['归属地市']
x1 = df_count.index
y1 = df_count.values

# 基础数据
city = x1
values2 = y1
#list1 = [[city[i],values2[i]] for i in range(len(city))]
list1 = [[city[i]+"市",int(values2[i])] for i in range(len(city))]
c = (
    Map(
        #初始化配置项
        init_opts=opts.InitOpts(width = "900px",height = "500px",chart_id='六月话题')
        )
        .add("话题情况", list1, "浙江")
        #全局配置项
        .set_global_opts(
        title_opts=opts.TitleOpts(title="6月浙江各地市创建话题数"), visualmap_opts=opts.VisualMapOpts(max_=50)
    )
        #.render(path="D:/6月浙江各地市创建话题数.html")
        .render()
)
# 打开html
os.system("render.html")
