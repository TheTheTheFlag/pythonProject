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

from sklearn.model_selection import train_test_split, GridSearchCV

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
# housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
#              s=housing["population"] / 100, label="population",
#              c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
#              )
# plt.legend()

##使用corr函数查看关联度，数据量少时可使用
corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)

##查看分布图
from pandas.plotting import scatter_matrix

# attributes = ["median_house_value", "median_income", "total_rooms",
#               "housing_median_age"]
# scatter_matrix(housing[attributes], figsize=(12, 8))

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
##############################下###############################
##数据清洗
# total_bedrooms有一些缺失值。有三个解决选项
# housing.dropna(subset=["total_bedrooms"])    # 选项1删除total_bedrooms列空白值的行
# housing.drop("total_bedrooms", axis=1)       # 选项2删除total_bedrooms列
# median = housing["total_bedrooms"].median()
# housing["total_bedrooms"].fillna(median)     # 选项3进行赋值（0、平均值、中位数等等），这里选择平均值
# 创建一个imputer实例，使用该属性的中位值替换缺失值
from sklearn.impute import SimpleImputer as Imputer

imputer = Imputer(strategy="median")
# 只有数值类型数据可以计算中位数，所以要取出一份只有数值类型字段的数据，即删除ocean_proximity字段数据
housing_num = housing.drop("ocean_proximity", axis=1)  # drop下axis=1时含义为按列删除，其他时候为按行选择
# 用fit()方法将imputer实例拟合到训练数据
imputer.fit(housing_num)
# imputer.statistics_  # 统计
# housing_num.median().values
# 使用这个“训练过的”imputer来对训练集进行转换，通过将缺失值替换为中位数
X = imputer.transform(housing_num)
# 将转换后数据放回到Pandas DataFrame中
housing_tr = pd.DataFrame(X, columns=housing_num.columns)
# housing_tr
##处理文本和分类属性
# 前面，我们丢弃了分类属性ocean_proximity，因为它是一个文本属性，不能计算出中位数。大多数机器学习算法更喜欢和数字打交道，所以让我们把这些文本标签转换为数字
from sklearn.preprocessing import LabelEncoder, StandardScaler

encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
# housing_cat_encoded

##Scikit-Learn提供了一个编码器OneHotEncoder，用于将整书分类值转变为独热矢量。注意fit_transform()用于2D数组，而housing_cat_encoded是一个1D数组，所以需要将其变形
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1, 1))
# housing_cat_1hot
# toarray()方法可以SciPy稀疏矩阵转化为NumPy密集数组
housing_cat_1hot.toarray()

##使用类LabelBinarizer，我们可以用一步执行这两个转换（从文本分类到整数分类，再从整数分类到独热矢量）
##默认返回的结果是一个密集NumPy数组。向构造器LabelBinarizer传递sparse_output=True，就可以得到一个稀疏矩阵
from sklearn.preprocessing import LabelBinarizer

# encoder = LabelBinarizer(sparse_output=True)
encoder = LabelBinarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)
# housing_cat_1hot

##自定义转换量
# 据准备步骤越自动化，可以自动化的操作组合就越多，越容易发现更好用的组合（并能节省大量时间）
from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
                         bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)
# housing_extra_attribs

##特征缩放
# 有两种常见的方法可以让所有的属性有相同的量度：线性函数归一化（Min-Max scaling）和标准化（standardization）

##转换Pipeline
# 你已经看到，存在许多数据转换步骤，需要按一定的顺序执行。幸运的是，Scikit-Learn提供了类Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([
    ('imputer', Imputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

housing_num_tr = num_pipeline.fit_transform(housing_num)

# 一个完整的处理数值和分类属性的pipeline
from sklearn.pipeline import FeatureUnion, Pipeline

# 打个小补丁,解决报错fit_transform() takes 2 positional arguments but 3 were given
LabelBinarizer.__fit_transform = LabelBinarizer.fit_transform
LabelBinarizer.fit_transform = lambda self, X, y=None, **fit_params: LabelBinarizer.__fit_transform(self, X)


# 每个子pipeline都以一个选择转换量开始：通过选择对应的属性（数值或分类）、丢弃其它的，来转换数据，并将输出DataFrame转变成一个NumPy数组。Scikit-Learn没有工具来处理Pandas DataFrame，因此我们需要写一个简单的自定义转换量来做这项工作
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([
    ('selector', DataFrameSelector(num_attribs)),
    ('imputer', Imputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attribs)),
    ('label_binarizer', LabelBinarizer()),
])

full_pipeline = FeatureUnion(transformer_list=[
    ("num_pipeline", num_pipeline),
    ("cat_pipeline", cat_pipeline),
])

from sklearn.base import BaseEstimator, TransformerMixin

housing_prepared = full_pipeline.fit_transform(housing)
# housing_prepared
print(housing_prepared.shape)

##在训练集上训练和评估
# 一个线性回归模型
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)
print(lin_reg)

# 有了一个可用的线性回归模型。用一些训练集中的实例做下验证
some_data = housing.iloc[:5]
some_labels = housing_labels.iloc[:5]
some_data_prepared = full_pipeline.transform(some_data)
print("Predictions:\t", lin_reg.predict(some_data_prepared))
print("Labels:\t\t", list(some_labels))

##使用Scikit-Learn的mean_squared_error函数，用全部训练集来计算下这个回归模型的RMSE
from sklearn.metrics import mean_squared_error

