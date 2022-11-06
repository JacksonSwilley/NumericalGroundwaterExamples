'''
A Domain subclass that creates a domain given a grid,
Storage, and Conductivity.
'''

from Domain import Domain
from Grid import Grid
import numpy as np

class GriddedDomain(Domain):

    def __init__(__self__, Grid, Storage, Conductivity):

        __self__.Count = Grid.Count
        __self__.Elements = Grid.Elements