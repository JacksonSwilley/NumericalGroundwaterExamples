'''
Abstract Base Class for boundary conditions, all of which have a
grid and a method for applying bouundary conditions to create a matrix
of solutions
'''

from Meta import Meta

class BoundaryCondition(metaclass = Meta):

    ApplyBC = None

    def CheckAttributes(__self__):
        if __self__.ApplyBC == None:
            raise NotImplementedError(
                    'Subclass must define __self__.ApplyBC Method.')