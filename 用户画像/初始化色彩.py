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
        # 系列名称，用于 tooltip 的显示，legend 的图例筛选
        series_name="",
        data_pair=list1,
        # 叠加图的类型（目前只支持 Bar3D，Line3D，Lines3D，Scatter3D）
        type_=None,
        maptype="浙江",
        # 是否选中图例
        is_selected=True,
        # 是否显示标记图形
        is_map_symbol_show=True,
        # 是否开启动画
        is_animation=True,
        # animation_duration_update=100,
        animation_easing_update="cubicOut",
        # 仅在 Scatter3D，Bar3D，Map3D 起作用
        # 标签配置项
        label_opts=opts.LabelOpts(is_show=True, position="inside", rotate=30),
        # 图元样式配置项
        itemstyle_opts=None,
    )
        .add_schema(
        maptype="浙江",
        map3d_label=opts.Map3DLabelOpts(is_show=True, distance=None, formatter=None, text_style=None),
        # 高亮标签配置项
        emphasis_label_opts=opts.Map3DLabelOpts(is_show=True),  # 显示标签
        # 图元样式配置项
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",
            opacity=1,
            border_width=0.8,
            border_color="rgb(62,215,213)",
        ),
        # 高亮图元样式配置项
        emphasis_itemstyle_opts=None,
        # 光照相关的设置。在 shading 为 'color' 的时候无效
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.2,
            is_main_shadow=False,
            main_alpha=55,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )

        .render("map3d_with_scatter3d.html")
)
# 打开html
# os.system("d:/WJ/用户画像输出/浙江各地市活跃人数.html")