import numpy as np
from matplotlib import pyplot as plt, cm
from mpl_toolkits.mplot3d import Axes3D

nx = 161
ny = 161

nu = .05
dx = 2/( nx - 1 )
dy = 2/( ny - 1 )
sigma = .25
dt = sigma * dx * dy / nu

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

# velocity in x dir
u = np.ones((ny,nx))
un = np.ones((ny,nx))
R = np.ones((ny,nx))

# velocity in y dir
v = np.ones((ny,nx))
vn = np.ones ((ny,nx))

def diffuse(nt):
    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 1.5
    v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 10
    
    for n in range (nt + 1):
        un = u.copy()
        u[1:-1,1:-1] = (un[1:-1,1:-1] +
                        nu * (dt / dx**2) * 
                        (un[1:-1, 2:] - 2 * un[1:-1,1:-1] + un[1:-1,0:-2]) +
                        nu * (dt / dy**2) *
                        (un[2:, 1:-1] - 2 * un[1:-1,1:-1] + un[0:-2,1:-1]))
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

        vn = v.copy()
        v[1:-1,1:-1] = (vn[1:-1,1:-1] +
                        nu * (dt / dx**2) * 
                        (vn[1:-1, 2:] - 2 * vn[1:-1,1:-1] + vn[1:-1,0:-2]) +
                        nu * (dt / dy**2) *
                        (vn[2:, 1:-1] - 2 * vn[1:-1,1:-1] + vn[0:-2,1:-1]))
        v[0, :] = 1
        v[-1, :] = 1
        v[:, 0] = 1
        v[:, -1] = 1

        R[:,:] = ((u[:,:] * u[:,:])+(v[:,:] * v[:,:]))**(0.5)

        plt.figure()
        plt.contourf(x , y , R)

        plt.savefig("diffuse" +  str(n) + ".png", format="PNG")


    

diffuse(50)