import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 画图中的显示中文
from sklearn.preprocessing import MinMaxScaler

mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False
from factor_analyzer import FactorAnalyzer

data = pd.read_excel('d:/WJ/机器学习输入/REF2.xls')
# 去掉前两列索引变量
df_model = data.iloc[:,7:]
df_model.iloc[:, 0:1] = -df_model.iloc[:, 0:1]

# 归一化处理(x-μ)/std
df_model = df_model.apply(lambda x: (x - x.mean()) / x.std())

# mms = MinMaxScaler()
# df_model = mms.fit_transform(df_model)
# print(df_model)

# 充分性检测
print('巴特利球形度检验')
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value, p_value = calculate_bartlett_sphericity(df_model)
print('卡方值：', chi_square_value, 'P值', p_value)

# 相关性检验kmo要大于0.6
from factor_analyzer.factor_analyzer import calculate_kmo

kmo_all, kmo_model = calculate_kmo(df_model)
print('KMO检验：', kmo_model)
# 查看相关矩阵特征值
fa = FactorAnalyzer(3, rotation='varimax', method='principal', impute='mean')  # 旋转：方差最大法
fa.fit(df_model)
ev, v = fa.get_eigenvalues()
#########################################################################
cf = np.cov(np.transpose(df_model))  # 计算协方差矩阵

ev, v = np.linalg.eig(cf)  # 特征值和特征向量
print('协方差矩阵：', cf)

print('相关矩阵特征值：', ev)
# Create scree plot using matplotlib
plt.figure(figsize=(8, 6.5))
plt.scatter(range(1, df_model.shape[1] + 1), ev)
plt.plot(range(1, df_model.shape[1] + 1), ev)
plt.title('碎石图', fontdict={'weight': 'normal', 'size': 25})
plt.xlabel('因子', fontdict={'weight': 'normal', 'size': 15})
plt.ylabel('特征值', fontdict={'weight': 'normal', 'size': 15})
plt.grid()
# plt.savefig('E:/suishitu.jpg')
plt.show()

# 确定因子个数
#n_factors = sum(ev > 1)
n_factors = 3
# 取旋转后的结果
fa2 = FactorAnalyzer(n_factors, rotation='varimax', method='principal')
fa2.fit(df_model)
# 给出贡献率
var = fa2.get_factor_variance()

# 计算因子得分
fa2_score = fa2.transform(df_model)

# 得分表
column_list = ['fac' + str(i) for i in np.arange(n_factors) + 1]
fa_score = pd.DataFrame(fa2_score, columns=column_list)
for col in fa_score.columns:
    data[col] = fa_score[col]
print("\n各因子得分:\n", fa_score)

# 方差贡献表
df_fv = pd.DataFrame()
df_fv['因子'] = column_list
df_fv['方差贡献'] = var[1]
df_fv['累计方差贡献'] = var[2]
df_fv['累计方差贡献占比'] = var[1] / var[1].sum()
print("\n方差贡献表:\n", df_fv)
data['factor_score'] = ((var[1] / var[1].sum()) * fa2_score).sum(axis=1)
data = data.sort_values(by='factor_score', ascending=False).reset_index(drop=True)
data['rank'] = data.index + 1
print(data)
