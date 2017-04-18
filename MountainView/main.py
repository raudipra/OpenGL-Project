#OpenGL library import
import OpenGL
import ctypes
OpenGL.ERROR_ON_COPY = True

#For creating window
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from OpenGL.GL import shaders

VERTEX_SHADER = """
#version 330

layout (location=0) in vec4 position;
layout (location=1) in vec4 color;

smooth out vec4 theColor;

void main()
{
    gl_Position = position;
    theColor = color;
}
"""

FRAGMENT_SHADER = """
#version 330

smooth in vec4 theColor;
out vec4 outputColor;

void main()
{
    outputColor = theColor;
}
"""

shaderProgram = None
VAO = None

#Array of 4 tuple
#array for:
fourTupleArrayHB = []
fourTupleArrayCahaya = []

#Height and width of the image
imageWidth = "1500"
imageHeight = "705"

#Height and width of the window
windowWidth = int(1500)
windowHeight = int(705)

def initialize():
    global VERTEX_SHADER
    global FRAGMENT_SHADER
    global shaderProgram
    global VAO
    # compile shaders and program
    vertexShader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)

    # triangle position and color
    vertexData = numpy.array([0.0, 0.5, 0.0, 1.0,
                            0.5, -0.366, 0.0, 1.0,
                            -0.5, -0.366, 0.0, 1.0,
                            1.0, 0.0, 0.0, 1.0,
                            0.0, 1.0, 0.0, 1.0,
                            0.0, 0.0, 1.0, 1.0, ],
                            dtype=numpy.float32)

    # create VAO
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # create VBO
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertexData.nbytes, vertexData, GL_STATIC_DRAW)

    # enable array and set up data
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, None)
    # the last parameter is a pointer
    # python donot have pointer, have to using ctypes
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(48))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

#Function to initiate the 2D orthogonal window
def initiate2DWindow(r,g,b):
    #Clear buffer
    glClearColor(r,g,b,0.0)
    #Set 2D orthogonal window with specified width and height
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, float(imageWidth), 0.0, float(imageHeight))

def drawMountain():
    global shaderProgram
    global VAO
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # active shader program
    glUseProgram(shaderProgram)

    glBindVertexArray(VAO)

    # draw triangle
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glBindVertexArray(0)
    glUseProgram(0)

    glutSwapBuffers()

#Function to draw the display
def renderDisplay():
    #Clear buffer
    glClear(GL_COLOR_BUFFER_BIT)

    #Draw dragon
    drawLangit()
    drawCahaya()
    drawMatahari()
    drawPelangi()
    drawMountain()

    #Draw line and flush the buffer
    glFlush()

def drawMatahari():
    posx, posy = 750,350
    sides = 500
    radius = 100
    glBegin(GL_POLYGON)
    glColor3ub(255,0,0)
    glVertex2i(750,350)
    glColor3ub(255, 240, 0)
    for i in range(sides+2):
        cosine = (radius * cos(i*2*pi/sides))+posx
        sine = (radius * sin(i*2*pi/sides))+posy
        glVertex2f(cosine,sine)
    glEnd()


def drawPelangi():
    posx, posy = 750,-10
    sides = 500
    glBegin(GL_LINE_LOOP)
    for j in range(100):
        radius = 650-j
        if (j<=25) :
            glColor3ub(0, 0+(j*10), 255-(j*10))
        elif (j<=50) :
            glColor3ub(0+((j-25)*10), 255, 0)
        elif (j<=75) :
            glColor3ub(255, 255-((j-50)*10), 0)
        else :
            glColor3ub(255, 0, 0)
        for i in range(sides/2):
            cosine = (radius * cos(i*2*pi/sides))+posx
            sine = (radius * sin(i*2*pi/sides))+posy
            glVertex2f(cosine,sine)
    glEnd()

def drawCahaya():
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(40,0)
    glVertex2i(0,40)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(0,390)
    glVertex2i(0,310)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(0,660)
    glVertex2i(40,700)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(460,700)
    glVertex2i(540,700)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(960,700)
    glVertex2i(1040,700)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(1460,700)
    glVertex2i(1500,660)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(1500,390)
    glVertex2i(1500,310)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(1500,40)
    glVertex2i(1460,0)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(960,0)
    glVertex2i(1040,0)

    glColor3ub(255, 255, 255)
    glVertex2i(750,350)
    glColor3ub(132, 184, 224)
    glVertex2i(460,0)
    glVertex2i(540,0)
    glEnd()

def drawLangit():
    glBegin(GL_POLYGON)
    glColor3ub(93,185,237)
    glVertex2i(0,0)
    glVertex2i(1500,0)
    glColor3ub(129,220,215)
    glVertex2i(750,350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(93,185,237)
    glVertex2i(1500,0)
    glVertex2i(1500,705)
    glColor3ub(129,220,215)
    glVertex2i(750,350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(93,185,237)
    glVertex2i(1500,705)
    glVertex2i(0,705)
    glColor3ub(129,220,215)
    glVertex2i(750,350)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(93,185,237)
    glVertex2i(0,705)
    glVertex2i(0,0)
    glColor3ub(129,220,215)
    glVertex2i(750,350)
    glEnd()

#Initiate glut windoe
glutInit(sys.argv)
#Set display mode to single using RGB coloring method
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
#Set initial window size to
glutInitWindowSize (windowWidth, windowHeight)
#Set initial window position to bottom left
glutInitWindowPosition (0, 0)
#Create window with desired name
glutCreateWindow ("Grafika Pemandangan")
#Shader
initialize()
#Pop the window
initiate2DWindow(0,0,0)
#Render the display
glutDisplayFunc(renderDisplay)
#Run glut main loop to keep the window open until it's closed
glutMainLoop()
