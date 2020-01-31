import numpy
from matplotlib import pyplot
import time

nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = 0.2
dt = sigma * dx

x = numpy.linspace(0,2,nx) # dividing 0<x<2 into nx parts
y = numpy.linspace(0,2,ny) # dividing 0<y<2 into ny parts
u = numpy.ones((ny,nx))

# assignig initial conditions
u[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx) : int(1 / dx + 1)] = 2


start_time=time.time()
# Method I in Array
for n in range (nt + 1):
    un = u.copy()
    row, col = u.shape # dimension of matrice u
    for j in range (1,row):
        for i in range (1,col):
            u[j , i]=(un[j , i]-(c * dt / dx *
                                 (un[j , i] - un[j , i - 1])) -
                      (c * dt / dy *
                       (un[j , i]-un[j - 1 , i])))
            u[ 0 , : ] = 1
            u[ -1, : ] = 1
            u[ : , 0 ] = 1
            u[: , -1 ] = 1

print("Process finished in %s seconds " % (time.time() - start_time))
pyplot.contourf(x,y,u)
pyplot.colorbar()
pyplot.show()