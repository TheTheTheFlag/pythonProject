import xlrd
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm  # 字体管理器
import numpy as np
import pyecharts.options as opts
import os
from numpy import random
from pyecharts.charts import Bar


# %matplotlib inline
from pyecharts.globals import ThemeType

citys = ['湖州', '金华', '宁波', '台州', '舟山', '嘉兴', '杭州', '丽水', '衢州', '绍兴', '温州']
# 读取文件
workbook = xlrd.open_workbook('D:\\WJ\\KOL用户.xls')
sheet = workbook.sheet_by_index(0)
# 姓名
user_name = sheet.col_values(2)[1:]
# 手机号码
user_phone = sheet.col_values(1)[1:]
# 地市
ascription = sheet.col_values(16)[1:]
# 组织
user_organization = sheet.col_values(4)[1:]
# 职务
# 游客
user_visitor = sheet.col_values(18)[1:]
# 省职工代表
user_province = sheet.col_values(20)[1:]
# 市职工代表
user_city = sheet.col_values(19)[1:]

# 获取地市分布人数及占比
# 分布人数
as_dict = dict()
for i in ascription:
    if i in citys:
        as_dict[i] = ascription.count(i)
print("各地市KOL总人数：%s" % as_dict)
# 获取总数
num = len(ascription)
# print(num)
# 占比
# .apply()函数是将方法依次作用于元素
# lambda定义匿名函数
# format()转换格式，'.2%'代表保留两位小数得百分数，可以自定义保留位数
persent_dict = dict()
for i in as_dict:
    # persent_dict[i] = as_dict[i] / num * 100
    # persent_dict[i] = (as_dict[i] / num * 100).apply(lambda x: format(x, '.4%'))
    persent_dict[i] = "%.4f%%" % (as_dict[i] / num * 100)  # 保留小数点后4位
print("各地市KOL总人数占比：%s" % persent_dict)
# # 形成饼图
# # 准备字体
# my_font = fm.FontProperties(fname='C:\Windows\Fonts\Arial.ttf')
# date = []
# for a in persent_dict:
#     date.append(persent_dict[a])
# print(date)
# # 准备标签
# labels = ['省公司', '湖州', '金华', '宁波', '台州', '舟山', '嘉兴', '杭州', '丽水', '衢州', '绍兴', '温州']
# # 将排列在最后的温州分离出来
# explode = [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0]
# # 自定义颜色
# colors = ['red', 'orange', 'yellow', 'cyan', 'magenta', 'purple', 'pink', 'blue', 'brown', 'khaki', 'olive', 'gold']
# # 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
# plt.axes(aspect='equal')
# # 控制X轴和Y轴的范围(用于控制饼图的圆心、半径)
# plt.xlim(0, 8)
# plt.ylim(0, 8)
# # 不显示边框
# plt.gca().spines['right'].set_color('none')
# plt.gca().spines['top'].set_color('none')
# plt.gca().spines['left'].set_color('none')
# plt.gca().spines['bottom'].set_color('none')
# # 开始绘制
# plt.pie(x=date,  # 绘制数据
#         labels=labels,  # 添加标签
#         explode=explode,  # 突出显示杭州
#         colors=colors,  # 设置自定义填充色
#         autopct='%.4f%%',  # 设置百分比格式
#         pctdistance=0.8,  # 设置百分比标签和圆心的距离
#         labeldistance=1.0,  # 设置标签和圆心的距离
#         startangle=180,  # 设置饼图的初始角度
#         center=(4, 4),  # 设置饼图的圆心（相当于X轴和Y轴的范围）
#         radius=3.8,  # 设置饼图的半径（同上）
#         counterclock=False,  # 是否为逆时针方向，False表示顺时针方向
#         wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
#         textprops={'fontsize': 12, 'color': 'black', 'fontproperties': my_font},  # 设置文本标签的属性值
#         frame=1  # 是否显示饼图的圆圈，1为显示
#         )
# # 不显示X轴、Y轴的刻度值
# plt.xticks(())
# plt.yticks(())
# # 添加图形标题
# plt.title('地市活跃用户分布图', fontproperties=my_font)
# # 显示图形
# plt.show()

