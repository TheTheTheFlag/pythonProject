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

# 近7天KOL活跃人数
# 近7天活跃人数.xlsx
# 近6月地市活跃人数.xlsx
# 地市话题攻克情况.xlsx
# 近6月地市话题类型.xlsx
# 地市话题攻克情况.xlsx
# 上周活跃详情.xlsx
# 话题列表.xlsx

# 000漏斗图-KOL转化情况
df_000 = pd.read_excel('d:/WJ/用户画像输入/近7天KOL活跃人数.xlsx')
df_000 = df_000.fillna(value=0)
df_000[['全量人数', '全量活跃人数', '月活跃人数', '周活跃人数']] = df_000[
    ['全量人数', '全量活跃人数', '月活跃人数', '周活跃人数']].applymap(lambda x: str(x).strip())
df_0001 = df_000['全量人数'].values
list_000_1 = [int(df_0001[i]) for i in range(len(df_0001))]
df_0002 = df_000['全量活跃人数'].values
list_000_2 = [int(df_0002[i]) for i in range(len(df_0002))]
df_0003 = df_000['月活跃人数'].values
list_000_3 = [int(df_0003[i]) for i in range(len(df_0003))]
df_0004 = df_000['周活跃人数'].values
list_000_4 = [int(float(df_0004[i])) for i in range(len(df_0004))]


def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total_000_1 = sumOfList(list_000_1, len(list_000_1))
total_000_2 = sumOfList(list_000_2, len(list_000_2))
total_000_3 = sumOfList(list_000_3, len(list_000_3))
total_000_4 = sumOfList(list_000_4, len(list_000_4))

x_data_000 = ["全量人数", "全量活跃人数", "月活跃人数", "周活跃人数"]
y_data_000 = [total_000_1, total_000_2, total_000_3, total_000_4]
# x_data = ["全量活跃人数", "月活跃人数", "周活跃人数"]
# y_data = [total_000_2, total_000_3, total_000_4]

data_000 = [[x_data_000[i], y_data_000[i]] for i in range(len(x_data_000))]


def funnel_markpoint() -> Funnel:
    c = (
        Funnel(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE, chart_id=1))
            .add(
            series_name="",
            data_pair=data_000,
            gap=0.5,
            # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="KOL转化情况", subtitle=""))
    )
    return c


print("漏斗图-KOL转化情况数据: ", data_000)
print('漏斗图-KOL转化情况已废弃')


