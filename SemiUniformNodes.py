'''
Approximately uniform nodes
'''
class SemiUniformNodes(Nodes):

    def __init__(__self__, Bounds, Dimensions):
        __self__.Bounds = Bounds
        __self__.Dimensions =  Dimensions

        Y, X = np.mgrid[Bounds[0]:Bounds[1]:Dimensions[0]*1j, 
            Bounds[0]:Bounds[1]:Dimensions[0]*1j]

        __self__.Points = np.array([X.flatten(order='C'), Y.flatten(order='C')]).T