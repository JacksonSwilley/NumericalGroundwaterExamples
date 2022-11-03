'''
This is anabstract base class that specifies the requirements of a "Method" class,
"Method" as in numerical method, not a code-function
'''
class Method(metaclass = Meta):

    BuildMatrix = None
    BuildSolution = None

    def CheckAttributes(__self__):
        if __self__.BuildMatrix is None:
            raise NotImplementedError(
                'Subclass must define __self__.BuildMatrix method.')
        
        if __self__.BuildSolution is None:
            raise NotImplementedError(
                'Subclass must define __self__.BuildSolution method.')