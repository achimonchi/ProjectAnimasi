import bpy, os

def run() :
    path = os.path.expanduser('E:\Project\Animasi\Texture\carpet2.jpg')

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


    bpy.ops.mesh.primitive_cube_add(
        location=(-2,3,.2)
    )
    ob = bpy.context.object
    ob.scale=(1.3,1.5,.01)
    ob.name="KarpetTamu"
    mymesh = ob.data
    mymesh.materials.append(mat)


    path = os.path.expanduser('E:\Project\Animasi\Texture\carpet1.jpg')

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


    bpy.ops.mesh.primitive_cube_add(
        location=(0,-4.5,.2)
    )
    ob = bpy.context.object
    ob.scale=(2.7,2,.01)
    ob.name="KarpetKomputer"
    mymesh = ob.data
    mymesh.materials.append(mat)

if __name__ == "__main__" :
    run()