
'''
An abstract base class that requires all concrete subclasses to have a
method for stepping forward once
'''

from Meta import Meta

class Scheme(metaclass = Meta):
    
    Step = None
    NumberOfInitialConditions = 1

    def CheckAttributes(__self__):
        if __self__.Step is None:
            raise NotImplementedError(
                'Subclass must define __self__.Step method.')