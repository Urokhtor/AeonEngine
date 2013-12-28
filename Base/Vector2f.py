from math import sqrt

class Vector2f:
    
    def __init__(self, x = 0, y = 0, vector = None):
        if vector is not None:
            self.values = [vector[0], vector[1]]
        
        else:
            self.values = [x, y]
    
    def at(self, index):
        if index > 1:
            return None
        
        return self.values[index]
    
    def dot(self, vector):
        return self.values[0] * vector.values[0] + self.values[1] * vector.values[1]
    
    def lengthSqr(self):
        return dot(self)
    
    def length(self):
        return sqrt(dot(self))
    
    def normalise(self):
        return self.divide(self.length())
    
    def multiplicate(self, vector):
        return Vector2f(self.values[0] * vector.values[0], self.values[1] * vector.values[1])
    
    def divide(self, vector):
        return Vector2f(self.values[0] / vector.values[0], self.values[1] / vector.values[1])
    
    def sum(self, vector):
        return Vector2f(self.values[0] + vector.values[0], self.values[1] + vector.values[1])
        
    def subtract(self, vector):
        Vector2f(self.values[0] - vector.values[0], self.values[1] - vector.values[1])
    
    def move(self, vector):
        self.values[0] += vector.values[0]
        self.values[1] += vector.values[1]