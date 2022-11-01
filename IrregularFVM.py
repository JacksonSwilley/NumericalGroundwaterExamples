'''
This is a concrete subclass of Method, that creates a finite volume method matrix
for an irregular grid and paramters that can change with state
'''
class IrregularFVM(Method):

    def BuildMatrix(__self__, Configuration):

        n = Configuration.Domain.Count

        Matrix = np.zeros((n,n))

        if(Configuration.ChangeInTime == 0):
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Area[j] * element.Conductivity[j] / element.Length[j]
            
                Matrix[i, i] = -np.sum(Matrix[i, :])

        else:
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = -Configuration.ChangeInTime() * element.Area[j] * element.Conductivity[j] / element.Length[j]
            
                Matrix[i, i] = -np.sum(Matrix[i, :]) + 1

        return Matrix