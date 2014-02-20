# -*- coding: utf-8 -*-
"""
"""

import cv2
import numpy as np

def toto(path):
    # setup video capture
    cap = cv2.VideoCapture(path)

    # get frame, store in array
    while True:
        ret, im = cap.read()
        # The frame is in im
        
        #make process here
        
        # Display
        cv2.imshow('video test', im)
        
        #todo fix quit key 
        key = cv2.waitKey(10)
        print key       
        print ord('q')
        
        if key == ord('q'):
            break


##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_video():
    toto(0)
    
if __name__ == "__main__":
    test_video()