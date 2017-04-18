#OpenGL library import
import OpenGL
OpenGL.ERROR_ON_COPY = True

#For creating window
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

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

#Function to initiate the 2D orthogonal window
def initiate2DWindow(r,g,b):
    #Clear buffer
    glClearColor(r,g,b,0.0)
    #Set 2D orthogonal window with specified width and height
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, float(imageWidth), 0.0, float(imageHeight))

#Function to draw the display
def renderDisplay():
    #Clear buffer
    glClear(GL_COLOR_BUFFER_BIT)

    drawLangit()
    drawCahaya()
    drawMatahari()
    drawPelangi()
    drawLeftMountain()
    drawRightMountain()
    drawClouds(150, 500)
    drawClouds(1350, 500)

    #Left
    drawTree(0,-500)
    drawTree(120,-500)
    drawTree(240,-500)

    #Middle
    drawTree(450,-500)
    drawTree(570,-500)
    drawTree(690,-500)

    #Right
    drawTree(900,-500)
    drawTree(1020,-500)
    drawTree(1140,-500)

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

def drawWhiteCircle(posx, posy):
    sides = 200
    radius = 30
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    for i in range(sides+2):
        cosine = (radius * cos(i*2*pi/sides))+posx
        sine = (radius * sin(i*2*pi/sides))+posy
        glVertex2f(cosine,sine)
    glEnd()

def drawClouds(posx, posy):
    #Corner left
    drawWhiteCircle(posx-95, posy)

    #Two left
    drawWhiteCircle(posx-70, posy-10)
    drawWhiteCircle(posx-70, posy+10)

    #Middle left
    drawWhiteCircle(posx-40, posy-20)
    drawWhiteCircle(posx-40, posy)
    drawWhiteCircle(posx-40, posy+20)

    #Middle
    drawWhiteCircle(posx, posy-25)
    drawWhiteCircle(posx, posy)
    drawWhiteCircle(posx, posy+25)

    #Middle right
    drawWhiteCircle(posx+40, posy-20)
    drawWhiteCircle(posx+40, posy)
    drawWhiteCircle(posx+40, posy+20)

    #Two right
    drawWhiteCircle(posx+70, posy-10)
    drawWhiteCircle(posx+70, posy+10)

    #Corner right
    drawWhiteCircle(posx+95, posy)

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

def drawTree(dx, dy):
    #batang
    glBegin(GL_POLYGON)
    glColor3ub(102, 51, 0)
    glVertex2i(150+dx, 500+dy)
    glVertex2i(230+dx, 500+dy)
    glVertex2i(190+dx, 600+dy)
    glEnd()

    #draw leaves
    glBegin(GL_POLYGON)
    glColor3ub(10, 51, 0)
    glVertex2i(130+dx, 540+dy)
    glVertex2i(250+dx, 540+dy)
    glColor3ub(0, 255, 0)
    glVertex2i(190+dx, 610+dy)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(10, 51, 0)
    glVertex2i(135+dx, 570+dy)
    glVertex2i(245+dx, 570+dy)
    glColor3ub(0, 255, 0)
    glVertex2i(190+dx, 630+dy)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(10, 51, 0)
    glVertex2i(140+dx, 590+dy)
    glVertex2i(240+dx, 590+dy)
    glColor3ub(0, 255, 0)
    glVertex2i(190+dx, 650+dy)
    glEnd()

def drawLeftMountain():
    dx = 25
    dy = -300

    #Draw mountain
    glBegin(GL_POLYGON)
    #glColor3ub(173, 216, 230)
    #glColor3ub(0, 191, 255)
    #glColor3ub(30, 144, 255)
    glColor3ub(25, 25, 112)
    glVertex2i(dx, 300+dy)
    glColor3ub(30, 144, 255)
    glVertex2i(950+dx, 300+dy)
    glColor3ub(255, 255, 255)
    glVertex2i(375+dx, 900+dy)
    glEnd()

def drawRightMountain():
    dx = 575
    dy = -300

    #Draw mountain
    glBegin(GL_POLYGON)
    #glColor3ub(30, 144, 255)
    glColor3ub(25, 25, 112)
    glVertex2i(dx, 300+dy)
    glColor3ub(30, 144, 255)
    glVertex2i(900+dx, 300+dy)
    glColor3ub(255, 255, 255)
    glVertex2i(475+dx, 900+dy)
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
#Pop the window
initiate2DWindow(0,0,0)
#Render the display
glutDisplayFunc(renderDisplay)
#Run glut main loop to keep the window open until it's closed
glutMainLoop()
