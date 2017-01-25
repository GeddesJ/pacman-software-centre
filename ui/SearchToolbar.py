'''
Created on 25Jan.,2017

@author: jonathan
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication

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
        
class SearchBox():
    """
    Object representing the package search box and associate functions to send
    off search requests.
    
    TODO: docs
    """
    
class CheckUpdatesBtn():
    """
    A Q___ which when clicked will check for package updates
    
    TODO: docs
    """
    
class ApplyBtn():
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