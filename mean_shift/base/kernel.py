#! /usr/bin/python2.7

"""
Mean shift - kernel
Contient les fonctions de caclcul des kernels
"""

import numpy as np

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
def kernel_centre(im, cx, cy, normal=1):
    H,W = im.shape    
    X,Y = np.meshgrid(np.arange(-cx,W-cx),np.arange(-cy,H-cy))    
    k = kernel(np.sqrt(np.multiply(X,X) + np.multiply(Y,Y)))
    return k
    
    

def kernel_g(x, normal=1):
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