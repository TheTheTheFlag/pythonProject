# date 参数是时间格式的时间， n是要计算前几个月
import datetime

def getTheMonth(date, n):
    month = date.month
    year = date.year
    for i in range(n):
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
    return datetime.date(year, month, 1).strftime('%Y-%m')

# 测试
date = datetime.datetime.today()         # 输出 2019-04-15
getTheMonth(date, 1).strftime("%Y-%m")   # 输出 2019-03
getTheMonth(date, 6).strftime("%Y-%m")   # 输出 2018-10