#  统计类标签：姓名，地市，组织，职务，是否KOL，是否游客，是否省市职代，是否活跃，业务偏好


# 规则类标签：是否活跃（7天内有登录或留言），业务偏好（参与留言/浏览的话题业务前三类）

# 读取留言话题
ly_workbook = xlrd.open_workbook('D:\\WJ\\留言记录.xls')
ly_sheet = ly_workbook.sheet_by_index(0)
# 留言人手机号码
ly_phone = ly_sheet.col_values(7)[1:]
# 留言时间
ly_time = ly_sheet.col_values(2)[1:]
# 留言人城市
ly_ascription = ly_sheet.col_values(8)[1:]
# 获取留言数量
gl_list = []
ly_ascription_list = []
# 过滤去重
for i in range(0, len(ly_phone)):
    if ly_phone[i] not in gl_list:
        gl_list.append(ly_phone[i])
    else:
        pass
for y in range(0, len(gl_list)):
    if gl_list[y] in user_phone:
        ly_ascription_list.append(ly_ascription[y])
    else:
        pass
# 11个地市
ly_ascription_dict = dict()
for l in ly_ascription_list:
    if l in citys:
        ly_ascription_dict[l] = ly_ascription_list.count(l)
    else:
        pass
print("各地市活动参与总人数：%s" % ly_ascription_dict)

# 留言活跃
print(ly_time)
ly_time_new = []
for i in ly_time:
    ly_time_new.append(datetime.datetime.strptime(i[:18], '%d-%b-%y %H.%M.%S'))
now_time = datetime.datetime.strptime('2021-07-14 00.00.00', '%Y-%m-%d %H.%M.%S')
time_list = []
now_time_list = []
time_dict = dict()
demo = []
for b, k in enumerate(ly_ascription):
    # b:下标
    # k:地市
    if k in citys:
        time_list.append(datetime.datetime.strptime(ly_time[b][:18], '%d-%b-%y %H.%M.%S'))
for i in time_list:
    # 各地市活跃人数
    # 判断近7天有无登录或留言
    day_time = (now_time - i).days
    if day_time <= 7:
        now_time_list.append(i)
for i in now_time_list:  # 获取时间所对应的地市下标
    if i in ly_time_new:
        demo.append(ly_time_new.index(i))
# 获取地市
time_address = []
for i in demo:
    time_address.append(ly_ascription[i])
for i in time_address:
    if i in citys:
        time_dict[i] = time_address.count(i)
print("各地市活跃人数：%s" % time_dict)

# citys = ['湖州', '金华', '宁波', '台州', '舟山', '嘉兴', '杭州', '丽水', '衢州', '绍兴', '温州']
as_people = [137, 1129, 321, 1159, 89, 156, 641, 115, 392, 156, 4413]
paety_people = [29, 167, 138, 69, 25, 129, 312, 61, 25, 139, 253]
run_people = [3, 180, 49, 44, 31, 44, 136, 2, 93, 53, 77]


# 显示数值
y1 = [x for x in as_people]
y2 = [y for y in paety_people]
y3 = [z for z in run_people]

goods = citys
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(citys)
    .add_yaxis('KOL人数', y1, stack='stack1')
    .add_yaxis('参与人数', y2, stack='stack1')
    .add_yaxis('活跃人数', y3, stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='KOL活跃情况'),
                     xaxis_opts=opts.AxisOpts(name='地市'),
                     yaxis_opts=opts.AxisOpts(name='活跃人数'),
                     visualmap_opts=opts.VisualMapOpts(max_=1000),
                     toolbox_opts=opts.ToolboxOpts(),
                     datazoom_opts=opts.DataZoomOpts()
                     )
)

bar.render('D:/KOL活跃情况堆叠图.html')
os.system("D:/KOL活跃情况堆叠图.html")