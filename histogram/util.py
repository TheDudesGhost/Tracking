#! /usr/bin/python2.7

import numpy as np

def histo(dataIn):
    histo, bins = np.histogram(dataIn, 255)
    return histo, bins

# Affiche un histogramme créé par numpy
def histOutline(histIn, binsIn):
    stepSize = binsIn[1] - binsIn[0]

    bins = np.zeros(len(binsIn)*2 + 2, dtype=np.float)
    data = np.zeros(len(binsIn)*2 + 2, dtype=np.float)
    for bb in range(len(binsIn)):
        bins[2*bb + 1] = binsIn[bb]
        bins[2*bb + 2] = binsIn[bb] + stepSize
        if bb < len(histIn):
            data[2*bb + 1] = histIn[bb]
            data[2*bb + 2] = histIn[bb]
   
    bins[0] = bins[1]
    bins[-1] = bins[-2]
    data[0] = 0
    data[-1] = 0
           
    return (bins, data)