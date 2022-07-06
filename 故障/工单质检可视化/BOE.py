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
##所有数据的量
df0 = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df0 = df0[['处理组别', '数量']] = df0[['关联处理小组', 'BOC质检情况']]
df0['数量'] = 1
df0 = df0[['处理组别', '数量']]
df0 = df0.groupby("处理组别", as_index=False).sum({'数量': 'count'})

##驳回的量
df = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df[['处理组别', '驳回数量']] = df[['关联处理小组', 'BOC质检情况']]
df = df[df.驳回数量 == '驳回']
df['驳回数量'] = 1
df = df[['处理组别', '驳回数量']]
df = df.groupby("处理组别", as_index=False).sum({'驳回数量': 'count'})

##通过的量
df1 = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df1[['处理组别', '通过数量']] = df1[['关联处理小组', 'BOC质检情况']]
df1 = df1[df1.通过数量 == '通过']
df1['通过数量'] = 1
df1 = df1[['处理组别', '通过数量']]
df1 = df1.groupby("处理组别", as_index=False).sum({'通过数量': 'count'})

##关联全量和驳回的量
df2 = pd.merge(df0, df, on='处理组别', how='left')
df2 = df2.fillna(value=0)
df2['驳回率'] = round(df2['驳回数量'] / df2['数量'], 2) * 100

##BOE/SRE驳回的量
df3 = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df4 = df3
df5 = df3
df6 = df5
df3[['回复人', '关联处理大组', '处理组别', '驳回数量']] = df3[['判断后回复人', '关联处理大组', '关联处理小组', 'BOC质检情况']]
# df3 = df3[df3.驳回数量 == '驳回']
df3 = df3[(df3.关联处理大组 == 'BOE') & (df3.驳回数量 == '驳回')]
df4 = df4[(df4.关联处理大组 == 'SRE') & (df4.驳回数量 == '驳回')]
df5 = df5[df5.关联处理大组 == 'BOE']
df6 = df6[df6.关联处理大组 == 'SRE']
df3 = df3.append(df4)  # BOESRE驳回量
df5 = df5.append(df6)  # BOESRE全量
df3['驳回数量'] = 1
df3 = df3[['处理组别', '回复人', '驳回数量']]
df3 = df3.groupby("回复人", as_index=False).sum({'驳回数量': 'count'})

df5['数量'] = 1
df5 = df5[['回复人', '数量']]
df5 = df5.groupby("回复人", as_index=False).sum({'数量': 'count'})
df5 = pd.merge(df5, df3, on='回复人', how='left')
df5 = df5.fillna(value=0)
df5['驳回率'] = round(df5['驳回数量'] / df5['数量'], 2) * 100
df3.to_excel('d:/WJ/机器学习输入/BOE驳回.xlsx')

##BOE/SRE通过的量
df7 = pd.read_excel('d:/WJ/机器学习输入/duty.xlsx')
df8 = df7
df7[['回复人', '关联处理大组', '处理组别', '驳回数量']] = df7[['判断后回复人', '关联处理大组', '关联处理小组', 'BOC质检情况']]
df7 = df7[(df7.关联处理大组 == 'BOE') & (df7.驳回数量 == '通过')]
df8 = df8[(df8.关联处理大组 == 'SRE') & (df8.驳回数量 == '通过')]

df7 = df7.append(df8)  # BOESRE通过量
df7['通过数量'] = 1
df7 = df7[['回复人', '关联处理大组', '处理组别', '通过数量']]
df77 = df7
#print(df7)
df7.to_excel('d:/WJ/机器学习输入/BOE&SRE通过.xlsx')
df7 = df7.groupby("回复人", as_index=False).sum({'通过数量': 'count'})
df7.to_excel('d:/WJ/机器学习输入/BOE通过.xlsx')

#####
def excel_one_line_to_list(a):
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column = list(df.columns)
list_1 = excel_one_line_to_list(column.index('处理组别'))
list_2 = excel_one_line_to_list(column.index('驳回数量'))

dict_001_1 = {list_1[i]: list_2[i] for i in range(len(list_1))}
d_order = sorted(dict_001_1.items(), key=lambda x: x[1], reverse=False)
list_4 = []
for i in range(len(d_order)):
    list_4.append(d_order[i][0])
list_5 = []
for i in range(len(d_order)):
    list_5.append(d_order[i][1])


#####
def excel_one_line_to_list1(a):
    df_li = df1.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column1 = list(df1.columns)
list_7 = excel_one_line_to_list1(column1.index('处理组别'))
list_8 = excel_one_line_to_list1(column1.index('通过数量'))

dict_001_2 = {list_7[i]: list_8[i] for i in range(len(list_7))}
d_order1 = sorted(dict_001_2.items(), key=lambda x: x[1], reverse=False)
list_9 = []
for i in range(len(d_order1)):
    list_9.append(d_order1[i][0])
list_10 = []
for i in range(len(d_order1)):
    list_10.append(d_order1[i][1])


#####
def excel_one_line_to_list2(a):
    df_li = df2.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column2 = list(df2.columns)
list_bhx = excel_one_line_to_list2(column2.index('处理组别'))
list_bhy = excel_one_line_to_list2(column2.index('驳回率'))

dict_bhl = {list_bhx[i]: list_bhy[i] for i in range(len(list_bhx))}
d_order_bhl = sorted(dict_bhl.items(), key=lambda x: x[1], reverse=False)
list_bhl_x = []
for i in range(len(d_order_bhl)):
    list_bhl_x.append(d_order_bhl[i][0])
list_bhl_y = []
for i in range(len(d_order_bhl)):
    list_bhl_y.append(d_order_bhl[i][1])


#####BOE/SRE
def excel_one_line_to_list3(a):
    df_li = df3.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column3 = list(df3.columns)
