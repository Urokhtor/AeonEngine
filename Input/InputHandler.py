from AeonEngine.Base.Module import Module
from AeonEngine.Input.InputManager import InputManager

class InputHandler(Module):
    
    def __init__(self, environment, timer):
        Module.__init__(self, environment, timer, "input")
        self.setTargetFPS(250)
        self.inputManager = InputManager(environment)
        self.inputManager.init()
    
    def doUpdate(self, cumTime):
        # How to handle input here? Obviously we'll need to load some kind of key settings
        # somewhere, should we handle the loaded keys here or pass somewhere?
        # Could we do something like "if KEY_LEFT: player->moveLeft()"?
        self.inputManager.handleInput(cumTime)