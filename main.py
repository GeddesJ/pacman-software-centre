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
        self._actionmanager = ActionManager()
        
    def getActionManager(self):
        """
        Returns ActionManager instance
        
        getActionManager() => ActionManager
        """
        return self._actionmanager

if __name__ == '__main__':
    Qapp = QApplication(sys.argv)
    app = Application()
    ex = MainWindow(app)
    sys.exit(Qapp.exec_())