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

import scipy.ndimage as ndimage

#radius = 30


# Histogramme pondere du modele par le kernel choisi
def distribution(im,ci,cj,roi):
    rawdata = geo.rawdata(im,roi)
    ker = bk.kernel_centre(im,ci,cj)
    raw_ker = geo.rawdata(ker,roi)
    histo,bins = bh.histo(rawdata,weights=raw_ker)   
    return histo,bins

# Test OK
def distribution_RGB(im_rgb,ci,cj,roi):
    im_rgb = im_rgb.astype(float)
    # Calcul des distributions    
    histo_R, bins = distribution(im_rgb[:,:,0],ci,cj,roi) 
    histo_G, bins = distribution(im_rgb[:,:,1],ci,cj,roi)
    histo_B, bins = distribution(im_rgb[:,:,2],ci,cj,roi)
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
    return np.multiply(np.multiply(wR,wG),wB)#wR+wG+wB
    


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

    
def prediction_RGB(im, posI, posJ,radius,q):
    oldI,oldJ = posI,posJ
    
    # Distributions (histogrammes) & Bhattacharyya 
    roi = geo.region.roi_cercle(im[:,:,0],posI,posJ,radius)
    p,bins = distribution_RGB(im,posI,posJ,roi)
    old_coeff = b_coeff_RGB(p,q)    
    # Weights
    im = im.astype(float)
    roiI,roiJ = geo.roi(im[:,:,0],roi)
    rawR = geo.rawdata(im[:,:,0],roi) # roiI -> colonnes
    rawG = geo.rawdata(im[:,:,1],roi)
    rawB = geo.rawdata(im[:,:,2],roi)
    h = roiI.shape[0]
    weight = weights_RGB(p,q,bh.bin_RGB([rawR,rawG,rawB],bins))
    # Update Y1
    newI = (np.multiply(np.multiply(roiI,weight),bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posI-roiI)/h,(posI-roiI)/h)))).sum()
    newJ = (np.multiply(np.multiply(roiJ,weight),bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posJ-roiJ)/h,(posJ-roiJ)/h)))).sum()
    newI, newJ = int(newI), int(newJ)    
    # Test
    roi = geo.region.roi_cercle(im[:,:,0],newI,newJ,radius)
    p,bins = distribution_RGB(im,newI,newJ,roi)
    new_coeff = b_coeff_RGB(p,q)
    while new_coeff < old_coeff and ((newI-oldI)**2 + (newJ-oldJ)**2)>2:
        newI, newJ = int(0.5*(newI+oldI)), int(0.5*(newJ+oldJ))
        p,bins = distribution_RGB(im,newI,newJ,roi)
        new_coeff = b_coeff_RGB(p,q)
    
    return newI,newJ
    

    
    plt.show()
    
  
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_algo():
    a = np.array(np.arange(0,256))
    p,bins = np.histogram(a,256,(0,256))
    print p
    index = bh.bin_RGB([a,a,a],bins)
    print index[1]
#    radius = 100   
#    im = util.imread('../resource/me.jpg')
#    im=im.astype(float)
#    posI,posJ = 300,300
#    oldI,oldJ = 301,300
#    roi = geo.region.roi_cercle(im[:,:,0],oldI,oldJ,radius)   
#    q,bins = distribution_RGB(im,oldI,oldJ,roi)
#    p,bins = distribution_RGB(im,posI,posJ,roi)
#    
#    plt.subplot(611)
#    plt.plot(p[0])
#    plt.subplot(612)
#    plt.plot(q[0])
#    plt.subplot(613)
#    plt.plot(p[1])
#    plt.subplot(614)
#    plt.plot(q[1])
#    plt.subplot(615)
#    plt.plot(p[2])
#    plt.subplot(616)
#    plt.plot(q[2])
#    plt.show()
    
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
    
    
    
    
    
    
    