from datetime import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Bar, Line
from pyecharts.globals import ThemeType


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
    print(previous_months(i, time.strftime("%Y%m", time.localtime())))
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))

# 获取数据列表
df_006_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xlsx')
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

list10 = [list_values_006_1, list_values_006_2, list_values_006_3, list_values_006_4, list_values_006_5, list_values_006_6]
dict2_006 = {before_n_mons[i]: list10[i] for i in range(len(list10))}

tl_006 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
print(list_006_city)
for date_006, data_006 in dict2_006.items():
    print(date_006)
    print(data_006)
    bar = (
        Bar(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
            .add_xaxis(list_006_city)
            .add_yaxis("", data_006, label_opts=opts.LabelOpts(is_show=None), stack='stack1')
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            title_opts=opts.TitleOpts("近6月地市话题数 (时间: {} 月)".format(date_006))
        )

    )
    line = (
        Line(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
            .add_xaxis(list_006_city)
            .add_yaxis("", data_006, label_opts=opts.LabelOpts())
            .set_global_opts(
            title_opts=opts.TitleOpts("近6月地市话题数 (时间: {} 月)".format(date_006))
        )
    )

    tl_006.add(bar.overlap(line), "{}月".format(date_006))
tl_006.render("地市话题攻克情况.html")
