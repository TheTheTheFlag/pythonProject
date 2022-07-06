from typing import List

import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line

# 数据准备
list1 = [['丽水市', 1900], ['台州市', 7600], ['嘉兴市', 2600], ['宁波市', 6100], ['杭州市', 3300], ['温州市', 12200], ['湖州市', 800], ['绍兴市', 5400],
         ['舟山市', 900], ['衢州市', 1600], ['金华市', 7200]]
data = [
    {
        "time": "2019年",
        "data": [
            {"name": "杭州市", "value": [3469.0, 10.12]},
            {"name": "湖州市", "value": [2998.0, 8.75]},
            {"name": "衢州市", "value": [2770.0, 8.08]},
            {"name": "嘉兴市", "value": [2011.0, 5.87]},
            {"name": "宁波市", "value": [1926.0, 5.62]},
            {"name": "绍兴市", "value": [1691.0, 4.93]},
            {"name": "台州市", "value": [1660.0, 4.84]},
            {"name": "温州市", "value": [1519.0, 4.43]},
            {"name": "丽水市", "value": [1486.0, 4.34]},
            {"name": "金华市", "value": [1326.0, 3.87]},
            {"name": "舟山市", "value": [1245.0, 3.63]},
        ],
    },
    {
        "time": "2020年",
        "data": [
            {"name": "杭州市", "value": [3469.0, 10.12]},
            {"name": "湖州市", "value": [2998.0, 8.75]},
            {"name": "衢州市", "value": [2770.0, 8.08]},
            {"name": "嘉兴市", "value": [2011.0, 5.87]},
            {"name": "宁波市", "value": [1926.0, 5.62]},
            {"name": "绍兴市", "value": [1691.0, 4.93]},
            {"name": "台州市", "value": [1660.0, 4.84]},
            {"name": "温州市", "value": [1519.0, 4.43]},
            {"name": "丽水市", "value": [1486.0, 4.34]},
            {"name": "金华市", "value": [1326.0, 3.87]},
            {"name": "舟山市", "value": [1245.0, 3.63]},
        ],
    },
    {
        "time": "2021年",
        "data": [
            {"name": "杭州市", "value": [3469.0, 10.12]},
            {"name": "湖州市", "value": [2998.0, 8.75]},
            {"name": "衢州市", "value": [2770.0, 8.08]},
            {"name": "嘉兴市", "value": [2011.0, 5.87]},
            {"name": "宁波市", "value": [1926.0, 5.62]},
            {"name": "绍兴市", "value": [1691.0, 4.93]},
            {"name": "台州市", "value": [1660.0, 4.84]},
            {"name": "温州市", "value": [1519.0, 4.43]},
            {"name": "丽水市", "value": [1486.0, 4.34]},
            {"name": "金华市", "value": [1326.0, 3.87]},
            {"name": "舟山市", "value": [1245.0, 3.63]},
        ],
    },

]

time_list = [str(d) + "年" for d in range(2019, 2022)]
print(time_list)
total_num = [
    3.4,
    4.5,
    5.8,
    6.8,
    7.6,
    8.3,
    8.8,
    9.9,
    10.9,
    12.1,
    14,
    16.8,
    19.9,
    23.3,
    28,
    33.3,
    36.5,
    43.7,
    52.1,
    57.7,
    63.4,
    68.4,
    72.3,
    78,
    84.7,
    91.5,
]
maxNum = 5000
minNum = 30


def get_year_chart(year: str):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == year
    ][0]
    print(map_data)
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == year:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
        .add(

            series_name="",
            # data_pair=map_data,
            data_pair=list1,
            maptype="浙江",
            zoom=1,
            #center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(year) + "浙江话题活跃情况",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    line_chart = (
        Line()
        .add_xaxis(time_list)
        .add_yaxis("", total_num)
        .add_yaxis(
            "",
            data_mark,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="浙江话题活跃情况", pos_left="72%", pos_top="5%"
            )
        )
    )
    bar_x_data = [x[0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
        .add_xaxis(xaxis_data=bar_x_data)
        .add_yaxis(
            series_name="",
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    pie_data = [[x[0], x[1][0]] for x in map_data]
    pie = (
        Pie()
        .add(
            series_name="",
            data_pair=pie_data,
            radius=["15%", "35%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
        .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
        .add(
            line_chart,
            grid_opts=opts.GridOpts(
                pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            ),
        )
        .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
        .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == "__main__":
    timeline = Timeline(
        init_opts=opts.InitOpts(width="1600px", height="900px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_year_chart(year=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )

    timeline.render("浙江话题活跃情况.html")
