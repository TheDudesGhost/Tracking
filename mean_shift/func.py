#! /usr/bin/python2.7

"""
Mean shift - func
Contient les fonctions calculant les fonctions mathematiques
requises pour le calcul de la mean shift
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np

import kernel as ker



# Histogramme pondere du modele par le kernel choisi
# Kernel normal choisi par defaut
def distribution_model(im_model, k=1):
    H,W = im.shape    
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))    
    
    if k==1:
        ker = ker.kernel()    
    return q

# Calcul de la distribution de la cible par rapport a Z, centree en y
def distribution_cible(hist_target, y):
    # TODO : calculer la distribution par rapport a z en y    
    return p_y

# Coefficient de Bhattacharyya
# @param : pz, qz, 2 histogrammes de meme taille
# @return : b, valeur du coeffcient de Bhattacharyya
def b_coeff (pz,qz):
    # pz & qz : 2 histogrammes a comparer
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
    
def test_kernel():
    print('Bonjour')
    print ker.kernel(1)
    
if __name__ == "__main__":
    test_kernel()