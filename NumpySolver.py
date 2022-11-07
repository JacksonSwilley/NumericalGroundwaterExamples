'''
Simplest concrete subclass of solver.
Just a wrapped version of np.linalg.inv()
'''

from Solver import Solver
from numpy.linalg import inv

class NumpySolver(Solver):

    def __init__(__self__):
        pass
    
    def InvertMatrix(__self__, Coefficients):
        return inv(Coefficients)

