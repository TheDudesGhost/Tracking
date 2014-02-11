#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np

import histogram.util as h
import mean_shift.func as ms

import random as rand
import matplotlib.pyplot as plt


im = np.matrix(range(0,99))
im_n = ms.kernel(im)

