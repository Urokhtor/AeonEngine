from threading import RLock

class BaseManager:
    
    def __init__(self, environment):
        self.environment = environment
        self.objectList = []
        self.mutex = RLock()
    
    def add(self, object):
        self.mutex.acquire()
        self.objectList.append(object)
        self.mutex.release()
        return True
    
    def remove(self, object):
        if object not in self.objectList:
            return False
        
        self.mutex.acquire()
        self.objectList.remove(object)
        self.mutex.release()
        return True
    
    def removeIndex(self, index):
        if index >= len(self.objectList):
            return False
        
        self.mutex.acquire()
        self.objectList.pop(index)
        self.mutex.release()
        return True
    
    def get(self, index):
        if len(self.objectList) <= index or index < 0:
            return None
        
        return self.objectList.get(index)
    
    def set(self, index, object):
        if len(self.objectList) < index or index < 0:
            return False
            
        self.mutex.acquire()
        self.objectList.insert(index, object)
        self.mutex.release()
        return True
    
    def clear(self):
        self.mutex.acquire()
        self.objectList[:] = []
        self.mutex.release()