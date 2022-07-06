import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
from numpy import random
from pandas.core import frame

df = pd.read_excel('d:/WJ/SR/kol2.xlsx')
df_all = df[['业务类别', '话题标题', '话题描述', '状态', '归属地市', '创建人', '组织']].applymap(lambda x: str(x).strip())
df_count_All = df_all.groupby('创建人')['话题标题'].count()
print(df_count_All.index)
df_all_2 = df_all[df_all.创建人 == '李东海']
print(df_all_2[['业务类别', '话题标题', '话题描述']])
df_all_1 = df_all_2[['业务类别', '话题标题', '话题描述']]
list1 = [[df_all_1['业务类别'], df_all_1['话题标题'], df_all_1['话题描述']]]

# print(list1)

# file = open('D:/WJ/SC/黄珊珊.txt', 'w')
# file.write(str(list1))
# file.close()

writer = pd.ExcelWriter('d:/WJ/SC/ext.xlsx')
df_all_1.to_excel(writer, 'Sheet1')
writer.save()
# 读取excel保存成txt格式
excel_file = pd.read_excel('d:/WJ/SC/ext.xlsx')
excel_file.to_csv('D:/WJ/SC/李东海.txt', sep='\t', index=False)
