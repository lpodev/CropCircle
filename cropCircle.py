import numpy as np
import matplotlib.pyplot as plt
import math

r1 = 1
r2 = 1.25
x = np.linspace(-10.0, 10.0, 1000)
y = np.linspace(-10.0, 10.0, 1000)
X, Y = np.meshgrid(x,y)

F = (X-3)**2 + (Y)**2 - r1**2
L = (X-3.25)**2 + (Y)**2 - r2**2


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.contour(X,Y,F,[0])
plt.contour(X,Y,L,[0])
plt.show()




