# 柱状堆叠图
import pyecharts.options as opts
import os
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

df = pd.read_excel('d:/WJ/用户画像输入/全量活跃人员.xlsx')
df[['地市', '活跃人数', '全量活跃人数', '全量人数']] = df[['REGION', 'ACT_COUNT', 'ACT_ALL_COUNT', 'ALL_COUNT']].applymap(
    lambda x: str(x).strip())
df1 = df[['地市', '活跃人数', '全量活跃人数', '全量人数']]
x1 = df1.地市.values
y1 = df1.活跃人数.values
y2 = df1.全量活跃人数.values
y3 = df1.全量人数.values
print(x1)
print(y1)
print(y2)
print(y3)

# list1 = [[x1[i]] for i in range(len(x1))]
# list2 = [[y1[i]] for i in range(len(y1))]
# list3 = [[y2[i]] for i in range(len(y3))]
# list4 = [[y3[i]] for i in range(len(y3))]
list1 = x1.tolist()
list2 = y1.tolist()
list3 = y2.tolist()
list4 = y3.tolist()

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(list1)
    .add_yaxis('全量人数', list4, stack='stack1')
    .add_yaxis('全量活跃人数', list3, stack='stack1')
    .add_yaxis('7天活跃人数', list2, stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True,position="inside",rotate=30))
    .set_global_opts(title_opts=opts.TitleOpts(title='人员情况'),
                     xaxis_opts=opts.AxisOpts(name='地市'),
                     yaxis_opts=opts.AxisOpts(name='话题'),
                     visualmap_opts=opts.VisualMapOpts(max_=10000),
                     toolbox_opts=opts.ToolboxOpts(),
                     datazoom_opts=opts.DataZoomOpts())
)

bar.render('d:/WJ/用户画像输出/人员情况堆叠图.html')
os.system("d:/WJ/用户画像输出/人员情况堆叠图.html")
