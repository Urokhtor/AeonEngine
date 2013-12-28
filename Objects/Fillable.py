class Fillable:
    
    def __init__(self, filled = False):
        self.filled = filled
    
    def setFilled(self, filled):
        self.filled = filled
    
    def getFilled(self):
        return self.filled