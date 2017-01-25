'''
Created on 25Jan.,2017

@author: jonathan
'''
from PyQt5.QtWidgets import QAction
from util.constants import TOOLTIPS, KEYBOARD_SHORTCUTS

class ActionManager(object):
    """
    Manages the creation and storage of all QActions
    
    TODO: docs
    """
    
    def __init__(self):
        "Constructor: ActionManager() => None"
        self._actions = {}
        
    def initialiseAction(self, keyword, parent, **kwargs):
        """
        Takes keyword arguments and initialises a QAction object based on the
        parameters. The parameters are as follows:
        keyword - a string which will map to the QAction object in the
                    dictionary. REQUIRED
        parent - a QWidget which this action will be effective for. REQUIRED
        title - a string which will be the title of the QAction in menus or on
                buttons. If this isn't specified, the keyword will be used as
                the title.
        icon - a QIcon for any icons to be associated with this action.
        tooltip - a string which is the description of what the QAction does.
                    If this is not specified then the function will look at the
                    TOOLTIPS variable in constants.py, and if there is nothing
                    there the QAction object will be initialised with no 
                    tooltip.
        shortcut - a string which represents a keyboard shortcut to activate
                    this QAction. If this isn't specified, the shortcut will be
                    searched in the KEYBOARD_SHORTCUTS constant. The shortcut 
                    will be set to nothing if no shortcuts are found or
                    specified.
        action - a function which is triggered when the QAction is triggered.
                This is set to the notImplemented function of this class if no
                function is specified. Functions can be added after the fact by
                using the bind function of this class.
                
        When QAction object is initialised, it is stored in a dictionary within
        this object.
                
        initialiseAction(str, {title: str, tooltip: str, shortcut: str, 
                                action: function}) => None
        """
        #Extract info
        title = kwargs.get("title", keyword)
        icon = kwargs.get("icon", None)
        tooltip = kwargs.get("tooltip", TOOLTIPS.get(keyword, ""))
        shortcut = kwargs.get("shortcut", KEYBOARD_SHORTCUTS.get(keyword, ""))
        action = kwargs.get("action", self.notImplemented)
        
        #Initialise QAction
        if icon is None:
            newAction = QAction(title, parent)
        else:
            newAction = QAction(icon, title, parent)
            
        newAction.setShortcut(shortcut)
        newAction.setStatusTip(tooltip)
        newAction.triggered.connect(action)
        
        #Add to ActionManager
        self._actions[keyword] = newAction
        
    def getAction(self, keyword):
        """
        Returns the QAction object associated with the keyword.
        
        getAction(str) => QAction
        """
        return self._actions.get(keyword)
        
    def bind(self, keyword, function):
        """
        Connects the action returned by the keyword to the function input
        Precondition: QActions must have been initialised and keyword has to map
        to an QAction
        
        bind(str, func) => None
        """
        self.getAction(keyword).triggered.connect(function)
        
    def notImplemented(self):
        "Runs if an action has no associated function."
        print("Not Implemented")