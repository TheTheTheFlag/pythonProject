from datetime import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Bar, Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 获取数据列表
df_003_ = pd.read_excel('d:/WJ/机器学习输入/score.xlsx')
print(df_003_.describe())
df_003_1 = df_003_['日期']
df_003_2 = df_003_['七月得分']
df_003_3 = df_003_['八月得分']
df_003_4 = df_003_['九月得分']
df_003_5 = df_003_['十月得分']
#
list_1 = []
for i in range(len(df_003_1)):
    list_1.append(str(df_003_1[i]))
print(list_1)
list_2 = []
for i in range(len(df_003_2)):
    list_2.append(df_003_2[i])
print(list_2)
list_3 = []
for i in range(len(df_003_3)):
    list_3.append(df_003_3[i])
print(list_3)
list_4 = []
for i in range(len(df_003_4)):
    list_4.append(df_003_4[i])
print(list_4)
list_5 = []
for i in range(len(df_003_5)):
    list_5.append(df_003_5[i])
print(list_5)
#
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#db5856'}, {offset: 1, color: '#0b8b87'}], false)"
)
line = (
    Line(init_opts=opts.InitOpts())
        .add_xaxis(xaxis_data=list_1)
        .add_yaxis("7月得分", list_2, label_opts=opts.LabelOpts(is_show=False), is_smooth=True, areastyle_opts=opts.AreaStyleOpts(
        color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
        type_='average')], linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')))
        .add_yaxis("8月得分", list_3, label_opts=opts.LabelOpts(is_show=False), is_smooth=True, areastyle_opts=opts.AreaStyleOpts(
        color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
        type_='average')], linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')))
        .add_yaxis("9月得分", list_4, label_opts=opts.LabelOpts(is_show=False), is_smooth=True, areastyle_opts=opts.AreaStyleOpts(
        color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
        type_='average')], linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')))
        .add_yaxis("10月得分", list_5, label_opts=opts.LabelOpts(is_show=False), is_smooth=True, areastyle_opts=opts.AreaStyleOpts(
        color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
        type_='average')], linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')))
        .add_yaxis("95分线", ['95'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        .add_yaxis("70分线", ['70'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        .add_yaxis("30分线", ['30'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        .set_global_opts(
        title_opts=opts.TitleOpts("故障得分")
    )
)

line.render("故障得分.html")
