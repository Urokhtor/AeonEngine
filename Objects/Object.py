from AeonEngine.Objects.Positional import Positional
from AeonEngine.Objects.Rectangle import Rectangle

class Object(Positional):
    """
        Generic base for all the game's objects including entities and items.
    """
    
    def __init__(self):
        Positional.__init__(self)
        self.id = 0
        self.name = "Object"
        self.boundingRectangle = Rectangle()
        self.speed = 100 # Should we have separate x and y speed, perhaps in own class?
        
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def update(self, cumTime):
        self.move(self.speed * cumTime/1000, self.speed * cumTime/1000)
        self.boundingRectangle.move(self.speed * cumTime/1000, self.speed * cumTime/1000)
    
    def render(self, cumTime, renderer):
        renderer.render(self.boundingRectangle)