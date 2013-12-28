from time import sleep, time

class Module:
    
    def __init__(self, environment, timer, name):
        self.environment = environment
        self.timer = timer
        self.name = name
        self.lastTime = self.timer.getCumulativeTime() # Unix time of the last loop.
        self.lastLoopTime = 0 # Frame time.
        self.targetFPS = 0.01666
        self.setTargetFPS(60)
        self.printTime = False
    
    def doUpdate(self, cumTime):
        raise NotImplementedError("Subclass deriving from Module hasn't implemented update method")
    
    def update(self):
        cumTimeBegin = self.timer.getCumulativeTime()
        
        # Mark the last time we'll pass to the objects to be rendered - if needed.
        self.lastLoopTime = cumTimeBegin - self.lastTime
        self.lastTime = cumTimeBegin
        
        self.doUpdate(self.lastLoopTime)
        
        cumTimeEnd = self.timer.getCumulativeTime()
        waitTime = self.targetFPS - (cumTimeEnd - cumTimeBegin)/1000.0
        
        if self.printTime:
            print(self.name + " took: " + str(self.lastLoopTime/1000.0))
        
        if waitTime < 0 or self.targetFPS == 0: return
        
        sleep(waitTime)
    
    def updateThread(self):
        while 1: self.update() # Not sure if we should get rid of the method callback overhead.
    
    def getTargetFPS(self):
        return self.targetFPS
    
    def setTargetFPS(self, target):
        self.targetFPS = (1000.0/float(target))/1000.0
    
    def getFPS(self):
        return 1000.0/self.lastLoopTime