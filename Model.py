'''
Oh yeah babyyyyyy! This is how the sausage gets made son!
'''

from Configuration import Configuration
from Scheme import Scheme
from Method import Method
from Solver import Solver
from Results import Results
from State import State
import time

class Model(object):

    def __init__(__self__, Configuration: Configuration, \
            Scheme: Scheme, Method: Method, Solver: Solver):
        __self__.Configuration = Configuration
        __self__.Scheme = Scheme
        __self__.Method = Method
        __self__.Solver = Solver
        __self__.Results = Results(Configuration)
        __self__.RunTime = []

    def Simulate(__self__, State: State):

        NumberOfSteps = __self__.Configuration.TimingInfo.NumberOfSteps

        StartTime = time.time()

        __self__.Results.ProvideData(State)

        for i in range(NumberOfSteps):
            __self__.Scheme.Step(__self__.Configuration, __self__.Method, __self__.Solver, State)
            
            __self__.Results.ProvideData(State)
        
        __self__.RunTime.append(time.time() - StartTime)