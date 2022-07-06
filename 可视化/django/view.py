from datetime import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Bar, Line, Grid
from pyecharts.globals import ThemeType

import json
from random import randrange

from django.http import HttpResponse

from pyecharts.charts import Bar
from pyecharts import options as opts


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


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

list_003_10 = [list_values_003_1, list_values_003_2, list_values_003_3, list_values_003_4, list_values_003_5,
               list_values_003_6]
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
tl_003.render("近6月地市活跃人数.html")


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
df_006_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xls')
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

list10 = [list_values_006_1, list_values_006_2, list_values_006_3, list_values_006_4, list_values_006_5,
          list_values_006_6]
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


def grid_table():
    grid = (
        Grid()
            .add(tl_003, grid_opts=opts.GridOpts(pos_left="55%"))
            .add(tl_006, grid_opts=opts.GridOpts(pos_right="55%"))
            .dump_options_with_quotes()
    )
    return grid



class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(grid_table()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("templates/index.html").read())
