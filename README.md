# FBX-to-NPY Converter
Script to process and convert .fbx file format to .npy file format only for human motion analysis.

The script needs the Blender to run. If you don't have Blender, then you can download it from the link below:

https://www.blender.org/download/

For Mixamo Data, use this link:

https://www.mixamo.com/#/?page=1&type=Motion%2CMotionPack&limit=96

Once the Blender is downloaded, install it and add it's directory PATH to the ENVIRONMENT VARIABLES.

A). To run the script:
 1. Open CMD prompt with administrator permisson.
 2. Change to the directory where 'fbx2npy.py' is located.
 3. Type the command: 'blender --background -P fbx2npy.py'
 4. If you installed and add Blender directory PATH correctly, then above command won't be a problem.

B). To visualise the .npy generated files, use 'visualise_frames.py'. This only works with single .npy file so be careful to mention PATH to .npy file.

Voila!! you have prepared the .npy files for your ML/DL project or anything else.
