import pandas as pd

df = pd.read_excel('d:/WJ/数据准备/登录日志2.xlsx')
df['天数'] = df["ACTIVE_TIME"] - df["CREATE_TIME"]

# 使用透视表，计算创角日期对应用户第x天登录的数量（非重复计数）
# Values可以对需要的计算数据进行筛选
# pivot_table必须拥有一个index，即设置索引
# columns类似Index可以设置列层次字段，它不是一个必要参数，作为一种分割数据的可选方式
# aggfunc参数可以设置我们对数据聚合时进行的函数操作。
data = pd.pivot_table(df, values='PHONE_NUMBER', index='CREATE_TIME', columns='天数',
                      aggfunc=lambda x: len(x.unique()),
                      #aggfunc=lambda x: x.value_counts().count(),
                      #aggfunc=lambda x: len(x.dropna().unique()),
                      fill_value=0).reset_index()
print(data.head())
# data.to_excel('d:/WJ/数据准备/lcl.xlsx')

# 将单元格改为数值格式，用于后续计算留存比例
data = data.applymap(lambda x: pd.to_numeric(x, errors='ignore'))

# 留存率计算
# 用 1 days 列 除以  0 days为次日留存率，依次类推
# 我们用for循环语句可以实现该算法
create_index = data.columns
df = data.iloc[:, [0, 1]]
for i in range(2, 8):  # 这里我们只算到7日留存率
    s = data[create_index[i]]*100 / data[create_index[1]]  # 1 days 列 除以  0 days为次日留存率，依次类推
    print(s)
    print(data[create_index[i]])
    df = pd.concat([df, s], axis=1)

df.columns = ['创角日期', '注册玩家数', '次日留存率', '3日留存率', '4日留存率', '5日留存率', '6日留存率', '七日留存率']
# df = df.fillna(0)  # 空值置0
print(df.head())


# --登录日期间隔表
# CREATE OR REPLACE VIEW sjjg as
# select a.phone_number, b.create_time, a.active_time,ROUND(TO_NUMBER(a.active_time - b.create_time))  diff
#   from (select phone_number,TRUNC(create_time) active_time
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1) a
#   left join (select phone_number,min(TRUNC(create_time)) create_time
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1 group by phone_number) b
#     on a.phone_number = b.phone_number
#  order by a.phone_number,b.create_time,a.active_time;
# --留存率
# SELECT s.create_time 日期,count(DISTINCT s.phone_number) 人数,
# count(DISTINCT CASE WHEN s.diff=1 THEN s.phone_number ELSE NULL END ) 次日留存,
# to_char(count(DISTINCT CASE WHEN s.diff=1 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 次日留存率,
# count(DISTINCT CASE WHEN s.diff=3 THEN s.phone_number ELSE NULL END ) 日3留存,
# to_char(count(DISTINCT CASE WHEN s.diff=3 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 日3留存率,
# count(DISTINCT CASE WHEN s.diff=7 THEN s.phone_number ELSE NULL END ) 日7留存,
# to_char(count(DISTINCT CASE WHEN s.diff=7 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 日7留存率,
# count(DISTINCT CASE WHEN s.diff=30 THEN s.phone_number ELSE NULL END ) 日30留存,
# to_char(count(DISTINCT CASE WHEN s.diff=30 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 日30留存率,
# count(DISTINCT CASE WHEN s.diff=60 THEN s.phone_number ELSE NULL END ) 日60留存,
# to_char(count(DISTINCT CASE WHEN s.diff=60 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 日60留存率,
# count(DISTINCT CASE WHEN s.diff=90 THEN s.phone_number ELSE NULL END ) 日90留存,
# to_char(count(DISTINCT CASE WHEN s.diff=90 THEN s.phone_number ELSE NULL END ) /count(DISTINCT s.phone_number)* 100, 'fm99990.0') 日90留存率
# FROM sjjg s
# GROUP BY s.create_time;