import pandas as pd

# 1、读取数据
df = pd.read_excel('d:/WJ/数据准备/登录日志.xlsx')

# 2.时间截取为日期
# object处理方式
# df['CREATE_TIME'] = str(df['CREATE_TIME']).str.split(' ').str[0]

# datetime64[ns]处理方式，截取后变成object格式
df['CREATE_TIME'] = pd.DatetimeIndex(df['CREATE_TIME']).date
# 转化为时间格式,否则分组排序会报数据格式错误
df["CREATE_TIME"] = pd.to_datetime(df["CREATE_TIME"])

# SELECT phone_number,TRUNC(create_time) CREATE_TIME
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#  order by CREATE_TIME;

# 3、删除重复记录，每天每个号码保留一条记录
df.drop_duplicates(inplace=True)
# SELECT phone_number,TRUNC(create_time) CREATE_TIME
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME;

# 4、分组排序，得到一个辅助列，当前记录时间
df['RANK'] = df['CREATE_TIME'].groupby(df['PHONE_NUMBER']).rank()
# SELECT phone_number,TRUNC(create_time) CREATE_TIME,
# rank() over (partition by phone_number order by phone_number,TRUNC(create_time)) rank
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME;
print(df)
# 5、计算差值，这一步是辅助操作，使用第三步中的RANK列与用户登录日期做差值得到一个日期date_sub，若某用户某几列该值相同，则代表这几天属于连续登录
# 因为RANK列是float型，我们在做时间差的时候需要用到to_timedelta且unit='d'用来表示减去的是天数，这样获得的差值就会是一个日期
df['date_sub'] = df['CREATE_TIME'] - pd.to_timedelta(df['RANK'], unit='d')
# select phone_number,CREATE_TIME,rank,CREATE_TIME-RANK date_sub
# from (
# SELECT phone_number,TRUNC(create_time) CREATE_TIME,
# rank() over (partition by phone_number order by phone_number,TRUNC(create_time)) rank
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME);

# 6、计算每个用户date_sub列出现的次数即可算出该用户连续登录的天数
data = df.groupby(['PHONE_NUMBER', 'date_sub']).count().reset_index()
# select phone_number,date_sub,count(date_sub) value from
# (select phone_number,CREATE_TIME,rank,CREATE_TIME-rank date_sub
# from (
# SELECT phone_number,TRUNC(create_time) CREATE_TIME,
# rank() over (partition by phone_number order by phone_number,TRUNC(create_time)) rank
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME)
#  )group by phone_number,date_sub;

# 修改rank列名
data = data[['PHONE_NUMBER', 'date_sub', 'RANK']].rename(columns={'RANK': '连续登录天数'})

# 7、计算每个用户连续登录的最大天数
data = data.sort_values(by='连续登录天数', ascending=False).groupby('PHONE_NUMBER').first().reset_index()
# select phone_number,max(value) from (
# select phone_number,date_sub,count(date_sub) value from
# (select phone_number,CREATE_TIME,rank,CREATE_TIME-rank date_sub
# from (
# SELECT phone_number,TRUNC(create_time) CREATE_TIME,
# rank() over (partition by phone_number order by phone_number,TRUNC(create_time)) rank
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME)
#  )group by phone_number,date_sub) group by phone_number;
print(data)
data.to_excel('d:/WJ/数据准备/连续登录.xlsx')

# 最大未登录天数
# select phone_number,min(date_sub) from
# (select phone_number,CREATE_TIME,rank,rank-CREATE_TIME date_sub
# from (
# SELECT phone_number,TRUNC(create_time) CREATE_TIME,
# trunc(to_date('2021-12-01','yyyy-mm-dd')) rank
# FROM User_active_time_report f
# WHERE f.CREATE_TIME >= to_date('2021-10-01', 'yyyy-mm-dd')
#    AND f.CREATE_TIME < to_date('2021-12-01', 'yyyy-mm-dd') + 1
#    group by phone_number,TRUNC(create_time)
#  order by phone_number,CREATE_TIME)
#  ) group by phone_number;
