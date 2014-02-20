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

im = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
H,W = im.shape
X,Y = np.meshgrid(np.arange(0,W),np.arange(0,H))
print ''
#ms.b_coeff



