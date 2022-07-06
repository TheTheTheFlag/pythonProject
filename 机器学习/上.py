import pandas as pd

housing = pd.read_csv("D:\pythonProject\机器学习\housing.csv")
# housing.info() #查看数据结构
# housing.head() #查看前5行数据
# housing['ocean_proximity'].value_counts() #统计ocean_proximity的类型分布
# housing.describe() #查看数据分布及详情
import matplotlib.pyplot as plt
# housing.hist(bins=50, figsize=(20,15))
# plt.show()#可视化

##创建训练集
import hashlib
import numpy as np


def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing_with_id = housing.reset_index()  # adds an `index` column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

housing["income_cat"].value_counts() / len(housing)

##恢复数据
for set in (strat_train_set, strat_test_set):
    set.drop(["income_cat"], axis=1, inplace=True)

##复制训练集数据
housing = strat_train_set.copy()

##查看数据分布图
# housing.plot(kind='scatter',x='longitude',y='latitude',alpha=0.1)
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
             s=housing["population"] / 100, label="population",
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
             )
# plt.legend()

##使用corr函数查看关联度，数据量少时可使用
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

##查看分布图
from pandas.plotting import scatter_matrix

attributes = ["median_house_value", "median_income", "total_rooms",
              "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))

##具体查看主要关联数据图像
housing.plot(kind='scatter', x='median_income', y='median_house_value', alpha=0.1)

##使用现有字段推测其他字段
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]

##再次查看关联度
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

##还原数据
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()