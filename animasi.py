import bpy, time

def run() :
    scene = bpy.context.scene

    # # Create new lamp datablock
    # lamp_data = bpy.data.lamps.new(name="New Lamp", type='POINT')

    # # Create new object with our lamp datablock
    # lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # # Link lamp object to the scene so it'll appear in this scene
    # scene.objects.link(lamp_object)

    # # Place lamp to a specified location
    # lamp_object.location = (1, 1, 1)

    # # And finally select it make active
    # lamp_object.select = True
    # scene.objects.active = lamp_object

    saklar = bpy.data.objects['saklar']
    saklar.rotation_mode = 'XYZ'
    saklar.rotation_euler = (0,-.3,0)

    color = bpy.data.materials.new('color')
    color.diffuse_color = (0,0,0)

    layar = bpy.data.objects['layarMonitor']
    layar.location=(-3.19,-5.7,2.15)
    layar.active_material = color
    
    kursi = bpy.data.objects['punggungKursiKomputer']
    kursi.location=(-2.5,-5.65,1.65)

    camera = bpy.data.objects['Camera']
    camera.location = (-4,11,2)
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler = (1.5,0,3.3)

    animate_door = bpy.data.objects['manik2']
    animate_door.rotation_mode = 'XYZ'

    bpy.context.scene.frame_set(0)
    camera.location = (-4,12,2.2)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(50)
    camera.location = (-4,10,2.2)
    camera.keyframe_insert(data_path="location")
    
    bpy.context.scene.frame_set(60)
    animate_door.rotation_euler = (0,0,0)
    animate_door.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(110)
    animate_door.rotation_euler = (0,0,-1.5)
    animate_door.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(150)
    camera.location = (-4,7.8,2.2)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler = (1.5,0,3.3)
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(160)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(165)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(175)
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(180)
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(185)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(190)
    camera.location = (-4,7.8,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(195)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)
    
    bpy.context.scene.frame_set(200)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(205)
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(210)
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(215)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(220)
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)
    
    bpy.context.scene.frame_set(230)
    camera.location = (1.3,7.8,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(245)
    camera.location = (1.3,7,2.5)
    camera.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(250)
    camera.location = (1.3,6.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(255)
    camera.location = (1.3,6,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(260)
    camera.location = (1.3,5.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(265)
    camera.location = (1.3,5,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(270)
    camera.location = (1.3,4.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.5
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(275)
    camera.location = (1.3,4,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.5
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(280)
    camera.location = (1.3,3.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(285)
    camera.location = (1.3,3,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(290)
    camera.location = (1.3,2.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(295)
    camera.location = (1.3,2,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(300)
    camera.location = (1.3,1.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(305)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(325)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 1
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(335)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 1
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(355)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(360)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(370)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3.5
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(375)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3.5
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(385)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(390)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 3
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(400)
    camera.location = (1.3,1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(405)
    camera.location = (2,0,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(410)
    camera.location = (2,0,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4.3
    camera.keyframe_insert('rotation_euler', index=2)
    saklar.rotation_euler.y = -.3
    saklar.keyframe_insert('rotation_euler', index=1)

    bpy.context.scene.frame_set(415)
    camera.location = (2,0,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4.3
    camera.keyframe_insert('rotation_euler', index=2)
    saklar.rotation_euler.y = -.3
    saklar.keyframe_insert('rotation_euler', index=1)

    bpy.context.scene.frame_set(420)
    camera.location = (2,0,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 4.3
    camera.keyframe_insert('rotation_euler', index=2)
    saklar.rotation_euler.y = .3
    saklar.keyframe_insert('rotation_euler', index=1)
    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="myLamp", type='POINT')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="myLamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    # scene.objects.link(lamp_object)

    # Place lamp to a specified location
    lamp_object.location = (0, -3, 5)

    # And finally select it make active
    # lamp_object.select = True
    # scene.objects.active = lamp_object
    scene.objects.link(lamp_object)

    lamp = bpy.data.lamps['myLamp']
    lamp.energy = 0
    lamp.keyframe_insert(data_path='energy', index=-1)

    bpy.context.scene.frame_set(425)
    lamp.energy = 3
    lamp.keyframe_insert(data_path='energy', index=-1)

    bpy.context.scene.frame_set(435)
    camera.location = (2,0,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(440)
    camera.location = (2,0,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(445)
    camera.location = (1.5,-.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(450)
    camera.location = (1,-1,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(455)
    camera.location = (.5,-1.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(460)
    camera.location = (0,-2,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(465)
    camera.location = (-.5,-2.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)

    bpy.context.scene.frame_set(470)
    camera.location = (-1,-3,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-2.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")
    
    bpy.context.scene.frame_set(475)
    camera.location = (-1,-3,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-2.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(485)
    camera.location = (-1,-3,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(490)
    camera.location = (-1,-3,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(495)
    camera.location = (-1.5,-3.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(500)
    camera.location = (-2,-4,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(505)
    camera.location = (-2.5,-4.5,2.4)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(510)
    camera.location = (-2.5,-5,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2.4
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(515)
    camera.location = (-2.5,-5,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(520)
    camera.location = (-2.5,-5,2.5)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2
    camera.keyframe_insert('rotation_euler', index=2)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")
    camera.rotation_euler.y = 0
    camera.keyframe_insert('rotation_euler', index=1)
    camera.rotation_euler.x = 1.5
    camera.keyframe_insert('rotation_euler', index=0)

    bpy.context.scene.frame_set(525)
    camera.location = (-2.5,-5,2)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2
    camera.keyframe_insert('rotation_euler', index=2)
    camera.rotation_euler.x = 1.7
    camera.keyframe_insert('rotation_euler', index=0)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")

    bpy.context.scene.frame_set(535)
    camera.location = (-2.5,-5,2)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2
    camera.keyframe_insert('rotation_euler', index=2)
    camera.rotation_euler.x = 1.7
    camera.keyframe_insert('rotation_euler', index=0)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")
    color.diffuse_color = (0,0,0)
    color.keyframe_insert(data_path="diffuse_color", index=-1)

    bpy.context.scene.frame_set(540)
    camera.location = (-2.5,-5,2)
    camera.keyframe_insert(data_path="location")
    camera.rotation_euler.z = 2
    camera.keyframe_insert('rotation_euler', index=2)
    camera.rotation_euler.x = 1.7
    camera.keyframe_insert('rotation_euler', index=0)
    kursi.location=(-1.5,-5.65,1.65)
    kursi.keyframe_insert(data_path="location")
    color.diffuse_color = (1,1,1)
    color.keyframe_insert(data_path="diffuse_color", index=-1)





        




    


    
if __name__ == "__main__" :
    run()