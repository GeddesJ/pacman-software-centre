'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, qApp
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from util.constants import APPLICATION_NAME as APPNAME
from util.constants import KEYBOARD_SHORTCUTS
from util.constants import TOOLTIPS

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
        self._initExitAction()
        self._initUpdatesAction()
        
        #Add file menu and items
        self.fileMenu = self.menu.addMenu('&File')
        self.fileMenu.addAction(self._updatesAction)
        self.fileMenu.addAction(self._exitAction)
        
        #Add view menu and add items
        self.viewMenu = self.menu.addMenu('&View')
        
        
        #Add tools menu and items
        self.toolsMenu = self.menu.addMenu('&Tools')
        
        #Add help menu and items
        self.helpMenu = self.menu.addMenu('&Help')
        
    def _initExitAction(self):
        """
        Initialises the application exit action and associated 
        keyboard shortcut.
        
        _initExitAction() => None
        """
        self._exitAction = QAction(QIcon(), '&Exit', self) #TODO: Need an icon
        self._exitAction.setShortcut(KEYBOARD_SHORTCUTS["quit"])
        self._exitAction.setStatusTip(TOOLTIPS["quit"])
        #Attaches action to the application quit when triggered
        self._exitAction.triggered.connect(qApp.quit) 
        #self.statusBar() #Don't know if I want this yet
        
    def _initUpdatesAction(self):
        """
        Initialises the application 'check for updates' action and associated 
        keyboard shortcut.
        
        _initUpdatesAction() => None
        """
        self._updatesAction = QAction(QIcon(), 'Check for Updates', self) #TODO: Need an icon
        self._updatesAction.setShortcut(KEYBOARD_SHORTCUTS["check updates"])
        self._updatesAction.setStatusTip(TOOLTIPS["check updates"])
        #TODO: This needs to actually check for updates
        
    
        
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())  
        
        