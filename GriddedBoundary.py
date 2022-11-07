from Boundary import Boundary
from Conductivity import Conductivity
from BoundaryCondition import BoundaryCondition
from Grid import Grid

class GriddedBoundary(Boundary):
    def __init__(__self__, Grid: Grid, \
        Conductivty: Conductivity, \
        BoundaryConditions: BoundaryCondition, \
        Sources: BoundaryCondition=None):

        __self__.Count = Grid.Count
        __self__.Index = Grid.BoundaryIndex
        __self__.Elements = Grid.BoundaryElements