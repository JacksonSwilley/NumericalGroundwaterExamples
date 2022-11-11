'''
A Domain subclass that creates a domain given a grid,
Storage, and Conductivity.
'''

import numpy as np
from Domain import Domain
from Grid import Grid
from Conductivity import Conductivity
from Storage import Storage
from Source import Source

class GriddedDomain(Domain):

    def __init__(__self__, Grid: Grid, \
        Storage: Storage, \
        Conductivity: Conductivity, \
        Source: list[Source] = None):

        __self__.Count = Grid.Count
        __self__.Index = Grid.Index
        __self__.Elements = Grid.Elements
        __self__.Shape = Grid.Shape
        __self__.Regular = True

        for element in __self__.Elements:
            element.Storage = Storage.ReturnS(element.Center[0], \
                element.Center[1], element.Center[2])

            element.Conductivities = [0, 0, 0, 0, 0, 0]

            Kx, Ky, Kz = Conductivity.ReturnK(element.Center[0], \
                element.Center[1], element.Center[2])
            
            Ke = [Kx, Kx, Ky, Ky, Kz, Kz].copy()

            for j in range(6):

                if element.AdjacentCells[j] >=0:

                    j = int(j)

                    neighbor = __self__.Elements[int(element.AdjacentCells[j])]

                    Kx, Ky, Kz = Conductivity.ReturnK(neighbor.Center[0], \
                        neighbor.Center[1], neighbor.Center[2]).copy()
                    
                    K2 = [Kx, Kx, Ky, Ky, Kz, Kz][j]
                    
                    K1 = Ke[j]

                    element.Conductivities[j] = element.Lengths[j] \
                        / ( (element.Lengths[j] - element.InsideLengths[j]) / K2  \
                        + (element.InsideLengths[j]) / K1)

            if Source != None:
                for j in range(len(Source)):
                    Source[j].ApplySource(element)

        
        for boundary in Grid.BoundaryElements:

            i = int(boundary.AdjacentCells)
            element = __self__.Elements[i]

            face = int(boundary.Face)

            Kx, Ky, Kz = Conductivity.ReturnK(boundary.Center[0], \
                boundary.Center[1], boundary.Center[2]).copy()

            Kb = [Kx, Kx, Ky, Ky, Kz, Kz][face]


            Kx, Ky, Kz = Conductivity.ReturnK(element.Center[0], \
                        element.Center[1], element.Center[2]).copy()
            
            Ke = [Kx, Kx, Ky, Ky, Kz, Kz][face]
            
            element.Conductivities[face] = 2 / (1/Kb + 1/Ke)