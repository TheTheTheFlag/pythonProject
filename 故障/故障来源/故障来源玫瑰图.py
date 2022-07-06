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
df_001 = pd.read_excel('d:/WJ/机器学习输入/故障来源.xlsx')
##故障类别
df = df_001[['故障等级', '数量']]
df = df.groupby("故障等级", as_index=False).sum({'数量': 'count'})


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_F5_1 = excel_one_line_to_list(column.index('故障等级'))
df_F5_2 = excel_one_line_to_list(column.index('数量'))

data = [[df_F5_1[i], df_F5_2[i]] for i in range(len(df_F5_1))]
pie0 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="故障类别"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie0.render("故障类别.html")

##F4及以上
df_F5 = df_001[df_001.故障等级 == 'F4及以上'][['来源', '数量']]
df = df_F5


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_F5_1 = excel_one_line_to_list(column.index('来源'))
df_F5_2 = excel_one_line_to_list(column.index('数量'))
data = [[df_F5_1[i], df_F5_2[i]] for i in range(len(df_F5_1))]
pie1 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="F4及以上故障来源"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie1.render("F4及以上故障来源.html")

##G5F5
df_F5 = df_001[df_001.故障等级 == 'G5F5'][['来源', '数量']]
df = df_F5


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_F5_1 = excel_one_line_to_list(column.index('来源'))
df_F5_2 = excel_one_line_to_list(column.index('数量'))
data = [[df_F5_1[i], df_F5_2[i]] for i in range(len(df_F5_1))]
pie2 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="G5F5故障来源"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie2.render("G5F5故障来源.html")

# 获取数据列表
df_002 = pd.read_excel('d:/WJ/机器学习输入/转派情况.xlsx')
##转派大组
df = df_002[['转派大组', 'NUM1']]
df = df.groupby("转派大组", as_index=False).sum({'NUM1': 'count'})


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_ZPDZ_1 = excel_one_line_to_list(column.index('转派大组'))
df_ZPDZ_2 = excel_one_line_to_list(column.index('NUM1'))

data = [[df_ZPDZ_1[i], df_ZPDZ_2[i]] for i in range(len(df_ZPDZ_1))]
pie3 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="转派情况-大组"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie3.render("转派情况-大组.html")

##转派小组
df = df_002[['转派小组', 'NUM2']]
df = df.groupby("转派小组", as_index=False).sum({'NUM2': 'count'})


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_ZPXZ_1 = excel_one_line_to_list(column.index('转派小组'))
df_ZPXZ_2 = excel_one_line_to_list(column.index('NUM2'))

data = [[df_ZPXZ_1[i], df_ZPXZ_2[i]] for i in range(len(df_ZPXZ_1))]
pie4 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="转派情况-小组"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie4.render("转派情况-小组.html")

##转派人
df = df_002[['转派人', 'NUM3']]
df = df.groupby("转派人", as_index=False).sum({'NUM3': 'count'})


def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
df_ZPR_1 = excel_one_line_to_list(column.index('转派人'))
df_ZPR_2 = excel_one_line_to_list(column.index('NUM3'))

data = [[df_ZPR_1[i], df_ZPR_2[i]] for i in range(len(df_ZPR_1))]
pie5 = (
    Pie(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        "数量",
        data,
        rosetype="radius",
        radius=["30%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {c} ({d}%)",
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="转派情况-处理人"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="0%"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
)
#pie5.render("转派情况-处理人.html")

def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)  # 不可拖动
    # page = Page(layout=Page.DraggablePageLayout)  # 可拖动
    page.add(
        pie0,
        pie1,
        pie2,
        pie3,
        pie4,
        pie5,
    )
    page.render("GOC.html")


if __name__ == "__main__":
    page_draggable_layout()

with open(os.path.join(os.path.abspath(".."), "GOC.html"), 'r+', encoding="utf8") as html:
    html_bf = BeautifulSoup(html, "lxml")
    divs = html_bf.find_all("div")
    divs[0][
        "style"] = "width:1800px;height:1000px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;background: url(bj3.jpg)"  # 修改图表大小、位置、边框
    divs[1][
        "style"] = "width:600px;height:400px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Pie大小、位置、边框
    divs[2][
        "style"] = "width:600px;height:400px;position:absolute;top:0px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Bar大小、位置、边框
    divs[3][
        "style"] = "width:600px;height:400px;position:absolute;top:0px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
    # body = html_bf.find("body")
    divs[4][
        "style"] = "width:600px;height:400px;position:absolute;top:500px;left:0px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
    # body = html_bf.find("body")
    divs[5][
        "style"] = "width:600px;height:400px;position:absolute;top:500px;left:600px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
    # body = html_bf.find("body")
    divs[6][
        "style"] = "width:600px;height:400px;position:absolute;top:500px;left:1200px;border-style:solid;border-color:#444444;border-width:3px;"  # 修改Map大小、位置、边框
    # body = html_bf.find("body")
    # divs[7][
    #     "style"] = "width:2000px;height:4000px;position:absolute;top:900px;left:0px;border-style:solid;border-color:#00000;border-width:3px;"  # 修改Map大小、位置、边框
    body = html_bf.find("body")
    body["style"] = "background-color:#333333;"  # 背景顔色
    # body["style"] = "background: url(bj2.jpg)"
    div_title = "<div align=\"left\" style=\"width:1200px;\">\n<span style=\"font-size:32px;font face=\'黑体\';color:#FFF\"><b>GOC</b></div>"  # 修改页面背景色、追加标题
    body.insert(0, BeautifulSoup(div_title, "lxml").div)
    html_new = str(html_bf)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
