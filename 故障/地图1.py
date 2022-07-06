# coding:utf-8
from typing import List

import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line
import pandas as pd
import os
import datetime
import pyecharts.options as opts

from pyecharts.charts import Timeline, Pie

# 获取日期列表
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


#time_list = get_nday_list(8)
time_list = ['2021-08-03', '2021-08-04', '2021-08-05']

df = pd.read_excel('d:/WJ/用户画像输入/近7天活跃人数.xls')
df = df.fillna(value=0)

df[['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']] = df[
    ['地市', '前7天人数', '前6天人数', '前5天人数', '前4天人数', '前3天人数', '前2天人数', '前1天人数', '当天人数']].applymap(lambda x: str(x).strip())
df1 = df[['地市', '前7天人数']]
df2 = df[['地市', '前6天人数']]
df3 = df[['地市', '前5天人数']]
df4 = df[['地市', '前4天人数']]
df5 = df[['地市', '前3天人数']]
df6 = df[['地市', '前2天人数']]
df7 = df[['地市', '前1天人数']]
df8 = df[['地市', '当天人数']]

city = df1.地市
print(city)
values1 = df1.前7天人数
print(values1)
values2 = df2.前6天人数
values3 = df3.前5天人数
values4 = df4.前4天人数
values5 = df5.前3天人数
values6 = df6.前2天人数
values7 = df7.前1天人数
values8 = df8.当天人数

list1 = [[city[i] + "市", int(float(values1[i]))] for i in range(len(city))]
list2 = [[city[i] + "市", int(float(values2[i]))] for i in range(len(city))]
list3 = [[city[i] + "市", int(float(values3[i]))] for i in range(len(city))]
list4 = [[city[i] + "市", int(float(values4[i]))] for i in range(len(city))]
list5 = [[city[i] + "市", int(float(values5[i]))] for i in range(len(city))]
list6 = [[city[i] + "市", int(float(values6[i]))] for i in range(len(city))]
list7 = [[city[i] + "市", int(float(values7[i]))] for i in range(len(city))]
list8 = [[city[i] + "市", int(float(values8[i]))] for i in range(len(city))]

list10 = [list1, list2, list3, list4, list5, list6, list7, list8]
dict1 = {time_list[i]: list10[i] for i in range(len(time_list))}
print(dict1)
# 数据准备
#data = [{"time": "2021-08-03", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-04", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-05", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-06", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-07", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-08", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-09", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}, {"time": "2021-08-10", "data": [{"name": "金华市", "value": 19}, {"name": "嘉兴市", "value": 4}, {"name": "湖州市", "value": 1}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 19}, {"name": "台州市", "value": 8}, {"name": "舟山市", "value": 13}, {"name": "衢州市", "value": 2}, {"name": "绍兴市", "value": 5}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 15}, {"name": "金华市", "value": 33}, {"name": "嘉兴市", "value": 13}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 23}, {"name": "温州市", "value": 101}, {"name": "台州市", "value": 6}, {"name": "舟山市", "value": 2}, {"name": "衢州市", "value": 1}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 8}, {"name": "金华市", "value": 25}, {"name": "嘉兴市", "value": 7}, {"name": "湖州市", "value": 3}, {"name": "宁波市", "value": 13}, {"name": "温州市", "value": 43}, {"name": "台州市", "value": 3}, {"name": "舟山市", "value": 3}, {"name": "衢州市", "value": 4}, {"name": "绍兴市", "value": 14}, {"name": "丽水市", "value": 3}, {"name": "杭州市", "value": 10}, {"name": "金华市", "value": 10}, {"name": "嘉兴市", "value": 6}, {"name": "湖州市", "value": 2}, {"name": "宁波市", "value": 17}, {"name": "温州市", "value": 26}, {"name": "台州市", "value": 11}, {"name": "舟山市", "value": 1}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 7}, {"name": "丽水市", "value": 1}, {"name": "杭州市", "value": 54}, {"name": "金华市", "value": 14}, {"name": "嘉兴市", "value": 11}, {"name": "湖州市", "value": 8}, {"name": "宁波市", "value": 10}, {"name": "温州市", "value": 33}, {"name": "台州市", "value": 7}, {"name": "舟山市", "value": 4}, {"name": "衢州市", "value": 3}, {"name": "绍兴市", "value": 12}, {"name": "丽水市", "value": 2}, {"name": "杭州市", "value": 19}, {"name": "金华市", "value": 1}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 0}, {"name": "温州市", "value": 10}, {"name": "台州市", "value": 2}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 6}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 2}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 9}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 0}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 0}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 2}, {"name": "金华市", "value": 0}, {"name": "嘉兴市", "value": 8}, {"name": "湖州市", "value": 0}, {"name": "宁波市", "value": 1}, {"name": "温州市", "value": 2}, {"name": "台州市", "value": 1}, {"name": "舟山市", "value": 7}, {"name": "衢州市", "value": 0}, {"name": "绍兴市", "value": 6}, {"name": "丽水市", "value": 0}, {"name": "杭州市", "value": 3}]}]
new_list = list()
for i in dict1.keys():
    one_dict = dict()
    one_dict['time'] = i
    one_dict['data'] = []
    new_list.append(one_dict)
    for j in dict1.values():
        for g in j:
            two_dict = dict()
            two_dict['name'] = g[0]
            two_dict['value'] = g[1]
            one_dict['data'].append(two_dict)

