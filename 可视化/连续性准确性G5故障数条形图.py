from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType


list2 = [
    {"value": 79, "percent": 79 / (79 + 116)},
    {"value": 34, "percent": 34 / (34 + 74)},
    {"value": 84, "percent": 84 / (84 + 127)},
    {"value": 84, "percent": 84 / (84 + 183)},
    {"value": 73, "percent": 73 / (73 + 132)},
    {"value": 26, "percent": 26 / (26 + 133)},
]

list3 = [
    {"value": 116, "percent": 116 / (79 + 116)},
    {"value": 74, "percent": 74 / (34 + 74)},
    {"value": 127, "percent": 127 / (33 + 127)},
    {"value": 183, "percent": 183 / (84 + 183)},
    {"value": 132, "percent": 132 / (73 + 132)},
    {"value": 133, "percent": 133 / (26 + 133)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(['1月', '2月', '3月', '4月', '5月', '6月'])
    # .add_yaxis("连续性", list2, stack="stack1", category_gap="50%")
    # .add_yaxis("准确性", list3, stack="stack1", category_gap="50%")
    .add_yaxis("连续性", list2, category_gap="50%")
    .add_yaxis("准确性", list3, category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="top",
            # formatter=JsCode(
            #     "function(x){return x.value,Number(x.data.percent * 100).toFixed() + '%';}"
            # ),
            formatter='{c}'
        )
    )
    .render("stack_bar_percent.html")
)
