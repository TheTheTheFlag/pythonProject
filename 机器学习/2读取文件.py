import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hashlib

from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

# def load_housing_data(housing_path=HOUSING_PATH):
#     csv_path = os.path.join(housing_path, "housing.csv")
#     return pd.read_csv(csv_path)

#  经度、维度、房屋年龄中位数、总房间数、卧室数量、人口数、家庭数、收入中位数、房屋价值中位数、大海距离
housing = pd.read_csv('d:/WJ/机器学习输入/housing.csv')
# #  快速查看数据结构
# print(housing.head())
# print(housing.info())
# print(housing["ocean_proximity"].value_counts())
# print(housing.describe())
#
# housing.hist(bins=50, figsize=(20, 15))
# plt.show()
# #  创建测试集
# 随机抽样
# train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
# print(train_set.head())
# print(test_set.head())

#  分层抽样 分层采样测试集的收入分类比例与总数据集几乎相同，而随机采样数据集偏差严重
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
print(housing["income_cat"].value_counts() / len(housing))

#  删除income_cat属性，使数据回到初始状态
for set in (strat_train_set, strat_test_set):
    set.drop(["income_cat"], axis=1, inplace=True)

# #  数据探索和可视化、发现规律,数据集很小,直接创建一个副本，以免损伤训练集
housing = strat_train_set.copy()
# #  地理数据可视化
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
             s=housing["population"] / 100, label="population",
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
             )
plt.legend()
# #  查找关联，数据集并不是非常大，你可以很容易地使用corr()方法计算出每对属性间的标准相关系数（也称作皮尔逊相关系数）
# 相关系数的范围是-1到1。当接近1时，意味强正相关；例如，当收入中位数增加时，房价中位数也会增加。当相关系数接近-1时，意味强负相关；你可以看到，纬度和房价中位数有轻微的负相关性（即，越往北，房价越可能降低）。最后，相关系数接近0，意味没有线性相关性
corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))

# 另一种检测属性间相关系数的方法是使用Pandas的scatter_matrix函数，它能画出每个数值属性对每个其它数值属性的图。

attributes = ["median_house_value", "median_income", "total_rooms",
              "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))

# 最有希望用来预测房价中位数的属性是收入中位数，因此将这张图放大
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)

# #  属性组合试验
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]
corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))

# #  为机器学习算法准备数据
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()