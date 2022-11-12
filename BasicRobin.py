'''
A boundary Condition
'''

from BoundaryCondition import BoundaryCondition
from BoundaryElement import BoundaryElement
import numpy as np

class BasicRobin(BoundaryCondition):

    def __init__(__self__, Faces:list, Heads: list, \
        Conductivities: list, Lengths: list):

        assert len(Faces) == len(Heads)
        assert len(Faces) == len(Conductivities)
        assert len(Faces) == len(Lengths)
        __self__.Faces = Faces
        __self__.Coefficients = [0, 0, 0, 0, 0, 0]
        __self__.Heads = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        __self__.Conductivities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        __self__.Lengths = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        ticker = 0
        for i in Faces:
            __self__.Coefficients[i] = 1
            __self__.Heads[i] = Heads[ticker]
            __self__.Conductivities[i] = Conductivities[ticker]
            __self__.Lengths[i] = Lengths[ticker]

            ticker = ticker + 1
  
    def ApplyBC(__self__, BoundaryElement: BoundaryElement):

        Face = BoundaryElement.Face

        if Face in set(__self__.Faces):
            BoundaryElement.Coefficient = BoundaryElement.Coefficient + __self__.Coefficients[Face]
            BoundaryElement.Head = BoundaryElement.Head + __self__.Heads[Face]
            BoundaryElement.Conductivities[Face] = (BoundaryElement.Length + __self__.Lengths[Face]) \
                / (BoundaryElement.Length / BoundaryElement.Conductivities[Face] + \
                __self__.Lengths[Face] / __self__.Conductivities[Face])

            BoundaryElement.Length = BoundaryElement.Length + __self__.Lengths[Face]