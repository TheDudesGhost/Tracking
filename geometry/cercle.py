 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees du cercle dans une image
# TODO : optimiser !
def roi_cercle(im,cx,cy,r, raw=0):
    H,W = im.shape
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))
    roi = (((X-cx)**2 + (Y-cy)**2) <= (r**2 + 1)) * 1
    
    #Juste rawdata
    if raw==1:    
        rawdata, roiX, roiY = (im+1)*roi, 0, 0
        rawdata = rawdata.flatten()
        rawdata = rawdata[rawdata != 0] -1
    
    else:    
        roiX,roiY,rawdata = (X+1)*roi, (Y+1)*roi, (im+1)*roi
        roiX,roiY,rawdata = roiX.flatten(), roiY.flatten(), rawdata.flatten()    
        roiX = roiX[roiX != 0] -1
        roiY = roiY[roiY != 0] -1
        rawdata = rawdata[rawdata != 0] -1
    
    return roiX,roiY,rawdata
    

# TODO : Faire une fonction extract_roi
    
    
    
    
    
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