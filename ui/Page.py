'''
Created on 28Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class Page(QWidget):
    '''
    A widget which represents a page - a widget which will contain other widgets
    '''


    def __init__(self, parent=None):
        '''
        Constructor: Page(QWidget) => None
        '''
        super().__init__(parent)
        
        self.setMinimumSize(400, 400)
        #FIXME: Temp
        self.setAutoFillBackground(True)
        pallete = self.palette()
        pallete.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(pallete)