#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
from numpy import array
# select 日期,case when 日期='2021-07' then sum(flag1)
#                  when 日期='2021-08' then sum(flag1)
#                  when 日期='2021-09' then sum(flag1)
#                  when 日期='2021-10' then sum(flag1)   end 九十以上
#            ,case when 日期='2021-07' then sum(flag2)
#                  when 日期='2021-08' then sum(flag2)
#                  when 日期='2021-09' then sum(flag2)
#                  when 日期='2021-10' then sum(flag2)   end 八十到九十
#            ,case when 日期='2021-07' then sum(flag3)
#                  when 日期='2021-08' then sum(flag3)
#                  when 日期='2021-09' then sum(flag3)
#                  when 日期='2021-10' then sum(flag3)   end 七十到八十
#            ,case when 日期='2021-07' then sum(flag4)
#                  when 日期='2021-08' then sum(flag4)
#                  when 日期='2021-09' then sum(flag4)
#                  when 日期='2021-10' then sum(flag4)   end 六十到七十
#            ,case when 日期='2021-07' then sum(flag5)
#                  when 日期='2021-08' then sum(flag5)
#                  when 日期='2021-09' then sum(flag5)
#                  when 日期='2021-10' then sum(flag5)   end 五十到六十
#            ,case when 日期='2021-07' then sum(flag6)
#                  when 日期='2021-08' then sum(flag6)
#                  when 日期='2021-09' then sum(flag6)
#                  when 日期='2021-10' then sum(flag6)   end 四十到五十
#            ,case when 日期='2021-07' then sum(flag7)
#                  when 日期='2021-08' then sum(flag7)
#                  when 日期='2021-09' then sum(flag7)
#                  when 日期='2021-10' then sum(flag7)   end 三十到四十
#            ,case when 日期='2021-07' then sum(flag8)
#                  when 日期='2021-08' then sum(flag8)
#                  when 日期='2021-09' then sum(flag8)
#                  when 日期='2021-10' then sum(flag8)   end 二十到三十
#            ,case when 日期='2021-07' then sum(flag9)
#                  when 日期='2021-08' then sum(flag9)
#                  when 日期='2021-09' then sum(flag9)
#                  when 日期='2021-10' then sum(flag9)   end 十到二十
#            ,case when 日期='2021-07' then sum(flag10)
#                  when 日期='2021-08' then sum(flag10)
#                  when 日期='2021-09' then sum(flag10)
#                  when 日期='2021-10' then sum(flag10)   end 十以下
# from (
# select to_char(a.日期,'yyyy-mm') 日期,
#      case when 得分>=90 then 1 end flag1,
#       case when 得分<90 and 得分>=80 then 1 end flag2,
#        case when 得分<80 and 得分>=70 then 1 end flag3,
#          case when 得分<70 and 得分>=60 then 1 end flag4,
#            case when 得分<60 and 得分>=50 then 1 end flag5,
#              case when 得分<50 and 得分>=40 then 1 end flag6,
#                case when 得分<40 and 得分>=30 then 1 end flag7,
#                  case when 得分<30 and 得分>=20 then 1 end flag8,
#                    case when 得分<20 and 得分>=10 then 1 end flag9,
#                      case when 得分<10  then 1 end flag10
#   from jxh_10_222 a) group by 日期;
# 读取数据
df = pd.read_excel('d:/WJ/机器学习输入/统计.xlsx')
wj = df.copy()
df = df.iloc[:, 1:]
df = df.fillna(value=0)

print(df)
# 定义熵值法函数
def cal_weight(x):
    '''熵值法计算变量的权重'''
    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))
    # x = x.apply(lambda x: ((np.max(x) - x) / (np.max(x) - np.min(x))))
    '''
    如果数据实际不为零，则赋予最小值
    if x==0:
        x=0.00001
    else:
        pass
    '''
    # 求k
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    k = 1.0 / math.log(rows)

    lnf = [[None] * cols for i in range(rows)]

    # 矩阵计算--
    # 信息熵

    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf
    # print("总贡献度: ", E)
    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # print("冗余度: ", d)
    # 计算各指标的权重
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # 计算各样本的综合得分,用最原始的数据

    w = pd.DataFrame(w)
    return w


if __name__ == '__main__':
    # 计算df各字段的权重
    w = cal_weight(df)  # 调用cal_weight
    w.index = df.columns
    w.columns = ['weight']
    print(w)  # 输出权重
    print('熵权法计算权重运行完成!')
a = w.iloc[0:1, 0:1].values[0][0]
b = w.iloc[1:2, 0:1].values[0][0]
c = w.iloc[2:3, 0:1].values[0][0]
d = w.iloc[3:4, 0:1].values[0][0]
e = w.iloc[4:5, 0:1].values[0][0]
f = w.iloc[5:6, 0:1].values[0][0]
g = w.iloc[6:7, 0:1].values[0][0]
h = w.iloc[7:8, 0:1].values[0][0]
i = w.iloc[8:9, 0:1].values[0][0]
j = w.iloc[9:10, 0:1].values[0][0]


wj['综合得分'] = ((a)*df['九十以上']+(b)*df['八十到九十']+(c)*df['七十到八十']+(d)*df['六十到七十']+(e)*df['五十到六十']+(f)*df['四十到五十']+(g)*df['三十到四十']+(h)*df['二十到三十']+(i)*df['十到二十']+(j)*df['十以下'])
wj = wj.sort_values(by='综合得分', ascending=False).reset_index(drop=True)
# wj['排名'] = wj.index + 1
print(wj)
wj.to_excel("d:/WJ/机器学习输入/gz.xls")