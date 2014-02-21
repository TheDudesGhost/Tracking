#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt


def histo(dataIn, weights=None, bins=256, range_=(0,256)):
    assert(dataIn is not None)
    histo, bins = np.histogram(dataIn, bins, range_, weights=weights, density=True)
    return histo, bins

# Affiche un histogramme cree par numpy
def plotHist(dataIn):
    plt.hist(dataIn)
    plt.show()


# Histogramme d'une ROI en forme de cercle
def histo_roi_cercle(im,weights,cx,cy,r):
    H,W = im.shape    
    assert(cx+r <= W-1 and cx-r >= 0)
    assert(cy+r <= H-1 and cy-r >= 0)
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))    
    weights_roi = weights * (((X-cx)**2 + (Y-cy)**2) <= (r**2 + 1))    
    histo_roi,bins = histo(im, weights=weights_roi)
    return histo_roi,bins
    
    

def histo_roi_quad(im,weights,cx,cy,h,w):
    H,W = im.shape    
    assert(cx+w <= W-1 and cx-w >= 0)
    assert(cy+h <= H-1 and cy-h >= 0)
    roi = im[cx-h/2:cx+h/2 , cy-w/2:cy+w/2]
    histo_roi,bins = histo(roi, weights=weights)
    return histo_roi,bins


# Retourne l'index du bin auquel appartiemt la couleur
def bin_please(couleur,bins):
    tmp = (bins <= couleur)
    return tmp.sum()-1

##############################################################################
################################      TESTS       ############################
##############################################################################


def test_roi(circle=1):
    from scipy.misc import lena
    im = lena().astype(float)
    if circle==1 :    
        hroi = histo_roi_cercle(im, 250,250,100)
    else :
        roi,raw = roi_quad(im, 250,250,50,100)    
    plt.subplot(211)    
    plt.imshow(im, cmap='Greys')
    plt.subplot(212)
    plt.imshow(roi, cmap='Greys')    
    plt.show()
    print raw.shape

if __name__ == "__main__":
    test_roi(1)