#! import /usr/bin/python2.7

"""
Geometry - func
Contient les fonctions de masque utilisant les ROI contenues dans le package roi
"""

import numpy as np

# Renvoie 2 vecteurs contenant les coordonnees des points de l'image
# appartenant a la roi
def roi(im,roi):
    H,W = im.shape
    J,I = np.meshgrid(np.arange(0,W),np.arange(0,H))    
    
    roiI,roiJ = (I+1)*roi, (J+1)*roi
    roiI,roiJ = roiI.flatten(), roiJ.flatten()   
    roiI = roiI[roiI != 0] -1
    roiJ = roiJ[roiJ != 0] -1
    return roiI,roiJ
    
# Renvoie les valeurs des points appartenant a& la roi
def rawdata(im,roi):
    rawdata = (im+1)*roi
    rawdata = rawdata.flatten()
    rawdata = rawdata[rawdata != 0] -1
    return rawdata
    

if __name__ == "__main__":
    import region
    import scipy.misc as util
    import matplotlib.pyplot as plt
    im=util.lena()
    roi_test = region.roi_cercle(im,250,250,30)
    roiI,roiJ = roi(im,roi_test)
    plt.imshow(roiI)
    plt.show()
    