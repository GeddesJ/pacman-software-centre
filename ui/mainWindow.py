'''
Created on 23Jan.,2017

@author: jonathan
'''

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, qApp, QAction
from PyQt5.QtGui import QIcon
from util.constants import APPLICATION_NAME as APPNAME
from util.constants import KEYBOARD_SHORTCUTS, TOOLTIPS

def notImplemented():
    #FIXME: This function is temporary
    print("Not implemented yet")   

class mainWindow(QMainWindow):
    '''
    Object representing the root window for the application.
    TODO: docs
    '''

    def __init__(self):
        '''
        Constructor: mainWindow() => None
        '''
        super().__init__()
        
        #Set up menubar and actions
        self.menuStructure()        
        self._initMenuBar()
        
        #Window management
        self.resize(900, 610)
        self.centre()
        self.setWindowTitle(APPNAME)
        self.show()
        
    def menuStructure(self):
        """
        A function to keep everything neat. Just creates the dictionary
        containing a description of the elements which make up the menubar
        structure in the menubar.
        
        menuStructure() => None
        """
        self._menuStructure = [ #Stores all the menubar items
        ("&File", [
            ("&Check for Updates", TOOLTIPS["check updates"], notImplemented),
            ("&Apply Changes", TOOLTIPS["apply"], notImplemented),
            ("&Clear Selection", TOOLTIPS["clear"], notImplemented),
            ("&Exit", TOOLTIPS["quit"], qApp.quit)]),
        
        ("&View", [
            ("&Installed", TOOLTIPS["installed"], notImplemented),
            ("&Package Groups", TOOLTIPS["groups"], notImplemented)]),
        
        ("&Tools", [
            ("&Settings", TOOLTIPS["settings"], notImplemented)]),
                               
        ("&Help", [
            ("&Help", TOOLTIPS["help"], notImplemented),
            ("&Glossary", TOOLTIPS["glossary"], notImplemented),
            ("&About {}".format(APPNAME), TOOLTIPS["about"], notImplemented),
            ("&About Qt", TOOLTIPS["aboutqt"], notImplemented)]) 
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
        
        #Create menus and menubar objects
        for menuname, menuiteminfolist in self._menuStructure:
            menu = self.menubar.addMenu(menuname)
            self.menus.append(menu)
            self.menuObjects[menuname] = []
            
            for menuiteminfo in menuiteminfolist:
                menuaction = self._initMenuAction(menuiteminfo)
                self.menuObjects[menuname].append(menuaction)
                menu.addAction(menuaction)

        
    def _initMenuAction(self, menuinfo):
        """
        Generic function which will create a QAction object for all menubar
        actions, as well as setup keyboard shortcuts.
        The menuinfo input is a tuple featuring the item name, tooltip
        description and a function which will execute when the item is pressed.
        
        _initMenuAction( (str, str, func) ) => QAction
        """
        #Pull out data
        name, tooltip, action = menuinfo
        #Initialise QAction
        menuAction = QAction(QIcon(), name, self) #TODO: Sort out icons
        menuAction.setShortcut(KEYBOARD_SHORTCUTS.get(name, ""))
        menuAction.setStatusTip(tooltip)
        menuAction.triggered.connect(action)
        return menuAction

        
        