# 001玫瑰图-7天活跃情况
def get_nday_list_001_(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list_001_ = get_nday_list_001_(8)
# 获取数据列表
df_001 = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xlsx')
df_001 = df_001.fillna(value=0)
df_001[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']] = df_001[
    ['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']].applymap(lambda x: str(x).strip())
df = df_001[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']]

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

list_001_1 = [[city_001[i] + "市", int(float(values_001_1[i]))] for i in range(len(city_001))]
list_001_2 = [[city_001[i] + "市", int(float(values_001_2[i]))] for i in range(len(city_001))]
list_001_3 = [[city_001[i] + "市", int(float(values_001_3[i]))] for i in range(len(city_001))]
list_001_4 = [[city_001[i] + "市", int(float(values_001_4[i]))] for i in range(len(city_001))]
list_001_5 = [[city_001[i] + "市", int(float(values_001_5[i]))] for i in range(len(city_001))]
list_001_6 = [[city_001[i] + "市", int(float(values_001_6[i]))] for i in range(len(city_001))]
list_001_7 = [[city_001[i] + "市", int(float(values_001_7[i]))] for i in range(len(city_001))]
list_001_8 = [[city_001[i] + "市", int(float(values_001_8[i]))] for i in range(len(city_001))]
list_001_4 = [list_001_1, list_001_2, list_001_3, list_001_4, list_001_5, list_001_6, list_001_7, list_001_8]
dict_001_1 = {time_list_001_[i]: list_001_4[i] for i in range(len(list_001_4))}
# 1.创建时间线对象


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
            visualmap_opts=opts.VisualMapOpts(max_=30, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近7日各地市活跃人数 (时间: {}日 )".format(date)))
    )
    tl_001.add(pie, "{}".format(date))
tl_001.render("001玫瑰图-7天活跃情况.html")
print("玫瑰图-7天活跃情况数据: ", dict_001_1)
print('玫瑰图-7天活跃情况已输出')


#  002-条形图+折线图人员活跃情况
def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons_003 = []
for i in range(6):
    before_n_mons_003.append(previous_months(i, time.strftime("%Y%m", time.localtime())))
before_n_mons_0031 = before_n_mons_003[::-1]
# 获取数据列表
df_003_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xlsx')
df_003_ = df_003_.fillna(value=0)
df_003_[['地市', '当月人数', '上月人数', '前2月人数', '前3月人数', '前4月人数', '前5月人数']] = df_003_[
    ['REGION', 'MON_KOL_ACT_USER', 'LAST_1_MON_KOL_ACT_USER', 'LAST_2_MON_KOL_ACT_USER', 'LAST_3_MON_KOL_ACT_USER',
     'LAST_4_MON_KOL_ACT_USER', 'LAST_5_MON_KOL_ACT_USER']].applymap(lambda x: str(x).strip())
df_003_1 = df_003_[['地市', '当月人数']]
df_003_2 = df_003_[['地市', '上月人数']]
df_003_3 = df_003_[['地市', '前2月人数']]
df_003_4 = df_003_[['地市', '前3月人数']]
df_003_5 = df_003_[['地市', '前4月人数']]
df_003_6 = df_003_[['地市', '前5月人数']]

city_003_ = df_003_1.地市
values_003_1 = df_003_1.当月人数
values_003_2 = df_003_2.上月人数
values_003_3 = df_003_3.前2月人数
values_003_4 = df_003_4.前3月人数
values_003_5 = df_003_5.前4月人数
values_003_6 = df_003_6.前5月人数

# 1.创建时间线对象
list_city_003_ = [city_003_[i] for i in range(len(city_003_))]
list_values_003_1 = [values_003_1[i] for i in range(len(values_003_1))]
list_values_003_2 = [values_003_2[i] for i in range(len(values_003_2))]
list_values_003_3 = [values_003_3[i] for i in range(len(values_003_3))]
list_values_003_4 = [values_003_4[i] for i in range(len(values_003_4))]
list_values_003_5 = [values_003_5[i] for i in range(len(values_003_5))]
list_values_003_6 = [values_003_6[i] for i in range(len(values_003_6))]

list_003_10 = [list_values_003_6, list_values_003_5, list_values_003_4, list_values_003_3, list_values_003_2,
               list_values_003_1]
dict_003_2 = {before_n_mons_0031[i]: list_003_10[i] for i in range(len(list_003_10))}
tl_003 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
for date_003, data_003 in dict_003_2.items():
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
            .add_xaxis(list_city_003_)
            .add_yaxis("", data_003, label_opts=opts.LabelOpts(is_show=None))
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=500, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月地市活跃人数 (时间: {} 月)".format(date_003))
        )

    )
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
            .add_xaxis(list_city_003_)
            .add_yaxis("", data_003, label_opts=opts.LabelOpts(),
                       markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=500, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月地市活跃人数 (时间: {} 月)".format(date_003))
        )
    )

    tl_003.add(bar.overlap(line), "{}月".format(date_003))
    tl_003.add_schema()
tl_003.render("002-条形图+折线图人员活跃情况.html")
print("条形图+折线图人员活跃情况数据: ", dict_003_2)
print('条形图+折线图人员活跃情况已输出')

#  003漏斗图-话题攻克情况
df_004_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xlsx')
df_004_ = df_004_.fillna(value=0)
df_004_[['收集中话题数', '攻克中话题数', '已攻克话题数', '已关闭话题数']] = df_004_[
    ['SJZ_NUM', 'GKZ_NUM', 'YGK_NUM', 'YGB_NUM']].applymap(lambda x: str(x).strip())
df_004_1 = df_004_['收集中话题数'].values
list_004_1 = [int(df_004_1[i]) for i in range(len(df_004_1))]
df_004_2 = df_004_['攻克中话题数'].values
list_004_2 = [int(df_004_2[i]) for i in range(len(df_004_2))]
df_004_3 = df_004_['已攻克话题数'].values
list_004_3 = [int(df_004_3[i]) for i in range(len(df_004_3))]
df_004_4 = df_004_['已关闭话题数'].values
list_004_4 = [int(df_004_4[i]) for i in range(len(df_004_4))]
list_004_5 = list_004_3 + list_004_4

total_004_1 = sumOfList(list_004_1, len(list_004_1))
total_004_2 = sumOfList(list_004_2, len(list_004_2))
total_004_3 = sumOfList(list_004_3, len(list_004_3))
total_004_4 = sumOfList(list_004_4, len(list_004_4))

