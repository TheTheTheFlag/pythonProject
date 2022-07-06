import pandas as pd
import pyecharts.options as opts

from pyecharts.charts import Line
from pyecharts.globals import ThemeType


# 获取数据列表
df_006_ = pd.read_excel('d:/WJ/用户画像输入/留存率曲线.xlsx')
df_006_[['日期', '人数', '次日留存', '次日留存率', '日3留存', '日3留存率', '日7留存', '日7留存率', '日30留存率', '日60留存率', '日90留存率']] = df_006_[
    ['日期', '人数', '次日留存', '次日留存率', '日3留存', '日3留存率', '日7留存', '日7留存率', '日30留存率', '日60留存率', '日90留存率']].applymap(lambda x: str(x).strip())
df = df_006_[['日期', '人数', '次日留存', '次日留存率', '日3留存', '日3留存率', '日7留存', '日7留存率', '日30留存率', '日60留存率', '日90留存率']]

date_006 = df.日期
values_006_1 = df.次日留存率
values_006_2 = df.日3留存率
values_006_3 = df.日7留存率
values_006_4 = df.日30留存率
values_006_5 = df.日60留存率
values_006_6 = df.日90留存率

# 1.创建时间线对象
list_006_date_ = [date_006[i] for i in range(len(date_006))]
list_values_006_1 = [values_006_1[i] for i in range(len(values_006_1))]
list_values_006_2 = [values_006_2[i] for i in range(len(values_006_2))]
list_values_006_3 = [values_006_3[i] for i in range(len(values_006_3))]
list_values_006_4 = [values_006_4[i] for i in range(len(values_006_4))]
list_values_006_5 = [values_006_5[i] for i in range(len(values_006_5))]
list_values_006_6 = [values_006_6[i] for i in range(len(values_006_6))]

c = (
    Line(init_opts=opts.InitOpts(width="1800px", height="1000px"))
    .add_xaxis(list_006_date_)
    .add_yaxis("次日留存率", list_values_006_1, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .add_yaxis("3日留存率", list_values_006_2, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .add_yaxis("7日留存率", list_values_006_3, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .add_yaxis("30日留存率", list_values_006_4, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .add_yaxis("60日留存率", list_values_006_5, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .add_yaxis("90日留存率", list_values_006_6, label_opts=opts.LabelOpts(is_show=None), is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="留存率曲线"))
    .render("留存率曲线.html")
)
