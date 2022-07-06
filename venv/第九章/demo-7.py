import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from numpy.random import randn

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum())
plt.show()