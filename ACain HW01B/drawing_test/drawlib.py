# Drawing Routines that are similar to those in OpenGL

#Created by: Ashley Cain

from matrix_stack import *
vertexList = []   
isOrtho = False 
myFov = 0 

vLeft = 0 
vRight = 0
vBottom = 0
vTop = 0



def gtOrtho(left, right, bottom, top, near, far):
    global vLeft
    vLeft = left 
    
    global vRight
    vRight = right 
    
    global vBottom
    vBottom = bottom
    
    global vTop
    vTop = top
    
    global isOrtho
    isOrtho = True 

def gtPerspective(fov, near, far):
    global myFov  
    myFov = fov 
    
    global isOrtho
    isOrtho = False

def gtVertex(x, y, z):
    global vertexList 
    
    finals = multiplyVecMat([x, y, z, 1], get_ctm()) 
    finalX = finals[0] 
    finalY = finals [1]
    finalZ = finals[2]    
    
    vertexList.append((finalX, finalY, finalZ)) 

def gtBeginShape():
    pass

def gtEndShape():
    
    global myFov
    k = tan(radians(myFov) / 2)
    index = 0
    
    global vLeft
    global vRight
    global vTop
    global vBottom
    global vertexList
    global isOrtho
    

    if (isOrtho):
        while (index < len(vertexList) - 1): 
            vertexX1 = ((vertexList[index][0] - vLeft) * width) / (float(vRight - vLeft))
            vertexY1 = height - (vertexList[index][1] - vBottom)  * (width / (float(vTop - vBottom)))
        
            index = index + 1
            
            vertexX2 = ((vertexList[index][0] - vLeft)  * width) / (float(vRight - vLeft))
            vertexY2 = height - (vertexList[index][1] - vBottom)  * (width / (float(vTop - vBottom)))

            line(vertexX1, vertexY1, vertexX2, vertexY2)
            index = index + 1
    else:
        while (index < len(vertexList) - 1): 
    
            pX1 = vertexList[index][0] / float(abs(vertexList[index][2]))
            pY1 = vertexList[index][1] / float(abs(vertexList[index][2]))
            x1 = (float(pX1 + k)) * (width / (float(2 * k)))
            y1 = height - (float(pY1 + k))  * (height / (float(2 * k)))
            
            index = index + 1
            
            pX2 = vertexList[index][0] / float(abs(vertexList[index][2]))
            pY2 = vertexList[index][1] / float(abs(vertexList[index][2]))
            x2 = (float(pX2 + k))  * (width / (float(2 * k)))
            y2 = height - (float(pY2 + k))  * (height / (float(2 * k)))
            
            line(x1, y1, x2, y2)
            
            index = index + 1
    
    
    vertexList = []

def multiplyVecMat (vec, mat):
    final = []
    
    for index in range(4):
        v0 = mat[index][0] * vec[0]
        v1 = mat[index][1] * vec[1]
        v2 = mat[index][2] * vec[2]
        v3 = mat[index][3] * vec[3]
        final.append(v0 + v1 + v2 + v3)
    
    return final
