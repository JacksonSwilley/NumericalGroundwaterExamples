'''
Abstract Base class for storage. All Stroages subclasses
must return a storage if provided with a point in sapce.
'''

from Meta import Meta

class Storage(metaclass=Meta):

        ReturnS = None

        def CheckAttributes(__self__):
            if __self__.ReturnS is None:
                raise NotImplementedError(
                    'Subclass must define __self__.ReturnS Method.')