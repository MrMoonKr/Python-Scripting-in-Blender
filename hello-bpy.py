import bpy

from bpy import data as D
from bpy import context as C

# Convenience Imports
from mathutils import *
from math import *

# Convenience Variables
C = bpy.context
D = bpy.data

# Print all objects names in the scene
for obj in C.scene.objects:
    print(obj.name)

