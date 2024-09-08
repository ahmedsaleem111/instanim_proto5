'''
Animation Transcript:
- Drawing In Cube Wireframe
- Annotate Side Lengths
- Pop in Dots
- Pop in Bounds
- Reverse ^^ all simultaneously
'''
import bpy
import numpy as np
import math

FPS = 60

# list of common sample colors (as size-3 numpy array)
colors = {
    'black':                np.array([0,                    0,                  0                   ]),
    'white':                np.array([1,                    1,                  1                   ]),
    'red':                  np.array([1,                    0,                  0                   ]),
    'lime':                 np.array([0,                    1,                  0                   ]),
    'blue':                 np.array([0,                    0,                  1                   ]),
    'yellow':               np.array([1,                    1,                  0                   ]),
    'cyan':                 np.array([0,                    1,                  1                   ]),
    'magenta':              np.array([1,                    0,                  1                   ]),
    'silver':               np.array([0.752941176470588,    0.752941176470588,  0.752941176470588   ]),
    'gray':                 np.array([0.501960784313725,    0.501960784313725,  0.501960784313725   ]),
    'maroon':               np.array([0.501960784313725,    0,                  0                   ]),
    'olive':                np.array([0.501960784313725,    0.501960784313725,  0                   ]),
    'green':                np.array([0,                    0.501960784313725,  0                   ]),
    'purple':               np.array([0.501960784313725,    0,                  0.501960784313725   ]),
    'teal':                 np.array([0,                    0.501960784313725,  0.501960784313725   ]),
    'navy':                 np.array([0,                    0,                  0.501960784313725   ]),
    'dark red':             np.array([0.545098039215686,    0,                  0                   ]),
    'brown':                np.array([0.647058823529412,    0.164705882352941,  0.164705882352941   ]),
    'firebrick':            np.array([0.698039215686274,    0.133333333333333,  0.133333333333333   ]),
    'crimson':              np.array([0.862745098039216,    0.0784313725490196, 0.235294117647059   ]),
    'red':                  np.array([1,                    0,                  0                   ]),
    'tomato':               np.array([1,                    0.388235294117647,  0.27843137254902    ]),
    'coral':                np.array([1,                    0.498039215686275,  0.313725490196078   ]),
    'indian red':           np.array([0.803921568627451,    0.36078431372549,   0.36078431372549    ]),
    'light coral':          np.array([0.941176470588235,    0.501960784313725,  0.501960784313725   ]),
    'dark salmon':          np.array([0.913725490196078,    0.588235294117647,  0.47843137254902    ]),
    'salmon':               np.array([0.980392156862745,    0.501960784313725,  0.447058823529412   ]),
    'light salmon':         np.array([1,                    0.627450980392157,  0.47843137254902    ]),
    'orange red':           np.array([1,                    0.270588235294118,  0                   ]),
    'dark orange':          np.array([1,                    0.549019607843137,  0                   ]),
    'orange':               np.array([1,                    0.647058823529412,  0                   ]),
    'gold':                 np.array([1,                    0.843137254901961,  0                   ]),
    'dark golden rod':      np.array([0.72156862745098,     0.525490196078431,  0.0431372549019608  ]),
    'golden rod':           np.array([0.854901960784314,    0.647058823529412,  0.125490196078431   ]),
    'pale golden rod':      np.array([0.933333333333333,    0.909803921568627,  0.666666666666667   ]),
    'dark khaki':           np.array([0.741176470588235,    0.717647058823529,  0.419607843137255   ]),
    'khaki':                np.array([0.941176470588235,    0.901960784313726,  0.549019607843137   ]),
    'olive':                np.array([0.501960784313725,    0.501960784313725,  0                   ]),
    'yellow':               np.array([1,                    1,                  0                   ]),
    'yellow green':         np.array([0.603921568627451,    0.803921568627451,  0.196078431372549   ]),
    'dark olive green':     np.array([0.333333333333333,    0.419607843137255,  0.184313725490196   ]),
    'olive drab':           np.array([0.419607843137255,    0.556862745098039,  0.137254901960784   ]),
    'lawn green':           np.array([0.486274509803922,    0.988235294117647,  0                   ]),
    'chart reuse':          np.array([0.498039215686275,    1,                  0                   ]),
    'green yellow':         np.array([0.67843137254902,     1,                  0.184313725490196   ]),
    'dark green':           np.array([0,                    0.392156862745098,  0                   ]),
    'green':                np.array([0,                    0.501960784313725,  0                   ]),
    'forest green':         np.array([0.133333333333333,    0.545098039215686,  0.133333333333333   ]),
    'lime':                 np.array([0,                    1,                  0                   ]),
    'lime green':           np.array([0.196078431372549,    0.803921568627451,  0.196078431372549   ]),
    'light green':          np.array([0.564705882352941,    0.933333333333333,  0.564705882352941   ]),
    'pale green':           np.array([0.596078431372549,    0.984313725490196,  0.596078431372549   ]),
    'dark sea green':       np.array([0.56078431372549,     0.737254901960784,  0.56078431372549    ]),
    'medium spring green':  np.array([0,                    0.980392156862745,  0.603921568627451   ]),
    'spring green':         np.array([0,                    1,                  0.498039215686275   ]),
    'sea green':            np.array([0.180392156862745,    0.545098039215686,  0.341176470588235   ]),
    'medium aqua marine':   np.array([0.4,                  0.803921568627451,  0.666666666666667   ]),
    'medium sea green':     np.array([0.235294117647059,    0.701960784313725,  0.443137254901961   ]),
    'light sea green':      np.array([0.125490196078431,    0.698039215686274,  0.666666666666667   ]),
    'dark slate gray':      np.array([0.184313725490196,    0.309803921568627,  0.309803921568627   ]),
    'teal':                 np.array([0,                    0.501960784313725,  0.501960784313725   ]),
    'dark cyan':            np.array([0,                    0.545098039215686,  0.545098039215686   ]),
    'aqua':                 np.array([0,                    1,                  1                   ]),
    'cyan':                 np.array([0,                    1,                  1                   ]),
    'light cyan':           np.array([0.87843137254902,     1,                  1                   ]),
    'dark turquoise':       np.array([0,                    0.807843137254902,  0.819607843137255   ]),
    'turquoise':            np.array([0.250980392156863,    0.87843137254902,   0.815686274509804   ]),
    'medium turquoise':     np.array([0.282352941176471,    0.819607843137255,  0.8                 ]),
    'pale turquoise':       np.array([0.686274509803922,    0.933333333333333,  0.933333333333333   ]),
    'aqua marine':          np.array([0.498039215686275,    1,                  0.831372549019608   ]),
    'powder blue':          np.array([0.690196078431373,    0.87843137254902,   0.901960784313726   ]),
    'cadet blue':           np.array([0.372549019607843,    0.619607843137255,  0.627450980392157   ]),
    'steel blue':           np.array([0.274509803921569,    0.509803921568627,  0.705882352941177   ]),
    'corn flower blue':     np.array([0.392156862745098,    0.584313725490196,  0.929411764705882   ]),
    'deep sky blue':        np.array([0,                    0.749019607843137,  1                   ]),
    'dodger blue':          np.array([0.117647058823529,    0.564705882352941,  1                   ]),
    'light blue':           np.array([0.67843137254902,     0.847058823529412,  0.901960784313726   ]),
    'sky blue':             np.array([0.529411764705882,    0.807843137254902,  0.92156862745098    ]),
    'light sky blue':       np.array([0.529411764705882,    0.807843137254902,  0.980392156862745   ]),
    'midnight blue':        np.array([0.0980392156862745,   0.0980392156862745, 0.43921568627451    ]),
    'navy':                 np.array([0,                    0,                  0.501960784313725   ]),
    'dark blue':            np.array([0,                    0,                  0.545098039215686   ]),
    'medium blue':          np.array([0,                    0,                  0.803921568627451   ]),
    'blue':                 np.array([0,                    0,                  1                   ]),
    'royal blue':           np.array([0.254901960784314,    0.411764705882353,  0.882352941176471   ]),
    'blue violet':          np.array([0.541176470588235,    0.168627450980392,  0.886274509803922   ]),
    'indigo':               np.array([0.294117647058824,    0,                  0.509803921568627   ]),
    'dark slate blue':      np.array([0.282352941176471,    0.23921568627451,   0.545098039215686   ]),
    'slate blue':           np.array([0.415686274509804,    0.352941176470588,  0.803921568627451   ]),
    'medium slate blue':    np.array([0.482352941176471,    0.407843137254902,  0.933333333333333   ]),
    'medium purple':        np.array([0.576470588235294,    0.43921568627451,   0.858823529411765   ]),
    'dark magenta':         np.array([0.545098039215686,    0,                  0.545098039215686   ]),
    'dark violet':          np.array([0.580392156862745,    0,                  0.827450980392157   ]),
    'dark orchid':          np.array([0.6,                  0.196078431372549,  0.8                 ]),
    'medium orchid':        np.array([0.729411764705882,    0.333333333333333,  0.827450980392157   ]),
    'purple':               np.array([0.501960784313725,    0,                  0.501960784313725   ]),
    'thistle':              np.array([0.847058823529412,    0.749019607843137,  0.847058823529412   ]),
    'plum':                 np.array([0.866666666666667,    0.627450980392157,  0.866666666666667   ]),
    'violet':               np.array([0.933333333333333,    0.509803921568627,  0.933333333333333   ]),
    'magenta':              np.array([1,                    0,                  1                   ]),
    'orchid':               np.array([0.854901960784314,    0.43921568627451,   0.83921568627451    ]),
    'medium violet red':    np.array([0.780392156862745,    0.0823529411764706, 0.52156862745098    ]),
    'pale violet red':      np.array([0.858823529411765,    0.43921568627451,   0.576470588235294   ]),
    'deep pink':            np.array([1,                    0.0784313725490196, 0.576470588235294   ]),
    'hot pink':             np.array([1,                    0.411764705882353,  0.705882352941177   ]),
    'light pink':           np.array([1,                    0.713725490196078,  0.756862745098039   ]),
    'pink':                 np.array([1,                    0.752941176470588,  0.796078431372549   ]),
    'antique white':        np.array([0.980392156862745,    0.92156862745098,   0.843137254901961   ]),
    'beige':                np.array([0.96078431372549,     0.96078431372549,   0.862745098039216   ]),
    'bisque':               np.array([1,                    0.894117647058824,  0.768627450980392   ]),
    'blanched almond':      np.array([1,                    0.92156862745098,   0.803921568627451   ]),
    'wheat':                np.array([0.96078431372549,     0.870588235294118,  0.701960784313725   ]),
    'corn silk':            np.array([1,                    0.972549019607843,  0.862745098039216   ]),
    'lemon chiffon':        np.array([1,                    0.980392156862745,  0.803921568627451   ]),
    'light golden yellow':  np.array([0.980392156862745,    0.980392156862745,  0.823529411764706   ]),
    'light yellow':         np.array([1,                    1,                  0.87843137254902    ]),
    'saddle brown':         np.array([0.545098039215686,    0.270588235294118,  0.0745098039215686  ]),
    'sienna':               np.array([0.627450980392157,    0.32156862745098,   0.176470588235294   ]),
    'chocolate':            np.array([0.823529411764706,    0.411764705882353,  0.117647058823529   ]),
    'peru':                 np.array([0.803921568627451,    0.52156862745098,   0.247058823529412   ]),
    'sandy brown':          np.array([0.956862745098039,    0.643137254901961,  0.376470588235294   ]),
    'burly wood':           np.array([0.870588235294118,    0.72156862745098,   0.529411764705882   ]),
    'tan':                  np.array([0.823529411764706,    0.705882352941177,  0.549019607843137   ]),
    'rosy brown':           np.array([0.737254901960784,    0.56078431372549,   0.56078431372549    ]),
    'moccasin':             np.array([1,                    0.894117647058824,  0.709803921568627   ]),
    'navajo white':         np.array([1,                    0.870588235294118,  0.67843137254902    ]),
    'peach puff':           np.array([1,                    0.854901960784314,  0.725490196078431   ]),
    'misty rose':           np.array([1,                    0.894117647058824,  0.882352941176471   ]),
    'lavender blush':       np.array([1,                    0.941176470588235,  0.96078431372549    ]),
    'linen':                np.array([0.980392156862745,    0.941176470588235,  0.901960784313726   ]),
    'old lace':             np.array([0.992156862745098,    0.96078431372549,   0.901960784313726   ]),
    'papaya whip':          np.array([1,                    0.937254901960784,  0.835294117647059   ]),
    'sea shell':            np.array([1,                    0.96078431372549,   0.933333333333333   ]),
    'mint cream':           np.array([0.96078431372549,     1,                  0.980392156862745   ]),
    'slate gray':           np.array([0.43921568627451,     0.501960784313725,  0.564705882352941   ]),
    'light slate gray':     np.array([0.466666666666667,    0.533333333333333,  0.6                 ]),
    'light steel blue':     np.array([0.690196078431373,    0.768627450980392,  0.870588235294118   ]),
    'lavender':             np.array([0.901960784313726,    0.901960784313726,  0.980392156862745   ]),
    'floral white':         np.array([1,                    0.980392156862745,  0.941176470588235   ]),
    'alice blue':           np.array([0.941176470588235,    0.972549019607843,  1                   ]),
    'ghost white':          np.array([0.972549019607843,    0.972549019607843,  1                   ]),
    'honeydew':             np.array([0.941176470588235,    1,                  0.941176470588235   ]),
    'ivory':                np.array([1,                    1,                  0.941176470588235   ]),
    'azure':                np.array([0.941176470588235,    1,                  1                   ]),
    'snow':                 np.array([1,                    0.980392156862745,  0.980392156862745   ]),
    'black':                np.array([0,                    0,                  0                   ]),
    'dim gray':             np.array([0.411764705882353,    0.411764705882353,  0.411764705882353   ]),
    'gray':                 np.array([0.501960784313725,    0.501960784313725,  0.501960784313725   ]),
    'dark gray':            np.array([0.662745098039216,    0.662745098039216,  0.662745098039216   ]),
    'silver':               np.array([0.752941176470588,    0.752941176470588,  0.752941176470588   ]),
    'light gray':           np.array([0.827450980392157,    0.827450980392157,  0.827450980392157   ]),
    'gainsboro':            np.array([0.862745098039216,    0.862745098039216,  0.862745098039216   ]),
    'white smoke':          np.array([0.96078431372549,     0.96078431372549,   0.96078431372549    ]),
    'white':                np.array([1,                    1,                  1                   ])
}





