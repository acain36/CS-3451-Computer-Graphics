# Created by Ashley Cain
# This is the provided code for the ray tracing project.
#
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

from __future__ import division
import traceback

#light object
class Light:
    def __init__(self, x, y, z, r, g, b):
        self.pos = [x, y, z]
        self.light_color = [r, g, b]
        
        
#ray object -> origin, direction
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        
        
#surface_material
class Surface_Material:
    def __init__(self, dr, dg, db, ar, ag, ab, sr, sg, sb, spec_power, k_refl):
        self.diffuse = (dr, dg, db)
        self.ambiant = (ar, ag, ab)
        self.specular_color = (sr, sg, sb)
        self.specular_power = spec_power
        self.k_refl = k_refl
        
        
        
#sphere object
class Sphere:
    def __init__(self, x, y, z,radius, surface_mat):
        self.radius = radius
        self.center = [x, y, z]
        self.material = surface_mat
        
#Hit object
class Hit:
    def __init__(self, hit_sphere, normal_vector, t_value, intersection_point):
        self.Sphere = hit_sphere
        self.normal_vector = normal_vector
        self.t_value = t_value
        self.intersection_point = intersection_point
        

#define global variables to be set according to information read in files

scene_spheres = []
# will hold all sphere objects in the scene
fov = 0
eye = []
uvw = []
scene_lights = []
# will hold all light objects in scene
surface_material = 0
scene_background = color(0, 0, 0)    
debug_flag = False   # print debug information when this is True

def setup():
    size(320, 320) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    frameRate(30)

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# read and interpret a scene description .cli file based on which key has been pressed
def handleKeyPressed():
    if key == '1':
        interpreter("01_one_sphere.cli")
    elif key == '2':
        interpreter("02_three_spheres.cli")
    elif key == '3':
        interpreter("03_shiny_sphere.cli")
    elif key == '4':
        interpreter("04_many_spheres.cli")
    elif key == '5':
        interpreter("05_one_triangle.cli")
    elif key == '6':
        interpreter("06_icosahedron_and_sphere.cli")
    elif key == '7':
        interpreter("07_colorful_lights.cli")
    elif key == '8':
        interpreter("08_reflective_sphere.cli")
    elif key == '9':
        interpreter("09_mirror_spheres.cli")
    elif key == '0':
        interpreter("10_reflections_in_reflections.cli")



# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global scene_spheres, fov, eye, uvw, scene_lights, surface_material, scene_background
    reset_scene()  # you should initialize any data structures that you will use here
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse the lines in the file in turn
    for line in lines:
        # what this does: will go through files looking for key words
        # associated with objects below and will set values in case of 
        # encountering that word
        
        # DONE: for incomplete fns, use float(words[*]) to get attribute vals
        # and assign to variables
        words = line.split()  # split up the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            radius = float(words[1])
            #use sphere class to make a sphere
            #add sphere to list of spheres
            scene_spheres.append(Sphere(x, y, z, radius, surface_material))
            # call your sphere making routine here
            # for example: create_sphere(x,y,z,radius)
        elif words[0] == 'fov':
            fov = float(words[1])
        elif words[0] == 'eye':
            #set eye
            eye = [float(words[1]), float(words[2]), float(words[3])]
            
        elif words[0] == 'uvw': 
            #set uvw
            u = [float(words[1]), float(words[2]), float(words[3])]
            v = [float(words[4]), float(words[5]), float(words[6])]
            w = [float(words[7]), float(words[8]), float(words[9])]
            
            uvw = [u, v, w]
            
        elif words[0] == 'background':
            #set background color
            scene_background= [float(words[1]),float(words[2]), float(words[3])]
        
        elif words[0] == 'light':
            #attributes of a single light
            #use light class to make a light
            #add light to list of lights
            scene_lights.append(Light(float(words[1]), float(words[2]), float(words[3]), float(words[4]), float(words[5]), float(words[6])))
            
        elif words[0] == 'surface':
            #set surface material
            surface_material = Surface_Material(float(words[1]), float(words[2]), float(words[3]), float(words[4]), float(words[5]), float(words[6]), float(words[7]),float(words[8]), float(words[9]), float(words[10]),float(words[11]))
            
        elif words[0] == 'begin':
            # 3B
            pass
        elif words[0] == 'vertex':
            #3B
            pass
        elif words[0] == 'end':
            #3B
            pass
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

