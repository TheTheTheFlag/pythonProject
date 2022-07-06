import pandas as pd
import os

from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Map3D
from pyecharts.charts import Map, Geo, Timeline
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType, ChartType

df = pd.read_excel('d:/WJ/用户画像输入/活跃人员.xlsx')
df[['人员', '归属地市']] = df[['PHONE_NUMBER', 'REGION']].applymap(lambda x: str(x).strip())
df1 = df[['人员', '归属地市']]
df_count = df1.groupby('归属地市')['人员'].count()
x1 = df_count.index
y1 = df_count.values

# 基础数据
city = x1
values2 = y1
# list1 = [[city[i],values2[i]] for i in range(len(city))]
list1 = [[city[i] + "市", int(values2[i])] for i in range(len(city))]

c = (
    Map3D(
        # 初始化配置项
        init_opts=opts.InitOpts(width="900px", height="500px", chart_id='活跃人数情况', theme=ThemeType.DARK)
    )
        .add(
        series_name="",
        data_pair=list1,
        maptype="浙江",
        # type_=ChartType.LINES3D,
    )
        .add_schema(
        maptype="浙江",
        map3d_label=opts.Map3DLabelOpts(is_show=True),

    )
.set_global_opts(
        title_opts=opts.TitleOpts(
            title="浙江各地市活跃人数",
            subtitle="单位:人",
            pos_left="left",
            pos_top="top",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=25, color="rgba(125,125,125, 0.9)"
            )),
        visualmap_opts=opts.VisualMapOpts(
            is_calculable=True,
            dimension=0,
            pos_left="10",
            pos_top="center",
            range_text=["High", "Low"],max_=100, item_height=100, item_width=10, type_='color', range_color=["#B6E4FD", "#CCG403"]),

        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            trigger="item"
        ),

    )

        .render("map3d_with_scatter3d.html")
)
# 打开html
# os.system("d:/WJ/用户画像输出/浙江各地市活跃人数.html")