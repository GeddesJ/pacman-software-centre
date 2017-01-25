'''
Created on 25Jan.,2017

@author: jonathan
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SearchToolbar(QWidget):
    '''
    Object representing the toolbar containing the search box, 
    check for updates button and apply changes button
    
    TODO: docs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
        #Create Buttons
        
        #Check for updates button
        self._checkUpdatesBtn = QPushButton("Check for Updates")
        self._checkUpdatesBtn.setIcon(QIcon("refresh.png"))
        
        #Apply changes button
        self._applyBtn = QPushButton("Apply Changes")
        self._applyBtn.setIcon(QIcon("tick.png"))
        
        #Search box
        self._searchBox = QLineEdit()
        self._searchBox.setPlaceholderText("Type to Search")
        self._searchBox.setMinimumWidth(400)
        self._searchBox.setAlignment(Qt.AlignCenter)
        
        #Setup Layout Manager
        layout = QHBoxLayout()
        layout.addWidget(self._checkUpdatesBtn)
        layout.addWidget(self._applyBtn)
        layout.addStretch(1)
        layout.addWidget(self._searchBox)
        layout.addStretch(1)
        self.setLayout(layout)
        
        self.resize(900, 50) #FIXME: This is just for testing purposes
        self.show()
        
class SearchBox(QWidget):
    """
    Object representing the package search box and associate functions to send
    off search requests.
    
    TODO: docs
    """
    
class CheckUpdatesBtn(QPushButton):
    """
    A Q___ which when clicked will check for package updates
    
    TODO: docs
    """
    
    def __init__(self, title, parent):
        "Constructor: CheckUpdatesBtn() => None"
        super().__init__(title, parent)
        
        
        
    
class ApplyBtn(QPushButton):
    """
    A Q___ which when clicked will begin the process of applying package and
    application changes the user has queued. 
    
    TODO: docs
    """
        
if __name__ == "__main__":
    #FIXME: This is temporary
    app = QApplication(sys.argv)
    ex = SearchToolbar()
    sys.exit(app.exec_())