# class Dot:

#     def __init__(self,
#         radius=1,
#         rgba=(1, 0, 0, 1),
#         location=(0, 0, 0),        
#     ):
#         self.radius = radius
#         self.rgba = rgba
#         self.location = location

def setSceneEnd(time):    
    bpy.context.scene.frame_end = int(time*FPS)


def setBackground(color):
    world = bpy.context.scene.world
    world.use_nodes = False
    world.color = color



def clearLights():
    # Select all light sources
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='LIGHT')

    # Delete the selected light sources
    bpy.ops.object.delete()


def clearMeshes():
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Delete all objects
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()


def clearCameras():
    # Select all cameras
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='CAMERA')

    # Delete the selected cameras
    bpy.ops.object.delete()



def createSun(
    location=(10, 10, 10),
    energy=5,
    angle=.7,
    color=(1, 1, 1) # white

):
    bpy.ops.object.light_add(type='SUN', location=location)

    sun_lamp = bpy.context.object
    sun_lamp.data.energy = energy
    sun_lamp.data.angle = angle  # Approximately 45 degrees
    sun_lamp.data.color = color 

    return sun_lamp


def createPointLight(
    location=(0, 0, 0),
    energy=100,
    color=(1, 1, 1) # white    
):
    bpy.ops.object.light_add(type='POINT', location=location)

    point_light = bpy.context.object
    point_light.data.energy = energy
    point_light.data.color =color

    return point_light



