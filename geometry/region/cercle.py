 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees du cercle dans une image
# TODO : optimiser !
def roi_cercle(im,ci,cj,r):
    H,W = im.shape
    J,I = np.meshgrid(np.arange(0,W),np.arange(0,H))
    roi = (((J-cj)**2 + (I-ci)**2) <= (r**2 + 1)) * 1
    return roi
    

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