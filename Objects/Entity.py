
class Entity(Object):
    """
        Generic class for entities. Player(s), NPCs and monsters inherit from this class.
    """
    
    def __init__(self):
        Object.__init__(self)
    
    #def update(self):
    #    raise NotImplementedError("Update was not implemented for an object inherited from Object class")