def createBall(
    rgba = (1, 0, 0, 1),
    location = (0, 0, 0),
    radius=1
):
    # Create a new mesh object
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=location)

    # Get a reference to the newly created object
    obj = bpy.context.active_object

    # Create a new material and assign it to the object
    mat = bpy.data.materials.new(name="Red Material")
    obj.data.materials.append(mat)

    # Set the material properties to make it red
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    principled_bsdf = nodes.get("Principled BSDF")
    if principled_bsdf is not None:
        principled_bsdf.inputs['Base Color'].default_value = rgba

    obj.scale = (radius, radius, radius)

    return obj


def createPoint(
    rgba = (1, 0, 0, 1),
    location = (0, 0, 0)        
):
    return createBall(rgba=rgba, location=location, radius=.001)


def createCylinder(
    rgba = (1, 0, 0, 1),
    radius=1,
    depth=1,
    location=(0, 0, 0)
):

    # Add a cylinder
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, enter_editmode=False, align='WORLD')

    # Get the newly created cylinder object
    cylinder = bpy.context.object

    # Create a material for the cylinder
    material = bpy.data.materials.new(name='CylinderMaterial')
    cylinder.data.materials.append(material)

    # Set the material properties (e.g., color)
    material.use_nodes = True
    material.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = rgba

    # Optionally, set the cylinder's position and rotation
    cylinder.location = location  # Set the cylinder's position
    cylinder.rotation_euler = (0, 0, 0)  # Set the cylinder's rotation    

    return cylinder



