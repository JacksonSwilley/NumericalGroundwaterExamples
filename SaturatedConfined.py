'''
Simplest concrete configuration class. Interface areas and aquifer
properties are constant.
'''
class SaturatedConfined(Configuration):

    def __init__(__self__, Domain, Boundary, TimingInfo):
        __self__.Domain = Domain
        __self__.Boundary = Boundary
        __self__.TimingInfo = TimingInfo