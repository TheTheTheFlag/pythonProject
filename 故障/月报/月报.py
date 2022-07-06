# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :pythonProject
# @File     :周报v4.0
# @Date     :2022/3/9 8:41
# @Author   :JXH
# @Email    :1762556953@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
# 1、取消资金类，特保类主动发现率输出
# 2、重复模块统计周期变更为近30天
# 3、BOE业务重灾区较上周期
from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', None)

path = 'D:/WJ/数据准备/周报数据/数据.xlsx'
start_date = '20220301'
end_date = '20220320'
diff_start = str(int(start_date) - 100)  # 上月1号
diff_end = str(int(end_date) - 100)  # 上月今天
df_all = pd.read_excel(path)
df_all.fillna(value=0)
df_all['人工反馈时间'] = pd.to_datetime(df_all['人工反馈时间'], format='%Y%m%d %H:%M:%S', errors='coerce')
df_mon = df_all.copy()
df_mon = df_mon[(df_mon['故障单号'].str[2:10] >= str(start_date)) & (df_mon['故障单号'].str[2:10] <= str(end_date))]  # 本月

df_last_mon = df_all.copy()
df_last_mon = df_last_mon[
    (df_last_mon['故障单号'].str[2:10] >= str(diff_start)) & (df_last_mon['故障单号'].str[2:10] <= str(diff_end))]  # 上月同期

df_last_30d = df_all.copy()
df_last_30d = df_last_30d[
    (df_last_30d['故障单号'].str[2:10] >= str(diff_end)) & (df_last_30d['故障单号'].str[2:10] <= str(end_date))]  # 近30天

df_gzs = df_mon.copy()
df_gzs_same = df_gzs[(df_gzs['故障等级'] == '同原因')]
print('G5及以上故障数【{0}起】，同原因故障数【{1}起】'.format(df_gzs.故障单号.count(), df_gzs_same.故障单号.count()))

# 系统可用率及影响时长
天数 = pd.to_datetime(end_date) - pd.to_datetime(start_date)
天数 = 天数.days + 1
影响时长 = round(df_gzs['故障影响时长'].sum(), 2)  # 卡顿中断跌零：单地市乘以业务下降百分比后再乘以0.5  卡顿：单次故障上限6分钟
系统使用时长 = 24 * 60 * 天数
系统可用率 = round((系统使用时长 - 影响时长) / 系统使用时长 * 100, 2)
print('系统可用率【{0}%】，影响时长【{1}min】'.format(系统可用率, 影响时长))

# 1-5-10及时率
df_lxx = df_gzs_same[(df_gzs_same['是否连续性问题'] == '是')]
# 连续性故障数 = df_lxx.故障单号.count()
# 一五十超时故障数 = df_lxx[pd.notnull(df_lxx['SLA超时原因'])].故障单号.count()
# 一五十达标率 = round((连续性故障数 - 一五十超时故障数) / 连续性故障数 * 100)
# print('1-5-10及时率【{0}% ({1}/{2})】，原因①【x起】，原因②【x起】，原因③【x起】'.format(一五十达标率, 连续性故障数 - 一五十超时故障数, 连续性故障数))
print('1-5-10及时率【x% (x/x)】，原因①【x起】，原因②【x起】，原因③【x起】')

# oc调度超时 连续性故障清单中响应时长大于5的部分
df_oc = df_gzs.copy()
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


故障分 = fault_score(df_gzs)
本月故障分 = fault_score(df_mon)
# 提前发现多久
df_before = df_gzs.copy()

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
# a = df_gzs['是否系统发现'][df_gzs.是否系统发现 == '主动发现'].count()
# print('平均提前发现:', str(round(c / a, 2)) + '分钟')
df_F4 = df_gzs[(df_gzs['故障等级'].str.contains('F4|F3|F2|F1'))]
x1 = df_F4.是否系统发现.count()
x2 = df_F4[(df_F4['是否系统发现'] == '主动发现')].是否系统发现.count()
if x1 == 0:
    print('本月故障分【{0}分】：F4【{1}分】，G4【{2}分】，F4及以上主动发现率【-】，平均提前【{3}分钟】发现。'.format(故障分, fault_score(
        df_gzs[(df_gzs['故障等级'] == 'G5F4')]), fault_score(
        df_gzs[(df_gzs['故障等级'] == 'G4F4')]) + fault_score(
        df_gzs[(df_gzs['故障等级'] == 'G4F3')]) + fault_score(
        df_gzs[(df_gzs['故障等级'] == 'G4F2')]) + fault_score(
        df_gzs[(df_gzs['故障等级'] == 'G4F1')]),
                                                                              round(c / a, 2),
                                                                              本月故障分, c))
