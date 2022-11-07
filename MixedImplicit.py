'''
This scheme solves for hydraulic head implicitly but updates
input paramters explicitly.
'''

from Scheme import Scheme
from Configuration import Configuration
from Method import Method
from State import State
from Solver import Solver

class MixedImplicit(Scheme):

    def Step(__self__, Configuration: Configuration, Method: Method, \
        Solver: Solver, State: State):

        Configuration.UpdateDomain(State)
        Configuration.UpdateBoundary(State)

        Coefficients, Solution = Method.BuildMatrices(Configuration, State)

        Coefficents = Solver.InvertMatrix(Coefficients)

        State.Update(Coefficents @ Solution, Configuration)