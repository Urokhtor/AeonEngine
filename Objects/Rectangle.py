from AeonEngine.Objects.Positional import Positional
from AeonEngine.Objects.TwoDimensional import TwoDimensional
from AeonEngine.Objects.Fillable import Fillable

class Rectangle(Positional, TwoDimensional, Fillable):
    
    def __init__(self, x = 0, y = 0, w = 0, h = 0, filled = False):
        Positional.__init__(self, x, y)
        TwoDimensional.__init__(self, w, h)
        Fillable.__init__(self, filled)