x_data_004_ = ["收集中话题数", "攻克中话题数", "已攻克话题数", "已关闭话题数"]
y_data_004_ = [total_004_1, total_004_2, total_004_3, total_004_4]

data_004_ = [[x_data_004_[i], y_data_004_[i]] for i in range(len(x_data_004_))]


def funnel_2_markpoint() -> Funnel:
    c = (
        Funnel(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
            .add(
            series_name="",
            data_pair=data_004_,
            gap=0.5,
            # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="话题转化情况", subtitle=""))
    )
    return c


print("漏斗图-话题攻克情况数据: ", data_004_)
print('漏斗图-话题攻克情况已废弃')


# 004玫瑰图-话题类型情况
def get_nday_list_005_(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list_005_ = get_nday_list_005_(8)


def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons = []
for i in range(6):
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))
before_n_mons_005 = before_n_mons[::-1]


def get_nday_list_005_(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list_005_ = get_nday_list_005_(8)
# 获取数据列表
df_005_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市话题类型.xlsx')
df_005_ = df_005_.fillna(value=0)
df_005_[['话题类型', '当月话题数', '上月话题数', '前2月话题数', '前3月话题数', '前4月话题数', '前5月话题数']] = df_005_[
    ['话题类型', 'MON_TOPIC_TAG', 'LAST_MON_TOPIC_TAG', 'LAST_2_MON_TOPIC_TAG', 'LAST_3_MON_TOPIC_TAG',
     'LAST_4_MON_TOPIC_TAG', 'LAST_5_MON_TOPIC_TAG']].applymap(lambda x: str(x).strip())
df_005_1 = df_005_[['话题类型', '当月话题数']]
df_005_2 = df_005_[['话题类型', '上月话题数']]
df_005_3 = df_005_[['话题类型', '前2月话题数']]
df_005_4 = df_005_[['话题类型', '前3月话题数']]
df_005_5 = df_005_[['话题类型', '前4月话题数']]
df_005_6 = df_005_[['话题类型', '前5月话题数']]
tag_005 = df_005_1.话题类型
values_005_1 = df_005_1.当月话题数
values_005_2 = df_005_2.上月话题数
values_005_3 = df_005_3.前2月话题数
values_005_4 = df_005_4.前3月话题数
values_005_5 = df_005_5.前4月话题数
values_005_6 = df_005_6.前5月话题数

list_005_1 = [[tag_005[i], int(values_005_1[i])] for i in range(len(tag_005))]
list_005_2 = [[tag_005[i], int(values_005_2[i])] for i in range(len(tag_005))]
list_005_3 = [[tag_005[i], int(values_005_3[i])] for i in range(len(tag_005))]
list_005_4 = [[tag_005[i], int(values_005_4[i])] for i in range(len(tag_005))]
list_005_5 = [[tag_005[i], int(values_005_5[i])] for i in range(len(tag_005))]
list_005_6 = [[tag_005[i], int(values_005_6[i])] for i in range(len(tag_005))]
list_005_4 = [list_005_6, list_005_5, list_005_4, list_005_3, list_005_2, list_005_1]

dict1_005 = {before_n_mons_005[i]: list_005_4[i] for i in range(len(list_005_4))}
# 1.创建时间线对象


tl_005 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
for date_005, data_005 in dict1_005.items():
    # for i in time_list_005_:
    pie = (
        Pie()
            .add(
            "话题数",
            # [list_005_(z) for z in zip(city, values_005_1)],
            data_005,
            rosetype="radius",
            radius=["30%", "55%"],
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(max_=30, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月各类型话题数 (时间: {}月 )".format(date_005)))
    )
    tl_005.add(pie, "{}".format(date_005))
    tl_005.add_schema()
tl_005.render("004玫瑰图-话题类型情况.html")
print("玫瑰图-话题类型情况数据: ", dict1_005)
print('玫瑰图-话题类型情况已输出')

# 005条形图+折线图月度话题情况
def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list = get_nday_list(8)


def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons = []
for i in range(6):
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))
before_n_mons006 = before_n_mons[::-1]
# 获取数据列表
df_006_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xlsx')
df_006_ = df_006_.fillna(value=0)
df_006_[['地市', '当月话题数', '上月话题数', '前2月话题数', '前3月话题数', '前4月话题数', '前5月话题数']] = df_006_[
    ['REGION', 'MON_ALL_TOPIC_NUM', 'LAST_MON_ALL_TOPIC_NUM', 'LAST_2_MON_ALL_TOPIC_NUM', 'LAST_3_MON_ALL_TOPIC_NUM',
     'LAST_4_MON_ALL_TOPIC_NUM', 'LAST_5_MON_ALL_TOPIC_NUM']].applymap(lambda x: str(x).strip())
df_006_1 = df_006_[['地市', '当月话题数']]
df_006_2 = df_006_[['地市', '上月话题数']]
df_006_3 = df_006_[['地市', '前2月话题数']]
df_006_4 = df_006_[['地市', '前3月话题数']]
df_006_5 = df_006_[['地市', '前4月话题数']]
df_006_6 = df_006_[['地市', '前5月话题数']]

city_006 = df_006_1.地市
values_006_1 = df_006_1.当月话题数
values_006_2 = df_006_2.上月话题数
values_006_3 = df_006_3.前2月话题数
values_006_4 = df_006_4.前3月话题数
values_006_5 = df_006_5.前4月话题数
values_006_6 = df_006_6.前5月话题数

# 1.创建时间线对象
list_006_city = [city_006[i] for i in range(len(city_006))]
list_values_006_1 = [values_006_1[i] for i in range(len(values_006_1))]
list_values_006_2 = [values_006_2[i] for i in range(len(values_006_2))]
list_values_006_3 = [values_006_3[i] for i in range(len(values_006_3))]
list_values_006_4 = [values_006_4[i] for i in range(len(values_006_4))]
list_values_006_5 = [values_006_5[i] for i in range(len(values_006_5))]
list_values_006_6 = [values_006_6[i] for i in range(len(values_006_6))]

list10 = [list_values_006_6, list_values_006_5, list_values_006_4, list_values_006_3, list_values_006_2,
          list_values_006_1]
dict2_006 = {before_n_mons006[i]: list10[i] for i in range(len(list10))}

tl_006 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
for date_006, data_006 in dict2_006.items():
    bar = (
        Bar(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
            .add_xaxis(list_006_city)
            .add_yaxis("", data_006, label_opts=opts.LabelOpts(is_show=None), stack='stack1')
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=40, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月地市话题数 (时间: {} 月)".format(date_006))
        )

    )
    line = (
        Line(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
            .add_xaxis(list_006_city)
            .add_yaxis("", data_006, label_opts=opts.LabelOpts(),
                       markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=40, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月地市话题数 (时间: {} 月)".format(date_006))
        )
    )

    tl_006.add(bar.overlap(line), "{}月".format(date_006))
    tl_006.add_schema()
tl_006.render("005条形图+折线图月度话题情况.html")

print("条形图+折线图月度话题情况数据: ", dict2_006)
print('条形图+折线图月度话题情况已输出')

# 006表格-上周活跃详情
df_007_ = pd.read_excel('d:/WJ/用户画像输入/上周活跃详情.xlsx')
df_007_ = df_007_.fillna(value=0)
# df_007_[['地市', '包含登录活跃人数']] = df_007_[['地市', '包含登录活跃人数']].applymap(lambda x: str(x).strip())
list_007_1 = []
for line in df_007_:
    list_007_1.append(line)

df_007_x = []

for i in range(len(df_007_)):
    df_007_x.append(df_007_.iloc[i].values)

for i in range(len(df_007_)):
    # df_007_x[i][9] = str(df_007_x[i][9]*100) + '%'
    df_007_x[i][9] = str(round(df_007_x[i][8] * 100 / df_007_x[i][6], 2)) + '%'


def table_base() -> Table:
    table1 = Table()
    table1.add(list_007_1, df_007_x).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="上周活跃详情表")
    )
    return table1
print("表格-上周活跃详情表头数据: ", list_007_1)
print("表格-上周活跃详情表数据: ", df_007_x)
print('表格-上周活跃详情已输出')

#  007-条形图地市时间轴活跃情况
def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons_008 = []
for i in range(6):
    before_n_mons_008.append(previous_months(i, time.strftime("%Y%m", time.localtime())))

# 获取数据列表
df_008_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xlsx')
df_008_ = df_008_.fillna(value=0)
df_008_[['地市', '当月人数', '上月人数', '前2月人数', '前3月人数', '前4月人数', '前5月人数']] = df_008_[
    ['REGION', 'MON_KOL_ACT_USER', 'LAST_1_MON_KOL_ACT_USER', 'LAST_2_MON_KOL_ACT_USER', 'LAST_3_MON_KOL_ACT_USER',
     'LAST_4_MON_KOL_ACT_USER', 'LAST_5_MON_KOL_ACT_USER']].applymap(lambda x: str(x).strip())
mon_008_ = df_008_.地市
list_mon_008_ = [mon_008_[i] for i in range(len(mon_008_))]  # 时间轴：地市
temp_008 = df_008_[['地市', '当月人数', '上月人数', '前2月人数', '前3月人数', '前4月人数', '前5月人数']].set_index("地市")
result_008 = temp_008.stack().reset_index()
result_008.columns = ['地市', '月份', '人数']

df_008_1 = result_008[result_008.地市 == list_mon_008_[0]][['月份', '人数']]
city_008_ = df_008_1.月份  # X轴：月份
values_008_1 = df_008_1.人数
values_008_1.index = [0, 1, 2, 3, 4, 5]

df_008_2 = result_008[result_008.地市 == list_mon_008_[1]][['月份', '人数']]
values_008_2 = df_008_2.人数
values_008_2.index = [0, 1, 2, 3, 4, 5]

df_008_3 = result_008[result_008.地市 == list_mon_008_[2]][['月份', '人数']]
values_008_3 = df_008_3.人数
values_008_3.index = [0, 1, 2, 3, 4, 5]

df_008_4 = result_008[result_008.地市 == list_mon_008_[3]][['月份', '人数']]
values_008_4 = df_008_4.人数
values_008_4.index = [0, 1, 2, 3, 4, 5]

df_008_5 = result_008[result_008.地市 == list_mon_008_[4]][['月份', '人数']]
values_008_5 = df_008_5.人数
values_008_5.index = [0, 1, 2, 3, 4, 5]

df_008_6 = result_008[result_008.地市 == list_mon_008_[5]][['月份', '人数']]
values_008_6 = df_008_6.人数
values_008_6.index = [0, 1, 2, 3, 4, 5]

df_008_7 = result_008[result_008.地市 == list_mon_008_[6]][['月份', '人数']]
values_008_7 = df_008_7.人数
values_008_7.index = [0, 1, 2, 3, 4, 5]

df_008_8 = result_008[result_008.地市 == list_mon_008_[7]][['月份', '人数']]
values_008_8 = df_008_8.人数
values_008_8.index = [0, 1, 2, 3, 4, 5]

df_008_9 = result_008[result_008.地市 == list_mon_008_[8]][['月份', '人数']]
values_008_9 = df_008_9.人数
values_008_9.index = [0, 1, 2, 3, 4, 5]

df_008_10 = result_008[result_008.地市 == list_mon_008_[9]][['月份', '人数']]
values_008_10 = df_008_10.人数
values_008_10.index = [0, 1, 2, 3, 4, 5]

df_008_11 = result_008[result_008.地市 == list_mon_008_[10]][['月份', '人数']]
values_008_11 = df_008_11.人数
values_008_11.index = [0, 1, 2, 3, 4, 5]

# 1.创建时间线对象
list_city_008_ = [city_008_[i] for i in range(len(city_008_))]  # X轴：月份
list_values_008_1 = [values_008_1[i] for i in range(len(values_008_1))]  # Y轴-杭州
list_values_008_2 = [values_008_2[i] for i in range(len(values_008_2))]
list_values_008_3 = [values_008_3[i] for i in range(len(values_008_3))]
list_values_008_4 = [values_008_4[i] for i in range(len(values_008_4))]
list_values_008_5 = [values_008_5[i] for i in range(len(values_008_5))]
list_values_008_6 = [values_008_6[i] for i in range(len(values_008_6))]
list_values_008_7 = [values_008_7[i] for i in range(len(values_008_7))]
list_values_008_8 = [values_008_8[i] for i in range(len(values_008_8))]
list_values_008_9 = [values_008_9[i] for i in range(len(values_008_9))]
list_values_008_10 = [values_008_10[i] for i in range(len(values_008_10))]
list_values_008_11 = [values_008_11[i] for i in range(len(values_008_11))]

list_008_10 = [list_values_008_1, list_values_008_2, list_values_008_3, list_values_008_4, list_values_008_5,
               list_values_008_6, list_values_008_7, list_values_008_8, list_values_008_9, list_values_008_10,
               list_values_008_11]
# dict_008_2 = {before_n_mons_008[i]: list_008_10[i] for i in range(len(list_008_10))}
dict_008_2 = {list_mon_008_[i]: list_008_10[i] for i in range(len(list_008_10))}
tl_008 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
for date_008, data_008 in dict_008_2.items():
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
            .add_xaxis(before_n_mons_008)
            .add_yaxis("", data_008, label_opts=opts.LabelOpts(is_show=True))
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=500, min_=100, item_width=15, item_height=80),
            title_opts=opts.TitleOpts("近6月地市活跃人数 (地市: {} )".format(date_008))
        )

    )
    # line = (
    #     Line(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    #         .add_xaxis(list_city_008_)
    #         .add_yaxis("人数", data_008, label_opts=opts.LabelOpts(),
    #                    markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts("近6月地市活跃人数 (时间: {} 月)".format(date_008))
    #     )
    # )
    #
    # tl_008.add(bar.overlap(line), "{}月".format(date_008))
    tl_008.add(bar, "{}市".format(date_008))
