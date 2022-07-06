import pandas as pd

pd.set_option('display.max_columns', None)
path = 'D:/WJ/数据准备/标签清单.xlsx'  # input("请输入文件路径（格式：D:/WJ/数据准备/标签清单.xlsx）      :")
start_date = '20211201'  # input("请输入开始日期（格式YYYYMMDD）      :")
end_date = '20211217'  # input("请输入结束日期（格式YYYYMMDD）      :")
df = pd.read_excel(path)
df['人工反馈时间'] = pd.to_datetime(df['人工反馈时间'], format='%Y%m%d %H:%M:%S', errors='coerce')

df = df[(df['故障单号'].str[2:10] >= str(start_date)) & (df['故障单号'].str[2:10] <= str(end_date))]


df_x = df[(df['是否连续性问题'] == '是')]
x3 = df_x[pd.notnull(df_x.SLA超时原因)].故障单号.count()
print('一五十超时故障数:', x3)

df_主动发现 = df.copy()


df_主动发现 = df_主动发现[df_主动发现['是否系统发现'] == '主动发现']
a = df_主动发现.是否系统发现.count()
b = df.是否系统发现.count()
print('主动发现故障数:', a)
print('人工反馈故障数:', b - a)
# if df_主动发现.故障单号.count() > 0:
#     print('主动发现故障清单:')
# else:
#     print('无主动发现故障')
# print(df_主动发现[['故障单号', '故障等级', '主动发现时间', '人工反馈时间']])
print('故障主动发现率:', str(round(a / b * 100, 2)) + '%')

# 提前发现多久
df1 = df.copy()
df2 = df.copy()

df1 = df1[pd.isnull(df1.人工反馈时间)]  # 人工反馈时间为空
df2 = df2[pd.notnull(df2.人工反馈时间)]  # 人工反馈时间不为空
df1["提前发现多久"] = df1.人工反馈时间 - df1.主动发现时间
df1["提前发现多久"] = df1.提前发现多久.astype('timedelta64[m]')
df2["提前发现多久"] = df2.人工反馈时间 - df2.主动发现时间
df2["提前发现多久"] = df2.提前发现多久.astype('timedelta64[m]')
df = pd.concat([df1, df2])
df.to_excel('d:/WJ/数据准备/提前发现率.xlsx', index=False)
c = df['提前发现多久'].sum()
c = df['提前发现多久'][df.是否系统发现 == '主动发现'].sum()
print('平均提前发现:', str(round(c / a, 2)) + '分钟')


# 类型


def excel_one_line_to_list(df_in, x):
    if df_in.reset_index(drop=True).equals(df_主动发现.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
        df_return = df_return[(df_return['场景类别'].str.contains(x))]
        df_return = df_return[(df_return['场景类别'].str.contains(x, na=False))]
        print('主动发现' + x + '故障数：', df_return['场景类别'].count())
    elif df_in.reset_index(drop=True).equals(df.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
        df_return = df_return[(df_return['场景类别'].str.contains(x))]
        df_return = df_return[(df_return['场景类别'].str.contains(x, na=False))]
        print(x + '故障数：', df_return['场景类别'].count())
    else:
        print('错误的DF名')


df_F4 = df[(df['故障等级'].str.contains('F4|F3|F2|F1'))]
x1 = df_F4.是否系统发现.count()
x2 = df_F4[(df_F4['是否系统发现'] == '主动发现')].是否系统发现.count()
print('主动发现F4以上故障数: ', x2)
print('F4以上故障数: ', x1)

excel_one_line_to_list(df_主动发现, '白屏卡顿')
excel_one_line_to_list(df, '白屏卡顿')
excel_one_line_to_list(df_主动发现, '中断')
excel_one_line_to_list(df, '中断')
excel_one_line_to_list(df_主动发现, '业务跌零')
excel_one_line_to_list(df, '业务跌零')
excel_one_line_to_list(df_主动发现, '资金类')
excel_one_line_to_list(df, '资金类')
excel_one_line_to_list(df_主动发现, '舆情类')
excel_one_line_to_list(df, '舆情类')
excel_one_line_to_list(df_主动发现, '资损')
excel_one_line_to_list(df, '资损')
excel_one_line_to_list(df_主动发现, '触发红线')
excel_one_line_to_list(df, '触发红线')
# path2 = input("按回车退出")

# D:\pythonProject\故障>pyinstaller --console --onefile JXH.py

# D:\pythonProject\故障>pyinstaller -F -i bitbug_favicon.ico JXH.py


df_连续性 = df.copy()

df_连续性 = df_连续性[(df_连续性['是否连续性问题'] == '是') & (df_连续性['OC调度时长'] > 5)]
df_连续性['OC调度是否超时'] = '是'

print('连续性故障OC调度超时数：', df_连续性.OC调度是否超时.count())
if df_连续性.OC调度是否超时.count() > 0:
    print('连续性故障OC调度超时清单：')
    print(df_连续性[['故障单号', '故障等级', 'OC调度时长']])
else:
    print('无OC调度超时连续性故障')