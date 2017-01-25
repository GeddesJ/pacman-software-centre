'''
Created on 23Jan.,2017

@author: jonathan
'''

from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, qApp, QAction, 
                             QToolBar)
from PyQt5.QtGui import QIcon
from util.constants import APPLICATION_NAME as APPNAME
from util.constants import KEYBOARD_SHORTCUTS, TOOLTIPS
from ui.SearchToolbar import SearchToolbar

class MainWindow(QMainWindow):
    '''
    Object representing the root window for the application.
    TODO: docs
    '''

    def __init__(self, app):
        '''
        Constructor: MainWindow(Application) => None
        '''
        super().__init__()
        
        #Store a reference to the application object
        self._application = app
               
        #Set up menubar and actions
        self.menuStructure()        
        self._initMenuBar()
        
        #Set up search toolbar
        #self.searchToolbar = QToolBar()
        #self.searchToolbar.addWidget(SearchToolbar())
        #self.addToolBar(self.searchToolbar)
        
        #Window management
        self.resize(900, 610)
        self.centre()
        self.setWindowTitle(APPNAME)
        self.show()
        
    def menuStructure(self):
        """
        A function to keep everything neat. Just creates the list
        containing a description of the elements which make up the menubar
        structure in the menubar.
        
        menuStructure() => None
        """
        self._menuStructure = [ #Stores all the menubar items
        ("&File", [
            ("check updates", "&Check for Updates"),
            ("apply", "&Apply Changes"),
            ("clear", "&Clear Selection"),
            ("exit", "&Exit")]),
        
        ("&View", [
            ("installed", "&Installed"),
            ("groups", "&Package Groups")]),
        
        ("&Tools", [
            ("settings", "&Settings")]),
                               
        ("&Help", [
            ("help", "&Help"),
            ("glossary", "&Glossary"),
            ("about", "&About {}".format(APPNAME)),
            ("aboutqt", "&About Qt")]) 
        ]
        
    def centre(self):
        """
        Centres the window in the screen.
        
        centre() => None
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def _initMenuBar(self):
        """
        Initialises the application menubar.
        
        initMenuBar() => None
        """
        #Initialise menubar and actions
        self.menubar = self.menuBar()
        self.menuObjects = {} #Stores the menubar items
        self.menus = [] #Stores parent menus
        actionmanager = self._application.getActionManager()
        
        #Create menus and menubar objects
        for menuname, menuiteminfolist in self._menuStructure:
            menu = self.menubar.addMenu(menuname)
            self.menus.append(menu)
            self.menuObjects[menuname] = []
            
            for menuiteminfo in menuiteminfolist:
                keyword, name = menuiteminfo
                actionmanager.initialiseAction(keyword, self, title=name)
                newaction = actionmanager.getAction(keyword)
                menu.addAction(newaction)
                

    
    def _initSearchToolbar(self):
        """
        
        """

        
        