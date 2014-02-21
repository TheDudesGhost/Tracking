# -*- coding: utf-8 -*-
"""
"""

import cv2
import cv2.cv as cv
import numpy as np

from geometry import *

def is_rect_nonzero(r):
    (_,_,w,h) = r
    return (w > 0) and (h > 0)

class Video:
    
    def __init__(self, path):
        self.path = path
        cv.NamedWindow( "Demo", 1 )
        
        cv.SetMouseCallback("Demo", self.on_mouse)
        
        self.drag_start = None
        self.track_window = None
        self.selection = (0,0,0,0)
    
    def on_mouse(self, event, x, y, flags, param):
        if event == cv.CV_EVENT_LBUTTONDOWN:
            self.drag_start = (x, y)
        if event == cv.CV_EVENT_LBUTTONUP:
            self.drag_start = None
            self.track_window = self.selection
        if self.drag_start:
            xmin = min(x, self.drag_start[0])
            ymin = min(y, self.drag_start[1])
            xmax = max(x, self.drag_start[0])
            ymax = max(y, self.drag_start[1])
            self.selection = (xmin, ymin, xmax - xmin, ymax - ymin)

    def toto(self):
        # setup video capture
        cap = cv2.VideoCapture(self.path)
        
        # get frame, store in array
        while(cap.isOpened()):
            ret, im = cap.read()
            if not ret:
                break
            # The frame is in im
            
            # If mouse is pressed, highlight the current selected rectangle
            # and recompute the histogram
    
            if self.drag_start and is_rect_nonzero(self.selection):
                frame = cv.fromarray(im)
                sub = cv.GetSubRect(frame, self.selection)
                save = cv.CloneMat(sub)
                save = cv.fromarray(cv2.GaussianBlur(np.array(save), (0, 0), 5))
                cv.ConvertScale(frame, frame, 0.5)
                
                
                cv.Copy(save, sub)
                x,y,w,h = self.selection

                cv.Rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
                frame = np.array(frame)
            elif is_rect_nonzero(self.selection):
                frame = cv.fromarray(im)
                sub = cv.GetSubRect(frame, self.selection)
                save = cv.CloneMat(sub)
                save = cv.fromarray(cv2.GaussianBlur(np.array(save), (0, 0), 5))
                cv.Copy(save, sub)
                frame = np.array(frame)
            else:
                frame = im
                
            #elif self.track_window and is_rect_nonzero(self.track_window):
            #    cv.EllipseBox( frame, track_box, cv.CV_RGB(255,0,0), 3, cv.CV_AA, 0 )
    
            #make process here
            #im = cv2.GaussianBlur(im, (0, 0), 5)
    
            # Display
            cv2.imshow('Demo', frame)
            
            # Use Q to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        
        cap.release()


##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_video(path):
    video = Video(path)
    video.toto()
    #toto(0)
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    test_video('../resource/car.mp4')