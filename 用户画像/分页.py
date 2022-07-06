from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab, Map
from pyecharts.faker import Faker

list1 = [['丽水市', 1900], ['台州市', 7600], ['嘉兴市', 2600], ['宁波市', 6100], ['杭州市', 3300], ['温州市', 12200], ['湖州市', 800], ['绍兴市', 5400],
         ['舟山市', 900], ['衢州市', 1600], ['金华市', 7200]]
list2 = [['丽水市', 190], ['台州市', 760], ['嘉兴市', 260], ['宁波市', 610], ['杭州市', 330], ['温州市', 1220], ['湖州市', 80], ['绍兴市', 540],
         ['舟山市', 90], ['衢州市', 160], ['金华市', 720]]
list3= [['丽水市', 19], ['台州市', 76], ['嘉兴市', 26], ['宁波市', 61], ['杭州市', 33], ['温州市', 122], ['湖州市', 8], ['绍兴市', 54],
         ['舟山市', 9], ['衢州市', 16], ['金华市', 72]]


def map_datazoom_all() -> Map:
    c = (
        Map()
            .add("总人数", list1, "浙江")
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=5000),
        )
    )
    return c


def map_datazoom() -> Map:
    c = (
        Map()
            .add("总活跃人数", list2, "浙江")
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=500),
        )
    )
    return c


def map_datazoom_7() -> Map:
    c = (
        Map()
            .add("7天活跃人数", list3, "浙江")
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c


def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c


tab = Tab()
tab.add(map_datazoom_all(), "全量人员")
tab.add(map_datazoom(), "全量活跃人员")
tab.add(map_datazoom_7(), "7天活跃人员")
tab.render("tab_base.html")