def createCylinderBetween(
    p1=(0, 0, 0), p2=(0, 0, 2), r=2,
    rgba=(1, 0, 0, 1) # red
):
    (x1, y1, z1), (x2, y2, z2) = p1, p2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1    
    dist = np.sqrt(dx**2 + dy**2 + dz**2)

    bpy.ops.mesh.primitive_cylinder_add(
        radius = r, 
        depth = dist,
        location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)   
    ) 

    phi = math.atan2(dy, dx) 
    theta = math.acos(dz/dist) 

    # Get the newly created cylinder object
    cylinder = bpy.context.object

    cylinder.rotation_euler[1] = theta 
    cylinder.rotation_euler[2] = phi 

    # Create a material for the cylinder
    material = bpy.data.materials.new(name='CylinderMaterial')
    cylinder.data.materials.append(material)

    # Set the material properties (e.g., color)
    material.use_nodes = True
    material.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = rgba

    return cylinder


def updateCylinderBetween(
    cylinder,
    p1=(0, 0, 0), p2=(0, 0, 2)
):
    (x1, y1, z1), (x2, y2, z2) = p1, p2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1    
    dist = np.sqrt(dx**2 + dy**2 + dz**2)

    phi = math.atan2(dy, dx) 
    theta = math.acos(dz/dist) 

    # Get the newly created cylinder object
    cylinder.location = (dx/2 + x1, dy/2 + y1, dz/2 + z1)  
    cylinder.dimensions[2] = dist

    cylinder.rotation_euler[1] = theta 
    cylinder.rotation_euler[2] = phi 




