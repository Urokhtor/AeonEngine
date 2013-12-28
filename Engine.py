from time import sleep
from threading import Thread
from AeonEngine.Environment import Environment

class Engine:
    
    def __init__(self):
        self.isRunning = True
        self.environment = Environment()
        self.inputThread = Thread(target = self.handleInput)
        self.updateThread = Thread(target = self.update)
        self.renderThread = Thread(target = self.render)
    
    def handleInput(self):
        # Do something like pass the accumulated time to the input handler.
        self.environment.inputHandler.updateThread()
    
    def update(self):
        # Update something, like all the game objects.
        #self.world.update(self.internalTimer.getCumulativeTime())
        self.environment.world.updateThread()
        
    def render(self):
        keyDown = self.environment.inputHandler.inputManager.keyboardDownEvent
        keyUp = self.environment.inputHandler.inputManager.keyboardUpEvent
        mouseEvent = self.environment.inputHandler.inputManager.mapMouseEvent
        motionEvent = self.environment.inputHandler.inputManager.mapMotionEvent
        passiveEvent = self.environment.inputHandler.inputManager.mapPassiveEvent
        self.environment.renderer.initGLUT(1024, 768, keyDown, keyUp, mouseEvent, motionEvent, passiveEvent)
        
    def execute(self):
        self.updateThread.start()
        self.renderThread.start()
        self.inputThread.start()
        
        while 1:
            sleep(0.001)
            
            # Keep track of the game timer.
            self.environment.internalTimer.update()
            
    def getIsRunning(self):
        return self.isRunning
    
    def setIsRunning(self, flag):
        self.isRunning = flag
    
    def getTimer(self):
        return self.internalTimer
        