# -*- coding: utf-8 -*-
"""
"""

import cv2.cv as cv
import cv2
import numpy as np

def toto(path):
    # setup video capture
    cap = cv2.VideoCapture(path)
    
    print cap

    # get frame, store in array
    while(cap.isOpened()):
        ret, im = cap.read()
        # The frame is in im

        #make process here
        im = cv2.GaussianBlur(im, (0, 0), 5)

        # Display
        cv2.imshow('video test', im)
        
        # Use Q to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_video():
    toto('./car.mp4')
    #toto(0)
    
if __name__ == "__main__":
    test_video()