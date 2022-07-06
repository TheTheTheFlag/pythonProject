# 导入python所需要的库及函数包
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import math as math
from numpy import *
import numpy.linalg as nlg
from factor_analyzer import factor_analyzer, Rotator
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity

# 0读取数据
df = pd.read_excel('d:/WJ/机器学习输入/REF2.xls')
wj = df.copy()
data = df.iloc[:, 7:]
data.iloc[:, 0:1] = -data.iloc[:, 0:1]
# 数据预处理 ,去除空值的记录:
data.dropna()
# 数据以非科学计数法展示
np.set_printoptions(suppress=True)

# 1标准差标准化
# 直接调用sklearn库进行数据标准化
std = StandardScaler()
std = MinMaxScaler()
data_zs = std.fit_transform(data)
print(data_zs)

# 2充分性检测(Adequacy Test)
# KMO值：0.9以上非常好；0.8以上好；0.7一般；0.6差；0.5很差；0.5以下不能接受
# Bartlett’s test of sphericity 是用来检测观察到的变量之间是否关联, 如果检测结果在统计学上不显著, 就不能采用因子分析，巴特利球形检验的值范围在0-1，越接近1，使用因子分析效果越好
# kmo值要大于0.7
kmo = calculate_kmo(data)
# bartlett球形度检验p值要小于0.05
bartlett = calculate_bartlett_sphericity(data)
print("\n因子分析适用性检验:")
print('kmo:{},bartlett:{}'.format(kmo[1], bartlett[1]))
chi_square_value, p_value = calculate_bartlett_sphericity(data)
print('卡方值：', chi_square_value, 'P值', p_value)
# 3相关系数矩阵（协方差矩阵）
# 皮尔森相关系数
data_corr = data.corr()
print("\n相关系数:\n", data_corr)
# 获得协方差矩阵，cov是numpy库中计算协方差的函数，获得协方差矩阵9*9
# 注：标准化后的矩阵的协方差矩阵 即为 原始数据的相关系数矩阵
data_zs_cov = np.cov(data_zs.T)
# data_zs_cov = np.cov(data_zs)

print("\n协方差矩阵：\n", data_zs_cov)

# 4特征值&特征向量
# 求解特征值以及特征向量，直接调用求特征值和特征向量的函数
e, ev = nlg.eig(data_zs_cov)
# 查看特征值
eig = pd.DataFrame()
eig['names'] = data.columns
eig['e'] = e
eig.sort_values('e', ascending=False, inplace=True)
print("\n特征值\n：", eig)
# 查看特征向量，一行为一个特征向量
eig1 = pd.DataFrame(ev)
eig1.columns = data.columns
eig1.index = data.columns
print("\n特征向量\n", eig1)

# 5主成分个数（因子个数），方差，贡献率，累计贡献率
# 计算各特征值的方差贡献率
w = list()
for i in range(len(e)):
    w.append(eig['e'][i] / eig['e'].sum())
print(w)
# 计算特征值的累计贡献率
q = list()
for j in range(len(e)):
    q.append(eig['e'][:j].sum() / eig['e'].sum())
print(q)
# 求公因子个数m,使用前m个特征值的比重大于80%的标准，选出了公共因子,根据累计贡献率得出
for m in range(len(e)):
    print(eig['e'][:m].sum())
    print(eig['e'].sum())
    print(eig['e'][:m].sum() / eig['e'].sum())
    if eig['e'][:m].sum() / eig['e'].sum() >= 0.8:
        print("\n主成分个数:", m)
        break
# 6因子分析
# 主成分个数为m个,提取方法为主成分提取方法,旋转方法为最大方差法
m = 3
fa = FactorAnalyzer(n_factors=m, method='principal', rotation='varimax')
fa.fit(data)
# 因子载荷矩阵(成分矩阵)
pd.DataFrame(fa.loadings_)
# 给出贡献率,第一行表示特征值方差，第二行表示贡献率，第三行表示累计贡献率
# 该过程与上述求方差贡献率结果一致
var = fa.get_factor_variance()
for i in range(0, 3):
    print(var[i])
# 公因子方差 ， 特殊因子方差，因子的方差贡献度 ，反映公共因子对所有变量的贡献
fa.get_communalities()

# 7因子得分
# 计算各个企业的因子得分
fa_t_score = np.dot(np.mat(data_zs), np.mat(fa.loadings_))
print("\n每个企业的因子得分：\n",pd.DataFrame(fa_t_score))

# 8综合得分(加权计算）
weight = var[1]     #计算每个因子的权重
fa_t_score_final = (np.dot(fa_t_score, weight) / e.sum()).real
print(fa_t_score_final)

