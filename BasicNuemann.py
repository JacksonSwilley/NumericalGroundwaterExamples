'''
A boundary Condition
'''

from BoundaryCondition import BoundaryCondition

class BasicNeumann(BoundaryCondition):

    def __init__(__self__, Faces:list, Fluxes:list):

        assert len(Faces) == len(Fluxes)
        __self__.Faces = Faces
        __self__.Coefficients = [0, 0, 0, 0, 0, 0]
        __self__.Heads = [0, 0, 0, 0, 0, 0]
        __self__.Fluxes = [0, 0, 0, 0, 0, 0]

        ticker = 0
        for i in Faces:
            __self__.Fluxes[i] = Fluxes[ticker]
            ticker = ticker + 1
    
    def ReturnBC(__self__, Face):

        return [__self__.Coefficients[Face], \
            __self__.Heads[Face], __self__.Fluxes[Face]]