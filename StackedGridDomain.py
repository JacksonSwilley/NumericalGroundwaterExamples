class StackedGridDomain(Domain):

    def __init__(__self__, Grid, Storage, Conductivity, Thickness=[1]):

        layers = len(Thickness)

        __self__.Count = Grid.Count * layers
        __self__.Elements = [Element] * __self__.Count

        for i in range(__self__.Count):
            __self__.Elements[i] = Element(i, Storage, Conductivity, Grid, Thickness)

        for element in __self__.Elements:
            for i in element.AdjacentCells:
                