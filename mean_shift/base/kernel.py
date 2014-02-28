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
        kernel = np.exp(-0.5*x)
        kernel = np.multiply(kernel,kernel>1e-4)
    else : # Epanechnikov
        #c = 4.0/3*pi
        kernel = np.multiply(x<1,1-x)
    
    if kernel.sum() != 0 :
        kernel = kernel / kernel.sum() # Normallisation du kernel
    else :
        kernel = np.zeros(kernel.shape)
    return kernel
    
# Calcul la fonction kernel au centre (cx,cy) pour l'image im
def kernel_centre(im_shape, ci, cj, normal=1, h=0):
    H,W = im_shape    
    J,I = np.meshgrid(np.arange(-cj,W-cj),np.arange(-ci,H-ci))
    if h>0:
        k = kernel((np.multiply(I,I) + np.multiply(J,J))/h**2,normal)
    else :
        k = kernel((np.multiply(I,I) + np.multiply(J,J)),normal)
    return k
    
    

    
if __name__ == "__main__":
    I,J = np.meshgrid(np.arange(0,5),np.arange(0,10))
    print I
    print J
#    shape = 100,100
#    ci,cj = 50,50
#    h = 25
#    k1 = kernel_centre(shape,ci,cj,normal=1,h=0)
#    k2 = kernel_centre(shape,ci,cj,normal=1,h=25)
#
#    plt.imshow(k1)
#    plt.show()