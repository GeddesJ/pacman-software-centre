'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys, logging
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow
from model.actionmanager import ActionManager
from util.constants import LOGLEVEL, LOGPATH

class Application(QApplication):
    """
    The root application object. Responsible for passing global application
    objects around to the sub objects.
    
    TODO: docs
    """
    
    def __init__(self, argv):
        "Constructor: Application() => None"
        super().__init__(argv)
        
        #Set up logging
        logging.basicConfig(filename=LOGPATH, level=LOGLEVEL,
                format="%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        logging.info("Application Startup")
        
        #Initialise ActionManager and UI
        self._actionManager = ActionManager()
        logging.debug("Action Manager Initialised")
        self._userInterface = MainWindow(self)
        logging.debug("User Interface Initialised")
        
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
        self.getActionManager().bind("quit", self.quit)
        #About Qt
        self.getActionManager().bind("aboutqt", self.aboutQt)
        
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
    
    def quit(self, *args, **kwargs):
        """
        Override QApplication.quit(). Exits the application.
        """
        logging.info("Application Termination \n")
        super().quit(args, kwargs)

if __name__ == '__main__':
    app = Application(sys.argv)
    ex = app.getUserInterface()
    sys.exit(app.exec_())
    
    
    