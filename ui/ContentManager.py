'''
Created on 28Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QStackedWidget
from ui.pages import *
from ui.Page import Page #FIXME: Temp

class ContentManager(QStackedWidget):
    '''
    Manages switching between the different sections in the application.
    
    TODO: docs
    '''


    def __init__(self, parent=None):
        '''
        Constructor: ContentManager(QWidget) => None
        '''
        super().__init__(parent)
        self.setContentsMargins(10, 10, 10, 10)
        
        self.addWidget(Page())
        