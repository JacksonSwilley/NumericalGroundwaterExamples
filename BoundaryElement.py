'''
BoundaryElement is essentially a helper class that is the base of all
boundaries. We use BoundarElement to hold the geometry of the domain.
'''

import numpy as np

class BoundaryElement(object):

    def __init__(__self__, Index, Face, Center, AdjacentCell, Area, InsideDistance):

        __self__.Index = Index
        __self__.Face = Face
        __self__.FaceLayout = ['0: Left\n1: Right\n2: Front\n3: Back\n' \
            '4: Bottom\n5: Top\n-99: In-Domain Source']
        __self__.Center = Center
        __self__.AdjacentCell = AdjacentCell
        __self__.Area = Area
        __self__.Length = InsideDistance
        __self__.Coefficient = 0
        __self__.Head = 0
        __self__.Flux = 0

    # def Area(__self__, Locator):
    #     return __self__.Areas[np.where(__self__.AdjacentCells == Locator)]

    # def Length(__self__, Locator):
    #     return __self__.Lengths[np.where(__self__.AdjacentCells == Locator)]
    
    # def Conductivity(__self__, Locator):
    #     return __self__.Conductivities[np.where(__self__.AdjacentCells == Locator)]