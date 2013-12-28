import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

from AeonEngine.Base.Module import Module
from AeonEngine.Base.TextureManager import TextureManager
from AeonEngine.Objects.Rectangle import Rectangle

class RenderEngine(Module):
    
    def __init__(self, environment, timer):
        Module.__init__(self, environment, timer, "renderer")
        self.printTime = True
        self.textureManager = TextureManager(environment)
        self.window = None
        self.fov = 45.0
        self.width = 0
        self.height = 0
        self.zoom = 0.001
        self.x = 0
        self.y = 0
        
        self.teapotIndex = 1
        self.triangleIndex = 2
        self.rotY = 0
    
    # DEBUG CODE
    def drawScene(self, elapsedTime):
        glPushMatrix()
        glRotatef(self.rotY,0.0,1.0,0.0)
        #glTranslatef(self.rotY, 0, 0) # Move the object
        glCallList(self.teapotIndex)
        #glCallList(self.triangleIndex)
        glPopMatrix()
        self.rotY += 360.0*(elapsedTime/1000.0) # One rotation per second.
        
        if self.rotY > 360.0:
            self.rotY - 360.0
    
    def changeSize(self, width, height):
        """
            Rescales the screen for the new size. Prevents objects on the screen from stretching.
        """
        
        if height == 0: height = 1
        
        dWidth = width - self.width
        dHeight = height - self.height
        
        self.width = width
        self.height = height
        self.x += dWidth
        self.y -= dHeight
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(self.x, self.y, width, height)
        glOrtho(0, self.width, self.height, 0, 0, 1) # 0,0 is at top left.
        glMatrixMode(GL_MODELVIEW)
    
    def initGLUT(self, width, height, keyDown, keyUp, mouse, motionEvent, passiveEvent):
        self.width = width
        self.height = height
        
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)# | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(b"Aeon test")
        
        glutDisplayFunc(self.update)
        glutIdleFunc(self.update)
        glutReshapeFunc(self.changeSize)
        
        # TO BE IMPLEMENTED
        # glutVisibilityFunc(null) # I.e. what do we do when we are minimised or maximised?
        # glutEntryFunc(null) # When pointer enters/leaves the screen, is accurate on X, but is it accurate on Windows?
        # glutOverlayDisplayFunc(null) # Not sure about this, check glutDisplayFunc()
        
        glutKeyboardFunc(keyDown)
        glutKeyboardUpFunc(keyUp)
        glutSpecialFunc(keyDown)
        glutSpecialUpFunc(keyUp)
        glutMouseFunc(mouse)
        glutMotionFunc(motionEvent)
        glutPassiveMotionFunc(passiveEvent)
        glutIgnoreKeyRepeat(1)
        
        self.initGL(width, height)
        self.compileLists()
    
        glutMainLoop()
    
    def initGL(self, width, height):
        glShadeModel(GL_SMOOTH)
        
        #glEnable(GL_DEPTH_TEST)
        #glEnable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearStencil(0)
        glClearDepth(1.0)
        #glDepthFunc(GL_LEQUAL)
        glMatrixMode(GL_PROJECTION)
        self.changeSize(width, height) # Init the camera view.
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(1, 10, 0, 0, 0, 0, 0, 1, 0)
        #self.initLights()
    
    def initLights(self):
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
        
        glLightfv(GL_LIGHT0, GL_POSITION, [10, 10, 10, 1])
        
        glEnable(GL_LIGHT0)
    
    def compileLists(self):
        
        glNewList(self.teapotIndex, GL_COMPILE)
        #glutWireTeapot(1.0)
        glutSolidTeapot(1.0)
        glEndList()
        
        glNewList(self.triangleIndex, GL_COMPILE)
        glBegin(GL_TRIANGLES)
        glVertex3f(4.0,-2.0, 0.0)
        glVertex3f(8.0, 0.0, 1.0)
        glVertex3f(6.0, 2.0, 1.0)
        glEnd()
        glEndList()
    
    def doUpdate(self, cumTime):
        glClear(GL_COLOR_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)# | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()
        glTranslatef(0.375, 0.375, 0) # Correct the pixel position.
        
        #####
        glEnable(GL_TEXTURE_2D)
        #glColor4f(1, 1, 1, 0.4)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D, self.textureManager.textureID)
        
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex2f(200, 200)
        glTexCoord2f(1.0, 0.0)
        glVertex2f(712, 200)
        glTexCoord2f(1.0, 1.0)
        glVertex2f(712, 712)
        glTexCoord2f(0.0, 1.0)
        glVertex2f(200, 712)
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glColor4f(1, 1, 1, 1)
        #####
        
        self.environment.world.sceneManager.getCurrentScene().onPreRender(cumTime)
        self.environment.world.sceneManager.getCurrentScene().onRender(cumTime)
        self.environment.world.sceneManager.getCurrentScene().onPostRender(cumTime)

        glPopMatrix()
        
        glFlush()
        glutSwapBuffers()
    
    def render(self, object):
        if type(object) is Rectangle:
            self.renderRectangle(object)
    
    def renderRectangle(self, rectangle):
        x = rectangle.getX()
        y = rectangle.getY()
        w = rectangle.getWidth()
        h = rectangle.getHeight()
        
        if rectangle.getFilled():
            glBegin(GL_QUADS)
        
        else:
            glBegin(GL_LINE_LOOP)
            
        glVertex2f(x, y)
        glVertex2f(x+w, y)
        glVertex2f(x+w, y+h)
        glVertex2f(x, y+h)
        glEnd()
        