'''
Created on 28Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QWidget, QRadioButton, QBoxLayout
from PyQt5.QtCore import Qt
import logging


class TabBar(QWidget):
    '''
    Tab bar widget which supports multiple orientations

    TODO: docs
    '''

    def __init__(self, parent=None):
        '''
        Constructor: TabBar(QWidget) => None
        '''
        super().__init__(parent)
        
        self._orientation = Qt.Horizontal  # Default orientation is horizontal
        self.setLayout(QBoxLayout(QBoxLayout.LeftToRight, self))
        self._tabs = []

    def setOrientation(self, orientation):
        """
        Sets the orientation of the tab bar. Orientation is either Qt.Vertical
        or Qt. Horizontal

        setOrientation(self, Qt.orientation) => None
        """
        self._orientation = orientation

        # Test what orientation it is to determine which layout to use
        # TODO: Maybe this part should get a separate function?
        if orientation == Qt.Horizontal:
            logging.debug("Changed TabBar orientation to horizontal")
            self.layout().setDirection(QBoxLayout.LeftToRight)
        elif orientation == Qt.Vertical:
            logging.debug("Changed TabBar orientation to vertical")
            self.layout().setDirection(QBoxLayout.TopToBottom)
        else:
            logging.warning(
                "Invalid orientation specified to TabBar - {}".format(orientation))
            

    def orientation(self):
        """
        Returns the current orientation of this tab bar.

        orientation() => Qt.orientation
        """
        return self._orientation

    def addTab(self, **kwargs):
        """
        Appends a tab to the end of this tab bar. 
        Keyword arguments are as follows:
        title - string - The title of the tab to be displayed
        icon - QIcon - An icon to display for this tab
        view - QWidget - The widget to display on the content manager when this
                        tab is selected.

        addTab({name:str, icon:QIcon, view:QWidget}) => None
        """
        title = kwargs.get("title", "")
        icon = kwargs.get("icon")
        view = kwargs.get("view")
        
        #TODO: Deal with icon and view
        newTab = Tab(title)
        self._tabs.append(newTab)
        self.layout().addWidget(newTab)

    def insertTab(self, index, **kwargs):
        """
        Inserts a tab to this tab bar at the index specified.
        Keyword arguments are as follows:
        title - string - The title of the tab to be displayed
        icon - QIcon - An icon to display for this tab
        view - QWidget - The widget to display on the content manager when this
                        tab is selected.

        insertTab(int, {name:str, icon:QIcon, view:QWidget}) => None
        """
        title = kwargs.get("title", "")
        icon = kwargs.get("icon")
        view = kwargs.get("view")
        
        #TODO: Deal with icon and view
        newTab = Tab(title)
        self._tabs.insert(index, newTab)
        self.layout().insertWidget(index, newTab)

    def removeTab(self, index=-1):
        """
        Removes the tab at the index provided. If no index is provided removes 
        the last tab.

        removeTab(int) => None
        """
        removedTab = self._tabs.pop(index)
        self.layout().removeWidget(removedTab)
        
class Tab(QRadioButton):
    """
    Object representing an individual tab widget for TabBar
    
    TODO: docs
    """
    
    def __init__(self, text=None, parent=None, icon=None):
        "Constructor: Tab(str, QWidget, QIcon) => None"
        super().__init__(parent)
        
        if text:
            self.setText(text)
        
        if icon:
            self.setIcon(icon)
    
    
