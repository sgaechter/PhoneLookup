#! /usr/bin/env python3

######################################################
# PhoneLookup CLI                                    #
#                                                    #
# v 0.1                                              #
######################################################

import urllib.request
import webbrowser
from tkinter import *
import sys


entry_text = sys.argv
entry = str(entry_text[1:])
url='https://tel.local.ch/'+entry
webbrowser.open_new(url)