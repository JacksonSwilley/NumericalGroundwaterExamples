'''
RectangularGrid build a full 3D grid of spatially-aware
elements and their boundary counterparts
'''
import numpy as np
from Element import Element
# from BoundaryElement import BoundaryElement


class RectangularGrid(object):
    def __init__(__self__, DeltaX, DeltaY=[1], DeltaZ=[1]):
        __self__.Count = len(DeltaX) * len(DeltaY) * len(DeltaZ)
        __self__.Index = np.arange(0,__self__.Count, 1)

        id = np.reshape(__self__.Index,(len(DeltaX), len(DeltaY), len(DeltaZ)), order='F')
        AdjacentCells = np.zeros((len(DeltaX), len(DeltaY), len(DeltaZ), 6)) - 99

        # x-1 neighbor
        AdjacentCells[1:,:,:,0] = id[0:-1,:,:]
        # x+1 neighbor
        AdjacentCells[0:-1,:,:,1] = id[1:,:,:]
        # y-1 neighbor
        AdjacentCells[:,1:,:,2] = id[:,0:-1,:]
        # y+1 neighbor
        AdjacentCells[:,0:-1,:,3] = id[:,1:,:]
        # z-1 neighbor
        AdjacentCells[:,:,1:,4] = id[:,:,0:-1]
        # z+1 neighbor
        AdjacentCells[:,:,0:-1,5] = id[:,:,1:]
        # wipe lonely cells
        AdjacentCells[AdjacentCells==-99] = None
        AdjacentCells.astype(int)

        Centers = np.zeros((len(DeltaX), len(DeltaY), len(DeltaZ), 3))
        Centers[:,:,:,0], \
        Centers[:,:,:,1], \
        Centers[:,:,:,2]  \
            = np.meshgrid( \
            np.cumsum(DeltaX) - DeltaX/2, \
            np.cumsum(DeltaY) - DeltaY/2, \
            np.cumsum(DeltaZ) - DeltaZ/2, \
            indexing='ij')
        
        InsideDistances = np.zeros(np.shape(AdjacentCells)) - 99

        for k in range(len(DeltaZ)):
            for j in range(len(DeltaY)):
                for i in range(len(DeltaX)):
                    InsideDistances[i, j, k, 0] = DeltaX[i] / 2
                    InsideDistances[i, j, k, 1] = DeltaX[i] / 2
                    InsideDistances[i, j, k, 2] = DeltaY[j] / 2
                    InsideDistances[i, j, k, 3] = DeltaY[j] / 2
                    InsideDistances[i, j, k, 4] = DeltaZ[k] / 2
                    InsideDistances[i, j, k, 5] = DeltaZ[k] / 2

        Distances = np.zeros(np.shape(AdjacentCells), float) - 99

        dx = (DeltaX[0:-1] + DeltaX[1:]) / 2
        dy = (DeltaY[0:-1] + DeltaY[1:]) / 2
        dz = (DeltaZ[0:-1] + DeltaZ[1:]) / 2

        for k in range(len(dz)):
            for j in range(len(dy)):
                for i in range(len(dx)):
                    Distances[1:,j,k,0] = dx
                    Distances[:-1,j,k,1] = dx
                    Distances[i,1:,k,2] = dy
                    Distances[i,:-1,k,3] = dy
                    Distances[i,j,1:,4] = dz
                    Distances[i,j,:-1,5] = dz


        Areas = np.zeros(np.shape(AdjacentCells)) - 99

        for k in range(len(DeltaZ)):
            for j in range(len(DeltaY)):
                for i in range(len(DeltaX)):
                    Areas[i, j, k, 0] = DeltaY[j] * DeltaZ[k]
                    Areas[i, j, k, 1] = DeltaY[j] * DeltaZ[k]
                    Areas[i, j, k, 2] = DeltaX[i] * DeltaZ[k]
                    Areas[i, j, k, 3] = DeltaX[i] * DeltaZ[k]
                    Areas[i, j, k, 4] = DeltaX[i] * DeltaY[j]
                    Areas[i, j, k, 5] = DeltaX[i] * DeltaY[j]     

        ticker = 0
        __self__.Elements = [Element] * __self__.Count
        for k in range(len(DeltaZ)):
            for j in range(len(DeltaY)):
                    for i in range(len(DeltaX)):
                        assert __self__.Index[ticker] == id[i,j,k]

                        __self__.Elements[__self__.Index[ticker]] = \
                            Element(__self__.Index[ticker], [i,j,k], \
                                Centers[i,j,k,:], \
                                AdjacentCells[i,j,k,:], \
                                Areas[i,j,k,:], \
                                Distances[i,j,k,:], \
                                InsideDistances[i,j,k,:], \
                                DeltaZ[k])

                        ticker = ticker + 1

        GhostCount = np.count_nonzero(np.isnan(AdjacentCells))
        GhostIndex = np.arange(0,GhostCount, 1)

        # x = 0 face
        left = np.zeros((len(DeltaY), len(DeltaZ),3))
        left[:,:,0] = 0
        left[:,:,1] = Centers[0,:,:,1]
        left[:,:,2] = Centers[0,:,:,2]
        # x = x_max face
        right = np.zeros((len(DeltaY), len(DeltaZ),3))
        right[:,:,0] = np.sum(DeltaX)
        right[:,:,1:] = Centers[0,:,:,1:]
        # y = 0 face
        front = np.zeros((len(DeltaX),len(DeltaZ),3))
        front[:,:,1] = 0
        front[:,:,0] = Centers[:,0,:,0]
        front[:,:,2] = Centers[:,0,:,2]

        # y = y_max face
        back = np.zeros((len(DeltaX),len(DeltaZ),3))
        back[:,:,1] = np.sum(DeltaY)
        back[:,:,0] = Centers[:,0,:,0]
        back[:,:,2] = Centers[:,0,:,2]

        # z = 0 face
        bottom = np.zeros((len(DeltaX),len(DeltaY),3))
        bottom[:,:,2] = 0
        bottom[:,:,0:-1] = Centers[:,:,0,0:-1]

        # z = z_max face
        top = np.zeros((len(DeltaX),len(DeltaY),3))
        top[:,:,2] = np.sum(DeltaZ)
        top[:,:,0:-1] = Centers[:,:,0,0:-1]

        GhostCenters = [left, right, front, back, bottom, top]

        left = id[0,:,:]
        right = id[-1,:,:]
        front = id[:,0,:]
        back = id[:,-1,:]
        bottom = id[:,:,0]
        top = id[:,:,-1]
        GhostAdjacentCells = [left, right, front, back, bottom, top]