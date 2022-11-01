'''
This is a concrete subclass of Method, that creates a finite difference method matrix
for a regular grid and paramters that can change with state.
'''
class RegularFDM(Method):
    def BuildMatrix(__self__, Configuration):

        if Configuration.Domain.Regular != True:
            raise TypeError(
                'RegularFDM, regular finite difference method, requires a regular\n'
                'grid. Reconfigure to regular domain or use IrregularFVM.')

        n = Configuration.Domain.Count

        Matrix = np.zeros((n,n))

        if(Configuration.ChangeInTime() == 0):
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = element.Conductivity[j] / element.Length[j]**(2)
            
                Matrix[i, i] = -2 * np.sum(Matrix[i, :])

        else:
            for i in range(n):
                element = Configuration.Domain.Elements[i]

                for j in  element.AdjacentCells:

                    Matrix[i, j] = -Configuration.ChangeInTime() * element.Conductivity[j] / element.Length[j]**(2)
            
                Matrix[i, i] = -2 * np.sum(Matrix[i, :]) + 1

        return Matrix