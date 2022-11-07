'''
Helper object for handing model results
'''

from Configuration import Configuration
from State import State
import numpy as np

class Results(object):

    def __init__(__self__, Configuration: Configuration):

        __self__.Shape = (int(Configuration.Domain.Count), \
            int(Configuration.TimingInfo.NumberOfSteps))
        
        __self__.Data = np.zeros((__self__.Shape[0],__self__.Shape[1]) )
    
    def ProvideData(__self__, State: State):
        __self__.Data[:, State.TimeIndex] = State.Data.flatten()

