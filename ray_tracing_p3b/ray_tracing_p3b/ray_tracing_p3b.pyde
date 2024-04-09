# Created by Ashley Cain
# This is the provided code for the ray tracing project.
#
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

from __future__ import division
import traceback

class Light:
    def __init__(self, x, y, z, r, g, b):
        self.pos = PVector(x, y, z)
        self.light_color = [r, g, b]

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

class Surface_Material:
    def __init__(self, dr, dg, db, ar, ag, ab, sr, sg, sb, specularPower, k_refl):
        self.diffuse = (dr, dg, db)
        self.ambiant = (ar, ag, ab)
        self.specular_color = (sr, sg, sb)
        self.specular_power = specularPower
        self.k_refl = k_refl

class Hit:
    def __init__(self, Shape, normal_vector, t_value, intersection_point, ray):
        self.Shape = Shape
        self.normal_vector = normal_vector
        self.t_value = t_value
        self.intersection = intersection_point
        self.ray = ray
        
class Sphere:
    def __init__(self, x, y, z, radius, surface_mat):
        self.radius = radius
        self.center = [x, y, z]
        self.material = surface_material
        
    def intersect(self, er):
        dx = er.direction.x
        dy = er.direction.y
        dz = er.direction.z
        
        ux = er.origin.x - self.center[0]
        uy = er.origin.y - self.center[1]
        uz = er.origin.z - self.center[2]

        r = self.radius
        
        a = (dx**2) + (dy**2) + (dz**2)
        b = ((2*dx*ux) + (2*dy*uy) + (2*dz*uz))
        c = (ux**2) + (uy**2) + (uz**2) - (r**2)
            
        sqrt_val = (b**2) - (4*a*c)
        if sqrt_val < 0:
            return -10
        else:
            t_val = (-b - sqrt(sqrt_val)) / (2*a)
            return t_val
            
class Triangle:
    def __init__(self, vertex1, vertex2, vertex3, surface_mat):
        self.v1 = PVector(vertex1[0], vertex1[1], vertex1[2])
        self.v2 = PVector(vertex2[0], vertex2[1], vertex2[2])
        self.v3 = PVector(vertex3[0], vertex3[1], vertex3[2])
        
        self.v1v2 = PVector.sub(self.v2, self.v1).normalize()
        self.v2v3 = PVector.sub(self.v3, self.v2).normalize()
        self.v3v1 = PVector.sub(self.v1, self.v3).normalize()
        
        self.material = surface_material
        
        self.normal_vector = PVector.cross(self.v1v2, self.v2v3).normalize()
        
    def intersect(self, er):
        denominator = PVector.dot(self.normal_vector, er.direction)
        if denominator != 0:
            numerator = PVector.dot(self.normal_vector, PVector.sub(self.v1, er.origin))
            return numerator/denominator
        else:
            return -10
             
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
    

scene_shapes = []
fov = 0
eye = []
uvw = []
scene_lights = []
surface_material = 0
background_color = color(0, 0, 0)    
debug_flag = False   
vertices= []
shadow_term = 1

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
    elif key == '-':
        interpreter("11_star.cli")



# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global vertices, scene_shapes, fov, eye, uvw, scene_lights, surface_material, background_color
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
            scene_shapes.append(Sphere(x, y, z, radius, surface_material))
            
        elif words[0] == 'fov':
            fov = float(words[1])
            
        elif words[0] == 'eye':
            eye = [float(words[1]), float(words[2]), float(words[3])]
            
        elif words[0] == 'uvw':
            u = [float(words[1]), float(words[2]), float(words[3])]
            v = [float(words[4]), float(words[5]), float(words[6])]
            w = [float(words[7]), float(words[8]), float(words[9])]
            uvw = [u, v, w]
            
        elif words[0] == 'background':
            background_color= [float(words[1]),float(words[2]), float(words[3])]
        
        elif words[0] == 'light':
            scene_lights.append(Light(float(words[1]), float(words[2]), float(words[3]), float(words[4]), float(words[5]), float(words[6])))
            
        elif words[0] == 'surface':
            surface_material = Surface_Material(float(words[1]), float(words[2]), float(words[3]), float(words[4]), float(words[5]), float(words[6]), float(words[7]),float(words[8]), float(words[9]), float(words[10]),float(words[11]))
            
        elif words[0] == 'begin':
            vertices = []
            
        elif words[0] == 'vertex':
            vertices.append([float(words[1]), float(words[2]), float(words[3])])
            
        elif words[0] == 'end':
            scene_shapes.append(Triangle(vertices[0], vertices[1], vertices[2], surface_material))
            
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
            
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
            
        else:
            print ("unknown command: " + word[0])

