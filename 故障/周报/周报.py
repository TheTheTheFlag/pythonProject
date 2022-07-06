# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :周报V3.0
# @Date     :2022/2/10 15:12
# @Author   :JXH
# @Email    :1762556953@qq.com
# @Software :PyCharm
-------------------------------------------------
"""

from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', None)

path = 'D:/WJ/数据准备/周报数据/数据.xlsx'
start_date = '20220328'
end_date = '20220402'
first_date = '20220301'
df_all = pd.read_excel(path)
df_all.fillna(value=0)
df_all['人工反馈时间'] = pd.to_datetime(df_all['人工反馈时间'], format='%Y%m%d %H:%M:%S', errors='coerce')
df_mon = df_all.copy()
df_mon = df_mon[(df_mon['故障单号'].str[2:10] >= first_date)]
# df_mon = df_mon[(df_mon['日期'] >= first_date)]
#  限定期限内清单
df_week = df_all[(df_all['故障单号'].str[2:10] >= str(start_date)) & (df_all['故障单号'].str[2:10] <= str(end_date))]
# df_week = df_all[(df_all['日期'] >= start_date) & (df_all['日期'] <= end_date)]
#  去除同原因清单
# df_week_alone = df_week[(df_week['故障等级'] != '同原因')]
df_week_alone = df_week
#  同原因清单
df_week_double = df_week[(df_week['故障等级'] == '同原因')]
print('G5及以上故障数【{0}起】，同原因故障数【{1}起】'.format(df_week.故障单号.count(), df_week_double.故障单号.count()))

# 系统可用率及影响时长
天数 = pd.to_datetime(end_date) - pd.to_datetime(start_date)
天数 = 天数.days + 1
影响时长 = round(df_week['故障影响时长'].sum(), 2)  # 卡顿中断跌零：单地市乘以业务下降百分比后再乘以0.5  卡顿：单次故障上限6分钟
系统使用时长 = 24 * 60 * 天数
系统可用率 = round((系统使用时长 - 影响时长) / 系统使用时长 * 100, 2)
print('系统可用率【{0}%】，影响时长【{1}min】'.format(系统可用率, 影响时长))

# 1-5-10及时率
df_lxx = df_week.copy()
df_lxx = df_lxx[(df_lxx['是否连续性问题'] == 1)]
连续性故障数 = df_lxx.故障单号.count()
一五十超时故障数 = df_lxx[(df_lxx['SLA是否达标'] == 0)].故障单号.count()
一五十达标率 = round((连续性故障数 - 一五十超时故障数) / 连续性故障数 * 100, 2)
print('1-5-10及时率【{0}% ({1}/{2})】，原因①【x起】，原因②【x起】，原因③【x起】'.format(一五十达标率, 连续性故障数 - 一五十超时故障数, 连续性故障数))
# print('1-5-10及时率【x% (x/x)】，原因①【x起】，原因②【x起】，原因③【x起】')

# oc调度超时 连续性故障清单中响应时长大于5的部分
df_oc = df_week_alone.copy()
df_oc = df_oc[(df_oc['是否连续性问题'] == '是') & (df_lxx['响应时长'] > 5)]
df_oc['OC调度是否超时'] = '是'

df_li = df_oc.values.tolist()
result = []
for s_li in df_li:
    result.append(s_li[2])

if df_oc.OC调度是否超时.count() > 0:
    print('oc调度超时【{0}起】，原因①【x起】，原因②【x起】，原因③【x起】'.format(df_oc.OC调度是否超时.count()))
    # print('连续性故障OC调度超时清单：')
    # print(result)
else:
    print('无OC调度超时连续性故障')


# 故障分及F4以上故障主动发现率
def fault_score(df_in):
    df = df_in
    G1F1扣分 = df[(df['故障等级'] == 'G1F1')].故障单号.count() * 160
    G2F1扣分 = df[(df['故障等级'] == 'G2F1')].故障单号.count() * 120
    G2F2扣分 = df[(df['故障等级'] == 'G2F2')].故障单号.count() * 80
    G3F1扣分 = df[(df['故障等级'] == 'G3F1')].故障单号.count() * 100
    G3F2扣分 = df[(df['故障等级'] == 'G3F2')].故障单号.count() * 60
    G3F3扣分 = df[(df['故障等级'] == 'G3F3')].故障单号.count() * 40
    G4F1扣分 = df[(df['故障等级'] == 'G4F1')].故障单号.count() * 80
    G4F2扣分 = df[(df['故障等级'] == 'G4F2')].故障单号.count() * 40
    G4F3扣分 = df[(df['故障等级'] == 'G4F3')].故障单号.count() * 20
    G4F4扣分 = df[(df['故障等级'] == 'G4F4')].故障单号.count() * 10
    G5F1扣分 = df[(df['故障等级'] == 'G5F1')].故障单号.count() * 20
    G5F2扣分 = df[(df['故障等级'] == 'G5F2')].故障单号.count() * 10
    G5F3扣分 = df[(df['故障等级'] == 'G5F3')].故障单号.count() * 5
    G5F4扣分 = df[(df['故障等级'] == 'G5F4')].故障单号.count() * 1
    故障分 = G1F1扣分 + G2F1扣分 + G2F2扣分 + G3F1扣分 + G3F2扣分 + G3F3扣分 + G4F1扣分 + G4F2扣分 + G4F3扣分 + G4F4扣分 + G5F1扣分 + G5F2扣分 + G5F3扣分 + G5F4扣分
    return 故障分


故障分 = fault_score(df_week_alone)
本月故障分 = fault_score(df_mon)
# 提前发现多久
df_before = df_week_alone.copy()

df_before = df_before[(df_before['是否系统发现'] == '主动发现')]
df_before = df_before[pd.notnull(df_before.主动发现时间)]  # 主动发现时间不为空
df_before = df_before[pd.notnull(df_before.人工反馈时间)]  # 人工反馈时间不为空
# df_before = df_before[(df_before['人工反馈时间'] > df_before['主动发现时间'])]
df_before["提前发现多久"] = df_before.人工反馈时间 - df_before.主动发现时间
df_before["提前发现多久"] = df_before["提前发现多久"].astype('timedelta64[m]')
df_before.to_excel('d:/WJ/数据准备/提前发现率.xlsx', index=False)
c = df_before['提前发现多久'].sum()
a = df_before['提前发现多久'].count()
if a <= 1:
    a = 1
else:
    a = a
# a = df_week_alone['是否系统发现'][df_week_alone.是否系统发现 == '主动发现'].count()
# print('平均提前发现:', str(round(c / a, 2)) + '分钟')
df_F4 = df_week_alone[(df_week_alone['故障等级'].str.contains('F4|F3|F2|F1'))]
x1 = df_F4.是否系统发现.count()
x2 = df_F4[(df_F4['是否系统发现'] == '主动发现')].是否系统发现.count()
if x1 == 0:
    print('本月累计【{4}分】，本周故障分【{0}分】：F4【{1}分】，G4【{2}分】，F4及以上主动发现率【-】，平均提前【{3}分钟】发现。'.format(故障分, fault_score(
        df_week_alone[(df_week_alone['故障等级'] == 'G5F4')]), fault_score(
        df_week_alone[(df_week_alone['故障等级'] == 'G4F4')]) + fault_score(
        df_week_alone[(df_week_alone['故障等级'] == 'G4F3')]) + fault_score(
        df_week_alone[(df_week_alone['故障等级'] == 'G4F2')]) + fault_score(
        df_week_alone[(df_week_alone['故障等级'] == 'G4F1')]),
                                                                                         round(c / a, 2),
                                                                                         本月故障分, c, a))
else:
    print(
        '本月累计【{7}分】，本周故障分【{0}分】：F4【{1}分】，G4【{2}分】，F4及以上主动发现率【{3:.0%} {4}/{5}】，平均提前【{6}分钟】发现。'.format(故障分,
                                                                                                     fault_score(
                                                                                                         df_week_alone[
                                                                                                             (
                                                                                                                     df_week_alone[
                                                                                                                         '故障等级'] == 'G5F4')]),
                                                                                                     fault_score(
                                                                                                         df_week_alone[
                                                                                                             (
                                                                                                                     df_week_alone[
                                                                                                                         '故障等级'] == 'G4F4')]) + fault_score(
                                                                                                         df_week_alone[
                                                                                                             (
                                                                                                                     df_week_alone[
                                                                                                                         '故障等级'] == 'G4F3')]) + fault_score(
                                                                                                         df_week_alone[
                                                                                                             (
                                                                                                                     df_week_alone[
                                                                                                                         '故障等级'] == 'G4F2')]) + fault_score(
                                                                                                         df_week_alone[
                                                                                                             (
                                                                                                                     df_week_alone[
                                                                                                                         '故障等级'] == 'G4F1')]),
                                                                                                     x2 / x1,
                                                                                                     x2, x1,
                                                                                                     round(
                                                                                                         c / a,
                                                                                                         2),
                                                                                                     本月故障分,
                                                                                                     c, a))
# 各类故障主动发现率
df_主动发现 = df_week_alone.copy()
df_qd = df_week_alone.copy()
df_主动发现 = df_主动发现[df_主动发现['是否系统发现'] == '主动发现']


def excel_one_line_to_list(df_in, x):
    if df_in.reset_index(drop=True).equals(df_主动发现.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
        # df_return = df_return[(df_return['场景类别'].str.contains(x))]
        df_return = df_return[(df_return['场景类别'].str.contains(x, na=False))]
        return df_return['场景类别'].count()
    elif df_in.reset_index(drop=True).equals(df_qd.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
        # df_return = df_return[(df_return['场景类别'].str.contains(x))]
        df_return = df_return[(df_return['场景类别'].str.contains(x, na=False))]
        return df_return['场景类别'].count()
    else:
        print('错误的DF名')


舆情类故障 = excel_one_line_to_list(df_qd, '舆情类')
舆情类 = excel_one_line_to_list(df_主动发现, '舆情类')
if 舆情类故障 == 0:
    print('舆情类故障【0起】，主动发现率【-】')
else:
    print('舆情类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(舆情类, 舆情类故障, 舆情类 / 舆情类故障))

卡顿故障 = excel_one_line_to_list(df_qd, '卡顿')
卡顿 = excel_one_line_to_list(df_主动发现, '卡顿')
if 卡顿故障 == 0:
    print('卡顿类故障【0起】，主动发现率【-】')
else:
    print('卡顿类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(卡顿, 卡顿故障, 卡顿 / 卡顿故障))

报错故障 = excel_one_line_to_list(df_qd, '报错')
报错 = excel_one_line_to_list(df_主动发现, '报错')
if 报错故障 == 0:
    print('报错类故障【0起】，主动发现率【-】')
else:
    print('报错类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(报错, 报错故障, 报错 / 报错故障))

业务跌零故障 = excel_one_line_to_list(df_qd, '业务跌零')
业务跌零 = excel_one_line_to_list(df_主动发现, '业务跌零')
if 业务跌零故障 == 0:
    print('跌零类故障【0起】，主动发现率【-】')
else:
    print('跌零类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(业务跌零, 业务跌零故障, 业务跌零 / 业务跌零故障))

资金类故障 = excel_one_line_to_list(df_qd, '资金类')
资金类 = excel_one_line_to_list(df_主动发现, '资金类')
if 资金类故障 == 0:
    print('资金类故障【0起】，主动发现率【-】')
else:
    print('资金类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(资金类, 资金类故障, 资金类 / 资金类故障))

特保类故障 = excel_one_line_to_list(df_qd, '特保')
特保类 = excel_one_line_to_list(df_主动发现, '特保')
if 特保类故障 == 0:
    print('特保类故障【0起】，主动发现率【-】')
else:
    print('特保类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(特保类, 特保类故障, 特保类 / 特保类故障))

资损故障 = excel_one_line_to_list(df_qd, '资损')
资损 = excel_one_line_to_list(df_主动发现, '资损')
if 资损故障 == 0:
    pass
else:
    print('资损类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(资损, 资损故障, 资损 / 资损故障))

触发红线故障 = excel_one_line_to_list(df_qd, '触发红线')
触发红线 = excel_one_line_to_list(df_主动发现, '触发红线')
if 触发红线故障 == 0:
    pass
else:
    print('触发红线类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(触发红线, 触发红线故障, 触发红线 / 触发红线故障))

# 灰度未发现故障数
s_date = datetime.strptime(start_date, '%Y%m%d').date()
e_date = datetime.strptime(end_date, '%Y%m%d').date()
全黑 = df_all.copy()
全黑 = 全黑[['日期', '全黑需求数']]
全黑 = 全黑[(df_all['日期'] >= str(s_date)) & (df_all['日期'] <= str(e_date))]
全黑 = 全黑.drop_duplicates().reset_index()
group_全黑 = 全黑.groupby(['日期'])  # 分组统计
全黑需求数 = group_全黑.sum().reset_index().全黑需求数.sum()
灰度 = df_all.copy()
灰度 = 灰度[['日期', '灰度需求数']]
灰度 = 灰度[(df_all['日期'] >= str(s_date)) & (df_all['日期'] <= str(e_date))]
灰度 = 灰度.drop_duplicates().reset_index()
group_灰度 = 灰度.groupby(['日期'])  # 分组统计
灰度需求数 = group_灰度.sum().reset_index().灰度需求数.sum()
灰度需求数.astype(int)

x5 = df_qd[(df_qd['是否经过灰度'] == 1)].故障单号.count()
print('灰度需求数【{0}起】，全黑需求数【{1}起】，灰度未发现故障数【{2}起】'.format(int(灰度需求数), int(全黑需求数), int(x5)))

# 影响模块TOP
df_影响模块 = df_week_alone.copy()
df_影响模块 = df_影响模块[['故障单号', '影响模块', '处理大组']]
df_影响模块 = df_影响模块.groupby(['影响模块', '处理大组']).count().reset_index()

df_影响模块.fillna(value=0)
BOE_影响模块 = df_影响模块[(df_影响模块['处理大组'] == 'BOE') & (df_影响模块['故障单号'] >= 2)]
BOE_影响模块 = BOE_影响模块.sort_values(by="故障单号", ascending=False)
SRE_影响模块 = df_影响模块[(df_影响模块['处理大组'] == 'SRE') & (df_影响模块['故障单号'] >= 2)]
SRE_影响模块 = SRE_影响模块.sort_values(by="故障单号", ascending=False)

if BOE_影响模块['影响模块'].count() > 1:
    print('boe影响模块top{0}：'.format(BOE_影响模块['影响模块'].count()))
    for i in range(BOE_影响模块['影响模块'].count()):
        print('{0}【{1}起】'.format(BOE_影响模块.iloc[i, 0], BOE_影响模块.iloc[i, 2]))
elif BOE_影响模块['影响模块'].count() == 1:
    print('boe影响模块top1：')
    print('{0}【{1}起】'.format(BOE_影响模块.iloc[0, 0], BOE_影响模块.iloc[0, 2]))
else:
    print('无boe影响模块top数据')
print('')
if SRE_影响模块['影响模块'].count() > 1:
    print('sre影响模块top{0}：'.format(SRE_影响模块['影响模块'].count()))
    for i in range(SRE_影响模块['影响模块'].count()):
        print('{0}【{1}起】'.format(SRE_影响模块.iloc[i, 0], SRE_影响模块.iloc[i, 2]))
elif SRE_影响模块['影响模块'].count() == 1:
    print('sre影响模块top1：')
    print('{0}【{1}起】'.format(SRE_影响模块.iloc[0, 0], SRE_影响模块.iloc[0, 2]))
else:
    print('无sre影响模块top数据')
