import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ips = pd.read_csv('examples/tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
# Not many 1- and 6-person parties
party_counts = party_counts.loc[:, 2:5]
# Normalize to sum to 1
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
#party_pcts.plot.bar()
#plt.show()

tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h')
sns.set(style="whitegrid")

tips['tip_pct'].plot.hist(bins=50) #直方图
tips['tip_pct'].plot.density()     #密度图
party_pcts.plot.bar()
plt.show()
