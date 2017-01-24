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
        self._initExitAction()
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
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu('&File')
        self.fileMenu.addAction(self._exitAction)
        
    def _initExitAction(self):
        """
        Initialises the application exit action and keyboard shortcut
        associated with the action.
        
        initExitAction
        """
        self._exitAction = QAction(QIcon(), '&Exit', self) #TODO: Need an icon
        self._exitAction.setShortcut(KEYBOARD_SHORTCUTS["quit"])
        self._exitAction.setStatusTip("Exit Application")
        #Attaches action to the application quit when triggered
        self._exitAction.triggered.connect(qApp.quit) 
        #self.statusBar() #Don't know if I want this yet
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())  
        
        