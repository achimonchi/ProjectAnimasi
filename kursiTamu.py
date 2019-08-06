import bpy,os

def kursi(name, colorType, colorName, locate, size, feets, back, fix, roFix) :
    # create color
    color = bpy.data.materials.new(colorName)
    color.diffuse_color = colorType

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

    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=locate)

    ob = bpy.context.object
    ob.name = name
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=size

    path1 = os.path.expanduser('E:/Project/Animasi/Texture/benang.jpg')
    
    try :
        imgPath1 = bpy.data.images.load(path1)
    except :
        raise NameError("Cannot load images %s " % path1)
    
    texture1 = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture1.image = imgPath1

    # create materials
    mat1 = bpy.data.materials.new('texture')
    mText1 = mat1.texture_slots.add()
    mText1.texture_coords = 'GLOBAL'
    mText1.texture = texture1

    # bantalan kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(0,0,1.2),
    rotation=(10.9955,0,0))

    ob = bpy.context.object
    ob.scale = (.5,.05,1.3)
    ob.name="BantalanKursi"
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # punggung kursi
    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=(-.5,0,1.5),
    rotation=(0,6.1,0))

    ob = bpy.context.object
    ob.name = "PunggungKursi"
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=(.055,1.4,.5)

    # bantalan punggung kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(-0.45,0,1.45),
    rotation=(10.9955,10.87,0))

    ob = bpy.context.object
    ob.name="BantalanPunggungKursi"
    ob.scale = (.4,.05,1.3)
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # kepala kursi
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        rotation=(0,7.67,0),
        location=(-0.53,0,1.7)
    )

    ob = bpy.context.object
    ob.scale = (.5,.6,.045)
    ob.name="KepalaKursi"
    mymesh = ob.data
    mymesh.materials.append(mat)

    # pegangan kursi
    for i in range(4) :
        locate2=(0,0,0)
        locate3=(0,0,0)
        
        if(i%2==0) :
            locate2=(.45,(i-1)*1.35,1.3)
            locate3=(.45,(i-1)*1.35,1.5)
            locate4=(.05,(i-1)*1.35,1.45)
            bpy.ops.mesh.primitive_uv_sphere_add(
                segments=32,
                ring_count=24,
                size=.05,
                location=locate3
            )

            ob = bpy.context.object
            ob.name = "BolaPegangan"
            mymesh = ob.data
            bpy.ops.object.shade_smooth()
            mymesh.materials.append(mat)

            bpy.ops.mesh.primitive_cube_add(location=locate4)
            ob = bpy.context.object
            ob.name = "CubePegangan"
            mymesh = ob.data
            ob.scale =(.4,.03,.03)
            mymesh.materials.append(mat)

        else :
            locate2=(-.3,(i-2)*1.35,1.3)

        bpy.ops.mesh.primitive_torus_add(
            major_radius=.5,
            minor_radius=.8,
            location=locate2
        )
        ob = bpy.context.object
        ob.name = "PeganganKursi"
        mymesh = ob.data
        ob.scale = (.05,.05,.2)
        bpy.ops.object.shade_smooth()
        mymesh.materials.append(mat)

        


    # kaki
    for i in range(4) :
        locate2 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4, (i-1)*1.2, 0.7)
        else :
            locate2 = (.4, (i-2)*1.2, 0.7)
        bpy.ops.mesh.primitive_torus_add(major_radius=.5,
        minor_radius=.8,
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'kakiKursiTamu'
        ob.scale = feets
        mymesh = ob.data
        mymesh.materials.append(mat)

    # bola
    for i in range(4) :
        locate2 = (0,0,0)
        locate3 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4,(i-1)*1.2,1)
            locate3 = (-.4,(i-1)*1.2,.2)
        else :
            locate2 = (.4,(i-2)*1.2,1)
            locate3 = (.4,(i-2)*1.2,.2)
        
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.07, 
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaAtasKursiTamu2'
        mymesh = ob.data
        mymesh.materials.append(mat)

        # bola bawah
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.1, 
        location=locate3)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaBawahKursiTamu'
        mymesh = ob.data
        mymesh.materials.append(mat)
    
    # parenting object
    p1 = bpy.data.objects['PeganganKursi']
    p2 = bpy.data.objects['PeganganKursi.001']
    p3 = bpy.data.objects['PeganganKursi.002']
    p4 = bpy.data.objects['PeganganKursi.003']
    pgKursi = bpy.data.objects['PunggungKursi']
    bA1 = bpy.data.objects['bolaAtasKursiTamu2']
    bA2 = bpy.data.objects['bolaAtasKursiTamu2.001']
    bA3 = bpy.data.objects['bolaAtasKursiTamu2.002']
    bA4 = bpy.data.objects['bolaAtasKursiTamu2.003']
    bB1 = bpy.data.objects['bolaBawahKursiTamu']
    bB2 = bpy.data.objects['bolaBawahKursiTamu.001']
    bB3 = bpy.data.objects['bolaBawahKursiTamu.002']
    bB4 = bpy.data.objects['bolaBawahKursiTamu.003']
    kk1 = bpy.data.objects['kakiKursiTamu']
    kk2 = bpy.data.objects['kakiKursiTamu.001']
    kk3 = bpy.data.objects['kakiKursiTamu.002']
    kk4 = bpy.data.objects['kakiKursiTamu.003']
    kursiPjg = bpy.data.objects['KursiPanjang']
    bantalan = bpy.data.objects['BantalanKursi']
    bantalanPunggung = bpy.data.objects['BantalanPunggungKursi']
    bP1 = bpy.data.objects['BolaPegangan']
    bP2 = bpy.data.objects['BolaPegangan.001']
    cP1 = bpy.data.objects['CubePegangan']
    cP2 = bpy.data.objects['CubePegangan.001']
    KepalaKursi = bpy.data.objects['KepalaKursi']

    bpy.ops.object.select_all(action="DESELECT")
    pgKursi.select = True
    p1.select = True
    p2.select = True
    p3.select = True
    p4.select = True
    bA1.select = True
    bA2.select = True
    bA3.select = True
    bA4.select = True
    bB1.select = True
    bB2.select = True
    bB3.select = True
    bB4.select = True
    kk1.select = True
    kk2.select = True
    kk3.select = True
    kk4.select = True
    kursiPjg.select = True
    bantalan.select=True
    bantalanPunggung.select=True
    bP1.select=True
    bP2.select=True
    cP1.select=True
    cP2.select=True
    KepalaKursi.select=True

    bpy.context.scene.objects.active = pgKursi
    bpy.ops.object.parent_set()
     
    pgKursi.location= fix
    # pgKursi.rotation=(0,0,10)
    
    rotate = bpy.context.active_object
    rotate.rotation_mode='XYZ'
    rotate.rotation_euler = roFix

