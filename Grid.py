'''
Abstract Base Class for grids
'''

from Meta import Meta

class Grid(metaclass = Meta):

    Count = None
    Index = None
    Elements = None
    BoundaryCount = None
    BoundaryIndex = None
    BoundaryElements = None
    Show = None
    
    def CheckAttributes(__self__):
        if __self__.Count is None:
            raise NotImplementedError(
                'Subclass must define __self__.Count attribute.')

        if __self__.Count is None:
            raise NotImplementedError(
                'Subclass must define __self__.Count attribute.')

        if __self__.Elements is None:
            raise NotImplementedError(
                'Subclass must define __self__.Elements attribute.')
        
        if __self__.BoundaryCount is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryCount attribute.')

        if __self__.BoundaryIndex is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryIndex attribute.')

        if __self__.BoundaryElements is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryElements attribute.')
        
        if __self__.Show is None:
            raise NotImplementedError(
                'Subclass must define __self__.Show method.')