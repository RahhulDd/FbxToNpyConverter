# FbxToNpyConverter
Script to process and convert .fbx file format to .npy file format only for human motion analysis.

The script needs the Blender to run. If you don't have Blender, then you can download it from the link below:

Once the Blender is downloaded, install it and add it's directory PATH to the ENVIRONMENT VARIABLES.

To run the script:
 1. Open CMD prompt with administrator permisson.
 2. Change to the directory where 'fbx2npy.py' is located.
 3. Type the command: 'blender --background -P fbx2npy.py'
 4. If you installed and add Blender directory PATH correctly, then above command won't be a problem.

Voila!! you have prepared the .npy files for your ML/DL project or anything else.
