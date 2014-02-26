#! /usr/bin/python2.7

"""
Mean shift - kernel
Contient les fonctions de caclcul des kernels
"""

import numpy as np
import matplotlib.pyplot as plt

# Definition du kernel utilise, Epanechnikov ou Gaussien
def kernel(x, normal=1):
    if normal==1: # normal
        kernel =  np.exp(-0.5*x)
    else : # Epanechnikov
        #c = 4.0/3*pi
        kernel = np.multiply(x<1,1-x)
    
    if kernel.sum() != 0 :
        kernel = kernel / kernel.sum() # Normallisation du kernel
    else :
        kernel = np.zeros(kernel.shape)
    return kernel
    
# Calcul la fonction kernel au centre (cx,cy) pour l'image im
def kernel_centre(im, ci, cj, normal=1):
    H,W = im.shape    
    J,I = np.meshgrid(np.arange(-cj,W-cj),np.arange(-ci,H-ci))    
    k = kernel((np.multiply(I,I) + np.multiply(J,J)),normal)
    return k
    
    

    
if __name__ == "__main__":
    im = np.zeros((25,25))
    ker = kernel_centre(im,12,12)
    plt.imshow(ker)
    plt.show()