from PIL import Image
from OpenGL.GL import *

from AeonEngine.Base.BaseDictManager import BaseDictManager

class TextureManager(BaseDictManager):
    
    def __init__(self, environment):
        BaseDictManager.__init__(self, environment)
        self.textureID = 1
    
    def load(self, file):
        texture = Image.open(file)
        texture.load()
        
        self.textureID = 1#glGenTextures(1)
        
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, self.textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)# GL_LINEAR_MIPMAP_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)# GL_LINEAR_MIPMAP_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP, GL_TRUE)
        #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture.size[0], texture.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, texture.tostring("raw", "RGB", 0, -1))
