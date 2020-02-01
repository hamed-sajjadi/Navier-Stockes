
import numpy
from matplotlib import pyplot, cm, interactive
from mpl_toolkits.mplot3d import Axes3D
import time

#In the previous files, i just worked on u, velocity vector on x direction
#But we should consider the velocity in y direction too, the v.

#The file ArrayMethodI & II.py was a 2-D velocity feild concerned by just u velocity vectors.
#Here i am going to involve the v.

nx = 41
ny = 41
nt = 120
nu = 0.01
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = 0.0009
dt = sigma * dx * dy / nu


x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx))
v = numpy.ones((ny,nx))         #Introducing the velocity in Y Dir.
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))
X, Y = numpy.meshgrid(x,y)
R = numpy.ones((ny,nx))

# assignig initial conditions
u[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2
v[int(0.5 / dy) : int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2 #IC of v



start_time=time.time()

for n in range (nt + 1):
    un = u.copy()
    vn = v.copy()

    u[1:-1,1:-1] = (un[1:-1,1:-1] -
                    un[1:-1,1:-1] * dt / dx *
                    (un[1:-1,1:-1] - un[1:-1,0:-2]) -
                    vn[1:-1,1:-1] * dt / dx *
                    (un[1:-1,1:-1] - un[0:-2,1:-1]) +
                    nu * dt / dx**2 *
                    (un[1:-1,2:] - 2*un[1:-1,1:-1] + un[1:-1,0:-2]) +
                    nu * dt / dy**2 *
                    (un[2:,1:-1] - 2*un[1:-1,1:-1] + un[0:-2,1:-1])
                    )

    v[1:-1,1:-1] = (vn[1:-1,1:-1] -
                    vn[1:-1,1:-1] * dt / dx *
                    (vn[1:-1,1:-1] - vn[1:-1,0:-2]) -
                    un[1:-1,1:-1] * dt / dx *
                    (vn[1:-1,1:-1] - vn[0:-2,1:-1]) +
                    nu * dt / dx**2 *
                    (vn[1:-1,2:] - 2*vn[1:-1,1:-1] + vn[1:-1,0:-2]) +
                    nu * dt / dy**2 *
                    (vn[2:,1:-1] - 2*vn[1:-1,1:-1] + vn[0:-2,1:-1])
                    )

    u[ 0 , : ] = 1
    u[ -1, : ] = 1
    u[ : , 0 ] = 1
    u[: , -1 ] = 1
        
    v[ 0 , : ] = 1
    v[ -1, : ] = 1
    v[ : , 0 ] = 1
    v[: , -1 ] = 1

    R[:,:] = ((u[:,:] * u[:,:])+(v[:,:] * v[:,:]))**(0.5)

    pyplot.subplot(2,2,1)
    pyplot.contourf(x,y,R)
    pyplot.title('R')

    pyplot.subplot(2,2,2)
    pyplot.contourf(x,y,u)
    pyplot.title('u')

    pyplot.subplot(2,2,3)
    pyplot.contourf(x,y,v)
    pyplot.title('v')

    pyplot.interactive(False)
    pyplot.savefig("BurgerEQ" +  str(n) + ".png", format="PNG")


print("Process finished in %s seconds " % (time.time() - start_time))


