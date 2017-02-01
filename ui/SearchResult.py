'''
Created on 1Feb.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class SearchResult(QWidget):
    '''
    Widget representing an individual search result. Contains options for 
    installation, status of package and possibly an icon.
    
    TODO: docs
    '''


    def __init__(self, name, icon, description, status, parent=None): #TODO: Not sure about status
        '''
        Constructor: SearchResult(str, QIcon, str, str, QWidget)
        '''
        super().__init__(parent)
        
        #Save off stuff for perhaps no reason
        self._name = name
        self._icon = icon
        self._description = description
        self._status = status
        
        self.setLayout(QHBoxLayout())
        self.setFixedHeight(150)
        
        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(icon.actualSize(QSize(32,32)))
        
        self.nameLabel = QLabel(name)
        
        self.statusLabel = QLabel(status)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SearchResult("Example", QIcon(), "This is a demo item", "installed")
    sys.exit(app.exec_())
        
        
        