import time
import datetime

now = datetime.datetime.now()
if now.month <= 6:
    before_date = "%s-%s-%s" % (now.year - 1, 6 + now.month, now.day)
else:
    before_date = "%s-%s-%s" % (now.year, now.month - 6)
print(before_date)

# 上面已经可以算出6个月前的今天，是字符串格式。如果想转回时间类型，则加上以下两句
#atime = datetime.datetime.strptime(before_date, "%Y-%m-%d")
#print(atime)