 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees du cercle dans une image
# TODO : optimiser !
def roi_cercle(im,ci,cj,r, raw=0):
    H,W = im.shape
    J,I = np.meshgrid(np.arange(0,W),np.arange(0,H))
    roi = (((J-cj)**2 + (I-ci)**2) <= (r**2 + 1)) * 1
    
    #Juste rawdata
    if raw==1:    
        rawdata, roiI, roiJ = (im+1)*roi, 0, 0
        rawdata = rawdata.flatten()
        rawdata = rawdata[rawdata != 0] -1
    
    else:    
        # roiI = les numeros de lignes des elements de la roi
        roiI,roiJ,rawdata = (I+1)*roi, (J+1)*roi, (im+1)*roi
        roiI,roiJ,rawdata = roiI.flatten(), roiJ.flatten(), rawdata.flatten()    
        roiI = roiI[roiI != 0] -1
        roiJ = roiJ[roiJ != 0] -1
        rawdata = rawdata[rawdata != 0] -1
    
    return roiI,roiJ,rawdata
    

# TODO : Faire une fonction extract_roi
    
    
    
    
    
#######################################################
####################    TEST    ####################### 
#######################################################

def test_cercle():
    im = lena()
    roiI,roiJ,rawdata = roi_cercle(im,250,250,5)
    print roiI
    print roiJ
    
    
if __name__ == "__main__":
    test_cercle()    