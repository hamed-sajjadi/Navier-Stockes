
import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
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

X, Y = numpy.meshgrid(x,y) #The X and Y values that you pass to plot_surface are not the 1-D vectors x and y.
                           #In order to use matplotlibs 3D plotting functions, you need to generate a grid of x, y values
                           #which correspond to each coordinate in the plotting frame.
                           #This coordinate grid is generated using the numpy function meshgrid.

# assignig initial conditions

u[int(0 / dy) : int(0.5 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2


start_time=time.time()
# Method II in Array
for n in range (nt + 1):
    un=u.copy()
    u[1:,1:]=(un[1:,1:]-(c * dt / dx * (un [1:,1:] - un[1:, 0:-1])) -
                        (c * dt / dy * (un [1:,1:] - un[0:-1, 1:])))
    u[ 0 , : ] = 1
    u[ -1, : ] = 1
    #u[0:40,60:100]=0
    #u[int(0 / dy) : int(0.5 / dy + 1),1] = 10
    u[ : , 0 ] = 1
    u[: , -1 ] = 1
    #pyplot.contourf(x,y,u)
    #pyplot.savefig("img" +  str(n) + ".png", format="PNG")
print("Process finished in %s seconds " % (time.time() - start_time))

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax  = fig.gca(projection = '3d')
surf = ax.plot_surface(X,Y,u[:], cmap = cm.viridis)
pyplot.show(surf)

