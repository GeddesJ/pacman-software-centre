'''
Created on 27Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QToolBar, QTabBar
from PyQt5.QtCore import Qt
from ui.TabBar import TabBar

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
        
        self._parent = parent
        
        self.setOrientation(Qt.Vertical) #Default orientation is vertical
        
        self._tabBar = NavigationTabs()
        
        self.addWidget(self._tabBar)
        
        self.orientationChanged.connect(self._tabBar.setOrientation)
        
        
class NavigationTabs(TabBar):
    """
    Tab bar containing the tabs which navigate between the sections in the
    application.
    
    TODO: docs
    """
    
    tabNames = ["Home", "Updates", "Installed", "AUR", "Operations", "Settings"]
    
    def __init__(self):
        "Constructor: NavigationTabs() => None"
        super().__init__()
        
        self.setOrientation(Qt.Vertical)
        
        for name in self.tabNames:
            self.addTab(title = name)
        
        
        
        