import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=None, hspace=None)

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()