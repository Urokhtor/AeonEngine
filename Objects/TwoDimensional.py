class TwoDimensional:
    
    def __init__(self, w = 0, h = 0):
        self.width = w
        self.height = h
    
    def setDimensions(self, w, h):
        self.width = w
        self.height = h
    
    def getDimensions(self):
        return (self.width, self.height)
    
    def setWidth(self, w):
        self.width = w
    
    def getWidth(self):
        return self.width
    
    def setHeight(self, h):
        self.height = h
    
    def getHeight(self):
        return self.height