from numpy.distutils.fcompiler import none
from pyecharts.charts import Funnel
import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType

df_004_ = pd.read_excel('d:/WJ/用户画像输入/地市话题攻克情况.xlsx')
df_004_[['收集中话题数', '攻克中话题数', '已攻克话题数', '已关闭话题数']] = df_004_[
    ['SJZ_NUM', 'GKZ_NUM', 'YGK_NUM', 'YGB_NUM']].applymap(lambda x: str(x).strip())
df_004_1 = df_004_['收集中话题数'].values
list_004_1 = [int(df_004_1[i]) for i in range(len(df_004_1))]
df_004_2 = df_004_['攻克中话题数'].values
list_004_2 = [int(df_004_2[i]) for i in range(len(df_004_2))]
df_004_3 = df_004_['已攻克话题数'].values
list_004_3 = [int(df_004_3[i]) for i in range(len(df_004_3))]
df_004_4 = df_004_['已关闭话题数'].values
list_004_4 = [int(df_004_4[i]) for i in range(len(df_004_4))]
list_004_5 = list_004_3 + list_004_4
def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total_004_1 = sumOfList(list_004_1, len(list_004_1))
total_004_2 = sumOfList(list_004_2, len(list_004_2))
total_004_3 = sumOfList(list_004_3, len(list_004_3))
total_004_4 = sumOfList(list_004_4, len(list_004_4))

x_data_004_ = ["收集中话题数", "攻克中话题数", "已攻克话题数", "已关闭话题数"]
y_data_004_ = [total_004_1, total_004_2, total_004_3, total_004_4]

data_004_ = [[x_data_004_[i], y_data_004_[i]] for i in range(len(x_data_004_))]

(
    Funnel(init_opts=opts.InitOpts(width="600px", height="400px", theme=ThemeType.DARK))
        .add(
        series_name="",
        data_pair=data_004_,
        sort_=none,
        gap=0.5,
        # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="地市话题攻克情况", subtitle=""))
        .render("地市话题攻克情况.html")
)