# render the ray tracing scene
def render_scene():
    global debug_flag, scene_lights, scene_spheres, scene_background, uvw, fov, eye, surface_material
    #using eye as origin, calculate focal distance as an int
    distance = float(1 / (tan(radians(fov / 2))))
    
    # double for-loop where each iteration is a new pixel at (i, j)
    for j in range(height):
        for i in range(width):
            # Current Pixel @ (i, j)
            
            #calculate U
            U = float(((2*i)/width) - 1)
            
            #calculate V
            V = -1 * float(((2*j)/height) - 1)
            
            #calculate ray direction vector using uvw
            #T1 = -distance * w
            #T1 = -distance*[uvw[2][0], uvw[2][1], uvw[2][2]]
            w1 = uvw[2][0] * -distance
            w2 = uvw[2][1] * -distance
            w3 = uvw[2][2] * -distance

            #T2 = V*(v)
            #T2 = V*[uvw[1][0], uvw[1][1], uvw[1][2]]
            v1 = uvw[1][0] * V
            v2 = uvw[1][1] * V
            v3 = uvw[1][2] * V
            
            #T3 = U*(u)
            #T3 = U*[uvw[0][0], uvw[0][1], uvw[0][2]]
            u1 = uvw[0][0] * U
            u2 = uvw[0][1] * U
            u3 = uvw[0][2] * U
            
            #Ray direction vector = T1 + T2 + T3
            #normalize this direction vector
            ray_direction_vector = normalized(w1 + v1 + u1, w2 + v2 + u2, w3 + v3 + u3)
            
            #create eye ray with origin and direction
            eye_ray = Ray(eye, ray_direction_vector)
            
            #call hit_point_color(eye_ray) which will return color depending on closest hit
            pixel = hit_point_color(eye_ray)
            
            pix_color = color(pixel[0], pixel[1], pixel[2])
            # Maybe set a debug flag to true for ONE pixel.
            # Have routines (like ray/sphere intersection)print extra information if this flag is set.
            # Below: checks the pixel at 160,160 and can print info for us to compare against
            debug_flag = False
            if i == 211 and j == 131:
                debug_flag = True
                print "uvw vectors:", uvw
                print "scalar u, v:", U, V
                print "ray origin: ", eye
                print "ray direction: ", eye_ray.direction 

            # create an eye ray for pixel (i,j) and cast it into the scene
            # calculate the correct color with diffuse method
            #pix_color = color(0.8, 0.2, 0.3)  # you will calculate the correct pixel color here using ray tracing
            set (i, j, pix_color)         # draw the pixel with the calculated color






### COMPLETED ###
#hit_point(eye_ray) returns the closest hit point color
    #minT = large number
    #Create for loop that iterated through each sphere in scene_spheres
        #intersection(eye_ray, sphere)
        #interpret t-value
            #if(t-value is positive & non-imaginary)
            # calculate intersection point (plug t-value into ray eq)
            # calculate normal vector (intersection point -> center of sphere)
            # store intersection point, material, normal vector
            # minT = t-value
    #Exit for-loop
    #if(minT <= large number)
        #set pixel color to diffuse(closestHit)
    #else 
        #return  the background color 
### COMPLETED ###

def hit_point_color(er):
    global scene_spheres, scene_background
    
    min_t = 100000000
    #closest_hit will be the hit object that has lowest t-val
    #closest hit to the eye and one that will determine the pixel color
    closest_hit = None
    
    for Sphere in scene_spheres:
        
        tval = intersection(er, er.origin[0] - Sphere.center[0], er.origin[1] - Sphere.center[1], er.origin[2] - Sphere.center[2] , Sphere)
        if tval >= 0 and tval < min_t:
            min_t = tval
            
            #calculate intersection point
            #x(t) = ox + t*dx
            xt = er.origin[0] + min_t * er.direction[0]
            yt = er.origin[1] + min_t * er.direction[1]
            zt = er.origin[2] + min_t * er.direction[2]
            intersection_point = [xt, yt, zt]
            
            #calculate normal vector = intersection_point - center
            norm_x = xt - Sphere.center[0]
            norm_y = yt - Sphere.center[1]
            norm_z = zt - Sphere.center[2]
            normal_vector = normalized(norm_x, norm_y, norm_z)
            
            #set the Hit object with the information calculated here
            closest_hit = Hit(Sphere, normal_vector, min_t, intersection_point)
            
    if closest_hit == None:
        return scene_background
    
    return diffuse(closest_hit)
