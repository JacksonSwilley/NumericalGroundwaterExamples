'''
Abstract Base Class for configurations, which hold the domain and update it
depending on the problem type. In the context of groundwater this could be
 confined versus unconfined, variable saturation, etc.
'''
class Configuration(metaclass = Meta):

    ChangeInTime = None
    Domain = None
    BoundaryCondition = None

    def CheckAttributes(__self__):

        if __self__.ChangeInTime is None:
            raise NotImplementedError(
                'Subclass must define __self__.ChangeInTime attribute.')

        if __self__.Domain is None:
            raise NotImplementedError(
                'Subclass must define __self__.Domain attribute.')
        
        if __self__.BoundaryCondition is None:
            raise NotImplementedError(
                'Subclass must define __self__.BoundaryCondition attribute.')