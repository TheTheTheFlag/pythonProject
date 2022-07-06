# 按组 驳回量 TOP （带驳回率）
# 按组 通过量 TOP （带驳回率）
# 个人 驳回量 TOP （区分组别）
# 个人 通过量 TOP （区分组别）
import body as body
import pandas as pd
import os
import datetime
import pyecharts.options as opts
from bs4 import BeautifulSoup
from pyecharts.charts import Timeline, Bar, Line, Funnel, Pie, Page

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.commons.utils import JsCode
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

##关联全量&通过&驳回的量
df2 = pd.merge(df0, df, on='处理组别', how='left')
df2 = pd.merge(df2, df1, on='处理组别', how='left')
df2 = df2.fillna(value=0)
df2['驳回率'] = round(df2['驳回数量'] / df2['数量'], 2) * 100
df_ord_bhsl = df2.sort_values(by="驳回数量", ascending=False)
df_ord_tgsl = df2.sort_values(by="通过数量", ascending=False)
print(df_ord_bhsl)
#df_ord_bhsl.to_excel('d:/WJ/机器学习输入/组别.xlsx')

##把驳回数量和驳回率转化为列表
def excel_one_line_to_list1(a):
    df_li = df_ord_bhsl.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


def excel_one_line_to_list2(a):
    df_li = df_ord_tgsl.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[a])
    return result


column1 = list(df_ord_bhsl.columns)
column2 = list(df_ord_tgsl.columns)

list_clzb = excel_one_line_to_list1(column1.index('处理组别'))
#list_clzb = list_clzb[-10:]
list_bhsl = excel_one_line_to_list1(column1.index('驳回数量'))
#list_bhsl = list_bhsl[-10:]
list_clzb2 = excel_one_line_to_list2(column2.index('处理组别'))
#list_clzb2 = list_clzb2[-10:]
list_tgsl = excel_one_line_to_list2(column2.index('通过数量'))
#list_tgsl = list_tgsl[-10:]
list_bhl = excel_one_line_to_list1(column1.index('驳回率'))
#list_bhl = list_bhl[-10:]
list_bhl2 = excel_one_line_to_list2(column2.index('驳回率'))
#list_bhl2 = list_bhl2[-10:]

list_x = []
for i in range(10):
    list_x.append('驳回数：' + str(list_bhsl[i]) + ' 驳回率：' + str(list_bhl[i]) + '%')
list_y = []
for i in range(10):
    list_y.append(str(list_bhl2[i]) + '%')


def str_new_line(data):
    for i in range(len(data)):
        s_new_line = list_x[i]
    return s_new_line


bar1 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.DARK))
        .add_xaxis(xaxis_data=list_clzb)
        # .extend_axis(
        # yaxis=opts.AxisOpts(
        #     name="驳回率",
        #     type_="value",s
        #     min_=0,
        #     max_=max(list_bhl),
        #     interval=5,
        #     axislabel_opts=opts.LabelOpts(is_show=True)))
        .add_yaxis("驳回数量", list_bhsl, label_opts=opts.LabelOpts(is_show=True, formatter=str_new_line),
                   markpoint_opts=opts.MarkPointOpts(
                       data=[opts.MarkPointItem(coord=[list_clzb[9], list_bhsl[9]], value=list_x[9]),
                             opts.MarkPointItem(coord=[list_clzb[8], list_bhsl[8]], value=list_x[8]),
                             opts.MarkPointItem(coord=[list_clzb[7], list_bhsl[7]], value=list_x[7]),
                             opts.MarkPointItem(coord=[list_clzb[6], list_bhsl[6]], value=list_x[6]),
                             opts.MarkPointItem(coord=[list_clzb[5], list_bhsl[5]], value=list_x[5]),
                             opts.MarkPointItem(coord=[list_clzb[4], list_bhsl[4]], value=list_x[4]),
                             opts.MarkPointItem(coord=[list_clzb[3], list_bhsl[3]], value=list_x[3]),
                             opts.MarkPointItem(coord=[list_clzb[2], list_bhsl[2]], value=list_x[2]),
                             opts.MarkPointItem(coord=[list_clzb[1], list_bhsl[1]], value=list_x[1]),
                             opts.MarkPointItem(coord=[list_clzb[0], list_bhsl[0]], value=list_x[0])],
                       symbol_size=[100, 50]
                   ))
        # .add_yaxis("通过数量", list_bhl, label_opts=opts.LabelOpts(is_show=True))
        # .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        # .set_series_opts(
        # tooltip_opts=opts.TooltipOpts(
        #     trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        #                              )
        # )
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检驳回情况'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 35}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_bhsl), item_width=10, item_height=40)
                         )
)

bar2 = (
    Bar(init_opts=opts.InitOpts(width="900px", height="1000px", theme=ThemeType.DARK))
        .add_xaxis(xaxis_data=list_clzb2)
        # .extend_axis(
        # yaxis=opts.AxisOpts(
        #     name="驳回率",
        #     type_="value",
        #     min_=0,
        #     max_=max(list_bhl),
        #     interval=5,
        #     axislabel_opts=opts.LabelOpts(formatter="{value} %")))
        .add_yaxis("通过数量", list_tgsl, label_opts=opts.LabelOpts(is_show=True), markpoint_opts=opts.MarkPointOpts(
        data=[opts.MarkPointItem(coord=[list_clzb2[9], list_tgsl[9]], value=list_y[9]),
              opts.MarkPointItem(coord=[list_clzb2[8], list_tgsl[8]], value=list_y[8]),
              opts.MarkPointItem(coord=[list_clzb2[7], list_tgsl[7]], value=list_y[7]),
              opts.MarkPointItem(coord=[list_clzb2[6], list_tgsl[6]], value=list_y[6]),
              opts.MarkPointItem(coord=[list_clzb2[5], list_tgsl[5]], value=list_y[5]),
              opts.MarkPointItem(coord=[list_clzb2[4], list_tgsl[4]], value=list_y[4]),
              opts.MarkPointItem(coord=[list_clzb2[3], list_tgsl[3]], value=list_y[3]),
              opts.MarkPointItem(coord=[list_clzb2[2], list_tgsl[2]], value=list_y[2]),
              opts.MarkPointItem(coord=[list_clzb2[1], list_tgsl[1]], value=list_y[1]),
              opts.MarkPointItem(coord=[list_clzb2[0], list_tgsl[0]], value=list_y[0])], symbol_size=[100, 50],
        symbol='pin'
    ))
        # .add_yaxis("通过数量", list_bhl, label_opts=opts.LabelOpts(is_show=True))
        # .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        # .set_series_opts(
        # tooltip_opts=opts.TooltipOpts(
        #     trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        #                              )
        # )
        .set_global_opts(title_opts=opts.TitleOpts(title='上月故障质检通过情况'),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 35}),
                         visualmap_opts=opts.VisualMapOpts(max_=max(list_tgsl), item_width=10, item_height=40)
                         )
)

line1 = (
    Line()
        .add_xaxis(xaxis_data=list_clzb)
        .add_yaxis(
        series_name="驳回率",
        y_axis=list_bhl,
        yaxis_index=1,
        label_opts=opts.LabelOpts(is_show=True),
    )
    # .reversal_axis()

)


# bar1.overlap(line1).render("上月故障质检驳回情况.html")


def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)  # 不可拖动
    # page = Page(layout=Page.DraggablePageLayout)  # 可拖动
    page.add(
        bar1,
        bar2,
    )
    page.render("NEWTOP.html")


if __name__ == "__main__":
    page_draggable_layout()
