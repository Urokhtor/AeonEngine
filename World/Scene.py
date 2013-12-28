class Scene:
    """
        Scene is the base class for playable environments, like exteriors, interiors and the world map.
        The interface defines methods that are called in different situations, such as entering a scene,
        or leaving a scene which allows the users to define things like loading and unloading resources for
        the environment.
    """
    
    def __init__(self, environment):
        self.environment = environment
        self.updateables = []
        self.renderables = []
        # We should also hold a map of some kind.
    
    def onInit(self):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onInit method")
    
    def onEnter(self):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onEnter method")
    
    def onUpdate(self, cumTime):
        if len(self.updateables) < 1:
            return
        
        for updateable in self.updateables:
            updateable.update(cumTime)
    
    def onPause(self):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onPause method")
    
    def onLeave(self):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onLeave method")
    
    def onPreRender(self, cumTime):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onPreRender method")
    
    def onRender(self, cumTime):
        if len(self.renderables) < 1:
            return
        
        for renderable in self.renderables:
            renderable.render(cumTime, self.environment.renderer)
    
    def onPostRender(self, cumTime):
        raise NotImplementedError("Subclass deriving from Scene class hasn't implemented onPostRender method")
    
    def addUpdateable(self, updateable):
        if updateable is None:
            return False
        
        if updateable.update is None:
            return False
        
        self.updateables.append(updateable)
        
    def addRenderable(self, renderable):
        if renderable is None:
            return False
        
        if renderable.render is None:
            return False
        
        self.renderables.append(renderable)