'''
Created on 25Jan.,2017

@author: jonathan
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QHBoxLayout, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SearchToolbar(QToolBar):
    '''
    Object representing the toolbar containing the search box, 
    check for updates button and apply changes button
    
    TODO: docs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super().__init__(parent)
        
        #Add Check for Updates and Apply Buttons
        self.addAction()
        
class SearchBox(QLineEdit):
    """
    Object representing the package search box and associate functions to send
    off search requests.
    
    TODO: docs
    """
    
    def __init__(self):
        "Constructor: SearchBox() => None"
        super().__init__()
        self.setPlaceholderText("Type to Search")
        self.setMinimumWidth(400)
        self.setAlignment(Qt.AlignCenter)
    
    
class CheckUpdatesBtn(QPushButton):
    """
    A Q___ which when clicked will check for package updates
    
    TODO: docs
    """
    
    def __init__(self):
        "Constructor: CheckUpdatesBtn() => None"
        super().__init__("Check for Updates")
        self.setIcon(QIcon("refresh.png")) #FIXME: This needs to be changed when we deal with icons
        
            
class ApplyBtn(QPushButton):
    """
    A Q___ which when clicked will begin the process of applying package and
    application changes the user has queued. 
    
    TODO: docs
    """
    
    def __init__(self):
        "Constructor: ApplyBtn => None"
        super().__init__("Apply Changes")
        self.setIcon(QIcon("tick.png")) #FIXME: This needs to be changed when we deal with icons
        
if __name__ == "__main__":
    #FIXME: This is temporary
    app = QApplication(sys.argv)
    ex = SearchToolbar()
    sys.exit(app.exec_())