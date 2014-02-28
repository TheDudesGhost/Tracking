#! /usr/bin/python2.7

"""
Contient des variables faisant partie de l'etat courant du programme, telles:
selection - i,j,r (coordonnees du point central de la selection, et rayon)
q - distribution du modele
ker - noyau
"""

class Etat:
    
    def __init__(self,i,j,r,ker,ker_target,q):
        self.selection = (i,j,r)
        self.ker = ker
        self.ker_target = ker_target
        self.q = q
        
    def setSelection(self,i,j,radius):
        self.selection = (i,j,radius)
        
    def getSelection(self):
        return self.selection
        
    def setModel(self,q):
        self.q = q
        
    def getModel(self):
        return self.q
        
    def setKernel(self,raw_ker):
        self.ker = raw_ker
        
    def getKernel(self):
        return self.ker
    
    def setKernelTarget(self,raw_ker_target):
        self.ker_target = raw_ker_target
        
    def getKernelTarget(self):
        return self.ker_target
        

        
