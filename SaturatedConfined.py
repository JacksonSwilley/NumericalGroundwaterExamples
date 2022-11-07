'''
Simplest concrete configuration class. Interface areas and aquifer
properties are constant.
'''

from Configuration import Configuration
from Domain import Domain
from Boundary import Boundary
from TimingInfo import TimingInfo

class SaturatedConfined(Configuration):

    def __init__(__self__, Domain: Domain, \
        Boundary: Boundary, \
        TimingInfo: TimingInfo):
        
        __self__.Domain = Domain
        __self__.Boundary = Boundary
        __self__.TimingInfo = TimingInfo

    def UpdateDomain(__self__, State=None):
        return super().UpdateDomain(State)
    
    def UpdateBoundary(__self__, State=None):
        return super().UpdateBoundary(State)