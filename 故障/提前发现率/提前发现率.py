import numpy as np
import pandas as pd
from pandas import isnull

df = pd.read_excel('D:/WJ/数据准备/标签清单.xlsx')
df_OC调度是否超时 = df.copy()
df_OC调度是否超时 = df_OC调度是否超时[(df_OC调度是否超时['是否连续性问题'] == '是') & (df_OC调度是否超时['响应时长'] > 5)]
df_OC调度是否超时['OC调度是否超时'] = '是'
print('OC调度超时清单：', df_OC调度是否超时)
print('OC调度超时数：', df_OC调度是否超时.OC调度是否超时.count())

a = df.是否系统发现[df.是否系统发现 == '主动发现'].count()
b = df.是否系统发现[df.是否系统发现 == '人工反馈'].count()

print('主动发现故障数:', a)
print('人工反馈故障数:', b)
print('故障主动发现率:', str(round(a / (a + b) * 100, 2)) + '%')

df1 = df.copy()
df2 = df.copy()

df1 = df1[pd.isnull(df1.人工反馈时间)]
df2 = df2[pd.notnull(df2.人工反馈时间)]
df1["提前发现多久"] = df1.故障新建时间 - df1.主动发现时间
df1["提前发现多久"] = df1.提前发现多久.astype('timedelta64[m]')
df2["提前发现多久"] = df2.人工反馈时间 - df2.主动发现时间
df2["提前发现多久"] = df2.提前发现多久.astype('timedelta64[m]')
df = pd.concat([df1, df2])
df.to_excel('d:/WJ/数据准备/提前发现率.xlsx', index=False)
c = df['提前发现多久'].sum()
c = df['提前发现多久'][df.是否系统发现 == '主动发现'].sum()
print('平均提前发现:', str(round(c / a, 2)) + '分钟')

df_3 = df.copy()
df_3['场景类别'].fillna("无", inplace=True)
df_3 = df_3[(df_3.场景类别.str.contains('资金类')) & (df_3.是否系统发现 == '主动发现')]
df_3 = df_3[(df_3['场景类别'].str.contains('资金类', na=False))]
print('主动发现资金类故障数：', df_3.场景类别.count())

df_4 = df.copy()
df_4['场景类别'].fillna("无", inplace=True)
df_4 = df_4[(df_4.场景类别.str.contains('资金类'))]
df_4 = df_4[(df_4['场景类别'].str.contains('资金类', na=False))]
print('资金类故障数：', df_4.场景类别.count())

df_5 = df.copy()
df_5['场景类别'].fillna("无", inplace=True)
df_5 = df_5[(df_5.场景类别.str.contains('白屏卡顿类')) & (df_5.是否系统发现 == '主动发现')]
df_5 = df_5[(df_5['场景类别'].str.contains('白屏卡顿类', na=False))]
print('主动发现白屏卡顿类故障数：', df_5.场景类别.count())

df_6 = df.copy()
df_6['场景类别'].fillna("无", inplace=True)
df_6 = df_6[(df_6.场景类别.str.contains('白屏卡顿类'))]
df_6 = df_6[(df_6['场景类别'].str.contains('白屏卡顿类', na=False))]
print('白屏卡顿类故障数：', df_6.场景类别.count())

df_7 = df.copy()
df_7['场景类别'].fillna("无", inplace=True)
df_7 = df_7[(df_7.场景类别.str.contains('舆情类')) & (df_7.是否系统发现 == '主动发现')]
df_7 = df_7[(df_7['场景类别'].str.contains('舆情类', na=False))]
print('主动发现舆情类故障数：', df_7.场景类别.count())

df_8 = df.copy()
df_8['场景类别'].fillna("无", inplace=True)
df_8 = df_8[(df_8.场景类别.str.contains('舆情类'))]
df_8 = df_8[(df_8['场景类别'].str.contains('舆情类', na=False))]
print('舆情类故障数：', df_8.场景类别.count())

df_9 = df.copy()
df_9['场景类别'].fillna("无", inplace=True)
df_9 = df_9[(df_9.场景类别.str.contains('业务跌零类')) & (df_9.是否系统发现 == '主动发现')]
df_9 = df_9[(df_9['场景类别'].str.contains('业务跌零类', na=False))]
print('主动发现业务跌零类故障数：', df_9.场景类别.count())

df_10 = df.copy()
df_10['场景类别'].fillna("无", inplace=True)
df_10 = df_10[(df_10.场景类别.str.contains('业务跌零类'))]
df_10 = df_10[(df_10['场景类别'].str.contains('业务跌零类', na=False))]
print('业务跌零类故障数：', df_10.场景类别.count())

df_11 = df.copy()
df_11['场景类别'].fillna("无", inplace=True)
df_11 = df_11[(df_11.场景类别.str.contains('F4|F3|F2|F1')) & (df_11.是否系统发现 == '主动发现')]
df_11 = df_11[(df_11['场景类别'].str.contains('F4|F3|F2|F1', na=False))]
print('主动发现F4及以上故障数：', df_11.场景类别.count())

df_12 = df.copy()
df_12['场景类别'].fillna("无", inplace=True)
df_12 = df_12[(df_12.场景类别.str.contains('F4|F3|F2|F1'))]
df_12 = df_12[(df_12['场景类别'].str.contains('F4|F3|F2|F1', na=False))]
print('F4及以上故障数：', df_12.场景类别.count())