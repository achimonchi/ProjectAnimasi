import bpy,os

def run() :
    # ==========================================
    #  create texture

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
    mText.mapping = "CUBE"
    mText.texture = texture


    # ===========================================
    # meja
    color = bpy.data.materials.new('color')
    color.diffuse_color=(1,1,1)

    black = bpy.data.materials.new('black')
    black.diffuse_color=(.1,.1,.1)

    black2 = bpy.data.materials.new('black2')
    black2.diffuse_color=(0,0,0)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-2,.9)
    )

    ob = bpy.context.object
    ob.name = "MejaKiri"
    ob.scale = (.5,.5,.7)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.5,-2,1)
    )

    ob = bpy.context.object
    ob.name = "PintuMejaKiriAtas"
    ob.scale = (.01,.4,.3)
    mymesh = ob.data
    mymesh.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.5,-2,.45)
    )

    ob = bpy.context.object
    ob.name = "PintuMejaKiriBawah"
    ob.scale = (.01,.4,.15)
    mymesh = ob.data
    mymesh.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-5.5,.9)
    )
    ob = bpy.context.object
    ob.name = "MejaKanan"
    ob.scale = (.5,.5,.7)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.5,-5.5,1)
    )

    ob = bpy.context.object
    ob.name = "PintuMejaKananAtas"
    ob.scale = (.01,.4,.3)
    mymesh = ob.data
    mymesh.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.5,-5.5,.45)
    )

    ob = bpy.context.object
    ob.name = "PintuMejaKananBawah"
    ob.scale = (.01,.4,.15)
    mymesh = ob.data
    mymesh.materials.append(color)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-3.8,.7)
    )

    ob = bpy.context.object
    ob.name = "MejaTengah"
    ob.scale = (.5,1.5,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    # ===========================================
    # dudukan tv
    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-3.8,1.25)
    )

    ob = bpy.context.object
    ob.name = "Dudukan1"
    ob.scale = (.3,.5,.05)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-3.8,1.3)
    )

    ob = bpy.context.object
    ob.name = "Dudukan2"
    ob.scale = (.1,.2,.05)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(4,-3.8,1.85)
    )

    ob = bpy.context.object
    ob.name = "TV"
    ob.scale = (.05,.8,.5)
    mymesh = ob.data
    mymesh.materials.append(black)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(3.95,-3.8,1.85)
    )

    ob = bpy.context.object
    ob.name = "LayarTV"
    ob.scale = (.01,.7,.45)
    mymesh = ob.data
    mymesh.materials.append(black2)

    # ===========================================
    

if __name__ == "__main__" :
    run()