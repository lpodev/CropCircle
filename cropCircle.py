import numpy as np
import matplotlib.pyplot as plt
import random

# On dessine l'axe x et l'axe y
x = np.linspace(-10.0, 10.0, 1000)
y = np.linspace(-10.0, 10.0, 1000)
X, Y = np.meshgrid(x, y)

# On définit nos matrices
matrix = [
    [1, 3],
    [1.25, 3.25],
    [1.5, 3],
    [2.5, 2],
    [1.125, 5.625],
    [1, 5.7525],
    [0.5625, 6.1875],
]

# On définit les axes et les centres de nos matrices
fig = plt.figure()
fig.set_size_inches(8, 8)
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# On dessine nos matrices et on les remplis avec des couleurs aléatoires
for line in matrix:
    y = ((X - line[1])**2) + (Y**2) - line[0] ** 2
    color = random.choice(['red', 'blue', 'green', 'orange', 'purple', 'white', 'black'])
    cs = plt.contour(X, Y, y, [0])
    p = cs.collections[0].get_paths()[0]
    patch = plt.fill(p.vertices[:,0], p.vertices[:,1], color=color, alpha=0.5)

# On affiche les cercles
plt.show()
