from pyecharts.charts import Funnel
import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType

df_000 = pd.read_excel('d:/WJ/用户画像输入/近7天KOL活跃人数.xlsx')
df_000[['全量人数', '全量活跃人数', '月活跃人数', '周活跃人数']] = df_000[
    ['全量人数', '全量活跃人数', '月活跃人数', '周活跃人数']].applymap(lambda x: str(x).strip())
df_0001 = df_000['全量人数'].values
list_000_1 = [int(df_0001[i]) for i in range(len(df_0001))]
df_0002 = df_000['全量活跃人数'].values
list_000_2 = [int(df_0002[i]) for i in range(len(df_0002))]
df_0003 = df_000['月活跃人数'].values
list_000_3 = [int(df_0003[i]) for i in range(len(df_0003))]
df_0004 = df_000['周活跃人数'].values
list_000_4 = [int(df_0004[i]) for i in range(len(df_0004))]


def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total_000_1 = sumOfList(list_000_1, len(list_000_1))
total_000_2 = sumOfList(list_000_2, len(list_000_2))
total_000_3 = sumOfList(list_000_3, len(list_000_3))
total_000_4 = sumOfList(list_000_4, len(list_000_4))

x_data_000 = ["全量人数", "全量活跃人数", "月活跃人数", "周活跃人数"]
y_data_000 = [total_000_1, total_000_2, total_000_3, total_000_4]
# x_data = ["全量活跃人数", "月活跃人数", "周活跃人数"]
# y_data = [total_000_2, total_000_3, total_000_4]

data_000 = [[x_data_000[i], y_data_000[i]] for i in range(len(x_data_000))]

# (
#     Funnel(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
#         .add(
#         series_name="",
#         data_pair=data_000,
#         gap=0.5,
#         # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
#         label_opts=opts.LabelOpts(is_show=True, position="inside"),
#         itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
#     )
#         .set_global_opts(title_opts=opts.TitleOpts(title="KOL转化情况", subtitle=""))
#         .render("KOL转化情况.html")
# )

funnel1 = (
    Funnel(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        series_name="",
        data_pair=data_000,
        gap=0.5,
        # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="KOL转化情况", subtitle=""))
        .render("KOL转化情况.html")
)
