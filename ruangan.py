import bpy,os

def cubeWithColor(name, colorType, colorName, locate, size, path) :
    color = bpy.data.materials.new(colorName)
    color.diffuse_color = colorType

    try :
        imgPath = bpy.data.images.load(path)
    except :
        raise NameError("Cannot load image %s" % path)
    
    texture = bpy.data.textures.new('ColorTex', type="IMAGE")
    texture.image = imgPath

    # create materials
    mat = bpy.data.materials.new('Texture')
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

def run() :
    white = (1,1,1)
    dinding = os.path.expanduser('E:\Project\Animasi\Texture\wall.jpg')
    floor = os.path.expanduser('E:/Project/Animasi/Texture/floor2.jpg')
    
    # create material

    cubeWithColor('LantaiUtama', white, 'White', (0,0,.1),       (5,8,.1), floor)
    cubeWithColor('LantaiKamarTengah', white, 'White', (6,0,.1),       (1,1,.1), floor)
    cubeWithColor('LantaiKamarDepan', white, 'White', (4,9.5,.1),     (1,1.5,.1), floor)
    cubeWithColor('LantaiDapur', white, 'White', (4,-9.5,.1),    (1,1.5,.1), floor)
    cubeWithColor('LantaiDepan', white, 'White', (-4,9.5,.3),    (1,1.5,.3), floor)
    cubeWithColor('Dinding', white, 'White', (-3.1,9.5,1.6), (.1,1.5,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (-4.9,1.5,1.6), (.1,9.5,1.5), dinding)
    cubeWithColor('DindingBelakang1', white, 'White', (-1,-7.9,1.6),    (4,.1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (3.1,-9.3,1.6), (.1,1.5,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (4,-10.9,1.6), (1,.1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (4.9,-6,1.6), (.1,5,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (5.9,-.9,1.6), (1.1,.1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (6.9,0,1.6), (.1,1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (5.9,.9,1.6), (1.1,.1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (4.9,6,1.6), (.1,5,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (4,10.9,1.6), (1,.1,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (3.1,9.5,1.6), (.1,1.5,1.5), dinding)
    cubeWithColor('Dinding', white, 'White', (0,8,1.6), (3.2,.1,1.5), dinding)

if __name__ == "__main__" :
    run()