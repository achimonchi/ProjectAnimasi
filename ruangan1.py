import bpy

def cubeWithColor(colorType, name, locate, size) :
    bpy.ops.mesh.primitive_cube_add(location=locate)
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (1, 0, 0) #change color
    

def run() :
    cubeWithColor((.1,.1,.1),'Cube1',(0,0,0),(0,0,0))

if __name__ == "__main__" :
    run()