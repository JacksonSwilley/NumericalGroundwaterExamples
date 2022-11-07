'''
Concrete boundary subclass. Will need to add transience later
unfortunately
'''

from Boundary import Boundary
from Conductivity import Conductivity
from BoundaryCondition import BoundaryCondition
from Grid import Grid

class GriddedBoundary(Boundary):
    def __init__(__self__, Grid: Grid, \
        Conductivity: Conductivity, \
        BoundaryConditions: list[BoundaryCondition]):

        __self__.Count = Grid.Count
        __self__.Index = Grid.BoundaryIndex
        __self__.Elements = Grid.BoundaryElements

        for boundary in __self__.Elements:

            i = int(boundary.AdjacentCells)
            element = Grid.Elements[i]

            face = int(boundary.Face)

            Kx, Ky, Kz = Conductivity.ReturnK(boundary.Center[0], \
                boundary.Center[1], boundary.Center[2]).copy()

            Kb = [Kx, Kx, Ky, Ky, Kz, Kz][face]

            Kx, Ky, Kz = Conductivity.ReturnK(element.Center[0], \
                        element.Center[1], element.Center[2]).copy()
            
            Ke = [Kx, Kx, Ky, Ky, Kz, Kz][face]
            
            boundary.Conductivities = 2 / (1/Kb + 1/Ke)

            face = boundary.Face
            boundary.Coefficient = 0
            boundary.Head = 0
            boundary.Flux = 0
            for j in range(len(BoundaryConditions)):
                C, H, Q = BoundaryConditions[j].ReturnBC(face)
                boundary.Coefficient = boundary.Coefficient + C
                boundary.Head = boundary.Head + H
                boundary.Flux = boundary.Flux + Q