from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.charts import Page, Bar, Funnel, Map
import os as os
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Pie, Bar

# 获取日期列表
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list = get_nday_list(8)
print(time_list)
# 获取数据列表
df = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xlsx')
df[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']] = df[
    ['地市', '7天前人数', '6天前人数', '5天前人数', '4天前人数', '3天前人数', '2天前人数', '昨天人数', '当天人数']].applymap(lambda x: str(x).strip())
df1 = df[['地市', '前7天人数']]
df2 = df[['地市', '前6天人数']]
df3 = df[['地市', '前5天人数']]
df4 = df[['地市', '前4天人数']]
df5 = df[['地市', '前3天人数']]
df6 = df[['地市', '前2天人数']]
df7 = df[['地市', '前1天人数']]
df8 = df[['地市', '今天人数']]

city = df1.地市
values1 = df1.前7天人数
values2 = df2.前6天人数
values3 = df3.前5天人数
values4 = df4.前4天人数
values5 = df5.前3天人数
values6 = df6.前2天人数
values7 = df7.前1天人数
values8 = df8.今天人数

# 1.创建时间线对象
list_city = [city[i] for i in range(len(city))]
list_values1 = [values1[i] for i in range(len(values1))]
list_values2 = [values2[i] for i in range(len(values2))]
list_values3 = [values3[i] for i in range(len(values3))]
list_values4 = [values4[i] for i in range(len(values4))]
list_values5 = [values5[i] for i in range(len(values5))]
list_values6 = [values6[i] for i in range(len(values6))]
list_values7 = [values7[i] for i in range(len(values7))]
list_values8 = [values8[i] for i in range(len(values8))]

list10 = [list_values1, list_values2, list_values3, list_values4, list_values5, list_values6, list_values7,
          list_values8]
dict2 = {time_list[i]: list10[i] for i in range(len(list10))}

list1 = [[city[i] + "市", int(values1[i])] for i in range(len(city))]
list2 = [[city[i] + "市", int(values2[i])] for i in range(len(city))]
list3 = [[city[i] + "市", int(values3[i])] for i in range(len(city))]
list4 = [[city[i] + "市", int(values4[i])] for i in range(len(city))]
list5 = [[city[i] + "市", int(values5[i])] for i in range(len(city))]
list6 = [[city[i] + "市", int(values6[i])] for i in range(len(city))]
list7 = [[city[i] + "市", int(values7[i])] for i in range(len(city))]
list8 = [[city[i] + "市", int(values8[i])] for i in range(len(city))]

list4 = [list1, list2, list3, list4, list5, list6, list7, list8]

dict1 = {time_list[i]: list4[i] for i in range(len(list4))}

tl = Timeline()

tl = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
for date, data in dict1.items():
    # for i in time_list:
    pie = (
        Pie()
            .add(
            "",
            # [list(z) for z in zip(city, values1)],
            data,
            rosetype="radius",
            radius=["30%", "55%"],
        )
         #.set_global_opts(title_opts=opts.TitleOpts("Pie-{}日活跃人数".format(date)))
    )
    tl.add(pie, "{}".format(date))
#tl.render("timeline_pie.html")

tl2 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
for date, data in dict2.items():
    bar = (
        Bar()
            .add_xaxis(list_city)
            .add_yaxis("人数", data, label_opts=opts.LabelOpts(position="right"))
            .reversal_axis()  # 坐标轴反转
            .set_global_opts(
            #title_opts=opts.TitleOpts("Bar-{}日活跃人数".format(date))
        )
    )
    tl2.add(bar, "{}日".format(date))
#tl2.render("timeline_bar_reversal.html")

tl3 = Timeline(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
for date, data in dict1.items():
    # for i in range(2015, 2020):
    map0 = (
        Map()
            .add("活跃人数", data, "浙江")
            .set_global_opts(
            #title_opts=opts.TitleOpts(title="Map-{}日活跃人数".format(date)),
            visualmap_opts=opts.VisualMapOpts(max_=50),
        )
    )
    tl3.add(map0, "{}日".format(date))
#tl3.render("timeline_map.html")


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        tl,  # pie
        tl2,  # bar
        tl3  # map
    )
    page.render("page_draggable_layout.html")


if __name__ == "__main__":
    page_draggable_layout()

with open(os.path.join(os.path.abspath("."),"page_draggable_layout.html"),'r+',encoding="utf8") as html:
    html_bf=BeautifulSoup(html,"lxml")
    divs=html_bf.find_all("div")
    divs[0]["style"]="width:600px;height:400px;position:absolute;top:70px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"    #修改图表大小、位置、边框
    divs[1]["style"]="width:600px;height:400px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  #修改Pie大小、位置、边框
    divs[2]["style"]="width:600px;height:400px;position:absolute;top:0px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  #修改Bar大小、位置、边框
    divs[3]["style"]="width:600px;height:400px;position:absolute;top:0px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  #修改Map大小、位置、边框
    body=html_bf.find("body")
    body["style"]="background-color:#333333;"
    div_title="<div align=\"center\" style=\"width:1200px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#FFFFFF\"><b>JXH</b></div>"    #修改页面背景色、追加标题
    body.insert(0,BeautifulSoup(div_title,"lxml").div)
    html_new=str(html_bf)
    html.seek(0,0)
    html.truncate()
    html.write(html_new)
    html.close()