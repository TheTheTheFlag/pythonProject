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
df_003_ = pd.read_excel('d:/WJ/用户画像输入/近6月地市活跃人数.xls')
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

list_003_10 = [list_values_003_1, list_values_003_2, list_values_003_3, list_values_003_4, list_values_003_5, list_values_003_6]
dict_003_2 = {before_n_mons[i]: list_003_10[i] for i in range(len(list_003_10))}

tl_003 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
print(list_city_003_)
for date_003, data_003 in dict_003_2.items():
    print(date_003)
    print(data_003)
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add_xaxis(list_city_003_)
            .add_yaxis("人数", data_003, label_opts=opts.LabelOpts(is_show=None))
            # .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            title_opts=opts.TitleOpts("近6月地市活跃人数 (时间: {} 月)".format(date_003))
        )

    )
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add_xaxis(list_city_003_)
            .add_yaxis("人数", data_003, label_opts=opts.LabelOpts())
            .set_global_opts(
            title_opts=opts.TitleOpts("近6月地市活跃人数 (时间: {} 月)".format(date_003))
        )
    )

    tl_003.add(bar.overlap(line), "{}月".format(date_003))
tl_003.render("近6月地市活跃人数2.html")
