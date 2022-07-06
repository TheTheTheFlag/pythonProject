import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn import preprocessing

# 导入数据
df = pd.read_excel('d:/WJ/机器学习输入/故障发布上线次日数据清单.xlsx')
df1 = pd.read_excel('d:/WJ/机器学习输入/故障发布上线次日数据清单.xlsx')
# 选取数值列
data = df.iloc[:, 5:10]
print(data)
df_model = df.iloc[:, 5:10]
##############反向指标修复
data.iloc[:, 0:1] = -data.iloc[:, 0:1]
df_model.iloc[:, 0:1] = -df_model.iloc[:, 0:1]

# 标准化处理
maxium = np.max(data, axis=0)  # 每列最大值
minium = np.min(data, axis=0)  # 每列最小值
# print(maxium['访问频率'])
# print(minium['访问频率'])
# print(data.iloc[:, 1:2])
data = (data - minium) * 1.0 / (maxium - minium)  # 数据标准化处理
print("标准化处理后数据：\n", data)
mms = MinMaxScaler()
data1 = mms.fit_transform(df_model)
# Fit() #求得训练集X的均值啊，方差啊，最大值啊，最小值啊这些训练集X固有的属性
# Transform() #在Fit的基础上，进行标准化，降维，归一化等操作（看具体用的是哪个工具，如PCA，StandardScaler等
# Fit_transform() #transform()和fit_transform()二者的功能都是对数据进行某种统一处理（比如标准化~N(0,1)，将数据缩放(映射)到某个固定区间，归一化，正则化等）
# fit_transform(trainData)对部分数据先拟合fit，找到该part的整体指标，如均值、方差、最大值最小值等等（根据具体转换的目的），然后对该trainData进行转换transform，从而实现数据的标准化、归一化等等
print("Fit_transform+MinMaxScaler标准化处理后数据：\n", data1)




# PCA函数
pca = PCA(n_components=3)
pca.fit(data1)
pca.components_  # 模型的各个特征向量 也叫成分矩阵
pca.explained_variance_  # 贡献方差，即特征根
pca.explained_variance_ratio_  # 各个成分各自的方差百分比（贡献率）

# 计算相关统计量
R = data.corr()
R.to_excel("d:/WJ/机器学习输入/故障相关矩阵.xls")
cf = np.cov(np.transpose(data))  # 计算协方差矩阵
c, d = np.linalg.eig(cf)  # 特征值和特征向量
x = c / np.sum(c)  # 各主成分贡献率，即权重

print('相关系数矩阵为:\n', R)
print("协方差矩阵", cf)
print("特征值（贡献方差、特征根）:\n", np.transpose(c))
print("PCA特征值（贡献方差、特征根）:\n", pca.explained_variance_)
print("特征向量:\n", d)
print("PCA特征向量:\n", pca.components_)
print("方差百分比（贡献率）:\n", np.transpose(x))
print("PCA方差百分比（贡献率）:\n", pca.explained_variance_ratio_)

# # 绘制碎石图确定维度
# def nd_confirm(data):
#     x = [i + 1 for i in range(len(data.columns))]
#     plt.plot(x, np.transpose(c)) #,特征值
#     plt.title("pic")
#     plt.xlabel('num')
#     plt.ylabel('characteristic value')
#     plt.grid()
#     plt.show()
#
#
# nd_confirm(data)


# k1_spss = pca.components_ / np.sqrt(pca.explained_variance_.reshape(-1, 1))  # 成分得分系数矩阵
# pca.components_ 行是成分，列是特征，这里进行转置，方便后边计算
print('pca:',pca.components_, pca.components_.shape)  # 成分矩阵,sklearn已经除过pca.explained_variance_，不需要再次处理
k1_spss = pca.components_.T
print(k1_spss)
# 确定权重
# 求指标在不同主成分线性组合中的系数
weight = (np.dot(k1_spss, pca.explained_variance_ratio_)) / np.sum(pca.explained_variance_ratio_)
print('weight:',weight)
#
weighted_weight = weight/np.sum(weight)
print('weighted_weight:', weighted_weight)


df['factor_score'] = (-1.1235082*df['需求均数']+(0.06630988)*df['次日故障数']+(0.05719831)*df['次日G5故障数']+(0.05719831)*df['次日上线相关故障数']+(0.05719831)*df['次日连续性故障数'])
df = df.sort_values(by='factor_score', ascending=False).reset_index(drop=True)
df['rank'] = df.index + 1
print(df)
df.to_excel("d:/WJ/机器学习输入/主成分分析法PCA-故障.xls")
