import pandas as pd
import os

from pyecharts.charts import Map, Geo
from pyecharts import options as opts

df = pd.read_excel('d:/WJ/用户画像输入/活跃人员.xlsx')
df[['人员', '归属地市']] = df[['PHONE_NUMBER', 'REGION']].applymap(lambda x: str(x).strip())
df1 = df[['人员', '归属地市']]
df_count = df1.groupby('归属地市')['人员'].count()
print(df_count)
x1 = df_count.index
y1 = df_count.values
print(x1)
print(y1)

# 基础数据
city = x1
values2 = y1
# list1 = [[city[i],values2[i]] for i in range(len(city))]
list1 = [[city[i] + "市", int(values2[i])] for i in range(len(city))]
print(list1)
c = (
    Map(
        # 初始化配置项
        init_opts=opts.InitOpts(width="900px", height="500px", chart_id='活跃人数')
    )
        .add("活跃人数", list1, "浙江")
        # 标签配置项
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", rotate=30))
        # 全局配置项
        .set_global_opts(
        toolbox_opts=opts.ToolboxOpts(),
        #datazoom_opts=opts.DataZoomOpts(),
        legend_opts=opts.LegendOpts(),
        title_opts=opts.TitleOpts(title="浙江各地市活跃人数"),
        visualmap_opts=opts.VisualMapOpts(max_=100, item_height=100, item_width=10, type_='color',
                                          range_color=["#B6E4FD", "#CCG403"])
    )
        .render(path="d:/WJ/用户画像输出/浙江各地市活跃人数.html")
)
# 打开html
# os.system("d:/WJ/用户画像输出/浙江各地市活跃人数.html")