# each 'changePeriod' is [p1, p2, time]
def changingCylinder(
    startTime=1,
    p1=(0, 0, 0), p2=(1, 1, 1),    
    radius=1,
    rgba=(1, 0, 0, 1),
    changePeriods=[]
):
    cylinder = createCylinderBetween(p1=p1, p2=p2, r=radius, rgba=rgba)

    startFrame = int(startTime*FPS)
    cylinder.keyframe_insert(data_path='location', frame=startFrame)
    cylinder.keyframe_insert(data_path='scale', frame=startFrame)

    for changePeriod in changePeriods:
        [p1, p2, time] = changePeriod

        nextFrame = int(time*FPS)

        updateCylinderBetween(cylinder, p1=p1, p2=p2)

        cylinder.keyframe_insert(data_path='location', frame=nextFrame)
        cylinder.keyframe_insert(data_path='scale', frame=nextFrame)

    return cylinder






class patternGroup:

    validMethods = [
        'stepConstant_scaleConstant',
        'stepLinear_scaleConstant'
    ]

    def __init__(self,
        method='stepConstant_scaleConstant',
        **kwargs
    ):
        self.kwargs = kwargs
        self.method = method

    def apply(self, start, end, *objs):
        if self.method == 'stepConstant_scaleConstant':
            scale = self.kwargs['scale'] # should just be one value in this case

            LEN = len(objs)

            totalDuration = end - start
            scaledDuration = totalDuration*scale
            step = (totalDuration - scaledDuration)/(LEN - 1)

            c = 0 # counter
            iStart, iEnd = start, start + scaledDuration
            while c < LEN:
                yield [iStart, iEnd]
                iStart += step
                iEnd += step
                c += 1



