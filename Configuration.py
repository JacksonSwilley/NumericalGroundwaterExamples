'''
Abstract Base Class for configurations, which hold the domain and update it
depending on the problem type. In the context of groundwater this could be
 confined versus unconfined, variable saturation, etc.
'''
from Meta import Meta

class Configuration(metaclass = Meta):

    TimingInfo = None
    Domain = None
    Boundary = None

    def UpdateDomain(__self__, State=None):
        pass

    def UpdateBoundary(__self__, State=None):
        pass

    def CheckAttributes(__self__):

        if __self__.TimingInfo is None:
            raise NotImplementedError(
                'Subclass must define __self__.TimingInfo attribute.')

        if __self__.Domain is None:
            raise NotImplementedError(
                'Subclass must define __self__.Domain attribute.')
        
        if __self__.Boundary is None:
            raise NotImplementedError(
                'Subclass must define __self__.Boundary attribute.')