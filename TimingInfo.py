'''
Abstract Base Class for timing information. Forces subclasses
to have required attributes
'''
from Meta import Meta

class TimingInfo(metaclass = Meta):

    StepSize = None
    StartTime = None
    NumberOfSteps = None

    def CheckAttributes(__self__):

        if __self__.StepSize is None:
            raise NotImplementedError(
                'Subclass must define __self__.StepSize attribute.')

        if __self__.StartTime is None:
            raise NotImplementedError(
                'Subclass must define __self__.StartTime attribute.')
        
        if __self__.NumberOfSteps is None:
            raise NotImplementedError(
                'Subclass must define __self__.NumberOfSteps attribute.')