tl_008.render("007条形图地市时间轴活跃情况.html")


print("条形图地市时间轴活跃情况数据: ", dict_008_2)
print('条形图地市时间轴活跃情况已输出')


#  8堆叠图-话题攻克情况
df = pd.read_excel('d:/WJ/用户画像输入/话题列表.xlsx')
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


# X轴坐标数据处理，将X轴输出为列表格式
num_list = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        num_list.append(k[i])
city = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        city.append(k[i - 1])

bar = (
    Bar(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
        .add_xaxis(city)
        .add_yaxis('收集中', ls_sjz, stack='stack1', color='#5aa5b4')
        .add_yaxis('攻克中', ls_gkz, stack='stack1', color='#aab988')
        .add_yaxis('已攻克', ls_ygk, stack='stack1', color='#e5a461')
        .add_yaxis('已关闭', ls_ygb, stack='stack1', color='#db605e')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='话题攻克情况'),
                         # xaxis_opts=opts.AxisOpts(name='地市'),
                         # yaxis_opts=opts.AxisOpts(name='话题'),
                         # visualmap_opts=opts.VisualMapOpts(max_=150),
                         toolbox_opts=opts.ToolboxOpts(),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45})
                         )
)
print("收集中话题：%s" % ls_sjz)
print("攻克中话题：%s" % ls_gkz)
print("已攻克话题：%s" % ls_ygk)
print("已关闭话题：%s" % ls_ygb)
print('堆叠图-话题攻克情况已输出')

