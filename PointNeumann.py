'''
A source
'''
from Source import Source
from Element import Element

class PointNeumann(Source):
    def __init__(__self__, Range, Flux):
        __self__.Range = Range
        __self__.Flux = Flux
    
    def ApplySource(__self__, Element: Element):

        x = Element.Center[0]
        y = Element.Center[1]
        z = Element.Center[2]

        if x >= __self__.Range[0] and x <= __self__.Range[1]:
            if y >= __self__.Range[2] and y <= __self__.Range[3]:
                if z >= __self__.Range[4] and z <= __self__.Range[5]:
                    Element.Source = Element.Source + __self__.Flux