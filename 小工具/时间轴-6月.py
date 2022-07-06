import datetime
import time

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


# 获取近6月月份
def previous_months(n: int, month: str = None) -> str:
    if month:
        return (parse(month + "01") + relativedelta(months=-n)).strftime("%Y%m")
    return (datetime.now() + relativedelta(months=-n)).strftime("%Y%m")


before_n_mons = []
for i in range(6):
    before_n_mons.append(previous_months(i, time.strftime("%Y%m", time.localtime())))
before_n_mons = before_n_mons[::-1]

print(before_n_mons)