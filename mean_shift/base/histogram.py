#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt


def histo(dataIn, weights=None, bins=32, range_=(0,256)):
    histo, bins = np.histogram(dataIn, bins, range_, weights=weights)
    #histo = histo/ histo.sum()
    return histo, bins

# Affiche un histogramme cree par numpy
def plotHist(dataIn):
    plt.hist(dataIn)
    plt.show()



# Retourne l'index du bin auquel appartient la couleur
def bin_please(couleur,bins):
    result = []
    for i,coul in enumerate(couleur):
        tmp = (bins <= coul)*1
        result.append(tmp.sum()-1)
    return result
    
# Version optimisee python (mais qui prend plus de temps que la precedente ...)
def bin_please_opt(couleur,bins):
    couleur = np.reshape(couleur,(len(couleur),1))
    bins = np.meshgrid(bins,np.arange(couleur.shape[0]))[0]
    lut = (bins <= couleur)*1
    lut = np.dot(lut,np.ones(lut.shape[1]))-1
    return lut
    
def bin_RGB(couleur_RGB,bins):
    #couleur_RGB = couleur_RGB.astype(float)
    index_R = bin_please(couleur_RGB[0],bins)
    index_G = bin_please(couleur_RGB[1],bins)
    index_B = bin_please(couleur_RGB[2],bins)
    return [index_R, index_G, index_B]    

##############################################################################
################################      TESTS       ############################
##############################################################################

if __name__ == "__main__":
    import time
    


    
    
