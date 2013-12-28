from AeonEngine.Base.BaseDictManager import BaseDictManager
from AeonEngine.Constants import *

class StateManager(BaseDictManager):
    
    def __init__(self, environment):
        BaseDictManager.__init__(self, environment)
    
    def init(self):
        # We should load state data from settings?
        self.objectDict[AEON_STATE_CAPTURE_KEYBOARD] = False
        self.objectDict[AEON_STATE_CAPTURE_MOUSE] = False