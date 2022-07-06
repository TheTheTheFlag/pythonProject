import body as body
import pandas as pd
import os
import datetime
import pyecharts.options as opts
from bs4 import BeautifulSoup
from pyecharts.charts import Timeline, Bar, Line, Funnel, Pie, Page

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

# 获取数据列表
df = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df1 = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')

df[['处理组别', '数量']] = df[['关联处理小组', 'BOC质检情况']]
df1[['处理组别', '数量']] = df1[['关联处理小组', 'BOC质检情况']]

df = df[df.数量 == '驳回']
df1 = df1[df1.数量 == '通过']

df['数量'] = 1
df1['数量'] = 1

df = df[['处理组别', '数量']]
df = df.groupby("处理组别", as_index=False).sum({'数量': 'count'})

df1 = df1[['处理组别', '数量']]
df1 = df1.groupby("处理组别", as_index=False).sum({'数量': 'count'})


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
list_1 = excel_one_line_to_list(column.index('处理组别'))
list_2 = excel_one_line_to_list(column.index('数量'))
print(max(list_2))

def excel_one_line_to_list1(a):
    df_li = df1.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column1 = list(df1.columns)
list_7 = excel_one_line_to_list1(column1.index('处理组别'))
list_8 = excel_one_line_to_list1(column1.index('数量'))


dict_001_1 = {list_1[i]: list_2[i] for i in range(len(list_1))}
d_order = sorted(dict_001_1.items(), key=lambda x: x[1], reverse=False)
list_4 = []
for i in range(len(d_order)):
    list_4.append(d_order[i][0])
list_5 = []
for i in range(len(d_order)):
    list_5.append(d_order[i][1])

dict_001_2 = {list_7[i]: list_8[i] for i in range(len(list_7))}
d_order1 = sorted(dict_001_2.items(), key=lambda x: x[1], reverse=False)
list_9 = []
for i in range(len(d_order1)):
    list_9.append(d_order1[i][0])
list_10 = []
for i in range(len(d_order1)):
    list_10.append(d_order1[i][1])

area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#db5856'}, {offset: 1, color: '#0b8b87'}], false)"
)
bar1 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_4)
        .add_yaxis("驳回数量", list_5, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检驳回情况'),
                             #  datazoom_opts=opts.DataZoomOpts(),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                             visualmap_opts=opts.VisualMapOpts(max_=max(list_2), item_width=15, item_height=80)
                             )
)

#bar1.render("故障质检驳回数量.html")

bar2= (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_9)
        .add_yaxis("通过数量", list_10, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检通过情况'),
                             #  datazoom_opts=opts.DataZoomOpts(),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                             visualmap_opts=opts.VisualMapOpts(max_=max(list_10), item_width=15, item_height=80)
                             )
)

#bar2.render("故障质检通过数量.html")


def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)  # 不可拖动
    #page = Page(layout=Page.DraggablePageLayout)  # 可拖动
    page.add(
        bar1,
        bar2,
    )
    page.render("GOC.html")


if __name__ == "__main__":
    page_draggable_layout()

# with open(os.path.join(os.path.abspath("."), "GOC.html"), 'r+', encoding="utf8") as html:
#     html_bf = BeautifulSoup(html, "lxml")
#     divs = html_bf.find_all("div")
#     divs[0][
#         "style"] = "width:1800px;height:1800px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;background: url(bj3.jpg)"  # 修改图表大小、位置、边框
#     divs[1][
#         "style"] = "width:1800px;height:900px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Pie大小、位置、边框
#     divs[2][
#         "style"] = "width:1800px;height:1800px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Bar大小、位置、边框
#     # divs[3][
#     #     "style"] = "width:600px;height:400px;position:absolute;top:0px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     # # body = html_bf.find("body")
#     # divs[4][
#     #     "style"] = "width:600px;height:400px;position:absolute;top:500px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     # # body = html_bf.find("body")
#     # divs[5][
#     #     "style"] = "width:600px;height:400px;position:absolute;top:500px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     # # body = html_bf.find("body")
#     # divs[6][
#     #     "style"] = "width:600px;height:400px;position:absolute;top:500px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
#     # body = html_bf.find("body")
#     # divs[7][
#     #     "style"] = "width:2000px;height:4000px;position:absolute;top:900px;left:0px;border-style:solid;border-color:#00000;border-width:3px;"  # 修改Map大小、位置、边框
#     body = html_bf.find("body")
#     body["style"] = "background-color:#FFF;"  # 背景顔色
#     # body["style"] = "background: url(bj2.jpg)"
#     div_title = "<div align=\"left\" style=\"width:1200px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#FFF\"><b>GOC</b></div>"  # 修改页面背景色、追加标题
#     body.insert(0, BeautifulSoup(div_title, "lxml").div)
#     html_new = str(html_bf)
#     html.seek(0, 0)
#     html.truncate()
#     html.write(html_new)
#     html.close()


