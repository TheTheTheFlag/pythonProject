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

corr_matrix = housing.corr()

print(corr_matrix["median_house_value"].sort_values(ascending=False))
