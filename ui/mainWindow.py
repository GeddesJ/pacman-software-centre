'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, qApp
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from util.constants import APPLICATION_NAME as APPNAME
from util.constants import KEYBOARD_SHORTCUTS, TOOLTIPS, MENULABELS

def notImplemented():
    #FIXME: This function is temporary
    print("Not implemented yet")   

class mainWindow(QMainWindow):
    '''
    Object representing the root window for the application.
    TODO: docs
    '''

    _actions = { #FIXME: Is this the best way to do this?
        "quit": qApp.quit,
        "check updates": lambda: print("Checking for Updates :p"), #TODO: Make it actually check for updates
        "clear": notImplemented,
        "apply": notImplemented,
        "installed": notImplemented,
        "groups": notImplemented,
        "settings": notImplemented,
        "help": notImplemented,
        "glossary": notImplemented,
        "about": notImplemented,
        "aboutqt": notImplemented
        }

    def __init__(self):
        '''
        Constructor: mainWindow() => None
        '''
        super().__init__()
        
        #Set up menubar and actions
        
        self._initMenuBar()
        
        #Window management
        self.resize(900, 610)
        self.centre()
        self.setWindowTitle(APPNAME)
        self.show()
        
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
        self.menu = self.menuBar()
        self.menuStructure = {} #Stores the menu items
        #FIXME: Is there a better way to organize this?
        self._initMenuAction("File", "check updates")
        self._initMenuAction("File", "apply")
        self._initMenuAction("File", "clear")
        self._initMenuAction("File", "quit")
        
        self._initMenuAction("View", "installed")
        self._initMenuAction("View", "groups")
        
        self._initMenuAction("Tools", "settings")
        
        self._initMenuAction("Help", "help")
        self._initMenuAction("Help", "glossary")
        self._initMenuAction("Help", "about")
        self._initMenuAction("Help", "aboutqt")
        
        #Add file menu and items
        self.fileMenu = self.menu.addMenu('&File')
        self.fileMenu.addActions(self.menuStructure.get("File", []))
        
        #Add view menu and add items
        self.viewMenu = self.menu.addMenu('&View')
        self.viewMenu.addActions(self.menuStructure.get("View", []))

        #Add tools menu and items
        self.toolsMenu = self.menu.addMenu('&Tools')
        self.toolsMenu.addActions(self.menuStructure.get("Tools", []))
        
        #Add help menu and items
        self.helpMenu = self.menu.addMenu('&Help')
        self.helpMenu.addActions(self.menuStructure.get("Help", []))
        
    def _initMenuAction(self, menu, action):
        """
        Generic function which will create a QAction object for all menubar
        actions, as well as setup keyboard shortcuts.
        The menu input is a string which is the name of the menu the action
        is under.
        The action input is a string which refers to what the menu item does.
        
        _initMenuAction(str, str) => None
        """
        #Initialise QAction
        menuAction = QAction(QIcon(), MENULABELS[action], self) #TODO: Sort out icons
        menuAction.setShortcut(KEYBOARD_SHORTCUTS.get(action, ""))
        menuAction.setStatusTip(TOOLTIPS.get(action, ''))
        menuAction.triggered.connect(self._actions[action])
        
        #Add menuAction to menuStructure dictionary
        if self.menuStructure.get(menu):
            self.menuStructure[menu].append(menuAction)
        else:
            self.menuStructure[menu] = [menuAction]     
    
        
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())  
        
        