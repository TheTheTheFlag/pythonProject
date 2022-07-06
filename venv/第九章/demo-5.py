import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from numpy.random import randn
#ax.plot(x, y, 'g--')
#ax.plot(x, y, linestyle='--', color='g')
plt.plot(randn(30).cumsum(), 'ko--')
plt.show()