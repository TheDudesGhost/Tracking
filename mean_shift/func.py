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


# Histogramme pondere du modele par le kernel choisi
def distribution(im,cx,cy,r):
    ker = bk.kernel_centre(im,cx,cy)
    histo = bh.histo_roi_cercle(im,ker,cx,cy,r)
    return histo


# Coefficient de Bhattacharyya
# @param : p, q, 2 histogrammes de meme taille
# @return : b, valeur du coeffcient de Bhattacharyya
def b_coeff (pz,qz):
    p,q = np.matrix(pz),np.matrix(qz)
    assert(p.shape == q.shape)
    b = (np.sqrt(np.multiply(p,q))).sum()
    return b
    

# Distance entre 2 histogrammes
# Calcul via leur coeff de Bhattacharyya
def distance (coeff_bhatta):
    return sqrt(1 - coeff_bhatta)
    

    
    
##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_distrib():
    im = scipy.misc.lena()
    h1 = distribution(im,250,250,20)
    h2 = distribution(im,252,252,20)
    h3 = distribution(im,100,100,20)
    
    b12 = b_coeff(h1,h1)
    b13 = b_coeff(h1,h3)
    
    print b12, distance(b12)
    print b13, distance(b13)
    
if __name__ == "__main__":
    test_distrib()