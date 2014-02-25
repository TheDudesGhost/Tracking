#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt


def histo(dataIn, weights=None, bins=32, range_=(0,256)):
    histo, bins = np.histogram(dataIn, bins, range_, weights=weights)
    histo = histo/ histo.sum()
    return histo, bins

# Affiche un histogramme cree par numpy
def plotHist(dataIn):
    plt.hist(dataIn)
    plt.show()



# Retourne l'index du bin auquel appartient la couleur
def bin_please(couleur,bins):
    result = []

    for i,coul in enumerate(couleur):
        tmp = (bins <= coul)
        result.append(tmp.sum()-1)
    return result
    
def bin_RGB(couleur_RGB,bins):
    index_R = bin_please(couleur_RGB[0],bins)
    index_G = bin_please(couleur_RGB[1],bins)
    index_B = bin_please(couleur_RGB[2],bins)
    return [index_R, index_G, index_B]    

##############################################################################
################################      TESTS       ############################
##############################################################################
