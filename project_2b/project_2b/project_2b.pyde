# Created by: Ashley Cain

### THE TRICERATOPS ###
### His name is Terry ###

# Object being replicated: triceratops using triceratops()\
# triceratops(): there are parameters of apple which is 1 or 0 and will either create an apple in the mouth of the triceratops or won't
# and there is a colorMod which modifies the red value in each rgb value for the skin color, which is why they look a bit different


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

        #camera (0, -80, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        if(time < 1.5):
            camera (time*10, -time*30, time*120, 0, 0, 0, 0,  1, 0)  # position of the virtual camera
        
            
        background (207, 238, 250)  # clear screen and set background to light blue
        
        # set up the lights
        if(time <= 7.5):
            ambientLight(100, 100, 100)
            lightSpecular(255, 255, 255)
            directionalLight (100, 100, 100, 0, 5, -4)
        else:
            directionalLight (100-(time - 7.5) * 10, 100-(time - 7.5) * 10, 100-(time - 7.5) * 10, 0, 5, -4)
            ambientLight(100 -(time - 7.5) * 10, 100-(time - 7.5) * 10, 100-(time - 7.5) * 10)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (50.0)
    
    
    ### triceratops 1 ###
        pushMatrix()
        translate(-30, 0, 30)
        
        ### Movement ###
        if(time <= 1.67):
            rotateY(1.5*time)
        else:
            rotateY(2.5)
        if(time > 3 and time <= 4.6):
            translate((time - 3)*-20, 0, (time - 3)*10)
            #rotateY(2.5)
        if(time > 4.6 and time < 5.5):
            translate(-32, 0, 16)
        if(time >= 5.5 and time <= 7.5):
            translate(-32, 0, 16)
            rotateY(1.5 * (time - 5.5))
        if(time > 7.5):
            if(time < 15):
                translate(-32 + 15 * (time - 7.5), 0, 16)
            else:
                translate(-32 + 15 * (15 - 7.5), 0, 16)
            rotateY(3)
            background (207 - (time - 7.5)*9, 238 - (time - 7.5)*20, 250 - (time - 7.5)*15)
            
        
        
        
        
        triceratops(0, 1)
        popMatrix()
        
        
    ### triceratops 2 ###
        pushMatrix()
        
        # initial location is (60, -50, 38)
        translate(60, -50, 38)
        rotateY(-0.65)
        if(time >= 2 and time <= 3): 
            x = -10 * (time - 2)
            y = (0.5) * ((x)*(x))
            translate(x, y, 0)
        if(time > 3):
            # final location on ground(50, 0, 38)
            translate(-10, 50, 0)
        if(time < 4.8):
            triceratops(1, 2)
        else:
            triceratops(0, 2)
        
        popMatrix()
        
    ### YUM! ###
        if(time >= 4.8 and time <= 7):
            pushMatrix()
            fill(255, 255, 255)
            textMode(SHAPE)
            textSize(80)
            text("YUM!", -80, -50, -160)
            popMatrix()
    
    ### tree ###
        pushMatrix()
        tree(1)
        popMatrix()
        
    ### ground ###
        fill(121, 208, 33)
        pushMatrix()
        translate(0, 320, 0)
        box(500)
        popMatrix()
        
        
    except Exception:
        traceback.print_exc()


def tree(type):
    if(type == 1):
        fill(0, 255, 0)
    
    #translate(-60, 30, -200)
    pushMatrix()
    translate(90, -40, 38)
    scale(1, 1.5, 1)
    sphere(30)
    popMatrix()
    
    fill(164,116,73)
    pushMatrix()
    translate(95, -10, 38)
    scale(10, 30, 10)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    translate(68, -10, 38)
    sphere(3)
    popMatrix()
    
    pushMatrix()
    translate(60, -42, 44)
    sphere(3)
    popMatrix()
    
    pushMatrix()
    translate(66, -67, 40)
    sphere(3)
    popMatrix()
    
    
    
    
