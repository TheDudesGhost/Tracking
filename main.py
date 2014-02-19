#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np
import random as rand
import matplotlib.pyplot as plt

import mean_shift.func as ms
import mean_shift.base.kernel as bk
import mean_shift.base.histogram as bh





#######################################################
####################    TEST    ####################### 
#######################################################

im = np.matrix([0])
print im
hist,bins = bh.histo(im,bins=32)
print hist
print bins
#ms.b_coeff



