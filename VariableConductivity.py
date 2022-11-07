'''
K selector the bounds ([Xmin, Xmax, Ymin, Ymax, Zmin, Zmax])
and the values of K (Nx by Ny by Nz by 3)
'''

import numpy as np
from Conductivity import Conductivity

class VariableConductivity(Conductivity):
    
    def __init__(__self__, Bounds:list, Values:list):
        __self__.Bounds = Bounds
        __self__.Values = Values

        nx = np.shape(Values)[0]
        ny = np.shape(Values)[1]
        nz = np.shape(Values)[2]

        __self__.nx = nx
        __self__.ny = ny
        __self__.nz = nz

        __self__.dx = (Bounds[1] - Bounds[0]) / nx
        __self__.dy = (Bounds[3] - Bounds[2]) / ny
        __self__.dz = (Bounds[5] - Bounds[4]) / nz

        __self__.x = np.linspace(Bounds[0], Bounds[1], nx+1)
        __self__.y = np.linspace(Bounds[2], Bounds[3], ny+1)
        __self__.z = np.linspace(Bounds[4], Bounds[5], nz+1)

    def ReturnK(__self__, X=None, Y=None, Z=None, Saturation=None):

        i = 0
        for i in range(1,__self__.nx):
            if(__self__.x[i] >= X and __self__.x[i-1] <= X): break
        
        j = 0
        for j in range(1,__self__.ny):
            if(__self__.y[j] >= Y and __self__.y[j-1] <= Y): break
        
        k = 0
        for k in range(1,__self__.nz):
            if(__self__.z[k] >= Z and __self__.z[k-1] <= Z): break

        # i = np.where((__self__.x >= X - __self__.dx / 2) & (__self__.x <= X + __self__.dx / 2))
        # j = np.where((__self__.y >= Y - __self__.dy / 2) & (__self__.y <= Y + __self__.dy / 2))
        # k = np.where((__self__.z >= Z - __self__.dz / 2) & (__self__.z <= Z + __self__.dz / 2))

        values = __self__.Values[i,j,k,:].flatten()

        return [values[0], values[1], values[2]]