else:
    print(
        '本月故障分【{0}分】：F4【{1}分】，G4【{2}分】，F4及以上主动发现率【{3:.0%} {4}/{5}】，平均提前【{6}分钟】发现。'.format(
            故障分,
            fault_score(df_gzs[(df_gzs['故障等级'] == 'G5F4')]),
            fault_score(df_gzs[(df_gzs['故障等级'] == 'G4F4')]) + fault_score(
                df_gzs[(df_gzs['故障等级'] == 'G4F3')]) + fault_score(df_gzs[(df_gzs['故障等级'] == 'G4F2')]) + fault_score(
                df_gzs[(df_gzs['故障等级'] == 'G4F1')]),
            x2 / x1,
            x2,
            x1,
            round(c / a, 2),
            本月故障分,
            c))
# 各类故障主动发现率
df_主动发现 = df_gzs.copy()
df_qd = df_gzs.copy()
df_主动发现 = df_主动发现[df_主动发现['是否系统发现'] == '主动发现']


def excel_one_line_to_list(df_in, x):
    if df_in.reset_index(drop=True).equals(df_主动发现.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
        df_return = df_return[(df_return['场景类别'].str.contains(x, na=False))]
        return df_return['场景类别'].count()
    elif df_in.reset_index(drop=True).equals(df_qd.reset_index(drop=True)):
        df_return = df_in
        df_return['场景类别'].fillna("无", inplace=True)
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

卡顿报错故障 = excel_one_line_to_list(df_qd, '卡顿报错')
卡顿报错 = excel_one_line_to_list(df_主动发现, '卡顿报错')
if 卡顿报错故障 == 0:
    print('卡顿报错类故障【0起】，主动发现率【-】')
else:
    print('卡顿报错类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(卡顿报错, 卡顿报错故障, 卡顿报错 / 卡顿报错故障))

业务跌零故障 = excel_one_line_to_list(df_qd, '业务跌零')
业务跌零 = excel_one_line_to_list(df_主动发现, '业务跌零')
if 业务跌零故障 == 0:
    print('跌零类故障【0起】，主动发现率【-】')
else:
    print('跌零类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(业务跌零, 业务跌零故障, 业务跌零 / 业务跌零故障))

# 资金类故障 = excel_one_line_to_list(df_qd, '资金类')
# 资金类 = excel_one_line_to_list(df_主动发现, '资金类')
# if 资金类故障 == 0:
#     print('资金类故障【0起】，主动发现率【-】')
# else:
#     print('资金类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(资金类, 资金类故障, 资金类 / 资金类故障))
#
# 特保类故障 = excel_one_line_to_list(df_qd, '特保')
# 特保类 = excel_one_line_to_list(df_主动发现, '特保')
# if 特保类故障 == 0:
#     print('特保类故障【0起】，主动发现率【-】')
# else:
#     print('特保类故障【{0}/{1}起】，主动发现率【{2:.0%}】'.format(特保类, 特保类故障, 特保类 / 特保类故障))

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
全黑 = 全黑[['日期', '发布方式', '需求数']]
全黑 = 全黑[(df_all['日期'] >= str(s_date)) & (df_all['日期'] <= str(e_date)) & (df_all['发布方式'] == '全黑发布')]
全黑 = 全黑.drop_duplicates().reset_index()
group_全黑 = 全黑.groupby(['日期', '发布方式'])  # 分组统计
全黑需求数 = group_全黑.sum().reset_index().需求数.sum()
灰度 = df_all.copy()
灰度 = 灰度[['日期', '发布方式', '需求数']]
灰度 = 灰度[(df_all['日期'] >= str(s_date)) & (df_all['日期'] <= str(e_date)) & (df_all['发布方式'] == '灰度发布')]
灰度 = 灰度.drop_duplicates().reset_index()
group_灰度 = 灰度.groupby(['日期', '发布方式'])  # 分组统计
灰度需求数 = group_灰度.sum().reset_index().需求数.sum()
灰度需求数.astype(int)

x5 = df_qd[(df_qd['是否经过灰度'] == 1)].故障单号.count()
print('灰度需求数【{0}起】，全黑需求数【{1}起】，灰度未发现故障数【{2}起】'.format(int(灰度需求数), int(全黑需求数), int(x5)))
print('')
# 影响模块TOP
# df_影响模块 = df_last_30d.copy() # 近30天
df_影响模块 = df_mon.copy()  # 本月

df_影响模块 = df_影响模块[['故障单号', '影响模块', '处理大组']]
df_影响模块 = df_影响模块.groupby(['影响模块', '处理大组']).count().reset_index()
df_影响模块.fillna(value=0)
BOE_影响模块 = df_影响模块[(df_影响模块['处理大组'] == 'BOE') & (df_影响模块['故障单号'] >= 2)]
BOE_影响模块 = BOE_影响模块.sort_values(by="故障单号", ascending=False)
SRE_影响模块 = df_影响模块[(df_影响模块['处理大组'] == 'SRE') & (df_影响模块['故障单号'] >= 2)]
SRE_影响模块 = SRE_影响模块.sort_values(by="故障单号", ascending=False)

if BOE_影响模块['影响模块'].count() > 1:
    print('近30天boe影响模块top{0}：'.format(BOE_影响模块['影响模块'].count()))
    for i in range(BOE_影响模块['影响模块'].count()):
        print('{0}【{1}起】'.format(BOE_影响模块.iloc[i, 0], BOE_影响模块.iloc[i, 2]))
elif BOE_影响模块['影响模块'].count() == 1:
    print('近30天boe影响模块top1：')
    print('{0}【{1}起】'.format(BOE_影响模块.iloc[0, 0], BOE_影响模块.iloc[0, 2]))
else:
    print('近30天无boe影响模块top数据')

if SRE_影响模块['影响模块'].count() > 1:
    print('近30天sre影响模块top{0}：'.format(SRE_影响模块['影响模块'].count()))
    for i in range(SRE_影响模块['影响模块'].count()):
        print('{0}【{1}起】'.format(SRE_影响模块.iloc[i, 0], SRE_影响模块.iloc[i, 2]))
elif SRE_影响模块['影响模块'].count() == 1:
    print('近30天sre影响模块top1：')
    print('{0}【{1}起】'.format(SRE_影响模块.iloc[0, 0], SRE_影响模块.iloc[0, 2]))
else:
    print('近30天无sre影响模块top数据')

# 重复故障
BOE_重复故障 = df_mon.copy()
BOE_重复故障['场景类别'].fillna("无", inplace=True)
BOE_重复故障 = BOE_重复故障[(BOE_重复故障['维护责任大组'] == 'BOE') & (BOE_重复故障['场景类别'].str.contains('重复故障', na=False))]
df_boe_cf = BOE_重复故障.values.tolist()
result_boe_cf = []
for boe_cf in df_boe_cf:
    result_boe_cf.append(boe_cf[2])
SRE_重复故障 = df_mon.copy()
SRE_重复故障['场景类别'].fillna("无", inplace=True)
SRE_重复故障 = SRE_重复故障[(SRE_重复故障['维护责任大组'] == 'SRE') & (SRE_重复故障['场景类别'].str.contains('重复故障', na=False))]
df_sre_cf = SRE_重复故障.values.tolist()
result_sre_cf = []
for sre_cf in df_sre_cf:
    result_sre_cf.append(sre_cf[2])
print('')
if BOE_重复故障['维护责任大组'].count() > 0:
    print('本月BOE重复故障{0}起：'.format(BOE_重复故障['维护责任大组'].count()))
    print(result_boe_cf)
else:
    print('本月BOE无重复故障')
if SRE_重复故障['维护责任大组'].count() > 0:
    print('本月SRE重复故障{0}起：'.format(SRE_重复故障['维护责任大组'].count()))
    print(result_sre_cf)
else:
    print('本月SRE无重复故障')

# BOE业务重灾区
BOE_重灾区1 = df_mon.copy()
BOE_重灾区1 = BOE_重灾区1[(BOE_重灾区1['维护责任大组'] == 'BOE')]
BOE_重灾区2 = df_last_mon.copy()
BOE_重灾区2 = BOE_重灾区2[(BOE_重灾区2['维护责任大组'] == 'BOE')]
BOE_重灾区1 = BOE_重灾区1[['故障单号', '维护责任组']]
BOE_重灾区1 = BOE_重灾区1.groupby(['维护责任组']).count().reset_index()
BOE_重灾区2 = BOE_重灾区2[['故障单号', '维护责任组']]
BOE_重灾区2 = BOE_重灾区2.groupby(['维护责任组']).count().reset_index()

BOE_重灾区 = pd.merge(BOE_重灾区1, BOE_重灾区2, on=['维护责任组'], how='outer')
BOE_重灾区.columns = ['维护责任组', '本月故障数', '上月同期故障数']
BOE_重灾区['上月同期故障数'] = BOE_重灾区['上月同期故障数'].fillna(1)
BOE_重灾区['同比'] = round((BOE_重灾区['本月故障数'] - BOE_重灾区['上月同期故障数']) * 100 / BOE_重灾区['上月同期故障数'], 2)
print('')
print(BOE_重灾区.sort_values(by="同比", ascending=False))

with pd.ExcelWriter('D:/WJ/数据准备/周报数据/1月.xlsx') as writer:
    BOE_影响模块.to_excel(writer, sheet_name='BOE_影响模块', index=False)
    SRE_影响模块.to_excel(writer, sheet_name='SRE_影响模块', index=False)
    BOE_重灾区.to_excel(writer, sheet_name='BOE_重灾区', index=False)
