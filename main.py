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
    if v.is_radius_nonzero(video.selection):
        i,j,r = video.selection
        
        posI,posJ = 45,50
        oldI,oldJ = 50,50
        roi = geo.region.roi_cercle(im[:,:,0],oldI,oldJ,radius)   
        q,bins = distribution_RGB(im,oldI,oldJ,roi)
        posI,posJ = prediction_RGB(im,posI,posJ,radius,q)
        prediction_RGB(im, im,i,j,r,i,j)
    # TODO Uncomment when computation is done
    # video.setSelection(i, j, r)        
    
    if not video.check_event(im):
        break

video.end()








#######################################################
####################    TEST    ####################### 
#######################################################


#ms.b_coeff



