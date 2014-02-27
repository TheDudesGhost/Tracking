#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena

import numpy as np
import random as rand
import matplotlib.pyplot as plt

import mean_shift.func as ms
import mean_shift.base.kernel as bk
import mean_shift.base.histogram as bh

import geometry as geo
import video as v

video = v.Video('./resource/Juggling.mp4')
while(video.isOpened()):
    ret, im = video.getFrame()
    if not ret:
        break
    video.display_roi(im)
    video.display(im)
    # TODO Make computation
    if v.is_radius_nonzero(video.getSelection()):
        i,j,r = video.getSelection()
        roi = geo.region.roi_cercle(im[:,:,0],i,j,r)   
        q,bins = ms.distribution_RGB(video.getPrevious(),i,j,roi)
        i,j = ms.prediction_RGB(im,i,j,r,q)
        print i,j
        video.setSelection(i,j,r)
    # TODO Uncomment when computation is done
    # video.setSelection(i, j, r)        
    video.setPrevious(im)
    if not video.check_event(im):
        break

video.end()








#######################################################
####################    TEST    ####################### 
#######################################################


#ms.b_coeff



