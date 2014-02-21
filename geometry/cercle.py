 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees du cercle dans une image
# TODO : optimiser !
def roi_cercle(im,cx,cy,r):
    H,W = im.shape
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))
    roi = (((X-cx)**2 + (Y-cy)**2) <= (r**2 + 1)) * 1
    
    roiX,roiY,rawdata = (X+1)*roi, (Y+1)*roi, (im+1)*roi
    roiX = roiX.flatten() 
    roiY = roiY.flatten()
    rawdata = rawdata.flatten()    
#    roiX_flat = np.array(filter(lambda a: a!=0, roiX.flatten())) - 1
#    roiY_flat = np.array(filter(lambda a: a!=0, roiY.flatten())) - 1
#    rawdata_flat = np.array(filter(lambda a: a!=0, rawdata.flatten())) - 1
    roiX = roiX[roiX != 0] -1
    roiY = roiY[roiY != 0] -1
    rawdata = rawdata[rawdata != 0] -1
    
    return roiX,roiY,rawdata
    
 
    
    
    
    
    
#######################################################
####################    TEST    ####################### 
#######################################################

def test_cercle():
    im = lena()
    roiX,roiY,rawdata = roi_cercle(im,250,250,5)
    print roiX
    print roiY
    
    
if __name__ == "__main__":
    test_cercle()    