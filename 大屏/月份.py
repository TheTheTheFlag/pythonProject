from datetime import datetime, date
import datetime
import time
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import pandas as pd
import os
import datetime


def get_nday_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:  # -1倒序
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i - 1)))  # i-1从今天开始
    return before_n_days


time_list = get_nday_list(8)
print(time_list)


def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons = []
for i in range(6):
    print(previous_months(i, time.strftime("%Y%m", time.localtime())))
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))

print(before_n_mons)
