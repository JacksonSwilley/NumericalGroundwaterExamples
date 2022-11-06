'''
Abstract Base Class for Boundary classes. Will be used by 
configuration on instantiation.
'''

from Meta import Meta

class Boundary(metaclass=Meta):

    BoundaryElements = None
    BoundaryConditons = None
    
    def CheckAttributes(__self__):

        if __self__.BoundaryElements is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryElements attribute.')
        
        if __self__.BoundaryConditons is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryConditions attribute.')