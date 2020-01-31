import numpy
from matplotlib import pyplot
import time, sys

def LinearConv(nt):
    nx = 251
    dx = 2/(nx-1) # del x length
    C = 1 # wave speed C
    sigma = 0.5 # from Courant Number
    dt = sigma*dx/C

    u = numpy.ones(nx)
    u[int(0.5 / dx):int((1 / dx)+1)]=2
    pyplot.plot(numpy.linspace(0,2,nx),u,label='Initial u')

    # 1-D linear Convection
    ul=u.copy()
    un = numpy.ones(nx)
    for n in range(nt):
        un = ul.copy()
        for i in range (1,nx):
            ul[i]=un[i]-C*dt/dx*(un[i]-un[i-1])
    pyplot.plot(numpy.linspace(0,2,nx),ul,label='1D Linear Convection')

LinearConv(151)
pyplot.show()