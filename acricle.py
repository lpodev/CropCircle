import numpy as np
import matplotlib.pyplot as plt
import math

r1 = 1
r2 = 1.25
r3 = 1.5
r4 = 2.5
r5 = 1.125
r6 = 1
r7 = 0.5625
r8 = 0.46

c1 = 3
c2 = 3.25
c3 = 3
c4 = 2
c5 = 5.625
c6 = 5.7525
c7 = 6.1875
c8 = 7.21

x = np.linspace(-10.0, 10.0, 1000)
y = np.linspace(-10.0, 10.0, 1000)
X, Y = np.meshgrid(x, y)

matrix = [
    [1, 3],
    [1.25, 3.25],
    [1.5, 3],
    [2.5, 2],
    [1.125, 5.625],
    [1, 5.7525],
    [0.5625, 6.1875],
]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

for line in matrix:
      y = ((X - line[1])**2) + (Y**2) - line[0] ** 2
      plt.contour(X, Y, y, [0])

# plt.contour(X, Y, f1, [0])
# plt.contour(X, Y, f2, [0])
plt.show()
