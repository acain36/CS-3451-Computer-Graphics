# Created by: Ashley Cain

### THE TRICERATOPS ###
### His name is Terry ###

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        
        ### Variable time to help with the rotation of the object
        global time
        time += 0.01

        camera (0, -30, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (207, 238, 250)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(100, 100, 100);
        lightSpecular(255, 255, 255)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (50.0)
        
        pushMatrix()
        #rotateY(time)
        triceratops()
        popMatrix()
        
        
    except Exception:
        traceback.print_exc()



def triceratops ():
    
    ## Box for Body
    fill(143, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    scale(2, 1, 0.8)
    translate(0, 1, 0)
    box(12)
    popMatrix()
    
    ## Box for Back Ridge
    fill(147,112,219)
    pushMatrix()
    rotateY(radians(40))
    scale(1.8, 1, 0.2)
    translate(0, -2, 0)
    box(12)
    popMatrix()
    
    ## Box for Tail
    fill(143, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 1.2, 1)
    translate(12, 1, 0)
    box(8)
    popMatrix()
    
    ## Spheres for Tail Bumps
    fill(204, 204, 255)
    pushMatrix()
    rotateY(40)
    translate(-0.7, -2.2, 17)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    rotateY(40)
    translate(-0.7, -2.2, 20)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    rotateY(40)
    translate(-0.7, -2.2, 23)
    sphere(1)
    popMatrix()
    
    pushMatrix()
    rotateY(40)
    translate(-0.7, -2.2, 26)
    sphere(1)
    popMatrix()
    
    ## Cone for Tail
    fill(143, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(80))
    scale(4, 10, 4)
    translate(0.85, -2.1, 0)
    cone()
    popMatrix()
    
    ## Box for Tummy
    fill(102, 51, 153)
    pushMatrix()
    rotateY(radians(40))
    scale(1.6, 0.5, 0.7)
    translate(-2.5, 11, 0)
    box(12)
    popMatrix()
    
    ## Cylinder for Crown
    fill(204, 204, 255)
    pushMatrix()
    rotateY(radians(130))
    scale(8.5, 8.5, 1)
    translate(0, -1.25, -11)
    cylinder()
    popMatrix()
    
    ## Cylinder for Crown Detail
    fill(106,90,205)
    pushMatrix()
    rotateY(radians(130))
    scale(6.6, 6.6, 1)
    translate(0, -1.25, -11.5)
    cylinder()
    popMatrix()
    
    ## Box for Head
    fill(147,112,219)
    pushMatrix()
    rotateY(radians(40))
    scale(0.8, .9, 1)
    translate(-13, -7, 0)
    box(7)
    popMatrix()
    
    ## Cones for Horns
    fill(240, 240, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(-90))
    scale(1.5, 4, 1.5)
    translate(5.25, -4, 1.25)
    cone()
    popMatrix()
    
    fill(240, 240, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(-90))
    scale(1.5, 4, 1.5)
    translate(5.25, -4, -1.25)
    cone()
    popMatrix()
    
    ## Box for Head
    fill(150,111,214)
    pushMatrix()
    rotateY(radians(40))
    scale(0.8, 1.35, 1)
    translate(-18, -1.25, 0)
    box(7)
    popMatrix()
    
    ## Sphere for Eye 1
    fill(255, 255, 255)
    pushMatrix()
    rotateY(40)
    translate(-2, -3.5, -15)
    sphere(1.7)
    popMatrix()
    
    ##Sphere for Pupil 1
    fill(0, 0, 0)
    pushMatrix()
    rotateY(40)
    translate(-3, -3.5, -15)
    sphere(1)
    popMatrix()
    
    ## Sphere for Eye 2
    fill(255, 255, 255)
    pushMatrix()
    rotateY(40)
    translate(3, -3.5, -15)
    sphere(1.7)
    popMatrix()
    
    ## Sphere for Pupil 2
    fill(0, 0, 0)
    pushMatrix()
    rotateY(40)
    translate(4, -3.5, -15)
    sphere(1)
    popMatrix()
    
    ## Box for Mouth(top)
    fill(150,111,214)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.4, 1)
    translate(-18, -4.4, 0)
    box(7)
    popMatrix()
    
    ## Box for Mouth(bottom)
    fill(150,111,214)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.3, 1)
    translate(-18, 6.5, 0)
    box(7)
    popMatrix()
    
    ##Box for Tongue
    fill(255, 0, 0)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.3, 1)
    translate(-18, 5, 0)
    box(4)
    popMatrix()
    
    ##Box for Leg 1
    fill(167, 107, 207)
    pushMatrix()
    rotateY(radians(40))
    scale(1.1, 2, 0.5)
    translate(6, 3, 10)
    box(6)
    popMatrix()
    
    ##Box for Leg 2
    fill(167, 107, 207)
    pushMatrix()
    rotateY(radians(40))
    scale(1.1, 2, 0.5)
    translate(6, 3, -10)
    box(6)
    popMatrix()
    
    ##Box for Leg 3
    fill(167, 107, 207)
    pushMatrix()
    rotateY(radians(40))
    scale(0.85, 2, 0.5)
    translate(-8, 3, 10)
    box(6)
    popMatrix()
    
    ##Box for Leg 4
    fill(167, 107, 207)
    pushMatrix()
    rotateY(radians(40))
    scale(0.85, 2, 0.5)
    translate(-8, 3, -10)
    box(6)
    popMatrix()
    
    
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
# Draw a cone pointing in the -y direction (up), with radius 1, with y in range [-1, 1]
def cone(sides=50):
    sides = int(sides)

    # draw triangles making up the sides of the cone
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        theta_next = 2.0 * PI * (i + 1) / sides
        
        beginShape()
        normal(cos(theta), 0.6, sin(theta))
        vertex(cos(theta), 1.0, sin(theta))
        normal(cos(theta_next), 0.6, sin(theta_next))
        vertex(cos(theta_next), 1.0, sin(theta_next))
        normal(0.0, -1.0, 0.0)
        vertex(0.0, -1.0, 0.0)
        endShape()

    # draw the cap of the cone
    beginShape()
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        vertex(cos(theta), 1.0, sin(theta))
    endShape()
