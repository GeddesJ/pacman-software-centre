'''
Created on 28Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

class Page(QFrame):
    '''
    A widget which represents a page - a widget which will contain other widgets
    '''


    def __init__(self, parent=None):
        '''
        Constructor: Page(QWidget) => None
        '''
        super().__init__(parent)
        
        self.setMinimumSize(480, 300)
        # Set look of frame border
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
        # Set colour of frame
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setBrush(p.Background, p.dark())
        self.setPalette(p)
        
        
        