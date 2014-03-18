 #! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import lena

# Retourne les coordonnees du cercle dans une image
# TODO : optimiser !
def roi_quad(im_shape,ci,cj,r):
    H,W = im_shape
    roi = np.zeros((H,W))
    roi[ci-r/2:ci+r/2, cj-r/2:ci+r/2] = 1
    return roi
    


    
#######################################################
####################    TEST    ####################### 
#######################################################

def test_cercle():
    im = lena()
    roi = roi_quad(im.shape,250,250,400)
    im = np.multiply(roi,im)
    
    plt.imshow(im)
    plt.show()
    
if __name__ == "__main__":
    test_cercle()     
