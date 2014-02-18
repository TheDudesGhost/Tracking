#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np
import random as rand
import matplotlib.pyplot as plt

import histogram.util as h
import mean_shift.func as ms
import mean_shift.base.kernel as ker
import mean_shift.base.histogram as his





#######################################################
####################    TEST    ####################### 
#######################################################

X,Y = np.meshgrid(np.arange(0,50), np.arange(0,50))
im  = X
ker = ker.kernel_centre(im,25,25)
histo = h.histo_roi_quad(X,ker,25,25,5,5)
print histo
plt.plot(im)
plt.show()
#ms.b_coeff



