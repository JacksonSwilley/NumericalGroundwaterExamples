'''
Element is essentially a helper class that is the base of all domains.
We use Element to hold the geometry of the domain.
'''

import numpy as np

class Element(object):

    def __init__(__self__, Index, Indices, \
        Center, AdjacentCells, Areas, Distances, \
        InsideDistances, Thickness):

        __self__.Index = Index
        __self__.Indices = Indices
        __self__.Center = Center
        __self__.AdjacentCells = AdjacentCells
        __self__.Areas = Areas
        __self__.Footprint = Areas[4]
        __self__.Lengths = Distances
        __self__.InsideLengths = InsideDistances
        __self__.Volumes = __self__.Footprint * Thickness
    
    def Area(__self__, Locator):
        return __self__.Areas[np.where(__self__.AdjacentCells == Locator)]

    def Length(__self__, Locator):
        return __self__.Lengths[np.where(__self__.AdjacentCells == Locator)]
    
    def Conductivity(__self__, Locator):
        return __self__.Conductivities[np.where(__self__.AdjacentCells == Locator)]