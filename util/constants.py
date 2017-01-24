'''
Created on 23Jan.,2017

@author: jonathan
'''

#General
APPLICATION_NAME = "Need a name" #TODO: Find name
VERSION = "0.0.1"

#Application Keyboard Shortcuts - FIXME: This should be stored and managed from a config file
KEYBOARD_SHORTCUTS = {
    "quit": "Ctrl+Q",
    "check updates": "Ctrl+U",
    "help": "F1",
    "settings": "Ctrl+P",
    "apply": "Ctrl+I",
    "undo": "Ctrl+Z",
    "redo": "Ctrl+Shift+Z",
    "clear": "Ctrl+R"
    }

#Application Tool-tips
TOOLTIPS = {
    "quit": "Exit Application",
    "check updates": "Checks for system and application updates",
    "clear": "Clears the pending installation/removal operations",
    "help": "Shows help documentation",
    "glossary": "Shows a glossary of common Linux terms",
    "about": "Shows information about this application",
    "aboutqt": "Shows information about Qt",
    "settings": "Opens application settings",
    "apply": "Installs or removes selected applications or packages",
    "installed": "Shows a list of installed applications and packages on this system",
    "groups": "Shows a list of install groups to install software from"
    }

#Menu Labels
MENULABELS = {
    "quit": "&Exit",
    "check updates": "&Check for Updates",
    "clear": "&Clear Selection",
    "help": "&Help",
    "glossary": "&Glossary",
    "about": "&About {}".format(APPLICATION_NAME),
    "aboutqt": "&About Qt",
    "settings": "&Settings",
    "apply": "&Apply Changes",
    "installed": "&Installed",
    "groups": "&Package Groups"
    }