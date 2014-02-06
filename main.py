#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np
import histogram.util as h

#import histo

im=util.imread('./resource/einstein.jpg')
hist,bins = h.histo(im)
h.plotHist(im)

print(" I WON HAHA")