def kursi2(name, colorType, colorName, locate, size, feets, back, fix, roFix) :
    # create color
    color = bpy.data.materials.new(colorName)
    color.diffuse_color = colorType

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

    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=locate)

    ob = bpy.context.object
    ob.name = name
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=size
    path1 = os.path.expanduser('E:/Project/Animasi/Texture/benang.jpg')
    try :
        imgPath1 = bpy.data.images.load(path1)
    except :
        raise NameError("Cannot load images %s " % path1)
    
    texture1 = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture1.image = imgPath1

    mat1 = bpy.data.materials.new('texture')
    mText1 = mat1.texture_slots.add()
    mText1.texture_coords = 'GLOBAL'
    mText1.texture = texture1

    # bantalan kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(0,0,1.2),
    rotation=(10.9955,0,0))

    ob = bpy.context.object
    ob.scale = (.5,.05,1.3)
    ob.name="BantalanKursi2"
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # punggung kursi
    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=(-.5,0,1.5),
    rotation=(0,6.1,0))

    ob = bpy.context.object
    ob.name = "PunggungKursi2"
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=(.055,1.4,.5)

    # bantalan punggung kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(-0.45,0,1.45),
    rotation=(10.9955,10.87,0))

    ob = bpy.context.object
    ob.name="BantalanPunggungKursi2"
    ob.scale = (.4,.05,1.3)
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # kepala kursi
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        rotation=(0,7.67,0),
        location=(-0.53,0,1.7)
    )

    ob = bpy.context.object
    ob.scale = (.5,.6,.045)
    ob.name="KepalaKursi2"
    mymesh = ob.data
    mymesh.materials.append(mat)

    # pegangan kursi
    for i in range(4) :
        locate2=(0,0,0)
        locate3=(0,0,0)
        
        if(i%2==0) :
            locate2=(.45,(i-1)*1.35,1.3)
            locate3=(.45,(i-1)*1.35,1.5)
            locate4=(.05,(i-1)*1.35,1.45)
            bpy.ops.mesh.primitive_uv_sphere_add(
                segments=32,
                ring_count=24,
                size=.05,
                location=locate3
            )

            ob = bpy.context.object
            ob.name = "BolaPegangan2"
            mymesh = ob.data
            mymesh.materials.append(mat)
            bpy.ops.object.shade_smooth()

            bpy.ops.mesh.primitive_cube_add(location=locate4)
            ob = bpy.context.object
            ob.name = "CubePegangan2"
            mymesh = ob.data
            mymesh.materials.append(mat)
            ob.scale =(.4,.03,.03)

        else :
            locate2=(-.3,(i-2)*1.35,1.3)

        bpy.ops.mesh.primitive_torus_add(
            major_radius=.5,
            minor_radius=.8,
            location=locate2
        )
        ob = bpy.context.object
        ob.name = "PeganganKursi2"
        mymesh = ob.data
        mymesh.materials.append(mat)
        ob.scale = (.05,.05,.2)
        bpy.ops.object.shade_smooth()

        


    # kaki
    for i in range(4) :
        locate2 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4, (i-1)*1.2, 0.7)
        else :
            locate2 = (.4, (i-2)*1.2, 0.7)
        bpy.ops.mesh.primitive_torus_add(major_radius=.5,
        minor_radius=.8,
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'kakiKursiTamu2'
        ob.scale = feets
        mymesh = ob.data
        mymesh.materials.append(mat)

    # bola
    for i in range(4) :
        locate2 = (0,0,0)
        locate3 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4,(i-1)*1.2,1)
            locate3 = (-.4,(i-1)*1.2,.2)
        else :
            locate2 = (.4,(i-2)*1.2,1)
            locate3 = (.4,(i-2)*1.2,.2)
        
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.07, 
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaAtasKursiTamu22'
        mymesh = ob.data
        mymesh.materials.append(mat)

        # bola bawah
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.1, 
        location=locate3)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaBawahKursiTamu2'
        mymesh = ob.data
        mymesh.materials.append(mat)
    
    # parenting object
    p1 = bpy.data.objects['PeganganKursi2']
    p2 = bpy.data.objects['PeganganKursi2.001']
    p3 = bpy.data.objects['PeganganKursi2.002']
    p4 = bpy.data.objects['PeganganKursi2.003']
    pgKursi = bpy.data.objects['PunggungKursi2']
    bA1 = bpy.data.objects['bolaAtasKursiTamu22']
    bA2 = bpy.data.objects['bolaAtasKursiTamu22.001']
    bA3 = bpy.data.objects['bolaAtasKursiTamu22.002']
    bA4 = bpy.data.objects['bolaAtasKursiTamu22.003']
    bB1 = bpy.data.objects['bolaBawahKursiTamu2']
    bB2 = bpy.data.objects['bolaBawahKursiTamu2.001']
    bB3 = bpy.data.objects['bolaBawahKursiTamu2.002']
    bB4 = bpy.data.objects['bolaBawahKursiTamu2.003']
    kk1 = bpy.data.objects['kakiKursiTamu2']
    kk2 = bpy.data.objects['kakiKursiTamu2.001']
    kk3 = bpy.data.objects['kakiKursiTamu2.002']
    kk4 = bpy.data.objects['kakiKursiTamu2.003']
    kursiPjg = bpy.data.objects['KursiPanjang2']
    bantalan = bpy.data.objects['BantalanKursi2']
    bantalanPunggung = bpy.data.objects['BantalanPunggungKursi2']
    bP1 = bpy.data.objects['BolaPegangan2']
    bP2 = bpy.data.objects['BolaPegangan2.001']
    cP1 = bpy.data.objects['CubePegangan2']
    cP2 = bpy.data.objects['CubePegangan2.001']
    KepalaKursi = bpy.data.objects['KepalaKursi2']

    bpy.ops.object.select_all(action="DESELECT")
    pgKursi.select = True
    p1.select = True
    p2.select = True
    p3.select = True
    p4.select = True
    bA1.select = True
    bA2.select = True
    bA3.select = True
    bA4.select = True
    bB1.select = True
    bB2.select = True
    bB3.select = True
    bB4.select = True
    kk1.select = True
    kk2.select = True
    kk3.select = True
    kk4.select = True
    kursiPjg.select = True
    bantalan.select=True
    bantalanPunggung.select=True
    bP1.select=True
    bP2.select=True
    cP1.select=True
    cP2.select=True
    KepalaKursi.select=True

    bpy.context.scene.objects.active = pgKursi
    bpy.ops.object.parent_set()
     
    pgKursi.location= fix
    # pgKursi.rotation=(0,0,10)
    
    rotate = bpy.context.active_object
    rotate.rotation_mode='XYZ'
    rotate.rotation_euler = roFix

