import numpy
from matplotlib import pyplot
import time, sys

nx = 25 # number of grids
nt = 50 # number of time stpes
dx = 2/(nx-1) # del x length
dt = .01 #amout of each time steps
C = 1 # wave speed C
vis = 0.1 # viscosity

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
pyplot.plot(numpy.linspace(0,2,nx),ul,label='u 1 - D linear convection')

# 1-D Convection
uc=u.copy()
un = numpy.ones(nx)
for n in range(nt):
    un = uc.copy()
    for i in range (1,nx):
        uc[i]=un[i]-(un[i]*dt/dx*(un[i]-un[i-1])) #replacing u[i] instead of C wave speed (a constant)
pyplot.plot(numpy.linspace(0,2,nx),uc, label='u 1 - D convection')

# 1-D Diffusion
uvis=u.copy()
un = numpy.ones(nx)
for n in range(nt):
    un = uvis.copy()
    for i in range (2,nx-1):
        uvis[i]=un[i]+vis*dt/dx/dx*(un[i+1]-2*un[i]+un[i-1])
pyplot.plot(numpy.linspace(0,2,nx),uvis, label='u 1 - D Diffusion')

# 1-D Burger's Equation
ubur=u.copy()
un = numpy.ones(nx)
for n in range(nt):
    un = ubur.copy()
    for i in range (2,nx-1):
        ubur[i]=un[i]-(un[i]*dt/dx*(un[i]-un[i-1]))+vis*dt/dx/dx*(un[i+1]-2*un[i]+un[i-1])
pyplot.plot(numpy.linspace(0,2,nx),ubur, label='u 1 - D Burger Equation')

pyplot.legend(loc='best')
pyplot.show()