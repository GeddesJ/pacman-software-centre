'''
Created on 28Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import logging

class TabBar(QWidget):
    '''
    Tab bar widget which supports multiple orientations
    
    TODO: docs
    '''


    def __init__(self, parent):
        '''
        Constructor: TabBar(QWidget) => None
        '''
        
    def setOrientation(self, orientation):
        """
        Sets the orientation of the tab bar. Orientation is either Qt.Vertical
        or Qt. Horizontal
        
        setOrientation(self, Qt.orientation) => None
        """
        self._orientation = orientation
        
        #Test what orientation it is to determine which layout to use
        #TODO: Maybe this part should get a separate function?
        if orientation == Qt.Horizontal:
            logging.debug("Changed TabBar orientation to horizontal")
            self.setLayout(QHBoxLayout)
        elif orientation == Qt.Vertical:
            logging.debug("Changed TabBar orientation to vertical")
            self.setLayout(QVBoxLayout)
        else:
            logging.warning(
            "Invalid orientation specified to TabBar - {}".format(orientation))        
                
    def orientation(self):
        """
        Returns the current orientation of this tab bar.
        
        orientation() => Qt.orientation
        """
        return self._orientation
    
    
        