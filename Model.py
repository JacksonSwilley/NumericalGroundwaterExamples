class Model(metaclass = Meta):

    def __init__(__self__, Configuration, Scheme, Method, Solver):
        __self__.Configuration = Configuration
        __self__.Scheme = Scheme
        __self__.Method = Method
        __self__.Solver = Solver
        __self__.Results = Results(Configuration)
        __self__.RunTime = None

    def Simulate(__self__, State):
        if State.Shape[0] != __self__.Results.shape[0]:
            raise AttributeError('State is incompatible with Domain.\n'
                'Check the number of elements in the domain and state.')

        if State.Shape[1] != __self__.Scheme.NumberOfInitialConditions:
            raise AttributeError('State is incompatible with Scheme.\n'
                'Check required number of initial conditions for scheme.')

        NumberOfSteps = __self__.Configuration.RunLength
        NumberOfICs = __self__.Scheme.NumberOfInitialConditions

        StartTime = time.time()

        __self__.Results[:, :, :, 0:NumberOfICs] = State

        for i in range(NumberOfSteps):
            __self__.Scheme.Step(
                __self__.Configuration, 
                __self__.Method,
                __self__.Solver,
                State)
            
            __self__.Results[:, :, :, i + NumberOfICs] = State
        
        __self__.RunTime.append(time.time() - StartTime)