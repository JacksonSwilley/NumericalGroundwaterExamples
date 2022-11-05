'''
A Domain subclass that creates a domain given a grid, thicknesses,
Storage, and Conductivity.
'''

from Domain import Domain
from Element import Element
import numpy as np

class StackedGridDomain(Domain):

    def __init__(__self__, Grid, Storage, Conductivity, Thickness=[1]):

        layers = len(Thickness)

        __self__.Count = Grid.Count * layers
        __self__.Elements = [Element] * __self__.Count

        Index = 0

        for j in range(layers):
            for i in range(Grid.Count):
                __self__.Elements[Index] = Element(Index, Storage, Conductivity, Grid, Thickness)
                Index = Index + 1

        K = np.copy(__self__.Elements[:].Conductivity)

        for element in __self__.Elements:
            for i in element.AdjacentCells:
                element.Conductivity[i] = element.Length[i] \
                    / ( element.InsideLength[i] / element.Conductivity[i] \
                    +  (element.Lengths[i] - element.InsideLength[i]) / K[i] )