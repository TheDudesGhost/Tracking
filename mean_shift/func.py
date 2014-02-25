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

radius = 20


# Histogramme pondere du modele par le kernel choisi
def distribution(im,cx,cy,raw_ker):
    rawdata = geo.roi_cercle(im,cx,cy,radius, raw=1)[2]
    print rawdata.shape,raw_ker.shape
    histo,bins = bh.histo(rawdata,weights=raw_ker)   
    return histo,bins

# Test OK
def distribution_RGB(im_rgb,cx,cy):
    # Calcul du kernel
    ker = bk.kernel_centre(im_rgb[:,:,0],cx,cy)
    
    raw_ker = geo.roi_cercle(ker,cx,cy,radius, raw=1)[2]
    # Calcul des distributions    
    histo_R, bins = distribution(im_rgb[:,:,0],cx,cy,raw_ker) 
    histo_G, bins = distribution(im_rgb[:,:,1],cx,cy,raw_ker)
    histo_B, bins = distribution(im_rgb[:,:,2],cx,cy,raw_ker)
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
def prediction (im,posX,posY):
    p,binsP = distribution(im,posX,posY)
    q,binsQ = distribution(im,200,320)    
    roiX,roiY,rawdata = geo.roi_cercle(im,posX,posY,radius)
    h = roiX.shape[0]
    weight = weights(p,q,bh.bin_please(rawdata,binsP))
    #Calcul sur les X
    newX = (np.multiply(np.multiply(roiX,weight),bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum()
    newY = (np.multiply(np.multiply(roiY,weight),bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum()
    return newX,newY

    
def prediction_RGB(im, model, posX, posY):
    oldX,oldY = posX,posY
    # Distributions (histogrammes) & Bhattacharyya 
    p,bins = distribution_RGB(im,posX,posY)
    q,bins = distribution_RGB(model,374,456)
    old_coeff = b_coeff_RGB(p,q)    
    # Weights
    roiX,roiY,rawR = geo.roi_cercle(im[:,:,0],posX,posY,radius) # roiX -> colonnes
    rawG = geo.roi_cercle(im[:,:,0],posX,posY,radius,raw=1)[2]
    rawB = geo.roi_cercle(im[:,:,0],posX,posY,radius,raw=1)[2]
    h = roiX.shape[0]
    weight = weights(p,q,bh.bin_RGB([rawR,rawG,rawB],bins))
    # Update Y1
    newX = (np.multiply(np.multiply(roiX,weight),bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posX-roiX)/h,(posX-roiX)/h)))).sum()
    newY = (np.multiply(np.multiply(roiY,weight),bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum() / (np.multiply(weight,bk.kernel(np.multiply((posY-roiY)/h,(posY-roiY)/h)))).sum()
    newX, newY = int(newX), int(newY)    
    # Test
    p,bins = distribution_RGB(im,newX,newY)
    new_coeff = b_coeff_RGB(p,q)
    while new_coeff < old_coeff and ((newX-oldX)**2 + (newY-oldY)**2)>3:
        newX, newY = int(0.5*(newX+oldX)), int(0.5*(newY+oldY))
        p,bins = distribution_RGB(im,newX,newY)
        new_coeff = b_coeff_RGB(p,q)
    
    return newX,newY
    

    
    plt.show()
    
  
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_algo():
    im = ndimage.imread('../resource/me.jpg')
    test = im[:,:,0] *0   
    q,bins = distribution_RGB(im,374,456)
    
    for i in range(370,380):
        for j in range(450,460):
            print i,j
            p,bins = distribution_RGB(im,i,j)
            test[i,j] = b_coeff_RGB (p,q)
    
    plt.imshow(test)
    plt.show()

    
if __name__ == "__main__":
    import sys
    import os.path
    sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))    
    import geometry as geo    
    
    test_algo()
#    im = ndimage.imread('../resource/me.jpg')
#    x,y = 380,452
#    for i in range(30):    
#        x,y = prediction_RGB(im,im,x,y)
#        print x,y
    
    

else :
    import geometry as geo
    
    
    
    
    
    
    