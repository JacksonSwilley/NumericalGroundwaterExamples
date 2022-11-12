'''
This is a concrete subclass of Method, that creates a finite difference method matrix
for a regular grid and paramters that can change with state.
'''

from Method import Method
from Configuration import Configuration
from State import State
import numpy as np

class RegularFDM(Method):

    def BuildMatrices(__self__, Configuration:Configuration, \
        State:State=None):

        if Configuration.Domain.Regular != True:
            raise TypeError(
                'RegularFDM, regular finite difference method, requires a regular\n'
                'grid. Reconfigure to regular domain or use IrregularFVM.')

        n = Configuration.Domain.Count
        dt = Configuration.TimingInfo.StepSize

        Matrix = np.zeros((n,n))
        Solution = np.zeros((n,1))

        if(dt == 0):
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                Solution[i] = Solution[i] - element.Source

                for j in range(6):
                    if element.AdjacentCells[j] >= 0:
                        Matrix[i, int(element.AdjacentCells[j])] \
                            = element.Conductivities[j] / (element.Lengths[j] * element.InsideLengths[j] * 2)
            
                Matrix[i, i] = -np.sum(Matrix[i, :])
        
            for boundary in Configuration.Boundary.Elements:
                j = int(boundary.AdjacentCell)
                face = boundary.Face

                Matrix[j,j] = Matrix[j,j] -  boundary.Coefficient * boundary.Conductivities[face] / boundary.Length**(2)
                Solution[j] = Solution[j] - boundary.Head * boundary.Conductivities[face] / boundary.Length**(2) - \
                    boundary.Flux * boundary.Area / element.Volume

        elif(State == None):
            raise RuntimeError(
                'Transient solutions require an initial condition but no state was provided')

        else:
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                Solution[i] = Solution[i] - element.Source

                for j in range(6):
                    if element.AdjacentCells[j] >= 0:
                        
                        Matrix[i, int(element.AdjacentCells[j])] \
                            = element.Conductivities[j] / (element.Lengths[j] * element.InsideLengths[j] * 2)
            
                Matrix[i, i] = - np.sum(Matrix[i, :]) - element.Storage / dt
                Solution[i] = Solution[i] - State.Data[i] * element.Storage / dt
        
            for boundary in Configuration.Boundary.Elements:
                j = int(boundary.AdjacentCell)
                face = boundary.Face

                Matrix[j,j] =  Matrix[j,j] -  boundary.Coefficient * element.Conductivities[face] / boundary.Length**(2)
                Solution[j] = Solution[j] - boundary.Head * element.Conductivities[face] / boundary.Length**(2)  - \
                    boundary.Flux * boundary.Area / element.Volume

        return Matrix, Solution