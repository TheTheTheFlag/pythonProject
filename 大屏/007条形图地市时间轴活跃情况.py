from bs4 import BeautifulSoup
# from matplotlib.dviread import Page
from numpy.distutils.fcompiler import none
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime
from pyecharts.charts import Timeline, Bar, Line, Funnel, Pie, Page
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import pandas as pd
import time
# from datetime import datetime
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import os


#  007-条形图地市时间轴活跃情况
def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons_008 = []
for i in range(6):
    print(previous_months(i, time.strftime("%Y%m", time.localtime())))
    before_n_mons_008.append(previous_months(i, time.strftime("%Y%m", time.localtime())))

# 获取数据列表
df_008_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xlsx')
df_008_ = df_008_.fillna(value=0)
df_008_[['地市', '当月人数', '上月人数', '前2月人数', '前3月人数', '前4月人数', '前5月人数']] = df_008_[
    ['REGION', 'MON_KOL_ACT_USER', 'LAST_1_MON_KOL_ACT_USER', 'LAST_2_MON_KOL_ACT_USER', 'LAST_3_MON_KOL_ACT_USER',
     'LAST_4_MON_KOL_ACT_USER', 'LAST_5_MON_KOL_ACT_USER']].applymap(lambda x: str(x).strip())
mon_008_ = df_008_.地市
list_mon_008_ = [mon_008_[i] for i in range(len(mon_008_))]  # 时间轴：地市
print(list_mon_008_)
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
print(list_city_008_)
tl_008 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
for date_008, data_008 in dict_008_2.items():
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
            .add_xaxis(before_n_mons_008)
            .add_yaxis("", data_008, label_opts=opts.LabelOpts(is_show=True))
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
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
