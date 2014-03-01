#! /usr/bin/python2.7

import scipy.misc as util # imread / imsave / imresize / lena

import numpy as np
import random as rand
import matplotlib.pyplot as plt

import mean_shift.func as ms
import mean_shift.base.kernel as bk
import mean_shift.base.histogram as bh
import mean_shift.base as b

import geometry as geo
import video as v
import time

start_time = 0
etat_courant = b.Etat(0,0,0,0,0)
start = False
nb_img = 0

video = v.Video('./resource/Juggling.mp4')
#video = v.Video(0)

while(video.isOpened()):
    ret, im = video.getFrame()
    if not ret:
        break
    video.display_roi(im)
    video.display(im)
    # TODO Make computation
    if v.is_radius_nonzero(video.getSelection()) and not video.isPaused():
        if start==False : #Initialisation
            start=True
            j,i,r = video.getSelection()
            roi = geo.region.roi_cercle(im[:,:,0].shape,i,j,r)   
            ker = bk.kernel_centre(im[:,:,0].shape,i,j,normal=1,h=r)
            raw_ker = geo.rawdata(ker,roi)
            q,bins = ms.distribution_RGB(im,roi,raw_ker)
            etat_courant = b.Etat(i,j,r,raw_ker,q)
            start_time = time.time()
        
        j,i,r = video.getSelection()
        etat_courant.setSelection(i,j,r)
        i,j = ms.prediction_RGB(im,etat_courant)
        video.setSelection(j,i,r)
        nb_img = nb_img + 1

    # TODO Uncomment when computation is done       
    if not video.check_event(im):
        break

video.end()
end_time = time.time()


print "FPS = ",nb_img /(end_time - start_time)









#######################################################
####################    TEST    ####################### 
#######################################################


#ms.b_coeff



