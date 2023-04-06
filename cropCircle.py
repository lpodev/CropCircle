import numpy as np
import matplotlib.pyplot as plt
import math

r1 = 1
r2 = 1.25
r3 = 1.5
r4 = 2.5
r5 = 1.125

# define the axes
x = np.linspace(-1, 10, 1000)
y = np.linspace(0, 0, 1000)

y1 = np.sqrt(r1**2-(x-3)**2)
y2 = np.sqrt(r2**2-(x-3.25)**2)
y3 = np.sqrt(r3**2-(x-3)**2)
y4 = np.sqrt(r4**2-(x-2)**2)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.plot (x,y1)
plt.plot (x,y2)
plt.plot (x,y3)
plt.plot (x,y4)
plt.xlabel ("abcisses")
plt.ylabel("ordonnées")
ax.set_xlim(-1, 9)
ax.set_ylim(-3, 3)
plt.show()
