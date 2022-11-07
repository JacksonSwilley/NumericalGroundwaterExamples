'''
This is anabstract base class that specifies the requirements of a "Method" class,
"Method" as in numerical method, not a code-function
'''

from Meta import Meta

class Method(metaclass = Meta):

    BuildMatrices = None

    def CheckAttributes(__self__):
        if __self__.BuildMatrices is None:
            raise NotImplementedError(
                'Subclass must define __self__.BuildMatrices method.')