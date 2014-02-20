 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees d'une ellipse dans une image
def roi_ellipse(im,cx,cy,a,b):
    H,W = im.shape
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))
    roi = (( ((X-cx)/a**2)**2 + ((Y-cy)/b**2)**2 ) <= r**2) * 1
    
    roiX,roiY,rawdata = (X+1)*roi, (Y+1)*roi, (im+1)*roi
    
    #roiX_flat = np.matrix(filter(lambda a: a!=0, roiX.flatten())) - 1
    #roiY_flat = np.matrix(filter(lambda a: a!=0, roiY.flatten())) - 1
    #rawdata_flat = np.matrix(filter(lambda a: a!=0, rawdata.flatten())) - 1
    return roiX,roiY,rawdata
    #return roiX_flat,roiY_flat,rawdata_flat 

    
    
#######################################################
####################    TEST    ####################### 
#######################################################

def test_ellipse():
    im = lena()
    roiX,roiY,rawdata = roi_ellipse(im,250,250,5)
    print roiX
    print roiY
    
    
if __name__ == "__main__":
    test_ellipse()    