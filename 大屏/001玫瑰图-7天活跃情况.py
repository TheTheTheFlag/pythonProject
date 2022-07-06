import pandas as pd
import os
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


def get_nday_list_001_(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list_001_ = get_nday_list_001_(8)
print(time_list_001_)
# 获取数据列表
df_001 = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xlsx')
df_001[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']] = df_001[
    ['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']].applymap(lambda x: str(x).strip())
df_0011 = df_001[['地市', '前7天人数']]
df_0012 = df_001[['地市', '前6天人数']]
df_0013 = df_001[['地市', '前5天人数']]
df_0014 = df_001[['地市', '前4天人数']]
df_0015 = df_001[['地市', '前3天人数']]
df_0016 = df_001[['地市', '前2天人数']]
df_0017 = df_001[['地市', '前1天人数']]
df_0018 = df_001[['地市', '今天人数']]

city_001 = df_0011.地市
values_001_1 = df_0011.前7天人数
values_001_2 = df_0012.前6天人数
values_001_3 = df_0013.前5天人数
values_001_4 = df_0014.前4天人数
values_001_5 = df_0015.前3天人数
values_001_6 = df_0016.前2天人数
values_001_7 = df_0017.前1天人数
values_001_8 = df_0018.今天人数

list_001_1 = [[city_001[i] + "市", int(values_001_1[i])] for i in range(len(city_001))]
list_001_2 = [[city_001[i] + "市", int(values_001_2[i])] for i in range(len(city_001))]
list_001_3 = [[city_001[i] + "市", int(values_001_3[i])] for i in range(len(city_001))]
list_001_4 = [[city_001[i] + "市", int(values_001_4[i])] for i in range(len(city_001))]
list_001_5 = [[city_001[i] + "市", int(values_001_5[i])] for i in range(len(city_001))]
list_001_6 = [[city_001[i] + "市", int(values_001_6[i])] for i in range(len(city_001))]
list_001_7 = [[city_001[i] + "市", int(values_001_7[i])] for i in range(len(city_001))]
list_001_8 = [[city_001[i] + "市", int(values_001_8[i])] for i in range(len(city_001))]
list_001_4 = [list_001_1, list_001_2, list_001_3, list_001_4, list_001_5, list_001_6, list_001_7, list_001_8]

dict_001_1 = {time_list_001_[i]: list_001_4[i] for i in range(len(list_001_4))}
print(dict_001_1)
# 1.创建时间线对象


tl = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
for date, data in dict_001_1.items():
    # for i in time_list_001_:
    pie = (
        Pie()
            .add(
            "活跃人数",
            # [list_001_(z) for z in zip(city_001, values_001_1)],
            data,
            rosetype="radius",
            radius=["30%", "55%"],
        )
        # .set_global_opts(title_opts=opts.TitleOpts("{}活跃人数".format(date)))
    )
    tl.add(pie, "{}".format(date))
tl.render("近7天活跃人数.html")
