import numpy as np
import pandas as pd
import time
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from datetime import datetime

df = pd.read_excel('d:/kol.xlsx')
df[['创建人','归属地市']] = df[['创建人','归属地市']].applymap(lambda x: str(x).strip())
df['创建时间'] = pd.to_datetime(df['创建时间'],format = '%Y-%m-%d %H:%M:%S')
#重置日期列时间格式为00:00:00
df['创建时间'] = df['创建时间'].apply(lambda x: x).dt.normalize()
#使用pd_date_range筛选指定日期的数据
df_Jun = df[df['创建时间'].isin(pd.date_range('2021-6-1', '2021-6-30'))]

df_count = df_Jun.groupby('归属地市')['序号'].count()
#df_count = df_count['归属地市']
x1 = df_count.index
y1 = df_count.values

from matplotlib.font_manager import FontProperties   #显示中文，并指定字体
myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name(),style = 'dark')

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(2,1,1)
def make_autopct(values):
    def my_autopct(pct):
        total = sum(y1)
        val = int(round(pct*total/100.0))
        # 同时显示数值和占比的饼图
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
plt.pie(y1, labels=x1, autopct=make_autopct(y1),pctdistance=0.6,labeldistance=1.1,radius=1.5)
plt.legend(x1,loc="upper left",bbox_to_anchor=(1.6, 0.2, 0.5, 1))


ax2 = fig.add_subplot(2,1,2)
ax2 = sns.barplot(x=x1, y=y1, data=df_Jun, palette="pastel")   #seaborn画柱状图 data可以删除
plt.xticks(fontsize=16)          #设置x和y轴刻度值字体大小
plt.yticks(fontsize=16)
#plt.yticks(np.arange(0, 300, 50))   #设置y轴标签
plt.xlabel("6月地市", fontsize=16)  #设置x轴和y轴标签字体大小
plt.ylabel("6月话题数", fontsize=16)
x = np.arange(len(x1))    #在柱状图上插入数值
y = np.array(list(y1))
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=16)
#plt.show()

from pyecharts.charts import Map,Geo
from pyecharts import options as opts
#将数据处理成列表
locate = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','陕西','甘肃','青海','宁夏','新疆','西藏']
app_price = [10.84,8.65,18.06,8.90,5.04,29.20,8.98,17.80,27.81,24.24,12.72,11.10,6.30,7.00,22.45,16.92,11.00,14.99,18.85,5.85,1.40,7.32,14.61,4.62,6.05,8.07,6.73,15.54,13.00,39.07,25.61,21.3]
list1 = [[locate[i],app_price[i]] for i in range(len(locate))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="2019年全国各省苹果价格表"),
    visualmap_opts=opts.VisualMapOpts(max_=50)  #最大数据范围
    )
map_1.add("2019年全国各省苹果价格", list1, maptype="china")
map_1.render('d:/map1.html')

map2 = Map()
city = x1
values2 = y1
list1 = [[city[i],values2[i]] for i in range(len(city))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="6月浙江各地市创建话题数"),
    visualmap_opts=opts.VisualMapOpts(max_=50)  #最大数据范围
    )
map_1.add("6月浙江各地市创建话题数", list1, maptype="浙江")
map2.render(path="D:/6月浙江各地市创建话题数.html")