# render the ray tracing scene
def render_scene():
    global debug_flag, scene_lights, scene_shapes, background_color, uvw, fov, eye, surface_material
    
    # double for-loop where each iteration is a new pixel at (i, j)
    for j in range(height):
        for i in range(width):
            
            d = float(1 / (tan(radians(fov / 2))))
            U = float(((2*i)/width) - 1)
            V = -1 * float(((2*j)/height) - 1)

            x1 = uvw[2][0] * -d
            x2 = uvw[2][1] * -d
            x3 = uvw[2][2] * -d
            x = [x1, x2, x3]

            y1 = uvw[1][0] * V
            y2 = uvw[1][1] * V
            y3 = uvw[1][2] * V
            y = [y1, y2, y3]

            z1 = uvw[0][0] * U
            z2 = uvw[0][1] * U
            z3 = uvw[0][2] * U
            z = [z1, z2, z3]

            eye_origin = PVector(eye[0], eye[1], eye[2])
            eye_direction = PVector(x1 + y1 + z1, x2 + y2 + z2, x3 + y3 + z3)

            eye_ray = Ray(eye_origin, eye_direction)
            
            scene_hit = rayIntersectScene(eye_ray)
            pix_shade = background_color
            
            if scene_hit != None:
                pix_shade = (shade(scene_hit, scene_hit.ray, 10))

            pix_color = color(pix_shade[0], pix_shade[1], pix_shade[2])
            
            debug_flag = False
            if i == 211 and j == 131:
                debug_flag = True
                print "uvw vectors:", uvw
                print "scalar u, v:", U, V
                print "ray origin: ", eye
                print "ray direction: ", eye_ray.direction 

            set (i, j, pix_color)         # draw the pixel with the calculated color


def rayIntersectScene(er):
    global scene_shapes, background_color
    
    min_t = 100000000
    
    closest_hit = None
            
    for Shape in scene_shapes:
        
        if isinstance(Shape, Sphere):
            tval = Shape.intersect(er)
            if tval == -10:
                continue
            if tval >= 0 and tval < min_t:
                min_t = tval
                xt = er.origin.x + min_t * er.direction.x
                yt = er.origin.y + min_t * er.direction.y
                zt = er.origin.z + min_t * er.direction.z
                intersection_point = PVector(xt, yt, zt)
            
                norm_x = intersection_point.x - Shape.center[0]
                norm_y = intersection_point.y - Shape.center[1]
                norm_z = intersection_point.z - Shape.center[2]
                normal_vector = PVector(norm_x, norm_y, norm_z).normalize()
                
                closest_hit = Hit(Shape, normal_vector, min_t, intersection_point, er)
        
        if isinstance(Shape, Triangle):
            tval = Shape.intersect(er)
            if tval == -10:
                continue
            if tval > 0 and tval < min_t:
                P = PVector.add(er.origin, PVector.mult(er.direction, tval))
                triple1 = PVector.dot(PVector.cross(PVector.sub(P, Shape.v1),   PVector.sub(Shape.v2, Shape.v1)), Shape.normal_vector)
                triple2 = PVector.dot(PVector.cross(PVector.sub(P, Shape.v2),   PVector.sub(Shape.v3, Shape.v2)), Shape.normal_vector)
                triple3 = PVector.dot(PVector.cross(PVector.sub(P, Shape.v3),   PVector.sub(Shape.v1, Shape.v3)), Shape.normal_vector)                 
                    
                if(triple1 > 0) == (triple2 > 0) == (triple3 > 0):
                    minT = tval
                    t_normal = Shape.normal_vector
                    if PVector.dot(Shape.normal_vector, er.direction) >= 0:
                        t_normal = PVector.mult(Shape.normal_vector, -1)
                    
                    closest_hit = Hit(Shape, t_normal, min_t, P, er)
    
    return closest_hit

