# 按组 驳回量 TOP （带驳回率）
# 按组 通过量 TOP （带驳回率）
# 个人 驳回量 TOP （区分组别）
# 个人 通过量 TOP （区分组别）
import body as body
import pandas as pd
import os
import datetime
import pyecharts.options as opts
from bs4 import BeautifulSoup
from pyecharts.charts import Timeline, Bar, Line, Funnel, Pie, Page

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

# 获取数据列表
##所有数据的量
df0 = pd.read_excel('D:/WJ/数据准备/12月故障质检清单.xlsx')
df = df0.copy()
df1 = df0.copy()
df0 = df0[['处理人', '处理大别', '数量']] = df0[['关联处理人', '关联处理大组', '质检情况']]
df0['数量'] = 1
df0 = df0[['处理人', '处理大别', '数量']]
df_boe = df0[df0.处理大别 == 'BOE']
df_sre = df0[df0.处理大别 == 'SRE']
df_boesre = df_boe.append(df_sre)  # 限定范围在BOE和SRE
df0 = df_boesre.groupby("处理人", as_index=False).sum({'数量': 'count'})
##驳回的量
df[['处理人', '驳回数量']] = df[['关联处理人', '质检情况']]
df = df[df.驳回数量 == '驳回']
df['驳回数量'] = 1
df = df[['处理人', '驳回数量']]
df = df.groupby("处理人", as_index=False).sum({'驳回数量': 'count'})

##通过的量
df1[['处理人', '通过数量']] = df1[['关联处理人', '质检情况']]
df1 = df1[df1.通过数量 == '通过']
df1['通过数量'] = 1
df1 = df1[['处理人', '通过数量']]
df1 = df1.groupby("处理人", as_index=False).sum({'通过数量': 'count'})

##关联全量&通过&驳回的量
df2 = pd.merge(df0, df, on='处理人', how='left')
df2 = pd.merge(df2, df1, on='处理人', how='left')
df2 = df2.fillna(value=0)
df2['驳回率%'] = round(df2['驳回数量'] / df2['数量'], 2) * 100
df_ord_bhsl = df2.sort_values(by="驳回数量", ascending=False)
df_ord_tgsl = df2.sort_values(by="通过数量", ascending=False)
print("个人质检驳回数量TOP10:")
print(df_ord_bhsl[['处理人', '驳回数量', '驳回率%']].head(10))
print("个人质检通过数量TOP10:")
print(df_ord_tgsl[['处理人', '通过数量', '驳回率%']].head(10))

df_yxgr = df2.sort_values(by="驳回率%", ascending=True)
df_yxgr = df_yxgr[(df_yxgr.通过数量 >= 5) & (df_yxgr['驳回率%'] <= 20)]
print("优秀个人:")
print(df_yxgr)

with pd.ExcelWriter(r'D:\WJ\故障数据输出\故障质检情况-个人-12-01至12-15.xlsx') as writer:
    df_ord_bhsl[['处理人', '驳回数量', '驳回率%']].to_excel(writer, sheet_name='处理人', index=False)
    df_ord_tgsl[['处理人', '通过数量', '驳回率%']].to_excel(writer, sheet_name='处理人', startcol=6, index=False)
    df_yxgr.to_excel(writer, sheet_name='处理人', startcol=11, startrow=0, index=False)
print('文件导出成功')
