'''
A class to create a mesh grid and calculate necessary, grid-related parameters
'''
from Grid import Grid
from matplotlib.tri import triangulation
import numpy as np

class TriangularGrid(Grid):
    def __init__(__self__, Nodes):
        
        __self__.Nodes = Nodes

        # create triangulated grid
        tri = triangulation(Nodes[:,0], Nodes[:,1])

        # provide the class with the number of triangles
        __self__.Count = tri.triangles.shape[0]

        # find the cell centers of each triangle
        __self__.Centers = np.zeros((__self__.Count, 2))

        for i in range(__self__.Count):
            for j in range(2):
             __self__.Centers[i, j] = np.mean(Nodes[tri.triangles[i], j])

        # find the coordinates of all three vertices of each triangle
        __self__.Vertices = np.zeros((__self__.Count, 2, 3))

        for i in range(__self__.Count):
            for j in range(2):
                for k in range(3):
                    __self__.Vertices[i, j, k] = Nodes[tri.triangles[i], j][k]

        # find the side widths of each cell interface for each triangle
        __self__.SideWidths = np.zeros((__self__.Count, 3))

        for i in range(__self__.Count):
            for k in range(3):
                __self__.SideWidths[i, k] = norm(
                    [[__self__.Vertices[i, 0, k], __self__.Vertices[i, 1, k]],
                    [__self__.Vertices[i, 0, k-1], __self__.Vertices[i, 1, k-1]]])

        # find the indices (i) of the adjacent triangles
        __self__.AdjacentCells = np.zeros((__self__.Count, 3))
        
        for i in range(__self__.Count):
            k = 0
            for ii in range(__self__.Count):

                set_i_x = set(__self__.Vertices[i, 0, :])
                set_i_y = set(__self__.Vertices[i, 1, :])

                set_ii_x = set(__self__.Vertices[ii, 0, :])
                set_ii_y = set(__self__.Vertices[ii, 1, :])
                
                if(len(set_i_x & set_ii_x)==2 and len(set_i_y & set_ii_y)==2):
                    
                    __self__.AdjacentCells[i, k] = ii
                    k = k + 1
                
                if(k>2): break

        # find the indices (i) of the adjacent triangles
        __self__.Distances = np.zeros((__self__.Count, 3))

        for i in range(__self__.Count):
            for k in range(3):
                ii = int(__self__.AdjacentCells[i,k])
                __self__.Distances[i, k] = norm(
                    [[__self__.Centers[i, 0], __self__.Centers[i, 1]],
                    [__self__.Centers[ii, 0], __self__.Centers[ii, 1]]])
        
    def Show(__self__):
        super().Show()