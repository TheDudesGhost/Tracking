#! /usr/bin/python2.7

"""
Mean shift - func
Contient les fonctions calculant les fonctions mathematiques
requises pour le calcul de la mean shift
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc

import base.kernel as bk          
import base.histogram as bh

import scipy.ndimage as ndimage




# Histogramme pondere du modele par le kernel choisi
def distribution(im,cx,cy,roi):
    radius = 20
    roi_im = geo.roi_cercle(im,cx,cy,radius)[2]
    ker = bk.kernel_centre(im,cx,cy)
    roi_ker = geo.roi_cercle(ker,cx,cy,radius)[2]
    histo,bins = bh.histo(roi_im,weights=roi_ker)   
    return histo,bins


# Coefficient de Bhattacharyya
# @param : p, q, 2 histogrammes de meme taille
# @return : b, valeur du coeffcient de Bhattacharyya
def b_coeff (pz,qz):
    pz,qz = np.array(pz),np.array(qz)
    assert(pz.shape == qz.shape)
    b = (np.sqrt(np.multiply(pz,qz))).sum()
    return b
    

# Distance entre 2 histogrammes
# Calcul via leur coeff de Bhattacharyya
def distance (coeff_bhatta):
    return sqrt(1 - coeff_bhatta)
    

# Coefficients utilises dans le mean shift
# p et q : les 2 distributions (cible, modele)
# index = bh.bin_please ...
def weights (p,q,index):
    p = p.astype(float)
    p = np.array(p) + 0.000001
    q = np.array(q) + 0.000001
    return np.sqrt(np.take(q,index)/np.take(p,index))


#Prediction du nouvel emplacement de y
def prediction (im,posX,posY):
    radius = 20
    p,binsP = distribution(im,posX,posY,radius)
    q,binsQ = distribution(im,200,320,radius)    
    roiX,roiY,rawdata = geo.roi_cercle(im,posX,posY,radius)
    h = roiX.shape[0]
    weight = weights(p,q,bh.bin_please(rawdata,binsP))
    #Calcul sur les X
    newX = (np.multiply(np.multiply(roiX,weight),bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum()
    newY = (np.multiply(np.multiply(roiY,weight),bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum()
    return newX,newY

    
    
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_algo():
    im = ndimage.imread('../2.pgm')

    print prediction(im,200,320)
    
if __name__ == "__main__":
    import sys
    import os.path
    sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))    
    import geometry as geo    
    
    test_algo()
    
    

else :
    import geometry as geo
    
    
    
    
    
    
    