list_bsx = excel_one_line_to_list3(column3.index('回复人'))
list_bsy = excel_one_line_to_list3(column3.index('驳回数量'))

dict_bsl = {list_bsx[i]: list_bsy[i] for i in range(len(list_bsx))}
d_order_bsl = sorted(dict_bsl.items(), key=lambda x: x[1], reverse=False)
list_bsl_x = []
for i in range(len(d_order_bsl)):
    list_bsl_x.append(d_order_bsl[i][0])
list_bsl_y = []
for i in range(len(d_order_bsl)):
    list_bsl_y.append(d_order_bsl[i][1])
list_bsl_x = list_bsl_x[-10:]
list_bsl_y = list_bsl_y[-10:]


#####BOE/SRE驳回率
def excel_one_line_to_list4(a):
    df_li = df5.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column4 = list(df5.columns)
list_bs_bhl_x = excel_one_line_to_list4(column4.index('回复人'))
list_bs_bhl_y = excel_one_line_to_list4(column4.index('驳回率'))

dict_bsl_2 = {list_bs_bhl_x[i]: list_bs_bhl_y[i] for i in range(len(list_bs_bhl_x))}
d_order_bsl_2 = sorted(dict_bsl_2.items(), key=lambda x: x[1], reverse=False)

list_bsl_x_2 = []
for i in range(len(d_order_bsl_2)):
    list_bsl_x_2.append(d_order_bsl_2[i][0])
list_bsl_y_2 = []
for i in range(len(d_order_bsl_2)):
    list_bsl_y_2.append(d_order_bsl_2[i][1])
list_bsl_x_2 = list_bsl_x_2[-10:]
list_bsl_y_2 = list_bsl_y_2[-10:]


#####BOE/SRE
def excel_one_line_to_list5(a):
    df_li = df7.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column5 = list(df7.columns)
list_bsx_3 = excel_one_line_to_list5(column5.index('回复人'))
list_bsy_3 = excel_one_line_to_list5(column5.index('通过数量'))

dict_bsl_3 = {list_bsx_3[i]: list_bsy_3[i] for i in range(len(list_bsx_3))}
d_order_bsl_3 = sorted(dict_bsl_3.items(), key=lambda x: x[1], reverse=False)
list_bsl_x_3 = []
for i in range(len(d_order_bsl_3)):
    list_bsl_x_3.append(d_order_bsl_3[i][0])
list_bsl_y_3 = []
for i in range(len(d_order_bsl_3)):
    list_bsl_y_3.append(d_order_bsl_3[i][1])
list_bsl_x_3 = list_bsl_x_3[-10:]
list_bsl_y_3 = list_bsl_y_3[-10:]


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
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_2), item_width=10, item_height=40)
                         )
)

# bar1.render("故障质检驳回数量.html")

bar2 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_9)
        .add_yaxis("通过数量", list_10, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检通过情况'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_10), item_width=10, item_height=40)
                         )
)

# bar2.render("故障质检通过数量.html")

bar3 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_bhl_x)
        .add_yaxis("驳回率", list_bhl_y, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检驳回率'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_bhl_y), item_width=10, item_height=40)
                         )
)

# bar3.render("上月故障质检驳回率.html")


bar4 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_bsl_x)
        .add_yaxis("驳回数量", list_bsl_y, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月BOE质检驳回数量TOP10'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_bsl_y), item_width=10, item_height=40)
                         )
)

bar5 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_bsl_x_2)
        .add_yaxis("驳回率", list_bsl_y_2, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月BOE/SRE质检驳回率TOP10'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_bsl_y_2), item_width=10, item_height=40)
                         )
)


# bar5.render("上月BOE/SRE质检驳回率.html")


bar6 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=list_bsl_x_3)
        .add_yaxis("通过数量", list_bsl_y_3, label_opts=opts.LabelOpts(is_show=True))
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title='上月BOE质检通过数量TOP10'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 25}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_bsl_y_3), item_width=10, item_height=40)
                         )
)


# bar6.render("上月BOE/SRE质检通过数量.html")

def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)  # 不可拖动
    # page = Page(layout=Page.DraggablePageLayout)  # 可拖动
    page.add(
        #bar1,
        #bar2,
        #bar3,
        bar4,
        bar6,
        #bar5,
    )
    page.render("GOC.html")


if __name__ == "__main__":
    page_draggable_layout()

# with open(os.path.join(os.path.abspath("."), "GOC.html"), 'r+', encoding="utf8") as html:
#     html_bf = BeautifulSoup(html, "lxml")
#     divs = html_bf.find_all("div")
#     divs[0][
#         "style"] = "width:1000px;height:2000px;position:absolute;top:100px;left:0px;border-style:solid;border-color:#444444;border-width:0px;background: url(bj3.jpg)"  # 修改图表大小、位置、边框
#     divs[1][
#         "style"] = "width:640px;height:400px;position:absolute;top:0px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Pie大小、位置、边框
#     divs[2][
#         "style"] = "width:640px;height:400px;position:absolute;top:0px;left:640px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Bar大小、位置、边框
#     divs[3][
#         "style"] = "width:640px;height:400px;position:absolute;top:0px;left:1280px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
#     # body = html_bf.find("body")
#     divs[4][
#         "style"] = "width:640px;height:400px;position:absolute;top:500px;left:0px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
#     # body = html_bf.find("body")
#     divs[5][
#         "style"] = "width:640px;height:400px;position:absolute;top:500px;left:640px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
#     divs[6][
#         "style"] = "width:640px;height:400px;position:absolute;top:500px;left:1280px;border-style:solid;border-color:#444444;border-width:0px;"  # 修改Map大小、位置、边框
#     #body = html_bf.find("body")
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
