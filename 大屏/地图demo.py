from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker
import pandas as pd
import os
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.faker import Faker


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
print(dict1)

tl = Timeline()
for date, data in dict1.items():
#for i in range(2015, 2020):
    map0 = (
        Map()
        .add("活跃人数", data, "浙江")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}日活跃人数".format(date)),
            visualmap_opts=opts.VisualMapOpts(max_=50),
        )
    )
    tl.add(map0, "{}日".format(date))
tl.render("timeline_map.html")



df = pd.read_excel('d:/WJ/用户画像输入/话题列表.xlsx')
df[['状态', '创建人', '归属地市']] = df[['状态', '创建人', '归属地市']].applymap(lambda x: str(x).strip())

# 所有数据
df_All = df
df_count_All = df_All.groupby('归属地市')['序号'].count()
x_All = df_count_All.index
y_All = df_count_All.values
df_1 = df[df.状态 == '1']
df_1_count = df_1.groupby('归属地市')['序号'].count()
df_1_x = df_1_count.index
df_1_y = df_1_count.values
df_2 = df[df.状态 == '2']
df_2_count = df_2.groupby('归属地市')['序号'].count()
df_2_x = df_2_count.index
df_2_y = df_2_count.values
df_3 = df[df.状态 == '3']
df_3_count = df_3.groupby('归属地市')['序号'].count()
df_3_x = df_3_count.index
df_3_y = df_3_count.values
df_4 = df[df.状态 == '4']
df_4_count = df_4.groupby('归属地市')['序号'].count()
df_4_x = df_4_count.index
df_4_y = df_4_count.values

# Y轴坐标数据处理，和全量数据的Y轴数据保持一致，缺失地市补成0
list1 = [[x_All[i], int(y_All[i])] for i in range(len(x_All))]
list2 = [[df_1_x[i], int(df_1_y[i])] for i in range(len(df_1_x))]
list3 = [[df_2_x[i], int(df_2_y[i])] for i in range(len(df_2_x))]
list4 = [[df_3_x[i], int(df_3_y[i])] for i in range(len(df_3_x))]
list5 = [[df_4_x[i], int(df_4_y[i])] for i in range(len(df_4_x))]

dict_a = dict(list1)
dict_b = dict(list2)
dict_c = dict(list3)
dict_d = dict(list4)
dict_e = dict(list5)

ls_sjz = [[x, dict_b[x]] if x in dict_b else [x, 0] for x in dict_a]
ls_gkz = [[x, dict_c[x]] if x in dict_c else [x, 0] for x in dict_a]
ls_ygk = [[x, dict_d[x]] if x in dict_d else [x, 0] for x in dict_a]
ls_ygb = [[x, dict_e[x]] if x in dict_e else [x, 0] for x in dict_a]

print("收集中话题：%s" % ls_sjz)
print("攻克中话题：%s" % ls_gkz)
print("已攻克话题：%s" % ls_ygk)
print("已关闭话题：%s" % ls_ygb)

# X轴坐标数据处理，将X轴输出为列表格式
num_list = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        num_list.append(k[i])
city = list()
for b, k in enumerate(list1):
    for i in range(1, len(k)):
        city.append(k[i - 1])

bar = (
    Bar(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.WHITE))
        .add_xaxis(city)
        .add_yaxis('收集中', ls_sjz, stack='stack1', color='#5aa5b4')
        .add_yaxis('攻克中', ls_gkz, stack='stack1', color='#aab988')
        .add_yaxis('已攻克', ls_ygk, stack='stack1', color='#e5a461')
        .add_yaxis('已关闭', ls_ygb, stack='stack1', color='#db605e')
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='话题攻克情况'),
                         # xaxis_opts=opts.AxisOpts(name='地市'),
                         # yaxis_opts=opts.AxisOpts(name='话题'),
                         # visualmap_opts=opts.VisualMapOpts(max_=150),
                         toolbox_opts=opts.ToolboxOpts(),
                         #  datazoom_opts=opts.DataZoomOpts(),
                         xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45})
                         )
)
