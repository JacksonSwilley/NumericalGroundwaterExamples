'''
Abstract Base Class for boundary conditions, all of which have a
grid and a method for applying bouundary conditions to create a matrix
of solutions
'''
from Meta import Meta
class BoundaryCondition(metaclass = Meta):

    BoundaryCondition = None

    def CheckAttributes(__self__):
        raise NotImplementedError(
                'Subclass must define __self__.BoundaryCondition attribute.')