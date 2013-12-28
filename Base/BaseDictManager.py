from threading import RLock

class BaseDictManager:
    
    def __init__(self, environment):
        self.environment = environment
        self.objectDict = {}
        self.mutex = RLock()
    
    def add(self, name, object):
        if name in self.objectDict:
            return False
            
        self.mutex.acquire()
        self.objectDict[name] = object
        self.mutex.release()
        return True
    
    def remove(self, name):
        if name not in self.objectDict:
            return False
        
        self.mutex.acquire()
        del self.objectDict[name]
        self.mutex.release()
        return True
    
    def get(self, name):
        if name not in self.objectDict:
            return None
        
        return self.objectDict[name]
    
    def set(self, name, value):
        if name not in self.objectDict:
            return False
        
        self.mutex.acquire()
        self.objectDict[name] = value
        self.mutex.release()
        return True
    
    def clear(self):
        self.mutex.acquire()
        self.objectDict.clear()
        self.mutex.release()