'''
This is a concrete subclass of Method, that creates a finite volume method matrix
for an irregular grid and paramters that can change with state
'''

from Method import Method
from Configuration import Configuration
from State import State
import numpy as np

class IrregularFVM(Method):

    def BuildMatrices(__self__, Configuration:Configuration, \
        State:State=None):

        n = Configuration.Domain.Count
        dt = Configuration.TimingInfo.StepSize

        Matrix = np.zeros((n,n))
        Solution = np.zeros((n,1))

        if(dt == 0):
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in range(6):
                    if element.AdjacentCells[j] >= 0:
                        Matrix[i, j] = element.Areas[j] * element.Conductivities[j] / element.Lengths[j]        
                Matrix[i, i] = -np.sum(Matrix[i, :])

            for boundary in Configuration.Boundary.Elements:
                j = int(boundary.AdjacentCells)
                face = boundary.Face
                Matrix[j,j] = Matrix[j,j] - boundary.Coefficient * element.Areas[face] * element.Conductivities[face] / element.InsideLengths[face]
                Solution[j] = Solution[j] - boundary.Head * element.Areas[face] * element.Conductivities[face] / element.InsideLengths[face] + \
                    boundary.Flux

        elif(State == None):
            raise RuntimeError(
                'Transient solutions require an initial condition but no state was provided')
            
        else:
            t = State.TimeIndex
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in range(6):
                    if element.AdjacentCells[j] >= 0:
                        Matrix[i, j] = element.Area[j] * element.Conductivities[j] / element.Lengths[j]
            
                Matrix[i, i] = -np.sum(Matrix[i, :]) - element.Storage * element.Volume / dt
                Solution[i] = -State.Data[i] * element.Storage * element.Volume / dt
            
            for boundary in Configuration.Boundary.Elements:
                j = int(boundary.AdjacentCells)
                face = boundary.Face
                Matrix[j,j] = Matrix[j,j] - boundary.Coefficient[t] * element.Areas[face] * element.Conductivities[face] / element.InsideLengths[face]
                Solution[j] = Solution[j] - boundary.Head[t] * element.Areas[face] * element.Conductivities[face] / element.InsideLengths[face] + \
                    boundary.Flux[t] 

        return Matrix, Solution