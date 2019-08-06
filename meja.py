import bpy, os

def mejaTamu(name, colorType, colorName, locate, size, feets) :
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

    atasMeja = bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=locate)

    ob = bpy.context.object
    ob.name = name
    myMesh = ob.data
    myMesh.materials.append(mat)
    ob.scale = size

    a = bpy.data.objects['Meja1']

    a.select = True
    
    for i in range (4) :
        locate2 = (0,0,0)
        if(i%2==0) :
            locate2=(-1.5,i+1.5,.55)
            
        else :
            locate2 = (-2.5,i+.5,.55)
        
        bpy.ops.mesh.primitive_torus_add(major_radius=.5, 
        minor_radius=.8,
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        myMesh = ob.data
        myMesh.materials.append(mat)
        ob.name = "kaki"
        ob.scale = feets

    

    

    for i in range (4) :
        locate2 = (0,0,0)
        locate3 = (0,0,0)
        if(i%2==0) :
            locate2 = (-1.5,i+1.5,.9)
            locate3 = (-1.5,i+1.5,.15)
        else :
            locate2 = (-2.5, i+.5, .9)
            locate3 = (-2.5, i+.5, .15)
        
        # bola atas
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.07, 
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaAtas'
        myMesh = ob.data
        myMesh.materials.append(mat)

        # bola bawah
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.1, 
        location=locate3)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaBawah'
        myMesh = ob.data
        myMesh.materials.append(mat)

    k1 = bpy.data.objects['kaki']
    k2 = bpy.data.objects['kaki.001']
    k3 = bpy.data.objects['kaki.002']
    k4 = bpy.data.objects['kaki.003']

    bA1 = bpy.data.objects['bolaAtas']
    bA2 = bpy.data.objects['bolaAtas.001']
    bA3 = bpy.data.objects['bolaAtas.002']
    bA4 = bpy.data.objects['bolaAtas.003']

    bB1 = bpy.data.objects['bolaBawah']
    bB2 = bpy.data.objects['bolaBawah.001']
    bB3 = bpy.data.objects['bolaBawah.002']
    bB4 = bpy.data.objects['bolaBawah.003']

    bpy.ops.object.select_all(action="DESELECT")
    a.select = True
    k1.select = True
    k2.select = True
    k3.select = True
    k4.select = True
    bA1.select = True
    bA2.select = True
    bA3.select = True
    bA4.select = True
    bB1.select = True
    bB2.select = True
    bB3.select = True
    bB4.select = True

    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()

    a.location = (-2,3,1) 

def mejaTamu2(name, colorType, colorName, locate, size, feets) :
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

    atasMeja = bpy.ops.mesh.primitive_cube_add(view_align=False,
    enter_editmode=False,
    location=locate)

    ob = bpy.context.object
    ob.name = name
    myMesh = ob.data
    myMesh.materials.append(mat)
    ob.scale = size

    a = bpy.data.objects['Meja2']

    a.select = True
    
    for i in range (4) :
        locate2 = (0,0,0)
        if(i%2==0) :
            locate2=(-1.5,(i+5.3)/2.5,.45)
            
        else :
            locate2 = (-2.5,(i+4.3)/2.5,.45)
        
        bpy.ops.mesh.primitive_torus_add(major_radius=.5, 
        minor_radius=.8,
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = "kaki2"
        ob.scale = feets
        myMesh = ob.data
        myMesh.materials.append(mat)

    for i in range (4) :
        locate2 = (0,0,0)
        locate3 = (0,0,0)
        if(i%2==0) :
            locate2 = (-1.5,(i+5.3)/2.5,.7)
            locate3 = (-1.5,(i+5.3)/2.5,.15)
        else :
            locate2 = (-2.5,(i+4.3)/2.5, .7)
            locate3 = (-2.5,(i+4.3)/2.5, .15)
        
        # bola atas
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.07, 
        location=locate2)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaAtas2'
        myMesh = ob.data
        myMesh.materials.append(mat)

        # bola bawah
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32,
        ring_count=24,
        size=.1, 
        location=locate3)
        bpy.ops.object.shade_smooth()
        ob = bpy.context.object
        ob.name = 'bolaBawah2'
        myMesh = ob.data
        myMesh.materials.append(mat)

    k1 = bpy.data.objects['kaki2']
    k2 = bpy.data.objects['kaki2.001']
    k3 = bpy.data.objects['kaki2.002']
    k4 = bpy.data.objects['kaki2.003']

    bA1 = bpy.data.objects['bolaAtas2']
    bA2 = bpy.data.objects['bolaAtas2.001']
    bA3 = bpy.data.objects['bolaAtas2.002']
    bA4 = bpy.data.objects['bolaAtas2.003']

    bB1 = bpy.data.objects['bolaBawah2']
    bB2 = bpy.data.objects['bolaBawah2.001']
    bB3 = bpy.data.objects['bolaBawah2.002']
    bB4 = bpy.data.objects['bolaBawah2.003']

    bpy.ops.object.select_all(action="DESELECT")
    a.select = True
    k1.select = True
    k2.select = True
    k3.select = True
    k4.select = True
    bA1.select = True
    bA2.select = True
    bA3.select = True
    bA4.select = True
    bB1.select = True
    bB2.select = True
    bB3.select = True
    bB4.select = True

    bpy.context.scene.objects.active = a
    bpy.ops.object.parent_set()

    a.location = (-2,4.9,.8) 
def run() :
    red = (1,.5,.5)
    green = (.5,1,.5)
    # urutan parameter name, colorType, colorName, locate, size, feets 
    mejaTamu('Meja1', red,'Red',(-2,2.5,1),(.7,1.4,.05),(.05,.05,.4))
    mejaTamu2('Meja2', green,'Green',(-2,2.5,.8),(.7,.5,.05),(.05,.05,.3))

if __name__ == "__main__" :
    run()