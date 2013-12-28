from AeonEngine.Base.Vector2f import Vector2f

class Positional:
    
    def __init__(self, x = 0, y = 0, vector = None):
        self.position = None
        
        if vector is not None:
            self.position = Vector2f(vector=vector)
        
        else:
            self.position = Vector2f(x, y)
        
    def setPosition(self, x, y):
        self.position.values[0] = x
        self.position.values[1] = y
        
    def setVectorPosition(self, vector):
        self.position.values[0] = vector[0]
        self.position.values[1] = vector[1]
    
    def getPosition(self):
        return self.position
    
    def setX(self, x):
        self.position.values[0] = x
    
    def getX(self):
        return self.position.values[0]
    
    def setY(self, y):
        self.position.values[1] = y
    
    def getY(self):
        return self.position.values[1]
    
    def move(self, x, y):
        self.position.move(Vector2f(x, y))
    
    def vectorMove(self, vector):
        self.position.move(vector)