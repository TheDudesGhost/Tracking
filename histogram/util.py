#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt


def histo(dataIn, weights=None, bins=255, range_=(1,256)):
    if weights is None:    
        histo, bins = np.histogram(dataIn, bins, range_)
    else :
        histo, bins = np.histogram(dataIn, bins, range_, weights=weights)
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
    histo_roi = histo(im, weights=weights_roi)
    return histo_roi
    
# Extract circular roi from image
def roi_circle(im,cx,cy,r):
    H,W = im.shape    
    assert(cx+r <= W-1 and cx-r >= 0)
    assert(cy+r <= H-1 and cy-r >= 0)
    X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))    
    roi = (im+1) * (((X-cx)**2 + (Y-cy)**2) <= (r**2 + 1))    
    # Get the raw data    
    rawData = filter(lambda a: a != 0, roi.flatten())
    rawData = np.matrix(list(set(rawData) - set([1]*len(rawData))))
    roi -= 1*(roi>0)
    return roi,rawData
    

def roi_quad(im,cx,cy,h,w):
    H,W = im.shape    
    assert(cx+w <= W-1 and cx-w >= 0)
    assert(cy+h <= H-1 and cy-h >= 0)
    roi = im[cx-h/2:cx+h/2 , cy-w/2:cy+w/2]
    rawData = roi.flatten()
    return roi,rawData




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