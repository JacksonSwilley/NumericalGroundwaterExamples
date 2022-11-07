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

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Conductivity(j) / element.Length(j)**(2)
            
                Matrix[i, i] = -2 * np.sum(Matrix[i, :])
        
            for boundary in Configuration.Boundary.Elements:
                for j in boundary.AdjacentCells:
                    Matrix[j,j] += - boundary.Coefficient * element.Conductivity(j) / element.Length(j)**(2)
                    Solution[j] += - boundary.Head * element.Conductivity(j) / element.Length(j)**(2) + \
                        boundary.Flux / boundary.Volume(j)

        elif(State == None):
            raise RuntimeError(
                'Transient solutions require an initial condition but no state was provided')

        else:
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Conductivity(j) / element.Length(j)**(2)
            
                Matrix[i, i] = -2 * np.sum(Matrix[i, :]) - element.Storage / dt
                Solution[i] = -State.Data[i] * element.Storage / dt
        
            for boundary in Configuration.Boundary.Elements:
                for j in boundary.AdjacentCells:
                    Matrix[j,j] += - boundary.Coefficient * element.Conductivity(j) / element.Length(j)**(2)

                    Solution[j] += - boundary.Head * element.Conductivity(j) / element.Length(j)**(2) + \
                        boundary.Flux / boundary.Volume(j)

        return Matrix, Solution