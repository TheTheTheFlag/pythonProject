from datetime import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime
import pyecharts.options as opts
from matplotlib.dviread import Page

from pyecharts.charts import Timeline, Bar, Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 获取数据列表
df_003_ = pd.read_excel('d:/WJ/机器学习输入/score1.xlsx')
print(df_003_.describe())
df_003_1 = df_003_['日期']
df_003_2 = df_003_['得分']
df_003_3 = df_003_['扣分']

#
list_1 = []
for i in range(len(df_003_1)):
    list_1.append(str(df_003_1[i]))
list_2 = []
for i in range(len(df_003_2)):
    list_2.append(df_003_2[i])
list_3 = []
for i in range(len(df_003_3)):
    list_3.append(df_003_3[i])

dict_001_1 = {list_1[i]: list_2[i] for i in range(len(list_1))}
d_order = sorted(dict_001_1.items(), key=lambda x: x[1], reverse=True)
dict_001_2 = {list_1[i]: list_3[i] for i in range(len(list_1))}
d_order1 = sorted(dict_001_2.items(), key=lambda x: x[1], reverse=True)
list_4 = []
for i in range(len(d_order)):
    list_4.append(i)
list_5 = []
for i in range(len(d_order)):
    list_5.append(d_order[i][1])
list_6 = []
for i in range(len(d_order1)):
    list_6.append(d_order1[i][1])
#
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#db5856'}, {offset: 1, color: '#0b8b87'}], false)"
)
line1 = (
    Line(init_opts=opts.InitOpts(width="2000px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_1)
        .add_yaxis("得分", list_2, label_opts=opts.LabelOpts(is_show=False), is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(
                       color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
            name='平均值', type_='average'), opts.MarkLineItem(name='最大值', type_='max'),
            opts.MarkLineItem(name='95', y=95), opts.MarkLineItem(name='70', y=70),
            opts.MarkLineItem(name='30', y=30)]))
        .add_yaxis("扣分", list_3, label_opts=opts.LabelOpts(is_show=False), is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(
                       color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
            name='平均值', type_='average'), opts.MarkLineItem(name='最大值', type_='max'),
            opts.MarkLineItem(name='5', y=5), opts.MarkLineItem(name='30', y=30),
            opts.MarkLineItem(name='55', y=55), opts.MarkLineItem(name='80', y=80)]))
        # .add_yaxis("95分线", ['95'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)  , linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')
        # .add_yaxis("70分线", ['70'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        # .add_yaxis("30分线", ['30'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        .set_global_opts(
        title_opts=opts.TitleOpts("全年故障得分分布1")
    )
)
line1.render("全年故障得分分布1.html")

line2 = (
    Line(init_opts=opts.InitOpts(width="2000px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_4)
        .add_yaxis("得分", list_5, label_opts=opts.LabelOpts(is_show=False), is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(
                       color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
            name='平均值', type_='average'), opts.MarkLineItem(name='最大值', type_='max'),
            opts.MarkLineItem(name='95', y=95), opts.MarkLineItem(name='70', y=70),
            opts.MarkLineItem(name='30', y=30)]))
        .add_yaxis("扣分", list_6, label_opts=opts.LabelOpts(is_show=False), is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(
                       color=JsCode(area_color_js), opacity=1), markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(
            name='平均值', type_='average'), opts.MarkLineItem(name='最大值', type_='max'),
            opts.MarkLineItem(name='5', y=5), opts.MarkLineItem(name='30', y=30),
            opts.MarkLineItem(name='55', y=55), opts.MarkLineItem(name='80', y=80)]))
        # .add_yaxis("95分线", ['95'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)  , linestyle_opts=opts.LineStyleOpts(color='white', type_='dashed')
        # .add_yaxis("70分线", ['70'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        # .add_yaxis("30分线", ['30'] * 31, label_opts=opts.LabelOpts(is_show=False), is_smooth=True)
        .set_global_opts(
        title_opts=opts.TitleOpts("全年故障得分分布2")
    )
)
line2.render("全年故障得分分布2.html")

