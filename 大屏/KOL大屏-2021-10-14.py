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


list_001_1 = [[city_001[i] + "市", int(float(values_001_1[i]))] for i in range(len(city_001))]
list_001_2 = [[city_001[i] + "市", int(float(values_001_2[i]))] for i in range(len(city_001))]
list_001_3 = [[city_001[i] + "市", int(float(values_001_3[i]))] for i in range(len(city_001))]
list_001_4 = [[city_001[i] + "市", int(float(values_001_4[i]))] for i in range(len(city_001))]
list_001_5 = [[city_001[i] + "市", int(float(values_001_5[i]))] for i in range(len(city_001))]
list_001_6 = [[city_001[i] + "市", int(float(values_001_6[i]))] for i in range(len(city_001))]
list_001_7 = [[city_001[i] + "市", int(float(values_001_7[i]))] for i in range(len(city_001))]
list_001_8 = [[city_001[i] + "市", int(float(values_001_8[i]))] for i in range(len(city_001))]
list_001_4 = [list_001_1, list_001_2, list_001_3, list_001_4, list_001_5, list_001_6, list_001_7, list_001_8]

dict_001_1 = {time_list[i]: list_001_4[i] for i in range(len(list_001_4))}


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
# timeline_base().render("001玫瑰图-7天活跃情况.html")

# 2:近6月地市活跃人数条形图Timeline(Bar)
# 获取数据列表
df_008_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xls')
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


def timeline_base_02() -> Timeline:
    tl_02 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
    for date_008, data_008 in dict_008_2.items():
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
                .add_xaxis(before_n_mons)
                .add_yaxis("", data_008, label_opts=opts.LabelOpts(is_show=True))
                # .reversal_axis()  # 坐标轴反转
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=500, min_=100, item_width=15, item_height=80),
                title_opts=opts.TitleOpts("近6月地市活跃人数 (地市: {} )".format(date_008))
            )

        )
        tl_02.add(bar, "{}市".format(date_008))
    print("条形图地市时间轴活跃情况数据: ", dict_008_2)
    print('条形图地市时间轴活跃情况已输出')
    return tl_02


# 3:近6月地市活跃人数条形图+折线图Timeline(Bar+line)
# 获取数据列表
df_003_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xls')
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
dict_003_2 = {before_n_mons[i]: list_003_10[i] for i in range(len(list_003_10))}


def timeline_base_03() -> Timeline:
    tl_002 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
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

        tl_002.add(bar.overlap(line), "{}月".format(date_003))
        tl_002.add_schema()
    # tl_002.render("002-条形图+折线图人员活跃情况.html")
    print("条形图+折线图人员活跃情况数据: ", dict_003_2)
    print('条形图+折线图人员活跃情况已输出')
    return tl_002


# 4:近6月各类型话题数玫瑰图Timeline(Pie)
# 获取数据列表
df_005_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市话题类型.xls')
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

dict1_005 = {before_n_mons[i]: list_005_4[i] for i in range(len(list_005_4))}


def timeline_base_04() -> Timeline:
    tl_003 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
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
        tl_003.add(pie, "{}".format(date_005))
        tl_003.add_schema()
    # tl_005.render("004玫瑰图-话题类型情况.html")
    print("玫瑰图-话题类型情况数据: ", dict1_005)
    print('玫瑰图-话题类型情况已输出')
    return tl_003


#  5:话题攻克情况堆叠图
df = pd.read_excel('d:/WJ/用户画像输入/话题攻克情况.xls')


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
city = excel_one_line_to_list(column.index('归属地市'))
ls_sjz = excel_one_line_to_list(column.index('收集中'))
ls_gkz = excel_one_line_to_list(column.index('攻克中'))
ls_ygk = excel_one_line_to_list(column.index('已攻克'))
ls_ygb = excel_one_line_to_list(column.index('已关闭'))


