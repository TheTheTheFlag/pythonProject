from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import os
import numpy as np
import pandas as pd
import time
from pandas import Series, DataFrame
from datetime import datetime
from numpy import random, mean
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pandas import DataFrame, read_excel

df_001 = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xls')
df_001 = df_001.fillna(value=0)
df_001_path = df_001[['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']]
df_001[['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']] = df_001[
    ['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']]
df1 = df_001[['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '今天人数']]
print(df1)
df2 = df_001[['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数']]

#
# list_007_1 = []
# for line in df:
#     list_007_1.append(line)
# df_007_x = []
# df_007_max = []
#
# for i in range(len(df)):
#     df_007_x.append(df.iloc[i].values)
#     numbers = [float(x) for x in df_007_x[i]]
#     df_007_max.append(int(max(numbers)))
#     # print(max(df_007_max))
# # 方法2
# file = r'D:\WJ\用户画像输入\近7天活跃人数.xlsx'
# df = pd.read_excel(file)
# num_list = [df.columns[j] for j, i in enumerate(df.dtypes) if i in [np.float64, np.int64]]
# print(num_list)
# # del num_list[-1]
# # del num_list[-1]
# num_list = num_list[0:8] + num_list[7:8]
# print(num_list)
#
# a = [df[i].max() for i in num_list]
# print(max(a))

# # 方法3
# def openfile(path):
#     # 读取文件，然后构成字典
#     # path文件路径
#     # sheet_name:选取表的表名，默认是第一张表
#     df = DataFrame(read_excel(path))
#     num_list = [df.columns[j] for j, i in enumerate(df.dtypes) if i in [np.float64, np.int64]]
#     print(num_list)
#     # del num_list[-1]
#     # del num_list[-1]
#     num_list = num_list[0:8] + num_list[7:8]
#     print(num_list)
#
#     a = [df[i].max() for i in num_list]
#     print(max(a))
#
#
# if __name__ == '__main__':
#     path = 'd:/WJ/用户画像输入/近7天活跃人数.xlsx'
#     openfile(path)

# 方法4
max_1 = 100
mean_1 = 100

def openfile(max_path):
    global max_1
    global mean_1
    # 读取文件，然后构成字典
    # path文件路径
    # sheet_name:选取表的表名，默认是第一张表
    df_path = max_path
    num_list_path = [df_path.columns[j] for j, i in enumerate(df_path.dtypes) if i in [np.float64, np.int64]]
    # num_list = num_list[0:8] + num_list[7:8]
    a = [df_path[i].max() for i in num_list_path]
    b = [df_path[i].mean() for i in num_list_path]
    max_1 = int(max(b))
    mean_1 = int(mean(b))
    print(max_1)


df_001_path_2 = df_001[['前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数']]

if __name__ == '__main__':
    max_path = df_001_path
    openfile(max_path)
#print(max_1)

# if __name__ == '__main__':
#     max_path = df_001_path_2
#     openfile(max_path)
#
# #print(max_1)
