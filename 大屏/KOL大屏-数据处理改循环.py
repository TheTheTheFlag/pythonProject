import numpy as np
from bs4 import BeautifulSoup
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime
from pyecharts.charts import Timeline, Bar, Line, Funnel, Pie, Page
from pyecharts.components import Table
import pandas as pd
import time
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import os


# 近7天活跃人数.xls    1:近7日各地市活跃人数玫瑰图Timeline(Pie)
# 近6月地市活跃人数.xls 2:近6月地市活跃人数条形图Timeline(Bar) 3:近6月地市活跃人数条形图+折线图Timeline(Bar+line)
# 话题攻克情况.xls     5:话题攻克情况堆叠图
# 近6月地市话题类型.xls 4:近6月各类型话题数玫瑰图Timeline(Pie)
# 地市话题攻克情况.xls  6:近6月地市话题数条形图+折线图(Bar+line)
# 上周活跃详情.xls     7:上周活跃详情表格


# 获取近七天时间
def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list = get_nday_list(8)


# 获取近6月月份
def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons = []
for i in range(6):
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))
before_n_mons = before_n_mons[::-1]

# 1:近7日各地市活跃人数玫瑰图Timeline(Pie)
# 获取数据列表
df_001 = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xls')
df_001 = df_001.fillna(value=0)
df_001[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '前0天人数']] = df_001[
    ['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']].applymap(lambda x: str(x).strip())
df_001 = df_001[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '前0天人数']]
# 获取df_0011到df_0018数据，格式为：df_0011 = df_001[['地市', '前7天人数']]
for i in range((len(df_001.columns)-1)):  # 循环字段数-1次，因为地市字段和前i天人数一起输出，所以少一个字段数
    exec("df_001" + str(i + 1) + "=" + "df_001[['地市', '前" + str(7 - i) + "天人数']]")

city_001 = df_0011.地市
# 获取values_001_1到values_001_8数据，格式为：values_001_1 = df_0011.前7天人数
for i in range((len(df_001.columns)-1)):
    exec("values_001_" + str(i + 1) + "=" + "df_001" + str(i + 1) + ".前" + str(7 - i) + "天人数")
    # print("values_001_"+str(i+1)+"="+"df_001"+str(i+1)+".前"+str(7-i)+"天人数")

# 获取list_001_1到list_001_8数据，格式为：list_001_1 = [[city_001[i] + "市", int(float(values_001_1[i]))] for i in range(len(city_001))]
for i in range((len(df_001.columns)-1)):
    exec("list_001_" + str(i + 1) + "=" + "[[city_001[j]" + ", int(float(values_001_" + str(
        i + 1) + "[j]))] for j in range(len(city_001))]")
# list_001_44 = [list_001_1, list_001_2, list_001_3, list_001_4, list_001_5, list_001_6, list_001_7, list_001_8]
list_001_44 = []
for i in range((len(df_001.columns)-1)):
    exec("list_001_44.append(list_001_"+str(i + 1)+")")

dict_001_1 = {time_list[i]: list_001_44[i] for i in range(len(list_001_44))}

def timeline_base_01() -> Timeline:
    tl_001 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
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
                .set_global_opts(
                legend_opts=opts.LegendOpts(is_show=False),
                visualmap_opts=opts.VisualMapOpts(max_=150, item_width=15, item_height=80),
                title_opts=opts.TitleOpts("近7日各地市活跃人数 (时间: {}日 )".format(date)))
        )
        tl_001.add(pie, "{}".format(date))
    print("玫瑰图-7天活跃情况数据: ", dict_001_1)
    print('玫瑰图-7天活跃情况已输出')
    return tl_001


timeline_base_01().render("近7日各地市活跃人数玫瑰图Timeline(Pie).html")
