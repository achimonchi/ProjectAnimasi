import bpy, os

def run() :
    # ==========================================
    #  create texture

    path = os.path.expanduser('E:/Project/Animasi/Texture/wood.jpg')

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

    


    #alas meja
    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(-3,-5,1.55)
    )

    ob = bpy.context.object
    ob.scale=(.8,1.5,.1)
    ob.name = "alasMeja"
    mymesh = ob.data
    mymesh.materials.append(mat)
    # =============================
    # kaca meja
    color = bpy.data.materials.new('color')
    color.diffuse_color = (1,1,1)

    color2 = bpy.data.materials.new('color')
    color2.diffuse_color = (0,0,0)

    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(-3,-5,1.62)
    )

    ob = bpy.context.object
    ob.scale=(.75,1.45,.05)
    ob.name = "kacaMeja"
    mymesh = ob.data
    mymesh.materials.append(color)
    
    # ==========================================
    #  create texture2

    path2 = os.path.expanduser('E:/Project/Animasi/Texture/box.jpg')

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

    # ==========================================
    #  create texture3

    path3 = os.path.expanduser('E:/Project/Animasi/Texture/metal1.jpg')

    try :
        imgPath3 = bpy.data.images.load(path3)
    except :
        raise NameError("Cannot load image %s" % path3)
    
    texture3 = bpy.data.textures.new('ColorTex3', type="IMAGE")
    texture3.image = imgPath3

    # create materials
    mat3 = bpy.data.materials.new('texture3')
    mText3 = mat3.texture_slots.add()
    mText3.texture_coords = 'GLOBAL'
    mText3.mapping = "CUBE"
    mText3.texture = texture3
    
    # =============================
    # dudukan komputer
    bpy.ops.mesh.primitive_cube_add(
        view_align=False,
        enter_editmode=False,
        location=(-3.2,-5.7,1.65)
    )

    ob = bpy.context.object
    ob.scale=(.3,.4,.1)
    ob.name = "dudukanKomputer1"
    mymesh = ob.data
    mymesh.materials.append(mat2)

    # =============================
    # kaki komputer
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        location=(-3.3,-5.7,1.75)
    )
    bpy.ops.object.shade_smooth()
    ob = bpy.context.object
    ob.scale=(.03,.03,.5)
    ob.name = "kakiKomputer1"
    mymesh = ob.data
    mymesh.materials.append(mat3)
    
    # =============================
    # kaki komputer 2
    bpy.ops.mesh.primitive_torus_add(
        major_radius=1,
        minor_radius=.8,
        location=(-3.2,-5.7,1.53),
        rotation=(0,.2,0)
    )
    bpy.ops.object.shade_smooth()
    ob = bpy.context.object
    ob.scale=(.15,.2,.3)
    ob.name = "kakiKomputer2"
    mymesh = ob.data
    mymesh.materials.append(mat3)
    
    # =============================
    # punggungKomputer

    bpy.ops.mesh.primitive_cube_add(
        location=(-3.25,-5.7,2.15)
    )
    ob = bpy.context.object
    ob.scale=(.05,.02,.02)
    ob.name = "monitor"
    
    # =============================
    # monitor komputer
    bpy.ops.mesh.primitive_cube_add(
        location=(-3.2,-5.7,2.15)
    )
    ob = bpy.context.object
    ob.scale=(.02,.5,.3)
    ob.name = "monitor"
    mymesh = ob.data
    mymesh.materials.append(mat3)
    
    # =============================
    # layar monitor komputer
    bpy.ops.mesh.primitive_cube_add(
        location=(-3.19,-5.7,2.15)
    )
    ob = bpy.context.object
    ob.scale=(.018,.48,.28)
    ob.name = "layarMonitor"
    mymesh = ob.data
    mymesh.materials.append(color2)

    # =============================
    # kaki meja komputer
    bpy.ops.mesh.primitive_cube_add(
        location=(-2.3,-6.3,.8)
    )
    ob = bpy.context.object
    ob.scale=(.05,.05,.7)
    ob.name = "kakiMejaMonitor1"
    mymesh = ob.data
    mymesh.materials.append(mat3)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.3,-3.7,.8)
    )
    ob = bpy.context.object
    ob.scale=(.05,.05,.7)
    ob.name = "kakiMejaMonitor2"
    mymesh = ob.data
    mymesh.materials.append(mat3)

    bpy.ops.mesh.primitive_cube_add(
        location=(-3.6,-6.3,.8)
    )
    ob = bpy.context.object
    ob.scale=(.05,.05,.7)
    ob.name = "kakiMejaMonitor3"
    mymesh = ob.data
    mymesh.materials.append(mat3)

    bpy.ops.mesh.primitive_cube_add(
        location=(-3.6,-3.7,.8)
    )
    ob = bpy.context.object
    ob.scale=(.05,.05,.7)
    ob.name = "kakiMejaMonitor4"
    mymesh = ob.data
    mymesh.materials.append(mat3)

    # =============================
    # lapisan meja komputer
    bpy.ops.mesh.primitive_cube_add(
        location=(-3.6,-5,1.1)
    )
    ob = bpy.context.object
    ob.scale=(.01,1.3,.4)
    ob.name = "lapisanKakiMejaKomputer1"
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.9,-6.3,1.1)
    )
    ob = bpy.context.object
    ob.scale=(.6,0.01,.4)
    ob.name = "lapisanKakiMejaKomputer2"
    mymesh = ob.data
    mymesh.materials.append(mat)

    # =============================
    # laci meja komputer

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.9,-4.32,1.1)
    )
    ob = bpy.context.object
    ob.scale=(.6,.65,.4)
    ob.name = "laciMejaKomputer"
    mymesh = ob.data
    mymesh.materials.append(mat)

    bpy.ops.mesh.primitive_cube_add(
        location=(-2.36,-4.32,1.1)
    )
    ob = bpy.context.object
    ob.scale=(.1,.55,.3)
    ob.name = "laciMejaKomputer2"
    mymesh = ob.data
    mymesh.materials.append(color)


    # parenting
    alasMeja = bpy.data.objects['alasMeja']
    kacaMeja = bpy.data.objects['kacaMeja']
    dudukanKomputer1 = bpy.data.objects['dudukanKomputer1']
    kakiKomputer1 = bpy.data.objects['kakiKomputer1']
    kakiKomputer2 = bpy.data.objects['kakiKomputer2']
    monitor = bpy.data.objects['monitor']
    monitor2 = bpy.data.objects['monitor.001']
    layarMonitor = bpy.data.objects['layarMonitor']
    kakiMejaMonitor1 = bpy.data.objects['kakiMejaMonitor1']
    kakiMejaMonitor2 = bpy.data.objects['kakiMejaMonitor2']
    kakiMejaMonitor3 = bpy.data.objects['kakiMejaMonitor3']
    kakiMejaMonitor4 = bpy.data.objects['kakiMejaMonitor4']
    lapisanKakiMejaKomputer1 = bpy.data.objects['lapisanKakiMejaKomputer1']
    lapisanKakiMejaKomputer2 = bpy.data.objects['lapisanKakiMejaKomputer2']
    laciMejaKomputer = bpy.data.objects['laciMejaKomputer']
    laciMejaKomputer2 = bpy.data.objects['laciMejaKomputer2']

    bpy.ops.object.select_all(action="DESELECT")
    alasMeja.select = True
    kacaMeja.select = True
    dudukanKomputer1.select = True
    kakiKomputer1.select = True
    kakiKomputer2.select = True
    monitor.select = True
    layarMonitor.select = True
    kakiMejaMonitor1.select = True
    kakiMejaMonitor2.select = True
    kakiMejaMonitor3.select = True
    kakiMejaMonitor4.select = True
    lapisanKakiMejaKomputer1.select = True
    lapisanKakiMejaKomputer2.select = True
    laciMejaKomputer.select = True
    laciMejaKomputer2.select = True
    monitor2.select = True

    bpy.context.scene.objects.active = alasMeja
    bpy.ops.object.parent_set()

    alasMeja.location=(-3.7,-5,1.55)


if __name__ == "__main__" :
    run()