#! /usr/bin/python2.7

"""
Mean shift - func
Contient les fonctions calculant les fonctions mathematiques
requises pour le calcul de la mean shift
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc as util
import base.kernel as bk          
import base.histogram as bh
import base

import scipy.ndimage as ndimage

#radius = 30


# Histogramme pondere du modele par le kernel choisi
def distribution(im,roi,raw_ker):
    rawdata = geo.rawdata(im,roi)
    histo,bins = bh.histo(rawdata,weights=raw_ker)   
    return histo,bins

# Test OK
def distribution_RGB(im_rgb,roi,raw_ker):
    im_rgb = im_rgb.astype(float)   
    histo_R, bins = distribution(im_rgb[:,:,0],roi,raw_ker) 
    histo_G, bins = distribution(im_rgb[:,:,1],roi,raw_ker)
    histo_B, bins = distribution(im_rgb[:,:,2],roi,raw_ker)
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
    return wR+wG+wB#np.multiply(np.multiply(wR,wG),wB)#
    


#Prediction du nouvel emplacement de y
def prediction (im,posI,posJ):
    #Distribution
    roi = geo.region.roi_cercle(im,posI,posJ,radius)
    p,binsP = distribution(im,posI,posJ,roi)
    roi_origine = geo.region.roi_cercle(im,50,50,radius)
    q,binsQ = distribution(im,50,50,roi_origine)  
    # Weights
    roiI,roiJ = geo.roi(im,roi)
    rawdata = geo.rawdata(im,roi)
    h = roiI.shape[0]
    weight = weights(p,q,bh.bin_please(rawdata,binsP))
    #Calcul sur les X
    newI = (np.multiply(np.multiply(roiI,weight),bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum()
    newJ = (np.multiply(np.multiply(roiJ,weight),bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum()
    return newI,newJ



def prediction_RGB(im, etat_courant):
    # Initialisation
    posI,posJ,radius = etat_courant.getSelection()
    raw_ker = etat_courant.getKernel()
    q = etat_courant.getModel()
    # Distribution (histogramme) & Bhattacharyya
    im = im.astype(float)
    roi = geo.region.roi_cercle(im[:,:,0].shape,posI,posJ,radius)
    p,bins = distribution_RGB(im,roi,raw_ker)
    old_coeff = b_coeff_RGB(p,q)    
    # Weights im = im.astype(float)
    roiI,roiJ = geo.roi(im[:,:,0].shape,roi)
    rawR = geo.rawdata(im[:,:,0],roi) # roiI -> colonnes
    rawG = geo.rawdata(im[:,:,1],roi)
    rawB = geo.rawdata(im[:,:,2],roi)
    #h = roiI.shape[0]
    weight = weights_RGB(p,q,bh.bin_RGB([rawR,rawG,rawB],bins))
    # Update Y1
    temp_I = np.multiply(raw_ker,weight) #temp_I = weight #
    temp_J = np.multiply(raw_ker,weight) #temp_J = weight #
    newI = (np.multiply(temp_I,roiI)).sum() / temp_I.sum()
    newJ = (np.multiply(temp_J,roiJ)).sum() / temp_J.sum()    
    newI, newJ = int(newI), int(newJ)    
    # Test Bhattacharrya
    roi = geo.region.roi_cercle(im[:,:,0].shape,newI,newJ,radius)
    p,bins = distribution_RGB(im,roi,raw_ker)
    new_coeff = b_coeff_RGB(p,q)
    while new_coeff < old_coeff and ((newI-posI)**2 + (newJ-posJ)**2)>2:
        newI, newJ = int(0.5*(newI+posI)), int(0.5*(newJ+posJ))
        roi = geo.region.roi_cercle(im[:,:,0].shape,newI,newJ,radius)
        p,bins = distribution_RGB(im,roi,raw_ker)
        new_coeff = b_coeff_RGB(p,q)
    
#    plt.subplot(241)
#    plt.plot(p[0])
#    plt.title('target - R')
#    plt.subplot(242)
#    plt.plot(p[1])
#    plt.title('target - G')
#    plt.subplot(243)
#    plt.plot(p[2])
#    plt.title('target - B')
#    plt.subplot(244)
#    plt.plot(old_coeff)
#    plt.title('Old Bhattacharyya')
#    plt.subplot(245)
#    plt.plot(q[0])
#    plt.title('modele - R')
#    plt.subplot(246)
#    plt.plot(q[1])
#    plt.title('modele - G')
#    plt.subplot(247)
#    plt.plot(q[2])
#    plt.title('modele - B')
#    plt.subplot(248)
#    plt.plot(new_coeff)
#    plt.title('New Bhattacharyya')
#    plt.show()
    return newI,newJ
    
    
  
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_algo():
    ker = bk.kernel_centre((100,100),50,80,10)
    plt.imshow(ker)
    plt.show()
    
    
if __name__ == "__main__":
    import sys
    import os.path
    sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))    
    import geometry as geo    
    
    test_algo()

    
    

else :
    import geometry as geo
    
    
    
    
    
    
    