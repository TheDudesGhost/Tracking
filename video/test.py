# -*- coding: utf-8 -*-
"""
"""

import cv2
import cv2.cv as cv
import numpy as np

from math import sqrt

def is_radius_nonzero(r):
    (_,_,radius) = r
    return (radius > 0)

def distance(a, b):
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

class Video:
    
    def __init__(self, path):
        self.path = path
        cv2.namedWindow( "Demo", 1 )
        
        cv.SetMouseCallback("Demo", self.on_mouse)
        
        self.drag_start = None
        self.track_window = None
        self.selection = (0,0,0)
    
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

    def process(self):
        # setup video capture
        cap = cv2.VideoCapture(self.path)
        
        pause = False
        tmp = None
        
        # get frame, store in array
        while(cap.isOpened()):
            if not pause:
                ret, im = cap.read()
                if not ret:
                    break
            else:
                im = np.array(tmp)
                print "pause"
            # The frame is in im
            
            # If mouse is pressed, highlight the current selected rectangle
            # and recompute the histogram
    
            if self.drag_start and is_radius_nonzero(self.selection):
                # On est en train de sélectionner la zone                
                
                #frame = cv.fromarray(im) # Convertit des données np en cv
                #sub = cv.GetSubRect(frame, self.selection)
                #save = cv.CloneMat(sub)
                #save = cv.fromarray(cv2.GaussianBlur(np.array(save), (0, 0), 5))
                #cv.ConvertScale(frame, frame, 0.5)
                
                #cv.Copy(save, sub)
                x,y,radius = self.selection

                cv2.circle(im, (x,y), int(radius), (255,255,255))
            elif is_radius_nonzero(self.selection):
                # Ici la sélection est faite

                x,y,radius = self.selection

                cv2.circle(im, (x,y), int(radius), (255,255,255))                
            else:
                # Rien n'a jamais été selectionné
                None

            #elif self.track_window and is_rect_nonzero(self.track_window):
            #    cv.EllipseBox( frame, track_box, cv.CV_RGB(255,0,0), 3, cv.CV_AA, 0 )
    
            #make process here
            #im = cv2.GaussianBlur(im, (0, 0), 5)
    
            # Display
            cv2.imshow('Demo', im)

            key = cv2.waitKey(25) & 0xFF          
            
            # Use Q to quit
            if key == ord('q'):
                break
            if key == ord(' '):
                pause = not pause
                if pause:
                    tmp = im 
        
        cap.release()


##############################################################################
################################      TESTS       ############################
##############################################################################    
    
def test_video(path):
    video = Video(path)
    video.process()
    #toto(0)
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    test_video('../resource/car.mp4')