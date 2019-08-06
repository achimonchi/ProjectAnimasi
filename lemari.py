import bpy, os

def run() :
    path = os.path.expanduser('E:\Project\Animasi\Texture\wood.jpg')

    try :
        imgPath = bpy.data.images.load(path)
    except :
        raise NameError("Cannot load image %s" % path)
    
    texture = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture.image = imgPath

    # create materials
    mat = bpy.data.materials.new('texture')
    mText = mat.texture_slots.add()
    mText.texture_coords = 'GLOBAL'
    mText.texture = texture

    # tubuh utama
    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.6,3,1.5)
    )
    ob = bpy.context.object
    ob.name = "TubuhLemari"
    ob.scale = (1,1,1.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    # pintu
    color = bpy.data.materials.new('color')
    color.diffuse_color=(1,1,1)
    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(2.6,3.5,1.4)
    )
    ob = bpy.context.object
    ob.name = "PintuKiri"
    ob.scale = (.01,.45,1.4)
    mymesh = ob.data
    mymesh.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(2.6,2.5,1.4)
    )
    ob = bpy.context.object
    ob.name = "PintuKiri"
    ob.scale = (.01,.45,1.4)
    mymesh = ob.data
    mymesh.materials.append(color)



    # Pinggiran

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        location=(2.6,4,1.5)
    )

    bpy.ops.object.shade_smooth()

    ob = bpy.context.object
    ob.name = "PinggiranLemari1"
    ob.scale = (.1,.1,1.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        location=(2.6,2,1.5)
    )

    bpy.ops.object.shade_smooth()

    ob = bpy.context.object
    ob.name = "PinggiranLemari2"
    ob.scale = (.1,.1,1.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32,
        ring_count=24,
        size=.1,
        location=(2.6,4,3)
    )
    

    bpy.ops.object.shade_smooth()
    ob = bpy.context.object
    ob.name = "BolaLemari1"
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32,
        ring_count=24,
        size=.1,
        location=(2.6,2,3)
    )

    bpy.ops.object.shade_smooth()
    ob = bpy.context.object
    ob.name = "BolaLemari2"
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=1,
        location=(2.75,3,2.7),
        rotation=(0,10.99,0)
    )
    # bpy.ops.object.shade_smooth()
    ob = bpy.context.object
    ob.name = "AtasLemari"
    ob.scale=(.7,.7,.3)
    mymesh = ob.data
    mymesh.materials.append(mat)


if __name__ == "__main__" :
    run()