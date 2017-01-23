'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon
from util.constants import APPLICATION_NAME as APPNAME

class mainWindow(QWidget):
    '''
    Object representing the root window for the application.
    TODO: docs
    '''


    def __init__(self):
        '''
        Constructor: mainWindow() => None
        '''
        super().__init__()
        
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
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())  
        
        