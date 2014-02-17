#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np

import histogram.util as h
import mean_shift.func as ms

import random as rand
import matplotlib.pyplot as plt


im = np.eye(15,4)
ker = ms.kernel_centre(im,1,1)
print ker

#ms.b_coeff