data = new_list
print(data)

data1 = [
    {
        "time": '2021-08-03',
        "data": [
            {"name": "杭州市", "value": [3469.0]},
            {"name": "湖州市", "value": [2998.0, 8.75]},
            {"name": "衢州市", "value": [2770.0, 8.08]},
            {"name": "嘉兴市", "value": [2011.0, 5.87]},
            {"name": "宁波市", "value": [1926.0, 5.62]},
            {"name": "绍兴市", "value": [1691.0, 4.93]},
            {"name": "台州市", "value": [1660.0, 4.84]},
            {"name": "温州市", "value": [1519.0, 4.43]},
            {"name": "丽水市", "value": [1486.0, 4.34]},
            {"name": "金华市", "value": [1326.0, 3.87]},
            {"name": "舟山市", "value": [1245.0, 3.63]},
        ],
    },
    {
        "time": '2021-08-04',
        "data": [
            {"name": "杭州市", "value": [346.0, 10.12]},
            {"name": "湖州市", "value": [299.0, 8.75]},
            {"name": "衢州市", "value": [277.0, 8.08]},
            {"name": "嘉兴市", "value": [201.0, 5.87]},
            {"name": "宁波市", "value": [192.0, 5.62]},
            {"name": "绍兴市", "value": [169.0, 4.93]},
            {"name": "台州市", "value": [166.0, 4.84]},
            {"name": "温州市", "value": [151.0, 4.43]},
            {"name": "丽水市", "value": [148.0, 4.34]},
            {"name": "金华市", "value": [132.0, 3.87]},
            {"name": "舟山市", "value": [124.0, 3.63]},
        ],
    },
    {
        "time": '2021-08-05',
        "data": [
            {"name": "杭州市", "value": [34.0, 10.12]},
            {"name": "湖州市", "value": [29.0, 8.75]},
            {"name": "衢州市", "value": [27.0, 8.08]},
            {"name": "嘉兴市", "value": [20.0, 5.87]},
            {"name": "宁波市", "value": [19.0, 5.62]},
            {"name": "绍兴市", "value": [16.0, 4.93]},
            {"name": "台州市", "value": [16.0, 4.84]},
            {"name": "温州市", "value": [15.0, 4.43]},
            {"name": "丽水市", "value": [14.0, 4.34]},
            {"name": "金华市", "value": [13.0, 3.87]},
            {"name": "舟山市", "value": [12.0, 3.63]},
        ],
    },

]
#print(data[0])
#print(data[0].keys())
#print(data[0].values())


total_num = [
    3.4,
    4.5,
    5.8,
    6.8,
    7.6,
    8.3,
    8.8,
    9.9,
    10.9,
    12.1,
    14,
    16.8,
    19.9,
    23.3,
    28,
    33.3,
    36.5,
    43.7,
    52.1,
    57.7,
    63.4,
    68.4,
    72.3,
    78,
    84.7,
    91.5,
]
maxNum = 97300
minNum = 30


def get_day_chart(day: str):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == day
    ][0]
    #print(map_data)
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == day:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            maptype="浙江",
            zoom=1,
            # center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(day) + "全国分地区GPD情况（单位：亿） 数据来源：国家统计局",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    # line_chart = (
    #     Line()
    #         .add_xaxis(time_list)
    #         .add_yaxis("", total_num)
    #         .add_yaxis(
    #         "",
    #         data_mark,
    #         markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
    #     )
    #         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="全国GDP总量1993-2018年（单位：万亿）", pos_left="72%", pos_top="5%"
    #         )
    #     )
    # )
    print(map_data)
    bar_x_data = [x[0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    pie_data = [[x[0], x[1][0]] for x in map_data]
    #print(pie_data)
    pie = (
        Pie()
            .add(
            series_name="",
            data_pair=list1,
            radius=["15%", "35%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
            #     .add(
            #     line_chart,
            #     grid_opts=opts.GridOpts(
            #         pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            #     ),
            # )
            .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == "__main__":
    timeline = Timeline(
        init_opts=opts.InitOpts(width="1600px", height="900px", theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_day_chart(day=y)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )

    timeline.render("浙江话题活跃情况.html")
