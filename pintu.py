import bpy, os

def run():
    color = bpy.data.materials.new('color')
    color.diffuse_color = (1,1,1)

    color2 = bpy.data.materials.new('color2')
    color2.diffuse_color = (.1,.1,.1)


    #  ==========================================
    #  create texture

    path = os.path.expanduser('E:/Project/Animasi/Texture/metal1.jpg')

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
    mText.mapping = "CUBE"
    mText.texture = texture


    # ==========================================
    #  create texture 2

    path2 = os.path.expanduser('E:/Project/Animasi/Texture/fabric2.jpg')

    try :
        imgPath2 = bpy.data.images.load(path2)
    except :
        raise NameError("Cannot load image %s" % path2)
    
    texture2 = bpy.data.textures.new('ColorTex2', type="IMAGE")
    texture2.image = imgPath2

    # create materials
    mat2 = bpy.data.materials.new('texture2')
    mText2 = mat2.texture_slots.add()
    mText2.texture_coords = 'GLOBAL'
    mText2.mapping = "CUBE"
    mText2.texture = texture2
    

    # tubuh pintu
    bpy.ops.mesh.primitive_cube_add(
        location=(-3.25,7.95,1.8)
    )

    ob = bpy.context.object
    ob.scale=(.08,.05,1.2)
    ob.name= "tubuhPintuKiri"
    ob.data.materials.append(color)

    # tubuh pintu
    bpy.ops.mesh.primitive_cube_add(
        location=(-4.75,7.95,1.8)
    )

    ob = bpy.context.object
    ob.scale=(.08,.05,1.2)
    ob.name= "tubuhPintuKanan"
    ob.data.materials.append(color)

    # tubuh pintu
    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.95,2.75)
    )

    ob = bpy.context.object
    ob.scale=(.67,.05,.25)
    ob.name= "tubuhPintuAtas"
    ob.data.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.95,1.5)
    )

    ob = bpy.context.object
    ob.scale=(.5,.08,.95)
    ob.name= "tubuhPintuUtama"
    ob.data.materials.append(color2)

    bpy.ops.mesh.primitive_cube_add(
        location=(-3.4,7.95,1.5)
    )

    ob = bpy.context.object
    ob.scale=(.1,.1,1)
    ob.name= "manik1"
    ob.data.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-4.6,7.95,1.5)
    )

    ob = bpy.context.object
    ob.scale=(.1,.1,1)
    ob.name= "manik2"
    ob.data.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.949,2.4)
    )

    ob = bpy.context.object
    ob.scale=(.5,.1,.1)
    ob.name= "manik3"
    ob.data.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.949,2)
    )

    ob = bpy.context.object
    ob.scale=(.3,.1,.1)
    ob.name= "manik4"
    ob.data.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.949,1.6)
    )

    ob = bpy.context.object
    ob.scale=(.3,.1,.1)
    ob.name= "manik5"
    ob.data.materials.append(mat)
    
    bpy.ops.mesh.primitive_cube_add(
        location=(-4,7.949,1.2)
    )

    ob = bpy.context.object
    ob.scale=(.3,.1,.1)
    ob.name= "manik6"
    ob.data.materials.append(mat)

    # Parenting
    manik1 = bpy.data.objects['manik1']
    manik2 = bpy.data.objects['manik2']
    manik3 = bpy.data.objects['manik3']
    manik4 = bpy.data.objects['manik4']
    manik5 = bpy.data.objects['manik5']
    manik6 = bpy.data.objects['manik6']
    tubuhPintuUtama = bpy.data.objects['tubuhPintuUtama']

    bpy.ops.object.select_all(action="DESELECT")
    manik1.select = True
    manik2.select = True
    manik3.select = True
    manik4.select = True
    manik5.select = True
    manik6.select = True
    tubuhPintuUtama.select = True

    bpy.context.scene.objects.active = manik2
    bpy.ops.object.parent_set()

if __name__ == "__main__" :
    run()