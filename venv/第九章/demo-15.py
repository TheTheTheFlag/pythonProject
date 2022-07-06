import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
sns.distplot(values, bins=100, color='k')
values.plot.bar()
plt.show()