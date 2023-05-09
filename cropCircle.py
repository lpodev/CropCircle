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

def semicircle(r, h, k):
    x0 = h - r  # determine x start
    x1 = h + r  # determine x finish
    x = np.linspace(x0, x1, 10000)  # many points to solve for y

    # use numpy for array solving of the semicircle equation
    y = k + np.sqrt(r**2 - (x - h)**2)
    return x, y

def semi2circle(r, h, k):
    x0 = h - r  # determine x start
    x1 = h + r  # determine x finish
    x = np.linspace(x0, x1, 10000)  # many points to solve for y

    # use numpy for array solving of the semicircle equation
    y = k + np.sqrt(r**2 - (x - h)**2)
    return x, -y


# On dessine nos matrices et on les remplis avec des couleurs aléatoires
for line in matrix:
    # y = ((X - line[1])**2) + (Y**2) - line[0] ** 2
    # color = random.choice(['red', 'blue', 'green', 'orange', 'purple', 'white', 'black'])
    # cs = plt.plot(X, y, color=color)

    p,l = semicircle(line[0], line[1], 0)
    plt.scatter(p, l, s=3, c='turquoise')  # plot

    k,j = semi2circle(line[0], line[1], 0)
    plt.scatter(k, j, s=3, c='turquoise')

    plt.gca().set_aspect('equal', adjustable='box')

y_cercle = ((X - 6)**2) + (Y-2)**2 - 0.5 ** 2
plt.contour(X, Y, y_cercle, [0], colors='red')

y_transla = ((X - 6 + 8)**2) + (Y-2+4)**2 - 0.5 ** 2
plt.contour(X, Y, y_transla, [0])



# On affiche les cercles
plt.show()
