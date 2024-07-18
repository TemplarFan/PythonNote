from pylab import *
import numpy as np

# from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection="3d")
# ax = Axes3D(fig)

x = np.arange(1,10, 1)
y = np.arange(1,10, 1)
X, Y = np.meshgrid(x, y)
Z = 3*X+2*Y+30

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
ax.set_zlim3d(0,100)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()