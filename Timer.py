from time import time
from threading import RLock
from AeonEngine.Constants import AEON_MILLIS, AEON_MICROS

class Timer:
    """
        A thread-safe timer.
    """
    
    def __init__(self, _precision = AEON_MILLIS):
        """
            Initializes the timer object.
            
            Will raise a ValueError if user supplies an unsupported precision value.
        """
        
        self.currTime = 0
        self.lastTime = 0
        self.mutex = RLock()
        
        if not _precision == AEON_MILLIS and not _precision == AEON_MICROS:
            raise ValueError("Incompatible precision value " + str(_precision) + " for timer constructor")
            
        self.precision = _precision
        self.reset()
    
    def update(self):
        """
            Updates the timer. Assigns the currTime before update to the lastTime and then
            updates the currTime. After update the difference between currTime and lastTime
            is the time elapsed between last two updates.
        """
        
        self.mutex.acquire()
        self.lastTime = self.currTime
        
        if self.precision == AEON_MILLIS: self.currTime = self.getTimeMillis()
        elif self.precision == AEON_MICROS: self.currTime = self.getTimeMicros()
        self.mutex.release()
    
    def reset(self):
        """
            Resets the timer.
        """
        
        self.mutex.acquire()
        self.update()
        self.lastTime = self.currTime
        self.mutex.release()
    
    def getPassedTime(self):
        """
            Returns the passed time between last two updates. Notice that it's the
            user's responsibility to check if it's presented in AEON_MILLIS or AEON_MICROS
            format.
        """
        
        #self.mutex.acquire()
        tmp = 0
        if self.precision == AEON_MILLIS: tmp = self.currTime - self.lastTime
        elif self.precision == AEON_MICROS: tmp = (self.currTime - self.lastTime)/1000.0
        #self.mutex.release()
        
        return tmp
    
    def getCumulativeTime(self):
        """
            Returns the cumulated time since last reset().
        """
        
        #self.mutex.acquire()
        tmp = 0
        if self.precision == AEON_MILLIS: tmp = self.currTime
        elif self.precision == AEON_MICROS: tmp = self.currTime/1000.0
        #self.mutex.release()
        
        return tmp
    
    def getTimeMillis(self):
        """
            Returns current time since epoch in milliseconds.
            
            Notice that some systems might not support this precision.
        """
        
        return int(round(time()*1000))
    
    def getTimeMicros(self):
        """
            Returns current time since epoch in microseconds.
            
            Notice that some systems might not support this precision.
        """
        
        return int(round(time()*1000000))
    
    def getPrecision(self):
        """
            Returns the precision at which the timer keeps track of time.
            
            Values are either in milliseconds of microseconds.
        """
        
        return self.precision
        
    def setPrecisionMillis(self):
        """
            Sets the internal precision to milliseconds.
        """
        
        self.precision = AEON_MILLIS
        self.reset()
    
    def setPrecisionMicros(self):
        """
            Sets the internal precision to microseconds.
        """
        
        self.precision = AEON_MICROS
        self.reset()
