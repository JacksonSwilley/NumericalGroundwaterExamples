'''
BoundaryElement is essentially a helper class that is the base of all
boundaries. We use BoundarElement to hold the geometry of the domain.
'''

import numpy as np

class BoundaryElement(object):

    def __init__(__self__, Index, Face, Center, AdjacentCells, Areas, Distances):

        __self__.Index = Index
        __self__.Face = Face
        __self__.FaceLayout = ['0: Left\n1: Right\n2: Front\n3: Back\n' \
            '4: Bottom\n5: Top\n-99: In-Domain Source']
        __self__.Center = Center
        __self__.AdjacentCells = AdjacentCells
        __self__.Areas = Areas
        __self__.Lengths = Distances