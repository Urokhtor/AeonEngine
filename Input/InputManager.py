from threading import RLock
from AeonEngine.Base.BaseDictManager import BaseDictManager
from AeonEngine.Constants import *

class InputManager(BaseDictManager):
    """
        Manager that handles grabbing input and using that data to update states of player, world and game.
    """
    
    def __init__(self, environment):
        BaseDictManager.__init__(self, environment)
        self.eventKeys = {}
        self.eventMouse = {}
        self.mutex = RLock()
        
    def init(self):
        self.objectDict[AEON_KEY_LEFT] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_RIGHT] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_UP] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_DOWN] = {"state": False, "hold": False, "x": 0, "y": 0}
        
        self.objectDict[AEON_KEY_CTRL] = {"state": False, "hold": False, "x": 0, "y": 0}
        
        self.objectDict[AEON_KEY_SPACE] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_ESC] = {"state": False, "hold": False, "x": 0, "y": 0}
        
        self.objectDict[AEON_KEY_1] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_2] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_3] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_4] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_5] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_6] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_7] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_8] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_9] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_0] = {"state": False, "hold": False, "x": 0, "y": 0}
        
        self.objectDict[AEON_KEY_F1] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F2] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F3] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F4] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F5] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F6] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F7] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F8] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F9] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F10] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F11] = {"state": False, "hold": False, "x": 0, "y": 0}
        self.objectDict[AEON_KEY_F12] = {"state": False, "hold": False, "x": 0, "y": 0}
    
    def keyboardDownEvent(self, key, x, y):
        self.mapKeyboardEvent(key, AEON_KEYBOARD_STATE_DOWN, x, y)
    
    def keyboardUpEvent(self, key, x, y):
        self.mapKeyboardEvent(key, AEON_KEYBOARD_STATE_UP, x, y)
    
    def mapKeyboardEvent(self, key, state, x, y):
        if self.environment.stateManager.get(AEON_STATE_CAPTURE_KEYBOARD):
            return
        
        #print(key)
        #if isinstance(key, bytes): print("Intvalue: " + str(int.from_bytes(key, byteorder="big")))
        keyCache = []
        self.mutex.acquire()
        
        if isinstance(key, bytes):
            if key == b"\xe4": keyCache.append(("ä", state, x, y))
            elif key == b"\xf6": keyCache.append(("ö", state, x, y))
            elif key == b"\xe5": keyCache.append(("å", state, x, y))
            elif key == b"\xc4": keyCache.append(("Ä", state, x, y))
            elif key == b"\xd6": keyCache.append(("Ö", state, x, y))
            elif key == b"\xc5": keyCache.append(("Å", state, x, y))
            elif key == b"\xa7": keyCache.append(("§", state, x, y))
            elif key == b"\xbd": keyCache.append(("½", state, x, y))
            elif key == b"\t": keyCache.append(("tab", state, x, y))
            elif key == b" ": keyCache.append(("space", state, x, y))
            elif key == b"\x1b": keyCache.append(("esc", state, x, y))
            else: 
                try:
                    keyCache.append((key.decode("UTF-8", "ignore"), state, x, y))
                
                except Exception as e:
                    print("mapKeyboardEvent encountered an exception: " + str(e))
                    
        elif isinstance(key, int):
            if key >= 1 and key <= 12: keyCache.append(("F" + str(key), state, x, y))
            else: keyCache.append((str(key), state, x, y))
            
        self.mutex.release()
        
        self.updateKey(keyCache)
        # Now call some event system so user get information about the keyboard event?
        # Event should take the key information? Use eventKeys
        
    def updateKey(self, keyCache):
        if len(keyCache) <= 0:
            return
        
        self.mutex.acquire()
        
        for key, state, x, y in keyCache:
            if key in self.objectDict:
                # We will try to update hold status, but if glutIgnoreKeyRepeat(1) is set, this does nothing.
                # It's just an option to let either us or glut handle key repeats.
                if self.objectDict[key]["state"] and state and not self.objectDict[key]["hold"]: self.objectDict[key]["hold"] = True
                elif not state: self.objectDict[key]["hold"] = False
                
                self.objectDict[key]["state"] = state
                self.objectDict[key]["x"] = x
                self.objectDict[key]["y"] = y
                self.eventKeys[key] = self.objectDict[key] # Should we safecopy this?
                
        self.mutex.release()
        
    def mapMouseEvent(self, button, state, x, y):
        if self.environment.stateManager.get(AEON_STATE_CAPTURE_MOUSE):
            return
            
        print(button)
        print(state)
        print(x)
        print(y)
        # TODO: needs input dict for mouse too
        self.mutex.acquire()
        self.eventMouse[button] = {}
        self.eventMouse[button]["state"] = state
        self.eventMouse[button]["x"] = x
        self.eventMouse[button]["y"] = y
        self.mutex.release()
    
    def mapMotionEvent(self, x, y):
        """
            Maps the mouse cursor location upon movement when a mouse button is pressed.
        """
        
        if self.environment.stateManager.get(AEON_STATE_CAPTURE_MOUSE):
            return
        
        #print("Motion: " + str(x) + " " + str(y))
        pass
        
    def mapPassiveEvent(self, x, y):
        """
            Maps the mouse cursor location upon movement when no mouse button is pressed.
        """
        
        if self.environment.stateManager.get(AEON_STATE_CAPTURE_MOUSE):
            return
        
        #print("Passive: " + str(x) + " " + str(y))
        pass
    
    def handleInput(self, cumTime):
        # NOTE: we should probably use cumTime to detect holding keys down or something?
        # We should have a way of knowing whether the key has been pressed just now or has it been
        # pressed down for a while. Perhaps we should use an event queue?
        
        if len(self.eventKeys) > 0 and not self.environment.stateManager.get(AEON_STATE_CAPTURE_KEYBOARD):
            self.handleKeyboard(cumTime)
            # Then send event?
            
        if len(self.eventMouse) > 0 and not self.environment.stateManager.get(AEON_STATE_CAPTURE_MOUSE):
            self.handleMouse(cumTime)
            # Then send event?
            
    def handleKeyboard(self, cumTime):
        self.mutex.acquire()
        
        print(self.eventKeys)
        
        # Here we probably should have key bindings i.e. binding[AEON_KEY_LEFT] = action
        # Then, if key == AEON_KEY_LEFT and it's pressed, we get the action for the binding and execute it
        # or if the key is released we stop executing the action.
        
        for key, value in self.eventKeys.items():
            if key == "a":
                print("FPS: " + str(self.environment.renderer.getFPS()))
                self.environment.renderer.setTargetFPS(250)
                    
            elif key == "b":
                print("FPS: " + str(self.environment.renderer.getFPS()))
                self.environment.renderer.setTargetFPS(60)
                        
            elif key == "c":
                print("FPS: " + str(self.environment.renderer.getFPS()))
                self.environment.renderer.setTargetFPS(30)
                        
            elif key == "d":
                print("FPS: " + str(self.environment.renderer.getFPS()))
                self.environment.renderer.setTargetFPS(10)
            
            elif key == AEON_KEY_SPACE:
                print("Capturing keyboard input")
                self.environment.stateManager.set(AEON_STATE_CAPTURE_KEYBOARD, True)
            
            elif key == AEON_KEY_CTRL and value["state"] == True:
                print("Capturing mouse input")
                self.environment.stateManager.set(AEON_STATE_CAPTURE_MOUSE, True)
            
            elif key == AEON_KEY_CTRL and value["state"] == False:
                print("Releasing mouse input")
                self.environment.stateManager.set(AEON_STATE_CAPTURE_MOUSE, False)
            
            elif key == AEON_KEY_ESC and value["state"] == False:
                from os import _exit
                _exit(0) # This is not a safe way to quit.
        
        self.eventKeys.clear()
        self.mutex.release()
    
    def handleMouse(self, cumTime):
        self.mutex.acquire()
        
        print(self.eventMouse)
        
        self.eventMouse.clear()
        self.mutex.release()