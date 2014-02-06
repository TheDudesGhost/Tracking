#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt

def histo(dataIn):
    histo, bins = np.histogram(dataIn, 255)
    return histo, bins

# Affiche un histogramme cree par numpy
def plotHist(dataIn):
    plt.hist(dataIn)
    plt.show()