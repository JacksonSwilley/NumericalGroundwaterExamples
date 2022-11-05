'''
Abstract Base Class for domains, which hold the grid and its input
parameters in a distributed fashion.
'''
from Meta import Meta

class Domain(metaclass = Meta):

    Elements = None
    Count = None
    Shape = None
    Regular = False

    def CheckAttributes(__self__):

        if __self__.Elements is None:
            raise NotImplementedError(
                'Subclass must define __self__.Elements attribute.')

        if __self__.Count is None:
            raise NotImplementedError(
                'Subclass must define __self__.Count attribute.')
        
        if __self__.Shape is None:
            raise NotImplementedError(
                'Subclass must define __self__.Shape attribute.')