class Sweep: 

    def __init__(self,                 
        parameter,
        endValue,
        startValue=None,
        startTime = 1,
        endTime = 3,
        interpolation = 'SMOOTH'
    ):
        self.startTime = startTime
        self.endTime = endTime    
        self.interpolation = interpolation        
        self.parameter = parameter
        self.startValue = startValue
        self.endValue = endValue


    def apply(self, *objs):
        for obj in objs:
            startFrame = int(self.startTime*FPS)
            endFrame = int(self.endTime*FPS)

            if self.startValue != None: 
                setattr(obj, self.parameter, self.startValue)
            
            obj.keyframe_insert(data_path=self.parameter, frame=startFrame)
            setattr(obj, self.parameter, self.endValue)
            obj.keyframe_insert(data_path=self.parameter, frame=endFrame)
                        

    def applyPattern(self, pattern, *objs):
        assert isinstance(pattern, patternGroup)

        for obj, [iStart, iEnd] in zip(objs, pattern.apply(self.startTime, self.endTime, *objs)):
            startFrame = int(iStart*FPS)
            endFrame = int(iEnd*FPS)

            if self.startValue != None: 
                setattr(obj, self.parameter, self.startValue)
            
            obj.keyframe_insert(data_path=self.parameter, frame=startFrame)
            setattr(obj, self.parameter, self.endValue)
            obj.keyframe_insert(data_path=self.parameter, frame=endFrame)            




class Move(Sweep):

    def __init__(self,
        startTime = 1,
        endTime = 3,
        startLocation = None,
        endLocation = (1, 1, 1),
        interpolation = 'SMOOTH'
    ):
        self.startTime = startTime
        self.endTime = endTime    
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.interpolation = interpolation

    def apply(self, *objs):
        for obj in objs:
            startFrame = int(self.startTime*FPS)
            endFrame = int(self.endTime*FPS)

            if self.startLocation == None: obj.location = obj.location
            else: obj.location = self.startLocation
            obj.keyframe_insert(data_path='location', frame=startFrame)
            obj.location = self.endLocation
            obj.keyframe_insert(data_path='location', frame=endFrame)
                



    def applyPattern(self, pattern, *objs):
        assert isinstance(pattern, patternGroup)

        for obj, [iStart, iEnd] in zip(objs, pattern.apply(self.startTime, self.endTime, *objs)):
            startFrame = int(iStart*FPS)
            endFrame = int(iEnd*FPS)

            if self.startLocation == None: obj.location = obj.location
            else: obj.location = self.startLocation
            obj.keyframe_insert(data_path='location', frame=startFrame)
            obj.location = self.endLocation
            obj.keyframe_insert(data_path='location', frame=endFrame)
                






