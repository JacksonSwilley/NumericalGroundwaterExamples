'''
Abstract Base Class for grids
'''
from Meta import Meta
import matplotlib.pyplot as plt

class Grid(metaclass = Meta):

    Nodes = None
    Count = None
    Centers = None
    Vertices = None
    AdjacentCells = None
    Distances = None
 
    def Show(__self__):
                plt.figure(dpi = 200)
                plt.triplot(__self__.Nodes[:,0], __self__.Nodes[:,1])
                plt.scatter(__self__.Vertices[:,0,0], __self__.Vertices[:,1,0], color='blue')
                plt.scatter(__self__.Vertices[:,0,1], __self__.Vertices[:,1,1], color='blue')
                plt.scatter(__self__.Vertices[:,0,2], __self__.Vertices[:,1,2], color='blue')
                plt.scatter(__self__.Centers[:,0], __self__.Centers[:,1], color='k')
    
    def CheckAttributes(__self__):
        if __self__.Nodes is None:
            raise NotImplementedError(
                'Subclass must define __self__.Nodes attribute.')

        if __self__.Count is None:
            raise NotImplementedError(
                'Subclass must define __self__.Count attribute.')

        if __self__.Centers is None:
            raise NotImplementedError(
                'Subclass must define __self__.Centers attribute.')

        if __self__.AdjacentCells is None:
            raise NotImplementedError(
                'Subclass must define __self__.AdjacentCells attribute.')

        if __self__.Distances is None:
            raise NotImplementedError(
                'Subclass must define __self__.Distances attribute.')
        
        if __self__.Show is None:
            raise NotImplementedError(
                'Subclass must define __self__.Show attribute.')