def triceratops (apple, colorMod):
    
    ## Box for Body
    fill(143/colorMod, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    scale(2, 1, 0.8)
    translate(0, 1, 0)
    box(12)
    popMatrix()
    
    ## Box for Back Ridge
    fill(147/colorMod, 112, 219)
    pushMatrix()
    rotateY(radians(40))
    scale(1.8, 1, 0.2)
    translate(0, -2, 0)
    box(12)
    popMatrix()
    
    ## Box for Tail
    fill(143/colorMod, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 1.2, 1)
    translate(12, 1, 0)
    box(8)
    popMatrix()
    
    ## Spheres for Tail Bumps
    fill(204/colorMod, 204, 255)
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
    fill(143/colorMod, 153, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(80))
    scale(4, 10, 4)
    translate(0.85, -2.1, 0)
    cone()
    popMatrix()
    
    ## Box for Tummy
    fill(102/colorMod, 51, 153)
    pushMatrix()
    rotateY(radians(40))
    scale(1.6, 0.5, 0.7)
    translate(-2.5, 11, 0)
    box(12)
    popMatrix()
    
    ## Cylinder for Crown
    fill(204/colorMod, 204, 255)
    pushMatrix()
    rotateY(radians(130))
    scale(8.5, 8.5, 1)
    translate(0, -1.25, -11)
    cylinder()
    popMatrix()
    
    ## Cylinder for Crown Detail
    fill(106/colorMod,90, 205)
    pushMatrix()
    rotateY(radians(130))
    scale(6.6, 6.6, 1)
    translate(0, -1.25, -11.5)
    cylinder()
    popMatrix()
    
    ## Box for Head
    fill(147/colorMod, 112, 219)
    pushMatrix()
    rotateY(radians(40))
    scale(0.8, .9, 1)
    translate(-13, -7, 0)
    box(7)
    popMatrix()
    
    ## Cones for Horns
    ## NO COLOR MOD
    fill(240, 240, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(-90))
    scale(1.5, 4, 1.5)
    translate(5.25, -4, 1.25)
    cone()
    popMatrix()
    
    ## NO COLOR MOD
    fill(240, 240, 255)
    pushMatrix()
    rotateY(radians(40))
    rotateZ(radians(-90))
    scale(1.5, 4, 1.5)
    translate(5.25, -4, -1.25)
    cone()
    popMatrix()
    
    ## Box for Head
    fill(150/colorMod, 111, 214)
    pushMatrix()
    rotateY(radians(40))
    scale(0.8, 1.35, 1)
    translate(-18, -1.25, 0)
    box(7)
    popMatrix()
    
    ## Sphere for Eye 1
    ## NO COLOR MOD
    fill(255, 255, 255)
    pushMatrix()
    rotateY(40)
    translate(-2, -3.5, -15)
    sphere(1.7)
    popMatrix()
    
    ##Sphere for Pupil 1
    ## NO COLOR MOD
    fill(0, 0, 0)
    pushMatrix()
    rotateY(40)
    translate(-3, -3.5, -15)
    sphere(1)
    popMatrix()
    
    ## Sphere for Eye 2
    ## NO COLOR MOD
    fill(255, 255, 255)
    pushMatrix()
    rotateY(40)
    translate(3, -3.5, -15)
    sphere(1.7)
    popMatrix()
    
    ## Sphere for Pupil 2
    ## NO COLOR MOD
    fill(0, 0, 0)
    pushMatrix()
    rotateY(40)
    translate(4, -3.5, -15)
    sphere(1)
    popMatrix()
    
    ## Box for Mouth(top)
    fill(150/colorMod,111,214)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.4, 1)
    translate(-18, -4.4, 0)
    box(7)
    popMatrix()
    
    ## Box for Mouth(bottom)
    fill(150/colorMod,111,214)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.3, 1)
    translate(-18, 6.5, 0)
    box(7)
    popMatrix()
    
    ##Box for Tongue
    ## NO COLOR MOD
    fill(255, 0, 0)
    pushMatrix()
    rotateY(radians(40))
    scale(1, 0.3, 1)
    translate(-18, 5, 0)
    box(4)
    popMatrix()
    
    if(apple == 1):
        fill(255, 0, 0)
        pushMatrix()
        rotateY(radians(40))
        translate(-23, 1, 0)
        sphere(3)
        popMatrix()
    
    ##Box for Leg 1
    fill(167/colorMod, 107, 207)
    pushMatrix()
    rotateY(radians(40))
    scale(1.1, 2, 0.5)
    translate(6, 3, 10)
    box(6)
    popMatrix()
    
    ##Box for Leg 2
    pushMatrix()
    rotateY(radians(40))
    scale(1.1, 2, 0.5)
    translate(6, 3, -10)
    box(6)
    popMatrix()
    
    ##Box for Leg 3
    pushMatrix()
    rotateY(radians(40))
    scale(0.85, 2, 0.5)
    translate(-8, 3, 10)
    box(6)
    popMatrix()
    
    ##Box for Leg 4
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
