import datetime
import time

import pandas as pd


print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
today = time.strftime("%Y-%m-%d", time.localtime())
lastday = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
print(today)
print(lastday)

time_list = []
for i in pd.date_range(start=lastday, end=today):
    time_list.append(i)
print(time_list)

ly_time_new = []
for i in time_list:
    ly_time_new.append(time.strftime("%Y-%m-%d", time_list(i)))
print(ly_time_new)