housing_predictions = lin_reg.predict(housing_prepared)
lin_mse = mean_squared_error(housing_labels, housing_predictions)
lin_rmse = np.sqrt(lin_mse)
print("回归模型的RMSE: ", lin_rmse)
# 68628.413493824875

##来训练一个DecisionTreeRegressor。这是一个强大的模型，可以发现数据中复杂的非线性关系
from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_labels)
# 训练集评估
housing_predictions = tree_reg.predict(housing_prepared)
tree_mse = mean_squared_error(housing_labels, housing_predictions)
tree_rmse = np.sqrt(tree_mse)
print("DecisionTreeRegressor模型的RMSE: ", tree_rmse)
# 0.0
# 严重过拟合数据

##使用交叉验证做更佳的评估
# 使用Scikit-Learn的交叉验证功能。下面的代码采用了K折交叉验证（K-fold cross-validation）：它随机地将训练集分成十个不同的子集，成为“折”，然后训练评估决策树模型10次，每次选一个不用的折来做评估，用其它9个来做训练。结果是一个包含10个评分的数组
from sklearn.model_selection import cross_val_score

scores = cross_val_score(tree_reg, housing_prepared, housing_labels,
                         scoring="neg_mean_squared_error", cv=10)
# Scikit-Learn交叉验证功能期望的是效用函数（越大越好）而不是成本函数（越低越好），因此得分函数实际上与MSE相反（即负值），这就是为什么代码在计算平方根之前先计算-scores
rmse_scores = np.sqrt(-scores)


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("K折交叉验证-Standard deviation:", scores.std())


print(display_scores(rmse_scores))
# 注意到交叉验证不仅可以让你得到模型性能的评估，还能测量评估的准确性（即，它的标准差）。决策树的评分大约是71200，通常波动有±3200

# 计算下线性回归模型的的相同分数，以做确保
lin_scores = cross_val_score(lin_reg, housing_prepared, housing_labels,
                             scoring="neg_mean_squared_error", cv=10)

lin_rmse_scores = np.sqrt(-lin_scores)
print(display_scores(lin_rmse_scores))
# 决策树模型过拟合很严重

##现在再尝试最后一个模型：RandomForestRegressor。第7章我们会看到，随机森林是通过用特征的随机子集训练许多决策树。在其它多个模型之上建立模型成为集成学习(Ensemble Learning)，它是推进ML算法的一种好方法
from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor()
forest_reg.fit(housing_prepared, housing_labels)
[...]
print(rmse_scores)
print("RandomForestRegressor模型的RMSE: ", display_scores(rmse_scores))

# 用Python的模块pickle，非常方便地保存Scikit-Learn模型，或使用sklearn.externals.joblib，后者序列化大NumPy数组更有效率
# import joblib
#
# joblib.dump(my_model, "my_model.pkl")
# # 然后
# my_model_loaded = joblib.load("my_model.pkl")


# 模型微调你应该使用Scikit-Learn的GridSearchCV来做这项搜索工作。你所需要做的是告诉GridSearchCV要试验有哪些超参数，要试验什么值，GridSearchCV就能用交叉验证试验所有可能超参数值的组合。例如，下面的代码搜索了RandomForestRegressor超参数值的最佳组合
param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]

forest_reg = RandomForestRegressor()

grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error')

grid_search.fit(housing_prepared, housing_labels)
# 参数的最佳组合
print(grid_search.best_params_)
# 最佳的估计量
print(grid_search.best_estimator_)

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
    print(np.sqrt(-mean_score), params)
# 在这个例子中，我们通过设定超参数max_features为6，n_estimators为30，得到了最佳方案。对这个组合，RMSE的值是49959，这比之前使用默认的超参数的值（52634）要稍微好一些。祝贺你，你成功地微调了最佳模型


##分析最佳模型和它们的误差
# 通过分析最佳模型，常常可以获得对问题更深的了解。比如，RandomForestRegressor可以指出每个属性对于做出准确预测的相对重要性
feature_importances = grid_search.best_estimator_.feature_importances_
print("每个属性对于做出准确预测的相对重要性: ", feature_importances)
# 将重要性分数和属性名放到一起
extra_attribs = ["rooms_per_hhold", "pop_per_hhold", "bedrooms_per_room"]
cat_one_hot_attribs = list(encoder.classes_)
attributes = num_attribs + extra_attribs + cat_one_hot_attribs
sorted(zip(feature_importances, attributes), reverse=True)
# 有了这个信息，你就可以丢弃一些不那么重要的特征（比如，显然只要一个分类ocean_proximity就够了，所以可以丢弃掉其它的

# 用测试集评估系统
# 调节完系统之后，你终于有了一个性能足够好的系统。现在就可以用测试集评估最后的模型了。这个过程没有什么特殊的：从测试集得到预测值和标签，运行full_pipeline转换数据（调用transform()，而不是fit_transform()！），再用测试集评估最终模型
final_model = grid_search.best_estimator_

X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"].copy()

X_test_prepared = full_pipeline.transform(X_test)

final_predictions = final_model.predict(X_test_prepared)

final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = np.sqrt(final_mse)  # => evaluates to 48,209.6
print("最终模型: ", final_rmse)
# 评估结果通常要比交叉验证的效果差一点，如果你之前做过很多超参数微调（因为你的系统在验证集上微调，得到了不错的性能，通常不会在未知的数据集上有同样好的效果）。这个例子不属于这种情况，但是当发生这种情况时，你一定要忍住不要调节超参数，使测试集的效果变好；这样的提升不能推广到新数据上。
