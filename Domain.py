'''
Abstract Base Class for domains, which hold the grid and its input
parameters in a distributed fashion.
'''
class Domain(metaclass = Meta):

    Count = None
    Elements = None
    UpdateElements = None

    def CheckAttributes(__self__):
        if __self__.Count is None:
            raise NotImplementedError(
                'Subclass must define __self__.Count attribute.')
        
        if __self__.Elements is None:
            raise NotImplementedError(
                'Subclass must define __self__.Elements attribute.')

        if __self__.UpdateElements is None:
            raise NotImplementedError(
                'Subclass must define __self__.UpdateElements attribute.')