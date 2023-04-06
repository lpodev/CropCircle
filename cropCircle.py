import numpy as np
import matplotlib.pyplot as plt
import math

r1 = 1
r2 = 1.25
r3 = 1.5
r4 = 2.5
r5 = 1.125

x = np.linspace(-1, 10, 1000)
y = np.linspace(0, 0, 1000)
y1 = np.sqrt(r1**2-(x-3)**2)
y2 = np.sqrt(r2**2-(x-3.25)**2)
y3 = np.sqrt(r3**2-(x-3)**2)
y4 = np.sqrt(r4**2-(x-2)**2)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.plot (x, y1)
plt.plot (x,y2)
plt.plot (x,y3)
plt.plot (x,y4)
plt.xlabel ("abcisses")
plt.ylabel("ordonnées")
ax.set_xlim(-1, 9)
ax.set_ylim(-3, 3)

plt.show()

#F = np.sqrt((x-3)**2 - r1**2)
#L = (X-3.25)**2 + (Y)**2 - r2**2
#G = (X-3)**2 + (Y)**2 - r3**2
#H = (X-2)**2 + (Y)**2 - r4**2

#def F():
 #   return ((x - 3) ** 2) + (Y ** 2) - r1 ** 2

#def L():
  #  return (X-3.25)**2 + (Y)**2 - r2**2

#def G():
   # return (X-3)**2 + (Y)**2 - r3**2

#def H():
    #return (X-2)**2 + (Y)**2 - r4**2

#def SQRT_F():
 #   return math.hypot(x,r1)


#fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#res = F()

#print(f"F ==> {F()}")
#print(f"f_1 ==> {f_1(X, Y, r1)}")

#draws = [F(), L(), G(), H(), SQRT_F()]


#for d in draws:
  #  plt.contour(X, Y, d, [0])

plt.contour(X,Y,F,[0])
plt.contour(X,Y,F,[0])
plt.contour(X,Y,L,[0])
plt.contour(X,Y,G,[0])
plt.contour(X,Y,H,[0])
# plt.contour(X,Y,SQRT_F,[0])
plt.show()


