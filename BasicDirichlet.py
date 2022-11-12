'''
A boundary condition
'''

from BoundaryCondition import BoundaryCondition
from BoundaryElement import BoundaryElement

class BasicDirichlet(BoundaryCondition):

    def __init__(__self__, Faces:list, Heads:list):

        assert len(Faces) == len(Heads)
        __self__.Faces = Faces
        __self__.Coefficients = [0, 0, 0, 0, 0, 0]
        __self__.Heads = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        __self__.Fluxes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        ticker = 0
        for i in Faces:
            __self__.Heads[i] = Heads[ticker]
            __self__.Coefficients[i] = 1
            ticker = ticker + 1
    
    def ApplyBC(__self__, BoundaryElement: BoundaryElement):

        Face = BoundaryElement.Face

        BoundaryElement.Coefficient = BoundaryElement.Coefficient + __self__.Coefficients[Face]
        BoundaryElement.Head = BoundaryElement.Head + __self__.Heads[Face]
        BoundaryElement.Flux = BoundaryElement.Flux + __self__.Fluxes[Face]