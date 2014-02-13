#! /usr/bin/python2.7

"""
Mean shift - util
Contient les fonctions calculant les fonctions mathematiques
requises pour le calcul de la mean shift
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np


# Definition du kernel utilise, Epanechnikov ou Gaussien
def kernel(x, dim=2, normal=1):
    if normal==1: # normal
        kernel = (2*pi)**(-dim/2) * np.exp(-0.5*x)
    else : # Epanechnikov
        c = 4.0/3*pi
        kernel = np.multiply(x<1,1-x)*(0.5/c)*(dim+2)
    return kernel

# Calcul de la distribution du modele par rapport a Z, centree en 0
def distribution_model(im_model, z):
    return qz

# Calcul de la distribution de la cible par rapport a Z, centree en y
def distribution_cible(im_target, y, z):
    # TODO : calculer la distribution par rapport a z en y    
    return pz_y

# Coefficient de Bhattacharyya
# @param : pz, qz, 2 histogrammes de même taille
# @return : b, valeur du coeffcient de Bhattacharyya
def b_coeff (pz,qz):
    # pz & qz : 2 histogrammes a comparer
    p,q = np.matrix(pz),np.matrix(qz)
    assert(p.shape == q.shape)
    b = (np.sqrt(p,q)).sum()
    return b
    

# Distance entre 2 histogrammes
# Calcul via leur coeff de Bhattacharyya
def distance (coeff_bhatta)
    return sqrt(1 - coeff_bhatta)
    

    
    
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_kernel():
    # TEST KERNEL NORMAL
    im = np.matrix(range(0,10000))
    plt.subplot(221)
    plt.plot(im.A1)
    im_n = kernel( np.multiply(im-5000,im-5000)/1000000.)
    plt.subplot(222)
    plt.plot(im_n.A1)
    # TEST KERNEL EPANECHNIKOV
    im_bis = np.matrix(range(0,1000)).astype(float)
    im_bis -= 500
    im_bis /= 250.
    plt.subplot(223)
    plt.plot(im_bis.A1)
    im_n = kernel( im_bis, normal=0)
    plt.subplot(224)
    plt.plot(im_n.A1)
    plt.show()    
    
if __name__ == "__main__":
    test_kernel()