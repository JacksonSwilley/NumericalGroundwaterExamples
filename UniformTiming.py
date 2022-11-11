'''
Concrete Base Class of TimingInfo. Generates
a TimingInfo Object with a uniform time step.
'''

from TimingInfo import TimingInfo
import numpy as np

class UniformTiming(TimingInfo):

    def __init__(__self__, StartTime=0, StepSize=0, NumberOfSteps=1):
        __self__.StepSize = StepSize
        __self__.StartTime = StartTime
        __self__.NumberOfSteps = NumberOfSteps
        __self__.Time = np.linspace(StartTime, \
            StartTime + StepSize * (NumberOfSteps), num=NumberOfSteps+1)