def Bar_base_01() -> Bar:
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
    print("地市：%s" % city)
    print("收集中话题：%s" % ls_sjz)
    print("攻克中话题：%s" % ls_gkz)
    print("已攻克话题：%s" % ls_ygk)
    print("已关闭话题：%s" % ls_ygb)
    print('堆叠图-话题攻克情况已输出')
    return bar


# 6:近6月地市话题数条形图+折线图(Bar+line)
# 获取数据列表
df_006_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xls')
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
dict2_006 = {before_n_mons[i]: list10[i] for i in range(len(list10))}


def timeline_base_05() -> Timeline:
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
    print("条形图+折线图月度话题情况数据: ", dict2_006)
    print('条形图+折线图月度话题情况已输出')
    return tl_006


# 7:上周活跃详情表格
df_007_ = pd.read_excel('d:/WJ/用户画像输入/上周活跃详情.xls')
order = ['地市', '包含登录活跃人数', '不包含登录活跃人数', '创建话题数', '创建话题类型', '浏览人数', '浏览次数', '留言人数', '留言次数', '登录人数', '登录次数', '留言率',
         '关注人数', '关注次数', '点赞人数', '点赞次数']
# 对于列进行重排序
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


def table_base() -> Table:
    table1 = Table()
    table1.add(list_007_1, df_007_x).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="上周活跃详情表")
    )
    return table1


print("表格-上周活跃详情表头数据: ", list_007_1)
print("表格-上周活跃详情表数据: ", df_007_x)
print('表格-上周活跃详情已输出')


def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)  #  不可拖动
    # page = Page(layout=Page.DraggablePageLayout)  # 可拖动
    page.add(
        timeline_base_01(),
        timeline_base_02(),
        timeline_base_03(),
        timeline_base_04(),
        Bar_base_01(),
        timeline_base_05(),
        table_base()
    )
    page.render("index.html")


if __name__ == "__main__":
    page_draggable_layout()

with open(os.path.join(os.path.abspath("."), "index.html"), 'r+', encoding="utf8") as html:
    html_bf = BeautifulSoup(html, "lxml")
    divs = html_bf.find_all("div")
    divs[0][
        "style"] = "width:1000px;height:2000px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;background: url(bj3.jpg)"  # 修改图表大小、位置、边框
    divs[1][
        "style"] = "width:640px;height:400px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Pie大小、位置、边框
    divs[2][
        "style"] = "width:640px;height:400px;position:absolute;top:0px;left:640px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Bar大小、位置、边框
    divs[3][
        "style"] = "width:640px;height:400px;position:absolute;top:0px;left:1280px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
    #body = html_bf.find("body")
    divs[4][
        "style"] = "width:640px;height:400px;position:absolute;top:500px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
    #body = html_bf.find("body")
    divs[5][
        "style"] = "width:640px;height:400px;position:absolute;top:500px;left:640px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
    #body = html_bf.find("body")
    divs[6][
        "style"] = "width:640px;height:400px;position:absolute;top:500px;left:1280px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
    #body = html_bf.find("body")
    divs[7][
        "style"] = "width:1800px;height:4000px;position:absolute;top:900px;left:0px;border-style:solid;border-color:#00000;border-width:0px;"  # 修改Map大小、位置、边框
    body = html_bf.find("body")
    body["style"] = "background-color:#0000;"
    # body["style"] = "background: url(bj2.jpg)"
    div_title = "<div align=\"left\" style=\"width:1200px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#33333\"><b>大咖说</b></div>"  # 修改页面背景色、追加标题
    body.insert(0, BeautifulSoup(div_title, "lxml").div)
    html_new = str(html_bf)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    # refesh = '<meta http-equiv="Refresh" content="3";/>  <!--页面每1秒刷新一次-->'
    # html.write(refesh)
    html.close()

# Page.save_resize_html('index.html', cfg_file='chart_config.json', dest='大屏展示.html')