def kursi3(name, colorType, colorName, locate, size, feets, back, fix, roFix) :
    # create color
    color = bpy.data.materials.new(colorName)
    color.diffuse_color = colorType
    
    path = os.path.expanduser('E:\Project\Animasi\Texture\wood.jpg')
    
    try :
        imgPath = bpy.data.images.load(path)
    except :
        raise NameError("Cannot load images %s " % path)
    
    texture = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture.image = imgPath

    # create materials
    mat = bpy.data.materials.new('texture')
    mText = mat.texture_slots.add()
    mText.texture_coords = 'GLOBAL'
    mText.texture = texture


    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=locate)

    ob = bpy.context.object
    ob.name = name
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=size

    path1 = os.path.expanduser('E:/Project/Animasi/Texture/benang.jpg')
    
    try :
        imgPath1 = bpy.data.images.load(path1)
    except :
        raise NameError("Cannot load images %s " % path1)
    
    texture1 = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture1.image = imgPath1

    # create materials
    mat1 = bpy.data.materials.new('texture')
    mText1 = mat1.texture_slots.add()
    mText1.texture_coords = 'GLOBAL'
    mText1.texture = texture1

    # bantalan kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(0,0,1.2),
    rotation=(10.9955,0,0))

    ob = bpy.context.object
    ob.scale = (.5,.05,1.3)
    ob.name="BantalanKursi3"
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # punggung kursi
    bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=(-.5,0,1.5),
    rotation=(0,6.1,0))

    ob = bpy.context.object
    ob.name = "PunggungKursi3"
    mymesh = ob.data
    mymesh.materials.append(mat)
    ob.scale=(.055,1.4,.5)

    # bantalan punggung kursi
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,
    radius=1,
    depth=2,
    location=(-0.45,0,1.45),
    rotation=(10.9955,10.87,0))

    ob = bpy.context.object
    ob.name="BantalanPunggungKursi3"
    ob.scale = (.4,.05,1.3)
    mymesh = ob.data
    mymesh.materials.append(mat1)

    # kepala kursi
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=32,
        radius=1,
        depth=2,
        rotation=(0,7.67,0),
        location=(-0.53,0,1.7)
    )

    ob = bpy.context.object
    ob.scale = (.5,.6,.045)
    ob.name="KepalaKursi3"
    mymesh = ob.data
    mymesh.materials.append(mat)

    # pegangan kursi
    for i in range(4) :
        locate2=(0,0,0)
        locate3=(0,0,0)
        
        if(i%2==0) :
            locate2=(.45,(i-1)*1.35,1.3)
            locate3=(.45,(i-1)*1.35,1.5)
            locate4=(.05,(i-1)*1.35,1.45)
            bpy.ops.mesh.primitive_uv_sphere_add(
                segments=32,
                ring_count=24,
                size=.05,
                location=locate3
            )

            ob = bpy.context.object
            ob.name = "BolaPegangan3"
            mymesh = ob.data
            mymesh.materials.append(mat)
            bpy.ops.object.shade_smooth()

            bpy.ops.mesh.primitive_cube_add(location=locate4)
            ob = bpy.context.object
            ob.name = "CubePegangan3"
            mymesh = ob.data
            mymesh.materials.append(mat)
            ob.scale =(.4,.03,.03)

        else :
            locate2=(-.3,(i-2)*1.35,1.3)

        bpy.ops.mesh.primitive_torus_add(
            major_radius=.5,
            minor_radius=.8,
            location=locate2
        )
        ob = bpy.context.object
        ob.name = "PeganganKursi3"
        mymesh = ob.data
        mymesh.materials.append(mat)
        ob.scale = (.05,.05,.2)
        bpy.ops.object.shade_smooth()
        

        


    # kaki
    for i in range(4) :
        locate2 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4, (i-1)*1.2, 0.7)
        else :
            locate2 = (.4, (i-2)*1.2, 0.7)
        bpy.ops.mesh.primitive_torus_add(major_radius=.5,
        minor_radius=.8,
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'kakiKursiTamu3'
        ob.scale = feets
        mymesh = ob.data
        mymesh.materials.append(mat)

    # bola
    for i in range(4) :
        locate2 = (0,0,0)
        locate3 = (0,0,0)
        if(i%2 == 0) :
            locate2 = (-.4,(i-1)*1.2,1)
            locate3 = (-.4,(i-1)*1.2,.2)
        else :
            locate2 = (.4,(i-2)*1.2,1)
            locate3 = (.4,(i-2)*1.2,.2)
        
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.07, 
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaAtasKursiTamu23'
        mymesh = ob.data
        mymesh.materials.append(mat)

        # bola bawah
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.1, 
        location=locate3)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaBawahKursiTamu3'
        mymesh = ob.data
        mymesh.materials.append(mat)
    
    # parenting object
    p1 = bpy.data.objects['PeganganKursi3']
    p2 = bpy.data.objects['PeganganKursi3.001']
    p3 = bpy.data.objects['PeganganKursi3.002']
    p4 = bpy.data.objects['PeganganKursi3.003']
    pgKursi = bpy.data.objects['PunggungKursi3']
    bA1 = bpy.data.objects['bolaAtasKursiTamu23']
    bA2 = bpy.data.objects['bolaAtasKursiTamu23.001']
    bA3 = bpy.data.objects['bolaAtasKursiTamu23.002']
    bA4 = bpy.data.objects['bolaAtasKursiTamu23.003']
    bB1 = bpy.data.objects['bolaBawahKursiTamu3']
    bB2 = bpy.data.objects['bolaBawahKursiTamu3.001']
    bB3 = bpy.data.objects['bolaBawahKursiTamu3.002']
    bB4 = bpy.data.objects['bolaBawahKursiTamu3.003']
    kk1 = bpy.data.objects['kakiKursiTamu3']
    kk2 = bpy.data.objects['kakiKursiTamu3.001']
    kk3 = bpy.data.objects['kakiKursiTamu3.002']
    kk4 = bpy.data.objects['kakiKursiTamu3.003']
    kursiPjg = bpy.data.objects['KursiPanjang3']
    bantalan = bpy.data.objects['BantalanKursi3']
    bantalanPunggung = bpy.data.objects['BantalanPunggungKursi3']
    bP1 = bpy.data.objects['BolaPegangan3']
    bP2 = bpy.data.objects['BolaPegangan3.001']
    cP1 = bpy.data.objects['CubePegangan3']
    cP2 = bpy.data.objects['CubePegangan3.001']
    KepalaKursi = bpy.data.objects['KepalaKursi3']

    bpy.ops.object.select_all(action="DESELECT")
    pgKursi.select = True
    p1.select = True
    p2.select = True
    p3.select = True
    p4.select = True
    bA1.select = True
    bA2.select = True
    bA3.select = True
    bA4.select = True
    bB1.select = True
    bB2.select = True
    bB3.select = True
    bB4.select = True
    kk1.select = True
    kk2.select = True
    kk3.select = True
    kk4.select = True
    kursiPjg.select = True
    bantalan.select=True
    bantalanPunggung.select=True
    bP1.select=True
    bP2.select=True
    cP1.select=True
    cP2.select=True
    KepalaKursi.select=True

    bpy.context.scene.objects.active = pgKursi
    bpy.ops.object.parent_set()
     
    pgKursi.location= fix
    # pgKursi.rotation=(0,0,10)
    
    rotate = bpy.context.active_object
    rotate.rotation_mode='XYZ'
    rotate.rotation_euler = roFix
def run():
    blue = (.5,.5,1)
    kursi('KursiPanjang',blue,'Biru', (0,0,1.1),(.5,1.4,.1),(.05,.05,.6),(.08,.08,.4),(-4.3,3,1.45), (0,-0.2,0) )
    kursi2('KursiPanjang2',blue,'Biru', (0,0,1.1),(.5,1.4,.1),(.05,.05,.6),(.08,.08,.4),(0.3,3,1.45), (0,-0.2,3.15) )
    kursi3('KursiPanjang3',blue,'Biru', (0,0,1.1),(.5,1.4,.1),(.05,.05,.6),(.08,.08,.4),(0.9,-7.6,1.45), (0,-0.2,1.59) )
    

if __name__ == "__main__" :
    run()