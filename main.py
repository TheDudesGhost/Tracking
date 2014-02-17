#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np

import histogram.util as h
import mean_shift.func as ms

import random as rand
import matplotlib.pyplot as plt


X,Y = np.meshgrid(np.arange(0,255), np.arange(0,255))
im  = (X+Y)/2*((X-122)**2 + (Y-122)**2 <= 10)
ker = ms.kernel_centre(im,122,122)

histo = h.histo_roi_cercle(X,ker,122,122,10)


#ms.b_coeff