# def page_draggable_layout():
#     # page = Page(layout=Page.SimplePageLayout)  #  不可拖动
#     page = Page(layout=Page.DraggablePageLayout)  # 可拖动
#     page.add(
#         #  funnel_markpoint(),
#         tl_001,
#         tl_008,
#         tl_003,
#         #  funnel_2_markpoint(),
#         tl_005,
#         bar,
#         tl_006,
#         table_base()
#     )
#     page.render("index.html")
#
#
# if __name__ == "__main__":
#     page_draggable_layout()
#
# with open(os.path.join(os.path.abspath("."), "index.html"), 'r+', encoding="utf8") as html:
#     html_bf = BeautifulSoup(html, "lxml")
#     divs = html_bf.find_all("div")
#     divs[0][
#         "style"] = "width:1800px;height:2000px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;background: url(bj3.jpg)"  # 修改图表大小、位置、边框
#     divs[1][
#         "style"] = "width:600px;height:400px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Pie大小、位置、边框
#     divs[2][
#         "style"] = "width:600px;height:400px;position:absolute;top:0px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Bar大小、位置、边框
#     divs[3][
#         "style"] = "width:600px;height:400px;position:absolute;top:0px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     divs[4][
#         "style"] = "width:600px;height:400px;position:absolute;top:500px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     divs[5][
#         "style"] = "width:600px;height:400px;position:absolute;top:500px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     divs[6][
#         "style"] = "width:600px;height:400px;position:absolute;top:500px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     divs[7][
#         "style"] = "width:2000px;height:4000px;position:absolute;top:900px;left:0px;border-style:solid;border-color:#00000;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     body["style"] = "background-color:#0000;"
#     # body["style"] = "background: url(bj2.jpg)"
#     div_title = "<div align=\"left\" style=\"width:1200px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#33333\"><b>大咖说</b></div>"  # 修改页面背景色、追加标题
#     body.insert(0, BeautifulSoup(div_title, "lxml").div)
#     html_new = str(html_bf)
#     html.seek(0, 0)
#     html.truncate()
#     html.write(html_new)
#     html.close()

Page.save_resize_html('index.html', cfg_file='chart_config.json', dest='大屏展示.html')
