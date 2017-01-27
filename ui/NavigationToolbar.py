'''
Created on 27Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QToolBar, QTabBar, QWidget
from PyQt5.QtCore import Qt

class NavigationToolbar(QToolBar):
    '''
    Toolbar which holds a tabbed interface for switching between different
    sections in the app.
    
    TODO: docs
    '''
    
    def __init__(self, parent):
        '''
        Constructor: NavigationToolbar(MainWindow) => None
        '''
        super().__init__(parent)
        
        self.setOrientation(Qt.Vertical) #Default orientation is vertical
        
        self.addWidget(NavigationTabs())
        
        
class NavigationTabs(QTabBar):
    """
    Tab bar containing the tabs which navigate between the sections in the
    application.
    
    TODO: docs
    """
    
    tabNames = ["Home", "Updates", "Installed", "AUR", "Operations", "Settings"]
    
    def __init__(self):
        "Constructor: NavigationTabs() => None"
        super().__init__()
        
        self.setTabsClosable(False) #Tabs aren't closable
        self.setMovable(False) #Tabs aren't movable
        
        for name in self.tabNames:
            self.addTab(name)
        
        
        
        