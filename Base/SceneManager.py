from AeonEngine.Base.BaseDictManager import BaseDictManager

class SceneManager(BaseDictManager):
    
    def __init__(self, environment):
        BaseDictManager.__init__(self, environment)
        self.currentScene = None
    
    def setCurrentScene(self, name):
        if name not in self.objectDict:
            return False
        
        self.currentScene = self.get(name)
        return True
    
    def getCurrentScene(self):
        return self.currentScene