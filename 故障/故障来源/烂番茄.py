#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math
from numpy import array

# 读取数据
df = pd.read_excel('d:/WJ/机器学习输入/JPG.xlsx')
wj = df.copy()
# df = df[['转入数量', '质检数', '参与处理故障数', '质检得分', '故障处理耗时得分']]
df = df[['转入数量', '质检数', '参与处理故障数']]
print(df)
# 数据预处理 ,去除空值的记录
df.dropna()


# print(df.iloc[: , 0:1])

# 定义熵值法函数
def cal_weight(x):
    '''熵值法计算变量的权重'''
    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) * 100 / (np.max(x) - np.min(x))))
    print(x)
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
    print("总贡献度: ", E)
    # 计算冗余度
    d = 1 - E.sum(axis=0)
    print("冗余度: ", d)
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
# d = w.iloc[3:4, 0:1].values[0][0]
# e = w.iloc[4:5, 0:1].values[0][0]
# wj['综合得分'] = ((a)*df['转入数量']+(b)*df['质检数']+(c)*df['参与处理故障数']+(d)*df['质检得分']+(e)*df['故障处理耗时得分'])
wj['综合得分'] = ((a) * df['转入数量'] + (b) * df['质检数'] + (c) * df['参与处理故障数'])
wj = wj.sort_values(by='综合得分', ascending=False).reset_index(drop=True)
wj['排名'] = wj.index + 1
print(wj)
# wj.to_excel("d:/WJ/故障数据输出/JPG.xls")
