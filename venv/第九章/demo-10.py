import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

from numpy.random import randn
from datetime import datetime

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color='g', alpha=0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
#plt.show()
plt.savefig('d:/figpath.png', dpi=400, bbox_inches='tight')