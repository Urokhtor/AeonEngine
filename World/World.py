from time import sleep
from AeonEngine.Base.EntityManager import EntityManager
from AeonEngine.Base.SceneManager import SceneManager

from AeonEngine.Base.Module import Module

class World(Module):
    
    def __init__(self, environment, timer):
        Module.__init__(self, environment, timer, "world")
        #self.printTime = True
        #self.playerManager = PlayerManager()
        #self.currPlayer = self.playerManager.getCurrentPlayer()
        self.entityManager = EntityManager(self.environment)
        self.sceneManager = SceneManager(self.environment)
        #self.currScene = self.sceneManager.getCurrentScene()
        #self.weatherManager = WeatherManager() # Yeah, 2D engines can support dynamic weathers!
    
    def doUpdate(self, cumTime):
        self.sceneManager.getCurrentScene().onUpdate(cumTime)