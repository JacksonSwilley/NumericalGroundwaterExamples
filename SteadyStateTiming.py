'''
Concrete subclass of TimingInfo used to provide
the necessary time information for steady-state
simulations.
'''

from TimingInfo import TimingInfo

class SteadyStateTiming(TimingInfo):

    def __init__(__self__):
        __self__.StepSize = 0
        __self__.StartTime = 0
        __self__.NumberOfSteps = 1
        __self__.Time = __self__.StartTime