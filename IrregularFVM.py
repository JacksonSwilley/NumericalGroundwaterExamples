'''
This is a concrete subclass of Method, that creates a finite volume method matrix
for an irregular grid and paramters that can change with state
'''
class IrregularFVM(Method):

    def BuildMatrices(__self__, Configuration, State=None):

        n = Configuration.Domain.Count
        dt = Configuration.TimingInfo.StepSize

        Matrix = np.zeros((n,n))
        Solution = np.zeros((n,1))

        if(dt == 0):
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Area(j) * element.Conductivity(j) / element.Length(j)
            
                Matrix[i, i] = -np.sum(Matrix[i, :])

            for boundary in Configuration.Boundary.Elements:

                for j in boundary.AdjacentCells:
                    Matrix[j,j] += - boundary.Coefficient * element.Area(j) * element.Conductivity(j) / element.Length(j)
                    Solution[j] += - boundary.Head * element.Area(j) * element.Conductivity(j) / element.Length(j) + \
                        boundary.Flux

        elif(State == None):
            raise RuntimeError(
                'Transient solutions require an initial condition but no state was provided')
            
        else:
            t = State.TimeIndex
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Area(j) * element.Conductivity(j) / element.Length(j)
            
                Matrix[i, i] = -np.sum(Matrix[i, :]) - element.Storage * element.Volume / dt
                Solution[i] = -State.Data[i] * element.Storage * element.Volume / dt
            
            for boundary in Configuration.Boundary.Elements:

                for j in boundary.AdjacentCells:
                    Matrix[j,j] += - boundary.Coefficient[t] * element.Area(j) * element.Conductivity(j) / element.Length(j)
                    Solution[j] += - boundary.Head[t] * element.Area(j) * element.Conductivity(j) / element.Length(j) + \
                        boundary.Flux[t] 

        return Matrix, Solution

        