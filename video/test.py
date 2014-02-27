# -*- coding: utf-8 -*-
"""
"""

import cv2
import cv2.cv as cv
import numpy as np

from math import sqrt

def is_radius_nonzero(selection):
    (_,_,radius) = selection
    return (radius > 0)

def distance(a, b):
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

class Video:
    
    def __init__(self, path, windowName = "Demo"):
        self.path = path
        self.wName = windowName
        cv2.namedWindow(self.wName, 1)
        
        cv.SetMouseCallback(self.wName, self.on_mouse)
        
        self.drag_start = None
        self.track_window = None
        self.selection = (0,0,0)

        self.cap = cv2.VideoCapture(self.path)
        self.pause = False
        self.tmp = None
        self.prev = None
    
    def on_mouse(self, event, x, y, flags, param):
        if event == cv.CV_EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
        if event == cv.CV_EVENT_LBUTTONUP:
            self.drag_start = None
            self.track_window = self.selection
        if self.drag_start:
            posX, posY = self.drag_start
            radius = distance(self.drag_start, (x, y))
            self.selection = (posX, posY, radius)

    def getFrame(self):
        if self.cap.isOpened():
            if not self.pause:
                return self.cap.read()
            else:
                return True, np.array(self.tmp)
    
    def display_roi(self, im):
        if is_radius_nonzero(self.selection):
                # Une zone a ete selectionnee dans le passe                
                i, j, radius = self.selection
                
                cv2.circle(im, (i, j), int(radius), (255,255,255))

    def display(self, im):
        cv2.imshow(self.wName, im)
    
    def check_event(self, im):
        key = cv2.waitKey(25) & 0xFF          
            
        # Use Q to quit
        if key == ord('q'):
            return False
        if key == ord(' '):
            self.pause = not self.pause
            if self.pause:
                self.tmp = im
        return True
    
    def isOpened(self):
        return self.cap.isOpened()
    
    def setSelection(self, i, j, r):
        self.selection = (i, j, r)
    
    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
    def getSelection(self):
        return self.selection
    
    def getPrevious(self):
        return self.prev
    
    def setPrevious(self, im):
        self.prev = im

##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_video(path):
    video = Video(path)
    while(video.isOpened()):
        ret, im = video.getFrame()
        if not ret:
            break
        video.display_roi(im)
        video.display(im)
        # TODO Make computation 
        
        # TODO Uncomment when computation is done
        # video.setSelection(i, j, r)  
        
        video.setPrev(im)
        
        if not video.check_event(im):
            break
    
    video.end()
    
if __name__ == "__main__":
    test_video('../resource/Juggling.mp4')