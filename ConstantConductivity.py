'''
A single value for hydraulic condictivity indepent of direction
space, or saturation
'''

from Conductivity import Conductivity
class ConstantConductivity(Conductivity):
    def __init__(__self__, Value):
        __self__.Value = Value
    
    def ReturnK(__self__, X=None, Y=None, Z=None, Saturation=None):
        return [__self__.Value, __self__.Value, __self__.Value,]