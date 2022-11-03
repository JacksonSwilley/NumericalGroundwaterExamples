'''
This scheme solves for hydraulic head implicitly but updates
input paramters explicitly.
'''
from Scheme import Scheme

class MixedImplicit(Scheme):

    def Step(Configuration, Method, Solver, State):

        Configuration.UpdateDomain(State)
        Configuration.UpdateBoundary(State)

        Coefficients, Solution = Method.BuildMatrices(Configuration, State)

        Coefficents = Solver.InvertMatrix(Coefficients)

        State.Update(Coefficents @ Solution, Configuration)