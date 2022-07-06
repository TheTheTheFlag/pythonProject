import pandas as pd
import os
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from datetime import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Bar, Line
from pyecharts.globals import ThemeType


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
    print(previous_months(i, time.strftime("%Y%m", time.localtime())))
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))


def get_nday_list_005_(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list_005_ = get_nday_list_005_(8)
print(time_list_005_)
# 获取数据列表
df_005_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市话题类型.xlsx')
df_005_[['话题类型', '当月话题数', '上月话题数', '前2月话题数', '前3月话题数', '前4月话题数', '前5月话题数']] = df_005_[
    ['话题类型', 'MON_TOPIC_TAG', 'LAST_MON_TOPIC_TAG', 'LAST_2_MON_TOPIC_TAG', 'LAST_3_MON_TOPIC_TAG', 'LAST_4_MON_TOPIC_TAG', 'LAST_5_MON_TOPIC_TAG']].applymap(lambda x: str(x).strip())
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
list_005_4 = [list_005_1, list_005_2, list_005_3, list_005_4, list_005_5, list_005_6]

dict1_005 = {before_n_mons[i]: list_005_4[i] for i in range(len(list_005_4))}
# 1.创建时间线对象


tl_005 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
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
        # .set_global_opts(title_opts=opts.TitleOpts("{}话题数".format(date_005)))
    )
    tl_005.add(pie, "{}".format(date_005))
tl_005.render("近6月地市话题类型.html")
