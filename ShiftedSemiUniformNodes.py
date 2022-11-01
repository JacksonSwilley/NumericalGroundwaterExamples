'''
Approximately uniform nodes but shifted by 1/2 increment on one axis
'''
class ShiftedSemiUniformNodes(Nodes):

    def __init__(__self__, Bounds, Dimensions):
        __self__.Bounds = Bounds
        __self__.Dimensions =  Dimensions
        
        Y, X = np.mgrid[Bounds[0]:Bounds[1]:Dimensions[0]*1j,
        Bounds[0]:Bounds[1]:Dimensions[0]*1j]
            
        shift =  (X[0, 1] - X[0,0]) / 2
        X[::2] = X[::2] + shift

        __self__.Points = np.array([X.flatten(order='C'), Y.flatten(order='C')]).T