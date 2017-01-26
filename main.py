'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from model.actionmanager import ActionManager

class Application(object):
    """
    TODO: decide how this will be arranged and what this is for
    """
    
    def __init__(self):
        "Constructor: Application() => None"
        self._actionManager = ActionManager()
        self._userInterface = MainWindow(self)
        
        #Bind actions
        self.bindActions()
        
    def bindActions(self):
        """
        Binds all actions to the functions which will trigger when the actions
        are triggered.
        
        TODO: Is this the best way/place for this?
        
        bindActions() => None
        """
        #Quit
        self.getActionManager().bind("quit", QApplication.quit)
        #About Qt
        self.getActionManager().bind("aboutqt", QApplication.aboutQt)
        
    def getActionManager(self):
        """
        Returns ActionManager instance
        
        getActionManager() => ActionManager
        """
        return self._actionManager
    
    def getUserInterface(self):
        """
        (For Now at least) Returns the MainWindow object which forms the user
        interface.
        
        getUserInterface() => MainWindow
        """
        return self._userInterface

if __name__ == '__main__':
    Qapp = QApplication(sys.argv)
    app = Application()
    ex = app.getUserInterface()
    sys.exit(Qapp.exec_())