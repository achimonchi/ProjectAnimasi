import bpy, os

def run():
    color = bpy.data.materials.new('color')
    color.diffuse_color = (.5,1,.5)


    # ==========================================
    #  create texture

    path = os.path.expanduser('E:/Project/Animasi/Texture/plastic2.jpg')

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


    # =====================
    # alas kursi
    bpy.ops.mesh.primitive_cube_add(
        location=(-2.5,-5.5,1.2)
    )

    ob = bpy.context.object
    ob.name = 'bawahKursiKomputer'
    ob.scale=(.5,.5,.05)
    mymesh = ob.data
    mymesh.materials.append(mat)

    # bantalan
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        location=(-2.5,-5.5,1.25),
        rotation=(10.9955,0,0)
    )
    ob = bpy.context.object
    ob.name="bantalanKursiKomputer"
    ob.scale = (.45,.05,.45)
    mymesh = ob.data
    mymesh.materials.append(mat2)


    # =====================
    # punggung kursi
    bpy.ops.mesh.primitive_cube_add(
        location=(-1.95,-5.5,1.65),
        rotation=(0,-6.1,0)
    )

    ob = bpy.context.object
    ob.name = 'punggungKursiKomputer'
    ob.scale=(.05,.5,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    # bantalan 

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        location=(-2,-5.5,1.6),
        rotation=(10.9955,-10.80,0)
    )
    ob = bpy.context.object
    ob.name="bantalanPunggungKursiKomputer"
    ob.scale = (.45,.05,.45)
    mymesh = ob.data
    mymesh.materials.append(mat2)

    # =====================
    # kursi
    bpy.ops.mesh.primitive_cube_add(
        location=(-2.1,-5.15,.7)
    )
    ob = bpy.context.object
    ob.name="kakiKursiKomputer1"
    ob.scale = (.05,.05,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.1,-5.9,.7)
    )
    ob = bpy.context.object
    ob.name="kakiKursiKomputer2"
    ob.scale = (.05,.05,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.83,-5.9,.7)
    )
    ob = bpy.context.object
    ob.name="kakiKursiKomputer3"
    ob.scale = (.05,.05,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.83,-5.15,.7)
    )
    ob = bpy.context.object
    ob.name="kakiKursiKomputer4"
    ob.scale = (.05,.05,.5)
    mymesh = ob.data
    mymesh.materials.append(mat)

    # parenting object
    bawahKursiKomputer = bpy.data.objects['bawahKursiKomputer']
    bantalanKursiKomputer = bpy.data.objects['bantalanKursiKomputer']
    punggungKursiKomputer = bpy.data.objects['punggungKursiKomputer']
    bantalanPunggungKursiKomputer = bpy.data.objects['bantalanPunggungKursiKomputer']
    kakiKursiKomputer1 = bpy.data.objects['kakiKursiKomputer1']
    kakiKursiKomputer2 = bpy.data.objects['kakiKursiKomputer2']
    kakiKursiKomputer3 = bpy.data.objects['kakiKursiKomputer3']
    kakiKursiKomputer4 = bpy.data.objects['kakiKursiKomputer4']

    bpy.ops.object.select_all(action="DESELECT")
    bawahKursiKomputer.select = True
    bantalanKursiKomputer.select = True
    bantalanPunggungKursiKomputer.select = True
    punggungKursiKomputer.select = True
    kakiKursiKomputer1.select = True
    kakiKursiKomputer2.select = True
    kakiKursiKomputer3.select = True
    kakiKursiKomputer4.select = True

    bpy.context.scene.objects.active = punggungKursiKomputer
    bpy.ops.object.parent_set()

    punggungKursiKomputer.location=(-2.5,-5.65,1.65)



if __name__ == "__main__" :
    run()