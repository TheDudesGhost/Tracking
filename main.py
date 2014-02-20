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

im = np.arange(1,10,0.2)
hist,bins = np.histogram(im,3,(0,10))

print im
print hist
print bins

b=bh.bin_please(4.5,bins)
print hist[b]
print b
#ms.b_coeff



