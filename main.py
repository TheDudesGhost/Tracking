#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena

import numpy as np
import random as rand
import matplotlib.pyplot as plt

import mean_shift.func as ms
import mean_shift.base.kernel as bk
import mean_shift.base.histogram as bh

#import geometry


def test_mean_shift ():
    im = util.lena()    
        
    roiX,roiY,raw = geo.roi_cercle(im,250,250,5)
    ker = bk.kernel_centre(im,250,250)
    roi_ker = geo.roi_cercle(ker,250,250,5)[2]
    histo1,bins1 = bh.histo(raw,weights=roi_ker)
    histo2,bins2 = bh.histo_roi_cercle(im,ker,250,250,5)
    
    print histo2
    print histo1    
    
    plt.subplot(311)
    plt.plot(histo1)
    plt.subplot(312)
    plt.plot(histo2)
    plt.subplot(313)
    plt.plot(histo1 - histo2)
    
    plt.show()
    return 0
    
#test_mean_shift()

im = util.imread('./resource/me.jpg')  
histo,bins = np.histogram(im,bins=32)
plt.plot(histo)
plt.show()

print histo,bins









#######################################################
####################    TEST    ####################### 
#######################################################


#ms.b_coeff



