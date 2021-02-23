import bpy
import os
import time
import sys
import json
from mathutils import Vector
import numpy as np 

HOME_FILE_PATH = os.path.abspath('C:\\Users\\dubs\\Desktop\\BlenderTrialMotionRetargeting2d\\homefile.blend')
MIN_NR_FRAMES = 64
RESOLUTION = (512, 512)

#Crucial joints sufficient for visualisation #FIX ME - Add more joints if desirable for MixamRig
BASE_JOINT_NAMES = ['Head', 'Neck',
                    'RightArm', 'RightForeArm', 'RightHand', 'LeftArm', 'LeftForeArm', 'LeftHand',
                    'Hips', 'RightUpLeg', 'RightLeg', 'RightFoot', 'LeftUpLeg', 'LeftLeg', 'LeftFoot',
                    ]
#Source directory where .fbx exist
SRC_DATA_DIR ='C:\\Users\\dubs\\Desktop\\BlenderTrialMotionRetargeting2d\\regular'

#Ouput directory where .fbx to JSON dict will be stored
OUT_DATA_DIR ='C:\\Users\\dubs\\Desktop\\BlenderTrialMotionRetargeting2d\\fbx2json'

#Final directory where NPY files will ve stored
FINAL_DIR_PATH ='C:\\Users\\dubs\\Desktop\\BlenderTrialMotionRetargeting2d\\json2npy'

#Number of joints to be used from MixamoRig
joint_names = ['mixamorig:' + x for x in BASE_JOINT_NAMES]

def fbx2jointDict():
    
    #Remove 'Cube' object if exists in the scene
    if bpy.data.objects.get('Cube') is not None:
        cube = bpy.data.objects['Cube']
        bpy.data.objects.remove(cube)
    
    #Intensify Light Point in the scene
    if bpy.data.objects.get('Light') is not None:
        bpy.data.objects['Light'].data.energy = 2
        bpy.data.objects['Light'].data.type = 'POINT'
    
    #Set resolution and it's rendering percentage
    bpy.data.scenes['Scene'].render.resolution_x = RESOLUTION[0]
    bpy.data.scenes['Scene'].render.resolution_y = RESOLUTION[1]
    bpy.data.scenes['Scene'].render.resolution_percentage = 100
    
    #Base file for blender
    bpy.ops.wm.save_as_mainfile(filepath=HOME_FILE_PATH)
    
    #Get animation(.fbx) file paths
    anims_path = os.listdir(SRC_DATA_DIR)
    
    #Make OUT_DATA_DIR
    if not os.path.exists(OUT_DATA_DIR):
        os.makedirs(OUT_DATA_DIR)    
    
    for anim_name in anims_path:
        
        anim_file_path = os.path.join(SRC_DATA_DIR,anim_name)
        save_dir = os.path.join(OUT_DATA_DIR,anim_name.split('.')[0],'JointDict')
        
        #Make save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        #Load HOME_FILE and .fbx file
        bpy.ops.wm.read_homefile(filepath=HOME_FILE_PATH)
        bpy.ops.import_scene.fbx(filepath=anim_file_path)
        
        #End Frame Index for .fbx file
        frame_end = bpy.data.actions[0].frame_range[1]
        
        for i in range(int(frame_end)+1):
            
            bpy.context.scene.frame_set(i)
            
            bone_struct = bpy.data.objects['Armature'].pose.bones
            armature = bpy.data.objects['Armature']

            out_dict = {'pose_keypoints_3d': []}
        
            for name in joint_names:
                global_location = armature.matrix_world @ bone_struct[name].matrix @ Vector((0, 0, 0))
                l = [global_location[0], global_location[1], global_location[2]]
                out_dict['pose_keypoints_3d'].extend(l)
            
            save_path = os.path.join(save_dir,'%04d_keypoints.json'%i)
            with open(save_path,'w') as f:
                json.dump(out_dict, f)

def jointDict2npy():
    
    json_dir = OUT_DATA_DIR
    npy_dir = FINAL_DIR_PATH
    if not os.path.exists(npy_dir):
        os.makedirs(npy_dir)
        
    anim_names = os.listdir(json_dir)
    
    for anim_name in anim_names:
        files_path = os.path.join(json_dir,anim_name,'jointDict')
        frame_files = os.listdir(files_path)
        
        motion = []
                
        for frame_file in frame_files:
            file_path = os.path.join(files_path,frame_file)
            
            with open(file_path) as f:
                info = json.load(f)
                joint = np.array(info['pose_keypoints_3d']).reshape((-1, 3))
            motion.append(joint[:15,:])
            
        motion = np.stack(motion,axis=2)
        save_path = os.path.join(npy_dir,anim_name)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            
        print(save_path)
        
        np.save(save_path+'\\'+'{i}.npy'.format(i=anim_name),motion)
        
if __name__ == '__main__':
    
    #Convert .fbx files to JSON dict
    fbx2jointDict()
    
    #Convert JSON dict to NPY 
    jointDict2npy()           


