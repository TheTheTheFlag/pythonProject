from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker

list1 = [['丽水市', 19], ['台州市', 76], ['嘉兴市', 26], ['宁波市', 61], ['杭州市', 33], ['温州市', 122], ['湖州市', 8], ['绍兴市', 54], ['舟山市', 9], ['衢州市', 16], ['金华市', 72]]

tl = Timeline()
for i in range(2015, 2020):
    map0 = (
        Map()
        .add("活跃人数", list1, "浙江")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    tl.add(map0, "{}年".format(i))
tl.render("timeline_map.html")
