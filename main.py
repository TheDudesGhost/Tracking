#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np
import random as rand
import matplotlib.pyplot as plt

import mean_shift.func as ms
import mean_shift.base.kernel as bk
import mean_shift.base.histogram as bh

import geometry as geo





#######################################################
####################    TEST    ####################### 
#######################################################

im = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
a,b = im*3,im*3
print a
print b
#ms.b_coeff



