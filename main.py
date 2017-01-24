'''
Created on 23Jan.,2017

@author: jonathan
'''

import sys
from PyQt5.QtWidgets import QApplication
from ui.mainWindow import mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())