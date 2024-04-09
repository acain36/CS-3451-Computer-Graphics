# Provided code for Subdivison and Geodesic Spheres

from __future__ import division
import traceback

# parameters used for object rotation by mouse
mouseX_old = 0
mouseY_old = 0
rot_mat = PMatrix3D()

V = []
G = []
O = {}
currentCorner = 0
currentCornerVisible = False
showRandomColors = False

def print_mesh():
    global V, O, G
    print "Vertex table (maps corner num to vertex num):"
    print "corner num\tvertex num:"
    for c, v in enumerate(V):
        print c, "\t\t", v
    print ""

    print "Opposite table (maps corner num to opposite corner num):"
    print "corner num\topposite corner num"
    for c, o in O.iteritems():
        print c, "\t\t", o
    print ""

    print "Geometry table (maps vertex num to position): "
    print "vertex num\tposition:"
    for v, g in enumerate(G):
        print v, "\t\t", g
    print ""

    print ""
    print ""
 
    
          
def nextCorner(cornerNum):
    triangleNum = cornerNum//3
    return 3 * triangleNum + ((cornerNum + 1) % 3)



def previousCorner(cornerNum): 
    triangleNum = cornerNum//3
    return 3 * triangleNum + ((cornerNum - 1) % 3)

    
            
def oppositeCorner(cornerNum):
    global O
    return O[cornerNum]
  
    
        
def swingCorner(cornerNum):
    return nextCorner(oppositeCorner(nextCorner(cornerNum)))
 
    
          
def Otable(G, V):
    global O
    triplets = []
    
    for i in range(0, len(V)):
        triplets.append([min(V[nextCorner(i)], V[previousCorner(i)]), max(V[nextCorner(i)], V[previousCorner(i)]), i]) 
         
    triplets = sorted(triplets)
    
    for j in range(0, len(triplets), 2):
        cornerA = triplets[j][2]
        cornerB = triplets[j+1][2]
        O[cornerA] = cornerB
        O[cornerB] = cornerA
    

    
            
def inflate():
    global G
    for i in range(0, len(G)):
        G[i].normalize()
    return G




def subdivide():
    global G, V, O
    numEdges = len(V)//2
    newG = G
    newV = []
    midpoints = {}
    
    for a, b in O.items():
        endpoint1 = G[V[previousCorner(a)]]
        endpoint2 = G[V[nextCorner(a)]]
        
        midpoint = PVector.add(endpoint1, endpoint2)
        midpoint = PVector.mult(midpoint, 0.5)
        
        midpointIndex = len(newG)
        newG.append(midpoint)
        
        midpoints[a] = midpointIndex
        
        endpoint1 = G[V[previousCorner(b)]]
        endpoint2 = G[V[nextCorner(b)]]
        
        midpoint = PVector.add(endpoint1, endpoint2)
        midpoint = PVector.mult(midpoint, 0.5)
        
        midpointIndex = len(newG)
        newG.append(midpoint)
        
        midpoints[b] = midpointIndex
    
    for x in range(0, len(V), 3):
        y = x+1
        z = x+2
        
        newV.extend([V[x], midpoints[z], midpoints[y]])
        newV.extend([midpoints[z], V[y], midpoints[x]])
        newV.extend([midpoints[y], midpoints[x], V[z]])
        newV.extend([midpoints[x], midpoints[z], midpoints[y]])
        
    G = newG
    V = newV
        
    Otable(G, V)
   
    
     
      
        
class PVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "PVector(%f, %f, %f)" % (self.x, self.y, self.z)
    def __add__(self, other):
        return PVector.add(self, other)
    def __mul__(self, n):
        return PVector.mult(self, n)
    def __rmul__(self, n):
        return PVector.mult(self, n)
    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z
    def copy(self):
        return PVector(self.x, self.y, self.z)
    def div(self, n):
        return PVector(
            self.x / n,
            self.y / n,
            self.z / n,
        )
    @staticmethod
    def dist(a, b):
        return PVector.sub(a, b).mag()
    @staticmethod
    def add(a, b):
        return PVector(
            a.x + b.x,
            a.y + b.y,
            a.z + b.z,
        )
    @staticmethod
    def sub(a, b):
        return PVector(
            a.x - b.x,
            a.y - b.y,
            a.z - b.z,
        )
    @staticmethod
    def mult(a, n):
        return PVector(
            n * a.x,
            n * a.y,
            n * a.z,
        )
    @staticmethod
    def pairwise_mult(a, b):
        return PVector(
            a.x * b.x,
            a.y * b.y,
            a.z * b.z,
        )

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z
    @staticmethod
    def cross(a, b):
        return PVector(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x,
        )
    def normalize(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self







# initalize things
def setup():
    size (800, 800, OPENGL)
    frameRate(30)
    noStroke()
    
    
# draw the current mesh (you will modify parts of this routine)
def draw():
    randomSeed(0)
    global V, O, G, showRandomColors, currentCornerVisible, currentCorner
    background (100, 100, 180)    # clear the screen to black

    perspective (PI*0.2, 1.0, 0.01, 1000.0)
    camera (0, 0, 6, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    
    # create an ambient light source
    ambientLight (102, 102, 102)

    # create two directional light sources
    lightSpecular (202, 202, 202)
    directionalLight (100, 100, 100, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    stroke (0)                    # draw polygons with black edges
    fill (200, 200, 200)          # set the polygon color to white
    ambient (200, 200, 200)
    specular (0, 0, 0)            # turn off specular highlights
    shininess (1.0)
    
    applyMatrix (rot_mat)   # rotate the object using the global rotation matrix

    # THIS IS WHERE YOU SHOULD DRAW YOUR MESH
  
    # part where you tell whether there are random colors
    
    # part to make current corner visible
    if currentCornerVisible:
        pushMatrix()
        currentVertex = G[V[currentCorner]]
        translate(currentVertex.x, currentVertex.y, currentVertex.z)
        sphere(0.1)
        popMatrix()
        
                        
    for c in range(0, len(V), 3):
        if showRandomColors:
            fill(random(255), random(255), random(255))
        else:
            fill(255, 255, 255)
            
        beginShape()
            
        # draw the three vertices
        vertex(G[V[c]].x, G[V[c]].y, G[V[c]].z)
        vertex(G[V[c+1]].x, G[V[c+1]].y, G[V[c+1]].z)
        vertex(G[V[c+2]].x, G[V[c+2]].y, G[V[c+2]].z)
        
        endShape(CLOSE)
    
    popMatrix()






# read in a mesh file (this needs to be modified)
def read_mesh(filename):
    global G, V, O
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        G.append(PVector(x, y, z))
        print "vertex: ", x, y, z

    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if (nverts != 3):
            print "error: this face is not a triangle"
            exit()

        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        V.extend([index1, index2, index3])
        print "triangle: ", index1, index2, index3
        
    Otable(G, V)
    print_mesh()







# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()




# process key presses (call your own routines!)
def handleKeyPressed():
    global currentCorner, currentCornerVisible, showRandomColors, V, G, O 
    if key == '1':
        read_mesh ('tetra.ply')
        
    elif key == '2':
        read_mesh ('octa.ply')
        
    elif key == '3':
        read_mesh ('icos.ply')
        
    elif key == '4':
        read_mesh ('star.ply')
        
    elif key == 'n': # next
        currentCorner = nextCorner(currentCorner)
        
    elif key == 'p': # previous
        currentCorner = previousCorner(currentCorner)
        
    elif key == 'o': # opposite
        currentCorner = oppositeCorner(currentCorner)
        
    elif key == 's': # swing
        currentCorner = swingCorner(currentCorner)
        
    elif key == 'd': # subdivide mesh
        subdivide()
        print_mesh()
    elif key == 'i': # inflate mesh
        inflate()
        
    elif key == 'r': # toggle random colors
        showRandomColors = not showRandomColors
        
    elif key == 'c': # toggle showing current corner
        currentCornerVisible = not currentCornerVisible
        
    elif key == 'q': # quit the program
        exit()






# remember where the user first clicked
def mousePressed():
    global mouseX_old, mouseY_old
    mouseX_old = mouseX
    mouseY_old = mouseY






# change the object rotation matrix while the mouse is being dragged
def mouseDragged():
    global rot_mat
    global mouseX_old, mouseY_old
    
    if (not mousePressed):
        return
    
    dx = mouseX - mouseX_old
    dy = mouseY - mouseY_old
    dy *= -1

    len = sqrt (dx*dx + dy*dy)
    if (len == 0):
        len = 1
    
    dx /= len
    dy /= len
    rmat = PMatrix3D()
    rmat.rotate (len * 0.005, dy, dx, 0)
    rot_mat.preApply (rmat)

    mouseX_old = mouseX
    mouseY_old = mouseY


    
