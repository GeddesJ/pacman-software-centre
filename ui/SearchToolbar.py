'''
Created on 25Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QPushButton, QLineEdit, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SearchToolbar(QToolBar):
    '''
    Object representing the toolbar containing the search box, 
    check for updates button and apply changes button
    
    TODO: docs
    '''


    def __init__(self, parent):
        '''
        Constructor: SearchToolbar(QWidget) => None
        '''
        super().__init__(parent)
        
        actionManager = parent.getApplication().getActionManager()
        #Add Check for Updates and Apply Buttons
        self.addAction(actionManager.getAction("check updates"))
        self.addAction(actionManager.getAction("apply"))
        self.addSeparator()
        self.addWidget(SearchWidget())
        
class SearchWidget(QLineEdit):
    """
    Object representing the package search box and associate functions to send
    off search requests.
    
    TODO: docs
    """
    
    def __init__(self):
        "Constructor: SearchWidget() => None"
        super().__init__()
        self.setPlaceholderText("Type to Search")
        self.setMinimumWidth(400)
        self.setAlignment(Qt.AlignCenter)
        
    