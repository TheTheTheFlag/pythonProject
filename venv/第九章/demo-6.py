import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from numpy.random import randn

data = np.random.randn(30).cumsum()

plt.plot(data,'k--',label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')  #线段描述
plt.show()