#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena
import numpy as np

import histogram.util as h
import mean_shift.func as ms

import random as rand
import matplotlib.pyplot as plt

# TEST KERNEL NORMAL
im = np.matrix(range(0,10000))

plt.subplot(221)
plt.plot(im.A1)
im_n = ms.kernel( np.multiply(im-5000,im-5000)/1000000.)
plt.subplot(222)
plt.plot(im_n.A1)

# TEST KERNEL EPANECHNIKOV
im_bis = np.matrix(range(0,1000)).astype(float)
im_bis -= 500
im_bis /= 250.

plt.subplot(223)
plt.plot(im_bis.A1)
im_n = ms.kernel( im_bis, normal=0)
plt.subplot(224)
plt.plot(im_n.A1)


plt.show()

