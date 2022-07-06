# 柱状堆叠图
import pyecharts.options as opts
import os
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

df = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xlsx')
df[['地市', '收集中', '攻克中', '已攻克', '已关闭']] = df[['地市', '收集中', '攻克中', '已攻克', '已关闭']].applymap(
    lambda x: str(x).strip())
df1 = df[['地市', '收集中', '攻克中', '已攻克', '已关闭']]
x1 = df1.地市.values
y1 = df1.收集中.values
y2 = df1.攻克中.values
y3 = df1.已攻克.values
y4 = df1.已关闭.values

print(x1)
print(y1)
print(y2)
print(y3)
print(y4)

list1 = x1.tolist()
list2 = y1.tolist()
list3 = y2.tolist()
list4 = y3.tolist()
list5 = y4.tolist()

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(list1)
    .add_yaxis('收集中话题数', list2, stack='stack1')
    .add_yaxis('攻克中话题数', list3, stack='stack1')
    .add_yaxis('已攻克话题数', list4, stack='stack1')
    .add_yaxis('已关闭话题数', list5, stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='话题情况'),
                     xaxis_opts=opts.AxisOpts(name='地市'),
                     yaxis_opts=opts.AxisOpts(name='话题'),
                     visualmap_opts=opts.VisualMapOpts(max_=50),
                     toolbox_opts=opts.ToolboxOpts(),
                     datazoom_opts=opts.DataZoomOpts())
)

bar.render('d:/WJ/用户画像输出/话题攻克情况堆叠图.html')
os.system("d:/WJ/用户画像输出/话题攻克情况堆叠图.html")
