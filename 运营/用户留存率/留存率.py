# 建立留存函数(里面默认data数据中有day/user_id两个字段数据，day为日期、user_id为用户id)

# 导入数据包
import pandas as pd
import numpy as np
from datetime import timedelta


# 建立n日留存率计算函数
def cal_retention(data, n):  # n为n日留存
    user = []
    date = pd.Series(data.day.unique()).sort_values()[:-n]  # 时间截取至最后一天的前n天
    retention_rates = []
    for i in date:
        new_user = set(data[data.day == i].user_id.unique()) - set(user)  # 识别新用户，本案例中设初始用户量为零
        user.extend(new_user)  # 将新用户加入用户群中
        # 第n天留存情况
        user_nday = data[data.day == i + timedelta(n)].user_id.unique()  # 第n天登录的用户情况
        a = 0
        for user_id in user_nday:
            if user_id in new_user:
                a += 1
        retention_rate = a / len(new_user)  # 计算该天第n日留存率
        retention_rates.append(retention_rate)  # 汇总n日留存数据
    data_retention = pd.Series(retention_rates, index=date)
    return data_retention


taobaoappDf = pd.read_excel('d:/WJ/数据准备/登录日志2.xlsx')
print(taobaoappDf)
taobaoappDf[['user_id', 'day']] = taobaoappDf[['PHONE_NUMBER', 'ACTIVE_TIME']]
data_retention = cal_retention(taobaoappDf, 3)  # 求用户的3日留存情况
print(data_retention)