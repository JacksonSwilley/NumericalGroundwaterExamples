'''
Helper object for handing model results
'''

from Configuration import Configuration
from State import State
import numpy as np
import matplotlib.pyplot as plt

class Results(object):

    def __init__(__self__, Configuration: Configuration):

        __self__.Shape = (int(Configuration.Domain.Count), \
            int(Configuration.TimingInfo.NumberOfSteps))
        
        __self__.Data = np.zeros((__self__.Shape[0],__self__.Shape[1]) )

        __self__.X = [0] * Configuration.Domain.Count
        __self__.Y = [0] * Configuration.Domain.Count
        __self__.Z = [0] * Configuration.Domain.Count

        for i in range(Configuration.Domain.Count):
            __self__.X[i] = Configuration.Domain.Elements[i].Center[0]
            __self__.Y[i] = Configuration.Domain.Elements[i].Center[1]
            __self__.Z[i] = Configuration.Domain.Elements[i].Center[2]
        
        __self__.Configuration = Configuration

    
    def ProvideData(__self__, State: State):
        __self__.Data[:, State.TimeIndex] = State.Data.flatten()

    def Show(__self__, Layer=0, Time=0):

        nx = __self__.Configuration.Domain.Shape[0]
        ny = __self__.Configuration.Domain.Shape[1]
        nz = __self__.Configuration.Domain.Shape[2]

        if nz <= 1:

            x = np.reshape(__self__.X,(nx,ny,nz),order='F')[:,:,0]
            y = np.reshape(__self__.Y,(nx,ny,nz),order='F')[:,:,0]
            h = np.reshape(__self__.Data,(nx,ny,nz),order='F')[:,:,0]

            plt.figure(dpi=300, figsize=(10,4))
            ax = plt.axes(projection='3d')
            ax.plot_surface(x,y,h, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
        
            plt.show()
        
        if nz > 1:

            x = np.reshape(__self__.X,(nx,ny,nz),order='F')[:,:,0]
            y = np.reshape(__self__.Y,(nx,ny,nz),order='F')[:,:,0]
            h = np.reshape(__self__.Data,(nx,ny,nz),order='F')[:,:,0]


            fig = plt.figure(dpi=300, figsize=(12,6))

            ax = fig.add_subplot(1, 2, 1, projection='3d')
            ax.plot_surface(x,y,h, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
            ax.set_title('Hydraulic Head: Top Layer')

            h = np.reshape(__self__.Data,(nx,ny,nz),order='F')[:,:,-1]

            ax = fig.add_subplot(1, 2, 2, projection='3d')
            ax.plot_surface(x,y,h, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
            ax.set_title('Hydraulic Head: Bottom Layer')
            plt.colorbar
            plt.tight_layout
            plt.show
            
