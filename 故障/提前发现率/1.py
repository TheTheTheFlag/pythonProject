import pandas as pd
x = {'total': 200.0, 'result_flag': True, 'results': [{'metric': 'fgbusi_sucrate', 'host_tag': '{"BUSI_ID":"月指标统一接口平台流量直充类重点业务成功率","CHANNEL_ID":"考核"}', 'time': '2021-12-17 11:05:00', 'value': 100.0}, {'metric': 'fgbusi_sucrate', 'host_tag': '{"BUSI_ID":"月指标统一接口平台流量直充类重点业务成功率","CHANNEL_ID":"考核"}', 'time': '2021-12-17 11:00:00', 'value': 100.0}]}

print(str(x).replace(',', ' \n'))