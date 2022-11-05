'''
Abstract Base Class for Nodes
'''
from Meta import Meta

class Nodes(metaclass = Meta):

    Points = None

    def CheckAttributes(__self__):
        if __self__.Points is None:
            raise NotImplementedError(
                'Subclass must define __self__.Points attribute.')