### COMPLETED ###




### COMPLETED ###
#intersection(eye_ray, sphere) will return tval for hit point or -99999999
    #ray equation
    #sphere equation
    #solve for t-values by combining
    #return t-value
### COMPLETED ###

def intersection(er, ux, uy, uz, Sphere):
    #implicit sphere equation
    #finding variable values
    #dx, dy, dz
    dx = er.direction[0]
    dy = er.direction[1]
    dz = er.direction[2]
    
    #r = radius
    r = Sphere.radius
    
    #a = dx^2 + dy^2 + dz^2
    #b = 2*dx*ux + 2*dy*uy + 2*dz*uz
    #c = ux^2 + uy^2 + uz^2 - r^2
    a = (dx**2) + (dy**2) + (dz**2)
    b = ((2*dx*ux) + (2*dy*uy) + (2*dz*uz))
    c = (ux**2) + (uy**2) + (uz**2) - (r**2)
    
    if debug_flag:
        print "testing intersection with the sphere whose color is ", Sphere.material.diffuse # change these variable names to match the rest of your code!
        print "a, b, c coefficients of the quadratic: ", a, b, c
        print "dx: ", dx
        print "dy: ", dy
        print "dz: ", dz
        print "ux: ", ux
        print "uy: ", uy
        print "uz: ", uz
        print "ray origin: ", er.origin
        
    #quadratic equation
    #checking inside of square root
    sqrt_val = (b**2) - (4*a*c)
    if sqrt_val > 0:
        t_val = (-b - sqrt(sqrt_val)) / (2*a)
        return t_val
    else:
        return -1
### COMPLETED ###    
    
    
    


### COMPLETED ###
#TODO: diffuse(hit) will calculate the color to color the pixel
    #create a color(r,g,b) that will total all colors from light sources
    #for(each light in scene_lights)
        #calculate L-vector
        #normalize L-vector
        #calculate N*L
        #calculate resultant color = (hit diffuse)*(light color)*max(O, N*L)
        #add to the total color
    #return the total color
### COMPLETED ###
def diffuse(hitObj):
    global scene_lights
    total_r = 0
    total_g = 0
    total_b = 0
    
    for Light in scene_lights:
        #calculate L vector
        L_x = Light.pos[0] - hitObj.intersection_point[0]
        L_y = Light.pos[1] - hitObj.intersection_point[1]
        L_z = Light.pos[2] - hitObj.intersection_point[2]
        L = normalized(L_x, L_y, L_z)
        
        #calculate N vector
        N_x = hitObj.intersection_point[0] - hitObj.Sphere.center[0]
        N_y = hitObj.intersection_point[1] - hitObj.Sphere.center[1]
        N_z = hitObj.intersection_point[2] - hitObj.Sphere.center[2]
        N = normalized(N_x, N_y, N_z)
        
        if debug_flag:
            print "N: ", N
            print "L: ", L
            print "intersection_point: ", hitObj.intersection_point
            
        #calculate N and L dot product
        product = 0.0
        for i in range(len(N)):
            product += float(N[i] * L[i])
        
        #the diffuse coefficient
        diffuse_coefficient = max(0, product)
        
        #hit object's diffuse Material
        diffuse_material = hitObj.Sphere.material.diffuse
        
        #r,g,b calculations using (diffuse_material * light_color * diffuse_coefficient)
        
        r = diffuse_material[0] * Light.light_color[0] * diffuse_coefficient
        g = diffuse_material[1] * Light.light_color[1] * diffuse_coefficient
        b = diffuse_material[2] * Light.light_color[2] * diffuse_coefficient
        
        total_r += r
        total_g += g
        total_b += b
    
    diffused_color = [total_r, total_g, total_b]
    return diffused_color
### COMPLETED ###

                

### COMPLETED ###
#normalized(x, y, z) returns a normalized vector
def normalized(x, y, z):
    unit = sqrt((x**2) + (y**2) + (z**2))
    return [float(x/unit), float(y/unit), float(z/unit)]
### COMPLETED ###
    
    
# TODO: here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global scene_spheres, scene_lights, scene_background, fov, eye, uvw, surface_material
    scene_spheres = []
    fov = 0
    eye = []
    uvw = []
    scene_lights = []
    surface_material = 0
    scene_background = 0

# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
