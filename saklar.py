import bpy

color = bpy.data.materials.new('color')
color.diffuse_color = (1,1,1)

bpy.ops.mesh.primitive_cube_add(
    location=(4.8,-1.3,2),
    rotation=(0,-.3,0)
)

ob = bpy.context.object
ob.scale=(.03,.03,.1)
ob.name = 'saklar'

mesh = ob.data
mesh.materials.append(color)