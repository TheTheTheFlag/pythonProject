from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import os
import numpy as np
import pandas as pd
import time
from pandas import Series, DataFrame
from datetime import datetime
from numpy import random
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.globals import ThemeType

df_007_ = pd.read_excel('d:/WJ/用户画像输入/上周活跃详情.xls')
order = ['地市', '包含登录活跃人数', '不包含登录活跃人数', '创建话题数', '创建话题类型', '浏览人数', '浏览次数', '留言人数', '留言次数', '登录人数', '登录次数', '留言率', '关注人数', '关注次数', '点赞人数', '点赞次数']
#对于列进行重排序
df_007_ = df_007_[order]
df_007_ = df_007_.fillna(value=0)
list_007_1 = []
for line in df_007_:
    list_007_1.append(line)
df_007_x = []
for i in range(len(df_007_)):
    df_007_x.append(df_007_.iloc[i].values)
column = list(df_007_.columns)
aaa = column.index('登录人数')
bbb = column.index('留言人数')
ccc = column.index('留言率')
for i in range(len(df_007_)):
    # df_007_x[i][9] = str(df_007_x[i][9]*100) + '%'
    df_007_x[i][ccc] = str(round(df_007_x[i][bbb] * 100 / df_007_x[i][aaa], 2)) + '%'

table = (
    Table()
        .add(list_007_1, df_007_x)
        .set_global_opts(
        title_opts=ComponentTitleOpts(title="近7天活跃详情")
    )
        .render("近7天活跃详情.html")
)
