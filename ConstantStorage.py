'''
Storage term that is not dependent on space or saturation.
i.e. there is no accounting for dewatering.
'''

from Storage import Storage
class HomognousStorage(Storage):
    def __init__(__self__, Value):
        __self__.Value = Value
    
    def ReturnS(__self__  ,X=None, Y=None, Z=None, Saturation=None):
        return __self__.Value