from AeonEngine.Timer import Timer
from AeonEngine.Input.InputHandler import InputHandler
from AeonEngine.World.World import World
from AeonEngine.Renderer.RenderEngine import RenderEngine
from AeonEngine.Base.StateManager import StateManager

class Environment:
    """
        This class is a holder for all the pieces of the game engine which allows different pieces to interact
        with each other.
    """
    
    def __init__(self):
        #from AeonEngine.Constants import AEON_MICROS
        #self.internalTimer = Timer(AEON_MICROS) # Uncomment this and above to use microsecond precision.
        self.internalTimer = Timer() # Comment if you want to use microsecond precision.
        self.inputHandler = InputHandler(self, self.internalTimer)
        self.world = World(self, self.internalTimer)
        self.renderer = RenderEngine(self, self.internalTimer)
        self.stateManager = StateManager(self)
        self.stateManager.init()
    