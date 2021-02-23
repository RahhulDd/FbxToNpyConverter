import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def visualise_frames(pathtonpy='json2np/Aim Pistol/Aim Pistol.npy',up_view=0,side_view=90,x_lim=[-2,2],y_lim=[-2,2],z_lim=[-2,2]):
    #MIXAMO DATASET
    """
    Each POSE follow the given index joints below:
    
        0 - Head
        1 - Neck
        2 - Lshoulder
        3 - Lelbow
        4 - Lwrist
        5 - Rshoulder
        6 - Relbow
        7 - Rwrist
        8 - Pelvis
        9 - Lhip
        10 - Lknee
        11 - Lankle
        12 - Rhip
        13 - Rknee
        14 - Rankle
    """
    #Load .npy file
    motion3d = np.load(pathtonpy)

    #Index for bone links
    bones = [[0,1],[1,2],[2,3],[3,4],[1,5],[5,6],[6,7],[1,8],[8,9],[9,10],[10,11],[8,12],[12,13],[13,14]]

    #Set offset for few frame visualisation
    offset = int(motion3d.shape[2]/5)
    offset_sum = 0

    #Output frames
    for i in range(5):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter(motion3d[:,0,offset_sum],motion3d[:,1,offset_sum],motion3d[:,2,offset_sum])
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)
        ax.set_zlim(z_lim)
        for i in range(len(bones)):
            ax.plot3D([motion3d[bones[i][0],0,offset_sum],motion3d[bones[i][1],0,offset_sum]],[motion3d[bones[i][0],1,offset_sum],motion3d[bones[i][1],1,offset_sum]],[motion3d[bones[i][0],2,offset_sum],motion3d[bones[i][1],2,offset_sum]])

        ax.view_init(up_view,side_view)
        print(offset_sum)
        ax.set_title('Frame: %d'%(offset_sum))
        offset_sum = offset_sum+offset

if __name__='__main__':
    visualise_frames()