class Scale(Sweep):

    def __init__(self,
        startTime = 1,
        endTime = 3,
        startScale = None,
        endScale = (1, 1, 1),
        interpolation = 'SMOOTH'
    ):
        self.startTime = startTime
        self.endTime = endTime    
        self.startScale = startScale
        self.endScale = endScale
        self.interpolation = interpolation


    def apply(self, *objs):
        for obj in objs:
            startFrame = int(self.startTime*FPS)
            endFrame = int(self.endTime*FPS)

            if self.startScale == None: obj.scale = obj.scale
            else: obj.scale = self.startScale
            obj.keyframe_insert(data_path='scale', frame=startFrame)
            obj.scale = self.endScale
            obj.keyframe_insert(data_path='scale', frame=endFrame)
                

    def applyPattern(self, pattern, *objs):
        assert isinstance(pattern, patternGroup)

        for obj, [iStart, iEnd] in zip(objs, pattern.apply(self.startTime, self.endTime, *objs)):
            startFrame = int(iStart*FPS)
            endFrame = int(iEnd*FPS)

            if self.startScale == None: obj.scale = obj.scale
            else: obj.scale = self.startScale
            obj.keyframe_insert(data_path='scale', frame=startFrame)
            obj.scale = self.endScale
            obj.keyframe_insert(data_path='scale', frame=endFrame)
                





class Pop(Sweep):

    def __init__(self,
        scale,
        startTime = 1,
        endTime = 3,
        overshoot = .2, # overshoot scale 20 % of end scale
        shrink = .2, # spend 20% of duration shrinking back down after overshoot    
    ):
        self.scale = scale
        self.startTime = startTime
        self.endTime = endTime
        self.overshoot = overshoot
        self.shrink = shrink

    def apply(self, *objs):
        for obj in objs:
            startFrame = int(self.startTime*FPS)
            endFrame = int(self.endTime*FPS)        
            overshootFrame = int(startFrame + (endFrame - startFrame)*(1 - self.shrink))

            overShootFactor = 1 + self.overshoot

            obj.keyframe_insert(data_path='scale', frame=startFrame)
            obj.scale = tuple(overShootFactor*comp for comp in self.scale) # overshoot scale
            obj.keyframe_insert(data_path='scale', frame=overshootFrame)
            obj.scale = self.scale
            obj.keyframe_insert(data_path='scale', frame=endFrame)


    def applyPattern(self, pattern, *objs):
        assert isinstance(pattern, patternGroup)

        for obj, [iStart, iEnd] in zip(objs, pattern.apply(self.startTime, self.endTime, *objs)):
            startFrame = int(iStart*FPS)
            endFrame = int(iEnd*FPS)
            overshootFrame = int(startFrame + (endFrame - startFrame)*(1 - self.shrink))

            overShootFactor = 1 + self.overshoot

            obj.keyframe_insert(data_path='scale', frame=startFrame)
            obj.scale = tuple(overShootFactor*comp for comp in self.scale) # overshoot scale
            obj.keyframe_insert(data_path='scale', frame=overshootFrame)
            obj.scale = self.scale
            obj.keyframe_insert(data_path='scale', frame=endFrame)


def pointInterpolate(p1, p2, t):
    return (p1[0] + t*(p2[0]-p1[0]), p1[1] + t*(p2[1]-p1[1]), p1[2] + t*(p2[2]-p1[2]))

