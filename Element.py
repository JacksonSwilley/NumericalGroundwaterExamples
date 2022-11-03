'''
Element is essentially a helper class that is the base of all domains.
We use Element to hold the physical properties of the domain.
'''
class Element(object):

    def __init__(__self__, Index, Storage, Conductivity, Grid, Thickness):

        __self__.Index = Index
        __self__.Areas = Grid.Sidewidths[Index,:] * Thickness
        __self__.AdjacentCells = Grid.AdjacentCells[Index,:]
        __self__.Lengths = Grid.Distances[Index,:]
        __self__.Conductivity = Conductivity
        __self__.Storage = Storage
        __self__.InsideLengths = Grid.InsideLengths[Index]
        __self__.Volume = Grid.Areas[Index] * Thickness
    
    def Area(__self__, Locator):
        return __self__.Areas[np.where(__self__.AdjacentCells == Locator)]

    def Length(__self__, Locator):
        return __self__.Length[np.where(__self__.AdjacentCells == Locator)]
    
    def Conductivity(__self__, Locator):
        return __self__.Conductivity[np.where(__self__.AdjacentCells == Locator)]