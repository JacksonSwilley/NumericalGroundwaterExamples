'''
Abstract Base Class for Conductivity. All concrete
subclasses must return K given a location.
'''

from Meta import Meta

class Conductivity(metaclass=Meta):

        ReturnK = None

        def CheckAttributes(__self__):
            if __self__.ReturnK is None:
                raise NotImplementedError(
                    'Subclass must define __self__.ReturnK Method.')