def shade(hit, ray, maxDep):
    global scene_lights, background_color
    
    if hit == None:
        return background_color
    
    R = 0
    G = 0
    B = 0
    
    tinyOffset = PVector.mult(hit.normal_vector, 0.0001)
    
    if maxDep > 0 and hit.Shape.material.k_refl > 0:
        rr_origin = PVector.add(hit.intersection, tinyOffset)
        d_scalar = PVector.dot(hit.normal_vector, ray.direction) * -2
        rr_direction = PVector.add(ray.direction, PVector.mult(hit.normal_vector, d_scalar)).normalize()
        rr = Ray(rr_origin, rr_direction)
        
        rr_hit = rayIntersectScene(rr)
        rr_color = shade(rr_hit, rr, maxDep - 1)
        
        R += rr_color[0] * hit.Shape.material.k_refl
        G += rr_color[1] * hit.Shape.material.k_refl
        B += rr_color[2] * hit.Shape.material.k_refl

        
    for light in scene_lights:
        shadow_term = 1
        sr_origin = PVector.add(hit.intersection, tinyOffset)
        sr_direction = PVector.sub(light.pos, hit.intersection).normalize()
        sr = Ray(sr_origin, sr_direction)
        
        sr_hit = rayIntersectScene(sr)
        
        d = PVector.dist(light.pos, hit.intersection)
        
        if sr_hit != None and hit.t_value < d and 0 < hit.t_value:
            shadow_term = 0
        
        if isinstance(hit.Shape, Sphere):
            Nx = hit.intersection.x - hit.Shape.center[0]
            Ny = hit.intersection.y - hit.Shape.center[1]
            Nz = hit.intersection.z - hit.Shape.center[2]
            N = PVector(Nx, Ny, Nz)
            
        if isinstance(hit.Shape, Triangle):
            N = hit.normal_vector.normalize()
        
        L = PVector.sub(light.pos, hit.intersection).normalize()
        D = hit.ray.direction
        
        H = PVector.sub(L, D).normalize()
        
        if debug_flag:
            print "N: ", N
            print "L: ", L
            print "intersection_point: ", hit.intersection

        diffuse_coefficient = max(0, PVector.dot(N, L))

        dr = hit.Shape.material.diffuse[0] * light.light_color[0] * diffuse_coefficient
        dg = hit.Shape.material.diffuse[1] * light.light_color[1] * diffuse_coefficient
        db = hit.Shape.material.diffuse[2] * light.light_color[2] * diffuse_coefficient
        
        specular_coefficient = max(0, PVector.dot(H, N))** hit.Shape.material.specular_power
        
        specr = hit.Shape.material.specular_color[0] * light.light_color[0] * specular_coefficient
        specg = hit.Shape.material.specular_color[1] * light.light_color[1] * specular_coefficient
        specb = hit.Shape.material.specular_color[2] * light.light_color[2] * specular_coefficient
        
        R += shadow_term * (dr + specr)
        G += shadow_term * (dg + specg)
        B += shadow_term * (db + specb)
    
    
    R += hit.Shape.material.ambiant[0]
    G += hit.Shape.material.ambiant[1]
    B += hit.Shape.material.ambiant[2]

    return [R, G, B]

def normalize(x, y, z):
    unit = sqrt((x**2) + (y**2) + (z**2))
    return [float(x/unit), float(y/unit), float(z/unit)]
    
def reset_scene():
    global scene_shapes, scene_lights, background_color, fov, eye, uvw, surface_material
    scene_shapes = []
    fov = 0
    eye = []
    uvw = []
    scene_lights = []
    surface_material = 0
    background_color = 0

# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass
