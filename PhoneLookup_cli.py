#! /usr/bin/env python3

######################################################
# PhoneLookup CLI                                    #
#                                                    #
# v 0.1                                              #
######################################################

import urllib.request
from unidecode import unidecode
import webbrowser
from tkinter import *
import sys


entry_text = sys.argv
entry = str(entry_text[1:])
url=url=f'https://www.local.ch/de/s/Switzerland/{unidecode(entry)}'
webbrowser.open_new(url)