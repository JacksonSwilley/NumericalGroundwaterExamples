'''
A boundary Condition
'''

from BoundaryCondition import BoundaryCondition
from BoundaryElement import BoundaryElement

class BasicNeumann(BoundaryCondition):

    def __init__(__self__, Faces:list, Fluxes:list):

        assert len(Faces) == len(Fluxes)
        __self__.Faces = Faces
        __self__.Coefficients = [0, 0, 0, 0, 0, 0]
        __self__.Heads = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        __self__.Fluxes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        ticker = 0
        for i in Faces:
            __self__.Fluxes[i] = Fluxes[ticker]
            ticker = ticker + 1
    
    def ApplyBC(__self__, BoundaryElement: BoundaryElement):

        Face = BoundaryElement.Face

        BoundaryElement.Coefficient = BoundaryElement.Coefficient + __self__.Coefficients[Face]
        BoundaryElement.Head = BoundaryElement.Head + __self__.Heads[Face]
        BoundaryElement.Flux = BoundaryElement.Flux + __self__.Fluxes[Face]