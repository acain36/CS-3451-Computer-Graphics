# Your Matrix Stack Library

# Created by: Ashley Cain

# you should modify the provided empty routines to complete the assignment

### creating a class for the stack holding the matrices

class stack(object):
    
    ### method for initializing the object
    def __init__(self):
        self.elem = []
        
    ### method for supporting the push operation
    def stackPush(self, data):
        self.elem.append(data)
        
    ### method for supporting the pop operation
    def stackPop(self):
        if(len(self.elem) <= 1):
            print("cannot pop the matrix stack")
        else:
            self.elem.pop()
       
   ### method for clearing all items from the stack     
    def stackClear(self):
        self.elem = []
        
    ### method for getting and returning the current matrix
    def stackCurrent(self):
        return(self.elem[-1])
            
 
    
### creating a stack object to update
myStack = stack()

### method to initialize the matrix stack so that there is only one identity matrix within
def gtInitialize():
    myStack.stackClear()
    myStack.stackPush([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    

### method to pop the current matrix off from off of the top of the stack as long as there is more than one matrix within the stack
def gtPopMatrix():
    myStack.stackPop()


### method to push a transformation onto the stack by:
### 1 - duplicate the current transformation matrix
### 2 - put a copy of the matrix on top of the stack
def gtPushMatrix():
    currentMatrix = myStack.stackCurrent()
    currentCopy = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
    for x in range(4):
        for y in range(4):
            currentCopy[x][y] = currentMatrix[x][y]
    myStack.stackPush(currentCopy)

        
### scales the current transformation matrix by using a scale transformation matrix
### new_ctm = old_ctm * scale_matrix
def gtScale(x,y,z):
    currentMatrix = myStack.stackCurrent()
    scaleMatrix = [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    newMatrix = matrixMultiply(currentMatrix, scaleMatrix)
    myStack.stackPop()
    myStack.stackPush(newMatrix)

### translates the current transformation matrix by using a translation transformation matrix
def gtTranslate(x,y,z):
    currentMatrix = myStack.stackCurrent()
    translateMatrix = [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]
    newMatrix = matrixMultiply(currentMatrix, translateMatrix)
    myStack.stackPop()
    myStack.stackPush(newMatrix)


### takes degrees and changes to radians before using trig identities to rotate about X axis
def gtRotateX(theta):
    rad = radians(theta)
    currentMatrix = myStack.stackCurrent()
    rotateMatrix = [[1, 0, 0, 0], [0, cos(rad), -sin(rad), 0], [0, sin(rad), cos(rad), 0], [0, 0, 0, 1]]
    newMatrix = matrixMultiply(currentMatrix, rotateMatrix)
    myStack.stackPop()
    myStack.stackPush(newMatrix)
    


### takes degrees and changes to radians before using trig identities to rotate about Y axis
def gtRotateY(theta):
    rad = radians(theta)
    currentMatrix = myStack.stackCurrent()
    rotateMatrix = [[cos(rad), 0, sin(rad), 0], [0, 1, 0, 0], [-sin(rad), 0, cos(rad), 0], [0, 0, 0, 1]]
    newMatrix = matrixMultiply(currentMatrix, rotateMatrix)
    myStack.stackPop()
    myStack.stackPush(newMatrix)


### takes degrees and changes to radians before using trig identities to rotate about Z axis
def gtRotateZ(theta):
    rad = radians(theta)
    currentMatrix = myStack.stackCurrent()
    rotateMatrix = [[cos(rad), -sin(rad), 0, 0], [sin(rad), cos(rad), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    newMatrix = matrixMultiply(currentMatrix, rotateMatrix)
    myStack.stackPop()
    myStack.stackPush(newMatrix)


### method will print the current matrix with a
def print_ctm():
    currentMatrix = myStack.stackCurrent()
    for x in range(4):
        print (str(currentMatrix[x][0]) + ' ' + str(currentMatrix[x][1]) + ' ' + str(currentMatrix[x][2]) + ' ' + str(currentMatrix[x][3]))
    print("\n")
    
def get_ctm():
    return myStack.stackCurrent()

### method to help with mutliplying two matrices
def matrixMultiply(matrix1, matrix2):
    finalMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(4):
        for y in range(4):
            for z in range(4):
                finalMatrix[x][y] += matrix1[x][z] * matrix2[z][y]
    return finalMatrix
