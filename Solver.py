'''
Abstract Base Class for Solvers
'''

from Meta import Meta

class Solver(metaclass=Meta):

    InvertMatrix = None

    def CheckAttributes(__self__):
        if __self__.InvertMatrix is None:
            raise NotImplementedError(
                'Subclass must define __self__.InvertMatirx method.')