'''
A boundary condition
'''

from BoundaryCondition import BoundaryCondition

class BasicDirichlet(BoundaryCondition):

    def __init__(__self__, Faces:list, Heads:list):

        assert len(Faces) == len(Heads)
        __self__.Faces = Faces
        __self__.Coefficients = [0, 0, 0, 0, 0, 0]
        __self__.Heads = [0, 0, 0, 0, 0, 0]
        __self__.Fluxes = [0, 0, 0, 0, 0, 0]

        ticker = 0
        for i in Faces:
            __self__.Heads[i] = Heads[ticker]
            __self__.Coefficients[i] = 1
            ticker = ticker + 1
    
    def ReturnBC(__self__, Face):

        return [__self__.Coefficients[Face], \
            __self__.Heads[Face], __self__.Fluxes[Face]]