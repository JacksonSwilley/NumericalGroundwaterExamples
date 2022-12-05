'''
State is a concrete class used to store the dependent variable
at the current time step, as well as the the current time
'''

from Configuration import Configuration

class State(object):

    def __init__(__self__, Data, Configuration: Configuration):

        __self__.TimeIndex = 0

        __self__.CurrentTime = Configuration.TimingInfo.Time[__self__.TimeIndex]

        if len(Data) == Configuration.Domain.Count:
            __self__.Data = Data
        else :
            raise RuntimeError(
                'Initial condition must be specified for every element\n'
                'in the domain.')


    def Update(__self__, Data, Configuration):

        if(Configuration.TimingInfo.StepSize) > 0:
            __self__.TimeIndex = __self__.TimeIndex + 1
            __self__.CurrentTime = Configuration.TimingInfo.Time[__self__.TimeIndex]
            


        if len(Data) == Configuration.Domain.Count:
            __self__.Data = Data
        else :
            raise RuntimeError(
                'State must be specified for every element in the domain.')