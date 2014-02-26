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
from pylab import *
import base.kernel as bk          
import base.histogram as bh

import scipy.ndimage as ndimage

radius = 20


# Histogramme pondere du modele par le kernel choisi
def distribution(im,ci,cj,raw_ker):
    rawdata = geo.roi_cercle(im,ci,cj,radius, raw=1)[2]
    histo,bins = bh.histo(rawdata,weights=raw_ker)   
    return histo,bins

# Test OK
def distribution_RGB(im_rgb,ci,cj):
    # Calcul du kernel
    ker = bk.kernel_centre(im_rgb[:,:,0],ci,cj)
    
    raw_ker = geo.roi_cercle(ker,ci,cj,radius, raw=1)[2]
    # Calcul des distributions    
    histo_R, bins = distribution(im_rgb[:,:,0],ci,cj,raw_ker) 
    histo_G, bins = distribution(im_rgb[:,:,1],ci,cj,raw_ker)
    histo_B, bins = distribution(im_rgb[:,:,2],ci,cj,raw_ker)
    return [histo_R,histo_G,histo_B], bins

# Coefficient de Bhattacharyya
# @param : p, q, 2 histogrammes de meme taille
# @return : b, valeur du coeffcient de Bhattacharyya
def b_coeff (pz,qz):
    pz,qz = np.array(pz),np.array(qz)
    b = (np.sqrt(np.multiply(pz,qz))).sum()
    return b

def b_coeff_RGB (p,q):
    bR = b_coeff(p[0],q[0])
    bG = b_coeff(p[1],q[1])
    bB = b_coeff(p[2],q[2])
    b = (bR + bG + bB)/3.0
    return b    

# Distance entre 2 histogrammes
# Calcul via leur coeff de Bhattacharyya
def distance (coeff_bhatta):
    return sqrt(1 - coeff_bhatta)
    

# Coefficients utilises dans le mean shift
# p et q : les 2 distributions (cible, modele)
# index = bh.bin_please ...
def weights (p,q,index):
    p = (np.array(p)).astype(float) + 0.00000001
    q = np.array(q) + 0.00000001
    return np.sqrt(np.take(q,index)/np.take(p,index))
    
# index = bh.bin_RGB ...
def weights_RGB (p,q,index):
    wR = weights(p[0],q[0],index[0])
    wG = weights(p[1],q[1],index[1])
    wB = weights(p[2],q[2],index[2])
    return np.multiply(np.multiply(wR,wG),wB)
    


#Prediction du nouvel emplacement de y
def prediction (im,posI,posJ):
    p,binsP = distribution(im,posI,posJ)
    q,binsQ = distribution(im,200,320)    
    roiI,roiJ,rawdata = geo.roi_cercle(im,posI,posJ,radius)
    h = roiI.shape[0]
    weight = weights(p,q,bh.bin_please(rawdata,binsP))
    #Calcul sur les X
    newI = (np.multiply(np.multiply(roiI,weight),bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum()
    newJ = (np.multiply(np.multiply(roiJ,weight),bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum()
    return newI,newJ

    
def prediction_RGB(im, model, posI, posJ):
    oldI,oldJ = posI,posJ
    # Distributions (histogrammes) & Bhattacharyya 
    p,bins = distribution_RGB(im,posI,posJ)
    q,bins = distribution_RGB(model,374,456)
    old_coeff = b_coeff_RGB(p,q)    
    # Weights
    roiI,roiJ,rawR = geo.roi_cercle(im[:,:,0],posI,posJ,radius) # roiI -> colonnes
    rawG = geo.roi_cercle(im[:,:,0],posI,posJ,radius,raw=1)[2]
    rawB = geo.roi_cercle(im[:,:,0],posI,posJ,radius,raw=1)[2]
    h = roiI.shape[0]
    weight = weights(p,q,bh.bin_RGB([rawR,rawG,rawB],bins))
    # Update Y1
    newI = (np.multiply(np.multiply(roiI,weight),bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum()
    newJ = (np.multiply(np.multiply(roiJ,weight),bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum()
    newI, newJ = int(newI), int(newJ)    
    # Test
    p,bins = distribution_RGB(im,newI,newJ)
    new_coeff = b_coeff_RGB(p,q)
    while new_coeff < old_coeff and ((newI-oldI)**2 + (newJ-oldJ)**2)>3:
        newI, newJ = int(0.5*(newI+oldI)), int(0.5*(newJ+oldJ))
        p,bins = distribution_RGB(im,newI,newJ)
        new_coeff = b_coeff_RGB(p,q)
    
    return newI,newJ
    

    
    plt.show()
    
  
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_algo():
    J,I = np.meshgrid(np.arange(-50,51),np.arange(-50,51))
    J,I = 100-np.abs(J),100-np.abs(I)
    im = np.multiply(I,J)
      
    plt.imshow(im)
    plt.show()

    
if __name__ == "__main__":
    import sys
    import os.path
    sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))    
    import geometry as geo    
    
    test_algo()
#    im = ndimage.imread('../resource/me.jpg')
#    i,j = 480,370    
#    i,j = prediction_RGB(im,im,i,j)
#    print i,j
    
    

else :
    import geometry as geo
    
    
    
    
    
    
    