def wireFrameCubeEnterExit(
    sideLength=10,
    center=(0, 0, 0),
    vertices_rgba=(0, 0, 1, 1),
    edges_rgba=(1, 0, 0, 1),
    edges_radius=.1,
    vertices_radius=.5,
    enterStartTime=1,
    enterEndTime=2,
    exitStartTime=5,
    exitEndTime=6,
    goneRatio=.999
):
    # getting all eight coordinates of cube
    (cx, cy, cz) = center

    sideLength /= 2

    # bottom face
    p1 = (cx - sideLength, cy + sideLength, cz - sideLength)
    p2 = (cx + sideLength, cy + sideLength, cz - sideLength)
    p3 = (cx - sideLength, cy - sideLength, cz - sideLength)
    p4 = (cx + sideLength, cy - sideLength, cz - sideLength)

    # top face
    p5 = (cx - sideLength, cy + sideLength, cz + sideLength)
    p6 = (cx + sideLength, cy + sideLength, cz + sideLength)
    p7 = (cx - sideLength, cy - sideLength, cz + sideLength)
    p8 = (cx + sideLength, cy - sideLength, cz + sideLength)



    combos = [
        # bottom face
        (p1, p2), (p2, p4), (p4, p3), (p3, p1),
        # top face
        (p5, p6), (p6, p8), (p8, p7), (p7, p5),
        # side edges
        (p1, p5), (p6, p2), (p3, p7), (p8, p4)
    ]

    cyls = []
    for (pi, po) in combos:
        cyls.append(
            changingCylinder(
                startTime=enterStartTime, p1=pi, p2=pointInterpolate(pi, po, 1-goneRatio), radius=edges_radius, rgba=edges_rgba,
                changePeriods=[
                    [pi, po, enterEndTime],
                    [pi, po, exitStartTime],
                    [pointInterpolate(pi, po, goneRatio), po, exitEndTime],
                ]
            )
        )

    si = vertices_radius
    popIn = Pop(scale=(si, si, si), startTime=enterStartTime, endTime=enterEndTime)
    so = vertices_radius*(1-goneRatio)
    popOut = Pop(scale=(so, so, so), startTime=exitStartTime, endTime=exitEndTime, shrink=.8)

    dot1 = createBall(rgba=vertices_rgba, location=p1, radius=edges_radius*(1-goneRatio))
    dot2 = createBall(rgba=vertices_rgba, location=p2, radius=edges_radius*(1-goneRatio))
    dot3 = createBall(rgba=vertices_rgba, location=p3, radius=edges_radius*(1-goneRatio))
    dot4 = createBall(rgba=vertices_rgba, location=p4, radius=edges_radius*(1-goneRatio))
    dot5 = createBall(rgba=vertices_rgba, location=p5, radius=edges_radius*(1-goneRatio))
    dot6 = createBall(rgba=vertices_rgba, location=p6, radius=edges_radius*(1-goneRatio))
    dot7 = createBall(rgba=vertices_rgba, location=p7, radius=edges_radius*(1-goneRatio))
    dot8 = createBall(rgba=vertices_rgba, location=p8, radius=edges_radius*(1-goneRatio))

    popIn.apply(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)
    popOut.apply(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)








if __name__ == "__main__":
    setSceneEnd(10)

    clearMeshes()
    clearLights()
    clearCameras()
    
    setBackground((0, 0, 0))
    createPointLight(energy=1000000, location=(100, 100, 100))
    createPointLight(energy=1000000, location=(-100, -100, -100))

    popIn = Pop((.25, .25, .25), startTime=1, endTime=2)
    popOut = Pop((.001, .001, .001), startTime=9, endTime=10, shrink=.8)

    dots = []
    for i in range(-5, 6, 2):
        for j in range(-5, 6, 2):
            for k in range(-5, 6, 2):
                dots.append(createPoint(location=(i, j, k), rgba=(*colors['red'], 1)))

    popIn.applyPattern(patternGroup(scale=.7), *dots)
    popOut.applyPattern(patternGroup(scale=.7), *dots)

    wireFrameCubeEnterExit(
        edges_rgba=(*colors['teal'], 1),
        vertices_rgba=(*colors['dark sea green'], 1),
        enterStartTime=1,
        enterEndTime=1.5,
        exitStartTime=9.5,
        exitEndTime=10
    )


    
                