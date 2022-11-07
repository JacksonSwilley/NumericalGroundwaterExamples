'''
Abstract Base Class for Boundary classes. Will be used by 
configuration on instantiation.
'''

from Meta import Meta

class Boundary(metaclass=Meta):

    Elements = None
    
    def CheckAttributes(__self__):

        if __self__.Elements is None:
            raise NotImplementedError(
                'Subclass must define __self__.Elements attribute.')