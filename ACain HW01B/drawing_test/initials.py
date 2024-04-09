# The routine below should draw your initials in perspective

# Created by: Ashley Cain
from matrix_stack import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective(50, 80, 70)
    
    gtPushMatrix()
    
    drawAC(-12, 30, 60)

    gtPopMatrix()
    
def drawAC(zoom, rX, rY):

    gtTranslate(0, 0, zoom)
    gtRotateX(rX)
    gtRotateY(rY)

    gtBeginShape()
    
    gtVertex(-2.25, -1.5, 0)
    gtVertex(-1.25, 1.5, 0)
    
    gtVertex(-1.25, 1.5, 0)
    gtVertex(-0.25, -1.5, 0)

    gtVertex(-1.75, 0, 0)
    gtVertex(-0.75, 0, 0)

    gtEndShape()
    
    gtBeginShape()
    
    gtVertex(0.25, 1.5, 0)
    gtVertex(0.25, -1.5, 0)
    
    gtVertex(0.25, 1.5, 0)
    gtVertex(2.25, 1.5, 0)

    gtVertex(0.25, -1.5, 0)
    gtVertex(2.25, -1.5, 0)
    
    gtVertex(2.25, 1.5, 0)
    gtVertex(2.25, 1, 0)

    gtVertex(2.25, -1, 0)
    gtVertex(2.25, -1.5, 0)

    gtEndShape()
    



    
