import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot()
plt.show()